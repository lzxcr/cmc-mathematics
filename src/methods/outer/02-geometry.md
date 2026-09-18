# 几何中的度量与变分

几何计算首先要辨认所用的结构：仿射变换保持直线、平行与比例，却未必保持距离和角度；曲面的内在长度由第一基本形式决定，而它在空间中怎样弯曲还需要第二基本形式。把这些层次分清，许多坐标运算就会变成同一个恒等式的不同应用。

## 仿射变换与度量 {#app:geometry-affine}

欧氏空间中的可逆仿射变换为 $x=Ay+b$，其中 $A$ 可逆。它把直线、平面与凸组合分别映成同类对象，但原来的欧氏长度在 $y$ 坐标中变为
\[
\|x_1-x_2\|^2=(y_1-y_2)^{\mathrm T}G(y_1-y_2),
\qquad G=A^{\mathrm T}A.
\]
$G$ 是坐标的度量矩阵。只有 $G=I$ 时变换保持长度；$G=\lambda^2I$ 时所有长度按同一比例缩放，因此仍保持角度。一般仿射变换则把球映成椭球。

设椭球为
\[
(x-c)^{\mathrm T}H(x-c)=1,\qquad H=H^{\mathrm T}>0.
\]
代入 $x=Ay+b$ 后，中心变为 $A^{-1}(c-b)$，二次型矩阵变为 $A^{\mathrm T}HA$，仍正定。谱分解 $H=U\operatorname{diag}(\lambda_i)U^{\mathrm T}$ 表明其主轴方向为 $U$ 的列向量，半轴长为 $\lambda_i^{-1/2}$。反过来，$x=c+H^{-1/2}u$ 把单位球面双射到此椭球。因此“仿射像仍为椭球”同时包含必要性与充分性。[取中点形成轨迹的题目](#pr:ch08-13th-A-makeup:1) 中 $A=I/2$，轴方向不变，半轴恰好减半。

降维时同样需要记录度量。若圆柱的母线方向为 $(1,0,1)$，垂直截面的正交坐标可取
\[
u=\frac{x-z}{\sqrt2},\qquad v=y.
\]
圆的方程在这组坐标中是标准形式；若改用 $x-z$ 而忘记因子 $1/\sqrt2$，就已改变横向长度尺度。这正是[由母线和两点确定圆柱](#pr:ch05-14th-A-makeup:1) 时归一化坐标的理由。

仿射结构也解释了体积坐标。对仿射无关的 $n+1$ 个顶点 $p_0,\ldots,p_n$，任意点 $x$ 唯一写成
\[
x=\sum_{i=0}^n\lambda_i p_i,\qquad \sum_{i=0}^n\lambda_i=1.
\]
将顶点 $p_i$ 换成 $x$，相应有向体积等于原有向体积的 $\lambda_i$ 倍：这是行列式对该顶点的仿射线性，其余顶点项都产生重复列而消失。故内部点恰好对应所有 $\lambda_i>0$；任何仿射函数 $\ell$ 都满足 $\ell(x)=\sum_i\lambda_i\ell(p_i)$。[四面体的体积平衡式](#pr:ch01-17th-A:1) 便是把这些系数代回 $\sum_i\lambda_i(p_i-x)=0$。移到外部时无需更换公式，只需继续使用有向体积。

## 极化、切平面与曲面上的直线 {#app:geometry-quadric}

令 $q(x)=x^{\mathrm T}Hx$，其中 $H$ 为实对称矩阵。它对应的对称双线性型为
\[
B(u,v)=u^{\mathrm T}Hv
=\frac12\bigl(q(u+v)-q(u)-q(v)\bigr).
\]
由双线性立刻得到精确展开
\[
q(p+tv)=q(p)+2tB(p,v)+t^2q(v).
\]
这不是渐近 Taylor 展开，没有被舍去的高阶余项。它同时控制切平面、直线交点和切锥。

在二次曲面 $q(x)=c$ 的正则点 $p$，条件 $Hp\neq0$ 保证法向量非零。若曲线 $\gamma$ 落在曲面上且 $\gamma(0)=p$，对 $q(\gamma)=c$ 求导，得到 $B(p,\gamma'(0))=0$。因此切空间及切平面分别为
\[
T_pS=\{v:B(p,v)=0\},\qquad
p+T_pS=\{x:B(p,x)=c\}.
\]
这也可由隐函数定理说明是完整的切空间，而非仅一个必要条件。含线性项的二次曲面 $F(x)=x^{\mathrm T}Hx+2b^{\mathrm T}x+d=0$ 同理：将法向量改为 $Hp+b$ 即可。

切方向不一定给出曲面上的直线。由精确展开，整条 $p+tv$ 落在 $S$ 上当且仅当
\[
B(p,v)=0,\qquad q(v)=0.
\]
第一个条件消去一次项，第二个条件消去二次项。正定二次型没有非零的零方向，所以椭球上没有直线；不定二次型则可能有。对 $q=x^2+y^2-z^2$、$p=(1,1,1)$，条件变成 $a+b-c=0$、$a^2+b^2-c^2=0$，从而 $ab=0$，恰得两条母线。这解释了[求母线夹角](#pr:ch04-14th-A:1) 与[同时平行于给定平面的母线](#pr:ch06-14th-A-makeup2:1) 为什么都由切平面中的零方向决定。

同一语言还能检验平面截线是否为圆。取截平面的一组欧氏正交归一基，记其列矩阵为 $U$，写 $x=p+Uy$。限制到平面后的二次项矩阵是 $U^{\mathrm T}HU$。若它正定，消去线性项后，非退化截线为欧氏圆当且仅当
\[
U^{\mathrm T}HU=\lambda I_2\qquad(\lambda>0).
\]
若所用基不正交归一，则正确条件是 $U^{\mathrm T}HU=\lambda U^{\mathrm T}U$：应比较二次型与平面的欧氏度量，而不能只看坐标方程的两个平方项系数。

## 切锥、有限切点与分支 {#app:geometry-tangent-cone}

设 $S=\{x:q(x)=c\}$ 为正则二次曲面，顶点 $m\notin S$，记 $k=q(m)-c\neq0$。沿非零方向 $v$ 的交点参数满足
\[
q(v)t^2+2B(m,v)t+k=0.
\]
若 $q(v)\neq0$，直线在有限点相切当且仅当这个二次方程有重根，即
\[
B(m,v)^2=kq(v).
\]
这时 $B(m,v)\neq0$，切点参数为
\[
t_*=-\frac{B(m,v)}{q(v)}=-\frac{k}{B(m,v)}.
\]
若 $q(v)=0$，则判别式条件迫使 $B(m,v)=0$，交点方程反而成为 $k=0$，没有任何有限解。因此，仅写判别式为零会多收这些方向。在齐次化后的射影描述中，它们可能表现为无穷远切触；在欧氏空间的题目中仍须明确排除。

真正的有限切点 $p=m+t_*v$ 满足
\[
B(p,v)=0,\qquad B(m,p)=q(p)=c.
\]
后一式说明所有接触点都位于同一个极平面。反过来，若正则点 $p\in S$ 满足 $B(m,p)=c$，则 $v=p-m$ 为切方向；并且
\[
q(v)=q(m)-c=k\neq0.
\]
因此该直线确实以 $p$ 为二重交点，不是被误收的渐近方向。这给出了接触曲线的必要充分刻画。

若题目只允许双叶曲面的某一叶，还必须把 $p=m+t_*v$ 代回相应不等式。对[从下方定点向上半叶作切线](#pr:ch02-16th-A:1) 的题目，$k=3$，有限性要求 $B(m,v)\neq0$，而上半叶要求 $p_z\geq\sqrt2$。代数锥方程既不记录有限性，也不记录叶的选择；这两条信息应随消元一起保留。切线的方向可反向参数化，但 $p$ 不变，所以分支条件也必须对 $v\mapsto-v$ 不变。

## 从折线长到速度积分 {#app:geometry-length}

对连续曲线 $\gamma:[a,b]\to\mathbb R^n$，定义其长度为所有内接折线长的上确界：
\[
L(\gamma)=\sup_{a=t_0<\cdots<t_m=b}
\sum_{j=1}^m\|\gamma(t_j)-\gamma(t_{j-1})\|.
\]
三角不等式保证加细划分不减少折线长。这个定义只依赖曲线的遍历方式，在保向同胚重参数化下不变；还未使用任何导数。

如果 $\gamma$ 绝对连续，则 $\gamma'$ 几乎处处存在、可积，而且 $\gamma(t)-\gamma(s)=\int_s^t\gamma'(u)\,\mathrm du$。由此有
\[
L(\gamma)=\int_a^b\|\gamma'(t)\|\,\mathrm dt.
\]
上界直接来自每个子区间上的积分三角不等式。为证反向，取阶梯向量函数 $v$ 使 $\int\|\gamma'-v\|<\varepsilon$，并令 $p(t)=\gamma(a)+\int_a^tv$。$p$ 是折线，故 $L(p)=\int\|v\|$；又对每个划分应用三角不等式，得到
\[
|L(\gamma)-L(p)|\leq L(\gamma-p)
\leq\int_a^b\|\gamma'-v\|<\varepsilon.
\]
同时 $|\int\|\gamma'\|-\int\|v\||<\varepsilon$，令 $\varepsilon\to0$ 即得等式。这里使用的是 $L^1$ 逼近，不要求导数连续。

特别地，Lipschitz 函数的图像 $\gamma(t)=(t,f(t))$ 是绝对连续曲线，因而
\[
L=\int_a^b\sqrt{1+|f'(t)|^2}\,\mathrm dt.
\]
[任意细划分下的折线长极限](#pr:ch09-12th-A:6) 还说明，这个上确界确实可由所有网格足够细的划分逼近，不能只检验某一组等分划分。绝对连续性也不能省成“几乎处处可导”：Cantor 函数的图像长为 $2$，而其导数几乎处处为零，速度积分只给出 $1$。确实，把第 $n$ 步保留区间及其间隙的端点加入划分，间隙贡献水平长度 $1-(2/3)^n$，保留区间贡献至少为 $1$ 的竖直增量；而任意折线长不超过总水平变化与总竖直变化之和 $2$。缺少的正是奇异变化所贡献的长度。

对正则 $C^2$ 曲线，令 $s$ 为弧长参数，单位切向量 $T=\mathrm d\gamma/\mathrm ds$，曲率为 $\kappa=\|\mathrm dT/\mathrm ds\|$。任意参数下的空间曲线满足
\[
\kappa=\frac{\|\gamma'\times\gamma''\|}{\|\gamma'\|^3}.
\]
它测量单位弧长内切向转动的速度，而不受行进快慢影响。曲面上的曲线还可将这种转动分成沿曲面与垂直曲面的两部分，下一节的基本形式正为此服务。

## 曲面的度量、弯曲与共形坐标 {#app:geometry-surface}

设 $X:U\subset\mathbb R^2\to\mathbb R^3$ 是正则 $C^2$ 参数曲面，即 $X_u,X_v$ 线性无关。曲线上一个坐标位移 $(\mathrm du,\mathrm dv)$ 对应空间位移 $X_u\mathrm du+X_v\mathrm dv$，因此第一基本形式为
\[
\mathrm I=E\,\mathrm du^2+2F\,\mathrm du\mathrm dv+G\,\mathrm dv^2,
\qquad
E=\langle X_u,X_u\rangle,\quad
F=\langle X_u,X_v\rangle,\quad
G=\langle X_v,X_v\rangle.
\]
其矩阵 $g=(g_{ij})$ 正定，$EG-F^2>0$。曲线 $t\mapsto X(u(t),v(t))$ 的速度平方是 $g_{ij}\dot u^i\dot u^j$，角度由同一内积决定，面积元则为
\[
\mathrm dA=\|X_u\times X_v\|\,\mathrm du\mathrm dv
=\sqrt{EG-F^2}\,\mathrm du\mathrm dv.
\]
这些是曲面内在的长度、角度与面积数据；更换参数只是对 $g$ 作坐标变换。

选单位法向量 $n$，第二基本形式为 $\mathrm{II}=b_{ij}\,\mathrm du^i\mathrm du^j$，其中 $b_{ij}=\langle X_{ij},n\rangle$。由 $\langle X_i,n\rangle=0$ 求导，得
\[
\langle-\partial_i n,X_j\rangle=b_{ij}.
\]
所以形算子 $S=-\mathrm dn$ 关于第一基本形式自伴，其矩阵为 $g^{-1}b$。它的两个实特征值 $\kappa_1,\kappa_2$ 是主曲率；定义平均曲率与 Gauss 曲率为
\[
H=\frac{\kappa_1+\kappa_2}{2},\qquad K=\kappa_1\kappa_2.
\]
更换法向量使 $S,H$ 变号而 $K$ 不变。本文采用 $S=-\mathrm dn$ 的约定，因此半径 $R$ 的球面取外法向时主曲率为 $-1/R$。

若曲面上的曲线按弧长参数化，单位切向为 $T$，其加速度分解为
\[
\gamma''=D_sT+\mathrm{II}(T,T)n.
\]
这里 $D_sT$ 是空间导数在切平面上的正交投影，称为沿曲线的协变导数；$\mathrm{II}(T,T)$ 是法曲率。在正交主方向中写 $T=\cos\theta\,e_1+\sin\theta\,e_2$，便得 Euler 公式
\[
\kappa_n(\theta)=\kappa_1\cos^2\theta+\kappa_2\sin^2\theta.
\]
所以一点在所有方向上的法曲率相同，当且仅当 $S$ 是标量算子；这就是脐点条件，而不是要求某一组任意坐标中的二阶偏导恰好相等。

球极投影给出一个可直接计算的共形例子。对
\[
X(u,v)=\frac{(2u,2v,u^2+v^2-1)}{1+u^2+v^2},
\]
求导内积得到
\[
\mathrm I=\frac4{(1+u^2+v^2)^2}(\mathrm du^2+\mathrm dv^2).
\]
每个点上所有方向都乘以同一个长度因子，故保角但不保长。这为[球极投影坐标题](#pr:ch09-12th-A:1) 提供了更进一步的解释。

以下涉及度量的二阶导数时，假设参数化及坐标变换足够光滑。一般形如 $\mathrm I=e^{2\omega}(\mathrm du^2+\mathrm dv^2)$ 的坐标称为等温坐标。在这组坐标中，直接计算度量的联络系数得
\[
\Gamma^k_{ij}
=\delta_{kj}\omega_i+\delta_{ki}\omega_j-\delta_{ij}\omega_k,
\qquad
K=-e^{-2\omega}(\omega_{uu}+\omega_{vv}).
\]
第二式由第一式代入曲率定义得到，也说明 Gauss 曲率可仅由度量计算。球极投影中 $\omega=\ln2-\ln(1+u^2+v^2)$，代入即得 $K=1$。这里是在已知等温坐标后使用公式；任意光滑曲面局部存在等温坐标是另一个需要证明的定理，不能把“选择这种坐标”当作无条件的代数换元。

作为对照，圆柱取参数 $X(u,v)=(R\cos(u/R),R\sin(u/R),v)$，则 $\mathrm I=\mathrm du^2+\mathrm dv^2$，局部与平面等距，故 $K=0$；它的两个主曲率却是 $-1/R,0$。这说明“在空间中弯曲”与“内在度量有曲率”并不是同一个概念。

## 第一变分、测地线与极小图形 {#app:geometry-variation}

固定时间区间 $[a,b]$，曲面上的光滑曲线 $\gamma$ 有长度与能量
\[
L(\gamma)=\int_a^b\|\dot\gamma\|\,\mathrm dt,
\qquad
\mathcal E(\gamma)=\frac12\int_a^b\|\dot\gamma\|^2\,\mathrm dt.
\]
长度与保向重参数化无关，能量则还衡量行进速度是否均匀。Cauchy–Schwarz 不等式给出 $\mathcal E\geq L^2/[2(b-a)]$，等号当且仅当速度恒定。因此用恒速参数时，最短曲线也使能量最小；能量的平方形式更便于变分。

设 $\gamma_\varepsilon$ 是固定端点的光滑变分，变分向量 $V=\partial_\varepsilon\gamma_\varepsilon|_{\varepsilon=0}$ 沿曲面切向，且两端为零。对能量求导并分部积分得
\[
\left.\frac{\mathrm d}{\mathrm d\varepsilon}
\mathcal E(\gamma_\varepsilon)\right|_{\varepsilon=0}
=\int_a^b\langle D_tV,\dot\gamma\rangle\,\mathrm dt
=-\int_a^b\langle V,D_t\dot\gamma\rangle\,\mathrm dt.
\]
因任意紧支撑切向场都可局部实现为变分，能量驻值的条件恰为 $D_t\dot\gamma=0$，称为测地线方程。对空间中的曲面，它等价于 $\ddot\gamma$ 处处沿曲面法向。该条件还给出 $(\|\dot\gamma\|^2)'=0$，所以此处测地参数自动恒速；任意非恒速重参数化则应改用弧长表述。

坐标形式为
\[
\ddot u^k+\Gamma^k_{ij}\dot u^i\dot u^j=0,
\qquad
\Gamma^k_{ij}=\frac12g^{k\ell}
(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij}).
\]
这些系数描述了坐标基沿曲面变化所需的修正。计算题若有几何模型，应先利用模型：圆柱展开为平面后，测地线成为直线，卷回去便是母线、平行圆或一般螺旋线；球面上的单位速测地线满足 $\gamma''=-\gamma/R^2$，因而落在一个过球心的平面上，即大圆。

测地线是局部驻值路径，并不自动是任意两端点间的全局最短路径。球面大圆上长于半周的弧就不是最短弧；圆柱上不同绕行次数对应展开平面中的不同端点副本，必须比较各段直线长度才能确定全局最短路径。写出微分方程解决的是驻值条件，不能替代这一步比较。

曲面的面积变分有类似结构。在固定边界的法向变分 $X_\varepsilon=X+\varepsilon\phi n$ 下，$\phi$ 在边界为零，度量的一阶变化为 $\dot g_{ij}=-2\phi b_{ij}$。用行列式求导公式得到
\[
\left.\frac{\mathrm d}{\mathrm d\varepsilon}\operatorname{Area}(X_\varepsilon)
\right|_{\varepsilon=0}=-2\int H\phi\,\mathrm dA.
\]
故面积驻值的条件是 $H=0$，称为极小曲面。其名称表达的是变分方程；一般曲面的全局面积最小性仍需另外证明。

对图形 $X(x,y)=(x,y,u(x,y))$，面积泛函为
\[
\mathcal A(u)=\int_\Omega\sqrt{1+|\nabla u|^2}\,\mathrm dx\mathrm dy.
\]
固定边界值，对 $u+\varepsilon\eta$ 求导并分部积分，驻值方程为
\[
\operatorname{div}\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}=0,
\]
即 $(1+u_y^2)u_{xx}-2u_xu_yu_{xy}+(1+u_x^2)u_{yy}=0$。它等价于图形平均曲率为零。在有界区域上，对具有相同边界值的光滑图形，积分核关于梯度凸；将凸性的一阶支撑不等式积分，并使用上式，便进一步得到 $\mathcal A(v)\geq\mathcal A(u)$。这里确能从驻值推出最小性，原因是图形面积泛函的凸结构，而非“第一变分为零”本身。
