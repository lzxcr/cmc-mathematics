# 解析函数、零点与留数方法

复分析的力量在于：局部可微性带来全局积分恒等式，而边界控制可以约束内部取值与零点。备考中应先辨认对象的区域、奇点和增长，再决定使用展开、最大值原理还是留数。围道的选择应服务于估计，而不只是把实积分补成闭曲线。

## Cauchy 公式与解析展开 {#app:complex-expansion}

若 $f$ 在闭圆盘 $\overline{D(a,R)}$ 的邻域解析，Cauchy 公式给出
\[
f(z)=\frac1{2\pi i}\int_{|\zeta-a|=R}\frac{f(\zeta)}{\zeta-z}\,\mathrm d\zeta,
\qquad |z-a|<R.
\]
把核写成几何级数，并在较小闭圆盘上一致求和，得到 Taylor 展开 $f(z)=\sum_{n\geq0}c_n(z-a)^n$，其中 $c_n=f^{(n)}(a)/n!$，且 $|c_n|\leq M_R/R^n$。于是当 $|z-a|\leq r<R$ 时，截断误差有显式界
\[
\left|f(z)-\sum_{n=0}^Nc_n(z-a)^n\right|
\leq M_R\frac{(r/R)^{N+1}}{1-r/R}.
\]
解析展开的优势不仅是“有无穷多导数”，还在于边界值给出了所有阶的统一控制。离最近奇点越近，可用的展开半径越小。

若 $f$ 在环域 $r<|z-a|<R$ 解析，则有唯一 Laurent 展开 $\sum_{n\in\mathbb Z}c_n(z-a)^n$，在每个紧子环域上一致收敛。系数由任意中间圆周上的同一积分给出。当内半径 $r=0$ 时，展开刻画 $a$ 处的孤立奇点：负次项不存在对应可去奇点；有有限个但至少一个非零负次项对应极点；有无限多个非零负次项对应本性奇点。这里必须选择展开区域：例如 $1/[z(z-1)]$ 在 $0<|z|<1$ 与 $|z|>1$ 有不同的 Laurent 展开。

## 最大模原理与边界增长 {#app:complex-maxmod}

解析函数在连通区域内部达到模的局部最大值时必为常数。一个解释来自圆周平均：中心值是边界值平均，若其模达到允许的最大值，三角不等式取等迫使小圆周上的值相同，再由恒等定理延拓。于是紧闭区域内的最大模通常由边界控制。

Cauchy 系数估计立即给出 Liouville 定理：有界整函数的所有正阶系数都为零。更一般地，若整函数满足 $|f(z)|\leq C(1+|z|)^m$，其中 $C>0$、$m\geq0$，令积分半径趋于无穷可知它是次数不超过 $\lfloor m\rfloor$ 的多项式。增长条件把解析问题转成有限维代数问题。

**应用。** 若 $\operatorname{Re}f\leq M$，不能直接声称 $|f|$ 有界；可改用 $e^f$ 或半平面到圆盘的变换。选择变换的依据是题设控制的是实部、模还是边界零点，而非机械套用最大模原理。

## 圆盘归一化与 Schwarz–Pick {#app:complex-disk}

若 $f:\mathbb D\to\mathbb D$ 解析且 $f(0)=0$，对 $f(z)/z$ 在半径 $r<1$ 的圆盘应用最大模原理，再令 $r\uparrow1$，得 $|f(z)|\leq|z|$、$|f'(0)|\leq1$。非平凡等号迫使 $f(z)=e^{i\theta}z$。这是 Schwarz 引理。

对任意 $a\in\mathbb D$，先用圆盘自同构 $\varphi_a(z)=(z-a)/(1-\overline az)$ 将定义域点移到零，再把函数值移到零。对复合映射应用 Schwarz 引理，得到
\[
\left|\frac{f(z)-f(a)}{1-\overline{f(a)}f(z)}\right|
\leq\left|\frac{z-a}{1-\overline az}\right|,
\qquad
\frac{|f'(a)|}{1-|f(a)|^2}\leq\frac1{1-|a|^2}.
\]
第一式在某对 $z\neq a$ 处取等，或第二式在某点取等，当且仅当 $f$ 为圆盘自同构。归一化把任意点估计转回唯一需要证明的原点情形。

若 $\operatorname{Re}h>0$ 且 $h(0)=1$，则 $w=(h-1)/(h+1)$ 映入圆盘且 $w(0)=0$。由 $|w(z)|\leq|z|$ 可得
\[
\frac{1-|z|}{1+|z|}\leq\operatorname{Re}h(z)
\leq\frac{1+|z|}{1-|z|}.
\]
圆盘、半平面与正实部函数之间的转换统一了大量看似不同的估计题。

## 零点因子与 Jensen 公式 {#app:complex-zeros}

设 $f$ 在闭圆盘邻域解析，$f(0)\neq0$，圆周 $|z|=R$ 上无零点。圆内零点按重数记为 $a_1,\ldots,a_N$。除去相应线性因子后，对无零点解析函数的 $\log|f|$ 使用调和平均性质，得到 Jensen 公式
\[
\log|f(0)|+\sum_{j=1}^N\log\frac R{|a_j|}
=\frac1{2\pi}\int_0^{2\pi}\log|f(Re^{it})|\,\mathrm dt.
\]
因此若边界模不超过 $M$，则半径 $r<R$ 内的零点数满足 $N(r)\log(R/r)\leq\log(M/|f(0)|)$。每个靠近中心的零点都要消耗一部分可用的边界增长。

同一估计也可用 Blaschke 因子 $B_a(z)=R(z-a)/(R^2-\overline az)$ 推导：它在 $|z|=R$ 上模为一，除去它不会改变边界模，却使中心值乘以 $R/|a|$。这给出竞赛中更短的证明；Jensen 公式则同时记录所有零点的距离。

## 辐角原理、Rouché 与极限的零点 {#app:complex-rouche}

若亚纯函数 $f$ 在正向简单闭曲线 $\Gamma$ 上无零点、极点，且在其内部除有限个极点外解析，则
\[
\frac1{2\pi i}\int_\Gamma\frac{f'(z)}{f(z)}\,\mathrm dz=N-P,
\]
零点与极点都按重数计算。局部写 $f=(z-a)^mg$，$g(a)\neq0$，便知 $f'/f$ 的留数为 $m$；极点对应负整数。这把零点计数变成边界绕数。

若 $f,g$ 在 $\Gamma$ 及其内部的邻域解析，且 $|g|<|f|$ 在边界成立，则同伦 $f+tg$（$0\leq t\leq1$）始终不经过零，边界绕数不变，所以 $f$ 与 $f+g$ 在内部有相同零点数。这是 Rouché 定理。严格边界不等式要逐点验证；只比较最高次项而没有给出适用半径，尚未完成证明。

**应用。** 在 $|z|=2$ 上，$|z^5|=32> |3z+1|\leq7$，所以 $z^5+3z+1$ 有五个根在该圆盘中。对局部一致收敛 $f_n\to f$，若 $f$ 在小圆周上无零点，则最终 $|f_n-f|<|f|$，小圆盘内零点数稳定。Hurwitz 定理由此推出：无零点解析函数的局部一致极限要么无零点，要么恒为零。常数零极限必须保留为例外。

## 留数定理与围道选择 {#app:complex-residues}

函数在孤立奇点 $a$ 的留数是 Laurent 展开中 $(z-a)^{-1}$ 的系数。留数定理为
\[
\int_\Gamma f(z)\,\mathrm dz=2\pi i\sum_a\operatorname{Res}(f,a)
\]
（简单闭曲线正向绕行，其内部除有限孤立奇点外解析）。对简单极点 $P/Q$，留数为 $P(a)/Q'(a)$；$m$ 阶极点可对 $(z-a)^mf(z)$ 求 $m-1$ 阶导数。选择局部展开有时比高阶求导更简洁。

围道积分转成实积分还须证明附加弧段消失。对有理函数，若在大圆弧上 $f(z)=O(|z|^{-2})$，弧长为 $O(R)$，则弧积分为 $O(R^{-1})$。例如上半圆内 $1/(1+z^4)$ 的两个极点为 $e^{i\pi/4},e^{3i\pi/4}$，各留数为 $1/(4z^3)$，和为 $-i/(2\sqrt2)$，故
\[
\int_{-\infty}^{\infty}\frac{\mathrm dx}{1+x^4}=\frac\pi{\sqrt2},
\qquad\int_0^\infty\frac{\mathrm dx}{1+x^4}=\frac\pi{2\sqrt2}.
\]
弧段估计同时说明原积分绝对收敛，推导没有省略极限步骤。

对于 $e^{iaz}R(z)$，$a>0$ 时选择上半平面，因为指数在那里衰减；$a<0$ 时反向选择。对含 $z^\alpha$ 或 $\log z$ 的函数，须先选分支，再沿割线两岸记录不同的相位。实轴上有极点时，绕开它的积分往往给 Cauchy 主值，不能与通常的反常积分混淆。

## 无穷远留数与代数求和 {#app:complex-infinity}

定义 $\operatorname{Res}_\infty f=-\operatorname{Res}_{w=0}(f(1/w)/w^2)$，即无穷远 Laurent 展开中 $z^{-1}$ 系数的相反数。对有理函数，所有有限留数与无穷远留数之和为零。

若首一多项式 $p$ 的 $n$ 个根 $\lambda_j$ 互异，则 $z^k/p(z)$ 在根处的留数为 $\lambda_j^k/p'(\lambda_j)$。当 $0\leq k<n$ 时，在无穷远比较 $z^{-1}$ 项即可得到
\[
\sum_j\frac{\lambda_j^k}{p'(\lambda_j)}
=\begin{cases}0,&k<n-1,\\1,&k=n-1.\end{cases}
\]
这与[插值最高次系数](#app:algebra-interpolation)是同一恒等式的两个解释。重根时必须使用高阶极点留数或 Hermite 插值，不能继续除以零的 $p'(\lambda_j)$。
