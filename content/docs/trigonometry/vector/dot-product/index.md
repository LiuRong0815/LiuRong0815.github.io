---
# bookCollapseSection: true
title: 向量的内积
weight: 3
bookHidden: true
prevPage: /docs/trigonometry/vector/vec-basic-theorem
prevPageTitle: 平面向量基本定理
nextPage: /docs/trigonometry/vector/space-vector
nextPageTitle: 空间向量
---

# 向量的内积


<myexample>
<p>已知正方形 $ABCD$ 的边长为 $2$, 点 $E$ 为 $AB$ 的中点, 点 $P$ 为对角线 $BD$ 上的动点, 求 $\overrightarrow{PE}\cdot\overrightarrow{PC}$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>以点 $B$ 为原点, $BC$ 为 $x$ 轴, $BA$ 为 $y$ 轴, 建立平面直角坐标系 (建议作图帮助理解), 则 $E(0,1)$, $C(2,0)$. 由题意可设 $P(p,p)$, 其中 $p\in[0,2]$, 则
    \[\overrightarrow{PE}\cdot\overrightarrow{PC}
    = (-p,1-p)\cdot(2-p,-p)
    = 2p^2-3p.\]
    结合二次函数单调性知, $\overrightarrow{PE}\cdot\overrightarrow{PC}
    \in \biggl[-\dfrac98,2\biggr]$.
</p>
</mysolution>

<myexample>
<p>已知向量 $\bm{a}$, $\bm{b}$ 的夹角为 $\dfrac{2\pi}3$, $|\bm{a}|=1$, $|\bm{b}|=2$. 若 $2\bm{a}-\bm{b}$ 与 $t\bm{a}+\bm{b}$ 垂直, 求 $t$ 的值.
</p>
</myexample>
<mysolution>
    <p>由题意, $\bm{a}^2= 1$, $\bm{b}^2= 4$, $\bm{a}\cdot\bm{b}= -1$,
    \[(2\bm{a}-\bm{b})(t\bm{a}+\bm{b})=0,\quad\text{即}\quad
        2t\bm{a}^2+(2-t)\bm{a}\cdot\bm{b}- \bm{b}^2=0,\]
    解得 $t= 2$.
</p>
</mysolution>
