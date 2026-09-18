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

## Cesàro 平均与 Stolz 的上下极限形式 {#app:limit-stolz}

若 $a_n\to L$，则 $n^{-1}\sum_{k=1}^na_k\to L$。证明把有限头部与最终落在 $L\pm\varepsilon$ 内的尾部分开，有限头部除以 $n$ 后消失。更一般地，正权 $w_k$ 满足 $W_n=\sum_{k\leq n}w_k\to\infty$ 时，$W_n^{-1}\sum_{k\leq n}w_ka_k\to L$。

**Stolz 的上下极限链。** 记
\[
r_n=\frac{a_n}{b_n},\qquad
u_n=\frac{a_{n+1}-a_n}{b_{n+1}-b_n}.
\]
在下列任一组条件下，都有
\[
\liminf u_n\leq\liminf r_n
\leq\limsup r_n\leq\limsup u_n,
\]
其中上下极限允许取 $\pm\infty$：

（1）无穷型：$b_n$ 严格递增到 $+\infty$，对实数列 $(a_n)$ 无其他要求；只需从 $b_n>0$ 的尾部起考虑商。

（2）零比零型：$b_n>0$ 严格递减到零，且 $a_n\to0$。

核心是正权平均。无穷型中，固定充分大的 $N$，则
\[
r_n=\frac{a_N}{b_n}
+\sum_{k=N}^{n-1}\frac{b_{k+1}-b_k}{b_n}u_k.
\]
有限头部 $a_N/b_n$ 趋于零，尾部正权之和趋于 $1$。因此 $u_k$ 的任意有限最终下界或上界，也是 $r_n$ 的下极限之下界或上极限之上界。让这些界逼近相应的上下极限，即得不等式链；用任意实数作界，也涵盖了无穷值。

零比零型则向尾端求和：由 $a_n,b_n\to0$，
\[
r_n=\sum_{k=n}^{\infty}\frac{b_k-b_{k+1}}{b_n}u_k.
\]
此式由有限望远镜求和后取极限得到，正权之和恰为 $1$，同样传递尾部的上下界。这里 $a_n\to0$ 不能删除，例如 $a_n=1+b_n$ 的差商恒为 $1$，而 $a_n/b_n\to+\infty$。

特别地，若 $u_n\to L$，不等式链便给出 $r_n\to L$，其中 $L$ 可以是扩展实数。这是通常的 Stolz 定理；无穷型并不要求 $a_n\to\infty$。

**何时可以反向。** 一般不能从商的收敛推出差商的收敛。例如 $a_n=nL+(-1)^n$、$b_n=n$ 时，$r_n\to L$，而 $u_n=L-2(-1)^n$ 振荡。以下两种附加条件分别控制尺度与振荡。

第一种是相邻尺度有固定分离：在上述任一种情形下，若最终有
\[
\frac{\max\{b_n,b_{n+1}\}}{|b_{n+1}-b_n|}\leq C,
\]
则 $r_n\to L\in\mathbb R$ 可以反推 $u_n\to L$。事实上，
\[
u_n-L=
\frac{b_{n+1}(r_{n+1}-L)-b_n(r_n-L)}{b_{n+1}-b_n},
\]
右侧两个系数都有界。无穷型的条件等价于增量 $(b_{n+1}-b_n)/b_n$ 最终有正下界；零比零型则是 $(b_n-b_{n+1})/b_n$ 最终有正下界。

若进一步有 $b_n/b_{n+1}\to0$（无穷型），或 $b_{n+1}/b_n\to0$（零比零型），且 $(r_n)$ 有界，则单个增量已支配相应尺度。由同一恒等式，分别有 $u_n-r_{n+1}\to0$ 或 $u_n-r_n\to0$，因而即使商不收敛，也有
\[
\liminf u_n=\liminf r_n,\qquad
\limsup u_n=\limsup r_n.
\]

第二种是单调性。若 $(v_n)$ 最终单调，且 $S_n=\sum_{k=1}^nv_k$ 满足 $S_n/n\to L\in\mathbb R$，则 $v_n\to L$。例如最终非减时，对充分大的 $n$，令 $m=\lfloor n/2\rfloor$，有
\[
\frac{S_n-S_m}{n-m}\leq v_n
\leq\frac{S_{2n}-S_n}{n}.
\]
两端均趋于 $L$；非增时不等号反向。这给出 Cesàro 平均的单调逆定理，也就是 $b_n=n$、差商最终单调时的 Stolz 逆向结论。平均会掩盖快速振荡，单调性正好排除了这一障碍。

**应用。** 对 $p>-1$，取 $a_n=\sum_{k=1}^nk^p$、$b_n=n^{p+1}$，差商趋于 $1/(p+1)$，所以 $\sum_{k\leq n}k^p\sim n^{p+1}/(p+1)$。若要求 $n^p/2$ 等修正项，则需[求和的 Euler–Maclaurin 公式](#app:taylor-em)。Stolz 负责首阶比例，带余项的求和公式负责更精细的信息。

## L’Hospital 法则与连续平均 {#app:limit-lhospital}

Stolz 的连续对应同样是不等式链。统一考虑 $x\uparrow\omega$，其中 $\omega$ 可以有限，也可以是 $+\infty$。设 $f,g$ 在该端点的左邻域内可微，且最终 $g>0$。在下列任一组条件下，
\[
\liminf_{x\uparrow\omega}\frac{f'(x)}{g'(x)}
\leq\liminf_{x\uparrow\omega}\frac{f(x)}{g(x)}
\leq\limsup_{x\uparrow\omega}\frac{f(x)}{g(x)}
\leq\limsup_{x\uparrow\omega}\frac{f'(x)}{g'(x)}:
\]

（1）无穷型：$g'>0$，且 $g(x)\to+\infty$；不要求 $f$ 也趋于无穷。

（2）零比零型：$g'<0$，且 $f(x),g(x)\to0$。

上下极限允许取扩展实数值，导数比收敛时便得到通常的 L’Hospital 法则。其他单侧趋近方向或分母符号，可通过反向参数化或同时将 $f,g$ 变号处理。

证明只需 Cauchy 中值定理：对端点附近的 $x<y$，某个 $\xi\in(x,y)$ 满足
\[
\frac{f(y)-f(x)}{g(y)-g(x)}=\frac{f'(\xi)}{g'(\xi)}.
\]
因此导数比的任意最终下界或上界，也约束相应的增量比。无穷型先固定 $x$，令 $y\uparrow\omega$，利用
\[
\frac{f(y)}{g(y)}=
\frac{f(x)}{g(y)}+
\left(1-\frac{g(x)}{g(y)}\right)
\frac{f(y)-f(x)}{g(y)-g(x)}
\]
消去固定头部。零比零型则固定 $x$ 后令 $y\uparrow\omega$，增量比直接趋于 $f(x)/g(x)$。再让有限的上下界逼近导数比的上下极限，即得完整链。

两种定理的共同机制是正权平均：离散情形把 $\Delta a$ 写成 $u\,\Delta b$；若 $f,g\in C^1$，连续情形则把 $f'\,\mathrm dx$ 写成 $(f'/g')g'\,\mathrm dx$。无穷型的正权分别为 $\Delta b$ 与 $g'\,\mathrm dx$；零比零型向尾端求和、积分，正权分别为 $-\Delta b$ 与 $-g'\,\mathrm dx$。Cauchy 中值定理使连续版不必额外要求导数连续。

**逆向需要控制局部振荡。** 在 $x\to+\infty$ 时，$f(x)=Lx+\sin x$、$g(x)=x$ 满足 $f/g\to L$，而 $f'/g'=L+\cos x$ 不收敛。即使取指数分母也不够：令
\[
f(x)=Le^x+\sin(e^{2x}),\qquad g(x)=e^x,
\]
仍有 $f/g\to L$，但 $f'/g'=L+2e^x\cos(e^{2x})$ 无界振荡。离散情形的尺度分离控制的是一个完整步长上的差商，无法自动约束连续情形在任意小区间内的振荡。

**单调密度定理。** 设 $u:[0,+\infty)\to[0,+\infty)$ 局部可积且最终单调，
\[
F(x)=\int_0^xu(t)\,\mathrm dt\sim Cx^\rho,
\qquad C,\rho>0,\quad x\to+\infty.
\]
则 $u(x)\sim C\rho x^{\rho-1}$。这提供了一个严格的“等价式求导”条件，而不要求 $u$ 连续。

固定 $\lambda>1$。若 $u$ 最终非减，对充分大的 $x$ 有
\[
\frac{F(x)-F(x/\lambda)}{x-x/\lambda}
\leq u(x)\leq
\frac{F(\lambda x)-F(x)}{(\lambda-1)x}.
\]
除以 $Cx^{\rho-1}$ 并取上下极限，左、右两端分别趋于
\[
\frac{1-\lambda^{-\rho}}{1-\lambda^{-1}},
\qquad
\frac{\lambda^\rho-1}{\lambda-1}.
\]
再令 $\lambda\downarrow1$，两者均趋于 $\rho$。最终非增时不等号反向，结论相同。$\rho=1$ 正是平均值收敛加单调性推出函数值收敛；一般的 $\rho$ 则同时恢复增长阶与首项系数。这类借助附加条件从平均恢复局部量的结论，通常称为 Tauber 型结论。

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
