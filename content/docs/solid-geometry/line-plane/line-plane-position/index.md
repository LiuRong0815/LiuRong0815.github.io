---
# bookCollapseSection: true
title: 直线与平面的位置关系
weight: 1
bookHidden: true
prevPage: /docs/solid-geometry/line-plane
prevPageTitle: 直线与平面
nextPage: /docs/solid-geometry/line-plane/line-plane-parallel
nextPageTitle: 线面平行
---

# 直线与平面的位置关系

<myexample>
<p>若直线 $l$ 与平面 $\alpha$ 相交, 判断下列命题的正误:
</p>
<p>(1) $\alpha$ 内存在无数条直线与 $l$ 异面;
</p>
<p>(2) $\alpha$ 内存在唯一一条直线与 $l$ 平行;
</p>
<p>(3) $\alpha$ 内存在无数条直线与 $l$ 平行;
</p>
<p>(4) $\alpha$ 内的直线与 $l$ 都相交.
</p>
</myexample>
<mysolution>
    <p>(1) 正确. $\alpha$ 内的直线, 只要不与 $l$ 相交, 两者即为异面关系.
</p>
<p>(2) 错误. 若 $\alpha$ 内存在直线与 $l$ 平行, 那么 $\alpha\parallel l$ (线面平行的判定定理), 与已知条件矛盾.
</p>
<p>(3) 错误. 理由同上.
</p>
<p>(4) 错误. 只要在 $\alpha$ 内的直线不过 $l$ 与 $\alpha$ 交点, 该直线就与 $l$ 不相交.
</p>
</mysolution>
</p>
<p><myexample>
<p>点 $M$, $N$ 分别是正方体 $ABCD$--$A_1B_1C_1D_1$ 的两棱 $AA_1$ 与 $A_1B_1$ 的中点, 点 $P$ 是正方形 $ABCD$ 的中心, 判断 $MN$ 与平面 $PCB_1$ 的位置关系.
</p>
</myexample>
<mysolution>
    <p>此题应先将平面 $PCB_1$ 延展, 找到其与正方体 $ABCD$--$A_1B_1C_1D_1$ 表面的交线, 然后判断位置关系. 由已知, $CP$ 延长线必过点 $A$, 所以平面 $PCB_1$ 也是平面 $ACB_1$. 因为 $MN$ 是 $\triangle AA_1B_1$ 的中位线, 所以 $MN\parallel AB_1$, 继而 $MN\parallel \text{面 }ACB_1$ (线面平行的判定定理), 即 $MN\parallel \text{面 }PCB_1$.
</p>
</mysolution>
</p>
<p><myexample>
<p>判断下列命题的正误:
</p>
<p>(1) 如果两条直线 $a$, $b$ 满足 $a\parallel b$, 那么 $a$ 平行于过 $b$ 的任何一个平面;
</p>
<p>(2) 如果直线 $a$ 和平面 $\alpha$ 平行, 那么 $a$ 与 $\alpha$ 内的任何一条直线都平行;
</p>
<p>(3) 如果直线 $a$, $b$ 和平面 $\alpha$ 满足 $a\parallel\alpha$, $b\parallel \alpha$, 那么 $a\parallel b$.
</p>
</myexample>
<mysolution>
    <p>(1) 不正确. 过 $b$ 的平面也可能经过 $a$, 此时 $a$ 在平面内.
</p>
<p>(2) 不正确. 此时 $a$ 仅与 $\alpha$ 内的一部分直线平行 (需方向一致).
</p>
<p>(3) 不正确. $a$ 与 $b$ 可能相交或异面. 平行线才有传递性, 即若直线 $a$, $b$, $c$ 满足 $a\parallel b$, $b\parallel c$, 则 $a\parallel c$.
</p>
</mysolution>
