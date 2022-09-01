---
# bookCollapseSection: true
title: 圆锥曲线综合
weight: 4
bookHidden: true
prevPage: /docs/analytic-geometry/conic-curves/parabola
prevPageTitle: 抛物线
nextPage: /docs/solid-geometry
nextPageTitle: 空间几何
---

# 圆锥曲线综合


<myexample>
<p>已知椭圆 $C$ 的中心为坐标原点, 离心率 $e=\dfrac{\sqrt3}2$, 一个焦点的坐标为 $(\sqrt3,0)$.
</p>
<p>(1) 求椭圆 $C$ 的方程;
</p>
<p>(2) 设直线 $l\colon y= \dfrac12x+m$ 与圆 $C$ 交于 $A$, $B$ 两点, 线段 $AB$ 的垂直平分线交 $x$ 轴于点 $T$. 当 $m$ 变化时, 求 $\triangle TAB$ 面积的最大值.
</p>
</myexample>
<mysolution>
    <p>(1) 设椭圆 $C$ 的方程为 \[
        \frac{x^2}{a^2}+ \frac{y^2}{b^2}= 1\quad (a>b>0),\]
    半焦距为 $c$, 则 \[
        e= \frac{c}{a}= \frac{\sqrt2}2,\quad 
        c= \sqrt3,\quad a^2= b^2+c^2,\]
    解得 $a=2$, $b=1$, 所求方程为 \[
        \frac{x^2}4+ y^2= 1.\]
</p>
<p>(2) (自行作草图) 将直线 $l$ 与椭圆 $C$ 的方程联立, \[\left\{\!\!\begin{array}{l}
        \dfrac{x^2}4+ y^2= 1,\\
        y= \dfrac12x+m,
    \end{array}\right.\]
    消去 $y$ 并整理, 可得 \[
        x^2+ 2mx+ (2m^2-2)= 0.\]
    设 $A(x_1,y_1)$, $B(x_2,y_2)$, 则 \[\left\{\!\!\begin{array}{l}
        x_1+x_2= -2m,\\
        x_1x_2= 2m^2- 2,\\
        \Delta= (2m)^2- 4(2m^2-2)> 0.
    \end{array}\right.\]
    由上述不等式解得 $m^2\in [0,2)$. 
</p>
<p>设线段 $AB$ 的中点为 $M(x_3,y_3)$, 则 \[\begin{gathered}
        x_3= \frac{x_1+x_2}{2}= -m,\\
        y_3= \frac12 x_3+m= \frac{m}{2},
    \end{gathered}\]
    设线段 $AB$ 的垂直平分线为 $l_1$, 则 $l_1$ 与 $l$ 的斜率互为负倒数, 即 $l_1$ 的斜率为 $-2$, 再由 $l_1$ 过点 $M$ 知 \[
        l_1\colon y- \frac{m}{2}= -2[x-(-m)].\]
    因为点 $T$ 是 $l_1$ 与 $x$ 轴的交点, 所以 $T\biggl(-\dfrac34m,0\biggr)$.
</p>
<p>将直线 $l$ 的方程改写为一般式 $x- 2y+ 2m= 0$, 并设点 $T$ 到直线 $l$ 的距离为 $d$, 则 \[
        d= \frac{\biggl|-\dfrac34m- 2\cdot 0+ 2m\biggr|}{\sqrt{1^2+(-2)^2}}
        = \frac{\sqrt5|m|}{4}.\]
    再由弦长公式, \[\begin{aligned}
        |AB|&= \sqrt{1+\biggl(\frac12\biggr)^2}|x_1-x_2|
         = \frac{\sqrt5}{2}\cdot \frac{\sqrt{\Delta}}{|1|}\\
        &= \frac{\sqrt5}{2}\cdot \sqrt{4(2-m^2)}
         = \sqrt5 \sqrt{2-m^2}.
    \end{aligned}\]
    所以 $\triangle TAB$ 的面积为 \[
        \frac12|AB|\cdot d= \frac58 |m|\sqrt{2-m^2}
        = \frac58 \sqrt{m^2(2-m^2)}.\]
    式中 $m^2(2-m^2)$ 是关于 $m^2$ 的二次函数, 由已经解出的 $m^2\in [0,2)$ 知, 当 $m^2= 1$ 时, $m^2(2-m^2)$ 取最大值 $1$. 所以,  $\triangle TAB$ 面积的最大值为 $\dfrac58$.
</p>
</mysolution>
