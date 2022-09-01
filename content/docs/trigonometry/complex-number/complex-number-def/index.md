---
# bookCollapseSection: true
title: 复数的定义
weight: 1
bookHidden: true
prevPage: /docs/trigonometry/complex-number
prevPageTitle: 复数
nextPage: /docs/trigonometry/complex-number/complex-number-operation
nextPageTitle: 复数的运算
---

# 复数的定义


<p>借用平面直角坐标系可以用点表示复数 $z=x+\mathrm{i}y$: 规定 $z$ 对应点 $(x,y)$, 此时的平面也称为复平面. 由此可知, $1+2\mathrm{i}$ 的对应点在第一象限, $2\mathrm{i}-1$ 的对应点在第二象限. $x$ 轴上的点全为实数, 所以称其为实轴; $y$ 轴上的点除原点外全为纯虚数, 所以称其为虚轴. $z$ 的对应点到原点的距离称为 $z$ 的模 (模长), 记作 $|z|$. 勾股定理表明, $|z|=\sqrt{x^2+y^2}$. 为了后续运算方便, 还定义 $z$ 的共轭复数 $\bar{z}= x-\mathrm{i}y$. 由定义, $z$ 与 $\bar{z}$ 关于实轴对称, 且 $z\bar{z}=x^2+y^2=|z|^2$. 还可以利用共轭复数或直接计算验证复数的模满足如下性质 (与实数的情形一致)
\[|z_1z_2|=|z_1||z_2|,\quad
    \Big|\frac{z_1}{z_2}\Big|= \frac{|z_1|}{|z_2|}\ (z_2\neq0).\]
</p>
<p><myexample>
<p>计算 $\biggl| \dfrac{1+\mathrm{i}}{\mathrm{i}}\biggr|$.
</p>
</myexample>
<mysolution>
    <p>方法一: 先化简绝对值内的式子,
    \[\frac{1+\mathrm{i}}{\mathrm{i}}
        = \frac{(1+\mathrm{i})\cdot(-\mathrm{i})}{\mathrm{i}\cdot(-\mathrm{i})}
        = -\mathrm{i}+1,\]
    所以
    \[\biggl| \dfrac{1+\mathrm{i}}{\mathrm{i}}\biggr|
        = |1-\mathrm{i}|= \sqrt{2}.\]
</p>
<p>方法二: 直接利用模的性质,
    \[\biggl| \dfrac{1+\mathrm{i}}{\mathrm{i}}\biggr|
        = \dfrac{|1+\mathrm{i}|}{|\mathrm{i}|}
        = \sqrt{2}.\]
    很显然, 这种方法更简单.
</p>
</mysolution>
</p>
<p><myexample>
<p>若复数 $z= \cos\theta+\mathrm{i}\sin\theta$, 当 $\theta= \dfrac{4\pi}3$ 时, $z$ 在复平面内对应的点位于哪个象限?
</p>
</myexample>
<mysolution>
    <p>此时 $z= \cos\dfrac{4\pi}3+\mathrm{i}\sin\dfrac{4\pi}3$, 对应点 $\Bigl(\cos\dfrac{4\pi}3,\sin\dfrac{4\pi}3\Bigr)$. 由于
    \[\cos\dfrac{4\pi}3< 0,\quad \sin\dfrac{4\pi}3< 0,\]
    所以 $z$ 在复平面内对应的点位于第三象限.
</p>
</mysolution>
</p>
<p><myexample>
<p>在复平面内, 点 $A(-2,1)$ 对应的复数为 $z$, 计算 $z^2$.
</p>
</myexample>
<mysolution>
    <p>由题意, $z= -2+\mathrm{i}$, 所以 $z^2= 3-4\mathrm{i}$.
</p>
</mysolution>
</p>
<p><myexample>
<p>若复数 $z$ 满足 $(1+\mathrm{i})z= 1+a\mathrm{i}$ ($a\in\mathbf{R}$), 且其在复平面内对应的点位于第二象限, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>解关于 $z$ 的方程,
    \[z= \frac{1+a\mathrm{i}}{1+\mathrm{i}}
        = \frac12(1-a)+ \frac12(1+a)\mathrm{i},\]
    由题意, $1-a< 0$ 且 $1+a>0$, 所以 $a\in(-1,1)$.
</p>
</mysolution>
