---
# bookCollapseSection: true
title: 不等式的性质
weight: 1
bookHidden: true
prevPage: ../../inequality
prevPageTitle: 不等式
# nextPage: ../fraction-high-order-inequality
# nextPageTitle: 分式不等式与高次不等式
---

# 不等式的性质


<p>\subsection{绝对值的几何意义}
</p>
<p>实数 $a$ 的绝对值定义为
\[|a|=\begin{cases}
  a, & a>0,\\
  0, & a=0,\\
  -a, & a< 0
  \end{cases}= \begin{cases}
    a, & a\geqslant 0,\\
    -a, & a< 0,
    \end{cases}\]
其几何意义为数轴上坐标为 $a$ 的点到原点的距离. 进而可以知道, 数轴上两点 $x_1$, $x_2$ 之间的距离为 $|x_1-x_2|$, 如下图所示.
</p>
<p><center>
  \includegraphics[scale=1]{2020-1009-2110-crop}\qquad
  \includegraphics[scale=1]{2020-1009-2120-crop}
</center>
</p>
<p>例如, $|x-1|$ 表示点 $x$ 到 $1$ 的距离; $|x+2|=|x-(-2)|$ 表示点 $x$ 到 $-2$ 的距离; $|2x-2|= 2|x-1|$ 表示点 $x$ 到 $1$ 的距离的 $2$ 倍; $|4+2x|= 2|x-(-2)|$ 表示点 $x$ 到 $-2$ 的距离的 $2$ 倍. 注意, 前面运用了绝对值的运算法则: $|ka|= |k|\,|a|$ (为什么?).
</p>
<p>再由勾股定理可知, 平面直角坐标系中两点 $A(x_A,y_A)$, $B(x_B,y_B)$ 之间的距离为
\[\begin{aligned}
  AB&= \sqrt{CD^2+EF^2}
     = \sqrt{|x_A-x_B|^2+|y_A-y_B|^2}\\
    &= \sqrt{(x_A-x_B)^2+(y_A-y_B)^2}.
\end{aligned}\]
</p>
<p><center>
  \includegraphics[scale=1]{2020-1009-2130-crop}
</center>
</p>
<p>函数 $y=|x|$ 的图象可以通过描点画图或图象变换 (即先画 $y=x$ 的图象, 再把 $x$ 轴下方的部分关于 $x$ 轴对称翻折到 $x$ 轴上方) 得到, 如下图所示:
</p>
<p><center>
  \includegraphics[scale=1]{2020-1011-1000-crop}
</center>
</p>
<p>一般的, $y= |f(x)|$ 的图象可以由 $y=f(x)$ 的图象经过变换得到, 如下图所示:
</p>
<p><center>
  \includegraphics[scale=1]{2020-1011-1010-crop}
</center>
</p>
<p>简单的带绝对值的不等式, 可以根据绝对值的几何意义直接求解. 如不等式 $|x|< 3$, 由 $|x|$ 表示点 $x$ 到原点的距离可知,  $x\in (-3,3)$; 而由不等式 $|x|\geqslant 3$, 可解得 $x\in(-\infty,-3]\cup[3,+\infty)$.
</p>
<p><myexample>
<p>解下列不等式:
  \begin{threecolpro}
    (1) $|x-1|\leqslant 2$; & (2) $|2x+1|> 3$; & (3) $|1-2x|\geqslant 5$.
  \end{threecolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 由题可将 $x-1$ 视为整体, 则 $-2\leqslant x-1\leqslant 2$, 即 $-1\leqslant x\leqslant 3$, 所以 $x\in [-1,3]$.
</p>
<p>(2) 由题, $2x+1< -3$ 或 $2x+1>3$, 即 $x< -2$ 或 $x>1$, 所以 $x\in(-\infty,-2)\cup (1,+\infty)$.
</p>
<p>(3) 由题, $1-2x\leqslant -5$ 或 $1-2x\geqslant 5$, 即 $x\geqslant 3$ 或 $x\leqslant -2$, 所以 $x\in(-\infty,-2]\cup [3,+\infty)$.
</p>
</mysolution>
</p>
<p>稍微复杂一些的带绝对值的不等式, 有的也可以根据绝对值的几何意义来求解. 只含一个绝对值的不等式, 可以按绝对值的几何意义适当讨论; 含两个绝对值的不等式, 讨论起来麻烦一点, 可以先尝试不等式两边平方.
</p>
<p><myexample>
<p>解下列不等式:
  \begin{threecolpro}
    (1) $|x+1|< 2x$; & (2) $|x-1|\geqslant 2x$; 
    & (3) $|2x+1|> |x|$.
  \end{threecolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 由题意,
  \[\left\{\!\!\begin{array}{l}
    2x>0,\\
    -2x< x+1< 2x,
  \end{array}\right.\text{解得}\ x\in(1,+\infty).\]
</p>
<p>(2) 若 $2x\leqslant 0$ 即 $x\leqslant 0$, 则不等式已成立. 
</p>
<p>若 $2x> 0$ 即 $x> 0$, 则不等式等价于 
  \[x-1\leqslant -2x\quad \text{或}\quad x-1\geqslant 2x,\]
  解得 $x\leqslant \dfrac13$ 或 $x\leqslant -1$. 结合 $x>0$ 知, 此时 $0< x\leqslant \dfrac13$. 
</p>
<p>综上所述, $x\in\biggl(-\infty,\dfrac13\biggr]$.
</p>
<p>(3) 不等式两边平方得 
  \[(2x+1)^2>x^2\quad \text{即}\quad (x+1)(3x+1)>0,\]
  解得 $x\in(-\infty,-1)\cup \biggl(\dfrac13,+\infty\biggr)$.
</p>
</mysolution>

<p>\begin{example}\label{exa:2020-1012-1900}
  解关于 $x$ 的不等式 $x^2-(2+a)x+2a< 0$.
</p>
</myexample>
<mysolution>
    <p>不等式化为 $(x-2)(x-a)< 0$, 所以根据二次函数 $y=(x-2)(x-a)$ 的图象知,
</p>
<p>若 $a< 2$, 则 $x\in (a,2)$; 
</p>
<p>若 $a=2$, 则 $x\in \varnothing$; 
</p>
<p>若 $a>2$, 则 $x\in (2,a)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:2020-1012-1900} 中关于 $x$ 的不等式虽然系数中带了参数 $a$, 但是仍然可以用因式分解的方法求得其解集. 由于系数中带了参数, 所以对应的二次函数图象由参数决定, 写解集时需要分类讨论, 讨论的主要依据是图象与 $x$ 轴交点的坐标. 再看一个复杂一点的例子.
</p>
<p>\begin{example}\label{exa:2020-1012-1910} 
  解关于 $x$ 的不等式:
  \begin{twocolpro}
    (1) $x^2+2x+ax+2a>0$; & (2) $2x^2+(2+a)x+a\geqslant 0$;\\ 
    (3) $x^2+ax-6a^2\leqslant 0$. &
  \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 不等式化为 
  \[x^2+(2+a)x+2a>0\quad\text{即}\quad (x+2)(x+a)>0,\]
  所以根据二次函数 $y=(x+2)(x+a)$ 的图象知, 
</p>
<p>若 $-a< -2$ 即 $a>2$, 则 $x\in (-\infty,-a)\cup (-2,+\infty)$; 
</p>
<p>若 $-a=-2$ 即 $a=2$, 则 $x\in \{x\mid x\neq-2\}$; 
</p>
<p>若 $-a>-2$ 即 $a< 2$, 则 $x\in (-\infty,-2)\cup (-a,+\infty)$.
</p>
<p>(2) 不等式化为 $(2x+a)(x+1)\geqslant 0$, 所以根据二次函数 $y=(2x+a)(x+1)$ 的图象知, 
</p>
<p>若 $-\dfrac{a}2< -1$ 即 $a>2$, 则 $x\in \biggl(-\infty,-\dfrac{a}2\biggr]\cup [-1,+\infty)$; 
</p>
<p>若 $-\dfrac{a}2=-1$ 即 $a=2$, 则 $x\in \realnum$; 
</p>
<p>若 $-\dfrac{a}2>-1$ 即 $a< 2$, 则 $x\in (-\infty,-1]\cup \biggl[-\dfrac{a}2,+\infty\biggr)$.
</p>
<p>(3) 不等式化为 $(x+3a)(x-2a)\leqslant 0$, 所以根据二次函数 $y=(x+3a)(x-2a)$ 的图象知, 
</p>
<p>若 $-3a< 2a$ 即 $a>0$, 则 $x\in [-3a,2a]$; 
</p>
<p>若 $-3a=2a$ 即 $a=0$, 则 $x\in \{0\}$; 
</p>
<p>若 $-3a>2a$ 即 $a< 0$, 则 $x\in [2a,-3a]$.
</p>
</mysolution>
</p>
<p>从例 \ref{exa:2020-1012-1910} 可以看出, 解系数带参数的关于 $x$ 的不等式, 步骤一般为: 把不等式整理为 $Ax^2+Bx+C>0$ 的形式 (建议 $A>0$), 再对二次式因式分解, 接着讨论对应二次方程的根的大小, 最后根据讨论的情况和二次函数图象写出对应的解集. 
</p>


<p>\subsection{比较两个式子的大小}
</p>
<p>比较 $a$ 与 $b$ 的大小一般转化为比较 $a-b$ 与 $0$ 的大小, 即把“比较两个变量的大小”转化为“比较一个变量与定值的大小”, 所以降低了难度. 容易知道,
\[\begin{aligned}
  a>b \Leftrightarrow a-b>0,\\
  a=b \Leftrightarrow a-b=0,\\
  a< b \Leftrightarrow a-b< 0.
\end{aligned}\]
在比较 $a-b$ 与 $0$ 的大小时, 一般是判断 $a-b$ 的正负号或计算其值域 (求最大值与最小值), 然后与 $0$ 比较. 偶尔也需要将式子适当的变形, 如例 \ref{exa: 2020-1013-2030} 中的 (4).
</p>
<p>\begin{example}\label{exa: 2020-1013-2030}
  比较下列各组式子的大小:
  \begin{twocolpro}
    (1) $x^2+1$, $2x$; & (2) $x^2+5x+6$, $2x^2+3x+9$;\\
    \multicolumn{2}{l}{(3) $\dfrac{\,b\,}a$, $\dfrac{b+m}{a+m}$, 其中 $a>b>0$, $m>0$;}\\
    \multicolumn{2}{l}{(4) $x^2+y^2+1$, $2(x+y-1)$.}\\
  \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 因为 $x^2+1-2x=(x-1)^2\geqslant 0$, 所以 $x^2+1\geqslant 2x$.
</p>
<p>(2) 因为 
  \[\begin{aligned}
       &2x^2+3x+9- (x^2+5x+6)\\
    ={}& x^2-2x+3= (x-1)^2+2>0,
  \end{aligned}\]
  所以 $x^2+5x+6< 2x^2+3x+9$.
</p>
<p>(3) 因为 
  \[\frac{b+m}{a+m}- \frac{\,b\,}a
    = \frac{a(b+m)-b(a+m)}{a(a+m)}
    = \frac{m(a-b)}{a(a+m)},\]
  由 $a>b>0$, $m>0$ 知 $m(a-b)>0$, $a(a+m)>0$, 所以 
  \[\frac{b+m}{a+m}- \frac{\,b\,}a>0,\quad \text{即}\quad 
    \frac{\,b\,}a< \frac{b+m}{a+m}.\]
</p>
<p>(4) 因为 
  \[\begin{aligned}
       &x^2+y^2+1- 2(x+y-1)\\
    ={}& x^2-2x+y^2-2y+3\\
    ={}& (x-1)^2+(y-1)^2+1>0,
  \end{aligned}\]
  所以 $x^2+y^2+1> 2(x+y-1)$.
</p>
</mysolution>

<p>\begin{example}\label{exa:201204-1920}
    若 $a>b$, 且 $a-\dfrac1a> b-\dfrac1b$, 求 $ab$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>后一不等式变形为
    \[a-b-\frac1a+\frac1b>0,\quad\text{即}\quad
      a-b+\frac{a-b}{ab}>0.\]
    由 $a>b$ 知 $a-b>0$, 上式两边同时除以 $a-b$ 得
    \[1+\frac1{ab}>0,\quad\text{即 (通分后化为乘法)}\quad (1+ab)ab>0.\]
    将 $ab$ 视为整体, 解得 $ab\in(-\infty,-1)\cup (0,+\infty)$.
</p>
</mysolution>
</p>
<p>\begin{example}\label{exa:201206-1410}
    若 $a$, $b>0$, 则“$a>b$”是“$a-\dfrac1a> b-\dfrac1b$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>方法一: 由例 \ref{exa:201204-1920} 中的变形过程可知
    \[a-\dfrac1a> b-\dfrac1b\Rightarrow
        (a-b)\biggl(1+\frac1{ab}\biggr)>0.\]
    再由 $a$, $b>0$ 得 $ab>0$, 即 $1+\dfrac1{ab}>0$, 所以上式等价于 $a-b>0$. 这表明“$a>b$”是“$a-\dfrac1a> b-\dfrac1b$”的充要条件.
</p>
<p>方法二: 构造函数 $f(x)=x-\dfrac1x$ ($x>0$), 则不等式 $a-\dfrac1a> b-\dfrac1b$ 化为 $f(a)>f(b)$. 因为 $\dfrac1x$ 在 $(0,+\infty)$ 上单调递减, 所以 $-\dfrac1x$ 在 $(0,+\infty)$ 上单调递增. 而 $x$ 在 $(0,+\infty)$ 上也单调递增, 所以 $f(x)=x-\dfrac1x$ ($x>0$) 单调递增. 这表明 $f(a)>f(b)\Leftrightarrow a>b$, 所求为充要条件.
</p>
</mysolution>
</p>
<p>{\bfseries 重要结论}(建议理解记忆)\quad 实际上 $f(x)=x-\dfrac1x$ ($x\neq0$) 在 $(-\infty,0)$ 和 $(0,+\infty)$ 上都是单调递增的, 其图形如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1204-1935-crop}
    </center>
</p>

