---
# bookCollapseSection: true
title: 面面平行
weight: 4
bookHidden: true
prevPage: /docs/solid-geometry/line-plane/line-plane-perp
prevPageTitle: 线面垂直
nextPage: /docs/solid-geometry/line-plane/plane-perp
nextPageTitle: 面面垂直
---

# 面面平行


<myexample>
<p>如图所示, 四棱锥 $P\text{--}ABCD$ 中, $AB\parallel CD$, $AB=2CD$, 点 $E$ 为 $PB$ 的中点.
</p>
<p>(1) 判断 $CE$ 与平面 $PAD$ 的位置关系, 并说明理由.
</p>
<p>(2) 若线段 $AB$ 上的点 $F$ 使得平面 $PAD\parallel \text{平面 }CEF$, 求 $\dfrac{AF}{FB}$ 的值.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0602-2350-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0602-2355-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>(1) 取 $PA$ 中点 $G$, 连接 $GD$, $GE$, 则可证 (自行补全过程)
    \[\begin{gathered}
        GE= \frac12 AB= DC,\\
        GE\parallel AB\parallel DC,
    \end{gathered}\]
    所以四边形 $DCEG$ 为平行四边形, 且 $CE\parallel DG$, 因此 $CE\parallel\text{平面 }PAD$.
</p>
<p>(2) 由平面 $PAD\parallel \text{平面 }CEF$ 知, $AD\parallel FC$, 所以四边形 $ADCF$ 为平行四边形, $AF=DC= \dfrac12AB$, 即 $\dfrac{AF}{FB}= 1$.
</p>
</mysolution>
</p>
<p><myexample>
<p>如图所示, 在正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 点 $S$ 是 $B_1D_1$ 的中点, 点 $E$, $F$, $G$ 分别是 $CB$, $CD$ 和 $CS$ 的中点. 求证: 平面 $EFG\parallel\text{平面 }BDD_1B_1$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0603-0000-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0603-0005-crop}
    </center>
</p>
</myexample>
<myproof>
    <p>连接 $SB$. 由题中的中点信息可知,
    \[EF\parallel BD,\quad EG\parallel BS,\]
    所以平面 $EFG\parallel\text{平面 }BDD_1B_1$.
</p>
</myproof>
</p>
<p>上例中, 条件“点 $S$ 是 $B_1D_1$ 的中点”可以减弱为“点 $S$ 在 $B_1D_1$ 上”(为什么?).
</p>
