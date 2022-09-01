---
# bookCollapseSection: true
title: 面面垂直
weight: 5
bookHidden: true
prevPage: /docs/solid-geometry/line-plane/plane-parallel
prevPageTitle: 面面平行
nextPage: /docs/solid-geometry/line-plane-space-vector
nextPageTitle: 用空间向量表示线面关系
---

# 面面垂直


<myexample>
<p>如左图所示, 已知 $P$ 是边长为 $2a$ 的菱形 $ABCD$ 所在平面外一点, $\angle ABC = 60^\circ$, $PC\perp$ 平面 $ABCD$, $PC =2a$, $E$ 为 $PA$ 的中点.
</p>
<p>(1) 求证: 平面 $EDB\perp$ 平面 $ABCD$.
</p>
<p>(2) 求二面角 $A\text{--}EB\text{--}D$ 的正切值.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0701-2130-1-crop}\qquad
        \includegraphics[scale=1.5]{2021-0701-2130-2-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>(1) 如右图所示, 连接 $AC$, 设其与 $BD$ 交于点 $F$, 则 $F$ 为 $AC$ 中点. 再连接 $EF$. 因为 $E$ 为 $PA$ 的中点, 所以 $PC\parallel EF$. 由 $PC\perp$ 平面 $ABCD$ 知, $EF\perp$ 平面 $ABCD$, 所以平面 $EDB\perp$ 平面 $ABCD$.
</p>
<p>(2) 求二面角的平面角, 关键是构造出对应的图形, 通常是过一个半平面上一点作到另一个半平面和公共棱的垂线, 以构成封闭的直角三角形.
</p>
<p>因为在边长为 $2a$ 的菱形 $ABCD$ 中 $\angle ABC = 60^\circ$, 所以 $AF\perp BD$, $AF=a$, $BF=\sqrt3a$. 由 $EF\perp$ 平面 $ABCD$ 知 $EF\perp AF$, 所以 $AF\perp$ 平面 $BDE$. 过点 $F$ 作 $FG\perp BE$ 于点 $G$, 连接 $GA$, 则易知 $BE\perp$ 平面 $AFG$. 因此 $AG\perp BE$, 结合 $FG\perp BE$ 知 $\angle AGF$ 为二面角 $A\text{--}EB\text{--}D$ 的平面角. 在 $\mathrm{Rt}\triangle BEF$ 中, $EF=\dfrac12 PC= a$, $BF=\sqrt3a$, 所以 $FG= \dfrac{\sqrt3 a}2$, 所求正切值为
    \[\tan\angle AGF= \frac{AF}{FG}= \frac{a}{\sqrt3 a/2}
        = \frac{2\sqrt3}3.\]
</p>
</mysolution>

<myexample>
<p>如图所示, 在四棱锥 $P\text{--}ABCD$ 中, $PA\perp$ 平面 $ABCD$, 底面 $ABCD$ 为菱形, $E$ 为 $CD$ 的中点.
</p>
<p>(1) 求证: $BD\perp$ 平面 $PAC$;
</p>
<p>(2) 若 $\angle ABC=60^\circ$, 求证: 平面 $PAB\perp$ 平面 $PAE$.
</p>
</myexample>
<myproof>
    <p>(1) 因为底面 $ABCD$ 为菱形, 所以 $AC\perp BD$. 由 $PA\perp$ 平面 $ABCD$ 知 $PA\perp BD$, 因此 $BD\perp$ 平面 $PAC$.
</p>
<p>(2) 因为菱形 $ABCD$ 中, $\angle ABC=60^\circ$, 所以 $\triangle ACD$ 均为等边三角形, $AB\parallel CD$. 由 $E$ 为 $CD$ 的中点知 $AE\perp CD$, 因此 $AE\perp AB$. 由 $PA\perp$ 平面 $ABCD$ 知 $PA\perp AE$, 所以 $AE\perp$ 平面 $PAB$, 进而平面 $PAB\perp$ 平面 $PAE$.
</p>
</myproof>

<myexample>
<p>已知四棱椎 $P\text{--}ABCD$ 中, 底面 $ABCD$ 为梯形, $BC\parallel AD$, $\angle ABC= 90^\circ$, $PA= BA= BC= \dfrac12 AD=1$, 平面 $PAB\perp$ 平面 $ABCD$, $PB=\sqrt2$, 点 $E$, $F$ 分别为 $PA$, $AD$ 中点,
</p>
<p>证明: (1) 平面 $BEF\parallel$ 平面 $PCD$;\quad
    (2) 平面 $PCD\perp$ 平面 $PAC$.
</p>
</myexample>
<myproof>
    <p>(1) 因为点 $F$ 为 $AD$ 中点, 所以 $FD= \dfrac12 AD= 1= BC$. 由 $BC\parallel AD$ 知四边形 $BCDF$ 为平行四边形, 则 $BF\parallel CD$. 因为点 $E$ 为 $PA$ 中点, 所以 $EF\parallel PD$, 因此平面 $BEF\parallel$ 平面 $PCD$.
</p>
<p>(2) 因为 $PA= BA=1$, $PB=\sqrt2$, 所以 $\angle PAB= 90^\circ$, 而平面 $PAB\perp$ 平面 $ABCD$, 因此 $PA\perp$ 平面 $ABCD$, 从而 $PA\perp CD$. 连接 $CF$, 由 $AF= BC= 1$, $AP\parallel BC$ 知四边形 $ABCF$ 为平行四边形, 所以 $CF=1$. 结合 $AF= CD= FD=1$ 知, $\angle ACD= 90^\circ$, 即 $AC\perp CD$. 结合 $PA\perp CD$ 知, $CD\perp$ 平面 $PAC$, 故平面 $PCD\perp$ 平面 $PAC$.
</p>
</myproof>

