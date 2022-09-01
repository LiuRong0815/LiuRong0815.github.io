---
# bookCollapseSection: true
title: 几何概型
weight: 2
bookHidden: true
prevPage: /docs/probability-statistics/probability/classical-probability
prevPageTitle: 古典概型
nextPage: /docs/probability-statistics/probability/conditional-probability
nextPageTitle: 条件概率
---

# 几何概型

<myexample>
<p>已知事件 $A$, $B$ 发生的概率分别为 $P(A)= 0.5$, $P(B)= 0.3$, 分别在下列条件下求概率 $P(A\cup B)$ 和 $P(AB)$:
</p>
<p>(1) $B\subseteq A$;\quad (2) $A$, $B$ 互斥.
</p>
</myexample>
<mysolution>
    <p>(1) 由 $B\subseteq A$ 知, \[
        A\cup B= A,\quad AB= B,\]
    所以 \[
        P(A\cup B)= P(A)= 0.5,\quad P(AB)= P(B)= 0.3.\]
</p>
<p>(2) 由 $A$, $B$ 互斥知, $AB=\varnothing$, 且 \[
        P(A\cup B)= P(A)+P(B)= 0.5+0.3= 0.8,\]
    所以 $P(AB)= P(\varnothing)= 0$.
</p>
</mysolution>
</p>
<p><myexample>
<p>判断下列说法的正误:
</p>
<p>(1) 若事件 $A$ 与 $B$ 互斥, 则 $P(A)+P(B)= 1$;
</p>
<p>(2) 若事件 $A$ 与 $B$ 满足 $P(A)+P(B)= 1$, 则这两个事件为对立事件;
</p>
<p>(3) “事件 $A$ 与 $B$ 互斥”是“事件 $A$ 与 $B$ 对立”的必要不充分条件;
</p>
<p>(4) 某人打靶时连续射击两次, 则事件“至少有一次中靶”与“至多有一次中靶”互为对立事件.
</p>
</myexample>
<mysolution>
    <p>(1) 事件 $A$ 与 $B$ 互斥说明 $A$ 与 $B$ 不会同时发生, 即 $AB= \varnothing$, 不一定有 $P(A)+P(B)= 1$. 该式在事件 $A$ 与 $B$ 对立时成立, 但对立仅是互斥的一种特例, 所以本说法不正确.
</p>
<p>(2) 不正确, 事件 $A$ 与 $B$ 为对立事件要求 $A\cup B= \Omega$, $AB= \varnothing$, 而 $P(A)+P(B)= 1$ 不能表明 $A$ 与 $B$ 的关系.
</p>
<p>(3) 正确, 对立是互斥的一种特例, 即 $\text{对立}\subseteq\text{互斥}$.
</p>
<p>(4) 不正确, “至少有一次中靶”的反面, 即互斥事件, 是“至多有零次中靶”, 即“全都没中靶”. 一般的, “至少有 $n$ 次中靶”的反面是“至多有 $n-1$ 次中靶”.
</p>
</mysolution>

