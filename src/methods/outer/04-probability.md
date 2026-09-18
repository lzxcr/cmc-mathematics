# 概率结构与极限定理

概率题中的积分、递推和极限，通常由少数几种结构产生：把随机变量映到新的空间，将独立变量相加，或先固定一部分信息再取平均。先辨认这些结构，往往就能选择合适的对象：极值适合分布函数，独立和适合卷积与特征函数，平方误差适合条件投影，随机跳跃适合转移算子。

本章由分布的定义出发，给出这些工具的推导，再将它们用于指数等待时间、正态回归和极限定理。条件期望的一般存在性和特征函数的唯一性使用标准定理并明确注明；密度变换、投影恒等式、正态条件公式以及这里使用的中心极限定理证明步骤均予以展开。

## 分布是测度：先描述事件，再求密度 {#app:probability-law}

随机变量 $X$ 的分布是实线上由 $\mu_X(B)=\mathbb P(X\in B)$ 定义的概率测度。分布函数
\[
F_X(t)=\mathbb P(X\le t)
\]
决定这个测度，因为 $\mathbb P(a<X\le b)=F_X(b)-F_X(a)$。它单调、右连续，并在两端分别趋于 $0,1$。只有当 $F_X(t)=\int_{-\infty}^tp_X(x)\,\mathrm dx$ 时，才称 $p_X$ 为其密度。常数随机变量有分布，却没有相对于长度测度的密度。

对非负或可积函数 $h$，有
\[
\mathbb Eh(X)=\int h(x)\,\mu_X(\mathrm dx).
\]
这由示性函数出发，经线性组合和单调收敛得到。它说明计算变换后变量的期望，不一定先求新密度；能在旧分布下直接积分时，就可以省去一次变量变换。

**极值的入口是事件分解。** 若 $X_1,\ldots,X_n$ 独立同分布，公共分布函数为 $F$，则
\[
\mathbb P\!\left(\max_iX_i\le t\right)=F(t)^n,
\qquad
\mathbb P\!\left(\min_iX_i>t\right)=(1-F(t))^n.
\]
因为最大值不超过 $t$ 意味着每个变量都不超过 $t$，最小值超过 $t$ 意味着每个变量都超过 $t$；独立性才允许相乘。若 $F$ 有密度 $f$，再求导可得极值密度。

当 $n\ge2$ 时，最小值 $U$ 和最大值 $V$ 的联合密度为
\[
p_{U,V}(u,v)=n(n-1)[F(v)-F(u)]^{n-2}f(u)f(v),\qquad u<v.
\]
解释各因子：有 $n(n-1)$ 种方式指定产生两端点的样本，其他 $n-2$ 个样本都必须落在中间区间。也可先写联合分布函数再求混合导数。这是[次序统计量题](#pr:fin09-hi:13)的基础；$n=1$ 时二维分布集中在对角线上，应单独处理。

## 变量变换：密度与体积元一起变化 {#app:probability-transforms}

设随机向量 $X$ 在开集 $D\subseteq\mathbb R^d$ 上有密度 $p_X$，$T:D\to T(D)$ 是连续可微双射且逆映射也连续可微。由积分换元，$Y=T(X)$ 的密度为
\[
p_Y(y)=p_X(T^{-1}(y))\left|\det DT^{-1}(y)\right|.
\]
Jacobian 修正的是体积元：等概率的小块在新坐标里可能有不同体积。应用时必须同时写清新区域。若变换有多个一一分支，要将各分支的贡献相加；例如 $Y=X^2$ 时，正负两个原像都可能产生同一个 $y$。

**一个可算的例子。** 独立的 $X_1,X_2$ 均匀分布于 $(0,1)$，令 $U=\min(X_1,X_2)$、$V=\max(X_1,X_2)$。在三角形 $0<u<v<1$ 上联合密度为 $2$。取
\[
S=U+V,\qquad D=V-U,
\qquad (U,V)=\left(\frac{S-D}{2},\frac{S+D}{2}\right).
\]
Jacobian 为 $1/2$，新区域为 $0<d<\min(s,2-s)$。所以
\[
p_S(s)=\begin{cases}s,&0<s<1,\\2-s,&1\le s<2,\\0,&\text{其他}.
\end{cases}
\]
这里 $U+V=X_1+X_2$，同一结果也能由卷积得到。两种做法相互核验，也展示了选坐标的重要性：和与差把三角区域的截面长度直接变成密度。

**条件事件也可进入换元。** 设 $X_1,\ldots,X_n$ 独立服从参数 $1$ 的指数分布，$Y=\min_iX_i$，$J$ 为最小值指标。固定 $J=j$ 后，写 $X_j=y$、$X_i=y+z_i$（$i\ne j$）。Jacobian 为 $1$，未归一化密度为
\[
e^{-ny}\prod_{i\ne j}e^{-z_i},\qquad y,z_i>0.
\]
积分给出 $\mathbb P(J=j)=1/n$；除以该概率后，密度分解为 $ne^{-ny}\prod_{i\ne j}e^{-z_i}$。因此在此条件下，最小值与剩余等待时间独立，后者仍为参数 $1$ 的指数分布。这既证明了无记忆性的多变量形式，也避免把“给定某个连续值”误当成普通正概率事件。完整应用见[指数样本题](#pr:fin16-high:12)。

## 独立和、卷积与 Gamma–Beta 分解 {#app:probability-convolution}

若 $X,Y$ 独立且有密度 $f,g$，由二维积分换元得到
\[
p_{X+Y}(s)=\int_{\mathbb R}f(x)g(s-x)\,\mathrm dx=(f*g)(s).
\]
积分区域由两个密度的支集共同决定。独立性保证联合密度为乘积；没有独立性时，应在同一个积分中使用真实的联合密度，不能直接卷积边缘密度。

参数 $1$ 的指数变量密度为 $e^{-x}1_{\{x>0\}}$。若 $S_n$ 为 $n$ 个独立指数变量之和，归纳计算
\[
p_{S_{n+1}}(s)=\int_0^s\frac{x^{n-1}e^{-x}}{(n-1)!}e^{-(s-x)}\,\mathrm dx
=\frac{s^ne^{-s}}{n!},\qquad s>0.
\]
这得到 $S_n\sim\operatorname{Gamma}(n,1)$，并给出其分布函数
\[
\mathbb P(S_n\le t)=1-e^{-t}\sum_{j=0}^{n-1}\frac{t^j}{j!},\qquad t\ge0.
\]
一般的 $\operatorname{Gamma}(a,1)$（$a>0$）密度为 $x^{a-1}e^{-x}/\Gamma(a)$，其中 $\Gamma(a)=\int_0^\infty x^{a-1}e^{-x}\,\mathrm dx$。

独立的 $U\sim\operatorname{Gamma}(a,1)$、$V\sim\operatorname{Gamma}(b,1)$ 有一个更精确的结构：总和 $S=U+V$ 与比例 $R=U/(U+V)$ 独立。因为反变换 $(U,V)=(SR,S(1-R))$ 的 Jacobian 为 $S$，联合密度成为
\[
\frac{s^{a+b-1}e^{-s}}{\Gamma(a+b)}
\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}r^{a-1}(1-r)^{b-1},
\qquad s>0,\ 0<r<1.
\]
两因子分别为 Gamma 与 Beta 密度。因此
\[
U+V\sim\operatorname{Gamma}(a+b,1),\qquad
\frac U{U+V}\sim\operatorname{Beta}(a,b).
\]
相同尺度参数是关键；若两个 Gamma 变量的指数衰减率不同，上式的指数项会同时依赖 $s,r$，独立分解通常失效。[指数最小值与总和之比](#pr:fin16-high:12)正是先识别独立的 Gamma 分量，再做这一变换。

## 特征函数：把独立相加变成相乘 {#app:probability-characteristic}

实随机变量的特征函数为 $\phi_X(t)=\mathbb Ee^{itX}$。它始终存在，因为被积函数的模为 $1$；这比只在部分参数上存在的矩母函数更适合讨论极限。对独立变量，
\[
\phi_{X+Y}(t)=\phi_X(t)\phi_Y(t),\qquad
\phi_{aX+b}(t)=e^{itb}\phi_X(at).
\]
第一式来自独立性，第二式来自代入。计算之前应先辨认独立和、尺度与平移，避免重复积分。

**公平二进位。** 固定 $a>0$，若 $D_k$ 独立且以相同概率取 $0,1$，则 $Y_n=a\sum_{k=1}^nD_k2^{-k}$ 等概率地取值于 $a j/2^n$（$0\le j<2^n$）。所以
\[
\phi_{Y_n}(t)=2^{-n}\sum_{j=0}^{2^n-1}e^{iatj/2^n}
\longrightarrow\int_0^1e^{iatx}\,\mathrm dx.
\]
右边是 $(0,a)$ 上均匀分布的特征函数。这里识别等概率网格比化简三角函数乘积更直接，见[二进位分布题](#pr:fin08-hi:13)。

下面使用两个标准定理：特征函数唯一决定概率分布；若特征函数列逐点收敛到在零点连续的函数，则该函数仍是某个概率分布的特征函数，原分布列弱收敛于它。这是 Lévy 连续性定理，本章不证明。弱收敛等价于对每个有界连续 $h$，期望 $\mathbb Eh(X_n)$ 收敛；它不自动允许取无界的 $h(x)=x$ 或 $x^2$。

例如，令 $X_n=n$ 的概率为 $1/n$，否则为 $0$，则 $X_n\to0$ 依概率，但 $\mathbb EX_n=1$。若需要同时传递期望，还必须控制尾部；矩界、控制收敛或一致可积性正用于补足这一环节。

## 矩、尾概率与截断 {#app:probability-moments}

期望给出位置，方差给出均方尺度。独立且平方可积的 $X_k$ 满足
\[
\mathbb E\sum_kX_k=\sum_k\mathbb EX_k,
\qquad
\operatorname{Var}\!\left(\sum_kX_k\right)=\sum_k\operatorname{Var}X_k.
\]
方差相加源于交叉协方差为零；均值线性则不要求独立。对平方可积的 $X$，由事件上 $(X-\mathbb EX)^2\ge t^2$ 得 Chebyshev 不等式
\[
\mathbb P(|X-\mathbb EX|\ge t)\le\frac{\operatorname{Var}X}{t^2}.
\]
因此想证明平均误差趋零，先比较总方差与归一化因子的平方。

尾概率也能直接表达矩。若 $T\ge0$、$r>0$，由 $T^r=\int_0^Trt^{r-1}\,\mathrm dt$ 和 Tonelli 定理，
\[
\mathbb ET^r=\int_0^\infty rt^{r-1}\mathbb P(T>t)\,\mathrm dt,
\]
允许两边同时为无穷。这把矩的存在性变成尾部积分，也给出截断矩的界
\[
\mathbb E[T^2 1_{\{T\le b\}}]\le\mathbb E\min(T,b)^2
=2\int_0^bt\,\mathbb P(T>t)\,\mathrm dt.
\]

当二阶矩不存在时，可以先截断再用方差。设 $X_i$ 独立同分布且 $t\mathbb P(|X_1|>t)\to0$。令 $Y_{ni}=X_i1_{\{|X_i|\le n\}}$、$\mu_n=\mathbb EY_{n1}$，则
\[
\mathbb P(\exists i\le n:X_i\ne Y_{ni})\le n\mathbb P(|X_1|>n)\to0,
\]
且上面的尾积分公式给出
\[
\frac{\mathbb EY_{n1}^2}{n}\le\frac2n\int_0^nt\mathbb P(|X_1|>t)\,\mathrm dt\to0.
\]
最后对截断和用 Chebyshev，就得到 $n^{-1}\sum_{i\le n}X_i-\mu_n\to0$ 依概率成立。这是[弱大数律与截断题](#pr:fin11-high:12)的完整机制：大值发生概率小，截断后的总方差也小；两者缺一不可。

需要下界时可反向使用二阶矩。对非负、平方可积且 $\mathbb EX>0$ 的 $X$，令 $E=\{X>\eta\mathbb EX\}$（$0<\eta<1$）。有 $(1-\eta)\mathbb EX\le\mathbb E(X1_E)$，再由 Cauchy–Schwarz，
\[
\mathbb P(E)\ge(1-\eta)^2\frac{(\mathbb EX)^2}{\mathbb EX^2}.
\]
这说明二阶矩与均值平方同阶时，随机变量以正概率达到均值的固定比例；只给出期望大，通常不能单独推出这种概率下界。

## 条件期望：信息子空间上的投影 {#app:probability-conditional}

设 $X$ 可积，$\mathcal G$ 表示已知信息，即一个子 $\sigma$ 代数。条件期望 $\mathbb E(X\mid\mathcal G)$ 是 $\mathcal G$ 可测的可积变量 $Z$，满足
\[
\mathbb E(Z1_A)=\mathbb E(X1_A),\qquad A\in\mathcal G.
\]
它在零测集之外唯一：若 $Z_1,Z_2$ 都满足定义，可对 $\{Z_1>Z_2\}$ 及其子水平集比较积分。一般存在性由 Radon–Nikodym 定理保证，此处将它作为标准结果使用。有限分割时没有这一抽象困难：在每个正概率分块上，$Z$ 就是 $X$ 在该块内的平均值。

若 $X\in L^2$，取 $Z=\mathbb E(X\mid\mathcal G)$。先证明 $Z$ 也平方可积：令 $Z_m=Z1_{\{|Z|\le m\}}$，定义和 Cauchy–Schwarz 给出 $\mathbb EZ_m^2=\mathbb E(XZ_m)\le\|X\|_2\|Z_m\|_2$；令 $m\to\infty$，得 $\|Z\|_2\le\|X\|_2$。定义进而蕴含
\[
\mathbb E[(X-Z)W]=0,\qquad W\in L^2(\mathcal G).
\]
先对简单的有界 $W$ 成立，再通过截断逼近推广。因此对任何 $\mathcal G$ 可测的平方可积预测量 $W$，
\[
\mathbb E(X-W)^2=\mathbb E(X-Z)^2+\mathbb E(Z-W)^2.
\]
条件期望于是是利用已知信息预测 $X$ 的最佳均方逼近，并在几乎处处相等的意义下唯一。它与有限维最小二乘具有同一正交结构，但允许全部可测预测函数；有限维正规方程见[投影与 Gram 矩阵](#app:linear-gram)。

三个常用结论可以直接从定义得到。首先，$\mathbb E\mathbb E(X\mid\mathcal G)=\mathbb EX$。其次，若 $\mathcal H\subseteq\mathcal G$，则塔式法则为
\[
\mathbb E[\mathbb E(X\mid\mathcal G)\mid\mathcal H]
=\mathbb E(X\mid\mathcal H).
\]
因为两边对每个 $A\in\mathcal H$ 有相同积分。最后，可积性成立时，已知的因子可以提出：$\mathbb E(WX\mid\mathcal G)=W\mathbb E(X\mid\mathcal G)$，其中 $W$ 为 $\mathcal G$ 可测。

将投影恒等式用于常数预测量 $\mathbb EX$，得到全方差公式
\[
\operatorname{Var}X
=\mathbb E\operatorname{Var}(X\mid\mathcal G)
+\operatorname{Var}(\mathbb E[X\mid\mathcal G]).
\]
第一项是给定信息后仍剩下的波动，第二项是不同信息情形间均值的波动。随机和、分层抽样以及混合分布中的方差计算，都可以沿这两部分拆开。

条件平均还会降低凸函数的期望：若 $\Phi$ 为凸函数且各项可积，条件 Jensen 不等式给出 $\Phi(\mathbb E[X\mid\mathcal G])\le\mathbb E[\Phi(X)\mid\mathcal G]$。有限分割时这是每个分块上的普通 Jensen；一般情形可用凸函数是其支撑仿射函数的上确界来证明。[密度比最优不等式题](#pr:fin15-high:7)将空间压缩为两块，正是在保留质量约束的同时降低凸代价。

## 正态回归：把不相关升级为独立 {#app:probability-gaussian}

一般变量不相关并不意味着独立；联合正态变量具有这一额外性质。若正态向量均值为零、协方差为 $\Sigma$，其特征函数为
\[
\mathbb Ee^{it^{\mathrm T}X}=e^{-t^{\mathrm T}\Sigma t/2}.
\]
当协方差分块对角时，特征函数分解为两块边缘特征函数的乘积，由唯一性得到两块独立。这也说明不能仅凭两个边缘分布分别正态就使用该结论，必须是联合正态。

设 $U,V$ 为联合正态的标量变量，且 $\operatorname{Var}V>0$。取
\[
a=\frac{\operatorname{Cov}(U,V)}{\operatorname{Var}V},\qquad
R=U-\mathbb EU-a(V-\mathbb EV).
\]
残差 $R$ 与 $V$ 不相关，故独立，且均值为零。因此
\[
\mathbb E(U\mid V)=\mathbb EU+a(V-\mathbb EV).
\]
这不仅给最佳线性预测，还给全部可测预测中的最佳平方误差预测。没有正态性时，同一系数仍给最佳线性预测，但条件期望可能是非线性函数。若 $V$ 方差为零，直接按常数信息处理，不能除以零。

**单指标响应的计算。** 设 $X\sim N(0,\Sigma)$，$\Sigma>0$，独立噪声 $\varepsilon\sim N(0,\sigma^2)$，$\sigma^2>0$。令
\[
Z=\beta_0^{\mathrm T}X+\varepsilon,\qquad Y=\operatorname{sgn}Z,
\qquad v=\operatorname{Var}Z=\beta_0^{\mathrm T}\Sigma\beta_0+\sigma^2.
\]
向量版正态回归给出 $\mathbb E(X\mid Z)=\Sigma\beta_0 Z/v$。于是
\[
\mathbb E(XY)=\frac{\Sigma\beta_0}{v}\mathbb E|Z|
=\sqrt{\frac2{\pi v}}\,\Sigma\beta_0,
\]
其中 $\mathbb E|Z|=2\int_0^\infty z e^{-z^2/(2v)}\,\mathrm dz/\sqrt{2\pi v}=\sqrt{2v/\pi}$。最小化 $\mathbb E(Y-\beta^{\mathrm T}X)^2$ 的正规方程为 $\Sigma\beta=\mathbb E(XY)$，所以
\[
\beta^*=\sqrt{\frac2{\pi v}}\,\beta_0.
\]
高维最小二乘因而只需一个一维绝对矩；这是[正态符号回归题](#pr:fin13-high:12)的主要简化。

更一般地，若 $Y=h(\beta_0^{\mathrm T}X,\varepsilon)\in L^2$、噪声独立于 $X$ 且 $\beta_0\ne0$，正态残差仍给出
\[
\beta^*=\frac{\mathbb E[(\beta_0^{\mathrm T}X)Y]}{\beta_0^{\mathrm T}\Sigma\beta_0}\,\beta_0.
\]
方向不变来自条件线性结构，响应函数只影响比例因子。平方可积性确保这里的最小二乘目标有意义；不能把“某个期望存在”直接当作充分条件。

## Poisson 到达、随机和与转移算子 {#app:probability-poisson}

设等待时间 $T_i$ 独立服从参数 $\lambda>0$ 的指数分布，$S_n=T_1+\cdots+T_n$，$S_0=0$，$N_t=\max\{n:S_n\le t\}$。指数分布满足
\[
\mathbb P(T>s+t\mid T>s)=e^{-\lambda t}.
\]
在固定时刻 $t$，若已到达 $n$ 次，过去的信息只把下一次等待时间限制为 $T_{n+1}>t-S_n$；无记忆性使剩余时间仍为参数 $\lambda$ 的指数分布，且其条件分布不依赖过去。后续等待时间又与过去独立，所以重新开始的过程与原过程同分布，由此得到 $N_t$ 的平稳独立增量。这是 Poisson 过程的等待时间构造。由 Gamma 分布函数相减，
\[
\mathbb P(N_t=k)=\mathbb P(S_k\le t)-\mathbb P(S_{k+1}\le t)
=e^{-\lambda t}\frac{(\lambda t)^k}{k!}.
\]
特别地，$\mathbb EN_t=\operatorname{Var}N_t=\lambda t$。

若 $N\sim\operatorname{Poisson}(\mu)$，独立同分布标记 $\xi_i$ 又与 $N$ 独立，令 $Z=\sum_{i=1}^N\xi_i$，空和取零。先对 $N$ 条件化，得到
\[
\phi_Z(t)=\mathbb E[\phi_\xi(t)^N]
=\exp\{\mu(\phi_\xi(t)-1)\}.
\]
若 $\xi\in L^2$，由全期望和全方差公式，
\[
\mathbb EZ=\mu\mathbb E\xi,\qquad
\operatorname{Var}Z=\mu\operatorname{Var}\xi+\mu(\mathbb E\xi)^2
=\mu\mathbb E\xi^2.
\]
随机跳数自身的波动贡献了第二项，不能漏掉。

对 $f\in L^1([0,T])$，到达点上的随机和满足
\[
\mathbb E\sum_{n\ge1:S_n\le T}f(S_n)=\lambda\int_0^Tf(s)\,\mathrm ds.
\]
证明是将第 $n$ 个到达时间的密度相加：$\sum_{n\ge1}\lambda^ns^{n-1}e^{-\lambda s}/(n-1)!=\lambda$。先对 $|f|$ 用 Tonelli，得到期望绝对可和，再对 $f$ 交换求和与积分。这给出[Poisson 积分题](#pr:fin14-high:12)中的无偏估计。

当 $f\in L^2([0,T])$ 时还有
\[
\operatorname{Var}\!\left(\sum_{n\ge1:S_n\le T}f(S_n)\right)
=\lambda\int_0^Tf(s)^2\,\mathrm ds.
\]
对分段常值函数，随机和是互不相交区间计数的线性组合，由独立增量和 Poisson 方差立即成立；一般 $L^2$ 函数由阶梯逼近和同一均方恒等式得到。独立重复取均值后，方差再除以样本次数。

**算子形式。** 若每次跳跃对应一个平均算子 $T$，跳率为 $\lambda$，则时刻 $t$ 的转移算子为
\[
P_t=e^{-\lambda t}\sum_{k=0}^\infty\frac{(\lambda t)^k}{k!}T^k
=e^{\lambda t(T-I)}.
\]
当 $T$ 在有界函数空间上为压缩算子时，级数按算子范数收敛，可逐项求导，生成算子就是 $\lambda(T-I)$。这同时解释半群关系 $P_{t+s}=P_tP_s$ 和演化方程 $\partial_tu=\lambda(T-I)u$。

[格点随机游走题](#pr:fin15-high:12)中，一步在四个方向各以 $1/4$ 的概率跳长 $\varepsilon$，跳率为 $\varepsilon^{-2}$。每个坐标的单步方差为 $\varepsilon^2/2$，故单位时间方差趋向 $1/2$，极限应为 $B_{t/2}$；生成算子也恰趋向 $\Delta/4$。先算协方差可以预先确定扩散常数，再用特征函数把分布收敛严格化。

## 大数律与中心极限定理：先找正确尺度 {#app:probability-limit}

大数律描述平均值的误差消失，中心极限定理描述误差在更细尺度上的形状。两者的归一化通常不同。若独立变量具有有限方差，记
\[
S_n=\sum_{k=1}^n(X_k-\mathbb EX_k),\qquad
s_n^2=\sum_{k=1}^n\operatorname{Var}X_k.
\]
当 $s_n^2/n^2\to0$ 时，Chebyshev 直接给出 $S_n/n\to0$ 依概率成立。要得到正态极限，则应研究 $S_n/s_n$，还需排除少数大项支配总波动。

**独立同分布情形。** 若 $X_k$ 独立同分布、均值为 $m$、方差为 $0<\sigma^2<\infty$，则
\[
\frac{\sum_{k=1}^nX_k-nm}{\sigma\sqrt n}\Rightarrow N(0,1).
\]
这里给出以 Lévy 连续性定理为基础的短证。标准化后只需考虑 $\mathbb EX=0$、$\mathbb EX^2=1$。二阶 Taylor 余项配合控制收敛给出
\[
\phi_X(t)=1-\frac{t^2}{2}+o(t^2).
\]
确切地，将 $e^{itX}-1-itX+(tX)^2/2$ 除以 $t^2$，被积量逐点趋零，并由常数倍 $X^2$ 控制。独立性于是给出
\[
\phi_{S_n/\sqrt n}(t)
=\phi_X(t/\sqrt n)^n
=\left(1-\frac{t^2}{2n}+o(n^{-1})\right)^n
\longrightarrow e^{-t^2/2}.
\]
极限是标准正态特征函数，结论由连续性定理得到。有限二阶矩在这里用于保证余项可控制，不能随意删除。

**不同分布的独立项。** 对每个 $n$，设 $X_{n1},\ldots,X_{nk_n}$ 相互独立、均值为零，且 $s_n^2=\sum_k\mathbb EX_{nk}^2>0$。若对每个 $\delta>0$，
\[
\frac1{s_n^2}\sum_k\mathbb E\!\left[X_{nk}^2
1_{\{|X_{nk}|>\delta s_n\}}\right]\longrightarrow0,
\]
则 $s_n^{-1}\sum_kX_{nk}\Rightarrow N(0,1)$。这是 Lindeberg 条件：相对于总标准差而言的大跳跃不能贡献非消失比例的方差。同一行内部独立即可，不要求不同行相互独立。

证明机制仍是特征函数的二阶展开。令 $Y_{nk}=X_{nk}/s_n$，则总二阶矩为 $1$。在 $|Y_{nk}|\le\delta$ 与其补集上分别估计余项，得到固定 $t$ 时
\[
\sum_k\mathbb E\left|e^{itY_{nk}}-1-itY_{nk}
+\frac{t^2Y_{nk}^2}{2}\right|
\le C_t\delta+C_t\sum_k\mathbb E[Y_{nk}^2 1_{\{|Y_{nk}|>\delta\}}].
\]
先令 $n\to\infty$，再令 $\delta\downarrow0$，总余项趋零。Lindeberg 条件还给出 $\max_k\mathbb EY_{nk}^2\to0$：小值部分至多为 $\delta^2$，大值部分由总尾矩控制。又因变量已中心化，有 $|\phi_{Y_{nk}}(t)-1|\le t^2\mathbb EY_{nk}^2/2$，故这些差的平方和趋零，取对数只产生可忽略的误差。独立乘积的对数因而趋于 $-t^2/2$。再次使用 Lévy 定理即得结论。

**一个完整的备考例子。** 令 $X_1,\ldots,X_n$ 独立且 $\mathbb P(X_i=1)=p$、$\mathbb P(X_i=0)=1-p$，其中固定 $0<p<1$，$S_n=\sum_iX_i$。则
\[
\mathbb ES_n=np,\qquad \operatorname{Var}S_n=np(1-p),
\qquad
\mathbb P\!\left(\left|\frac{S_n}{n}-p\right|\ge a\right)
\le\frac{p(1-p)}{na^2}.
\]
这已经给出带明确误差界的大数律。再由上述中心极限定理，对固定 $c>0$，
\[
\mathbb P\bigl(|S_n-np|\le c\sqrt{np(1-p)}\bigr)
\longrightarrow2\Phi(c)-1,
\]
其中 $\Phi$ 是标准正态分布函数。大数律把误差除以 $n$；中心极限定理把误差除以 $\sqrt n$，保留了非平凡的波动分布。极限定理本身只给收敛，不给有限样本近似的统一误差率。

**两类非同分布应用。** 对独立对称变量 $X_k=\pm k^\theta$，有 $s_n^2\sim n^{2\theta+1}/(2\theta+1)$，而 $\max_{k\le n}|X_k|/s_n\to0$，所以 Lindeberg 的截断项最终全部为零。中心极限定理对所有 $\theta>0$ 成立，大数律 $S_n/n\to0$ 却只在 $\theta<1/2$ 成立；见[加权符号变量题](#pr:fin10-hi:13)。

对独立 $X_k\sim\operatorname{Bernoulli}(1/k)$，均值和方差都为 $\log n+O(1)$，正确波动尺度是 $\sqrt{\log n}$。中心化变量被 $1$ 控制，而总方差趋于无穷，同样直接满足 Lindeberg 条件。它也描述均匀随机排列的循环数：插入第 $k$ 个数字时，$k$ 种等概率位置中恰有一种新建循环，其余位置将它接到现有循环内。独立插入使新增循环指标为独立的 $\operatorname{Bernoulli}(1/k)$；详见[稀疏计数题](#pr:fin12-high:12)。

若仅知 $X_n\to0$ 依概率且 $|X_n|\le1$，则仍能推出期望绝对值趋零，因为 $\mathbb E|X_n|\le\eta+\mathbb P(|X_n|>\eta)$。这常用于将大数律传递给有界连续函数。它与对原变量直接交换极限和期望是不同的一步。

## 熵、互信息与凸性 {#app:probability-entropy}

对有限概率分布 $p=(p_i)$，熵为 $H(p)=-\sum_i p_i\log p_i$，约定 $0\log0=0$。有限取值随机变量的联合概率分解为 $p(x,y)=p(x)p(y\mid x)$；在正概率位置取对数再求和，得到链式法则
\[
H(X,Y)=H(X)+H(Y\mid X).
\]
条件熵是对条件分布熵的平均，不需要在零概率条件事件上任意赋值。

对同一有限集合上的两种分布，定义相对熵
\[
D(p\Vert q)=\sum_{p_i>0}p_i\log\frac{p_i}{q_i},
\]
若某处 $p_i>0$ 而 $q_i=0$，取值为 $+\infty$。其余情形由 $-\log t\ge1-t$，
\[
D(p\Vert q)\ge1-\sum_{p_i>0}q_i\ge0.
\]
等号要求每个正概率位置都有 $p_i=q_i$，同时 $q$ 在剩余位置无质量，因此恰在 $p=q$ 时成立。

把 $p$ 取为联合分布、$q$ 取为边缘分布乘积，得到
\[
H(X)-H(X\mid Y)
=D(p_{XY}\Vert p_Xp_Y)=I(X;Y)\ge0.
\]
这同时证明条件熵平均不增及等号当且仅当独立，见[熵的链式法则题](#pr:fin17-high:12)。一个具体例子是独立公平位 $X,Z$ 和 $Y=X\mathbin{\oplus}Z$：$X$ 与 $Y$ 独立，故单独知道 $Y$ 不降低 $X$ 的熵；同时知道 $Y,Z$ 却能恢复 $X$。信息的作用取决于当前已经知道什么。

对有限变量 $X,Y,Z$，在每个 $Z=z$ 的条件分布内重复相对熵证明，再平均，得到
\[
I(X;Y\mid Z)=H(X\mid Z)-H(X\mid Y,Z)\ge0.
\]
若 $X,Z$ 在给定 $Y$ 后条件独立，则链式法则给出
\[
I(X;Z)\le I(X;Y).
\]
因为 $I(X;Y,Z)=I(X;Y)+I(X;Z\mid Y)=I(X;Y)$，另一方面它等于 $I(X;Z)+I(X;Y\mid Z)$。这就是数据处理不等式：通过已知信息再作随机处理，不能增加它与原变量之间的互信息。

这些结论都由概率分解和凸性导出。使用时须保留“平均”和“有限分布”的条件：某个特定观测值对应的条件熵可以高于原熵；连续变量的微分熵也不具有这里全部的非负性性质，不能直接照搬。
