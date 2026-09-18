# 素数分布与复分析的视野

素数定理展示了分析方法怎样描述离散算术结构：唯一分解产生 Euler 乘积，取对数导数产生加权素数计数，解析性质再控制它的渐近行为。本章证明初等转换，明确引用深层定理，并用可计算的例子说明这些结论能做什么。

## 从素数无穷到计数尺度 {#app:primes-counting}

记 $\pi(x)=\#\{p\leq x:p\text{ 为素数}\}$。Euclid 的论证说明素数无穷：有限个素数乘积加一不被其中任何一个整除。但这不给出 $\pi(x)$ 增长多快。素数定理断言
\[
\pi(x)\sim\frac{x}{\log x}\qquad(x\to\infty).
\]
这里是相对误差趋零，不是每个长度为 $\log x$ 的区间恰有一个素数。素数的局部间隔仍可剧烈波动，不能把平均密度解释为独立随机选择的精确规律。

较弱但仍深刻的 Chebyshev 估计给出：对充分大的 $x$，存在绝对常数 $0<c<C$ 使 $cx/\log x\leq\pi(x)\leq Cx/\log x$。它可由中心二项式系数的大小及其素因子分解推导；Stirling 公式提供了二项式系数的指数尺度。要把两个常数收紧成同一个 $1$，需要额外思想。

## Euler 乘积与算术信息 {#app:primes-zeta}

对 $\operatorname{Re}s>1$，唯一分解定理及绝对收敛给出
\[
\zeta(s)=\sum_{n\geq1}\frac1{n^s}
=\prod_p(1-p^{-s})^{-1}.
\]
先对有限个素数展开几何级数，得到只含这些素因子的整数之和，再以绝对收敛取极限；这是无限乘积合法性的证明。它还说明该半平面内 $\zeta$ 无零点，因为对数乘积绝对收敛。

定义 von Mangoldt 函数 $\Lambda(n)$：当 $n=p^k$、$k\geq1$ 时取 $\log p$，其他情形取零。在更小的紧半平面上可逐项对数求导，得到
\[
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_p\sum_{k\geq1}\frac{\log p}{p^{ks}}
=\sum_{n\geq1}\frac{\Lambda(n)}{n^s}.
\]
取对数将乘法分解拆开，求导则给出对数权重。这是解析对象与加权素数计数之间的核心接口。

令 $\psi(x)=\sum_{n\leq x}\Lambda(n)$、$\vartheta(x)=\sum_{p\leq x}\log p$。高次素数幂的贡献至多为 $O(\sqrt x(\log x)^2)=o(x)$，故 $\psi(x)\sim x$ 与 $\vartheta(x)\sim x$ 等价。再通过分部求和，它们与素数定理等价。权重改变让解析公式更简单，却没有改变主阶分布。

## 深层输入在哪里 {#app:primes-theorem}

本章引用以下经典事实：$\zeta(s)$ 可亚纯延拓到复平面，只有 $s=1$ 一个简单极点，留数为 $1$；它在直线 $\operatorname{Re}s=1$ 上没有零点。第二项是经典解析证明的关键，并不由 Euler 乘积在 $\operatorname{Re}s>1$ 的无零性自动推出。

还需要一个将变换的边界行为传回原函数的 Tauber 型定理。Wiener–Ikehara 定理的一种适用形式是：非负系数 Dirichlet 级数 $F(s)=\sum a_nn^{-s}$ 在 $\operatorname{Re}s>1$ 收敛，且对某个 $A\geq0$，$F(s)-A/(s-1)$ 连续延至闭半平面的有限边界点，则 $\sum_{n\leq x}a_n=Ax+o(x)$。取 $F=-\zeta'/\zeta$、$A=1$，极点与无零边界给出条件，从而 $\psi(x)\sim x$。

这里说明的是证明的结构，并未证明无零直线定理或 Tauber 定理。它们分别承担“边界没有额外振荡源”与“从变换恢复累计量”的工作。只写下 $\zeta(s)\sim1/(s-1)$ 就推出素数定理是不充分的，因为靠近一个实点的主项不足以控制整个边界上的行为。

## 分部求和的三个应用 {#app:primes-applications}

对光滑 $f$，离散分部求和给出
\[
\sum_{p\leq x}f(p)=\pi(x)f(x)-\int_2^x\pi(t)f'(t)\,\mathrm dt,
\]
按端点约定包含素数 $2$。这是把计数信息传递给加权和的通用方式。

**第 $n$ 个素数。** 若 $p_n$ 是第 $n$ 个素数，$n=\pi(p_n)\sim p_n/\log p_n$。取对数先得 $\log p_n\sim\log n$，再代回，得到 $p_n\sim n\log n$。反演渐近式时，先控制对数尺度再替换，避免循环论证。

**素数和。** 取 $f(t)=t$，由素数定理和积分比较得
\[
\sum_{p\leq x}p=x\pi(x)-\int_2^x\pi(t)\,\mathrm dt
\sim\frac{x^2}{2\log x}.
\]
其中 $\int_2^xt/\log t\,\mathrm dt\sim x^2/(2\log x)$ 可由分部积分或 L'Hôpital 得到；素数定理中的小 o 误差先切去固定头部，再统一估计尾部，才能穿过积分。

**素数倒数和。** 取 $f(t)=1/t$，同样得
\[
\sum_{p\leq x}\frac1p
=\frac{\pi(x)}x+\int_2^x\frac{\pi(t)}{t^2}\,\mathrm dt
\sim\log\log x.
\]
因此素数虽越来越稀疏，其倒数和仍发散。更精细的 $\log\log x+B+o(1)$ 需要比这里使用的相对渐近更强的误差控制，不能仅由 $\pi(t)\sim t/\log t$ 直接声称。

## 零点、误差与尚未解决的问题 {#app:primes-zeros}

通过 Perron 反演并移动积分直线，$-\zeta'/\zeta$ 的极点贡献素数计数的主项，Zeta 零点产生振荡修正项。这一“主极点—主项，其他奇点—误差”的原则与[留数](#app:complex-residues)和[Mellin 变换](#app:transform-mellin)一致。但完整显式公式需处理截断、端点权重及无穷零点和的求和方式，此处只说明机制，不写成无条件可交换的级数恒等式。

Riemann 猜想断言所有非平凡零点的实部都为 $1/2$，目前仍未解决。在该猜想下可推出 $\psi(x)=x+O(x^{1/2}(\log x)^2)$；这是一项条件结论，并非本卷已经证明的估计。竞赛应用通常不需要猜想，只需理解变换的奇点位置如何预示误差尺度。

## 进一步阅读与知识边界

内篇的严格分析基础可参考 Rudin《Principles of Mathematical Analysis》与《Real and Complex Analysis》；Fourier、复分析和实分析的连续路线可参考 Stein 与 Shakarchi 的 Princeton Lectures in Analysis 前三卷。渐近展开与特殊函数可参考 Olver《Asymptotics and Special Functions》，数值微分方程可参考 Hairer、Nørsett 与 Wanner《Solving Ordinary Differential Equations I》。这些教材补足本卷引用的测度、完备性、反演与稳定性定理。

代数可参考 Dummit 与 Foote《Abstract Algebra》，并以其中的模结构定理对照矩阵标准形；表示与 Lie 理论可分别参考 Serre《Linear Representations of Finite Groups》和 Hall《Lie Groups, Lie Algebras, and Representations》。概率极限可参考 Billingsley《Probability and Measure》；素数定理与 Zeta 函数的完整证明可参考 Davenport《Multiplicative Number Theory》及 Titchmarsh《The Theory of the Riemann Zeta-function》。

备考时不必按这些教材从头覆盖全部理论。遇到反复出现的结构，先掌握本卷相应的可用命题与自含例子；若题目触及所引用深层定理的边界，再按主题查证假设与证明。理论越一般，使用时越应把它怎样落实到本题写清楚。
