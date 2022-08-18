\sectioncounter{39}
</p>

<p>
\section{两条直线的平行与垂直}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
两条直线平行等价于它们的倾斜角相等, 由斜率与倾斜角的关系可知, 不竖直的两条直线平行等价于它们的斜率相等. 两条直线垂直等价于它们的倾斜角相差 $90^\circ$. 设直线 $l_1\perp l_2$, 倾斜角分别为 $\alpha_1$,$\alpha_2$ (均不为 $90^\circ$), 且不妨设 $\alpha_1=\alpha_2+90^\circ$. 又设 $l_1$,$l_2$ 的斜率分别为 $k_1$,$k_2$, 则 
\[k_1=\tan\alpha_1=\tan(\alpha_2+90^\circ)
    = -\cot\alpha= -\frac1{k_2},\]
即 $k_1k_2=-1$, 也称 $k_1$,$k_2$ 互为负倒数.
</p>

<p>
上述结论也可以用直线一般式的系数表示. 设 
\[l_1\colon A_1x+B_1y+C_1=0,\\
    l_2\colon A_2x+B_2y+C_2=0,\]
且不妨假设 $A_1B_1A_2B_2\neq 0$, 则 $l_1$,$l_2$ 的斜率分别为 $-\dfrac{A_1}{B_1}$,$-\dfrac{A_2}{B_2}$, 且
\begin{gather*}
    l_1\parallel l_2
      \Leftrightarrow -\frac{A_1}{B_1}=-\frac{A_2}{B_2}
      \Leftrightarrow A_1B_2=A_2B_1,\\
    l_1\perp l_2
      \Leftrightarrow \Bigl(-\frac{A_1}{B_1}\Bigr)\Bigl(-\frac{A_2}{B_2}\Big)= -1
      \Leftrightarrow A_1A_2+B_1B_2=0.
\end{gather*}
在使用这两组公式时, 按上一段中的斜率关系列式即可. 解题时, 常利用平行或垂直时一般式中系数的关系来简化列式. 如与直线 $l\colon 2x+3y+1=0$ 平行的直线可设为 $2x+3y+C=0$ ($C\neq 1$), 而与 $l$ 垂直的直线可设为 $3x-2y+C=0$, 其中 $C$ 为待定系数.
</p>

<p>
利用倾斜角的正切为斜率可以用几何法推得点 $(x_0,y_0)$ 到直线 $l\colon Ax+By+C=0$ 的距离
\[d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}.\]
推导此公式也可用两点间距离公式和二次函数求最值 (计算略复杂) 或向量的投影 (先确定直线的法向量). 设 $l_1\parallel l_2$, 且
\[l_1\colon Ax+By+C_1= 0,\quad l_2\colon Ax+By+C_2= 0,\]
则 $l_1$ 与 $l_2$ 之间的距离为 $\dfrac{|C_1-C_2|}{\sqrt{A^2+B^2}}$.
</p>

<p>
\lianxi
<myexercise>
    <p>    设直线 $l_1$ 过点 $(-1,3)$, 且平行于直线 $l_2\colon x-2y+3=0$, 求 $l_1$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设 $l_1\colon x-2y+C=0$ ($C\neq 3$), 将点 $(-1,3)$ 代入, $C=7$, 则 $l_1\colon x-2y+7=0$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设直线 $l_1$ 过点 $(3,4)$, 且垂直于直线 $l_2\colon 2x+3y-21=0$,求 $l_1$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设 $l_1\colon 3x-2y+C=0$, 将点 $(3,4)$ 代入, $C=-1$, 则 $l_1\colon 3x-2y-1=0$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若动点 $P$ 在直线 $l\colon x+2y-5=0$ 上, $O$ 为原点, 求 $|OP|$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    $|OP|$ 的最小值为点 $O$ 到直线 $l$ 的距离 $\dfrac5{\sqrt5}= \sqrt5$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知直线 $l_1\colon x+y+2=0$, 点 $M(1,5)$ 关于 $l_1$ 的对称点为 $N$, 直线 $l_2\colon y=3x+2$ 关于 $l_1$ 对称的直线为 $l_3$, 求 $N$ 的方程和 $l_3$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设 $N(a,b)$, 则线段 $MN$ 的中点 $\biggl(\dfrac{1+a}2, \dfrac{5+b}2\biggr)$ 在 $l_1$ 上且 $MN\perp l_1$ (即 $l_1$ 为线段 $MN$ 的中垂线), 所以
    \mymarginpar{$l_1$ 的倾斜角为特殊角 $135^\circ$, 点 $N$ 的坐标也可以由作图得到.}
    \[\left\{\!\!\begin{array}{l}
        \dfrac{1+a}2+ \dfrac{5+b}2+2= 0,\\
        \dfrac{b-5}{a-1}\cdot (-1)= -1,
    \end{array}\right.\ \text{则}\ 
    \left\{\!\!\begin{array}{l}
        a= -7,\\
        b= -3,
    \end{array}\right.\]
    而 $N(-7,-3)$. $l_1$ 与 $l_2$ 交点为 $P(-1,-1)$ 且在 $l_3$ 上, 而由点 $M$ 在 $l_2$ 上知点 $N$ 在 $l_3$ 上, 所以 $l_3$ 就是 $PN$, 即方程为 $x-3y-2=0$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{两直线的平行与垂直关系}
<span id="example-"></span>
<myexample>
    <p>
    (1) 若直线 $l_1 \colon ax+by=0$, $l_2 \colon (a-1)x+y+2b=0$, 且 $l_1$,$l_2$ 均平行于直线 $l_3\colon x+2y+3=0$, 求 $a$,$b$ 的值.
</p>

<p>
    (2) 若直线 
    \[\begin{gathered}
        l_1\colon (m-1)x+(2m+3)y+2=0,\\
        l_2\colon (m+2)x+(1-m)y-3=0
    \end{gathered}\]
    互相垂直, 求 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由已知, $\dfrac{a}1= \dfrac{b}2$, $\dfrac{a-1}1= \dfrac12$, 所以 $a= \dfrac32$, $b=3$. 经检验, $a$,$b$ 的值合题意.
    \mymarginpar{由平行关系解出的参数可能使得两条直线重合, 所以需要回代检验. 由垂直关系解出的参数则无需检验.}
</p>

<p>
    (2) 由题意, 
    \[(m-1)(m+2)+ (2m+3)(1-m)= 0,\]
    解得 $m=1$ 或 $-1$.
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    若直线 $l_1 \colon (3+a)x+4y=5-3a$ 与 $l_2 \colon 2x+(5+a)y=8$ 平行, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\dfrac{3+a}2= \dfrac4{5+a}$, $a=-1$ 或 $-7$. 经检验, $a=-7$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若直线 
    \[\begin{gathered}
        l_1\colon (2a+5)x+(a-2)y+4=0,\\
        l_2\colon (2-a)x+(a+3)y-1=0
    \end{gathered}\]
    互相垂直, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $(2a+5)(2-a)+ (a-2)(a+3)= 0$, $a=2$ 或 $-2$.
</p>
</mysolution>
</p>

<p>
\subsubsection{利用直线之间的关系求直线方程}
<span id="example-"></span>
<myexample>
    <p>
    已知两点 $M(0, 2)$, $N(-2, 0)$, 直线 $l\colon kx-y-2k+2=0$ ($k$ 为常数). 若点 $M$, $N$ 到直线 $l$ 的距离相等, 求 $k$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    方法一: 由点到直线的距离公式,
    \[\frac{|-2-k+2|}{\sqrt{k^2+1}}= 
    \frac{|-2k-2k+2|}{\sqrt{k^2+1}},\]
    解得 $k=1$ 或 $\dfrac13$.
</p>

<p>
    方法二: 直线 $l$ 过定点 $(2,2)$ 且斜率为 $k$. 由已知, $l\parallel MN$ 或 $l$ 过线段 $MN$ 的中点 $(-1,1)$, 对应地, $k=1$ 或 $\dfrac13$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    设直线 $l_1$ 与 $l_2\colon 3x+4y-6=0$ 平行且距离为 $2$, 求 $l_1$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    设 $l_1\colon 3x+4y+C=0$ ($C\neq -6$), 则
    \[\frac{|C-(-6)|}{\sqrt{3^2+4^2}}= 2,\quad
    C= 4\ \text{或\ } -16,\]
    所以 $l_1\colon 3x+4y+4=0$ 或 $3x+4y-16=0$.
</p>
</mysolution>
</p>

<p>
\subsubsection{关于直线(或点)的对称问题}
<span id="example-"></span>
<myexample>
    <p>
    已知点 $A(-4, 4)$, 直线 $l\colon 3x+y-2=0$.
</p>

<p>
    (1) 求点 $A$ 关于直线 $l$ 的对称点 $A'$ 的坐标;
</p>

<p>
    (2) 求直线 $l$ 关于点 $A$ 的对称直线 $l'$ 的方程.
</p>
</myexample>
<mysolution>
    <p>
    (1) 设 $A'(a,b)$, 则线段 $AA'$ 的中点在 $l$ 上且 $AA'\perp l$ (即 $l$ 为线段 $AA'$ 的中垂线), 所以
    \[\left\{\!\!\begin{array}{l}
        3\cdot \dfrac{a-4}2+ \dfrac{b+4}2- 2= 0,\\
        \dfrac{b-4}{a+4}\cdot (-3)= -1,
    \end{array}\right.\quad
    \left\{\!\!\begin{array}{l}
        a= 2,\\
        b= 6,
    \end{array}\right.\]
    因此 $A'(2,6)$.
</p>

<p>
    (2) 任取 $l'$ 上一点 $(x,y)$, 
    \mymarginpar{也可以在 $l$ 上取两点, 如 $P(0,2)$, $Q(1,5)$, 计算它们关于点 $A$ 的对称点 $P'$,$Q'$, 则直线 $P'Q'$ 就是 $l'$. 点 $(a,b)$ 关于点 $x_0,y_0$ 的对称点为 $(2x_0-a,2y_0-b)$.}
    则其关于点 $A$ 的对称点 $(-8-x,8-y)$ 在直线 $l$ 上, 所以
    \[3(-8-x)+ (8-y)- 2=0,\]
    则 $l'\colon 3x+y+18= 0$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知点 $P(3,2)$,$Q(1,4)$ 关于直线 $l$ 对称, 求 $l$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    $l$ 与直线 $PQ$ 垂直, 且过线段 $PQ$ 的中点 $(2,3)$, 则 $l\colon y=x+1$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
</p>

<p>
<myexercise>
    <p>    设直线 $l_1 \colon ax+2y=0$, $l_2 \colon x+(a+1)y+4=0$, 则“$a=1$”是“$l_1\parallel l_2$”的 $\underline{\qquad\qquad}$ 条件.
</p>
</myexercise>
<mysolution>
    <p>
    由 $l_1\parallel l_2$ 知,
    \[\frac{a}1= \frac2{a+1},\quad a=1,-2.\]
    经检验, 以上两值均使得 $l_1\parallel l_2$, 所以“$a=1$”是“$l_1\parallel l_2$”的充分不必要条件.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若过点 $P(1, 2)$ 作直线 $l$, 使点 $M(2,3)$ 和点 $N(4,-1)$ 到 $l$ 的距离相等, 求 $l$ 的斜率 $k$.
</p>
</myexercise>
<mysolution>
    <p>
    $l\parallel MN$ 或 $l$ 过线段 $MN$ 的中点 $(3,1)$, 则 $k=-2$ 或 $-\dfrac12$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知直线 $l_1$ 与 $l_2\colon x-y-1=0$ 垂直, 求 $l_1$ 的倾斜角.
</p>
</myexercise>
<mysolution>
    <p>
    $l_2$ 的斜率为 $-1$, 则 $l_1$ 的斜率为 $1$, 倾斜角为 $45^\circ$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    已知直线 $l_1 \colon x+(1+k)y=2-k$ 与 $l_2 \colon kx+2y+8=0$ 平行, 求 $k$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\dfrac1k= \dfrac{1+k}2$, $k=-2$ (舍) 或 $1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知两直线 $l_1 \colon ax-y+2a+1=0$, $l_2 \colon 2x-(a-1)y+2=0$ 互相垂直, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a\cdot 2+(a-1)= 0$, $a=\dfrac13$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    直线 $l_1$,$l_2$ 分别过点 $P(-1,3)$,$Q(2,-1)$, 且 $l_1\parallel l_2$, 求 $l_1$,$l_2$ 之间的距离 $d$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    作图可知, $d\in[0,|PQ|]= [0,5]$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $A$,$B$ 两点分别在两条互相垂直的直线 $l_1\colon 2x-y=0$ 和 $l_2\colon x+ay=0$ 上, 且线段 $AB$ 的中点为 $P\Big(0,\dfrac{10}a\Big)$, 求线段 $AB$ 的长.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $2\cdot 1+ (-1)a= a$, $a=2$, 则 $l_2\colon x+2y=0$, $P(0,5)$. 可设 $A(m,2m)$, $B(2n,-n)$, 由中点坐标公式,
    \[\left\{\!\!\begin{array}{l}
        \dfrac{m+2n}2= 0,\\
        \dfrac{2m-n}2= 5,
    \end{array}\right.\quad
    \left\{\!\!\begin{array}{l}
        m=4,\\
        n=-2.
    \end{array}\right.\]
    因此 $A(4,8)$,$B(-4,2)$, $|AB|= 10$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设直线 $l_1 \colon 3x+y=0$, $l_2 \colon x+3y-2=0$, 点 $P$ 在 $l_1$ 上, 且 $P$ 到原点的距离与到 $l_2$ 的距离相等, 求 $P$ 的坐标. 
</p>
</myexercise>
<mysolution>
    <p>
    设 $P(x,y)$, 则
    \[3x+y=0,\quad 
    \sqrt{x^2+y^2}= \frac{|x+3y-2|}{\sqrt{10}}.\]
    由前一式得 $y=-3x$, 代入后一式解得, $P(1,-3)$ 或 $\biggl(-\dfrac19,\dfrac13\biggr)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设直线 $l_1$ 过点 $A(0,1)$, $l_2$ 过点 $B(5,0)$, $l_1\parallel l_2$, 且 $l_1$ 与 $l_2$ 之间的距离为 $5$, 求 $l_1$,$l_2$ 的方程.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 若 $l_1$,$l_2$ 斜率存在, 设为 $k$, 则
    \[\begin{gathered}
        l_1\colon y=kx+1,\ \text{即}\ kx-y+1=0,\\
        l_2\colon y=k(x-5),\ \text{即}\ kx-y-5k=0,
    \end{gathered}\]
    所以
    \[\frac{|1-(-5k)|}{\sqrt{k^2+1}}= 5,\quad
    k=\frac{12}5.\]
    因此 $l_1\colon 12x-5y+5=0$, $l_2\colon 12x-5y-60=0$.
</p>

<p>
    (2) 若 $l_1$,$l_2$ 斜率不存在, 则
    \mymarginpar{用直线得点斜式, 一定要讨论斜率不存在的情况.}
    \[l_1\colon x=0,\quad l_2\colon x=5,\]
    也符合题意.
</p>
</mysolution>