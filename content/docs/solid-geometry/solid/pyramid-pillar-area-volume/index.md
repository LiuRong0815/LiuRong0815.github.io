---
# bookCollapseSection: true
title: 锥和柱的表面积与体积
weight: 2
bookHidden: true
prevPage: /docs/solid-geometry/solid/solid-classification
prevPageTitle: 几何体的分类
nextPage: /docs/solid-geometry/line-plane
nextPageTitle: 直线与平面
---

# 锥和柱的表面积与体积


<p>柱的表面积等于侧面积加两个底面积, 体积等于底面积乘以高. 锥的表面积等于侧面积加底面积, 体积等于 $\dfrac13$ 倍的底面积乘以高.
</p>
<p>用 $V$ 表示体积 (volume), $S$ 表示面积 (area), $h$ 表示高 (height), $r$ 表示底面半径 (radius), $l$ 表示圆锥的母线长, 则前述结论可写为以下公式:
\begin{gather*}
  S_{\text{柱}}= S_{\text{侧}}+2S_{\text{底}},\quad
  S_{\text{圆柱侧}}= 2\pi rh,\\
  V_{\text{柱}}= S_{\text{底}}h,\quad
  V_{\text{圆柱}}= \pi r^2h,\\
  S_{\text{锥}}= S_{\text{侧}}+S_{\text{底}},\quad
  S_{\text{圆锥}}= \pi rl+\pi r^2= \pi r(l+r),\\
  V_{\text{锥}}= \frac13S_{\text{底}}h,\quad
  V_{\text{圆锥}}= \frac13\pi r^2h.
\end{gather*}
圆锥的侧面展开图为扇形, 且扇形的弧就是底面圆周, 所以圆锥的侧面积公式就是扇形的面积公式, 而后者与三角形面积公式类似, 故
\[S_{\text{圆锥侧}}= \frac12\cdot 2\pi r\cdot l= \pi rl.\]
</p>
<p><myexample>
<p>已知正四面体的边长为 $a$, 求其表面积和体积.
</p>
</myexample>
<mysolution>
    <p>正四面体的四个面均为正三角形, 而各正三角形面积为 $\dfrac{\sqrt3}4 a^2$, 所以表面积为 $\sqrt3 a^2$.
</p>
<p>又设正四面体为四面体 $A\text{--}BCD$, 过点 $A$ 作面 $BCD$ 上的高 $AE$, 显然点 $E$ 为正三角形 $BCD$ 的中心. 再过点 $E$ 作 $EF\perp BC$ 于点 $F$, 可知 $\triangle BEF$ 中, $\angle EBF= 30^\circ$, $BF=\dfrac{a}2$, 所以 
    \[EF= \frac{BE}{\sqrt3}= \frac{a}{2\sqrt3},\quad 
        BE= 2EF= \frac{a}{\sqrt{3}}.\]
    考虑 $\mathrm{Rt}\triangle AEB$ 知, 
    \[AE= \sqrt{AB^2- BE^2}= \frac{\sqrt2 a}{\sqrt3},\]
    所以正四面体的体积为
    \[\frac13S_{\triangle BCD}\cdot AE
    = \frac13\cdot \frac{\sqrt3}{4}a^2\cdot \frac{\sqrt2 a}{\sqrt3}
    = \frac{\sqrt{2}a^3}{12}.\]
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0508-2200-crop}
    </center>
</p>
</mysolution>
</p>
<p><myexample>
<p>表面积为 $3\pi$ 的圆锥, 它的侧面展开图是一个半圆, 求其底面直径.
</p>
</myexample>
<mysolution>
    <p>设圆锥的底面半径为 $r$, 母线长为 $l$, 则计算表面积知
    \[\pi r^2+ \pi rl= 3\pi.\]
    由其侧面展开图是一个半圆知 $2\pi r= \pi l$, 联立解得 $r=1$, 所以圆锥的底面直径为 $2r=2$.
</p>
</mysolution>

<myexample>
<p>设底面半径和母线长均为 $r_1$ 的圆柱的表面积为 $S_1$, 半径为 $r_2$ 的球的表面积为 $S_2$. 若 $S_1= S_2$, 求 $r_1$ 与 $r_2$ 的数量关系.
</p>
</myexample>
<mysolution>
    <p>圆柱的表面积为两个底面积与侧面积之和, 而其侧面展开图为矩形, 所以
    \[S_1= 2\pi r_1^2+ 2\pi r_1\cdot r_1= 4\pi r_1^2,\]
    而球的面积为其大圆 (在球面上且圆心为球心的圆) 面积的 $4$ 倍, 即 $S_2= 4\pi r_2^2$, 结合 $S_1= S_2$ 知, $r_1= r_2$.
</p>
</mysolution>

<myexample>
<p>将边长为 $1$ 的正方形以其一边所在直线为旋转轴旋转一周, 求所得几何体的侧面积.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0714-2230-1-crop}\qquad
        \includegraphics[scale=1.5]{2021-0714-2230-2-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>容易知道, 所得几何体为圆柱体, 底面半径 $r$ 和高 $h$ 均为 $1$. 因为圆柱体的侧面展开图为矩形 (分别以底面周长和高为相邻两边), 所以所求侧面积为 \[2\pi r\cdot h= 2\pi\cdot 1\cdot 1= 2\pi.\]
</p>
</mysolution>
</p>
<p>若上题中改为“以一条对角线所在直线为旋转轴旋转一周”, 则所得图形为两个全等且底重合的圆锥的组合图形, 圆锥的底面半径 $r$ 和高 $h$ 均为 $\dfrac{\sqrt2}2$, 且母线 $l$ 为 $1$ (恰是正方形的边长). 又因为圆锥的侧面展开图为扇形 (半径为母线长 $l$, 弧长为底面周长), 面积公式为 $\dfrac12\cdot 2\pi r\cdot l= \pi rl$, 所以此时所得几何体的侧面积为 $2\pi rl= \sqrt2$.
</p>

