\sectioncounter{25}
</p>

<p>
\section{复数及其计算}
</p>

<p>
\subsection{知识梳理}
设方程 $x^2=-1$ 的解为 $\mathrm{i}$, 则 $\mathrm{i}^2=-1$. 
并称 $\mathrm{i}$ 为虚数单位, 而形如 $x+y\mathrm{i}$ 
($x$,$y\in\mathbb{R}$, $y\neq0$) 的数称为虚数, 记其为 $z$, 
其中实数 $x$ 为 $z$ 的实部, 实数 $y$ 为 $z$ 的虚部. 
实数和虚数统称为复数. 对复数 $z=x+\mathrm{i}y$ ($x$,$y\in\mathbb{R}$),
当 $y=0$ 时, $z$ 为实数; 当 $y\neq0$ 时, $z$ 为虚数, 
若还有 $x=0$, 则称 $z$ 为纯虚数. 两个复数相等规定为它们的实部和虚部分别相等, 如对 $x$,$y\in\mathbb{R}$, $x+\mathrm{i}= 3+\mathrm{i}y$ 等价于
$x=3$, $y=1$.
</p>

<p>
借用平面直角坐标系可以用点表示复数 $z=x+\mathrm{i}y$, 规定 $z$ 对应点 $(x,y)$, 此时的平面也称为复平面. 由此可知, $1+2\mathrm{i}$ 的对应点在第一象限, $2\mathrm{i}-1$ 的对应点在第二象限. $x$ 轴上的点全为实数, 所以称其为实轴; $y$ 轴上的点除原点外全为纯虚数, 所以称其为虚轴. $z$ 的对应点到原点的距离称为 $z$ 的模 (模长), 记作 $|z|$. 勾股定理表明, $|z|=\sqrt{x^2+y^2}$, 所以 $|z|=1$ 表示单位圆. 结合模的定义, $|z-(1+2\mathrm{i})|=3$ 表示以 $(1,2)$ 为圆心, $3$ 为半径的圆. 为了后续运算方便, 还定义 $z$ 的共轭复数 $\bar{z}= x-\mathrm{i}y$. 由定义, $z$ 与 $\bar{z}$ 关于实轴对称. 类似地, $z$ 关于虚轴的对称点为 $-x+\mathrm{i}y$.
</p>

<p>
复数的四则运算可以认为是关于 $\mathrm{i}$ 的多项式的四则运算, 
只不过运算结果中的 $\mathrm{i}^2$ 要化为 $-1$. 
例如, 若 $z_1=1+2\mathrm{i}$, $z_2=2+3\mathrm{i}$, 则
\begin{gather*}
    z_1+z_2= 3+5\mathrm{i},\quad z_1-z_2= -1-\mathrm{i},\\
    z_1z_2= 2+7\mathrm{i}+6\mathrm{i}^2= -4+7\mathrm{i},\\
    z_1\bar{z}_1= 1-4\mathrm{i}^2=5.
\end{gather*}
可以看出, 复数的加减运算同向量的坐标运算十分相似. 上面最后一式一般化就是 $z\bar{z}=x^2+y^2=|z|^2$. 由此可得
\[\frac{z_1}{z_2}= \frac{z_1\overline{z_2}}{|z_2|^2}
    = \frac{1}{13}(1+2\mathrm{i})(2-3\mathrm{i})
    = \frac1{13}(7+\mathrm{i}),\]
也就是复数的除法运算的第一步是利用共轭复数将分母实数化.
还可以利用共轭复数或直接计算验证复数的模满足如下性质 (与实数的情形一致)
\[|z_1z_2|=|z_1||z_2|,\quad
    \Big|\frac{z_1}{z_2}\Big|= \frac{|z_1|}{|z_2|}\ (z_2\neq0).\]
</p>

<p>
\lianxi
<myexercise>
    <p>    设 $\mathrm{i}$ 是虚数单位, 计算: $\mathrm{i}(1+\mathrm{i})$, $(1+2\mathrm{i})(1-\mathrm{i})^2$.
</p>
</myexercise>
<mysolution>
    <p>
    前者为 $-1+\mathrm{i}$, 后者为
    \[(1+2\mathrm{i})(-2\mathrm{i})= 4-2\mathrm{i}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若复数 $(m^2 +m)+(m^2-2m-3)\mathrm{i}$ ($m\in\mathbb{R}$) 是纯虚数,
    求 $m$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[\left\{\!\!\begin{array}{l}
        m^2 +m=0,\\
        m^2-2m-3\neq 0,
    \end{array}\right.\ \text{解得}\ m=0.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若复数 $z$ 满足 $(z-2)\mathrm{i}= 4+\mathrm{i}$ ($\mathrm{i}$ 为虚数单位), 求 $z$ 的模.
</p>
</myexercise>
<mysolution>
    <p>
    先解出 $z$, 
    \[z-2= \frac{4+\mathrm{i}}{\mathrm{i}}= 1- 4\mathrm{i},\]
    则 $z= 3-4\mathrm{i}$, 而 $|z|= 5$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知复数 $z=\dfrac{\sqrt3+\mathrm{i}}{1-\sqrt3\mathrm{i}}$, 
    $\bar{z}$ 是 $z$ 的共轭复数, 求 $z\bar{z}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $z\bar{z}= |z|^2= \dfrac{|\sqrt3+ \mathrm{i}|^2}{|1- \sqrt3\mathrm{i}|^2}= 1$.
    \mymarginpar{此题无需化简 $z$.}
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求满足方程 $(x+y)+ 2xy\mathrm{i}= 7+24\mathrm{i}$ 的实数对 $(x,y)$.
</p>
</myexercise>
<mysolution>
    <p>
    由复数相等的定义, $x+y=7$, $2xy=24$, 故 $(x,y)= (3,4)$ 或 $(4,3)$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{复数的概念及四则运算法则}
<span id="example-"></span>
<myexample>
    <p>
    设复数 $z=(1+\mathrm{i})m^2+ (5-2\mathrm{i})m+ 6-15\mathrm{i}$, $m\in\mathbb{R}. $当 $z$ 分别为实数、虚数和纯虚数时, 求相应的 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    先整理出 $z$ 的虚部与实部,
    \[\begin{aligned}
        z&= m^2+5m+6+ (m^2-2m-15)\mathrm{i}\\
        &= (m+2)(m+3)+ (m+3)(m-5)\mathrm{i}.
    \end{aligned}\]
    当 $z$ 为实数时, 虚部为 $0$, 即 $m= -3$ 或 $5$. 当 $z$ 为虚数时, 虚部不为 $0$, 即 $m\neq -3$ 和 $5$. 当 $z$ 为纯虚数时, 实部为 $0$ 且虚部不为 $0$, 即 $m= -2$. 
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知复数 $z_1$ 满足 $(z_1-2)(1+\mathrm{i})=1-\mathrm{i}$ ($\mathrm{i}$ 为虚数单位), 复数 $z_2$ 的虚部为 $2$, $z_1\cdot z_2$ 是实数, 求 $z_2$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    先解已知方程,
    \[z_1-2= \frac{1-\mathrm{i}}{1+\mathrm{i}}= -\mathrm{i},
        \quad\text{即}\quad z_1= 2-\mathrm{i}.\]
    由题意设 $z_2= x+2\mathrm{i}$, $x\in\mathbb{R}$, 则
    \mymarginpar{可以证明: 若 $z_1z_2$ 为非零实数, 则 $z_1= k\overline{z_2}$, 其中实数 $k$ 由 $z_1$, $z_2$ 唯一确定.}
    \[z_1z_2= (2-\mathrm{i})(x+2\mathrm{i})
        = 2x+2+ (4-x)\mathrm{i}.\]
    由 $z_1z_2$ 为实数知, $4-x=0$, 即 $x=4$, 所以 $z_2= 4+2\mathrm{i}$.
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    设复数 $z_1 =2-\mathrm{i}$, $z_2= m+\mathrm{i}$ ($m\in\mathbb{R}$, $\mathrm{i}$ 为虚数单位). 若 $z_1z_2$ 为实数, 求 $m$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由题意, 
    \[z_1z_2= (2-\mathrm{i})(m+\mathrm{i})
        = 2m+1+ (2-m)\mathrm{i},\]
    则 $2-m=0$, 即 $m=2$.
</p>

<p>
    方法二: 直接利用上例的注, $z_2= k\overline{z_1}$, $k\in\mathbb{R}$, 对比实部和虚部知只能 $m=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若复数 $(1+\mathrm{i})^2 =a+b\mathrm{i}$ ($a$, $b$ 是实数, $\mathrm{i}$ 是虚数单位), 求 $a$, $b$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    左边展开为 $2\mathrm{i}$, 故 $a=0$, $b=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知复数 $z$ 满足 $\mathrm{i}z= 1+\mathrm{i}$ ($\mathrm{i}$ 为虚数单位), 求 $|z|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $z= \dfrac{1+\mathrm{i}}{\mathrm{i}}$ 知, $|z|= \dfrac{|1+\mathrm{i}|}{|\mathrm{i}|}= \sqrt2$.
</p>
</mysolution>
</p>

<p>
\subsubsection{复数的几何意义}
<span id="example-"></span>
<myexample>
    <p>
    设 $z\in\mathbb{C}$, 若 $z^2$ 为纯虚数, 求 $z$ 在复平面上的对应点坐标满足的方程.
</p>
</myexample>
<mysolution>
    <p>
    设 $z= x+\mathrm{i}y$, $x$, $y\in\mathbb{R}$, 则
    \[z^2= x^2-y^2+ 2xy\mathrm{i}.\]
    由 $z^2$ 为纯虚数知, $x^2-y^2=0$ 且 $xy\neq 0$.
    \mymarginpar{结论里的两个方程表明, 对应点在直线 $y= \pm x$ 上 (不含原点).}
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    求满足等式 $|z-\mathrm{i}|+|z+\mathrm{i}|=3$ 的复数 $z$ 对应点的轨迹.
</p>
</myexercise>
<mysolution>
    <p>
    已知等式表示 $z$ 到 $\mathrm{i}$ 和 $-\mathrm{i}$ 的距离之和为 $3$, 而 $3> |\mathrm{i}- (\mathrm{i})|$, 所以所求轨迹为椭圆.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    化简: $\dfrac{1+2\mathrm{i}}{(1-\mathrm{i})^2}$.
</p>
</myexercise>
<mysolution>
    <p>
    原式 $= \dfrac{1+2\mathrm{i}}{-2\mathrm{i}}= -1+\dfrac{\mathrm{i}}2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求复数 $z= (1+2\mathrm{i})^2$ 的共轭复数 $\bar{z}$.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $z= -3+4\mathrm{i}$, 所以 $\bar{z}= -3-4\mathrm{i}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若复数 $z$ 满足 $\mathrm{i}z=2+4\mathrm{i}$, 求复平面内 $z$ 的对应点的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    $z= 4-2\mathrm{i}$, 对应点 $(4,-2)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在复平面内, 复数 $z= \dfrac{5\mathrm{i}}{2+\mathrm{i}}$ 的对应点位于第几象限?
</p>
</myexercise>
<mysolution>
    <p>
    计算可得
    \[z= \mathrm{i}(2-\mathrm{i})= 1+2\mathrm{i},\]
    对应点 $(1,2)$ 在第一象限.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    已知 $\mathrm{i}$ 是虚数单位, 计算 $(2+\mathrm{i})(3+\mathrm{i})$.
</p>
</myexercise>
<mysolution>
    <p>
    展开得 $5+5\mathrm{i}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $z_1= 3-2\mathrm{i}$, $z_2= 1+a\mathrm{i}$ ($a\in\mathbb{R}$). 若 $z_1z_2$ 为实数, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 直接计算,
    \[z_1z_2= 3+2a+ (3a-2)\mathrm{i},\]
    所以 $3a-2=0$, 即 $a= \dfrac23$.
</p>

<p>
    方法二: 也可写出 $z_2= k\overline{z_1}$, $k\in\mathbb{R}$, 即
    \[1+a\mathrm{i}= k(3+2\mathrm{i}),\]
    对比可得 $k= \dfrac13$, $a= 2k= \dfrac23$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若复数 $z_1=\dfrac{(2-\mathrm{i})^2}{\mathrm{i}}$, $z_2= \dfrac{1+3\mathrm{i}}{1-\mathrm{i}}$ ($\mathrm{i}$ 为虚数单位), 求 $|z_1|$, $|z_2|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $|z_1|= \dfrac{|2-\mathrm{i}|^2}{|\mathrm{i}|}= 5$, 而
    \[|z_2|= \dfrac{|1+3\mathrm{i}|}{|1-\mathrm{i}|}
        = \frac{\sqrt{10}}{\sqrt{2}}= \sqrt{2}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知复数 $z_1 =1+3\mathrm{i}$, $z_2 =3+\mathrm{i}$ ($\mathrm{i}$ 为虚数单位), 求 $z_1z_2$, $\dfrac{z_1}{z_2}$ 在复平面的对应点.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $z_1z_2= 10\mathrm{i}$, 
    \[\dfrac{z_1}{z_2}= \frac{1+3\mathrm{i}}{3+\mathrm{i}}
        = \frac{(1+3\mathrm{i})(3-\mathrm{i})}{10}
        = \frac35+ \frac45\mathrm{i},\]
    所以 $z_1z_2$ 对应点 $(0,10)$, $\dfrac{z_1}{z_2}$ 对应点 $\Bigl(\dfrac35, \dfrac45\Bigr)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若复数 $z=\dfrac{2-b\mathrm{i}}{3+\mathrm{i}}$ ($b\in\mathbb{R}$) 的实部与虚部互为相反数, 求实数 $b$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $z$ 化为
    \[\frac1{10}(2-b\mathrm{i})(3-\mathrm{i})
        = \frac1{10}[6-b- (2+3b)\mathrm{i}],\]
    已知表明 $6-a= 2+3b$, 解得 $b=1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\dfrac{1+m\mathrm{i}}{\mathrm{i}}= 1+n\mathrm{i}$ ($m$, $n\in\mathbb{R}$, $\mathrm{i}$ 为虚数单位), 求 $mn$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    已知式化为
    \[1+m\mathrm{i}= \mathrm{i}(1+n\mathrm{i})= -n+\mathrm{i},\]
    所以 $m=1$, $n=-1$, 而 $mn=-1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $a$, $b\in\mathbb{R}$, $\mathrm{i}$ 是虚数单位. 若 $(a+\mathrm{i})(1+\mathrm{i})=b\mathrm{i}$, 求 $a+b\mathrm{i}$ 在复平面的对应点.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[a-1+(a+1)\mathrm{i}= b\mathrm{i},\]
    则 $a=1$, $b= a+1= 2$, 所以 $a+b\mathrm{i}= 1+2\mathrm{i}$ 对应点 $(1,2)$. 
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知复数 $(2k^2 -3k-2)+(k^2-k)\mathrm{i}$ 在复平面内对应的点在第二象限, 求实数 $k$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $2k^2-3k-2< 0$ 且 $k^2-k>0$, 解得
    \[k\in \Bigl(-\frac12,0\Bigr)\cup (1,2).\]
</p>
</mysolution>