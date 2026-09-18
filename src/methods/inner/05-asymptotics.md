# 渐近估计与尺度选择 {#app:estimates}

分析估计首先识别控制变化的尺度，再选择在这一尺度上有效的界。余项必须服从最终操作：求和要可累积，积分要一致可积，求极值要一致小。本章从振幅与导数的平衡出发，再讨论缩放、紧性、递推与积分集中。

## 振幅与局部导数的两尺度估计 {#app:estimate-holder}

同一个量有两个上界时，应保留其中较小者。若 $Q\le A r^a$ 且 $Q\le B d r^{-c}$，其中 $a,c,A,B,d,r>0$，则
\[
Q\le\min\{A r^a,Bd r^{-c}\}
\le A^{c/(a+c)}B^{a/(a+c)}d^{a/(a+c)}.
\]
第二步是 $\min(U,V)\le U^\theta V^{1-\theta}$，取 $\theta=c/(a+c)$ 消去 $r$。等价地，解平衡方程 $A r^a=Bd r^{-c}$ 得到临界尺度。若两个界只在不同区域成立，就按这一尺度分区，分别使用各自有效的估计。

**振幅—导数准则。** 设 $a,b>0$，$u\in C[0,1]$，且 $u$ 在每个 $[\varepsilon,1]$ 上绝对连续。若存在常数 $A,B\ge0$，使
\[
|u(t)-u(0)|\le At^a,\qquad
|u'(t)|\le Bt^{a-b-1}\quad\text{几乎处处于 }(0,1),
\]
则存在与 $x,y$ 无关的常数 $C$，使
\[
|u(y)-u(x)|\le C|y-x|^\gamma,
\qquad \gamma=\min\left\{1,\frac a{b+1}\right\}.
\]

当 $a\ge b+1$ 时，$|u'|\le B$；先在 $0<x<y$ 上积分，再令 $x\downarrow0$，即得 Lipschitz 估计。设 $0<a<b+1$，记 $d=y-x$、$r=d^{1/(b+1)}$。对 $0\le x<y\le1$，有 $d\le r$。若 $x\le r$，则 $y\le2r$，振幅界给出
\[
|u(y)-u(x)|\le A(x^a+y^a)
\le A(1+2^a)r^a.
\]
若 $x>r$，则因 $a-b-1<0$，局部绝对连续性给出
\[
|u(y)-u(x)|\le B\int_x^yt^{a-b-1}\,\mathrm dt
\le Bd\,x^{a-b-1}\le Bd\,r^{a-b-1}.
\]
两者都是 $C d^{a/(b+1)}$。这里导数允许在零点附近不可积：靠近零点的一段已由振幅控制，无须跨过奇点积分。

**快速振荡的最优指数。** 对 $a,b>0$，令
\[
F_{a,b}(0)=0,\qquad F_{a,b}(x)=x^a\sin(x^{-b})\quad(0<x\le1).
\]
由 $|F_{a,b}(x)|\le x^a$ 及
\[
|F_{a,b}'(x)|
\le a x^{a-1}+b x^{a-b-1}
\le(a+b)x^{a-b-1},
\]
上述准则给出指数 $\gamma=\min\{1,a/(b+1)\}$，且端点指数本身可取。它也是最大的统一两点指数：若 $a<b+1$，取
\[
x_n=(2\pi n+\pi/2)^{-1/b},\qquad
y_n=(2\pi n+3\pi/2)^{-1/b}.
\]
两点的正弦值分别为 $1,-1$。于是
\[
|F_{a,b}(x_n)-F_{a,b}(y_n)|\asymp n^{-a/b},
\qquad |x_n-y_n|\asymp n^{-(b+1)/b},
\]
其中第二式由 $t\mapsto t^{-1/b}$ 的中值定理得到；符号 $\asymp$ 表示比值被两个正常数夹住。因此任意 $\beta>a/(b+1)$ 都使 Hölder 商趋于无穷。若 $a\ge b+1$，指数已经达到 $1$；区间上满足 $|u(y)-u(x)|\le C|y-x|^\beta$、$\beta>1$ 的函数必为常数，因为把 $[x,y]$ 等分为 $N$ 段后，右侧的总和是 $C|y-x|^\beta N^{1-\beta}\to0$。$F_{a,b}$ 非常数，故不能再提高指数。

这一区别属于两点几何：距零点约 $x$ 处，振幅为 $x^a$，一次振荡的距离为 $x^{b+1}$，两者决定统一指数。只与零点比较则有 $|F_{a,b}(x)|\le x^a$，并由正弦取值为 $1$ 的序列知这一幂次不能提高；这并不意味着任意两点都满足 $a$ 阶估计。上述结论限于 $[0,1]$；扩展到无界区间还须单独控制无穷远处的增长。

## 导数积分与连续模 {#app:estimate-derivative}

对一般函数，直接对导数积分使用 Hölder 不等式是系统方法，但前提是函数的增量能由导数积分恢复。设 $u$ 在有限闭区间 $I$ 上绝对连续，$u'\in L^p(I)$，$1<p<\infty$。则对 $x<y$，
\[
\begin{aligned}
|u(y)-u(x)|
&=\left|\int_x^yu'(t)\,\mathrm dt\right|\\
&\le |y-x|^{1-1/p}
\left(\int_x^y|u'(t)|^p\,\mathrm dt\right)^{1/p}
\le\|u'\|_{L^p(I)}|y-x|^{1-1/p}.
\end{aligned}
\]
这就是一维 Morrey 估计，即 $W^{1,p}(I)$ 的绝对连续代表属于 $C^{0,1-1/p}(I)$。$p=\infty$ 时直接得到 Lipschitz 界；特别地，$p=2$ 给出指数 $1/2$。绝对连续性不能只换成“几乎处处可导”：Cantor 函数的导数几乎处处为零，却不是常数。

$p=1$ 时仍有连续模
\[
\omega_u(h):=\sup_{\substack{x,y\in I\\|x-y|\le h}}|u(x)-u(y)|
\le\sup_{\substack{J\subset I\ \text{为区间}\\|J|\le h}}
\int_J|u'(t)|\,\mathrm dt\longrightarrow0,
\]
最后一步是 Lebesgue 积分的绝对连续性；但一般不能得到正的幂次。例如 $u(0)=0$、$u(x)=1/\log(e/x)$（$0<x\le1$）的导数为 $1/[x\log^2(e/x)]\in L^1(0,1)$，且 $u(x)=\int_0^xu'(t)\,\mathrm dt$；然而对每个 $\alpha>0$，$u(x)/x^\alpha\to\infty$。

**何时应改用分区估计。** 对 $f(x)=x\sin(1/x)$，
\[
f'(x)=\sin(1/x)-\frac{\cos(1/x)}x,
\qquad
\int_0^1\frac{|\cos(1/x)|}{x}\,\mathrm dx
=\int_1^\infty\frac{|\cos t|}{t}\,\mathrm dt=\infty.
\]
最后一个积分在每段周期上的贡献与 $1/n$ 同阶，而 $\sin(1/x)$ 在 $(0,1)$ 上绝对可积，故 $f'\notin L^1(0,1)$，也不属于任何 $L^p(0,1)$（$p>1$）。因此不能在包含零点的区间上直接套用上述估计。对 $x>0$，在 $[x,y]$ 上积分完全合法；再与近零点的振幅界配合，上一节仍能给出最优的 $1/2$ 阶估计。导数的积分范数提供方便的充分条件，振幅与局部尺度则能保留它看不到的振荡抵消。

## 缩放、紧性与极值扰动 {#app:estimate-scaling}

齐次结构提示先把变化的区域缩放到固定集合。例如 $F(Ru)=R^mP(u)+R^{m-1}Q(u)$，除以 $R^m$ 后只剩 $P+\varepsilon Q$，其中 $\varepsilon=R^{-1}$。这一步把“无穷远问题”变成紧集上的小扰动问题。

设 $K$ 是非空紧集，$P,Q$ 连续，$M=\max_KP$，$E=\{u\in K:P(u)=M\}$。则当 $\varepsilon\downarrow0$ 时，
\[
\max_K(P+\varepsilon Q)=M+\varepsilon\max_EQ+o(\varepsilon).
\]
证明体现两层选择。取极大点 $u_\varepsilon$，与 $E$ 中使 $Q$ 最大的点比较，利用 $Q$ 有界先得 $P(u_\varepsilon)\to M$；故 $u_\varepsilon$ 的每个聚点都在 $E$。又有
\[
\max_EQ\leq\frac{\max_K(P+\varepsilon Q)-M}{\varepsilon}
\leq Q(u_\varepsilon).
\]
右侧的上极限不超过 $\max_EQ$，结论随之成立。极小值同理，只需同时把两个最大值改为最小值。

若另有一致余项 $r_\varepsilon$，满足 $\sup_K|r_\varepsilon|=o(\varepsilon)$，结论不变。这里“一致”不能删去：极值点本身随参数移动，点态余项无法控制它。主项负责选出候选集，次项再在候选集中选点；这也解释了为何只比较最高次项不足以求出次阶极限。

## 递推的坐标选择与累积误差 {#app:estimate-recursion}

设正数列已知趋于零，且
\[
x_{n+1}=x_n-cx_n^{1+\alpha}+o(x_n^{1+\alpha}),\qquad c,\alpha>0.
\]
增量在原坐标中不断缩小。选择 $y_n=x_n^{-\alpha}$，由 $(1-u)^{-\alpha}=1+\alpha u+o(u)$ 得
\[
y_{n+1}-y_n\longrightarrow\alpha c.
\]
将差分求和并取 Cesàro 平均，得到 $y_n/n\to\alpha c$，即
\[
x_n\sim(\alpha cn)^{-1/\alpha}.
\]
坐标选择可由连续模型 $x'=-cx^{1+\alpha}$ 预见，但严格证明仍是离散差分求和。应先独立证明正性、轨道留在所需区间以及 $x_n\to0$，再使用局部展开。

若需要下一阶，应继续研究变换后的增量。例如 $y_{n+1}-y_n=A+B/y_n+O(y_n^{-2})$ 且 $y_n\sim An$、$A>0$ 时，先求得 $y_n=An+O(\log n)$，代回后便有
\[
y_n=An+\frac BA\log n+O(1).
\]
原因是 $1/y_n-1/(An)=O(\log n/n^2)$ 可求和，而 $\sum_{k<n}1/k=\log n+O(1)$。局部误差必须经过求和审查：每步 $o(1)$ 只保证总误差 $o(n)$，不能自动得到有界总误差。


## Laplace 方法：质量集中与二次尺度 {#app:estimate-laplace}

设 $\phi\in C^2[a,b]$ 在内部点 $x_0$ 有唯一最大值，$\phi''(x_0)<0$，$a(x)$ 连续且 $a(x_0)\neq0$。则
\[
\int_a^ba(x)e^{n\phi(x)}\,\mathrm dx
\sim a(x_0)e^{n\phi(x_0)}
\sqrt{\frac{2\pi}{n|\phi''(x_0)|}}.
\]
证明先在 $x_0$ 的固定邻域外用紧性得到 $\phi\leq\phi(x_0)-\eta$，这部分指数级小；邻域内令 $x=x_0+u/\sqrt n$，二阶 Taylor 模型成为 $e^{-cu^2/2}$。由 $\phi(x)-\phi(x_0)\leq-c_1(x-x_0)^2$ 给出可积 Gaussian 支配，再控制缩放区间外的尾部，才可合法取极限。

这解释了 $n^{-1/2}$ 从何而来：指数中 $n(x-x_0)^2$ 保持常数量级的窗口宽度正是 $n^{-1/2}$。若最高点退化为 $\phi(x)=\phi(x_0)-c|x-x_0|^m+o(|x-x_0|^m)$，局部尺度相应变成 $n^{-1/m}$；若最大值落在端点且一阶导数非零，尺度通常为 $n^{-1}$。

**应用。** $\int_0^1[x(1-x)]^n\,\mathrm dx$ 的最大点为 $1/2$。对 $\phi=\log(x(1-x))$，有 $\phi(1/2)=-\log4$、$\phi''(1/2)=-8$。由于 $\phi$ 在端点不光滑，先固定 $0<\delta<1/2$，在 $[\delta,1-\delta]$ 上应用上述结论；两个端点区间的总贡献至多为 $2\delta[\delta(1-\delta)]^n$，相对于主项指数级小。因此原积分等价于 $4^{-n}\sqrt\pi/(2\sqrt n)$。也可用 Beta 函数与 Stirling 公式核对，见[特殊函数](#app:special-beta)。两种方法分别从局部集中和精确恒等式解释同一个尺度。

## 尾部渐近与 Watson 型展开 {#app:estimate-watson}

设 $a$ 在 $[0,\infty)$ 上可测且局部可积，$a(t)=\sum_{k=0}^mc_kt^k+O(t^{m+1})$ 在 $0\leq t\leq\delta$ 成立，并存在常数 $C>0$、$c\geq0$、$T\geq\delta$，使 $|a(t)|\leq Ce^{ct}$ 对所有 $t\geq T$ 成立。则当 $x\to+\infty$ 时
\[
\int_0^\infty e^{-xt}a(t)\,\mathrm dt
=\sum_{k=0}^m\frac{c_kk!}{x^{k+1}}+O(x^{-m-2}).
\]
证明将积分在 $\delta$ 处分开；近端余项的绝对值由 $C\int_0^\infty e^{-xt}t^{m+1}\,\mathrm dt$ 控制。有限中段 $[\delta,T]$ 由局部可积性控制，无穷尾段由上述指数增长界控制，两者都指数级小。分数幂 $t^{\alpha+k-1}$（$\alpha>0$）同理产生 $\Gamma(\alpha+k)x^{-\alpha-k}$。这是 Watson 引理的一种常用形式。

**应用。** 换元 $t=x+u$ 后，Gaussian 尾为
\[
\int_x^\infty e^{-t^2}\,\mathrm dt
=e^{-x^2}\int_0^\infty e^{-2xu-u^2}\,\mathrm du
=\frac{e^{-x^2}}{2x}\left(1-\frac1{2x^2}+O(x^{-4})\right).
\]
在近端展开 $e^{-u^2}$，远端用指数衰减控制。若只需上界，直接由 $t/x\geq1$ 得 $\int_x^\infty e^{-t^2}\,\mathrm dt\leq e^{-x^2}/(2x)$；无需使用完整展开。

## 分区估计与一致参数 {#app:estimate-split}

遇到奇点、端点或移动峰，先把区域分成不同机制成立的部分。典型次序是：固定一个小邻域；在邻域内缩放并控制模型余项；在补集证明统一衰减；最后让邻域大小趋零。若把邻域大小过早设成 $n$ 的函数，容易把本来只对固定区域成立的估计误当作一致估计。

**反例提示。** $f_n(x)=n\mathbf1_{(0,1/n)}(x)$ 几乎处处趋零，积分却恒为 $1$。任何在每个固定 $x>0$ 处成立的展开，都看不到靠近零的主贡献。这正说明局部尺度与积分极限必须一起设计。实际计算中，可以先用图像或量纲猜尺度，但最后应写出支配、尾界或显式误差中的至少一种。
