# 数学竞赛：题解与方法

**Jacobi Lie** · [jssnlzx@seu.edu.cn](mailto:jssnlzx@seu.edu.cn) · [CC BY-SA 4.0](LICENSE.md)

- [《全国大学生数学竞赛题解》](build/book.pdf)：第 1—17 届初赛与决赛，共 352 道题。按届次正序排列，共同题合并，专属题标注年级组。
- [《数学竞赛的方法与结构》](build/methods.pdf)：内篇 10 章、外篇 6 章，从估计与余项控制延伸到更一般的数学结构，供深入理解、自由选读和进一步学习。

两卷的使用方式与编写取向见各自序言。两份 PDF 放在同一目录下，可在支持外部 PDF 目标的阅读器中沿主题链接往返。材料来自互联网公开渠道；目录中只保留当前正文、必要编号和构建文件。

## 项目结构

```text
src/                  两卷的目录、正文、序言及共用版式
scripts/              生成、检查和清理工具
tools/                KaTeX 检查器及依赖清单
build/                PDF 成品；检查和编译时临时生成中间文件
docs/                 收录与编号说明、编辑规范
```

题解每题一个 Markdown，每场 `index.json` 管理次序、组别与永久标识；方法卷按主题拆章。`src/sources.json` 只保留题卷名称与题号清单，用于检查遗漏和重复。共用设计见 [layout.tex](src/layout.tex)，署名和共享说明见 [credits.tex](src/credits.tex)。

## 构建

依赖 Python 3（含 `pypdf`）、Node.js、LuaLaTeX、latexmk 和 synaptic 6.0.1 或更新版本。字体为 TeX Gyre Pagella 与思源宋体／黑体 CN；模板源码位于 `/home/lzx/项目/synaptic`。

```sh
python3 -m pip install -r requirements.txt  # 首次安装 PDF 检查依赖
npm ci --prefix tools                     # 首次安装公式检查依赖
make pdf               # 检查、编译两卷，验证链接后自动清理中间文件
make check             # 检查源稿并生成 TeX，保留中间结果供排查
make book              # 检查后仅编译题解卷，再清理
make methods           # 检查后仅编译方法卷，再清理
make clean             # 清理 build/ 中非 PDF 文件和 Python 缓存
```

编译失败时保留日志便于排查；成功后 `build/` 仅留 PDF。清理不影响 `src/`，无需下载原始资料即可重建。检查不能代替数学证明，修改正文后仍须核验论证并目视检查版面。

详见[收录与编号](docs/COVERAGE.md)、[编辑规范](docs/EDITING.md)及[共享许可](LICENSE.md)。
