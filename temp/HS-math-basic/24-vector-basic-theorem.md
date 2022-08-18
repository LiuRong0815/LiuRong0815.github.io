\sectioncounter{23}
</p>

<p>
\section{平面向量基本定理及向量坐标表示}
</p>

<p>
\subsection{知识梳理}
两个向量 $\bm{a}$, $\bm{b}$ 的线性组合指形如 $k_1\bm{a}+k_2\bm{b}$ 的向量. 平面向量基本定理表明若 $\bm{a}$, $\bm{b}$ 不共线, 则任意 $\bm{c}$ 可表示为 $k_1\bm{a}+k_2\bm{b}$, 其中 $k_1$, $k_2$ 由 $\bm{c}$ 唯一确定. 
定理中不共线的 $\bm{a}$, $\bm{b}$ 也称为平面中所有向量的一个 (组) 基. 该定理说明在解向量题时, 应该尽可能用两个不共线的向量表示其他所有向量.
</p>

<p>
为了更方便地表示向量, 可把向量放在平面直角坐标系中考虑, 并取从原点分别指向 $(1,0)$ 和 $(0,1)$ 的两个单位向量 $\bm{i}$ 和 $\bm{j}$ 为基向量.
当把任意向量 $\bm{c}$ 表示为 $x\bm{i}+y\bm{j}$ 时, 定义其坐标为 $(x,y)$,
并记为 $\bm{c}=(x,y)$. 若平移 $\bm{c}$ 使其起点为原点, 
可知此时终点坐标恰为 $(x,y)$, 即 $A(x_A,y_A)\Leftrightarrow\overrightarrow{OA}=(x_A,y_A)$.
设 $\bm{a}=(x_1,y_1)$, $\bm{b}=(x_2,y_2)$, 则可知 
\[\bm{a}\pm\bm{b}= (x_1\pm x_2,y_1\pm y_2),\quad
    k\bm{a}= (kx_1,ky_1).\]
也可统一写为 $m\bm{a}+n\bm{b}= (mx_1+nx_2,my_1+ny_2)$. 
</p>

<p>
设点 $A(x_A,y_A)$, $B(x_B,y_B)$, 则有 
\[\overrightarrow{AB}
    = \overrightarrow{OB}- \overrightarrow{OA}
    = (x_B-x_A,y_B-y_A).\]
由勾股定理可得 $\bm{a}$ 的长度 $|\bm{a}|=\sqrt{x_1^2+y_1^2}$,
所以知两点 $A(x_A,y_A)$, $B(x_B,y_B)$ 间距离公式
\[|\overrightarrow{AB}|
    = \sqrt{(x_A-x_B)^2+(y_A-y_B)^2}.\]
</p>

<p>
因为数学中的向量只考虑自由向量, 所以两个向量平行等价于两者共线, 即非零向量 $\bm{a}$ 和 $\bm{b}$ 满足 $\bm{a}\parallel\bm{b}$ 的充要条件是存在 $k$ 使得 $\bm{a}=k\bm{b}$. 此式可化为
\[(x_1,y_1)=k(x_2,y_2), \text{\ 即\ } x_1y_2=x_2y_1,
    \text{\ 简记为\ } \frac{x_1}{x_2}=\frac{y_1}{y_2},\]
也就是两个向量对应坐标分量成比例.
更一般的情形是, 选取平面向量的任意一个基 $\bm{i}$, $\bm{j}$, 
将非零向量 $\bm{a}$ 和 $\bm{b}$ 分别表示为 $x_1\bm{i}+y_1\bm{j}$
和 $x_2\bm{i}+y_2\bm{j}$, 则 
\[\bm{a}\parallel\bm{b}\Leftrightarrow 
    x_1y_2=x_2y_1, \text{\ 仍简记为\ } 
    \frac{x_1}{x_2}=\frac{y_1}{y_2}.\]
</p>

<p>
\lianxi
<myexercise>
    <p>    已知向量 $\bm{a}=(1,2)$, $\bm{b}=(3,1)$, 求 $|2\bm{a}+3\bm{b}|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $2\bm{a}+3\bm{b}= (11,7)$ 可得, $|2\bm{a}+3\bm{b}|=\sqrt{170}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $A(1,2)$, $B(4,2)$, 向量 $\bm{a}=(x+y,x-2y)=\overrightarrow{AB}$, 求 $x-y$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\overrightarrow{AB}= (3,0)$, 所以
    \[\left\{\!\!\begin{array}{l}
        x+y= 3,\\
        x-2y= 0,
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        x=2,\\
        y=1,
    \end{array}\right.\]
    则 $x-y=1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $A(1,-3)$ 和向量 $\bm{a}=(3,4)$. 若 $\overrightarrow{AB}=2\bm{a}$, 求点 $B$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: $\overrightarrow{OB}= \overrightarrow{OA}+\overrightarrow{AB}= (7,5)$.
</p>

<p>
    方法二: 设 $B(x_B,y_B)$, 则已知等式化为
    \[(x_B-1,y_B+3)= 2(3,4),\quad\text{解得}\quad
        B(7,5).\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知向量 $\bm{a}=(5,12)$, $\bm{b}=(\sin\alpha,\cos\alpha)$, 
    且 $\bm{a}\parallel\bm{b}$, 求 $\tan\alpha $ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $5\cos\alpha= 12\sin\alpha$, 则 $\tan\alpha= \dfrac5{12}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $P_1(1,3)$, $P_2(4,-6)$, $P$ 是直线 $P_1P_2$ 上的一点, 且 $\overrightarrow{P_1P}= 2\overrightarrow{PP_2}$, 求点 $P$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 已知等式化为
    \[\begin{gathered}
        \overrightarrow{OP}-\overrightarrow{OP_1}
        = 2(\overrightarrow{OP_2}- \overrightarrow{OP}),\\
        \overrightarrow{OP}
        = \frac13\overrightarrow{OP_1}+ \frac23\overrightarrow{OP_2}
        = (3,-3).
    \end{gathered}\]
</p>

<p>
    方法二: 设 $P(x_P,y_P)$, 则已知等式化为
    \[(x_P-1,y_P-3)= 2(4-x_P,y_P+6),\]
    解得 $x_P= 3$, $y_P= -3$, 即 $P(3,-3)$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{平面向量基本定理的应用}
<span id="example-"></span>
<myexample>
    <p>
    已知 $\triangle ABC$ 中, 点 $D$, $E$ 分别为边 $AC$, $AB$ 上的点,
    且 $DA=2CD$, $EB=2AE$. 若 $\overrightarrow{BC}=\bm{a}$, 
    $\overrightarrow{CA}=\bm{b}$, 以 $\bm{a}$, $\bm{b}$ 为基向量表示 
    $\overrightarrow{DE}$.
</p>
</myexample>
<mysolution>
    <p>
    作草图, 视点 $C$ 为原点, 则
    \[\begin{aligned}
        \overrightarrow{DE}
        &= \overrightarrow{CE}- \overrightarrow{CD}
         = \frac13\overrightarrow{CB}+ \frac23\overrightarrow{CA}
            - \frac13\overrightarrow{CA}\\
        &= \frac13(\overrightarrow{CA}+ \overrightarrow{CB})
         = \frac13(\bm{b}- \bm{a}).
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知平行四边形 $ABCD$ 中, 边 $BC$, $CD$ 的中点分别为点 $E$, $F$.
    设 $\overrightarrow{AB}=\bm{m}$, $\overrightarrow{AD}=\bm{n}$,
    用 $\bm{m}$, $\bm{n}$ 表示 $\overrightarrow{AE}$ 和 $\overrightarrow{EF}$.
</p>
</myexercise>
<mysolution>
    <p>
    作草图, 视点 $A$ 为原点, 则
    \mymarginpar{此题也可以先求 $\overrightarrow{BD}$, 再利用 $\overrightarrow{EF}= \dfrac12\overrightarrow{BD}$.}
    \[\begin{gathered}
        \overrightarrow{AE}
        = \overrightarrow{AB}+ \overrightarrow{BE}
        = \bm{m}+ \frac12\bm{n},\\
        \overrightarrow{AF}
        = \overrightarrow{AD}+ \overrightarrow{DF}
        = \bm{n}+ \frac12\bm{m},
    \end{gathered}\]
    故 $\overrightarrow{EF}= \overrightarrow{AF}- \overrightarrow{AE}= \dfrac12(\bm{n}- \bm{m})$.
</p>
</mysolution>
</p>

<p>
\subsubsection{平面向量的坐标运算}
<span id="example-"></span>
<myexample>
    <p>
    已知点 $A(-2,4)$, $B(3,-1)$, $C(-3,-4)$. 设 $\overrightarrow{AB}=\bm{a}$, $\overrightarrow{BC}=\bm{b}$, $\overrightarrow{CA}=\bm{c}$, 且 $\overrightarrow{CM}=3\bm{c}$, $\overrightarrow{CN}=-2\bm{b}$.
</p>

<p>
    (1) 求 $3\bm{a}+\bm{b}-3\bm{c}$;\qquad
    (2) 求满足 $\bm{a}=m\bm{b}+n\bm{c}$ 的实数 $m$, $n$;
</p>

<p>
    (3) 求点 $M$ 及向量 $\overrightarrow{MN}$ 的坐标.
</p>
</myexample>
<mysolution>
    <p>
    (1) 因为 $\bm{a}= (5,-5)$, $\bm{b}= (-6,-3)$, $\bm{a}= (1,8)$, 所以 $3\bm{a}+\bm{b}-3\bm{c}= (6,-42)$.
</p>

<p>
    (2) 因为 $\bm{a}+\bm{b}+\bm{c}= \bm{0}$, 所以 $\bm{a}= -\bm{b}-\bm{c}$, 即 $m=n=-1$.
</p>

<p>
    (3) 设 $M(x_M,y_M)$, 则 $\overrightarrow{CM}=3\bm{c}$ 化为
    \[(x_M+3,y_M+4)= (3,24),\quad\text{解得}\quad
        x_M= 0,\ y_M= 20,\]
    即 $M(0,20)$. 由此可得
    \[\overrightarrow{MN}
        = \overrightarrow{CN}- \overrightarrow{CM}
        = -2\bm{b}- 3\bm{c}= (9,-18).\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知点 $A(1,1)$, $B(2,3)$, $C(3,2)$, 点 $P(x,y)$ 满足 
    $\overrightarrow{PA}+ \overrightarrow{PB}+ \overrightarrow{PC}=\bm{0}$, 求 $|\overrightarrow{OP}|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    已知等式化为
    \mymarginpar{已知等式表明点 $P$ 为 $\triangle ABC$ 的重心 (三条中线的公共点).}
    \[\begin{gathered}
        (\overrightarrow{OA}- \overrightarrow{OP})
        + (\overrightarrow{OB}- \overrightarrow{OP})
        + (\overrightarrow{OC}- \overrightarrow{OP})= \bm{0},\\
        \overrightarrow{OP}
        = \frac13(\overrightarrow{OA}+ \overrightarrow{OB}+ \overrightarrow{OC})
        = (2,2),
    \end{gathered}\]
    故 $|\overrightarrow{OP}|= 2\sqrt2$.
</p>
</mysolution>
</p>

<p>
\subsubsection{向量的平行 (共线)}
<span id="example-"></span>
<myexample>
    <p>
    设向量 $\overrightarrow{OA}=(k,12)$, $\overrightarrow{OB}=(4,5)$, 
    $\overrightarrow{OC}=(10,k)$, 当 $k$ 为何值时, $A$, $B$, $C$ 三点共线?
</p>
</myexample>
<mysolution>
    <p>
    $\overrightarrow{BA}= (k-4,7)$, $\overrightarrow{BC}= (6,k-5)$, 而 $A$, $B$, $C$ 三点共线表明 $\overrightarrow{BA}\parallel \overrightarrow{BC}$, 所以
    \[(k-4)(k-5)= 7\cdot 6,\quad\text{解得}\quad k=-2\ \text{或}\ 11.\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知 $\overrightarrow{OA}$, $\overrightarrow{OB}$ 不共线, 
    $\overrightarrow{OP}= a\overrightarrow{OA}+ b\overrightarrow{OB}$,
    验证: $A$, $P$, $B$ 三点共线的充要条件是 $a+b=1$.
</p>
</myexercise>
<mysolution>
    <p>
    $A$, $P$, $B$ 三点共线等价于 $\overrightarrow{AP}\parallel \overrightarrow{AB}$.
    \mymarginpar{本题的结论在解选择题或填空题时, 可以直接使用.}
</p>

<p>
    若 $\overrightarrow{AP}\parallel \overrightarrow{AB}$, 则存在 $\lambda$, 使得 $\overrightarrow{AP}= \lambda\overrightarrow{AB}$. 将此式用以 $O$ 为起点的向量表示, 整理得
    \[\overrightarrow{OP}= 
    (1-\lambda)\overrightarrow{OA}+ \lambda\overrightarrow{OB},\]
    所以 $a= 1-\lambda$, $b= \lambda$, 满足 $a+b=1$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    已知 $\bm{a}=(1,y)$, $\bm{b}=(x,-2)$, 且 $2\bm{a}-3\bm{b}=(5,8)$, 求 $x+y$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[\left\{\!\!\begin{array}{l}
        2-3x= 5,\\
        2y+6= 8,
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        x=-1,\\
        y=1,
    \end{array}\right.\]
    所以 $x+y=0$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若向量 $\overrightarrow{AB}=(1,2)$, $\overrightarrow{BC}=(3,4)$,
    求 $\overrightarrow{AC}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\overrightarrow{AC}= \overrightarrow{AB}+ \overrightarrow{BC}= (4,6)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $M(3,-2)$, $N(-5,4)$. 若 $\overrightarrow{MP}
      =\dfrac12\overrightarrow{MN}$, 求点 $P$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    等式化为 $\overrightarrow{OP}- \overrightarrow{OM}= \dfrac12(\overrightarrow{ON}- \overrightarrow{OM})$, 所以
    \[\overrightarrow{OP}
        = \frac12(\overrightarrow{OM}+ \overrightarrow{ON})
        = (-1,1).\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知向量 $\bm{a}=(1,k)$, $\bm{b}=(9,k-6)$. 若 $\bm{a}\parallel\bm{b}$, 求实数 $k$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $1\cdot(k-6)= k\cdot 9$, 则 $k= -\dfrac34$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
</p>

<p>
<myexercise>
    <p>    已知 $\overrightarrow{AB}=(3,4)$, 点 $A$ 的坐标为 $(2,1)$, 求点 $B$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    $\overrightarrow{OB}= \overrightarrow{OA}+ \overrightarrow{AB}= (5,5)$, 即 $B(5,5)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若向量 $\bm{a}=(1,1)$, $\bm{b}=(1,-1)$, $\bm{c}=(-1,-3)$, 
    用 $\bm{a}$, $\bm{b}$ 表示 $\bm{c}$.
</p>
</myexercise>
<mysolution>
    <p>
    设 $\bm{c}= \lambda\bm{a}+ \mu\bm{b}$, 则
    \[(-1,-3)= (\lambda+\mu,\lambda-\mu),\]
    解得 $\lambda= -2$, $\mu=1$, 所以 $\bm{c}= -2\bm{a}+ \bm{b}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\bm{a}+\bm{b}=(2,-8)$, $\bm{a}-\bm{b}=(-8,6)$, 求 $\bm{a}$, $\bm{b}$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    联立可解得 $\bm{a}= (-3,-1)$, $\bm{b}= (5,-7)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $M(3,2)$, $N(1,2)$, 向量 $\bm{a}=(x+3,x-3y+4)$ 与 $\overrightarrow{NM}$ 相等, 求实数 $y$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\overrightarrow{NM}= (2,0)$, 所以
    \[\left\{\!\!\begin{array}{l}
        x+3= 2,\\
        x-3y+4= 0,
    \end{array}\right.\ \text{解得}\ y=1.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $A(6,2)$, $B(1,14)$, 求与 $\overrightarrow{AB}$ 共线的单位向量.
</p>
</myexercise>
<mysolution>
    <p>
    $\overrightarrow{AB}= (5,12)$, 而所求单位向量为 $\pm\biggl(\dfrac5{13}, \dfrac{12}{13}\biggr)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知点 $A(-1,2)$, $B(2,8)$, $\overrightarrow{AC}= \dfrac13\overrightarrow{AB}$, $\overrightarrow{DA}= -\dfrac23\overrightarrow{BA}$, 求点 $C$ 和 $\overrightarrow{CD}$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    由 $\overrightarrow{AC}= \dfrac13\overrightarrow{AB}$ 知
    \[\overrightarrow{OC}
        = \frac23\overrightarrow{OA}+ \frac13\overrightarrow{OB}
        = (0,4),\]
    即 $C(0,4)$. 而由 $\overrightarrow{DA}= -\dfrac23\overrightarrow{BA}$ 知
    \[\overrightarrow{OD}
        = \frac13\overrightarrow{OA}+ \frac23\overrightarrow{OB},\]
    所以
    \[\overrightarrow{CD}
        = \overrightarrow{OD}- \overrightarrow{OC}
        = \frac13(\overrightarrow{OB}- \overrightarrow{OA})
        = (1,2).\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在平面直角坐标系中, $O$ 为原点, $A(-1,0)$, $B(0,\sqrt3)$, $C(3,0)$, 
    动点 $D$ 满足 $|\overrightarrow{CD}|=1$, 求 $|\overrightarrow{OA}
      + \overrightarrow{OB}+ \overrightarrow{OD}|$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[\begin{aligned}
        \overrightarrow{OA}+ \overrightarrow{OB}+ \overrightarrow{OD}
        &= (-1,\sqrt3)+ \overrightarrow{OC}+ \overrightarrow{CD}\\
        &= (2,\sqrt3)+ \overrightarrow{CD},
    \end{aligned}\]
    再由 $|\overrightarrow{CD}|=1$ 知, 所得向量终点的轨迹是以点 $(2,\sqrt3)$ 为圆心, 以 $1$ 为半径的圆. 画草图可知, 所求向量长度的最大值为 $\sqrt7+1$.
</p>
</mysolution>