"""Regressions for exact mathematics, canonical provenance and split TeX output."""
import copy
import json
import tempfile
from pathlib import Path
import unittest

from booklib import inline, load_book, load_methods, load_problem, math_spans, render
from check_sources import catalog_issues, check_sources, link_issues, math_issues
from verify_book import read_tex_tree, verify
from build_book import build, markdown_chapter
from clean import clean_build


PROBLEM = '# 题目\n\n证明 $1+1=2$。\n\n# 解答\n\n由整数加法定义即得。\n'


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def source_metadata(numbers):
    return dict(title='来源标题', problem_numbers=numbers)


def fixture(root, finals=False):
    part = 'finals' if finals else 'preliminary'
    edition = 13 if finals else 11
    paper = 'fin13-high' if finals else 'ch10-11th-A'
    directory = root/'problems'/part/f'{edition:02d}'
    directory.mkdir(parents=True)
    (directory/'01.md').write_text(PROBLEM)
    item = dict(id=f'{paper}:1', file='01.md', audience='high' if finals else 'all', origins=[dict(paper=paper, number=1)])
    write_json(directory/'index.json', dict(notes=[], items=[item]))
    chapter = dict(id=f'{part}-{edition:02d}', edition=edition, year=2022 if finals else 2019, title='章标题', index=str((directory/'index.json').relative_to(root)))
    book = dict(schema=1, sources='sources.json', parts=[dict(id='preliminary',title='初赛',chapters=[]),dict(id='finals',title='决赛',chapters=[])])
    book['parts'][int(finals)]['chapters'].append(chapter)
    write_json(root/'book.json', book)
    write_json(root/'sources.json', {paper:source_metadata([1])})
    (root/'frontmatter.md').write_text('# 序言\n\n阅读正文。\n')
    return root/'book.json'


class PipelineTests(unittest.TestCase):
    def test_formula_is_not_rewritten(self):
        formula = r"\[\begin{pmatrix}1 & \sqrt[3]{2}\\[2pt]0 & \{a\}\end{pmatrix}\]"
        self.assertEqual(render(formula), formula)
        self.assertEqual(len(list(math_spans(formula))), 1)

    def test_code_does_not_open_math(self):
        text = r"原文 `$\begin{array}{cc}`，应为 $A$。"
        self.assertEqual(len(list(math_spans(text))), 1)
        self.assertEqual(math_issues(text), [])
        self.assertIn(r"\textbackslash{}begin", inline(text))

    def test_nested_emphasis_keeps_math(self):
        self.assertEqual(inline(r"**取 $\{x\}$**。"), r"\textbf{取 $\{x\}$}。")

    def test_internal_links_preserve_math_and_excerpt_text(self):
        text = r'[算子 $T$](#app:linear-cyclic)'
        self.assertEqual(inline(text), r'\hyperref[app:linear-cyclic]{算子 $T$}')
        self.assertEqual(inline(text, set()), r'算子 $T$')
        self.assertEqual(inline(text, {'app:linear-cyclic':'methods.pdf'}),
                         r'\href{methods.pdf\#app:linear-cyclic}{算子 $T$}')

    def test_heading_anchors_and_link_integrity(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'methods.md'
            text = '# 理论 {#app:theory}\n\n## 算子 $T$ {#app:operator}\n\n[正文](#pr:test:1)\n'
            path.write_text(text)
            result = markdown_chapter(path)
            self.assertIn(r'\section{算子 $T$}', result)
            self.assertIn(r'\label{app:operator}', result)
            self.assertEqual(link_issues([(str(path), text)], {'pr:test:1'}), [])
            self.assertTrue(any('缺少内部链接目标' in e for e in link_issues([(str(path), text)], set())))
            self.assertTrue(any('重复锚点' in e for e in link_issues([('a',text),('b',text)], {'pr:test:1'})))

    def test_malformed_math_fails(self):
        for text in [r"$x", r"\[x", r"$\frac{1}{2$", r"$\begin{pmatrix}1\end{bmatrix}$", r"$\int_\mathbb R f$"]:
            self.assertTrue(math_issues(text), text)

    def test_one_problem_requires_ordered_unique_pair(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'problem.md'
            for text in [PROBLEM+'\n# 题目\n另一题\n', '# 解答\n答案\n# 题目\n问题\n', '# 题目\n问题\n', PROBLEM+'\n# 扩展\n旧标题\n']:
                path.write_text(text)
                with self.assertRaises(ValueError):
                    load_problem(path)
            body = r'\[\frac{1}{2}=0.5\]'
            path.write_text(PROBLEM+'\n# 评注\n\n'+body+'\n')
            self.assertEqual(load_problem(path)['评注'], body)

    def test_catalog_expands_stable_id_and_display_number(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = fixture(Path(directory))
            book = load_book(catalog)
            item = book['parts'][0]['chapters'][0]['items'][0]
            self.assertEqual(item['id'], 'ch10-11th-A:1')
            self.assertEqual(item['number'], 1)
            self.assertTrue(item['path'].is_absolute())
            self.assertEqual(item['blocks'], load_problem(item['path']))
            self.assertEqual(catalog_issues(book), [])

    def test_methods_catalog_rejects_schema_and_rendered_title_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            chapter_path = root/'inner'/'theory.md'
            chapter_path.parent.mkdir()
            valid_text = '# 理论 {#app:theory}\n\n## 工具\n\n正文。\n'
            chapter_path.write_text(valid_text)
            data = dict(schema=1, parts=[dict(id='inner', title='内篇', chapters=[
                dict(id='inner-theory', title='理论', file='inner/theory.md')])])
            catalog = root/'book.json'
            write_json(catalog, data)
            self.assertEqual(load_methods(catalog)['parts'][0]['chapters'][0]['title'], '理论')
            for text, message in [
                (valid_text.replace('# 理论 ', '# 另一标题 '), '一级标题与目录 title 不一致'),
                (valid_text+'\n# 第二章\n', '恰有一个一级标题'),
                ('## 只有节标题\n', '恰有一个一级标题'),
            ]:
                with self.subTest(text=text):
                    chapter_path.write_text(text)
                    with self.assertRaisesRegex(ValueError, message):
                        load_methods(catalog)
            chapter_path.write_text(valid_text)
            for key, value in [('schema', 2), ('parts', {}), ('parts', [None])]:
                with self.subTest(key=key, value=value):
                    malformed = copy.deepcopy(data)
                    malformed[key] = value
                    write_json(catalog, malformed)
                    with self.assertRaises(ValueError):
                        load_methods(catalog)

    def test_lost_last_origin_is_detected_without_fixed_total(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = fixture(Path(directory))
            book = load_book(catalog)
            book['sources']['ch10-11th-A']['problem_numbers'] = [1, 2]
            self.assertTrue(any('出处清单' in e or '清单不一致' in e for e in catalog_issues(book)))

    def test_source_title_and_problem_inventory_are_required(self):
        with tempfile.TemporaryDirectory() as directory:
            book = load_book(fixture(Path(directory)))
            for metadata in [None, {'problem_numbers': [1]},
                             {'title': ' ', 'problem_numbers': [1]},
                             {'title': 123, 'problem_numbers': [1]}]:
                with self.subTest(metadata=metadata):
                    book['sources']['ch10-11th-A'] = metadata
                    self.assertTrue(any('非空 title' in e for e in catalog_issues(book)))
            book['sources']['ch10-11th-A'] = {'title': '来源标题'}
            self.assertTrue(any('缺少来源 problem_numbers' in e for e in catalog_issues(book)))
            book['sources']['ch10-11th-A'] = source_metadata([1])
            self.assertEqual(catalog_issues(book), [])

    def test_topic_alias_does_not_make_high_problem_common(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = fixture(Path(directory), finals=True)
            book = load_book(catalog)
            item = book['parts'][1]['chapters'][0]['items'][0]
            book['sources']['fin13-fill'] = source_metadata([1])
            item['origins'].append(dict(paper='fin13-fill', number=1))
            self.assertEqual(catalog_issues(book), [])
            item['audience'] = 'all'
            self.assertTrue(any('实际组别 high' in e for e in catalog_issues(book)))
            book['sources']['fin13-low'] = source_metadata([1])
            item['origins'].append(dict(paper='fin13-low', number=1))
            self.assertEqual(catalog_issues(book), [])

    def test_duplicate_alias_and_canonical_id_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            book = load_book(fixture(Path(directory)))
            items = book['parts'][0]['chapters'][0]['items']
            items.append(copy.deepcopy(items[0]))
            errors = catalog_issues(book)
            self.assertTrue(any('重复永久题号' in e for e in errors))
            self.assertTrue(any('出处或别名重复' in e for e in errors))

    def test_orphan_file_is_not_silently_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            book = load_book(fixture(Path(directory)))
            item = book['parts'][0]['chapters'][0]['items'][0]
            (item['path'].parent/'orphan.md').write_text(PROBLEM)
            self.assertTrue(any('单题目录与文件不一致' in e for e in catalog_issues(book)))

    def test_catalog_cannot_escape_source_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = fixture(Path(directory))
            data = json.loads(catalog.read_text())
            data['sources'] = '../outside.json'
            write_json(catalog, data)
            with self.assertRaisesRegex(ValueError, '越出源目录'):
                load_book(catalog)

    def test_chapters_must_be_chronological(self):
        with tempfile.TemporaryDirectory() as directory:
            book = load_book(fixture(Path(directory)))
            chapter = book['parts'][0]['chapters'][0]
            later = copy.deepcopy(chapter)
            later.update(id='preliminary-12', edition=12, year=2020)
            book['parts'][0]['chapters'].insert(0, later)
            self.assertTrue(any('届数必须递增' in e for e in catalog_issues(book)))

    def test_frontmatter_math_is_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog = fixture(root)
            (root/'frontmatter.md').write_text('# 序言\n\n未闭合 $x\n')
            errors, _ = check_sources(katex=False, catalog=catalog)
            self.assertTrue(any('frontmatter.md' in e and '数学定界符' in e for e in errors))

    def test_nested_tex_labels_and_missing_references_are_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'main.tex').write_text('\\input{first.tex}\n\\input{second.tex}\n')
            (root/'first.tex').write_text(r'\BookProblem{题1}{same}\ref{missing}')
            (root/'second.tex').write_text(r'\BookProblem{题2}{same}')
            (root/'book.log').write_text('Output written on book.pdf (1 page).\n')
            report = verify(root/'main.tex', root/'book.log')
            self.assertTrue(any('重复标签' in e and 'pr:same' in e for e in report['errors']))
            self.assertTrue(any('缺少引用目标' in e and 'missing' in e for e in report['errors']))
            self.assertEqual(report['labels'], 2)

    def test_cyclic_tex_inputs_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'first.tex').write_text(r'\input{second}')
            (root/'second.tex').write_text(r'\input{first.tex}')
            with self.assertRaisesRegex(ValueError, '循环 TeX 输入'):
                read_tex_tree(root/'first.tex')

    def test_repeated_tex_input_is_not_a_cycle_and_comments_are_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'main.tex').write_text('% \\input{missing.tex}\n\\input{child.tex}\n\\input{child.tex}')
            (root/'child.tex').write_text(r'\label{twice}')
            self.assertEqual(read_tex_tree(root/'main.tex').count(r'\label{twice}'), 2)

    def test_unstable_pdf_bookmarks_block_verification(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'book.tex').write_text('Text')
            (root/'book.log').write_text('Output written on book.pdf (1 page).\n'
                                       '(rerunfilecheck) Rerun to get outlines right\n')
            self.assertEqual(verify(root/'book.tex', root/'book.log')['verdict'], 'fail')

    def test_excerpt_preserves_full_book_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cross_report = root/'cross-volume-verification.json'
            cross_report.write_text('{"verdict":"pass"}')
            full = build(root/'book.tex', set())
            self.assertFalse(cross_report.exists())
            self.assertIn(r'\hypertarget{exam:finals-17}{}',
                          (root/'chapters/finals-17.tex').read_text())
            cross_report.write_text('{"verdict":"pass"}')
            before = (root/'problem-index.json').read_bytes()
            excerpt = build(root/'sample.tex', {'finals-17'})
            self.assertTrue(cross_report.exists())
            self.assertEqual((root/'problem-index.json').read_bytes(), before)
            self.assertEqual(len(json.loads(before)), full['stats']['problems'])
            self.assertEqual(excerpt['stats']['sources'], 4)
            self.assertEqual(len(json.loads((root/'sample-problem-index.json').read_text())),
                             excerpt['stats']['problems'])

    def test_clean_build_preserves_pdfs_and_external_symlink_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            build_dir = root/'build'
            build_dir.mkdir()
            source_dir = root/'src'
            source_dir.mkdir()
            source = source_dir/'chapter.md'
            source.write_text('Source stays outside the build directory.\n')
            for name in ('book.pdf', 'methods.PDF', 'book.tex', 'book.log'):
                (build_dir/name).write_text(name)
            generated = build_dir/'chapters'
            generated.mkdir()
            (generated/'chapter.tex').write_text('Generated chapter.\n')
            (generated/'nested-source-link').symlink_to(source)
            (build_dir/'source-link.pdf').symlink_to(source)
            (build_dir/'source-directory').symlink_to(source_dir, target_is_directory=True)
            clean_build(build_dir)
            self.assertEqual({p.name for p in build_dir.iterdir()}, {'book.pdf', 'methods.PDF'})
            self.assertEqual((build_dir/'book.pdf').read_text(), 'book.pdf')
            self.assertEqual((build_dir/'methods.PDF').read_text(), 'methods.PDF')
            self.assertEqual(source.read_text(), 'Source stays outside the build directory.\n')
            directory_link = root/'linked-build'
            directory_link.symlink_to(source_dir, target_is_directory=True)
            clean_build(directory_link)
            self.assertTrue(directory_link.is_symlink())
            self.assertTrue(source.is_file())


if __name__ == '__main__':
    unittest.main()
