# 常用特殊函数与渐近联系

特殊函数把反复出现的积分、微分方程或乘积封装成统一对象。使用它们的价值在于继承递推、变换与渐近公式，而非给一个未计算的积分换名字。本章只选择与竞赛常见结构直接相连的函数，并说明公式的定义域。

## Gamma 函数与阶乘 {#app:special-gamma}

对 $\operatorname{Re}z>0$，定义
\[
\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,\mathrm dt,
\qquad t^{z-1}=e^{(z-1)\log t}.
\]
零端由 $t^{\operatorname{Re}z-1}$、无穷端由指数衰减保证可积；在右半平面的紧集上，加入任意固定次 $|\log t|$ 后仍可支配，所以可对 $z$ 求导。分部积分给出 $\Gamma(z+1)=z\Gamma(z)$，且 $\Gamma(1)=1$，因此 $\Gamma(n+1)=n!$。

由 Gaussian 二重积分转极坐标，$\int_{\mathbb R}e^{-x^2}\,\mathrm dx=\sqrt\pi$，换元 $t=x^2$ 得 $\Gamma(1/2)=\sqrt\pi$。递推便计算全部正半整数值。利用递推还可将 Gamma 亚纯延拓到复平面，极点为 $0,-1,-2,\ldots$，且留数为 $(-1)^n/n!$。

**应用。** 对 $a,p>0$、$q>-1$，换元 $t=ax^p$ 得
\[
\int_0^\infty x^qe^{-ax^p}\,\mathrm dx
=\frac1p a^{-(q+1)/p}\Gamma\!\left(\frac{q+1}{p}\right).
\]
先检查 $q>-1$ 这一零端条件，再代公式；无穷端由指数统一控制。

## Beta 函数与比例变量 {#app:special-beta}

对 $a,b>0$，定义 $B(a,b)=\int_0^1t^{a-1}(1-t)^{b-1}\,\mathrm dt$。在 $\Gamma(a)\Gamma(b)$ 的正二重积分中令 $x=ru,y=r(1-u)$，Jacobian 为 $r$，由 Tonelli 得
\[
B(a,b)=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}.
\]
总量 $r=x+y$ 与比例 $u=x/(x+y)$ 的分离，也解释了概率中的一个结构：两个独立且尺度参数相同的 Gamma 随机变量，其和与比例相互独立；和仍服从 Gamma 分布，比例服从 Beta 分布。

换元 $t=x/(1+x)$ 或 $t=\sin^2\theta$ 分别得到
\[
\int_0^\infty\frac{x^{a-1}}{(1+x)^{a+b}}\,\mathrm dx=B(a,b),
\qquad
\int_0^{\pi/2}\sin^{2a-1}\theta\cos^{2b-1}\theta\,\mathrm d\theta=\frac12B(a,b).
\]
这统一了许多三角幂积分与有理幂积分。参数微分可生成对数因子，但仍需在参数紧集上验证端点支配。

当 $0<a<1$ 时，钥匙孔围道对 $z^{a-1}/(1+z)$ 的两岸相位给出 $B(a,1-a)=\pi/\sin\pi a$，于是
\[
\Gamma(a)\Gamma(1-a)=\frac\pi{\sin\pi a}.
\]
这称为反射公式，可经解析延拓推广。围道证明的关键是小圆弧 $O(\varepsilon^a)$、大圆弧 $O(R^{a-1})$ 都消失，恰对应 $0<a<1$ 的可积范围。

## Stirling 公式及其可控修正 {#app:special-stirling}

对正整数 $n$，有
\[
n!=\sqrt{2\pi n}\left(\frac ne\right)^n
\exp\!\left(\frac1{12n}+O(n^{-3})\right).
\]
主尺度可由 $\Gamma(n+1)=\int_0^\infty t^ne^{-t}\,\mathrm dt$ 的 Laplace 方法得到：令 $t=n(1+u/\sqrt n)$，指数在最大点的二次项为 $-u^2/2$，Gaussian 积分给出 $\sqrt{2\pi n}$。远离最大点的两段需用指数衰减估计。

更精细的对数形式来自对 $\log k$ 应用 Euler–Maclaurin：
\[
\log n!=\left(n+\frac12\right)\log n-n+\frac12\log(2\pi)
+\frac1{12n}-\frac1{360n^3}+O(n^{-5}).
\]
边界修正给出 $n^{-1},n^{-3}$ 系数，可积高阶导数控制余项；常数可由上述 Gaussian 极限或 Wallis 乘积确定。此处陈述固定阶展开，不声称 Bernoulli 修正级数对固定 $n$ 收敛。

**应用。** 中心二项式系数满足 $\binom{2n}{n}\sim4^n/\sqrt{\pi n}$。固定 $0<p<1$，考虑 $\binom{n}{k}p^k(1-p)^{n-k}$，令 $k=np+O(\sqrt n)$ 并展开对数，二次项产生 Gaussian 形状；这与[中心极限定理](#app:probability-limit)的局部机制一致，但完整概率极限还需控制远处尾部。

固定实数 $a,b$ 时，还有 $\Gamma(n+a)/\Gamma(n+b)=n^{a-b}(1+O(n^{-1}))$。它常用于识别乘积、矩与积分的幂次尺度；若 $a,b$ 也随 $n$ 变化，则要重新检查一致性。

## 调和数、对数导数与 Zeta 函数 {#app:special-zeta}

记 $\psi(z)=\Gamma'(z)/\Gamma(z)$。对递推取对数求导，得到 $\psi(z+1)-\psi(z)=1/z$，故 $\psi(n+1)=\psi(1)+H_n$，其中 $\psi(1)=-\gamma$。这说明调和数是阶乘连续延拓的对数导数。

对 $\operatorname{Re}s>1$，Riemann Zeta 函数定义为 $\zeta(s)=\sum_{n\geq1}n^{-s}$，级数在紧子区域上一致绝对收敛。将 $1/(e^t-1)=\sum_{n\geq1}e^{-nt}$ 积分，可得
\[
\Gamma(s)\zeta(s)=\int_0^\infty\frac{t^{s-1}}{e^t-1}\,\mathrm dt.
\]
实数 $s>1$ 时先用 Tonelli，复数情形再用绝对可积性。零端行为约为 $t^{s-2}$，所以同样要求 $\operatorname{Re}s>1$。

**应用。** 对 $m>0$，$\int_0^\infty t^m/(e^t-1)\,\mathrm dt=\Gamma(m+1)\zeta(m+1)$。特殊函数把参数依赖压缩成一个可递推、可展开的表达式。Zeta 的解析延拓及零点如何控制素数，见[素数分布](#app:primes-zeta)，其中深层结论会另行标明。

## Bessel 函数与对称微分方程 {#app:special-bessel}

二维极坐标中的 Laplacian 为 $\partial_r^2+r^{-1}\partial_r+r^{-2}\partial_\theta^2$。对 Helmholtz 方程 $\Delta u+u=0$ 分离变量，角频率 $m$ 对应径向方程
\[
r^2R''+rR'+(r^2-m^2)R=0.
\]
对非负整数 $m$，在原点正则的解可由幂级数递推定义为
\[
J_m(r)=\sum_{k=0}^\infty\frac{(-1)^k}{k!(k+m)!}\left(\frac r2\right)^{2k+m}.
\]
比值判别保证对所有复数 $r$ 收敛，逐项代入即可验证方程。它是旋转对称问题中正弦、余弦的径向对应物。

特别地，$J_0(r)=\pi^{-1}\int_0^\pi\cos(r\cos\theta)\,\mathrm d\theta$，可通过一致展开余弦并计算偶次三角积分验证。因而圆周上的平面波平均成为 $J_0$。备考中掌握定义、方程与这一积分表示已经足以识别常见情形；更完整的零点、正交性和大参数展开可查特殊函数教材，不必在单道计算题里从头重建。
