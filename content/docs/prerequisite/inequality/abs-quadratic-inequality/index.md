---
# bookCollapseSection: true
title: 绝对值不等式与二次不等式
weight: 2
bookHidden: true
prevPage: /docs/prerequisite/inequality/inequality-property
prevPageTitle: 不等式的性质
# nextPage: /docs/prerequisite/inequality/fraction-high-order-inequality
# nextPageTitle: 分式不等式与高次不等式
---

# 绝对值不等式与二次不等式


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

