\sectioncounter{30}
</p>

<p>
\section{一元二次不等式}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
把两个代数式用不等号连接, 就得到不等式, 如 $a>b$, $x^2\leqslant x+1$ 等. 不等式主要用来表示两个式子的大小关系, 且
\[a>b\Leftrightarrow a-b>0,\quad a< b\Leftrightarrow a-b< 0.\]
这两个等价关系也蕴含了比较两个式子大小的方法: 两个式子的大小可转化为两式之差与零的大小, 而后者的判断一般应考虑两式之差的值域. 不等式有与等式类似的性质, 如两边加同一个式子, 不等号方向不变. 需注意, 不等号两边乘同一个负数, 不等号方向改变 (为什么?). 所以不能认为 $\dfrac1a>\dfrac1b \Leftrightarrow b>a$, 而应根据 $a$, $b$ 取值范围判断 (此时可结合反比例函数的图形).
</p>

<p>
形如 $ax^2+bx+c>0$ 或 $ax^2+bx+c\geqslant0$ 的不等式称为关于 $x$ 的二次不等式. 解二次不等式时, 一般先把不等号左边的式子因式分解, 再借助对应二次函数的图形来确定不等式的解集. 如 
\[x^2-x-2>0\Rightarrow (x+1)(x-2)>0,\]
由图形知 $x< -1$ 或 $x>2$. 为了方便应用此方法, 通常把二次项系数化为正数, 如 $-2x^2-x+1\geqslant 0$ 化为 $2x^2+x-1\leqslant 0$ (注意不等号方向变了). 此外, 二次不等式解集的端点就是对应二次方程的解.
</p>

<p>
上述方法也可以从代数角度理解. 对 $(x+1)(x-2)>0$, 以零点为分界点划分 $x$ 的取值范围, 并列出下表
\[\small\begin{array}{c|ccc}
    x & (-\infty,-1) & (-1,2) & (2,+\infty) \\
    \hline
    x+1 & - & + & + \\
    x-2 & - & - & + \\
    (x+1)(x-2) & + & - & +
\end{array}\]
可知解集为 $(-\infty,-1)\cup(2,+\infty)$. 注意表中略去了零点. 用同样的方法可以知 $(\mathrm{e}^x-1)(x-3)\leqslant 0$ 的解集为 $[0,3]$.
</p>

<p>
形如 $\dfrac{ax+b}{cx+d}>0$ 的关于 $x$ 的不等式也可以转化为二次不等式, 如不等式 $\dfrac{x-2}{x-3}>0$ 等价于 $(x-2)(x-3)>0$. 注意,
\[\frac{x-2}{x-3}\geqslant 0\Leftrightarrow \left\{\!\!\begin{array}{l}
    (x-2)(x-3)\geqslant 0,  \\
    x-3\neq 0.
\end{array}\right.\]
</p>

<p>
指数不等式、对数不等式、三角不等式大都需要结合对应函数的单调性来求解, 如
\[2^x>8\Rightarrow x>3,\quad
    \log_3 x< 2\Rightarrow 0< x< 9.\]
更一般地, 若函数 $f(x)$ 单调递增, 则
\[f(x_1)>f(x_2)\Rightarrow x_1>x_2.\]
</p>

<p>
\lianxi
</p>

<p>
<myexercise>
    <p>    解不等式: $(x-1)(x-2)>0$.
</p>
</myexercise>
<mysolution>
    <p>
    $x\in(-\infty,1)\cup (2,+\infty)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    解不等式: $-3x^2 +5x+2>0$.
</p>
</myexercise>
<mysolution>
    <p>
    先将二次项系数化为正数, 再分解因式,
    \[3x^2- 5x- 2< 0,\quad (3x+1)(x-2)< 0,\]
    则 $x\in\biggl(-\dfrac13,2\biggr)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    解不等式: $2^{x^2-2x}< 8$.
</p>
</myexercise>
<mysolution>
    <p>
    先化同底, 再利用指数函数单调性,
    \[2^{x^2-2x}< 2^3,\quad x^2-2x< 3,\]
    解得 $x\in (-1,3)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    解不等式 $\dfrac{x-1}x\geqslant 2$.
</p>
</myexercise>
<mysolution>
    <p>
    先移项、合并, 化为与 $0$ 比大小,
    \[\frac{x-1}x- 2\geqslant 0,\quad 
    \frac{-x-1}{x}\geqslant 0,\]
    再去负号、去分母,
    \[\frac{x+1}{x}\leqslant 0,\quad
    x(x+1)\leqslant 0\ \text{且}\ x\neq 0,\]
    解得 $x\in [-1,0)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若不等式 $ax^2 +bx-1>0$ 的解集是 $\{x\mid 3< x< 4\}$, 求 $a,b$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $3$ 和 $4$ 为对应的方程 $ax^2 +bx-1= 0$ 的两根, 由韦达定理,
    \[3+4= -\frac{b}{a},\quad 3\cdot 4= \frac{-1}a,\]
    解得 $a= -\dfrac1{12}$, $b=\dfrac{7}{12}$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{一元二次不等式的解法}
<span id="example-"></span>
<myexample>
    <p>
    (1) 解不等式: $-3x^2 +4x+4< 0$;
</p>

<p>
    (2) 解关于 $x$ 的不等式: $x^2 -(2a+1)x+a(a+1)< 0$.
</p>
</myexample>
<mysolution>
    <p>
    (1) 先将二次项系数化为正数, 再分解因式,
    \[3x^2- 4x- 4>0,\quad (3x+2)(x-2)>0,\]
    解得 $x\in\biggl(-\infty,-\dfrac23\biggr)\cup (2,+\infty)$.
</p>

<p>
    (2) 先分解因式, 再比较两根大小,
    \mymarginpar{若两根为 $2a$ 和 $a+1$, 则需分类讨论.}
    \[(x-a)(x-(a+1))< 0,\quad x\in(a,a+1).\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    解不等式: $(x-2)(x+3)>6$.
</p>
</myexercise>
<mysolution>
    <p>
    化为与 $0$ 比较并整理,
    \[x^2+x-12> 0,\quad (x-3)(x+4)>0,\]
    解得 $x\in(-\infty,-4)\cup (3,+\infty)$.
</p>
</mysolution>
</p>

<p>
\subsubsection{比较两个式子的大小}
<span id="example-"></span>
<myexample>
    <p>
    设 $a_1,a_2< 1$, 比较 $a_1a_2$ 与 $a_1+a_2-1$ 的大小.
</p>
</myexample>
<mysolution>
    <p>
    直接作差, 并分解因式,
    \[a_1a_2-(a_1+a_2-1)= (a_1-1)(a_2-1).\]
    由 $a_1,a_2< 1$ 知, $a_1-1< 0$, $a_2-1< 0$, 则
    \[(a_1-1)(a_2-1)>0,\quad a_1a_2> a_1+a_2-1.\]
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    设 $x+y+z=0$, $xyz>0$, 比较 $\dfrac1x+\dfrac1y+\dfrac1z$ 与 $0$ 的大小.
</p>
</myexample>
<mysolution>
    <p>
    由 $xyz>0$ 知, $x,y,z$ 均为正数或一正两负, 结合 $x+y+z=0$ 知, $x,y,z$ 一正两负. 不妨设 $x>0$, $y,z< 0$, 由 $x+y= -z$ 知, 
    \mymarginpar{由已知条件大致确定未知数的正负号, 可以简化推理.}
    \[\frac1x+ \frac1y= \frac{x+y}{xy}= \frac{-z}{xy}< 0,\]
    而 $\dfrac1z< 0$, 所以 $\dfrac1x+\dfrac1y+\dfrac1z< 0$.
</p>
</mysolution>
</p>

<p>
\lianxi
</p>

<p>
<myexercise>
    <p>    设 $a,b,c>0$, 比较 $\dfrac{b}a$ 与 $\dfrac{b+c}{a+c}$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    作差并整理, 
    \[\frac{b}a- \frac{b+c}{a+c}
    = \frac{c(b-a)}{a(a+c)}.\]
    由已知, $a(a+c)>0$ 且 $c>0$, 所以当 $b-a< 0$ 即 $b< a$ 时, 
    \[\frac{b}a- \frac{b+c}{a+c}< 0,\quad
    \frac{b}a< \frac{b+c}{a+c};\]
    当 $b=a$ 时, $\dfrac{b}a= \dfrac{b+c}{a+c}$; 当 $b>a$ 时, $\dfrac{b}a> \dfrac{b+c}{a+c}$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    解不等式: $2x^2 -x-1>0$.
</p>
</myexercise>
<mysolution>
    <p>
    $x\in\biggl(-\infty,-\dfrac12\biggr)\cup (1,+\infty)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知一元二次不等式 $f(x)< 0$ 的解集为 $\{x\mid x< -1\ \text{或}\ x> 1\}$, 求 $f(10^x)>0$ 的解集.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $f(x)>0$ 的解集为 $(-1,1)$, 而 $f(10^x)>0$ 的解集满足 $10^x\in (-1,1)$, 解得 $x\in (-\infty,0)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    解不等式: $\dfrac{\mathrm{e}^x-2}{x+4}>0$.
</p>
</myexercise>
<mysolution>
    <p>
    列表可知, $x\in (-\infty,-4)\cup (\ln 2,+\infty)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $x>0$, 比较 $\dfrac{x^2+1}x$ 与 $2$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    作差并整理,
    \[\frac{x^2+1}x- 2= \frac{(x-1)^2}{x}\geqslant 0,\]
    所以 $\dfrac{x^2+1}x\geqslant 2$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    解不等式: $\dfrac{x-1}{x+2}< 0$.
</p>
</myexercise>
<mysolution>
    <p>
    $x\in (-2,1)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    解不等式 $(x-2)(x+3)< -4$.
</p>
</myexercise>
<mysolution>
    <p>
    整理为与 $0$ 比大小, 可以解得 $x\in (-2,1)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知不等式 $x^2 +3x+a>0$ 的解集是 $\{x\mid x< -2\ \text{或}\ x>-1\}$, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由韦达定理, $a= (-1)\cdot (-2)= 2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $a,b>0$, 比较 $a-\dfrac1a$ 与 $b-\dfrac1b$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 作差并整理,
    \[\begin{aligned}
        a-\frac1a- \biggl(b-\frac1b\biggl)
        &= a-b+ \frac{a-b}{ab}\\
        &= (a-b)\biggl(1+\frac1{ab}\biggr).
    \end{aligned}\]
    由已知, $1+\dfrac1{ab}>0$, 则当 $a-b>0$ 即 $a>b$ 时,
    \[a-\frac1a- \biggl(b-\frac1b\biggl)>0,\quad
    a-\frac1a> b-\frac1b;\]
    当 $a=b$ 时, $a-\dfrac1a= b-\dfrac1b$; 当 $a< b$ 时, $a-\dfrac1a< b-\dfrac1b$.
</p>

<p>
    方法二: 容易知道, 函数 $f(x)= x- \dfrac1x$
    \mymarginpar{用同样的方法可以比较 $3^x+ 4^x$ 与 $25$ 的大小.}
    在 $(0,+\infty)$ 上单调递增. 因为 $a-\dfrac1a= f(a)$, $b-\dfrac1b= f(b)$, 所以答案同上. 
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若关于 $x$ 的不等式 $x^2 -2ax-8a^2 < 0$ ($a>0$) 的解集为 $(x_1,x_2)$, 且 $x_2-x_1=12$, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    解不等式可知, $x\in (-2a,4a)$, 所以
    \[x_1= -2a, x_2= 4a,\quad x_2-x_1= 6a.\]
    由 $x_2-x_1=12$ 知 $a= 2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $a\in\mathbb{Z}$, 关于 $x$ 的一元二次不等式 $x^2 -6x+a\leqslant0$  的解集中有且仅有 $3$ 个整数, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 作二次函数 $f(x)= x^2 -6x+a$ 的图形可知, 对称轴为 $x=3$, 所以 $3$ 个整数解为 $2,3,4$. 当 $f(2)= 0$ 时, $a=8$; 当 $f(1)= 0$ 时, $a=5$. 由 $a$ 表示图形的纵截距知, $a\in (5,8]$.
</p>

<p>
    方法二: 原不等式化为
    \[(x-3)^2\leqslant 9-a,\quad |x-3|\leqslant \sqrt{9-a},\]
    由题意, 
    \[\sqrt{9-a}\in [1,2),\quad a\in(5,8].\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设函数 $f(x)=\begin{cases}
      x^2+1, & x\geqslant 0,\\
      1, & x< 0,\end{cases}$
    解不等式: $f(3-x^2)>f(2x)$.
</p>
</myexercise>
<mysolution>
    <p>
    $f(x)$ 单调递增, 则原不等式等价于
    \[3-x^2> 2x,\quad x\in (-3,1).\]
</p>
</mysolution>