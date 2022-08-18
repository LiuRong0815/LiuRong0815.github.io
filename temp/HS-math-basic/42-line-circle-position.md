\sectioncounter{41}
</p>

<p>
\section{直线与圆的位置关系}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
直线与圆的位置关系有三种: 相离, 相切, 相交. 考虑圆 $C$ 与直线 $l$, 设圆 $C$ 的半径为 $r$, 点 $C$ 到 $l$ 的距离为 $d$, 则圆 $C$ 与直线 $l$ 的三种位置关系通常用 $r$ 与 $d$ 的大小刻画, 即
\[d>r\Leftrightarrow\text{相离},\quad 
    d=r\Leftrightarrow\text{相切},\quad 
    d< r\Leftrightarrow\text{相交}.\]
若直线斜率存在且不为 $0$, 也可以把直线与圆的方程联立, 消去一个元 (如 $y$) 后, 
由所得的一元二次方程的根的情况得到直线与圆的位置关系, 即
\[\Delta< 0\Leftrightarrow\text{相离},\quad 
    \Delta=0\Leftrightarrow\text{相切},\quad 
    \Delta>0\Leftrightarrow\text{相交}.\] 
后一方法也是判断直线与曲线是否相交的通用做法.
</p>

<p>
当直线与圆相切时, 过切点的半径垂直于该直线. 当直线与圆相交时, 以两交点为端点的线段是圆的弦. 求此弦长通常有两种方法, 分别是利用两点之间距离公式和利用垂径定理. 前一种方法为通用方法 (对一般的曲线均适用), 在圆中后一种方法更方便.
</p>

<p>
具体来说, 对于前面提到的圆 $C$ 与直线 $l$, 当它们相交时, 利用垂径定理可知半弦长为 $\sqrt{r^2-d^2}$, 故直线 $l$ 被圆 $C$ 截得的弦长为 $2\sqrt{r^2-d^2}$. 通用做法需利用直线 $y=kx+b$ 上两点 $A(x_1,y_1)$, $B(x_2,y_2)$ 之间距离公式
\[|AB|= \sqrt{1+k^2} |x_1-x_2|\]
和关于 $x$ 的二次方程 $Ax^2+Bx+C=0$ 的两根之间距离公式 (由求根公式可得)
\[|x_1-x_2|= \frac{\sqrt{\Delta}}{|A|}.\]
实际计算可参照下面第 $1$ 题的解题过程.
</p>

<p>
\lianxi
<myexercise>
    <p>    求直线 $l\colon x+y-3=0$ 被圆 $C\colon (x-2)^2 +(y+1)^2 =4$ 截得的弦长.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 点 $C(2,-1)$ 到 $l$ 的距离为
    \[d= \frac{|2+(-1)-3|}{\sqrt{1^2+1^2}}= \sqrt2,\]
    圆 $C$ 的半径 $r=2$. 由垂径定理, 所求弦长为
    \[2\sqrt{r^2-d^2}= 2\sqrt2.\]
</p>

<p>
    方法二: $l$ 的方程化为 $y=3-x$, 代入圆 $C$ 的方程并整理,
    \[x^2-6x+8=0.\]
    设 $l$ 与圆 $C$ 交于点 $A(x_1,y_1)$, $B(x_2,y_2)$, 则
    \mymarginpar{也可以解出 $x= 2,4$, 并得 $|x_1-x_2|=2$.}
    \[\begin{gathered}
        |x_1-x_2|= \frac{\sqrt{6^2- 4\cdot 8}}{|1|}= 2,\\
        |AB|= \sqrt{1+1^2}|x_1-x_2|= 2\sqrt2.
    \end{gathered}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l\colon x-y+1=0$ 与圆 $C\colon (x-a)^2 +y^2 =2$ 有公共点, 求 $a$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 点 $C(a,0)$ 到直线 $l$ 的距离小于或等于半径 $r=\sqrt2$, 即
    \[\frac{|a-0+1|}{\sqrt{1^2+1^2}}\leqslant \sqrt{2},\quad
    -3\leqslant a\leqslant 1,\]
    所以 $a\in[-3,1]$.
</p>

<p>
    方法二: 直线 $l$ 的方程化为 $y= x+1$. 代入圆 $C$ 的方程并整理,
    \[2x^2+ 2(1-a)x+ a^2-1= 0.\]
    由题意,
    \[\Delta= [2(1-a)]^2- 4\cdot 2(a^2-1)\geqslant 0,\]
    解得 $a\in[-3,1]$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l\colon \sqrt3 x-y+m=0$ 与圆 $C\colon x^2 +y^2 -2x-2=0$ 相切, 求 $m$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    圆 $C\colon (x-1)^2+y^2= 3$, 则圆心 $C(1,0)$, 半径 $r=\sqrt3$. 由题意, 圆心 $C$ 到直线 $l$ 的距离等于半径 $r$, 则
    \[\frac{|\sqrt3-0+m|}{\sqrt{3+1}}= \sqrt3,\quad
    m= \sqrt3,-3\sqrt3.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l\colon 3x+4y+m=0$ 与圆 $C\colon x^2+y^2-2x+4y+4=0$ 没有公共点, 求 $m$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    圆 $C\colon (x-1)^2+(y+2)^2= 1$, 则圆心 $C(1,-2)$, 半径 $r=1$. 由题意, 圆心 $C$ 到直线 $l$ 的距离大于半径 $r$, 则
    \[\frac{|3-8+m|}{\sqrt{3^2+4^2}}>1,\]
    解得, $x\in (-\infty,0)\cup (10,+\infty)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若圆 $C\colon x^2 +y^2 =9$ 的弦 $PQ$ 的中点为 $M(1,2)$, 求直线 $PQ$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由垂径定理, $CM\perp PQ$. 由 $CM$ 的斜率为 $2$ 知 $PQ$ 的斜率为 $-\dfrac12$, 则
    \[PQ\colon y-2= -\frac12(x-1).\]
</p>

<p>
    方法二: 显然 $PQ$ 的斜率存在, 设为 $k$, 则
    \mymarginpar{方法二对一般曲线也有效.}
    \[PQ\colon y-2= k(x-1),\]
    代入圆 $C$ 的方程并整理,
    \[(1+k^2)x^2+ 2k(2-k)x+ (2-k)^2-9= 0.\]
    设 $P(x_1,y_1)$, $Q(x_2,y_2)$, 则
    \[x_1+x_2= -\frac{2k(2-k)}{1+k^2}.\]
    由弦 $PQ$ 的中点为 $M(1,2)$ 知,
    \[\frac{x_1+x_2}{2}= 1,\quad x_1+x_2= 2,\]
    由此可以解得, $k= -\dfrac12$, 答案同方法一.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{直线与圆的位置关系}
<span id="example-"></span>
<myexample>
    <p>
    若圆 $C\colon (x-1)^2 +y^2 =1$ 与直线 $l\colon 3x+4y+m=0$ 相切, 求 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    圆心 $C(1,0)$ 到直线 $l$ 的距离等于半径 $r=1$, 则
    \[\frac{|3+0+m|}{\sqrt{3^2+4^2}}=1,\quad
    m=2,-8.\]
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知点 $P(x,y)$ 在圆 $C\colon x^2 +y^2 -4x+1=0$ 上, 求 $\dfrac{y}x$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>
    方法一: 设 $\dfrac{y}x= k$, 代入圆 $C$ 的方程,
    \[(1+k^2)x^2- 4x+ 1= 0,\]
    则
    \[\begin{gathered}
        \Delta= (-4)^2- 4(1+k^2)\cdot 1\geqslant 0,\\
        k\in [-\sqrt3,\sqrt3].
    \end{gathered}\]
</p>

<p>
    方法二: 圆 $C\colon (x-2)^2+y^2= 3$, 
    \mymarginpar{方法二也可用于求 $\dfrac{y+1}{x+1}$ 的取值范围. 此时方法一仍可行, 但是计算量要大一些.}
    且 $\dfrac{y}x= \dfrac{y-0}{x-0}$ 表示直线 $OP$ 的斜率, 而 $OP$ 与圆 $C$ 相交, 所以圆心 $C(2,0)$ 到直线 $OP$ 的距离小于或等于半径 $r=\sqrt3$. 设 
    \[OP\colon y=kx, \text{\ 即\ } kx-y=0,\]
    则
    \[\frac{|2k-0|}{\sqrt{k^2+1}}\leqslant \sqrt3,\quad
    k\in [-\sqrt3,\sqrt3].\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知直线 $l\colon ax+y-2=0$ 与圆 $C\colon (x-1)^2 +(y-a)^2 =4$ 相交于 $A$,$B$ 两点, 且 $\triangle ABC$ 为等边三角形, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为等边 $\triangle ABC$ 的边长为圆 $C$ 的半径 $r=2$, 由垂径定理, 圆心 $C(1,a)$ 到直线 $AB$ 的距离为 $\sqrt3$, 所以
    \[\frac{|a+a-2|}{\sqrt{a^2+1}}= \sqrt3,\quad
    a= 4\pm\sqrt{15}.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{垂径定理的应用}
<span id="example-"></span>
<myexample>
    <p>
    已知圆 $C\colon x^2+y^2 -2x-4y-11=0$ 被过点 $P(-1,1)$ 的直线 $l$ 截得的弦长为 $4\sqrt3$, 求直线 $l$ 的方程.
</p>
</myexample>
<mysolution>
    <p>
    圆 $C\colon (x-1)^2+ (y-2)^2= 16$, 则 $C(1,2)$, 半径 $r=4$. 由垂径定理, 圆心 $C$ 到直线 $l$ 的距离等于 $2$.
</p>

<p>
    若 $l$ 的斜率不存在, 则 $l\colon x=-1$, 符合题意.
</p>

<p>
    若 $l$ 的斜率存在, 设为 $k$, 则其方程为
    \[\begin{gathered}
        y-1= k(x+1),\\
        kx-y+k+1=0,
    \end{gathered}\]
    则
    \[\frac{|k-2+k+1|}{\sqrt{k^2+1^2}}= 2,\quad
    k= -\frac34.\]
    此时, $l\colon 3x+4y-1=0$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知圆 $C\colon x^2+y^2+ 2y-3= 0$, 直线 $l_1$ 经过点 $(1,0)$ 且与直线 $l_2\colon x-y+1=0$ 垂直, 并与圆 $C$ 交于 $A$, $B$ 两点, 求 $\triangle OAB$ 的面积.
</p>
</myexample>
<mysolution>
    <p>
    圆 $C\colon x^2+ (y+1)^2= 4$, 则 $C(0,-1)$, 半径 $r=2$. 直线 $l_1$ 的斜率为 $-1$, 则
    \[l_1\colon x+y-1= 0.\]
    因为圆心 $C$ 到直线 $l_1$ 的距离
    \[d= \frac{|0+(-1)-1|}{\sqrt{1^2+1^2}}= \sqrt2,\]
    由垂径定理, $|AB|= 2\sqrt2$, 则 $\triangle OAB$ 的面积为
    \[\frac12 d\cdot |AB|= 2.\]
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    设直线 $l\colon 3x+4y-5=0$ 与圆 $C\colon x^2 +y^2 =4$ 相交于 $A$,$B$ 两点, 求弦 $AB$ 的长.
</p>
</myexercise>
<mysolution>
    <p>
    圆心 $C(0,0)$ 到直线 $l$ 的距离
    \[d= \frac{|0+0-5|}{\sqrt{3^2+4^2}}= 1,\]
    而圆 $C$ 的半径 $r=2$, 由垂径定理, 
    \[|AB|= 2\sqrt{r^2-d^2}= 2\sqrt3.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知圆 $C\colon (x-4)^2 +(y-1)^2=5$ 内一点 $P(3, 0)$, 求过点 $P$ 的最短弦所在直线 $l$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    作图分析, 由垂径定理知, 当过点 $P$ 的弦最短时, 圆心 $C$ 到 $l$ 的距离最大且为 $|CP|$, 此时 $CP\perp l$. 由 $C(4,1)$ 知 $CP$ 的斜率为 $1$, 则 $l$ 的斜率为 $-1$, 方程为 $x+y=3$.
</p>
</mysolution>
</p>

<p>
\subsubsection{直线与圆的综合问题}
<span id="example-"></span>
<myexample>
    <p>
    已知圆 $C\colon (x-2)^2 +y^2 =1$, 点 $Q$ 是直线 $l\colon x+y-6=0$ 上的动点, 过点 $Q$ 作圆 $C$ 的切线 $QA$, $QB$, 切点为 $A$, $B$. 求四边形 $QACB$ 面积的最小值及此时点 $Q$ 的坐标.
</p>
</myexample>
<mysolution>
    <p>
    作图可知, 四边形 $QACB$ 的面积
    \[S_{QACB}= 2\cdot S_{\triangle CBQ}
        = |CB|\cdot |QB|= \sqrt{|QC|^2-1},\]
    所以当 $|QC|$ 最小时, $S_{QACB}$ 最小, 此时 $QC\perp l$. 由 $C(2,0)$ 知,
    \[\begin{gathered}
        |QC|= \frac{|2+0-6|}{\sqrt{1^2+1^2}}= 2\sqrt2,\\
        QC\colon x-y-2= 0,
    \end{gathered}\]
    则 $Q(4,2)$. 对应地, $S_{QACB}= \sqrt7$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知点 $C\Big(t,\dfrac2t\Big)$ ($t\neq0$), 圆 $C$ 过坐标原点 $O$, 直线 $l\colon 2x+y-4=0$ 与圆 $C$ 交于点 $M$,$N$, 且 $|OM|=|ON|$, 求圆 $C$ 的方程.
</p>
</myexample>
<mysolution>
    <p>
    由 $|OM|= |ON|$ 和圆的对称性知, $OC\perp MN$, 即 $OC\perp l$. 所以
    \[\frac{2}{t^2}\cdot (-2)= -1,\quad t=\pm2.\]
    若 $t= 2$, 则 $C(2,1)$, 圆 $C$ 的方程为
    \[(x-2)^2+ (y-1)^2= 5.\]
    若 $t= -2$, 则 $C(-2,-1)$, 圆 $C$ 的方程为
    \[(x+2)^2+ (y+1)^2= 5.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    “$m=\sqrt2$”是“直线 $l\colon y=x+m$ 与圆 $C\colon x^2 +y^2 =1$ 相切”的什么条件?
</p>
</myexercise>
<mysolution>
    <p>
    充分不必要条件.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知圆 $C\colon x^2 +y^2 -2x+2y=0$, 直线 $l\colon y+2=k(x-2)$, 求圆 $C$ 与直线 $l$ 的交点的个数.
</p>
</myexercise>
<mysolution>
    <p>
    直线 $l$ 过定点 $(2,-2)$,
    \mymarginpar{若定点在圆内, 则交点个数为 $2$.}
    恰在圆 $C$ 上, 则交点的个数为 $1$ (相切) 或 $2$ (相交).
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知直线 $l\colon ax-2by=2$ 平分圆 $C\colon x^2 +y^2 -4x+2y+1=0$ 的圆周, $a,b>0$, 求 $ab$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    圆 $C\colon (x-2)^2+(y+1)^2= 4$. 由题意, 直线 $l$ 过点 $C$, 则
    \[2a- 2b\cdot (-1)= 2,\quad a+b= 1.\]
    因为 $a,b>0$, 由均值不等式 $\dfrac{a+b}2\geqslant \sqrt{ab}$ 知, $ab\leqslant \dfrac12$, 即 $ab$ 的最大值为 $\dfrac12$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
</p>

<p>
<myexercise>
    <p>    求直线 $l\colon x-\sqrt3 y=0$ 截圆 $C\colon (x-2)^2 +y^2=4$ 所得劣弧的弧长.
</p>
</myexercise>
<mysolution>
    <p>
    圆 $C$ 的圆心 $C(2,0)$, 半径 $r=2$, 点 $C$ 到 $l$ 的距离
    \[d= \frac{|2-0|}{\sqrt{1+3}}= 1.\]
    设直线 $l$ 与圆 $C$ 交于点 $A$,$B$, 则 $\angle ACB= 120^\circ$, 故劣弧 $AB$ 长为
    \[\frac{120^\circ}{360^\circ}\cdot 2\pi r
    = \frac{4\pi}{3}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若点 $P(1,1)$ 为圆 $C\colon x^2 +y^2 -6x=0$ 的弦 $MN$ 的中点, 求弦 $MN$ 所在直线的方程.
</p>
</myexercise>
<mysolution>
    <p>
    圆 $C\colon (x-3)^2+y^2= 9$, 圆心 $C(3,0)$. 而 $CP\perp MN$, 由 $CP$ 的斜率为 $-\dfrac12$ 知, $MN$ 的斜率为 $2$, 故
    \[MN\colon y-1= 2(x-1).\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l_1\colon y=x+a$ 和 $l_2\colon y=x+b$ 将圆 $C\colon (x-1)^2 +(y-2)^2 =1$ 分成长度相等的四段弧, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    作图分析知, 圆 $C$ 截 $l_1$,$l_2$ 所得弦对应的圆心角均为 $90^\circ$, 故圆心 $C(1,2)$ 到 $l_1$,$l_2$ 的距离均为 $\sqrt2$. 对直线 $l_1\colon y=x+a$, 
    \[\sqrt{2}= \frac{|1-2+a|}{\sqrt2},\quad a=3,-1.\] 
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知直线 $l_1$ 和 $l_2$ 是圆 $C\colon x^2 +y^2 =2$ 的两条切线, 且交点为 $(1,3)$, 求直线 $l_1$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    作图分析知, $l_1$,$l_2$ 的斜率均存在. 设 $l_1$ 的斜率为 $k$, 则 $l_1$ 的方程为
    \[\begin{gathered}
        y-3= k(x-1),\\
        kx- y+ k+ 3= 0.
    \end{gathered}\]
    由题意, 点 $C(0,0)$ 到 $l_1$ 的距离为圆 $C$ 的半径 $r=\sqrt 2$, 故
    \[\frac{|k+3|}{\sqrt{k^2+1}}= \sqrt2,\quad k=-1,7.\]
    所以 $l_1$ 的方程为
    \[x+y-2= 0,\text{\ 或\ } 7x-y+10= 0.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设坐标原点为 $O$, 圆 $C\colon (x-2)^2 +y^2 =3$ 上有一点 $M(a,b)$ 满足 $\overrightarrow{OM}\cdot\overrightarrow{CM}=0$, 求 $\dfrac{b}a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $OM\perp CM$, 则 $OM$ 为圆 $C$ 的切线, 
    \mymarginpar{也可根据点 $M$ 在圆 $C$ 上和 $\overrightarrow{OM}\cdot\overrightarrow{CM}=0$ 解出 $a$,$b$ 的值.}
    而 $\dfrac{b}a= \dfrac{b-0}{a-0}$ 表示直线 $OM$ 的斜率. 作图可知, $\angle MOC= 60^\circ$, 则 $\dfrac{b}a= \pm\sqrt3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    点 $A$, $B$ 分别是 $x$ 轴和 $y$ 轴上的动点, 若以 $AB$ 为直径的圆 $C$ 与直线 $l\colon 2x+y-4= 0$ 相切, 求圆 $C$ 面积的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    设圆 $C$ 与直线 $l$ 相交于点 $D$, 圆 $C$ 的半径为 $r$, 则
    \mymarginpar{若由圆 $C$ 与直线 $l$ 相切, 利用点 $C$ 到直线 $l$ 距离等于半径, 则不易求解.}
    \[|OC|+ |CD|= 2r,\]
    且大于或等于点 $O$ 到直线 $l$ 的距离 $\dfrac4{\sqrt5}$. 所以 $r\geqslant \dfrac2{\sqrt5}$, 等号成立当且仅当 $OD\perp l$, 则圆 $C$ 面积的最小值为 $\dfrac{4\pi}5$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设点 $M(x_0,1)$, 若在圆 $O\colon x^2 +y^2=1$ 上存在点 $N$, 使得 $\angle OMN=45^\circ$, 求 $x_0$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    设点 $A(0,1)$, 取圆 $O$ 上任意一点, 可知 $\angle OMB$ 的最大值为 $\angle OMA$, 所以题意表明 $\angle OMA\geqslant 45^\circ$. 此时
    \[\tan\angle OMA= \frac{OA}{AM}
        = \frac1{|x_0|}\geqslant 1,\]
    解得 $0< |x_0|\leqslant 1$. 显然 $x_0=0$ 符合题意, 所以 $x_0\in[-1,1]$.
</p>
</mysolution>
