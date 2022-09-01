---
# bookCollapseSection: true
title: 线面垂直
weight: 3
bookHidden: true
prevPage: /docs/solid-geometry/line-plane/line-plane-parallel
prevPageTitle: 线面平行
nextPage: /docs/solid-geometry/line-plane/plane-parallel
nextPageTitle: 面面平行
---

# 线面垂直

<myexample>
<p>如图所示, 在四棱锥 $P\text{--}ABCD$ 中, 底面 $ABCD$ 为直角梯形, 且 $AD\parallel BC$, $\angle ABC=\angle PAD= 90^\circ$, 侧面 $PAD\perp$ 底面 $ABCD$, $PA= AB= BC = \dfrac12 AD$.
</p>
<p>(1) 求证: $CD\perp$ 平面 $PAC$;
</p>
<p>(2) 侧棱 $PA$ 上是否存在点 $E$, 使得 $BE\parallel$ 平面 $PCD$? 若存在, 指出点 $E$ 的位置并证明; 若不存在, 请说明理由.
</p>
<p><center>
        \includegraphics[scale=1.5]{2022-0430-1800-crop.pdf}
    </center>
</p>
</myexample>
<mysolution>
    <p>以下简要描述解题过程, 详情可自行补充.
</p>
<p>(1) 取 $AD$ 中点 $M$, 连接 $CM$, 可证 $\triangle ACD$ 为等腰直角三角形, $DC\perp AC$. 由题意得 $PA\perp$ 面 $ABCD$, 所以 $PA\perp CD$, 则 $CD\perp$ 平面 $PAC$.
</p>
<p>(2) 可以验证, 当 $E$ 为 $PA$ 中点时, 符合题意.
</p>
</mysolution>


<myexample>
<p>如左图所示, 在棱长为 $1$ 的正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 点 $E$ 是棱 $BC$ 的中点, 点 $F$ 是棱 $CD$ 上的动点. 试确定点 $F$ 的位置, 使得 $D_1E\perp$ 平面 $AB_1F$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0701-2110-1-crop}\qquad
        \includegraphics[scale=1.5]{2021-0701-2110-2-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>如右图所示, 连接 $A_1B$, $D_1C$, 则 $D_1E\subset$ 平面 $A_1BCD_1$. 由 $AB_1\perp A_1B$ 和 $AB_1\perp BC$ 可知 $AB_1\perp$ 平面 $A_1BCD_1$, 则 $AB_1\perp D_1E$, 所以只需 $D_1E\perp AF$ 即可说明 $D_1E\perp$ 平面 $AB_1F$.
</p>
<p>再连接 $DE$. 因为 $DD_1\perp$ 平面 $ABCD$, 所以 $D_1D\perp AF$. 此时 $D_1E\perp AF$ 等价于 $AF\perp$ 平面 $D_1DE$, 亦等价于 $DE\perp AF$. 在正方形 $ABCD$ 中, 因为点 $E$ 是 $BC$ 的中点, 由平面几何知识可得, $DE\perp AF$ 等价于 $F$ 是 $CD$ 中点.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 以上用的是分析法. 实际解题时, 可直接先猜测 $F$ 是 $CD$ 中点, 然后在该条件下证明 $D_1E\perp$ 平面 $AB_1F$: 先证 $DE\perp AF$, 再证 $AF\perp$ 平面 $D_1DE$, 得到 $AF\perp D_1E$; 接着证 $AB_1\perp$ 平面 $A_1BCD_1$, 则 $AB_1\perp D_1E$, 因此 $D_1E\perp$ 平面 $AB_1F$.
</p>
<p>(2) 用空间向量法 (高二会学到) 可以很容易列出与 $D_1E\perp$ 平面 $AB_1F$ 等价的方程组, 通过解方程 (通常是二元一次方程组) 可以确定点 $F$ 的位置.
</p>
</myremark>
</p>
<p><myexample>
<p>如左图所示, 正方形 $ACDE$ 的边长为 $2$, $AD$ 与 $CE$ 的交点为 $M$, $AE\perp$ 平面 $ABC$, $AC\perp BC$ 且 $AC=BC$.
</p>
<p>(1) 求证: $AM\perp$ 平面 $EBC$;
</p>
<p>(2) 求直线 $EC$ 与平面 $ABE$ 所成角的正切值.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0701-2120-1-crop}\qquad
        \includegraphics[scale=1.5]{2021-0701-2120-2-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>(1) 因为 $AE\perp$ 平面 $ABC$, 所以平面 $ACDE\perp$ 平面 $ABC$. 由 $AC\perp BC$ 知 $BC\perp$ 平面 $ACDE$, 则 $BC\perp AM$. 在正方形 $ACDE$ 中, $AM\perp EC$, 所以 $AM\perp$ 平面 $EBC$.
</p>
<p>(2) 首先要确定直线 $EC$ 在平面 $ABE$ 上的投影, 通常是过直线上某一点做平面的垂线. 如右图所示, 过点 $C$ 作 $CF\perp AB$ 于点 $F$, 连接 $EF$. 因为 $AE\perp$ 平面 $ABC$, 所以 $AE\perp CF$. 因此 $CF\perp$ 平面 $ABE$, 表明 $EF$ 是 $EC$ 在平面 $ABE$ 上的投影, $\angle CEF$ 为直线 $EC$ 与平面 $ABE$ 所成角.
</p>
<p>因为正方形 $ACDE$ 的边长为 $2$, $AC=BC$ 且 $AC\perp BC$, 所以 $AB= 2\sqrt2$, $AF=CF=\sqrt2$. 而 $AE\perp$ 平面 $ABC$, 所以 $AE\perp AF$, 结合 $AE=2$ 知 $EF=\sqrt6$, 因此所求正切值为
    \[\tan\angle CEF= \frac{CF}{EF}
        = \frac{\sqrt2}{\sqrt6}= \frac{\sqrt3}3.\]
    由结果可以看出 $\angle CEF= 30^\circ$.
</p>
</mysolution>

