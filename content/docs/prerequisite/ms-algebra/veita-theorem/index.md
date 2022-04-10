---
# bookCollapseSection: true
title: 韦达定理
weight: 3
prevPage: ../quadratic-equation
prevPageTitle: 一元二次方程的解法
nextPage: ../../ms-geometry
nextPageTitle: 初中几何提要
---

# 韦达定理

<p>设关于 $x$ 的一元二次方程 
\[ax^2+bx+c=0\quad (a\neq0)\]
的两根为 $x_1$, $x_2$, 则该方程必可变形为 
\[(x-x_1)(x-x_2)=0.\]
将后者展开,
\[x^2- (x_1+x_2)x+ x_1x_2=0,\]
并将前者改写为 
\[x^2+ \frac{b}a x+ \frac{c}{a}=0,\]
对比可知
\[\left\{\!\!\begin{array}{l}
    - (x_1+x_2)= \dfrac{b}a,\\
    x_1x_2= \dfrac{c}a,
\end{array}\right.\ \text{即}\quad
\left\{\!\!\begin{array}{l}
    x_1+x_2= -\dfrac{b}a,\\
    x_1x_2= \dfrac{c}a,
\end{array}\right.\]
上述结论称为<strong>韦达 (Veite, 法国数学家) 定理</strong>, 也称为<strong>根与系数的关系定理</strong>.</p>

<myremark>
    <p>利用上面的方法可以得到一元三次方程的韦达定理 (根与系数的关系). 例如, 若关于 $x$ 的三次方程 \[
        ax^3+bx^2+cx+d=0\quad (a\neq 0)\]
    的三根为 $x_1$, $x_2$, $x_3$, 则该方程必可变形为 \[
        (x-x_1)(x-x_2)(x-x_3)=0,\]
    再展开后与原方程对比系数, 可知 \[
    \left\{\!\!\begin{array}{l}
        x_1+x_2+x_3= -\dfrac{b}a,\\[6pt]
        x_1x_2+ x_2x_3+ x_3x_1= \dfrac{c}a,\\[6pt]
        x_1x_2x_3= -\dfrac{d}a.
    \end{array}\right.\]
    更一般的一元 $n$ 次方程的韦达定理也可以同理得出.</p>
</myremark>

也可以直接用 [求根公式](../quadratic-equation#求根公式) 来验证韦达定理: 由 \\[
    x_{1,2}= \frac{-b\pm\sqrt{b^2-4ac}}{2a}\\]
直接计算可得结论.

<p>需要注意的是, 韦达定理中无需假设方程的根为实根, 也即无论方程是否有实根, 韦达定理都成立. 例如, 二次方程 $x^2+x+1=0$ 的判别式 $\Delta=-3< 0$, 所以无实根. 但通过定义复数 (包含了实数, 一般高二学到), 该方程仍有两个复根. 若设这两个复根为 $x_1,x_2$, 则也有
\[\left\{\!\!\begin{array}{l}
    x_1+x_2= -1,\\
    x_1x_2= 1,
\end{array}\right.\]
正因为如此, 由于大部分高中题目只考虑实根, 所以用韦达定理时, <strong>必须额外写出</strong> $\Delta\geqslant 0$.</p>

## 韦达定理的简单应用

<myexample id="例 1">
    <p>设方程 $x^2-3x-2=0$ 的两个实根为 $x_1$, $x_2$, 求下列各式的值: \[x_1x_2,\quad x_1^2+x_2^2,\quad\dfrac1{x_1}+\dfrac1{x_2}.\]</p>
</myexample>
<mysolution>
    <p>此方程的判别式
    \[\Delta= (-3)^2-4(-2)= 17>0,\]
    所以确实有两个实根. 由韦达定理, \[\left\{\!\!\begin{array}{l}
        x_1+x_2= 3,\\
        x_1x_2= -2,
    \end{array}\right.\] 则 \[\begin{gathered}
        x_1^2+x_2^2= (x_1+x_2)^2- 2x_1x_2= 13,\\
        \dfrac1{x_1}+\dfrac1{x_2}= \frac{x_1+x_2}{x_1x_2}= -\frac32.
    \end{gathered}\]</p>
</mysolution>

<myremark>
    <p>上例中要求值的式子均为关于 $x_1,x_2$ 的对称式, 即将 $x_1,x_2$ 互换位置之后, 新式与原式相等. 类似的还有, \[
        x_1^3+x_2^3,\quad \frac{x_1}{x_2}+\frac{x_2}{x_2},\]
    等等. 可以证明, 关于 $x_1,x_2$ 的对称式一定能用 $x_1+x_2$ 和 $x_1x_2$ 表示. 所以 $x_1+x_2$ 和 $x_1x_2$ 也称为关于 $x_1,x_2$ 的“基本对称式”.</p>
</myremark>

<myexample>
    <p>若关于 $x$ 的方程 \[
        x^2- (2m^2+m-6)x+ m-2=0\]
    的两个实根互为相反数, 求 $m$ 的值.</p>
</myexample>
<mysolution>
    <p>设两实根为 $x_1$, $x_2$, 则 \[\left\{\!\!\begin{array}{l}
        x_1+x_2= 2m^2+m-6= 0,\\
        \Delta= [-(2m^2+m-6)]^2- 4(m-2)\\
        \phantom{\Delta}= -4(m-2)\geqslant 0.
    \end{array}\right.\] 由前一个方程解得 $m= \dfrac32$ 或 $-2$, 由后一个不等式解得 $m\leqslant 2$, 所以前述两个 $m$ 值均合题意.</p>
</mysolution>

## 利用韦达定理构造新的方程

<p>对关于 $x$ 的二次方程 $x^2+Bx+C=0$ (二次项系数为 $1$) 的两根 $x_1$, $x_2$, 韦达定理的结论比较简洁: \[x_1+x_2= -B,\quad x_1x_2= C.\] 用该结论也可以由两根之和与积写出对应的二次方程, 因为以 $x_1,x_2$ 为根的二次方程必可写为 \[
    (x-x_1)(x-x_2)=0,\]
即 \[
    x^2- (x_1+x_2)x+ x_1x_2=0.\]
例如, 若二次方程的两根 $x_1$, $x_2$ 满足 \[
    x_1+x_2= 3,\quad x_1x_2= 1,\]
则原方程必可变形为 $x^2- 3x+ 1=0$.</p>

<myexample>
    <p>设方程 $x^2-3x-2=0$ 的两个实根为 $x_1$, $x_2$, 求以下列各组数为两根的一元二次方程:</p>
    <p>(1) $x_1^2$, $x_2^2$;&emsp; (2) $\dfrac1{x_1}$, $\dfrac1{x_2}$.</p>
</myexample>
<mysolution>
    <p>由前面的说明, 只需要分别计算两根之和与两根之积. 由韦达定理, \[\left\{\!\!\begin{array}{l}
        x_1+x_2= 3,\\
        x_1x_2= -2,
    \end{array}\right.\]</p>
    <p>(1) 借用 <a href="#例 1">例 1</a> 的结论, \[\left\{\!\!\begin{array}{l}
        x_1^2+x_2^2= 13,\\
        x_1^2x_2^2= 4,
    \end{array}\right.\] 故所求方程为 $x^2- 13x+4=0$.</p>
    <p>(2) 同理, \[\left\{\!\!\begin{array}{l}
        \dfrac1{x_1}+\dfrac1{x_2}= -\dfrac32,\\
        \dfrac1{x_1}\cdot\dfrac1{x_2}= -\dfrac12,
    \end{array}\right.\] 故所求方程为 \[x^2+\dfrac32x-\dfrac12=0,\quad\text{即}\quad 2x^2+3x-1=0.\]</p>
</mysolution>

<myremark>
    <p>上例中 (2) 还有更简洁的解法. 考虑 $\dfrac1{x_1}$, $\dfrac1{x_2}$ 的形式可知, 若 $x$ 为所求一元二次方程的根, 则 $\dfrac1x$ 为原方程的根. 所以 $x$ 满足 \[\frac1{x^2}-\frac3x-2=0,\quad\text{即}\quad 2x^2+3x-1=0.\]</p>
</myremark>
