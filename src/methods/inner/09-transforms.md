# 含参积分与积分变换

参数能把难积分嵌入一个更容易微分或满足简单方程的函数族。积分变换则把同一思想系统化：先用一族核测试原函数，再让微分、卷积或缩放变成新变量上的代数运算。每一步都须保留定义域和交换运算的条件。

## 连续性、求导与 Leibniz 公式 {#app:transform-parameter}

设 $F(t)=\int_Ef(t,x)\,\mathrm d\mu(x)$。若 $f(t,x)$ 对 $t$ 连续且在参数的每个紧邻域内由同一 $L^1$ 函数支配，控制收敛给出 $F$ 连续。若偏导存在且 $|\partial_tf(t,x)|\leq g(x)$、$g\in L^1$，对差商应用同样论证得到 $F'(t)=\int_E\partial_tf(t,x)\,\mathrm d\mu$。可反复求导时，每一阶都要有对应控制。

有限区间上，若 $f$ 与 $\partial_tf$ 连续，$a(t),b(t)$ 可微，则
\[
\frac{\mathrm d}{\mathrm dt}\int_{a(t)}^{b(t)}f(t,x)\,\mathrm dx
=f(t,b(t))b'(t)-f(t,a(t))a'(t)+\int_{a(t)}^{b(t)}\partial_tf(t,x)\,\mathrm dx.
\]
边界项来自积分区间本身的变化。对于反常端点，应先截断再证明所有项的极限存在，不能直接照抄有限区间公式。

**应用。** 固定 $a>0$，令 $F(b)=\int_0^\infty e^{-ax}\sin(bx)/x\,\mathrm dx$。求导后的被积函数由 $e^{-ax}$ 支配，所以
\[
F'(b)=\int_0^\infty e^{-ax}\cos(bx)\,\mathrm dx=\frac a{a^2+b^2}.
\]
由 $F(0)=0$ 得 $F(b)=\arctan(b/a)$。若再令 $a\downarrow0$，需要额外的统一振荡尾界；对 $b>0$，Dirichlet 分部积分给出尾部 $O(1/(bR))$，从而恢复 $\int_0^\infty\sin(bx)/x\,\mathrm dx=\pi/2$。最后一步并没有一个显然的全区间绝对可积支配函数。

## 参数化差值与 Frullani 型积分 {#app:transform-frullani}

对 $a,b>0$，利用
\[
\frac{e^{-ax}-e^{-bx}}x=\int_a^be^{-tx}\,\mathrm dt
\]
可在有限参数区间内换序，得到
\[
\int_0^\infty\frac{e^{-ax}-e^{-bx}}x\,\mathrm dx
=\int_a^b\frac{\mathrm dt}{t}=\log\frac ba.
\]
当 $b>a$ 时可直接用 Tonelli；反向次序改变符号即可。这一表示让原来两项各自发散的差保持在同一个积分中。

一般地，若 $f$ 连续、在零与无穷处有有限极限，通过截断换元可得 Frullani 公式 $\int_0^\infty[f(ax)-f(bx)]\,\mathrm dx/x=(f(0)-f(\infty))\log(b/a)$。换元后仅余零端与无穷端的短区间积分，两端极限同时保证反常积分存在。一组便于直接换序的充分条件是 $f$ 局部绝对连续且 $f'\in L^1(0,\infty)$：写差为 $f(ax)-f(bx)=-\int_a^bxf'(tx)\,\mathrm dt$，绝对可积的二重积分保证换序。端点抵消与差值符号都必须保留。

## Laplace 变换与微分方程 {#app:transform-laplace}

对 $t\geq0$ 上的函数，定义 $\mathcal Lf(s)=\int_0^\infty e^{-st}f(t)\,\mathrm dt$。若 $f$ 局部可积且 $|f(t)|\leq Me^{ct}$，则 $\operatorname{Re}s>c$ 时绝对收敛。若 $f$ 绝对连续且相应边界项消失，分部积分给出
\[
\mathcal L(f')(s)=s\mathcal Lf(s)-f(0).
\]
因而常系数微分方程连同初值变成关于 $s$ 的代数方程。因果卷积 $(f*g)(t)=\int_0^tf(u)g(t-u)\,\mathrm du$ 在绝对可积条件下满足 $\mathcal L(f*g)=\mathcal Lf\,\mathcal Lg$。

**应用。** 对 $y'+ay=f$、$y(0)=y_0$，变换给出 $Y=(y_0+F)/(s+a)$。恢复后为
\[
y(t)=e^{-at}y_0+\int_0^te^{-a(t-u)}f(u)\,\mathrm du.
\]
这是积分因子公式；变换把它解释为初值响应与卷积响应。竞赛中若只需一阶方程，直接积分因子最短；面对高阶常系数、卷积项或分段外力时，变换的组织作用更明显。

Laplace 变换的唯一性和复反演公式需适当增长与正则性假设，可查专门教材。不能仅凭若干参数处的变换值就声称函数唯一；唯一性使用整个开半平面或足够丰富的参数集合。

## Fourier 变换、微分与卷积 {#app:transform-fourier}

约定 $\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,\mathrm dx$，反演系数为 $1/(2\pi)$。在 Schwartz 空间（函数及各阶导数都比任意幂衰减得快）中，各项绝对可积，分部积分与求导给出
\[
\widehat{f'}(\xi)=i\xi\widehat f(\xi),\qquad
\widehat{xf}(\xi)=i\frac{\mathrm d}{\mathrm d\xi}\widehat f(\xi),\qquad
\widehat{f*g}=\widehat f\,\widehat g.
\]
平移变成相位，缩放改变频率尺度。一般 $L^1$ 情形仍有变换与卷积公式；$L^2$ 情形通过 Plancherel 定理延拓，满足 $\|\widehat f\|_2^2=2\pi\|f\|_2^2$。这一延拓是均方意义的，不能随意把原始积分当成逐点绝对收敛。

**Gaussian 核。** 令 $G_t(x)=(4\pi t)^{-1/2}e^{-x^2/(4t)}$，$t>0$。配方或参数微分可得 $\widehat G_t(\xi)=e^{-t\xi^2}$，故 $G_s*G_t=G_{s+t}$。因此 $u(t)=G_t*f$ 的 Fourier 变换满足 $\partial_t\widehat u=-\xi^2\widehat u$，在适当条件下 $u_t=u_{xx}$。复杂的空间扩散变成每个频率独立衰减的标量方程。

Gaussian 还可用于反演的正则化：先乘 $e^{-\varepsilon\xi^2}$，让换序绝对合法；空间端则卷积 $G_\varepsilon$，最后利用[近似恒等算子](#app:integration-local)恢复原函数。这是一种可反复使用的“先控制，再取极限”的策略。

## Mellin 变换与乘法尺度 {#app:transform-mellin}

Mellin 变换定义为 $\mathcal Mf(s)=\int_0^\infty x^{s-1}f(x)\,\mathrm dx$，其收敛区域通常是一个竖直带。换元 $x=e^u$ 后，它成为 $u$ 变量上的双边 Laplace 变换；取 $s=\sigma+i\tau$ 时，又与 $e^{\sigma u}f(e^u)$ 的 Fourier 变换相连。

它把乘法缩放变成幂因子：$\mathcal M[f(ax)](s)=a^{-s}\mathcal Mf(s)$。因此涉及幂权、比例或 $x\mapsto1/x$ 对称的积分适合这一语言。$e^{-x}$ 的 Mellin 变换正是 $\Gamma(s)$；$1/(1+x)$ 在 $0<\operatorname{Re}s<1$ 中的变换为 $\pi/\sin\pi s$。

备考中未必需要完整 Mellin 反演理论。先识别可用的参数积分、写清竖直带及端点可积性，再用 Gamma–Beta 恒等式，往往就足以完成所需计算；这一视角还能预示为什么留数与幂次渐近会自然相遇。
