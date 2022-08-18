\sectioncounter{40}
</p>

<p>
\section{圆的方程}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
圆 (circle) 是到定点距离为定值的点的集合, 定点称为圆心 (center), 定值为半径 (radius). 圆心为 $C$ 的圆称为圆 $C$. 设 $C(a,b)$, 圆 $C$ 的半径为 $r$, 任取其上一点 $P(x,y)$, 则 $|PC|=r$, 用两点间距离公式表示为
\[\sqrt{(x-a)^2+(y-b)^2}= r,\ \text{即}\ 
    (x-a)^2+(y-b)^2= r^2.\]
上述第二个方程称为圆 $C$ 的标准方程, 也可以展开后化为 
\[x^2+y^2+Dx+Ey+F=0\]
的形式, 此形式称为圆的一般方程 (式中 $D^2+E^2- 4F>0$). 后者的 $x^2$,$y^2$ 前面的系数相同, 且可以通过分别对 $x$,$y$ 配方化为前者, 如
\[x^2+y^2+2x-4y+1=0\Rightarrow
    (x+1)^2+(y-2)^2=4.\]
</p>

<p>
圆的标准方程和一般方程中都有三个待定系数, 所以一般确定圆的方程需要三个条件. 解题时常会遇到直线与圆相切的条件, 由直线与圆的位置关系可知, 此条件等价于圆心到直线的距离为半径. 如直线 $l$ 过点 $A(3,0)$, 且与圆 $C\colon x^2 +y^2 =1$ 相切, 则可设 $l\colon y=k(x-3)$, 即 $kx-y-3k=0$. 由相切关系,
\[\frac{|-3k|}{\sqrt{k^2+1}}=1,\quad k=\pm\frac{\sqrt2}4,\]
所以 $l\colon y= \dfrac{\sqrt2}4(x-3)$ 或 $y= -\dfrac{\sqrt2}4(x-3)$.
</p>

<p>
点和圆的位置关系有三种: 点在圆外, 点在圆上, 点在圆内. 这三种位置关系取决于点到圆心的距离. 若点在圆外, 则过该点的圆的切线有两条, 它们的长度相等, 且点与圆心的连线平分两切线所成的角.
</p>

<p>
\lianxi
<myexercise>
    <p>    已知圆 $P$ 的内接正方形 $ABCD$ 相对的两个顶点的坐标分别是 $A(5,6)$, $C(3,4)$, 求该圆的方程.
</p>
</myexercise>
<mysolution>
    <p>
    $AC$ 为直径, 长 $2\sqrt2$, 则圆 $P$ 的半径为 $\sqrt2$. 而中点 $(4,5)$ 为圆心, 所以圆 $P$ 的方程为
    \[(x-4)^2+(y-5)^2= 2.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若圆 $C\colon x^2 +y^2 +4x+2by+b^2 =0$ 分别 (1) 经过原点; (2) 与 $x$ 轴相切, 求对应的 $b$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 将原点 $(0,0)$ 代入, $b=0$.
</p>

<p>
    (2) 方程化为标准方程,
    \[(x+2)^2+(y+b)^2= 4,\]
    则 $C(-2,-b)$, 半径 $r=2$. 由圆 $C$ 与 $x$ 轴相切知 $|-b|=2$, $b=\pm2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若点 $P(1,1)$ 在圆 $C\colon x^2 +y^2 -2ax+4ay-4=0$ 的内部, 求 $a$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    方程化为标准方程,
    \mymarginpar{此过程可一般化. 设 $P(a,b)$, 圆 $C$ 的一般式简记为 $G(x,y)=0$, 则
    \[\begin{gathered}
        \text{点 $P$ 在圆 $C$ 上}\Leftrightarrow G(a,b)=0,\\
        \text{点 $P$ 在圆 $C$ 内}\Leftrightarrow G(a,b)< 0,\\
        \text{点 $P$ 在圆 $C$ 外}\Leftrightarrow G(a,b)>0.\\
    \end{gathered}\]}
    \[(x-a)^2+(y+2a)^2= 5a^2+4,\]
    则圆心 $C(a,-2a)$, 半径 $r=\sqrt{5a^2+4}$. 由已知, $|PC|< r$, 即 $|PC|^2< r^2$, 则
    \[(1-a)^2+ (1+2a)^2< 5a^2+4,\]
    解得 $a\in(-\infty,1)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 $l\colon x-y+4=0$ 平分圆 $C\colon x^2 +y^2 +2ax-2ay+1=0$ 的周长, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    圆心 $C(-a,a)$ 在直线 $l$ 上, 则
    \mymarginpar{圆的一般式中的系数应确保圆的方程能化为标准形式, 即应检验解出的参数.}
    \[-a-a+4= 0,\quad a=2,\]
    此时圆 $C$ 的标准方程为
    \[(x+2)^2+ (y-2)^2= 9.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若圆 $C$ 的半径为 $1$, 圆心在第一象限, 且与直线 $l\colon 4x-3y=0$ 和 $x$ 轴都相切, 求该圆的标准方程.
</p>
</myexercise>
<mysolution>
    <p>
    设 $C(a,b)$, $a$,$b>0$. 因为圆 $C$ 的半径 $r=1$, 则
    \[\frac{|4a- 3b|}{\sqrt{4^2+3^2}}= |b|= 1,\]
    解得 $a=b=1$, 圆的标准方程为
    \[(x-1)^2+ (y-1)^2= 1.\]
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
</p>

<p>
\subsubsection{求圆的方程}
<span id="example-"></span>
<myexample>
    <p>
    设圆 $C$ 的圆心在 $y$ 轴上, 半径为 $1$, 且过点 $P(1,2)$ 的圆 $C$ 的方程.
</p>
</myexample>
<mysolution>
    <p>
    设 $C(0,b)$, 则 $|PC|=1$, 即
    \[(0-1)^2+ (b-2)^2= 1^2,\quad b=2,\]
    所以圆 $C$ 的方程为
    \[x^2+(y-2)^2=1.\]
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    圆 $C$ 与 $x$ 轴相切于点 $T(1,0)$, 与 $y$ 轴正半轴相交于两点 $A$,$B$, 且 $|AB|=2$, 求圆 $C$ 的标准方程.
</p>
</myexample>
<mysolution>
    <p>
    设圆 $C$ 的半径为 $r$, 则 $C(1,r)$. 因为点 $C$ 到 $y$ 轴的距离为 $1$, $|AB|=2$, 由垂径定理, $|AC|= \sqrt2$, 即 $r=\sqrt2$, 故圆 $C$ 的方程为
    \[(x-1)^2+ (y-\sqrt2)^2= 2.\]
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    若圆 $C$ 与 $y$ 轴交于两点 $A(0, -4)$, $B(0,-2)$, 且圆心在直线 $l\colon x=2$ 上, 求圆 $C$ 的方程. 
</p>
</myexercise>
<mysolution>
    <p>
    由垂径定理, 圆心 $C$ 也在线段 $AB$ 的中垂线 $y=-3$ 上, 所以 $C(2,-3)$, 圆 $C$ 的半径为 $|AC|=\sqrt5$, 故方程为
    \[(x-2)^2+(y+3)^2= 5.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    圆 $C$ 经过坐标原点和点 $P(4,0)$, 且与直线 $l\colon y=1$ 相切, 求圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    圆心 $C$ 在线段 $OP$ 的中垂线 $x=2$ 上, 故设 $C(2,c)$. 由已知, 点 $C$ 到直线 $y=1$ 的距离等于圆 $C$ 的半径, 即 $|CO|$, 则
    \[|c-1|= \sqrt{2^2+c^2},\quad c=-\frac32,\]
    圆 $C$ 的方程为
    \[(x-2)^2+ \biggl(y+\frac32\biggr)^2= \frac{25}4.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{与圆有关的运动问题}
<span id="example-"></span>
<myexample>
    <p>
    设圆 $O\colon x^2 +y^2 =1$ 与 $x$ 轴交于 $P$,$Q$ 两点, 点 $M$ 是圆 $O$ 上异于点 $P$,$Q$ 的任意一点, 直线 $PM$,$QM$ 分别交直线 $l\colon x=3$ 于点 $P'$,$Q'$. 证明: 以线段 $P'Q'$ 为直径的圆 $C$ 总经过定点, 并求出定点坐标.
</p>
</myexample>
<mysolution>
    <p>
    为妨设 $P(-1,0)$, $Q(1,0)$, 再设 $M(a,b)$, 则 $a\neq 1$, $a^2+b^2= 1$. 因为
    \[\begin{aligned}
        PM\colon &y= \frac{b}{a+1}(x+1),\\
        QM\colon &y= \frac{b}{a-1}(x-1),
    \end{aligned}\]
    所以
    \[P'\biggl(3,\frac{4b}{a+1}\biggr),\quad
    Q'\biggl(3,\frac{2b}{a-1}\biggr).\]
    设圆 $C$ 上任一点为 $A(x,y)$, 则 $\overrightarrow{P'A}\cdot \overrightarrow{Q'A}=0$, 即
    \mymarginpar{作图分析可知, 定点若存在, 则必在 $x$ 轴上, 故直接设定点为 $N(n,0)$, 再利用 $\overrightarrow{P'N}\perp \overrightarrow{Q'N}= 0$ 可以更简单地得到答案.}
    \[(x-3)(x-3)+ \biggl(y-\frac{4b}{a+1}\biggr)\biggl(y-\frac{2b}{a-1}\biggr)=0,\]
    结合 $a^2+b^2=1$ 整理得
    \[x^2-6x+1+ y^2+ \frac{2(3a-1)}{b}y=0.\]
    定点 $(x',y')$ 应使得
    \[x'^2-6x'+1+ y'^2= y'= 0,\quad x'= 3\pm 2\sqrt2,\]
    所以圆 $C$ 过定点 $(3+ 2\sqrt2,0)$ 和 $(3- 2\sqrt2,0)$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    设定点 $A(-3,0)$, $B(3,0)$, 动点 $P$ 到点 $A$ 的距离与到点 $B$ 的距离之比为 $1:2$, 求点 $P$ 的轨迹图形所围的面积.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $|BP|= 2|AP|$. 设 $P(x,y)$, 则
    \mymarginpar{对定点 $A$,$B$, 若动点 $P$ 满足
    \[|PA|= k|PB|\quad (k>0),\]
    则当 $k=1$ 时, 点 $P$ 的轨迹为线段 $AB$ 的中垂线; 当 $k\neq1$ 时, 点 $P$ 的轨迹为圆.}
    \[\sqrt{(x-3)^2+ y^2}= 2\sqrt{(x+3)^2+ y^2},\]
    平方整理得 $(x+5)^2+ y^2= 16$, 即点 $P$ 的轨迹是半径为 $4$ 的圆, 面积为 $16\pi$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    求经过三点 $A(0,0)$, $B(4,0)$, $C(0,6)$ 的圆 $P$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    $\triangle ABC$ 恰为直角三角形,
    \mymarginpar{对一般的三角形, 外接圆的圆心为三边中垂线的交点, 通常只需计算两边中垂线的交点.}
    外接圆的圆心 $P$ 为斜边 $BC$ 的中点 $(2,3)$, 半径为 $|OP|= \sqrt{13}$, 则圆 $P$ 的方程为
    \[(x-2)^2+ (y-3)^2= 13.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求圆心为 $C(3, -5)$, 且与直线 $l\colon x-7y+2=0$ 相切的圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    圆 $C$ 的半径为 $C$ 到 $l$ 的距离
    \[\frac{|3- 7\cdot(-5)+ 2|}{\sqrt{1^2+(-7)^2}}= 4\sqrt2,\]
    则圆 $C$ 的方程为
    \[(x-3)^2+ (y+5)^2= 32.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $P(2, 1)$ 在圆 $C\colon x^2 +y^2 +2ax-2y+b=0$ 上, 点 $P$ 关于直线 $l\colon x+y-1=0$ 的对称点 $P'$ 也在圆 $C$ 上, 求圆 $C$ 的圆心坐标和半径.
</p>
</myexercise>
<mysolution>
    <p>
    由垂径定理, 线段 $PP'$ 的中垂线 $l$ 过圆心 $C(-a,1)$, 则
    \[-a+1-1=0,\quad a=0.\]
    将点 $P(2,1)$ 代入圆 $C$ 的方程,
    \[5-2+b= 0,\quad b=-3.\]
    所以圆 $C$ 的方程为
    \mymarginpar{也可先利用对称关系求点 $P'$ 的坐标, 再将点 $P$,$P'$ 的坐标代入圆 $C$ 的方程, 解出 $a$,$b$.}
    \[\begin{gathered}
        x^2+y^2-2y-3= 0,\\
        x^2+ (y-1)^2= 4,
    \end{gathered}\]
    即圆心 $C(0,1)$, 半径为 $2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $M(x, y)$ 与两个定点 $O(0,0)$, $A(3,0)$ 的距离之比为 $2\colon 1$, 求点 $M$ 的轨迹方程.
</p>
</myexercise>
<mysolution>
    <p>
    $|MO|= 2|MA|$, 即 $x^2+y^2-8x+12= 0$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    设点 $A(-4,-5)$, $B(6,-1)$, 求以线段 $AB$ 为直径的圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 直径长 $|AB|= 2\sqrt{29}$, $C(1,-3)$, 则圆 $C$ 的方程为
    \[(x-1)^2+ (y+3)^2= 29.\]
</p>

<p>
    方法二: 任取圆 $C$ 上一点 $M(x,y)$, 则 $\overrightarrow{MA}\cdot \overrightarrow{MB}= 0$, 答案同上.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求经过点 $A(8, 1)$ 且与坐标轴都相切的圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    作图知, 点 $C$ 在第一象限角平分线上. 设 $C(c,c)$, $c>0$, 则
    \[c=|AC|= \sqrt{(c-8)^2+ (c-1)^2},\]
    解得 $c=5$ 或 $13$. 所以圆 $C$ 的方程为
    \[\begin{aligned}
        &(x-5)^2+ (y-5)^2= 25,\\
        \text{或\ }&(x-13)^2+ (y-13)^2= 169.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若方程 $x^2 +y^2 +2ax-ay+a=0$ 表示圆, 求实数 $a$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    可先化为圆的标准方程, 也可直接用结论. 解得
    \[a\in (-\infty,0)\cup \biggl(\frac45,+\infty\biggr).\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知圆 $C$ 经过点 $A(2,2)$ 且与 $y$ 轴相切, 圆心在直线 $y= -x+2$ 上, 求圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    由点 $C$ 在直线 $y= -x+2$ 上设 $C(c,-c+2)$, 则
    \[|c|= |AC|= \sqrt{(c-2)^2+(-c)^2},\]
    解得 $c=2$, 故圆 $C$ 的方程为
    \[(x-2)^2+ y^2=4.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设圆 $C$ 的半径为 $2$, 圆心在直线 $l_1\colon y=2x$ 上, 且截直线 $l_2\colon x-y-1=0$ 所得弦长为 $2\sqrt2$, 求圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    由垂径定理, 点 $C$ 到直线 $l_2$ 的距离为 $\sqrt2$. 设 $C(c,2c)$, 则
    \[\frac{|c- 2c- 1|}{\sqrt2}= \sqrt2,\quad c=1,-3.\]
    故圆 $C$ 的方程为
    \[\begin{aligned}
        &(x-1)^2+ (y-2)^2= 4,\\
        \text{或\ }&(x+3)^2+ (y+6)^2= 4.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知圆 $M$ 经过 $A(1,-2)$, $B(-1,0)$ 两点, 且在个两坐标轴上的四个截距之和为 $2$, 求圆 $M$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设圆 $M$ 的一般式为
    \[x^2+y^2+Dx+Ey+F= 0\quad (D^2+E^2-4F>0).\]
    圆 $M$ 在 $x$ 轴上的截距满足 $x^2+Dx+F=0$ (即令 $y=0$), 和为 $-D$ (韦达定理), 同样可知, 圆 $M$ 在 $y$ 轴上的截距之和为 $-E$, 则 $-D-E=2$. 将点 $A(1,-2)$, $B(-1,0)$ 代入圆 $M$ 的方程,
    \[\left\{\!\!\begin{array}{l}
        5+D-2E+F=0,\\
        1-D+F=0,
    \end{array}\right.\]
    解得, $D=-2$, $E=0$, $F=-3$, 满足 $D^2+E^2- 4F>0$. 所以圆 $M$ 的方程为
    \[x^2+y^2-2x-3=0.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    圆 $C$ 满足: 截 $y$ 轴所得的弦长为 $2$; 被 $x$ 轴分成两段圆弧, 其弧长比为 $3:1$; 圆心到直线 $l\colon x-2y=0$ 的距离为 $\dfrac{\sqrt5}5$. 求圆 $C$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设圆 $C$ 的半径为 $r$, $C(a,b)$, 由垂径定理, $1^2+a^2= r^2$. 又设圆 $C$ 与 $x$ 轴交于点 $A$,$B$, 则 $\angle ACB= 90^\circ$, 再由垂径定理, $\sqrt2|b|= r$, 所以 $1+a^2= 2b^2$. 由点 $C$ 到 $l$ 的距离为 $\dfrac{\sqrt5}5$ 知
    \[\frac{\sqrt5}5= \frac{|a-2b|}{\sqrt5},\quad a-2b= \pm1.\]
</p>

<p>
    若 $a-2b= 1$, 代入 $1+a^2= 2b^2$ 知, $a=b=-1$, 则 $r=\sqrt2$, 圆 $C$ 的方程为 
    \[(x+1)^2+ (y+1)^2= 2.\]
</p>

<p>
    若 $a-2b= -1$, 则 $a=b=1$, $r=\sqrt2$, 而圆 $C$ 的方程为 
    \[(x-1)^2+ (y-1)^2= 2.\]
</p>
</mysolution>
