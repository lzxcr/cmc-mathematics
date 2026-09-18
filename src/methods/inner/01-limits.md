# 极限、上下极限与渐近记号

求极限之前，先问对象是否真的收敛；求等价式之前，先问等价式将被怎样使用。上下极限描述尚未证明收敛的序列，渐近记号描述误差相对于指定尺度的大小。二者给后续的比较、展开和求和提供共同语言。

## 上下极限与子列 {#app:limit-limsup}

对实数列 $(a_n)$，允许取扩展实数值，定义
\[
\limsup_na_n=\lim_{N\to\infty}\sup_{n\geq N}a_n,
\qquad
\liminf_na_n=\lim_{N\to\infty}\inf_{n\geq N}a_n.
\]
前一个尾部上界单调下降，后一个尾部下界单调上升，所以两极限总存在于扩展实数系中。它们相等且有限，当且仅当 $a_n$ 收敛到这个公共值。对有界序列，上极限是子列极限的最大值，下极限是最小值；紧性保证极端聚点能够被取到。

若 $L=\limsup a_n\in\mathbb R$，其准确含义有两部分：任意 $\varepsilon>0$ 下，最终 $a_n<L+\varepsilon$；同时有无穷多个 $n$ 使 $a_n>L-\varepsilon$。前者给最终统一上界，后者防止上界被进一步降低。证明极限时常先设上下极限为 $l,L$，把递推或不等式传到它们，再证明 $L\leq l$。

有界实数列满足
\[
\liminf a_n+\liminf b_n\leq\liminf(a_n+b_n)
\leq\limsup(a_n+b_n)\leq\limsup a_n+\limsup b_n.
\]
一般不能把最右不等号改成等号：$a_n=(-1)^n$、$b_n=-a_n$ 的两个最大聚值不会同时出现。若一个数列收敛，则可把它的极限移出另一个数列的上下极限。连续单调函数也可相应移出；递减函数则交换上下极限。

**应用：渐近压缩。** 若 $a_n\geq0$ 有界，$a_{n+1}\leq q a_n+\varepsilon_n$，其中 $0\leq q<1$、$\varepsilon_n\to0$，则对上极限取界得到 $L\leq qL$，从而 $a_n\to0$。若未预先知道有界，可先用 $\varepsilon_n$ 有界及几何求和补上这一步。这种论证不要求 $a_n$ 单调。

## 大 O、小 o 与一致性 {#app:limit-notation}

在指定极限过程中，$f=O(g)$ 表示最终有 $|f|\leq C|g|$，常数 $C$ 不随趋近变量变化；$f=o(g)$ 表示 $f/g\to0$（分母须在所考虑区域内非零）；$f\sim g$ 表示 $f/g\to1$。$f\asymp g$ 通常表示二者非负且存在固定正数 $c,C$ 使 $cg\leq f\leq Cg$。每次都应明确是 $x\to0$、$n\to\infty$，还是另一个极限。

参数一致的 $r_\varepsilon(x)=O(\varepsilon^2)$（$x\in K$）表示同一个 $C$ 对所有 $x\in K$ 有效；一致小 o 则表示 $\sup_{x\in K}|r_\varepsilon(x)|/\varepsilon\to0$。若常数允许依赖参数，应写清其范围或记成 $O_a(\cdot)$。把固定参数结论用于随 $n$ 变化的参数，是误用渐近式的常见来源。

等价式可在乘除中替换，却不能任意穿过相减：$n+1\sim n$，但两者之差是 $1$，不是 $0$。存在抵消时，应改写成带余项的加法形式，例如
\[
\sqrt{1+x}=1+\frac x2-\frac{x^2}{8}+O(x^3).
\]
若要把差除以 $x^2$，只保留 $1+x/2+o(x)$ 就不够。展开到哪一阶，应由后续除法或累积的尺度反推。

逐项 $r_{n,k}=o(1)$ 不保证 $\sum_{k=1}^nr_{n,k}=o(1)$；即使所有项都等于 $1/n$，总和仍为 $1$。若有一致界 $|r_{n,k}|\leq Cn^{-2}$，才可立即得总和 $O(n^{-1})$。积分、乘积和行列式中的误差同样需要在操作层面控制。

## Cesàro 平均与 Stolz 定理 {#app:limit-stolz}

若 $a_n\to L$，则 $n^{-1}\sum_{k=1}^na_k\to L$。证明把有限头部与最终落在 $L\pm\varepsilon$ 内的尾部分开，有限头部除以 $n$ 后消失。更一般地，正权 $w_k$ 满足 $W_n=\sum_{k\leq n}w_k\to\infty$ 时，$W_n^{-1}\sum_{k\leq n}w_ka_k\to L$。

**Stolz 定理的无穷型。** 设 $b_n$ 严格递增且趋于 $+\infty$。若
\[
\frac{a_{n+1}-a_n}{b_{n+1}-b_n}\longrightarrow L,
\]
则 $a_n/b_n\to L$；$L$ 可为扩展实数。有限 $L$ 时，把充分大的各个增量夹在 $(L\pm\varepsilon)(b_{n+1}-b_n)$ 之间，望远镜求和后除以 $b_n$ 即得。无需额外要求 $a_n\to\infty$。

**零比零型。** 若 $b_n>0$ 严格递减到零，$a_n\to0$，且上述差商趋于 $L$，同一结论成立。此时应从 $n$ 向无穷远求和，利用两个序列的尾端极限；不能套用“分母趋于无穷”的证明。没有 $a_n\to0$，例如 $a_n=1+b_n$，结论立即失败。

**应用。** 对 $p>-1$，取 $a_n=\sum_{k=1}^nk^p$、$b_n=n^{p+1}$，差商趋于 $1/(p+1)$，所以 $\sum_{k\leq n}k^p\sim n^{p+1}/(p+1)$。若要求 $n^p/2$ 等修正项，则需[求和的 Euler–Maclaurin 公式](#app:taylor-em)。Stolz 负责首阶比例，带余项的求和公式负责更精细的信息。

## 从乘积到对数 {#app:limit-products}

正数乘积适合取对数，因为乘法误差变成可累积的加法误差。若 $u_k\to0$，则在 $|u_k|\leq1/2$ 时有一致估计
\[
\log(1+u_k)=u_k-\frac{u_k^2}{2}+O(|u_k|^3).
\]
于是有限乘积满足 $\log\prod_{k\leq n}(1+u_k)=\sum_{k\leq n}\log(1+u_k)$。若 $\sum|u_k|^3<\infty$，三阶余项的累计有界；若要证明归一化乘积趋于非零常数，则还要证明对应累计余项收敛。

**应用。** 固定 $a>-1$，由 $\log(1+a/k)=a/k+O(k^{-2})$ 得
\[
\log\prod_{k=1}^n\left(1+\frac ak\right)-a\log n
=a(H_n-\log n)+\sum_{k=1}^n\left(\log(1+a/k)-a/k\right).
\]
右端收敛，所以乘积除以 $n^a$ 趋于一个正的有限常数。关键不只是 $\log(1+x)\sim x$，而是误差 $O(k^{-2})$ 可求和。用 [Gamma 函数](#app:special-gamma)可进一步把常数识别为 $1/\Gamma(1+a)$。
