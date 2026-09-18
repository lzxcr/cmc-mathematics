# 级数、反常积分与振荡抵消

审敛首先区分质量与抵消。正项对象没有相消，比较尺度就足够；一般项对象则须追踪部分和或原函数。函数项级数还多了一层要求：若希望交换求和与极限、积分或导数，收敛必须在适当范数中受控。

## 正项级数：比较、比值与根值 {#app:series-positive}

对 $a_n\geq0$，部分和单调，所以收敛等价于部分和有界。若最终 $a_n\leq Cb_n$ 且 $\sum b_n<\infty$，则 $\sum a_n$ 收敛；若 $a_n\sim b_n>0$，两级数同敛散。模型 $\sum n^{-p}$ 在且仅在 $p>1$ 时收敛。

根值判别法给出 $L=\limsup_n\sqrt[n]{a_n}$：$L<1$ 时收敛，$L>1$ 时通项甚至不趋零；$L=1$ 时无结论。比值判别的常用充分条件为 $\limsup a_{n+1}/a_n<1$，或 $\liminf a_{n+1}/a_n>1$；需要各项最终为正。二者都在比较指数尺度，所以对 $n^{-p}$ 通常返回临界值 $1$，这时应换成幂次尺度。

例如若 $a_{n+1}/a_n=1-p/n+O(n^{-2})$，取对数并求和可得 $a_n\asymp n^{-p}$，事实上 $n^pa_n$ 趋于正数。于是 $p>1$ 收敛，$p\leq1$ 发散。这里 $O(n^{-2})$ 可求和，是精确结论的依据；仅有 $o(1/n)$ 在 $p=1$ 时不够，因为 $1/(n\log^2n)$ 与 $1/n$ 的比值主项相同，却敛散不同。

## 单调分组与积分判别 {#app:series-integral}

若 $f:[1,\infty)\to[0,\infty)$ 单调递减，则每个单位区间上
\[
f(k+1)\leq\int_k^{k+1}f(x)\,\mathrm dx\leq f(k).
\]
求和可知 $\sum f(k)$ 与 $\int_1^\infty f$ 同敛散；收敛时，尾和位于两个相邻的尾积分之间。它既是审敛法，也是误差估计。

对递减 $a_n\geq0$，按 $[2^j,2^{j+1})$ 分组，每组和夹在 $2^ja_{2^{j+1}}$ 与 $2^ja_{2^j}$ 之间。故 Cauchy 凝聚判别给出 $\sum a_n$ 与 $\sum_j2^ja_{2^j}$ 同敛散。于是
\[
\sum_{n\geq2}\frac1{n(\log n)^p}
\quad\text{在且仅在 }p>1\text{ 时收敛}.
\]
重复取对数可以处理更细的临界尺度。单调性是这些分组比较的条件；缺少它时，稀疏尖峰可能让采样值与积分完全失配。

## 一般项级数与 Abel 分部求和 {#app:series-dirichlet}

复数项级数满足 Cauchy 准则：收敛当且仅当任意足够远的有限尾和都一致小。绝对收敛保证这一点，并允许重排与换序；条件收敛不能任意重排。令 $A_k=\sum_{j=m}^ka_j$，离散分部积分为
\[
\sum_{k=m}^na_kb_k=A_nb_n+\sum_{k=m}^{n-1}A_k(b_k-b_{k+1}).
\]
若 $|A_k|\leq C$，则右侧由 $C(|b_n|+\sum|b_k-b_{k+1}|)$ 控制。它把通项的振荡放进部分和，把缓慢变化放进差分。

**Dirichlet 判别法。** 若 $a_n$ 的部分和有界，实数 $b_n$ 单调趋于零，则 $\sum a_nb_n$ 收敛。尾部原函数仍由某个固定常数控制，且 $\sum_{k=m}^{n-1}|b_k-b_{k+1}|=|b_m-b_n|$，所以尾和随 $m\to\infty$ 一致趋零。交错级数是 $a_n=(-1)^n$ 的特例。

**Abel 判别法。** 若 $\sum a_n$ 收敛，实数 $b_n$ 单调有界，则 $\sum a_nb_n$ 收敛。此时远处所有 $A_k$ 都一致小，而 $b_n$ 及其总变差有界。两判别的区别在于，Dirichlet 要求权重趋零，Abel 则利用原级数已经收敛。

**应用。** 对 $\theta\notin2\pi\mathbb Z$，几何和给出 $|\sum_{k=1}^Ne^{ik\theta}|\leq2/|1-e^{i\theta}|$。因此 $\sum e^{in\theta}/n^p$ 在 $p>0$ 时收敛；在 $p>1$ 时绝对收敛。若 $\theta$ 限制在远离 $2\pi\mathbb Z$ 的闭集，这个界一致，遂得到一致收敛；靠近共振点则不能沿用同一个常数。

## 反常积分的 Abel–Dirichlet 判别 {#app:series-ad-integral}

若 $F(x)=\int_a^xf(t)\,\mathrm dt$ 有界，$g$ 连续可微、单调趋零，则分部积分给出
\[
\int_u^vf(x)g(x)\,\mathrm dx
=(F(v)-F(u))g(v)-\int_u^v(F(x)-F(u))g'(x)\,\mathrm dx.
\]
由 $\int_u^v|g'|=|g(u)-g(v)|$ 得统一尾界，所以积分收敛。这是 Dirichlet 积分判别；单调有界变差的权重也可用 Stieltjes 积分表达。若 $\int_a^\infty f$ 本已收敛，$g$ 仅须单调有界，这给出 Abel 判别。

例如 $\int_1^\infty\sin x/x^p\,\mathrm dx$ 对所有 $p>0$ 收敛，而绝对收敛要求 $p>1$。后一个必要性可在每周期内 $|\sin x|\geq1/2$ 的固定长度子区间上比较，不能仅用 $|\sin x|\leq1$ 得到。

对 $\int_1^\infty e^{ix^\alpha}x^{-\beta}\,\mathrm dx$，其中 $\alpha>0$，先令 $t=x^\alpha$，化为 $\alpha^{-1}\int_1^\infty e^{it}t^{(1-\beta)/\alpha-1}\,\mathrm dt$。Dirichlet 判别在 $\beta>1-\alpha$ 时给出收敛；绝对收敛仍要求 $\beta>1$。相位增长速度决定抵消的强度。

## 一致收敛与逐项运算 {#app:series-uniform}

Weierstrass 判别：若 $|f_n(x)|\leq M_n$ 对所有 $x\in E$ 成立，且 $\sum M_n<\infty$，则级数绝对且一致收敛。紧区间上连续函数的一致极限连续，积分也可逐项交换。更一般的积分交换使用[控制收敛与绝对可积性](#app:integration-exchange)，不必强求一致收敛。

逐项求导需要更强条件。若 $f_n\in C^1[a,b]$，$\sum f_n(x_0)$ 在一点收敛，且 $\sum f_n'$ 一致收敛，则由
\[
f_n(x)=f_n(x_0)+\int_{x_0}^xf_n'(t)\,\mathrm dt
\]
求和可知原级数一致收敛，和函数可微，导数等于导数级数。仅有原级数一致收敛不能推出导数级数收敛。

幂级数在收敛圆内的每个较小闭圆盘上一致绝对收敛，可以任意逐项求导；边界必须另作判断。若 $\sum a_n$ 收敛，Abel 极限定理给出 $\lim_{r\uparrow1}\sum a_nr^n=\sum a_n$。证明用分部求和把表达式写成部分和的加权平均，权重非负、总质量趋于一且有限头部权重消失。它描述从圆内逼近边界的合法方式，并不保证边界级数在所有角度都收敛。
