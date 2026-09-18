# 不等式、对偶与矩方法

常用不等式可按结构组织：凸性给出支撑界，内积给出正交分解，范数对偶把乘积变成可控的积。每次使用应同时检查指数匹配、等号条件，以及估计是否保留所需尺度。

## 凸性、对偶界与等号结构 {#app:estimate-convexity}

可微凸函数满足切线不等式 $\phi(y)\geq\phi(x)+\phi'(x)(y-x)$。令 $x=\sum_jw_jx_j$，其中 $w_j\geq0$、$\sum_jw_j=1$，求和便得到 Jensen 不等式
\[
\phi\!\left(\sum_jw_jx_j\right)\leq\sum_jw_j\phi(x_j).
\]
严格凸时，所有正权对应的 $x_j$ 相等才可能取等。连续版本同样成立，但须保证相关期望存在。凸性把多变量不等式转化为一个局部支撑关系，并同时解释等号。

Young 不等式 $ab\leq a^p/p+b^q/q$（$a,b\geq0$，$p,q>1$，$1/p+1/q=1$）来自对 $a$ 的凸函数求极值。归一化后积分，便得到 Hölder 不等式。使用时应先选共轭指数来匹配已知范数，而非盲目把每项都估大。

积分或矩阵不等式中的“最佳常数”常来自对偶证书：构造一个已知非负的平方、正半定矩阵或支撑函数，使目标差恰等于该对象。求等号就是令证书消失；这比在一长串松弛中追踪等号更可靠。二次型形式见[Gram 矩阵与正性](#app:linear-gram)。

## 范数插值与矩方法 {#app:estimate-moments}

在同一测度空间上，若 $1\leq p<r<q<\infty$，$1/r=\theta/p+(1-\theta)/q$，且 $f\in L^p\cap L^q$，对 $|f|^{\theta r}|f|^{(1-\theta)r}$ 使用 Hölder 得
\[
\|f\|_r\leq\|f\|_p^\theta\|f\|_q^{1-\theta}.
\]
特别地，$p=1,r=2,q=4$ 时，非零函数满足 $\|f\|_1\geq\|f\|_2^3/\|f\|_4^2$。这把绝对值积分的下界转化为二阶、四阶矩的计算；振荡和中这两个矩常可由[正交性计数](#app:integration-fourier)求出。

在概率空间上，若 $X\geq0$ 且 $0<\mathbb EX^2<\infty$，则对 $0<\eta<1$，
\[
\mathbb P(X>\eta\mathbb EX)\geq(1-\eta)^2\frac{(\mathbb EX)^2}{\mathbb EX^2}.
\]
设 $E=\{X>\eta\mathbb EX\}$。从 $(1-\eta)\mathbb EX\leq\mathbb E(X\mathbf1_E)$ 出发，用 Cauchy–Schwarz 即得。均值说明总质量有多少，二阶矩限制它集中在极少数点上的程度；两者共同迫使一个具有正概率的事件出现。

## 内积不等式、加权配方与最优常数 {#app:inequality-cauchy}

Cauchy–Schwarz 来自 $\|u-tv\|^2\geq0$ 对标量 $t$ 的极小化。因此等号恰在两向量线性相关时成立，复数情形需相应使用共轭。加权形式
\[
\left|\sum_ka_kb_k\right|^2
\leq\left(\sum_kw_k|a_k|^2\right)
\left(\sum_k\frac{|b_k|^2}{w_k}\right),\qquad w_k>0,
\]
只是把权重的平方根分配到两个向量。选权重的目的，是使一侧恰好等于题设已知的量。

**应用。** 若 $x_i>0$、$\sum_i x_i=s$，则 $\sum_i a_i^2/x_i\geq(\sum_i|a_i|)^2/s$。对 $|a_i|/\sqrt{x_i}$ 与 $\sqrt{x_i}$ 使用上式即得；当所有 $a_i\neq0$ 时，最佳 $x_i$ 与 $|a_i|$ 成比例。这同时给出不等式、最佳常数与极值点，无需分别用多变量微分求解。

## Hölder、Minkowski 与对偶 {#app:inequality-holder}

对共轭指数 $p,q>1$，Hölder 给出 $\int|fg|\leq\|f\|_p\|g\|_q$。其等号条件是非零情形下 $|f|^p$ 与 $|g|^q$ 成比例；若还涉及复数积分的绝对值，须检查相位一致。由此可得
\[
\|f\|_p=\sup_{\|g\|_q\leq1}\left|\int f\overline g\right|,
\]
取 $g=|f|^{p-2}f/\|f\|_p^{p-1}$ 即达等。这个对偶式直接推出 Minkowski 三角不等式，并解释为何把困难的范数问题转成线性配对有利。

在总质量为 $1$ 的空间上，若 $1\leq p<q$，则 $\|f\|_p\leq\|f\|_q$。一般有限测度空间须补上因子 $\mu(E)^{1/p-1/q}$；在无限测度空间上没有这种无条件包含关系。尺度因子缺失往往说明归一化尚未完成。

## 凸序、重排与主序 {#app:inequality-majorization}

将实向量的分量递减排列。若 $\sum_{i=1}^kx_i\geq\sum_{i=1}^ky_i$ 对 $k<n$ 成立，且总和相等，称 $x$ 主序于 $y$。它表示 $x$ 更分散。Karamata 不等式断言对凸函数 $\phi$ 有 $\sum_i\phi(x_i)\geq\sum_i\phi(y_i)$。

可把这看成反复平均的结果：用两个分量的保和混合替换原分量，凸函数和不会增加；一般主序关系可分解为有限次这种混合，这是主序定理的内容。竞赛中常不必引用完整定理，只要显式写出题目所需的一两次凸组合，应用 Jensen 即可。

另一类顺序信息是重排不等式：对同序实数列 $a_1\leq\cdots\leq a_n$、$b_1\leq\cdots\leq b_n$，同序配对的乘积和最大，逆序最小。交换一个逆序对使总和增加 $(a_j-a_i)(b_j-b_i)\geq0$，反复交换即证。这个证明说明，最优配对来自每次局部交换的符号，而非偶然的代数展开。

## 积分型能量不等式 {#app:inequality-energy}

若绝对连续函数 $f$ 在 $[a,b]$ 满足 $f(a)=0$ 且 $f'\in L^2$，则
\[
|f(x)|^2=\left|\int_a^xf'(t)\,\mathrm dt\right|^2
\leq(x-a)\int_a^x|f'(t)|^2\,\mathrm dt.
\]
再积分即可得到一个 Poincaré 型界 $\|f\|_2\leq(b-a)\|f'\|_2/\sqrt2$。若两端都为零，最佳常数为 $(b-a)/\pi$，对应第一特征函数 $\sin(\pi(x-a)/(b-a))$；可由正弦级数的 Parseval 等式证明。

因此最佳不等式常与谱问题相连：最小 Rayleigh 商 $\int|f'|^2/\int|f|^2$ 就是相应边界条件下的最低特征值。备考中先用基本积分与 Cauchy–Schwarz 得到够用的界；题目追问最佳常数时，再寻找等号函数或相关谱结构。
