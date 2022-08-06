---
# bookCollapseSection: true
title: 二次三项式的因式分解
weight: 1
prevPage: ../
prevPageTitle: 初中代数提要
nextPage: ../quadratic-equation
nextPageTitle: 一元二次方程的解法
---

# 二次三项式的因式分解

<p>
因式分解是将多项式写成两个或多个次数较低的多项式之积, 如 \[\begin{gathered}
    x^2+3x+2= (x+1)(x+2),\\
    x^3-2x^2-3x= x(x+1)(x-3).
\end{gathered}\] 
因式分解时一般逆用多项式乘法公式. 这里简要回顾关于 $x$ 的整系数二次三项式 \[
    ax^2+bx+c\quad (a\neq 0)\]
的因式分解方法.
</p>

在对上述二次三项式因式分解时, 常用方法是

1. “提”: 提公因式
2. “套”: 套公式
3. “十字”: 用十字相乘法

<p>
具体来说, 在进行因式分解时, 应先将公因式提出, 并使得系数为<strong>整数</strong>, 以简化计算. 然后尝试套用平方差公式 \[
    a^2-b^2= (a+b)(a-b)\]
或完全平方公式 \[
    a^2\pm 2ab+b^2= (a\pm b)^2.\]
后一公式可以用结合图形记忆.

![完全平方公式示意图](/figs/2022/2022-08/2022-0806-1050.svg)
</p>

<p>
如果无法使用上述两个公式, 则可考虑十字相乘法, 即利用公式 \[
    x^2+(a+b)x+ab= (x+a)(x+b).\]
使用该公式时, 一般先将常数项分解, 然后拼凑出一次项系数. 对于无法快速判断系数分解方式的二次三项式, 有时也考虑用配方法或求根法 (见一元二次方程的解法) 来进行因式分解. 下面先给出一些对二次三项式 $ax^2+bx+c$ ($a\neq 0$) 应用十字相乘法的例子, 然后介绍配方法. 
</p>

## 情形一: 二次项系数 $a=1$

<myexample>
    <p>分解因式:
    </p>
    <p>(1) $x^2+7x+6$;&emsp;
    (2) $x^2-13x+36$.
    </p>
</myexample>

<mysolution>
    <p>(1) 常数 $6= 1\times 6= 2\times 3$, 而一次项系数 $7=1+6$, 所以 \[\begin{aligned}
        &x^2+7x+6\\
        ={}& x^2+(1+6)x+1\times 6\\
        ={}& (x+1)(x+6).
    \end{aligned}\]
    </p>
    <p>(2) 常数 $36$ 有多种分解方式, 考虑到一次项系数为 $-13$, 所以选择 $36=(-4)\times(-9)$, 相应地, \[\begin{aligned}
        &x^2-13x+36\\
        ={}& x^2-(4+9)x+(-4)\times (-9)\\
        ={}& (x-4)(x-9).
    \end{aligned}\]</p>
</mysolution>

由上例可以看出, 当常数项为正数时, 应将其分解为两个同号因数, 它们的符号与一次项系数的正负号相同.

<myexample>
    <p>分解因式:
    </p>
    <p>(1) $x^2+5x-24$;&emsp;
    (2) $x^2-2x-15$.</p>
</myexample>

<mysolution>
    <p>(1) 若将 $24$ 分解为 $3\times 8$, 恰有 $8-3=5$, 所以将 $-24$ 分解为 $(-3)\times 8$, 且 \[\begin{aligned}
        &x^2+5x-24\\
        ={}& x^2+(-3+8)x+(-3)\times 8\\
        ={}& (x-3)(x+8).
    \end{aligned}\]</p>
    <p>(2) 类似地, 将 $-15$ 分解为 $3\times(-5)$, 相应地, \[\begin{aligned}
        &x^2-2x-15\\
        ={}& x^2+(3-5)x+3\times (-5)\\
        ={}& (x+3)(x-5).
    \end{aligned}\]</p>
</mysolution>

由上例可以看出, 当常数项为负数时, 应将其分解为两个异号的因数, 其中绝对值较大的因数与一次项系数的正负号相同.

<myexercise>
    <p>分解因式:
    </p>
    <p>(1) $x^2+6x+5$;&emsp;
    (2) $x^2-4x-21$;
    </p>
    <p>(3) $x^2-11x+30$;&emsp;
    (4) $x^2-x-12$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $(x+1)(x+5)$;&emsp; (2) $(x+3)(x-7)$;
    </p>
    <p>(3) $(x-5)(x-6)$;&emsp; (4) $(x+3)(x-4)$.</p>
</details>

<myexample>
    <p>分解因式:</p>
    <p>(1) $x^2+xy-6y^2$;&emsp;
    (2) $(x^2+x)^2-8(x^2+x)+12$.</p>
</myexample>

<mysolution>
    <p>(1) 原式可视为关于 $x$ 的二次三项式, 并将 $y$ 视为已知数, 则应将 $-6y^2$ 分解. 考虑到一次项系数为 $y$, 所以将 $-6y^2$ 分解为 $(-2y)\cdot 3y$, 故 \[\begin{aligned}
        &x^2+xy-6y^2\\
        ={}& x^2+(-2y+3y)x+(-2y)\cdot 3y\\
        ={}& (x-2y)(x+3y).
    \end{aligned}\]</p>
    <p>(2) 此处可将 $x^2+x$ 视为整体, 再将常数项 $12$ 分解为 $(-2)\times(-6)$, 则 \[\begin{aligned}
        &(x^2+x)^2-8(x^2+x)+12\\
        ={}& (x^2+x-2)(x^2+x-6)\\
        ={}& (x-1)(x+2)(x-2)(x+3).
    \end{aligned}\]
    注意, 分解之后的因式若可以继续分解, 则应分解完全 (如本例).</p>
</mysolution>

<myexercise>
    <p>分解因式:</p>
    <p>(1) $x^4-7x^2-18$;&emsp;
    (2) $a^4-a^2b^2-12b^4$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $(x^2+2)(x+3)(x-3)$;</p>
    <p>(2) $(a^2+3b^2)(a+2b)(a-2b)$.</p>
</details>

## 情形二: 二次项系数不为 $1$

<p>此时需要逆用 (即由下面得到上面) 乘法公式 \[\begin{aligned}
    &(a_1x+b_1)(a_2x+b_2)\\
    ={}& a_1a_2x^2+(a_1b_2+a_2b_1)x+b_1b_2.
\end{aligned}\]
从式子的特点可以看出, 若要从下面的式子变形为上面的式子, 需要将二次项系数和常数项同时分解, 然后拼凑出一次项的系数. 具体操作可参考如下分解: \[\begin{array}{ccc}
    a_1\!\!\!\!\!  & & b_1\\
       & \Huge\times\!\! & \\
    a_2\!\!\!\!\! & & b_2
    \end{array}\rightarrow a_1b_2+a_2b_1.\]
第一列两个因子 $a_1$, $a_2$ 由分解二次项系数 $a_1a_2$ 得到, 第二列两个因子 $b_1$, $b_2$ 由分解常数项 $b_1b_2$ 得到. 这两列系数沿“十字”所示方向相乘后, 再相加即得一次项 (交叉项) 系数 $a_1b_2+a_2b_1$. 这一分解过程恰好也说明了“十字相乘法”名称的由来. 为了计算方便, 上面的“十字”式有时也列成 \[\begin{array}{ccc}
    a_1x\!\!\!\!\! & & b_1\\
      & \Huge\times\!\! & \\
    a_2x\!\!\!\!\! & & b_2
    \end{array}\]</p>

<myexample>
    <p>分解因式:</p>
    <p>(1) $12x^2-5x-2$;&emsp;
    (2) $5x^2+6xy-8y^2$.</p>
</myexample>

<mysolution>
    <p>(1) 二次项系数和常数项分解如下: \[\begin{array}{ccc}
        3x\!\!\!\!\! & & -2\\
      & \Huge\times\!\! & \\
        4x\!\!\!\!\! & & 1
    \end{array}\rightarrow 3x\cdot 1+4x\cdot (-2)= -5x,\] 故 \[12x^2-5x-2= (3x-2)(4x+1).\]</p>
    <p>(2) 将 $y$ 视为常数, 二次项系数和常数项分解如下: \[\begin{array}{ccc}
        x\!\!\!\!\! & & 2y\\
      & \Huge\times\!\! & \\
        5x\!\!\!\!\! & & -4y
        \end{array}\rightarrow x\cdot (-4y)+ 5x\cdot 2y= 6xy,\] 则 \[
        5x^2+6xy-8y^2= (x+2y)(5x-4y).\]</p>
</mysolution>

<myexercise>
    <p>分解因式:</p>
    <p>(1) $3x^2+11x+6$;&emsp;
    (2) $2a^2+ab-3b^2$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $(3x+2)(x+3)$;&emsp;
    (2) $(2a-3b)(a+2b)$.</p>
</details>

## 配方法

<p id="配方法">对关于 $x$ 的二次式 $x^2+bx+c$ 配 (平) 方是指利用完全平方公式, 由一次项系数 $b$ 确定常数 $\biggl(\dfrac{b}2\biggr)^2$ 即 $\dfrac{b^2}4$, 并将原式表示为完全平方式与另一个常数的和, 即 \[\begin{aligned}
        x^2+bx+c
        &= x^2+bx+\frac{b^2}4+ c-\frac{b^2}4\\
        &= \biggl(x+\frac{b}2\biggr)^2+ c-\frac{b^2}4.
    \end{aligned}\]
对关于 $x$ 的二次式 $ax^2+bx+c$ ($a\neq 0$) 配方, 只需要先提出二次项系数 $a$, 即 \[\begin{aligned}
        ax^2+bx+c
        &= a\biggl(x^2+\frac{b}a x\biggr)+ c\\
        &= a\biggl(x^2+\frac{b}a x+ \frac{b^2}{4a^2}\biggr)+ c-\frac{b^2}{4a}\\
        &= a\biggl(x+\frac{b}{2a}\biggr)^2+ \frac{4ac-b^2}{4a}.
    \end{aligned}\]
对二次三项式配方后, 再利用平方差公式, 即可完成因式分解, 见下面的例子.</p>

<myexample>
    <p>分解因式:</p>
    <p>(1) $x^2+6x-16$;&emsp;(2) $2x^2+3x-2$.</p>
</myexample>

<mysolution>
    <p>(1) 先配方, 再利用平方差公式, \[\begin{aligned}
        x^2+6x-16
        &= (x^2+6x+9)-9-16\\
        &= (x+3)^2- 5^2\\
        &= (x+3-5)(x+3+5)\\
        &= (x-2)(x+8).
    \end{aligned}\]</p>
    <p>(2) 先提二次项系数, 再配方, \[\begin{aligned}
        2x^2+3x-2
        &= 2\biggl(x^2+ \frac32x- 1\biggr)\\
        &= 2\biggl(x^2+ \frac32x+ \frac9{16}- \frac{25}{16}\biggr)\\
        &= 2\biggl[\biggl(x+ \frac34\biggr)^2- \biggl(\frac54\biggr)^2\biggr]\\
        &= 2\biggl(x+\frac34- \frac54\biggr)\biggl(x+\frac34+ \frac54)\\
        &= 2\biggl(x- \frac12\biggr)(x+2)\\
        &= (2x-1)(x+2).
    \end{aligned}\]</p>
</mysolution>

由上面的例子可以看出, 配方法的计算量有时会比较大 (容易出错), 所以通常还是优先考虑十字相乘法. 但如果不容易试出十字相乘法中系数的分解方式, 也不妨试试配方法. 此外, 配方这一变形技巧也能用于解一元二次方程、确定一元二次函数图象 (抛物线) 的顶点. 因此, 仍有必要掌握配方法的主要思路.

<myremark>
    <p>(1) 一般的平方和, 如 $x^2+1$, 是无法因式分解的. 如若不然, 可设 \[
        x^2+1= (x+a)(x+b),\] 
    其中 $a,b$ 是待定常数. 右边展开后为 $x^2+(a+b)x+ab$, 与左边对比, 对应项系数应该相等, 即 \[\left\{\!\!\begin{array}{l}
        0= a+b,\\
        1= ab,
    \end{array}\right.\] 
    由第一式得 $b=-a$, 代入第二式有 $a^2=-1$, 在实数范围内无解. 所以假设不成立, 即 $x^2+1$ 无法 (在实系数范围内) 因式分解. 同样地, $x^2+4y^2$, $9x^2+y^2$ 等, 一般也不考虑对其因式分解.
    </p>
    <p>(2) 但有些特殊的平方和 (不常见), 如 $x^4+4= (x^2)^2+ 2^2$, 可以因式分解, 因为 \[\begin{aligned}
        x^4+4
        &= x^4+4+4x^2- 4x^2\\
        &= (x^2+2)^2- (2x)^2\\
        &= (x^2+2- 2x)(x^2+1+ 2x)\\
        &= (x^2- 2x+2)(x^2+ 2x+2).
    \end{aligned}\]</p>
</myremark>
