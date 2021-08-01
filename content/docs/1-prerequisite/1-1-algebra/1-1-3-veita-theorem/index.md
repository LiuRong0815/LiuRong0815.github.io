---
# bookCollapseSection: true
title: 1.1.3 一元二次方程的韦达定理
weight: 3
prevPage: ../1-1-2-quadratic-equation
prevPageTitle: 1.1.2 一元二次方程的解法
nextPage: ../../1-2-geometry
nextPageTitle: 1.2 初中几何提要
---

# 1.1.3 一元二次方程的韦达定理

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

也可以直接用 [求根公式](../1-1-2-quadratic-equation#求根公式) 来验证上述结论: 由 \\[x_1= \frac{-b+\sqrt{b^2-4ac}}{2a},\quad x_2= \frac{-b-\sqrt{b^2-4ac}}{2a}\\] 直接计算可得一元二次方程的韦达定理.

<!-- 利用上面的方法可以得到一元三次方程的韦达定理 (根与系数的关系). 例如, 若关于 $x$ 的三次方程 
\[Ax^3+Bx^2+Cx+D=0\quad (A\neq0)\]
的三根为 $x_1$, $x_2$, $x_3$, 则该方程必可变形为 
\[(x-x_1)(x-x_2)(x-x_3)=0,\]
再展开后与原方程对比系数即可. 更一般的一元 $n$ 次方程的韦达定理也可以同理得出. -->

<p>需要注意的是, 韦达定理中无需假设方程的根为实根, 也就是无论方程是否有实根, 韦达定理都成立. 例如, 二次方程 $x^2+x+1=0$ 的判别式 $\Delta=-3< 0$, 所以无实根. 但通过定义复数 (包含了实数, 高二会学到), 该方程仍有两个复根. 若设这个两复根为 $x_1$, $x_2$, 则也有
\[\left\{\!\!\begin{array}{l}
    x_1+x_2= -\dfrac{1}1= -1,\\
    x_1x_2= \dfrac{1}1=1,
\end{array}\right.\]
正因为如此, 由于大部分高中题目只考虑实根, 所以用韦达定理时, <strong>必须额外写出</strong> $\Delta\geqslant 0$. 后续学圆锥曲线时, 基本的解题方法均是利用韦达定理结合判别式, 再适当对求解的表达式变形.</p>

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

<myexample>
    <p>若关于 $x$ 的方程 $x^2- (2m^2+m-6)x+ m-2=0$ 的两个实根互为相反数, 求 $m$ 的值.</p>
</myexample>
<mysolution>
    <p>设两实根为 $x_1$, $x_2$, 则 \[\left\{\!\!\begin{array}{l}
        x_1+x_2= 2m^2+m-6= 0,\\
        \Delta= [-(2m^2+m-6)]^2- 4(m-2)\\
        \phantom{\Delta}= -4(m-2)\geqslant 0.
    \end{array}\right.\] 由前一个方程解得 $m= \dfrac32$ 或 $-2$, 由后一个不等式解得 $m\leqslant 2$, 所以前述两个 $m$ 值均合题意.</p>
</mysolution>

## 利用韦达定理构造新的方程

<p>对关于 $x$ 的二次方程 $x^2+Bx+C=0$ (二次项系数为 $1$) 的两根 $x_1$, $x_2$, 韦达定理的结论比较简洁: \[x_1+x_2= -B,\quad x_1x_2= C.\] 用该结论也可以很快地写出两根符合一定条件的二次方程. 例如, 若二次方程的两根 $x_1$, $x_2$ 满足 \[x_1+x_2= 3,\quad x_1x_2= 1,\] 则原方程必可变形为 $x^2- 3x+ 1=0$ (为什么?).</p>

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
<!-- <myexample>
    <p>已知函数 $f(x)= (x-a)(x-b)-1$ ($a< b$) 的两个零点是 $m$, $n$ ($m< n$), 判断 $a$, $b$, $m$, $n$ 的大小.</p>
</myexample>
<mysolution>
    <p>考虑函数 $g(x)= (x-a)(x-b)$ 可知, 其图形与 $x$ 轴交于点 $(a,0)$, $(b,0)$. 因为 $f(x)= g(x)-1$ 的图形可由 $g(x)$ 的图形向下平移一个单位长度得到, 所以 $f(x)$ 的图形与 $x$ 轴的交点应分布在点 $(a,0)$, $(b,0)$ 两侧, 所以 \[m< a< b< n.\]</p>
</mysolution>

<myremark>
    <p>若上题是选择题或填空题, 则也可以取特殊值. 例如设 $a=0$, $b=2$, 可解出 \[m= 1-\sqrt2\approx -0.414,\quad 
        n= 1+\sqrt2\approx 2.414,\]
    同样得到 $m< a< b< n$. 该题也可以用韦达定理求解, 但并不方便.</p>
</myremark> -->