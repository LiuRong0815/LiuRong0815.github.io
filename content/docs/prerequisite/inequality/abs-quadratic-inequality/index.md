---
# bookCollapseSection: true
title: 绝对值不等式与二次不等式
weight: 2
# bookHidden: true
prevPage: /docs/prerequisite/inequality/inequality-property
prevPageTitle: 不等式的性质
nextPage: /docs/prerequisite/inequality/fraction-high-order-inequality
nextPageTitle: 分式不等式与高次不等式
---

# 绝对值不等式与二次不等式

绝对值不等式是含绝对值的不等式, 解这种不等式时, 一般是利用绝对值的几何意义去掉不等式中的绝对值符号, 即需要对式中的未知数取值分类讨论. 一些恒成立的绝对值不等式, 可以用于估计代数式的取值范围.

前面已经介绍了[简单二次不等式的解法](/docs/prerequisite/ms-function/quadratic-function-inequality#二次不等式的解法), 这里进一步介绍如何求解含参数的二次不等式.

<span id="绝对值不等式"></span>

## 绝对值的几何意义

<p>实数 $a$ 的绝对值定义为 \[
    |a|=\begin{cases}
    a, & a>0,\\
    0, & a=0,\\
    -a, & a< 0,
\end{cases}\]
有时也写成 \[
    |a|= \begin{cases}
    a, & a\geqslant 0,\\
    -a, & a< 0.
    \end{cases}\]
由定义可知, $|a|\geqslant 0$, 即绝对值必为非负数. 又有 $|a|\geqslant a$, 等号成立的条件是 $a\geqslant 0$. 此外还有 $|a|^2= a^2$, 两边取算术平方根, 则 \[
    |a|= \sqrt{|a|^2}= \sqrt{a^2}.\]
这是绝对值的另一种表示. 绝对值的几何意义是数轴上点 $a$ 到原点的距离, 则 $|a|= |-a|$; 进而可知, 数轴上两点 $x_1$, $x_2$ 之间的距离为 $|x_1-x_2|$, 如下图所示:
</p>

<img alt="绝对值的几何意义" src="/figs/2020/2020-10/2020-1009-2110.svg"></img>

<img alt="数轴上两点之间的距离" src="/figs/2020/2020-10/2020-1009-2120.svg"></img>

<p>例如, $|x-1|$ 表示点 $x$ 到 $1$ 的距离; $|x+2|=|x-(-2)|$ 表示点 $x$ 到 $-2$ 的距离; $|2x-2|= 2|x-1|$ 表示点 $x$ 到 $1$ 的距离的 $2$ 倍; $|4+2x|= 2|x-(-2)|$ 表示点 $x$ 到 $-2$ 的距离的 $2$ 倍. 
</p>
<p>注意, 前面运用了绝对值的乘法运算法则: $|ka|= |k|\,|a|$. 证明该法则的直接方法是, 依 $k$ 和 $a$ 的正负号分 $4$ 种情况讨论. 更好的证明方法是利用平方去掉绝对值: 该式等价于 \[
    |ka|^2= (|k|\,|a|)^2\Leftrightarrow (ka)^2= k^2 a^2,\]
而最后一式显然成立. 用同样的方法可以证明 \[
    \Bigl|\frac{a}b\Bigr|= \frac{|a|}{|b|}\quad (b\neq 0).\]
</p>

<p>函数 $y=|x|$ 的图象可以分段绘制, 即分别画出函数 $y= -x$ ($x< 0$) 和 $y= x$ ($x\geqslant 0$) 的图象; 也可以通过图象变换得到, 即先画出 $y=x$ 的图象, 再把 $x$ 轴下方的部分关于 $x$ 轴对称翻折到 $x$ 轴上方, 如下图所示:
</p>

<img alt="函数 $y=|x|$ 的图象" src="/figs/2022/2022-09/2022-0905-2100.svg"></img>

<myexample>
    <p>设 $a$, $b$ 为任意实数, 证明: $|a+b|\leqslant |a|+ |b|$, 并讨论等号成立的充要条件.
    </p>
</myexample>

<myproof>
    <p>不等号两边都是非负数, 所以先平方再整理, 原式等价于 \[\begin{aligned}
        &|a+b|^2\leqslant (|a|+ |b|)^2\\
        \Leftrightarrow{}& a^2+ 2ab+ b^2\leqslant a^2+ 2|ab|+ b^2\\
        \Leftrightarrow{}& ab\leqslant |ab|.
    \end{aligned}\]
    由绝对值的定义, 最后一式成立, 所以原式也成立.
    </p>
    <p>原式中等号等立, 等价于最后一式等号成立, 结合绝对值的定义, 又等价于 $ab\geqslant 0$. 因此, \[
        |a+b|= |a|+ |b|\]
    的充要条件是 $ab\geqslant 0$ (可大致认为 $a$ 与 $b$ 同号).
    </p>
</myproof>

<myremark>
    <p>将上述不等式中的 $b$ 换成 $-b$, 可得 \[
        |a-b|\leqslant |a|+ |b|,\]
    等号成立的充要条件是 $ab\leqslant 0$.
    </p>
</myremark>

解绝对值不等式的基本方法是<strong>零点分段法</strong>, 具体做法是: 先求出各绝对值内式子的零点 (使式子等于 $0$ 的未知数的值), 再用零点将数轴分为多个区间, 然后在每个区间上分别根据各绝对值内式子的正负号去掉绝对值.

<myexample>
    <p>解下列不等式:
    </p>
    <p>(1) $|x-1|\leqslant 2$;&emsp; (2)  $|2x-4|\geqslant 3+ |x+1|$.
    </p>
</myexample>

<mysolution>
    <p>(1) 题中应考虑零点 $1$, 将数轴分为两段: $(-\infty,1]$, $(1,+\infty)$.
    </p>
    <p>若 $x\in (-\infty,1]$, 则原不等式化为 \[
        -(x-1)\leqslant 2\Rightarrow x\geqslant -1,\]
    结合 $x\in (-\infty,1]$ 知, $x\in [-1,1]$.
    </p>
    <p>若 $x\in (1,+\infty)$, 则原不等式化为 \[
        x-1\leqslant 2\Rightarrow x\leqslant 3,\]
    结合 $x\in (1,+\infty)$ 知, $x\in (1,3]$.
    </p>
    <p>综上所述, $x\in [-1,3]$.
    </p>
    <p>(2) 题中应考虑零点 $-1$ 和 $2$, 将数轴分为三段: $(-\infty,-1]$, $(-1,2]$, $(2,+\infty)$.
    </p>
    <p>若 $x\in (-\infty,-1]$, 则原不等式化为 \[
        -(2x-4)\geqslant 3-(x+1)\Rightarrow x\leqslant 2,\]
    因此 $x\in (-\infty,-1]$.
    </p>
    <p>若 $x\in (-1,2]$, 则原不等式化为 \[
        -(2x-4)\geqslant 3+(x+1)\Rightarrow x\leqslant 0,\]
    因此 $x\in (-1,0]$.
    </p>
    <p>若 $x\in (2,+\infty]$, 则原不等式化为 \[
        2x-4\geqslant 3+(x+1)\Rightarrow x\geqslant 8,\]
    因此 $x\in [8,+\infty)$.
    </p>
    <p>综上所述, $x\in (-\infty,0]\cup [8,+\infty)$.
    </p>
</mysolution>

<myremark>
    <p>用零点对数轴分段时, 一般要求“不重不漏”, 如 (1) 中也可以将数轴分为 $(-\infty,1)$, $[1,+\infty)$, 但是不宜分为 $(-\infty,1]$, $[1,+\infty)$, 且不能分为 $(-\infty,1)$, $(1,+\infty)$.
    </p>
</myremark>

## 绝对值不等式的解法

虽然零点分段法是求解绝对值不等式的通用方法, 但是适当运用绝对值的几何意义, 有时能简化计算过程.

<p>对于简单的绝对值不等式, 可以根据绝对值的几何意义直接求解. 如不等式 $|x|< 3$, 由 $|x|$ 表示点 $x$ 到原点的距离可知, $x\in (-3,3)$; 而由不等式 $|x|\geqslant 3$, 可解得 $x\in(-\infty,-3]\cup[3,+\infty)$.
</p>

<myexample>
    <p>解下列不等式:
    </p>
    <p>(1) $|x-1|\leqslant 2$;&emsp; (2) $|2x+1|> 3$;&emsp; 
       (3) $|1-2x|\geqslant 5$.
    </p>
</myexample>

<mysolution>
    <p>(1) 将 $x-1$ 视为整体, 则 \[
        -2\leqslant x-1\leqslant 2,\]
    即 $-1\leqslant x\leqslant 3$, 所以 $x\in [-1,3]$.
    </p>
    <p>(2) 由题意, \[
        2x+1< -3\quad \text{或}\quad 2x+1>3,\]
    即 $x< -2$ 或 $x>1$, 所以 $x\in(-\infty,-2)\cup (1,+\infty)$.
    </p>
    <p>(3) 由题意, \[
        1-2x\leqslant -5\quad \text{或}\quad 1-2x\geqslant 5,\]
    即 $x\geqslant 3$ 或 $x\leqslant -2$, 所以 $x\in(-\infty,-2]\cup [3,+\infty)$.
    </p>
</mysolution>

<p>对于稍微复杂一些的绝对值不等式, 若只含一个绝对值, 则可以按绝对值的几何意义分类讨论; 若含两个绝对值, 除了用零点分段法, 也可以先尝试对不等式两边平方.
</p>

<myexample>
    <p>解下列不等式:
    </p>
    <p>(1) $|x+1|< 2x$;&emsp;  (2) $|x-1|\geqslant 2x$;&emsp; 
       (3) $|2x+1|> |x|$.
    </p>
</myexample>
<mysolution>
    <p>(1) 由题意, \[\left\{\!\!\begin{array}{l}
        2x>0,\\
        -2x< x+1< 2x,
    \end{array}\right.\text{解得}\ x\in(1,+\infty).\]
    </p>
    <p>(2) 若 $2x\leqslant 0$ 即 $x\leqslant 0$, 则不等式已成立. 
    </p>
    <p>若 $2x> 0$ 即 $x> 0$, 则不等式等价于 \[
        x-1\leqslant -2x\quad \text{或}\quad x-1\geqslant 2x,\]
    解得 $x\leqslant \dfrac13$ 或 $x\leqslant -1$. 结合 $x>0$ 知, 此时 $0< x\leqslant \dfrac13$. 
    </p>
    <p>综上所述, $x\in\biggl(-\infty,\dfrac13\biggr]$.
    </p>
    <p>(3) 不等式两边平方得 \[
        (2x+1)^2>x^2\quad \text{即}\quad (x+1)(3x+1)>0,\]
    解得 $x\in(-\infty,-1)\cup \biggl(\dfrac13,+\infty\biggr)$.
    </p>
</mysolution>

<myremark>
    <p>对上例 (1) 中的不等式, 也可以直接两边平方, 因为可以断定不等号两边均为非负数; 对上例 (2) 中的不等式, 直接两边平方并非等价变形, 所以会得到错误的答案, 例如, 由 $3> -4$ 并不能得到 $3^2> (-4)^2$. 解不等式时, 必须运用等价变形确保不等式的解集没有发生变化. 具体到用两边平方的方法解不等式, 应牢记: 仅当 $a$, $b\geqslant 0$ 时, 才有\[
        a> b\Leftrightarrow a^2> b^2.\]
    </p>
</myremark>

## 二次不等式

<p>解二次不等式 $ax^2+bx+c>0$ 或 $ax^2+bx+c\geqslant0$ 时, 一般先因式分解 $ax^2+bx+c$, 再借助对应二次函数的图形来确定不等式的解集. 如 \[
    x^2-x-2>0\Rightarrow (x+1)(x-2)>0,\]
由图形知 $x< -1$ 或 $x>2$. 为了方便应用此方法, 通常把二次项系数化为正数, 如 $-2x^2-x+1\geqslant 0$ 化为 $2x^2+x-1\leqslant 0$ (注意不等号方向变了). 
</p>

<myexercise>
    <p>解下列不等式:</p>
    <p>(1) $-3x^2 +5x+2>0$;&emsp; (2) $(x-2)(x+3)>6$.
    </p>
</myexercise>
<mysolution>
    <p>(1) 先将二次项系数化为正数, 再分解因式, \[
        3x^2- 5x- 2< 0,\quad (3x+1)(x-2)< 0,\]
    则 $x\in\biggl(-\dfrac13,2\biggr)$.
    </p>
    <p>(2) 化为与 $0$ 比较并整理, \[
        x^2+x-12> 0,\quad (x-3)(x+4)>0,\]
    解得 $x\in(-\infty,-4)\cup (3,+\infty)$.
    </p>
</mysolution>

<p>由二次不等式的解法可知, 两个二次不等式 \[
    ax^2+bx+c>0,\quad ax^2+bx+c\leqslant 0\]
的解集互为补集 (全集为实数集 $\mathbf{R}$), 且两者解集的端点 (除了 $-\infty$, $+\infty$) 就是对应二次方程 $ax^2+bx+c=0$ 的解. 例如, 由二次不等式 $ax^2+bx+c>0$ 的解集为 $(1,2)$ 可知, $ax^2+bx+c\leqslant 0$ 的解集为 $(-\infty,1]\cup [2,+\infty)$, 且方程 $ax^2+bx+c=0$ 的两根为 $1$, $2$, 进而可由<a href="/docs/prerequisite/ms-algebra/veite-theorem">韦达定理</a>得到 $a$, $b$, $c$ 的数量关系.
</p>

<myexample>
    <p>(1) 若关于 $x$ 的不等式 $x^2 +3x+a>0$ 的解集为 $\{x\mid x< -2\ \text{或}\ x>-1\}$, 求 $a$ 的值;
    </p>
    <p>(2) 若关于 $x$ 的不等式 $ax^2 +bx-1>0$ 的解集为 $\{x\mid 3< x< 4\}$, 求 $a,b$ 的值.
    </p>
</myexample>
<mysolution>
    <p>(1) 由韦达定理, $a= (-1)\cdot (-2)= 2$.
    </p>
    <p>(2)  $3$ 和 $4$ 为对应二次方程 $ax^2 +bx-1= 0$ 的两根, 由韦达定理, \[
        3+4= -\frac{b}{a},\quad 3\cdot 4= \frac{-1}a,\]
    解得 $a= -\dfrac1{12}$, $b=\dfrac{7}{12}$.
    </p>
</mysolution>

## 含参数的二次不等式的解法

解二次不等式时, 利用了对应的二次函数图象. 若二次不等式的系数含参数, 则对应的二次函数图象也随参数的取值不同而发生变化. 所以求解含参数的二次不等式时, 必须对参数分类讨论.

<myexample>
    <p>解关于 $x$ 的不等式:
    </p>
    <p>(1) $x^2-(2+a)x+2a< 0$; &emsp; 
        (2) $2x^2+(2+a)x+a\geqslant 0$.
    </p>
</myexample>

<mysolution>
    <p>(1) 不等式化为 \[
        (x-2)(x-a)< 0,\]
    所以根据二次函数 $y=(x-2)(x-a)$ 的图象知, 若 $a< 2$, 则 $x\in (a,2)$; 若 $a=2$, 则 $x\in \varnothing$; 若 $a>2$, 则 $x\in (2,a)$.
    </p>
    <p>(2) 不等式化为 \[
        (2x+a)(x+1)\geqslant 0,\]
    所以根据二次函数 $y=(2x+a)(x+1)$ 的图象知, 
    </p>
    <p>若 $-\dfrac{a}2< -1$ 即 $a> 2$, 则 $x\in \biggl(-\infty,-\dfrac{a}2\biggr]\cup [-1,+\infty)$; 
    </p>
    <p>若 $-\dfrac{a}2= -1$ 即 $a= 2$, 则 $x\in \mathbf{R}$; 
    </p>
    <p>若 $-\dfrac{a}2> -1$ 即 $a< 2$, 则 $x\in (-\infty,-1]\cup \biggl[-\dfrac{a}2,+\infty\biggr)$.
    </p>
</mysolution>

<myexercise>
    <p>解关于 $x$ 的不等式: \[
        x^2+2x+ax+2a>0.\]
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>不等式化为 \[
        x^2+(2+a)x+2a>0\quad\text{即}\quad (x+2)(x+a)>0,\]
    所以根据二次函数 $y=(x+2)(x+a)$ 的图象知, 
    </p>
    <p>若 $-a< -2$ 即 $a>2$, 则 $x\in (-\infty,-a)\cup (-2,+\infty)$; 
    </p>
    <p>若 $-a=-2$ 即 $a=2$, 则 $x\in \{x\mid x\neq-2\}$; 
    </p>
    <p>若 $-a>-2$ 即 $a< 2$, 则 $x\in (-\infty,-2)\cup (-a,+\infty)$.
    </p>
</details>

<p>上例中关于 $x$ 的不等式含参数 $a$, 所以写解集时需要分类讨论, 讨论的主要依据是对应二次方程两根的大小关系. 再看一个复杂一点的例子.
</p>

<myexample>
    <p>解关于 $x$ 的不等式: $x^2+ax-6a^2\leqslant 0$. 
    </p>
</myexample>

<mysolution>
    <p>不等式化为 \[
        (x+3a)(x-2a)\leqslant 0,\]
    所以根据二次函数 $y=(x+3a)(x-2a)$ 的图象知, 
    </p>
    <p>若 $-3a< 2a$ 即 $a>0$, 则 $x\in [-3a,2a]$; 
    </p>
    <p>若 $-3a=2a$ 即 $a=0$, 则 $x\in \{0\}$; 
    </p>
    <p>若 $-3a>2a$ 即 $a< 0$, 则 $x\in [2a,-3a]$.
    </p>
</mysolution>

<p>从上例可以看出, 解含参数的关于 $x$ 的二次不等式, 步骤为: 把不等式整理为 $Ax^2+Bx+C>0$ 的形式 (建议 $A>0$), 再对二次式因式分解, 接着讨论对应二次方程的根的大小, 最后根据讨论的情况和二次函数图象写出对应的解集. 
</p>

<myexercise>
    <p>(1) 解关于 $x$ 的不等式: $x^2 -(3a+1)x+2a(a+1)< 0$.
    </p>
    <p>(2) 若关于 $x$ 的不等式 $x^2 -2ax-8a^2 < 0$ 的解集为 $(x_1,x_2)$, 且 $x_2-x_1=12$, 求 $a$ 的值.
    </p>    
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) 提示: 先分解因式, 再比较两根 $2a$ 和 $a+1$ 的大小.
    </p>
    <p>(2) 若 $a=0$, 则不等式为 $x^2< 0$, 无解. 若 $a>0$, 解不等式可知, $x\in (-2a,4a)$, 则 \[
        x_1= -2a, x_2= 4a,\quad x_2-x_1= 6a.\]
    由 $x_2-x_1=12$ 知 $a= 2$. 类似地, 若 $a< 0$, 可得 $a=-2$.
    </p>
</details>

<myexample>
    <p>已知 $a\in\mathbf{Z}$, 关于 $x$ 的一元二次不等式 $x^2 -6x+a\leqslant0$ 的解集中有且仅有 $3$ 个整数, 求 $a$ 的值.
    </p>
</myexample>
<mysolution>
    <p>方法一: 作二次函数 $y= x^2 -6x+a$ 图象的草图, 开口向上且对称轴为 $x=3$, 所以 $3$ 个整数解必为 $2,3,4$. 结合图象知, 当 $x=2$ 时 $y\leqslant 0$, 当 $x=1$ 时 $y> 0$, 解得 $a\in (5,8]$.
    </p>
    <p>方法二: 原不等式化为 \[
        (x-3)^2\leqslant 9-a,\quad |x-3|\leqslant \sqrt{9-a},\]
    由题意并结合绝对值的几何意义,  \[
        \sqrt{9-a}\in [1,2),\quad a\in(5,8].\]
    </p>
</mysolution>
