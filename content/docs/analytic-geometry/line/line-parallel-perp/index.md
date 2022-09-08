---
# bookCollapseSection: true
title: 直线的平行与垂直
weight: 3
bookHidden: true
prevPage: /docs/analytic-geometry/line/line-equation
prevPageTitle: 直线的方程
nextPage: /docs/analytic-geometry/circle
nextPageTitle: 圆
---

# 直线的平行与垂直


<myexercise>
    设 $m\in\mathbf{R}$, 动直线 $l_1\colon x+my=0$ 和 $l_2\colon mx-y-m+3=0$ 分别过定点 $A,B$, $l_1$ 和 $l_2$ 交于点 $P(x,y)$, 求 $|PA|\cdot |PB|$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>    由题意, $A(0,0)$, $B(1,3)$ 且 $l_1\perp l_2$, 则 $\triangle PAB$ 为直角三角形, 且 $\angle P= 90^\circ$, 所以
    \mymarginpar{发现 $l_1\perp l_2$ 是解本题的关键.}
    \[|PA|^2+ |PB|^2= |AB|^2= 10.\]
    由 $|PA|^2+ |PB|^2\geqslant 2|PA|\cdot |PB|$ 知,
    \[|PA|\cdot |PB|\leqslant 5,\]
    等号成立当且仅当 $|PA|=|PB|= \sqrt5$.
</p>
</mysolution>
