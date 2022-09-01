---
# bookCollapseSection: true
title: 椭圆
weight: 1
bookHidden: true
prevPage: /docs/analytic-geometry/conic-curves
prevPageTitle: 圆锥曲线
nextPage: /docs/analytic-geometry/conic-curves/hyperbola
nextPageTitle: 双曲线
---

# 椭圆

<myexample>
<p>已知椭圆 $C\colon \dfrac{x^2}{a^2}+ \dfrac{y^2}{b^2}= 1\ (a>b>0)$ 的焦点坐标分别为 $F_1(-1,0)$, $F_2(1,0)$, $P$ 为椭圆 $C$ 上一点, 满足 $3|PF_1|= 5 |PF_2|$ 且 $\cos\angle F_1PF_2= \dfrac35$.
</p>
<p>(1) 求椭圆 $C$ 的标准方程;
</p>
<p>(2) 设直线 $l\colon y=kx+m$ 与椭圆 $C$ 交于 $A$, $B$ 两点, 点 $Q\biggl(\dfrac14,0\biggr)$ 使得 $|AQ|= |BQ|$, 求实数 $k$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 设椭圆 $C$ 的半焦距为 $c$, 则 $c=1$. 由 $3|PF_1|= 5 |PF_2|$ 可设 \[
        |PF_1|= 5t,\ |PF_2|= 3t,\quad t>0,\]
    按椭圆定义, \[
        2a= |PF_1|+|PF_2|= 8t\Rightarrow a=4t.\]
    在 $\triangle PF_1F_2$ 中, 由余弦定理, \[\begin{aligned}
        \cos\angle F_1PF_2
        &= \frac35= \frac{|PF_1|^2+ |PF_2|^2- |F_1F_2|^2}{2|PF_1|\,|PF_2|}\\
        &= \frac{(5t)^2+(3t)^2- 2^2}{2\cdot 5t\cdot 3t}
         = \frac{34t^2- 4}{30t^2},
    \end{aligned}\]
    解得 $t=\dfrac12$. 所以 \[
        a=4t=2,\quad b= \sqrt{a^2-c^2}= \sqrt3,\]
    椭圆 $C$ 的标准方程为 \[
        \frac{x^2}{4}+ \frac{y^2}{3}= 1.\]
</p>
<p>(2) 联立直线 $l$ 与椭圆 $C$ 的方程, 消去 $y$ 并整理, \[\begin{gathered}
        \frac{x^2}{4}+ \frac{(kx+m)^2}{3}= 1,\\
        (3+4k^2)x^2+ 8mkx+ 4m^2-12= 0.
    \end{gathered}\]
    设 $A(x_1,y_1)$, $B(x_2,y_2)$, 由韦达定理, \[\left\{\!\!\begin{array}{l}
        x_1+x_2= -\dfrac{8mk}{3+4k^2},\\
        x_1x_2= \dfrac{4m^2-12}{3+4k^2},\\
        \Delta= (8mk)^2- 4(3+4k^2)(4m^2-12)> 0,
    \end{array}\right.\]
    第三式解得 $4k^2+3> m^2$.
</p>
<p>设 $AB$ 的中点为 $M(x_0,y_0)$, 则 \[\begin{gathered}
        x_0= \frac12(x_1+x_2)= -\frac{4mk}{3+4k^2},\\
        y_0= kx_0+m= \frac{3m}{3+4k^2}.
    \end{gathered}\]
    因为 $|AQ|= |BQ|$, 所以 $MQ$ 是线段 $AB$ 的中垂线, 两者斜率互为负倒数, 即 \[
        -1= \frac{y_0- 0}{x_0- \dfrac14}\cdot k
        = \frac{\dfrac{3m}{3+4k^2}}{-\dfrac{4mk}{3+4k^2}- \dfrac14}\cdot k,\]
    整理得, $m= -\dfrac{3+4k^2}{4k}$. 将此式代入由 $\Delta>0$ 解出的不等式, 即得 \[\begin{gathered}
        4k^2+3> \biggl(-\dfrac{3+4k^2}{4k}\biggr)^2,\\
        k\in \biggl(-\infty,-\frac12\biggr)\cup \biggl(\frac12,+\infty\biggr).
    \end{gathered}\]
</p>
</mysolution>

<myexample>
<p>直线 $x-y+1= 0$ 与椭圆 $\dfrac{x^2}{4}+ \dfrac{y^2}{2}= 1$ 交于 $A$, $B$ 两点, 求弦 $AB$ 的中点 $M$ 的坐标.
</p>
</myexample>
<mysolution>
    <p>将直线方程代入椭圆方程, 消去 $y$ 并整理, \[
        3x^2+ 4y^2-2= 0.\]
    设 $A(x_1,y_1)$, $B(x_2,y_2)$, 则由韦达定理, $x_1+x_2= -\dfrac43$.
    再设 $M(x_0,y_0)$, 由中点坐标公式, \[
        x_0= \dfrac12(x_1+x_2)= -\frac23,\]
    代入直线方程知所求中点 $M$ 的坐标为 $\biggl(-\dfrac23,\dfrac13\biggr)$.
</p>
</mysolution>
</p>
<p><myexample>
<p>经过椭圆 $\dfrac{x^2}{2}+ y^2= 1$ 的左焦点 $F_1$ 作倾斜角为 $60^\circ$ 的直线 $l$, 与椭圆相交于 $A$, $B$ 两点, 求弦的中点 $M$ 的坐标.
</p>
</myexample>
<mysolution>
    <p>左焦点 $F_1$ 为 $(-1,0)$, 则 \[
        l\colon y=\tan 60^\circ(x+1)= \sqrt{3}(x+1).\]
    将直线 $l$ 的方程代入椭圆方程, 消去 $y$ 并整理, \[
        7x^2+ 12y^2-4= 0.\]
    设 $A(x_1,y_1)$, $B(x_2,y_2)$, 则由韦达定理, $x_1+x_2= -\dfrac{12}7$. 再设 $M(x_0,y_0)$, 由中点坐标公式, \[
        x_0= \dfrac12(x_1+x_2)= -\frac67,\]
    代入直线 $l$ 的方程知所求中点 $M$ 的坐标为 $\biggl(-\dfrac67,\dfrac{\sqrt3}7\biggr)$.
</p>
</mysolution>

