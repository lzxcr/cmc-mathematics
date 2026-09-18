#!/usr/bin/env python3
"""Strict, local Markdown/LaTeX reader for the book's deliberately small syntax."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
TOKEN = re.compile(r"`[^`\n]*`|(?<!\\)\\\[.*?(?<!\\)\\\]|(?<!\\)\$(?:\\.|[^$\\])*?\$", re.S)
ESCAPES = dict(zip("\\{}$&#%_^~", [r"\textbackslash{}", r"\{", r"\}", r"\$", r"\&", r"\#", r"\%", r"\_", r"\textasciicircum{}", r"\textasciitilde{}"] ))
SYMBOLS = {"→": r"\to", "⇒": r"\Rightarrow", "⇔": r"\Leftrightarrow", "∞": r"\infty", "≥": r"\ge", "≤": r"\le", "∈": r"\in", "⊆": r"\subseteq", "×": r"\times", "α": r"\alpha", "β": r"\beta", "ε": r"\varepsilon", "δ": r"\delta", "Σ": r"\Sigma", "ℝ": r"\mathbb{R}", "ℂ": r"\mathbb{C}", "ℚ": r"\mathbb{Q}"}


def math_spans(text: str):
    for match in TOKEN.finditer(text):
        value = match[0]
        if value.startswith("`"):
            continue
        display = value.startswith(r"\[")
        yield match.start(), match.end(), value[2:-2] if display else value[1:-1], display


def prose_without_tokens(text: str) -> str:
    return TOKEN.sub(lambda m: "\n" * m[0].count("\n"), text)


def escape(text: str) -> str:
    return "".join(ESCAPES.get(c, c) for c in text)


ANCHOR = r'[a-zA-Z][a-zA-Z0-9:-]*'
HEADING = re.compile(r'^(#{1,3}) (.+?)(?: \{#(' + ANCHOR + r')\})?\s*$', re.M)
INTERNAL_LINK = re.compile(r'\[([^]\n]+)\]\(#(' + ANCHOR + r')\)')


def inline(text: str, targets: set[str] | dict[str, str] | None = None) -> str:
    """Protect code and mathematics before processing emphasis or escaping prose."""
    vault: list[str] = []
    def keep(value: str) -> str:
        vault.append(value)
        return f"\x00{len(vault)-1}\x00"
    def token(m):
        value = m[0]
        return keep(r"\texttt{" + escape(value[1:-1]) + "}" if value.startswith("`") else value)
    text = TOKEN.sub(token, text)
    def internal(m):
        label = escape(m[1])
        if isinstance(targets, dict) and targets.get(m[2]):
            return keep(r'\href{' + escape(targets[m[2]] + '#' + m[2]) + '}{' + label + '}')
        return keep(r'\hyperref[' + m[2] + ']{' + label + '}'
                    if targets is None or m[2] in targets else label)
    text = INTERNAL_LINK.sub(internal, text)
    text = re.sub(r"\[([^]\n]+)\]\((https?://[^)\s]+)\)", lambda m: keep(r"\href{" + escape(m[2]) + "}{" + escape(m[1]) + "}"), text)
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: keep(r"\textbf{" + escape(m[1]) + "}"), text)
    text = "".join("$" + SYMBOLS[c] + "$" if c in SYMBOLS else ESCAPES.get(c, c) for c in text)
    # Nested protected fragments (e.g. mathematics inside bold text) resolve too.
    for _ in range(len(vault) + 1):
        if not re.search(r"\x00\d+\x00", text):
            break
        text = re.sub(r"\x00(\d+)\x00", lambda m: vault[int(m[1])], text)
    return text


def render(body: str, targets: set[str] | dict[str, str] | None = None) -> str:
    """Render paragraphs; mathematical commands and grouping stay byte-for-byte intact."""
    rendered = []
    for paragraph in re.split(r"\n\s*\n", body.strip()):
        if not paragraph.strip():
            continue
        if paragraph.startswith("> "):
            paragraph = re.sub(r"^> ?", "", paragraph, flags=re.M)
            rendered.append(r"\begin{quote}\small " + inline(paragraph, targets) + r"\end{quote}")
        else:
            rendered.append(inline(paragraph, targets))
    return "\n\n".join(rendered)


PROBLEM_HEAD = re.compile(r"^# (题目|解答|评注)\s*$", re.M)
PROBLEM_ID = re.compile(r"[a-zA-Z0-9-]+:[1-9]\d*\Z")


def load_problem(path: Path) -> dict[str, str]:
    """Read one canonical problem without rewriting any mathematical content."""
    text = path.read_text(encoding="utf-8")
    marks = list(PROBLEM_HEAD.finditer(text))
    if not marks or text[:marks[0].start()].strip():
        raise ValueError(f"{path}: 单题文件必须从题目块开始")
    blocks: dict[str, str] = {}
    for i, mark in enumerate(marks):
        kind = mark[1]
        if kind in blocks:
            raise ValueError(f"{path}: 重复的{kind}块")
        body = text[mark.end():marks[i + 1].start() if i + 1 < len(marks) else len(text)].strip()
        if re.search(r"^# ", body, re.M):
            raise ValueError(f"{path}: 未识别的块标题；允许题目、解答、评注")
        if not body:
            raise ValueError(f"{path}: 空白{kind}")
        blocks[kind] = body
    if list(blocks) not in [["题目", "解答"], ["题目", "解答", "评注"]]:
        raise ValueError(f"{path}: 单题须按题目、解答、可选评注的顺序配对")
    return blocks


def _json_object(path: Path) -> dict:
    import json
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: 无法读取 JSON：{error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path}: JSON 顶层必须为对象")
    return value


def _local_path(base: Path, value: str, label: str) -> Path:
    """Resolve catalog paths within their own source tree, never outside it."""
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError(f"{label}: 需要非空相对路径")
    result = (base / value).resolve()
    if not result.is_relative_to(base.resolve()):
        raise ValueError(f"{label}: 路径越出源目录")
    return result


def load_book(path: Path | None = None) -> dict:
    """Expand src/book.json into parts, chapters and canonical problem items.

    Item ``id`` is permanent provenance; ``number`` is the current consecutive
    chapter position. ``path`` and ``index_path`` are absolute Paths. Block bodies
    stay byte-for-byte equal to the Markdown reader's stripped input. Source
    metadata is returned as ``sources``; it is never mixed into rendered prose.
    """
    catalog_path = (path or ROOT / "src/book.json").resolve()
    base = catalog_path.parent
    book = _json_object(catalog_path)
    if book.get("schema") != 1:
        raise ValueError(f"{catalog_path}: 不支持的目录 schema")
    if not isinstance(book.get("parts"), list):
        raise ValueError(f"{catalog_path}: 缺少 parts 列表")
    sources_path = _local_path(base, book.get("sources", "sources.json"), "sources")
    book["sources"] = _json_object(sources_path)
    book["sources_path"] = sources_path
    book["path"] = catalog_path
    for part in book["parts"]:
        if not isinstance(part, dict) or not isinstance(part.get("chapters"), list):
            raise ValueError("分部必须为包含 chapters 列表的对象")
        for chapter in part["chapters"]:
            if not isinstance(chapter, dict):
                raise ValueError("章目录必须为对象")
            index_path = _local_path(base, chapter.get("index"), "chapter.index")
            index = _json_object(index_path)
            if not isinstance(index.get("notes"), list) or not isinstance(index.get("items"), list):
                raise ValueError(f"{index_path}: 需要 notes 和 items 列表")
            chapter["index_path"] = index_path
            chapter["notes"] = index["notes"]
            chapter["items"] = index["items"]
            for number, item in enumerate(chapter["items"], 1):
                if not isinstance(item, dict):
                    raise ValueError(f"{index_path}: item 必须为对象")
                value = item.get("file")
                if not isinstance(value, str) or Path(value).name != value or not value.endswith(".md"):
                    raise ValueError(f"{index_path}: 单题 file 必须为同目录下的 Markdown 文件名")
                item_path = _local_path(index_path.parent, value, "item.file")
                item["path"] = item_path
                item["number"] = number
                item["blocks"] = load_problem(item_path)
    return book


def iter_problems(book: dict):
    """Yield (part, chapter, item) in the book's display order."""
    for part in book["parts"]:
        for chapter in part["chapters"]:
            for item in chapter["items"]:
                yield part, chapter, item


def load_methods(path: Path | None = None) -> dict:
    catalog = (path or ROOT/'src/methods/book.json').resolve()
    book = _json_object(catalog)
    if type(book.get('schema')) is not int or book['schema'] != 1:
        raise ValueError(f'{catalog}: 不支持的目录 schema')
    if not isinstance(book.get('parts'), list):
        raise ValueError(f'{catalog}: 缺少 parts 列表')
    book['path'] = catalog
    paths = set()
    ids = set()
    for part in book['parts']:
        if not isinstance(part, dict) or not isinstance(part.get('chapters'), list):
            raise ValueError('方法卷分部必须为包含 chapters 列表的对象')
        for chapter in part['chapters']:
            if not isinstance(chapter, dict) or any(
                not isinstance(chapter.get(key), str) or not chapter[key].strip()
                for key in ('id', 'title', 'file')
            ):
                raise ValueError('方法卷章目录需要非空 id、title 和 file')
            chapter['path'] = _local_path(catalog.parent, chapter['file'], 'methods.file')
            if chapter['path'] in paths or chapter['id'] in ids:
                raise ValueError('方法卷章目录重复')
            headings = [h for h in HEADING.finditer(chapter['path'].read_text()) if h[1] == '#']
            if len(headings) != 1:
                raise ValueError(f"{chapter['path']}: 方法章必须恰有一个一级标题")
            if headings[0][2] != chapter['title']:
                raise ValueError(f"{chapter['path']}: 一级标题与目录 title 不一致")
            paths.add(chapter['path'])
            ids.add(chapter['id'])
    actual = {p.resolve() for folder in ('inner', 'outer') for p in (catalog.parent/folder).glob('*.md')}
    if actual != paths:
        raise ValueError('方法卷目录与章文件不一致：' + ', '.join(str(p) for p in actual ^ paths))
    return book


def method_texts(book: dict | None = None) -> list[tuple[str, str]]:
    book = book or load_methods()
    paths = [book['path'].parent/'frontmatter.md']
    paths += [c['path'] for p in book['parts'] for c in p['chapters']]
    return [(str(p.relative_to(ROOT)), p.read_text()) for p in paths]
