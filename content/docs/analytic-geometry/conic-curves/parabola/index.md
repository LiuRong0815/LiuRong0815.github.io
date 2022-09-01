---
# bookCollapseSection: true
title: 抛物线
weight: 3
bookHidden: true
prevPage: /docs/analytic-geometry/conic-curves/hyperbola
prevPageTitle: 双曲线
nextPage: /docs/analytic-geometry/conic-curves/conic-curves-line
nextPageTitle: 圆锥曲线综合
---

# 抛物线

<myexample>
<p>已知抛物线 $C\colon y^2=2px$ 过点 $P(1,1)$, 过点 $\biggl(0,\dfrac12\biggr)$ 作直线 $l$ 与抛物线 $C$ 交于不同的两点 $M$, $N$. 过点 $M$ 作 $x$ 轴的垂线, 分别与直线 $OP$, $ON$ 交于点 $A$, $B$, 其中 $O$ 为原点.
</p>
<p>(1) 求抛物线 $C$ 的方程, 并求其焦点坐标和准线方程;
</p>
<p>(2) 求证: $A$ 为线段 $BM$ 的中点.
</p>
</myexample>
<mysolution>
    <p>(1) 将点 $P(1,1)$ 代入抛物线 $C$ 的方程, \[
        1^2= 2p\cdot 1,\quad p=\frac12,\]
    所以 $C\colon y^2=x$, 焦点 $\biggl(\dfrac14,0\biggr)$, 准线 $x= -\dfrac14$.
</p>
<p>(2) 设 $l$ 斜率为 $k$, 则 \[
        l\colon y-\frac12= k(x-0)\Rightarrow
        y= kx+\frac12,\]
    代入 $C\colon y^2=x$ 整理得 \[
        k^2x^2+ (k-1)x+ \frac14= 0.\]
    设 $M(x_1,y_1)$, $N(x_2,y_2)$, 由韦达定理, \[\left\{\!\!\begin{array}{l}
        x_1+x_2= -\dfrac{k-1}{k^2},\\
        x_1x_2= \dfrac1{4k^2},
    \end{array}\right.\]
</p>
<p>由 $P(1,1)$ 知 $OP\colon y=x$, 而 $MA$ 为 $x$ 轴的垂线, 所以 $A(x_1,x_1)$. 再由 $N(x_2,y_2)$ 知 $ON\colon y= \dfrac{y_2}{x_2}x$, 而 $MB$ 为 $x$ 轴的垂线, 所以 $B\biggl(x_1,\dfrac{y_2x_1}{x_2}\biggr)$. 由中点坐标公式, 要证明 $A$ 为线段 $BM$ 的中点, 相当于证明 \[
        y_1+\dfrac{y_2x_1}{x_2}= 2x_1 \Leftrightarrow
        x_2y_1+ y_2x_1= 2x_1x_2.\]
</p>
<p>因为点 $M(x_1,y_1)$, $N(x_2,y_2)$ 在直线 $l$ 上, 所以 \[
        y_1= kx_1+\frac12,\quad y_2= kx_2+\frac12,\]
    结合韦达定理, 进而有 \[\begin{aligned}
        x_2y_1+ y_2x_1
        &= x_2\biggl(kx_1+\frac12\biggr)+ \biggl(kx_2+\frac12\biggr)x_1\\
        &= 2k x_1x_2+ \frac12(x_1+x_2)\\
        &= 2k\cdot \frac1{4k^2}+ \frac12\cdot\biggl(-\frac{k-1}{k^2}\biggr)\\
        &= \frac1{2k^2}- \frac{k-1}{2k^2}= \frac{1}{2k^2}\\
        &= 2x_1x_2.
    \end{aligned}\]
    因此求证的结论成立.
</p>
</mysolution>
