---
# bookCollapseSection: true
title: 圆与直线的位置关系
weight: 2
bookHidden: true
prevPage: /docs/analytic-geometry/circle/circle-equation
prevPageTitle: 圆的方程
nextPage: /docs/analytic-geometry/circle/circle-circle
nextPageTitle: 圆与圆的位置关系
---

# 圆与直线的位置关系

<myexample>
<p>圆 $C$ 经过点 $A(2,-1)$, 与直线 $x+y=1$ 相切, 且圆心在直线 $y=-2x$ 上.
</p>
<p>(1) 求圆 $C$ 的方程;
</p>
<p>(2) 已知直线 $l$ 经过原点, 并且被圆 $C$ 截得的弦长为 $2$, 求直线 $l$ 的方程.
</p>
</myexample>
<mysolution>
    <p>(1) 由圆心 $C$ 在直线 $y=-2x$ 上可设 $C(a,-2a)$, 再设半径 $r$. 将切线 $x+y=1$ 方程改写为 $x+y-1= 0$, 由题意, \[\left\{\!\!\begin{array}{l}
        (2-a)^2+ (-1+ 2a)^2= r^2,\\
        \dfrac{|a+(-2a)-1|}{\sqrt{1^2+1^2}}= r,
    \end{array}\right.\]
    即 \[\left\{\!\!\begin{array}{l}
        5a^2- 8a+ 5= r^2,\\
        |a+1|= \sqrt{2} r.
    \end{array}\right.\]
    将后一式平方并代入前一式, \[
        2(5a^2- 8a+ 5)= (a+1)^2,\]
    解得 $a= 1$, 所以 $r= \sqrt2$, $C(1,-2)$, 圆 $C$ 的方程为 \[
        (x-1)^2+ (y+2)^2= 4.\]
</p>
<p>(2) 因为直线 $l$ 被圆 $C$ 截得的弦长为 $2$, 由圆 $C$ 的半径 $r=\sqrt2$ 和垂径定理, 作图知, 圆心 $C$ 到直线 $l$ 的距离 $d= 1$. 由直线 $l$ 经过原点可设 \[
        l\colon mx+ ny= 0\quad (mn\neq 0),\]
    再由点到直线的距离公式, \[
        d= \frac{|m- 2n|}{\sqrt{m^2+n^2}}= 1,\]
    去分母后平方整理得, $4m= 3n$. 所以 \[
        l\colon 3x+4y=0.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>设直线 $l_1\colon y=kx+1$ 与圆 $x^2+y^2+2x -my=0$ 相交于 $A$, $B$ 两点, 若点 $A$, $B$ 关于直线 $l_2\colon x+y=0$ 对称, 求 $|AB|$ 的值.
</p>
</myexample>
<mysolution>
    <p>由题意, 直线 $l_2$ 是线段 $AB$ 的中垂线, 则 $l_2\perp l_1$ 且 $l_2$ 过圆心. 因为 $l_2\colon x+y=0$ 的斜率为 $-1$, 所以 $l_1$ 的斜率 $k=1$, 其一般式为 \[
        x-y+1=0.\]
    将圆的方程改为标准形式 \[
        (x+1)^2+ \biggl(y-\frac{m}2\biggr)^2= 1+\frac{m^2}{4},\]
    可得圆心 $\biggl(-1,\dfrac{m}2\biggr)$, 代入 $l_2$ 的方程, \[
        -1+\frac{m}2=0,\quad m=2.\]
    因此圆心 $(-1,1)$, 到直线 $l_1\colon x-y+1=0$ 的距离为 \[
        d= \frac{|-1-1+1|}{\sqrt{1+1}}= \frac{1}{\sqrt2}.\]
    又因为圆的半径 $r$ 满足 $r^2= 1+\dfrac{m^2}{4}= 2$, 所以由垂径定理, \[
        |AB|= 2\sqrt{r^2-d^2}= \sqrt6.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知圆 $C$ 过点 $M(0,-2)$, $N(3,1)$, 且圆心 $C$ 在直线 $l_1\colon x+2y+1=0$ 上.
</p>
<p>(1) 求圆 $C$ 的标准方程;
</p>
<p>(2) 设直线 $l_2\colon ax-y+1=0$ 与圆 $C$ 交于不同的两点 $A$, $B$, 是否存在实数 $a$, 使得过点 $P(2,0)$ 的直线 $l$ 垂直平分弦 $AB$? 若存在, 求出实数 $a$ 的值; 若不存在, 请说明理由.
</p>
</myexample>
<mysolution>
    <p>(1) 设 $C(a,b)$, 半径为 $r$, 则 \[
        C\colon (x-a)^2+(y-b)^2= r^2.\]
    由题意, \[\left\{\!\!\begin{array}{l}
        (a-0)^2+(b+2)^2= r^2,\\
        (a-3)^2+(b-1)^2= r^2,\\
        a+2b+1= 0.
    \end{array}\right.\]
    前两式作差并整理得, $a+b=1$, 与第三式联立知, $a=3$, $b=-2$. 所以 \[
        r^2= (a-0)^2+(b+2)^2= 9,\]
    圆 $C$ 的标准方程为 \[
        (x-3)^2+(y+2)^2= 9.\]
</p>
<p>(2) 先假设所求实数 $a$ 存在. 因为直线 $l$ 垂直平分弦 $AB$, 所以 $l$ 过圆心 $C(3,-2)$. 又因为 $l$ 过点 $P(2,0)$, 所以 \[
        l\colon y-0= \frac{-2-0}{3-2}(x-2),\]
    整理得 $l\colon 2x+y-4=0$, 斜率为 $-2$. 由 $AB\perp l$ 知 $l_2\perp l$, 而 $l_2\colon ax-y+1=0$ 的斜率为 $a$, 所以 \[
        (-2)\cdot a= -1,\quad a= \frac12.\]
</p>
<p>此时仍需检验求得的 $a$ 是否符合题意, 读题可知, 需检验 $l_2$ 是否与圆 $C$ 相交. 将 $a$ 的值代入 $l_2$ 知, \[
        l_2\colon x-2y+2=0.\]
    此时圆心 $C(3,-2)$ 到 $l_2$ 的距离 \[
        d= \frac{|3-2\cdot(-2)+2|}{\sqrt{1+4}}
        = \frac{9}{\sqrt5}> 3= r,\]
    表明直线 $l_2$ 与圆 $C$ 相离, 与题意不符. 因此不存在符合题意的 $a$.
</p>
</mysolution>

