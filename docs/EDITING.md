# 维护与编辑

## 文件职责

`src/book.json` 管理初赛、决赛及场次；`src/problems/<编>/<场次>/index.json` 管理单题顺序、组别、永久 `id` 和 `origins`。每题的题干、解答、评注同存一个 Markdown。`src/sources.json` 仅维护题卷名称及拆分后的题号清单，不依赖外部链接或历史下载文件。

`src/methods/book.json` 管理方法卷内外篇；每章一个 Markdown，一级标题须与目录一致。两卷序言分别在 `src/frontmatter.md`、`src/methods/frontmatter.md`，作者在 `src/layout.tex` 登记，共享说明在 `src/credits.tex` 统一维护。

## 数学与表述

主解揭示关键结构并完成论证；纯计算可简写，关键方法须说明动机、所需条件及中间步骤。评注保留本题的意义、边界情形和紧邻推广，共用理论转入方法卷。避免堆叠等价计算或没有新增思想的多种证明。

使用定理应核实假设，较深结论标明引用并提供专业阅读方向。点态展开不能冒充一致展开；交换求和、积分、极限或最值前，要解释余项如何控制。题目条件有缺陷时明确说明约定或订正。编译成功、数值试验和 AI 解释均不能替代证明。

## 语法与链接

单题只使用 `# 题目`、`# 解答`、可选 `# 评注`，按此顺序排列。题号、届次与组别由索引生成；小问用“（1）”，省略计分信息。方法章用 `# 章标题`、`## 节标题 {#app:topic}`，必要时使用三级标题。

行内数学用 `$…$`，行间数学用 `\[`、`\]`，多行推导用 `aligned`。解释器保留数学原文，不自动修补命令和括号。链接写成 `[方法卷：主题](#app:topic)` 或 `[某届某题](#pr:permanent-id)`；不写裸 TeX 引用或容易失效的页码。

## 检查与节选

```sh
python3 scripts/check_sources.py --problem src/problems/finals/17/01.md
make pdf
```

完整检查覆盖题解配对、来源题号、重复正文、孤立文件、编排与组别、公式和链接。`make pdf` 继续检查两卷编译日志及实际 PDF 的跨卷命名目标；全部通过才清理临时 TeX、索引、检查报告及编译缓存。失败时保留现场，修复后重建。

需要节选时先执行：

```sh
python3 scripts/build_book.py --only finals-17 --out build/sample.tex
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build build/sample.tex
python3 scripts/verify_book.py --tex build/sample.tex --log build/sample.log
make clean
```

节选生成独立索引，不覆盖全书目录；未包含的题目引用保留可读文字，方法链接继续指向同目录的 `methods.pdf`。永久 `id` 不随显示顺序变化，新增共同题应合并 `origins`，不复制正文。
