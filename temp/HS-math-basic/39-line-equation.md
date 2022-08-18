\sectioncounter{38}
</p>

<p>
\section{直线的斜率与方程}
</p>

<p>
\subsection{知识梳理}
在平面直角坐标系中, 直线的斜率定义为其上两点间纵坐标与横坐标增量的比值. 具体地, 取直线 $l$ 上两点 $A(x_A,y_A)$,$B(x_B,y_B)$, 则 $l$ 的斜率 
\[k=\dfrac{y_A-y_B}{x_A-x_B}.\]
从定义可知, 竖直的直线没有斜率 (或斜率为 $\infty$), 水平的直线斜率为 $0$, 且斜率为正表示直线对应的函数单调增, 而斜率为负则表示直线对应的函数单调减. 直线的倾斜角定义为直线向上的方向与 $x$ 轴正向的夹角, 取值范围是 $[0^\circ,180^\circ)$. 设直线 $l$ 斜率为 $k$, 倾斜角为 $\alpha$, 则由正切和斜率的定义可知 $k=\tan\alpha$.
</p>

<p>
直线与 $x$ 轴交点的横坐标为直线的横截距, 类似地可定义纵截距. 注意, 截距是坐标而不是距离, 所以取值可正可负. 如直线 $y=x+1$ 的横截距为 $-1$, 纵截距为 $1$, 而说直线 $l$ 的横截距为 $3$, 纵截距为 $2$ 是指 $l$ 过点 $(3,0)$ 和 $(0,2)$.
</p>

<p>
两点确定一条直线, 确定直线方程通常需要两个条件. 直线方程常见的形式如下:
\[\begin{aligned}
    &\text{点斜式:\ }y-y_0=k(x-x_0),\quad
     \text{斜截式:\ }y=kx+b,   \\
    &\text{两点式:\ }\frac{y-y_1}{y_2-y_1}= \frac{x-x_1}{x_2-x_1},\quad
     \text{截距式:\ }\frac{x}{a}+ \frac{y}{b}= 1,\\
    &\text{一般式:\ }Ax+By+C=0.
\end{aligned}\]
前三种方程由于使用了斜率, 所以无法表示竖直的直线, 其中斜截式和两点式都可以看成点斜式的特例. 截距式方程无法表示水平的直线和竖直的直线. 显然, 前四种方程都可以写成一般式. 当 $B\neq0$ 时, 一般式可写成斜截式 $y=-\dfrac{A}{B}x-\dfrac{C}B$, 从而可知其斜率和纵截距.
</p>

<p>
\lianxi
<myexercise>
    <p>    求直线 $l\colon -3x+2y=12$ 的斜率、横截距和纵截距.
</p>
</myexercise>
<mysolution>
    <p>
    方程化为斜截式: $y= \dfrac32 x+6$, 则斜率为 $\dfrac32$, 横截矩为 $-4$, 纵截距为 $6$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知两点 $A(4, 0)$, $B(0, 3)$, 点 $C(8, a)$ 在直线 $AB$ 上, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $AB\colon \dfrac{x}4+ \dfrac{y}3= 1$, 将 $C(8, a)$ 代入知, $a=-3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $m$ 为任意实数, 则直线 $y=mx+2m+1$ 恒过一定点, 求此定点的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    方程化为 $y= m(x+2)+ 1$, 过定点 $(-2,1)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l_1$ 经过点 $(1, 2)$, 且倾斜角是直线 $l_1\colon y=x+3$ 的倾斜角的 $2$ 倍, 求直线 $l_1$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    $l_2$ 的倾斜角为 $45^\circ$, 则 $l_1$ 的倾斜角为 $90^\circ$, 方程为 $x=1$.
</p>

<p>
    \varexercise 若 $l_2$ 的方程改为 $y= 2x+3$, 求直线 $l_1$ 的方程.
</p>

<p>
    设 $l_1$, $l_2$ 的倾斜角分别为 $\alpha_1$, $\alpha_2$, 则
    \mymarginpar{利用斜率等于倾斜角的正切.}
    \[\alpha_1= 2\alpha_2,\quad \tan\alpha_2= 2,\]
    所以由二倍角公式, $l_1$ 的斜率为
    \[\tan\alpha_1= \tan 2\alpha_2
        = \frac{2\tan\alpha_2}{1- \tan^2\alpha_2}
        = \frac43,\]
    方程为 $y-2= -\dfrac43(x-1)$.
</p>

<p>
    \varexercise 若 $l_1$ 仍经过点 $(1, 2)$, 且倾斜角比直线 $l_1\colon y= 2x+3$ 的倾斜角大 $45^\circ$, 求直线 $l_1$ 的方程.
</p>

<p>
    方法同上, 由和角的正切公式,
    \[\tan\alpha_1= \tan (\alpha_2+ 45^\circ)
        = \frac{\tan\alpha_2+ 1}{1- \tan\alpha_2}
        = -3,\]
    方程为 $y-2= -3(x-1)$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{直线的斜率公式}
<span id="example-"></span>
<myexample>
    <p>
    已知点 $A(1, -2)$, $B(2, m-1)$, $C(-1, 4)$, 直线 $AC$ 的斜率等于直线 $BC$ 的斜率的 $3$ 倍, 求 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    由题意,
    \[\frac{4-(-2)}{-1-1}= 3\cdot\frac{4-(m-1)}{-1-2},\quad m=2.\]
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知 $P(1, -1)$, $Q(2, 2)$, 直线 $l\colon mx+y+m=0$ 与线段 $PQ$ 有交点, 求实数 $m$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>
    $l$ 的方程化为 $m(x+1)+y=0$, 其过定点 $A(-1,0)$. 作图可知, $l$ 的斜率 $-m$ 介于直线 $AP$ 与 $AQ$ 的斜率之间, 所以
    \mymarginpar{必要时, 应考虑题意对应的图形.}
    \[-m\in \biggl[\frac{-1-0}{1-(-1)}, \frac{2-0}{2-(-1)}\biggr],\]
    即 $m\in \biggl[-\dfrac12, \dfrac23\biggr]$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知直线 $l$ 经过点 $M(2m^2 +1, 2)$, $N(2m^2 -1, m)$, 它的斜率为 $k> 1$, 求 $m$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    $k= \dfrac{2-m}2> 1$, 则 $m\in (-\infty,0)$.
</p>
</mysolution>
</p>

<p>
\subsubsection{直线的倾斜角与斜率}
<span id="example-"></span>
<myexample>
    <p>
    求直线 $x+\sqrt3 y+a=0$ 的倾斜角.
</p>
</myexample>
<mysolution>
    <p>
    斜率 $k= -\dfrac{\sqrt3}3$, 倾斜角为 $150^\circ$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    求直线 $x-\sqrt3 y+a=0$ 的倾斜角.
</p>
</myexercise>
<mysolution>
    <p>
    斜率 $k= \dfrac{\sqrt3}3$, 倾斜角为 $30^\circ$.
</p>
</mysolution>
</p>

<p>
\subsubsection{利用待定系数法求直线的方程}
<span id="example-"></span>
<myexample>
    <p>
    设直线 $l$ 经过点 $A(2,1)$, 且横截距等于纵截距的 $2$ 倍, 求 $l$ 的方程.
</p>
</myexample>
<mysolution>
    <p>
    设纵截距为 $a$, 横截距为 $2a$.
    \mymarginpar{横截矩、纵截距之一为 $0$ 时, 无法使用截距式, 故必须讨论.}
</p>

<p>
    若 $a= 0$, 则 $l$ 过原点 $(0,0)$, 方程为 $y= \dfrac12x$.
</p>

<p>
    若 $a\neq 0$, 则 $l\colon \dfrac{x}{2a}+ \dfrac{y}a= 1$. 将 $A(2,1)$ 代入, 解得 $a=2$, 故 $l$ 的方程为 $\dfrac{x}2+ y= 1$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    求直线 $l\colon \sqrt3x+y+1=0$ 的倾斜角.
</p>
</myexercise>
<mysolution>
    <p>
    $l$ 的斜率为 $-\sqrt3$, 倾斜角为 $120^\circ$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知两点 $A(3, 2)$, $B(8, 12)$, 若点 $C(-2, a)$ 在直线 $AB$ 上, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    直线 $AB$ 与直线 $AC$ 斜率相等, 则
    \[\frac{12-2}{8-3}= \frac{a-2}{-2-3},\quad a=-8.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若点 $A(ab, a+b)$ 在第一象限, 判断直线 $l\colon bx+ay-ab=0$ 所在的象限.
</p>
</myexercise>
<mysolution>
    <p>
    $ab>0$ 且 $a+b>0$, 则 $a,b>0$, 且 $l$ 过点 $(a,0)$ 和 $(0,b)$. 作图可知, $l$ 过第一、二、四象限. 
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $m$ 为任意实数, 则直线 $l\colon mx+y-1+2m=0$ 恒过一定点, 求该定点的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    $l$ 的方程化为 $m(x+2)+ y-1= 0$, 过定点 $(-2,1)$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    设直线 $l$ 的倾斜角为 $\alpha$, 且 $\sin\alpha=\dfrac35$, 求此直线的斜率.
</p>
</myexercise>
<mysolution>
    <p>
    作辅助直角三角形可知, 斜率为 $\tan\alpha= \dfrac34$ 或 $-\dfrac34$.
    \mymarginpar{$\alpha$ 可能为锐角或钝角.}
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设点 $A(2,-1)$, 点 $P$ 在坐标轴上, 且直线 $AP$ 的倾斜角为 $45^\circ$, 求点 $P$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    直线 $AP$ 的斜率为 $1$. 若点 $P$ 在 $x$ 轴上, 设 $P(x,0)$, 则
    \mymarginpar{也可直接求 $AP\colon y= x-3$, 其与坐标轴交于点 $(3,0)$ 或 $(0,-3)$.}
    \[\frac{-1-0}{2-x}= 1,\quad x=3.\]
    若点 $P$ 在 $y$ 轴上, 设 $P(0,y)$, 则
    \[\frac{-1-y}{2-0}= 1,\quad y= -3.\]
    故点 $P$ 为 $(3,0)$ 或 $(0,-3)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设直线 $PQ$ 的斜率为 $-2$, 将其绕点 $P$ 顺时针旋转 $45^\circ$ 得直线 $PR$, 求 $PR$ 的斜率.
</p>
</myexercise>
<mysolution>
    <p>
    设直线 $PQ$ 和 $PR$ 的倾斜角分别为 $\alpha_1$,$\alpha_2$, 则
    \[\tan\alpha_1= -2,\quad \alpha_1-45^\circ= \alpha_2,\]
    所以 $PR$ 的斜率为
    \[\tan\alpha_2= \tan(\alpha_1-46^\circ)
        = \frac{\tan\alpha_1- 1}{1+\tan\alpha_1}= 3.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设直线 $l$ 的斜率 $k\in[-1,\sqrt3)$, 求其倾斜角 $\alpha$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    作图可知, $\alpha\in [0^\circ,60^\circ)\cup [135^\circ,180^\circ)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设函数 $f(x)= \sin x$, $\dfrac\pi2< a< b< \pi$, 比较 $\dfrac{f(a)}a$ 和 $\dfrac{f(b)}b$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    由 $f(0)=0$ 知, $\dfrac{f(x)}x= \dfrac{f(x)- f(0)}{x- 0}$ 表示函数 $f(x)$ 的图形上一点 $(x,f(x))$ 与原点连线的斜率. 作图可知, $\dfrac{f(a)}a> \dfrac{f(b)}b$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 已知点 $A(5, -1)$, $B(7, 3)$, 且 $AC$ 边的中点 $M$ 在 $y$ 轴上, $BC$ 边的中点 $N$ 在 $x$ 轴上, 求顶点 $C$ 的坐标和直线 $MN$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设 $C(x,y)$, 则
    \[M\biggl(\frac{x+5}2, \frac{y-1}2\biggr),\quad
    N\biggl(\frac{x+7}2, \frac{y+3}2\biggr).\]
    由题意,
    \[\left\{\!\!\begin{array}{l}
        x+5=0,\\
        y+3=0,
    \end{array}\right.\quad\text{即}\quad
    \left\{\!\!\begin{array}{l}
        x=-5,\\
        y=-3,
    \end{array}\right.\]
    所以 $C(-5,-3)$. 因此 $M(0,-2)$, $N(1,0)$, 直线 $MN$ 的方程为 $x- \dfrac{y}2= 1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l_1 \colon y=kx-\sqrt3$ 与 $l_2 \colon 2x+3y-6=0$ 的交点在第一象限, 求直线 $l_1$ 的倾斜角 $\alpha$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    $l_1$ 过定点 $A(0,-\sqrt3)$, $l_2$ 与坐标轴交于点 $B(3,0)$, $C(0,2)$, 且 $l_1$ 与线段 $BC$ (不含端点) 有交点. 作图可知, $\alpha\in(30^\circ,90^\circ)$.
</p>
</mysolution>