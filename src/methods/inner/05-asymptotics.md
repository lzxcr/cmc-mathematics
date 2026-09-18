# 渐近估计与尺度选择 {#app:estimates}

渐近分析首先识别主尺度，再控制在这一尺度下被舍去的部分。余项必须服从最终操作：求和要可累积，积分要一致可积，求极值要一致小。本章从紧性、递推和积分集中三个角度说明这种控制。

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
