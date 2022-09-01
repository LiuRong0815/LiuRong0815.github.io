---
# bookCollapseSection: true
title: 条件概率
weight: 3
bookHidden: true
prevPage: /docs/probability-statistics/probability/geometric-probability
prevPageTitle: 几何概型
nextPage: /docs/probability-statistics/probability/expectation-variation
nextPageTitle: 期望与方差
---

# 条件概率

<p>在古典概型中, 设事件 $A$ 和 $B$ 均由样本空间 $\Omega$ 中的部分样本点组成, 用 $n(P)$ 表示集合 $P$ 中元素的个数, 则概率 $P(A)= \dfrac{n(A)}{n(\Omega)}$, 条件概率 \[
    P(A|B)= \frac{n(AB)}{n(B)}= \frac{P(AB)}{P(B)}.\]
注意, $P(AB)$ 与 $P(A|B)$ 是有区别的, 前者表示事件 $AB$ 在 $\Omega$ 中所占比例, 后者表示事件 $AB$ 在 $B$ 中所占比例, 所以 $P(AB)< P(A|B)$.
</p>
<p><myexample>
<p>某地区气象台统计, 该地区任一天下雨的概率为 $\dfrac4{15}$, 刮风的概率为 $\dfrac2{15}$, 在下雨天里, 刮风的概率为 $\dfrac38$, 求任一天既刮风又下雨的概率.
</p>
</myexample>
<mysolution>
    <p>用事件 $A$ 表示“下雨”, 事件 $B$ 表示“刮风”, 由题意, \[
        P(A)= \frac4{15},\quad P(B)= \frac2{15},\quad
        P(B|A)= \frac38.\]
    因为 $P(B|A)= \dfrac{P(AB)}{P(A)}$, 所以既刮风又下雨的概率为 \[
        P(AB)= P(B|A)P(B)= \frac38\cdot \frac4{15}
        = \frac1{10}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>在市场上供应的灯泡中, 甲厂产品占 $70\%$, 乙厂产品占 $30\%$. 甲厂产品的合格率是 $95\%$, 乙厂产品的合格率是 $80\%$, 求从市场上买到甲厂的合格灯泡的概率.
</p>
</myexample>
<mysolution>
    <p>用事件 $A$ 表示“买到甲厂灯泡”, 事件 $B$ 表示“买到合格灯泡”, 由题意, \[
        P(A)= 0.7,\quad P(B|A)= 0.95.\]
    因为 $P(B|A)= \dfrac{P(AB)}{P(A)}$, 所以买到甲厂的合格灯泡的概率为 \[
        P(AB)= P(B|A)P(B)= 0.7\times 0.95= 0.665.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>一个袋中装有 $7$ 个大小完全相同的球, 其中 $4$ 个白球, $3$ 个黄球. 从中不放回地摸 $4$ 次, 一次摸 $1$ 个球. 已知前两次摸得白球, 求后两次也摸得白球的概率.
</p>
</myexample>
<mysolution>
    <p>前两次摸得白球后, 袋中剩下 $2$ 个白球, $3$ 个黄球. 后两次也摸得白球的概率为 $\dfrac{\mathrm{C}_2^2}{\mathrm{C}_5^2}= \dfrac1{10}$.
</p>
</mysolution>
</p>
<p><myexample>
<p>设某种动物能活到 $20$ 岁的概率为 $0.8$, 能活到 $25$ 岁的概率为 $0.4$. 现有一只这种动物已经 $20$ 岁, 求它能活到 $25$ 岁的概率.
</p>
</myexample>
<mysolution>
    <p>用事件 $A$ 表示“能活到 $20$ 岁”, 事件 $B$ 表示“能活到 $25$ 岁”, 由题意, \[
        P(A)= 0.8,\quad P(B)= 0.4.\]
    所求概率为 \[
        P(B|A)= \frac{P(AB)}{P(A)}= \frac{P(B)}{P(A)}
        = \frac{0.4}{0.8}= \frac12,\]
    式中 $AB= B$ 是因为 $B\subset A$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知口袋中有 $2$ 个白球和 $4$ 个红球, 现从中随机抽取两次, 每次抽取 $1$ 个球.
</p>
<p>(1) 若采取放回的方法连续抽取两次, 求两次都取得白球的概率;
</p>
<p>(2) 若采取不放回的方法连续抽取两次, 求在第一次取出红球的条件下, 第二次取出的仍是红球的概率.
</p>
</myexample>
<mysolution>
    <p>(1) 当采取放回的方法时, 每次抽取都是重新开始, 列树形图可知, 所求概率为 \[\frac26\times \frac26= \frac19.\]
</p>
<p>(2) 当采取不放回的方法时, 第一次取出红球后, 剩下 $2$ 个白球和 $3$ 个红球, 所以第二次取出的仍是红球的概率为 $\dfrac35$.
</p>
</mysolution>


<p>在古典概型中, 样本空间 $\Omega$ 由一些基本样本点构成, 这些样本点代表等可能事件. 事件 $A$ 由 $\Omega$ 中的部分样本点组成, 其发生的概率 $P(A)$ 是指事件 $A$ 中样本点个数占 $\Omega$ 中样本点个数的比例. 例如, 从 $1$, $2$, $\cdots$, $6$ 中任取 $1$ 个数, 则样本空间记为 \[
    \Omega= \{1,2,3,4,5,6\}.\]
设事件 $A$ 为“取到大于 $3$ 的数”, 事件 $B$ 为“取到偶数”, 则 \[
    A= \{4,5,6\},\quad B= \{2,4,6\}.\]
用 $n(P)$ 表示集合 $P$ 中元素的个数, 则 \[
    n(A)= n(B)= 3,\quad n(\Omega)= 6,\]
按概率的定义, \[
    P(A)= P(B)= \frac{n(A)}{n(\Omega)}= \frac12.\]
</p>
<p>对事件 $A$ 和 $B$, 条件概率 $P(A|B)$ 是指当 $B$ 已经发生时, $A$ 发生的概率, 即此时的样本空间应取为 $B$ (而非原先的全集 $\Omega$). 现在对上述例子计算条件概率 $P(A|B)$. 按定义, $P(A|B)$ 指的是“取到偶数时, 该偶数大于 $3$ 的概率”. 此时样本空间变为 $B$ (取到偶数), 考虑的是该样本空间中大于 $3$ 的样本点的个数, 也就是考虑事件 $A\cap B= \{4,6\}$. 在概率中, $A\cap B$ 通常简记为 $AB$, 即省略交集符号. 所以 \[
    P(A|B)= \frac{n(A\cap B)}{n(B)}= \frac{n(AB)}{n(B)}= \frac23.\]
类似地, 由 $A\cap B= B\cap A$ 即 $AB= BA$ 可知, \[
    P(B|A)= \frac{n(BA)}{n(A)}= \frac23.\]
</p>
<p>上面的计算用了条件概率的定义, 也可以用事件的概率来求条件概率. 例如, 因为 \[
    P(A|B)= \frac{n(AB)}{n(B)}
    = \frac{n(AB)/n(\Omega)}{n(B)/n(\Omega)}
    = \frac{P(AB)}{P(B)},\]
所以将 $P(AB)= \dfrac13$ 和 $P(B)= \dfrac12$ 代入, 也可以得到 $P(A|B)= \dfrac23$. 同样地, \[
    P(B|A)= \frac{P(BA)}{P(A)}= \frac{P(AB)}{P(A)}.\]
解题时, 应该根据题目特点, 选择定义法或公式法中的一种.
</p>
<p>概率和条件概率的含义也可以用图形来解释. 样本空间 $\Omega$ 以及事件 $A$ 和 $B$ 的关系可以用韦恩图表示, $P(A)$ 的含义就是集合 $A$ 在全集 $\Omega$ 中所占比例, 而 $P(A|B)$ 的含义就是集合 $A$ 在集合 $B$ 中所占比例. 后者等价于集合 $A\cap B$ 在集合 $B$ 中所占比例. 所以 \[
    P(A)= \frac{n(A)}{n(\Omega)},\quad
    P(A|B)= \frac{n(A\cap B)}{n(B)}.\]
从这个角度来看, $P(A)= P(A|\Omega)$, 也可以视为条件概率.
</p>
<p><center>
    \includegraphics[scale=1.5]{2022-0417-1000-crop}
</center>
</p>
<p>\subsection{条件概率的应用}
</p>
<p><myexample>
<p>从 $1$, $2$, $3$, $4$, $5$ 中任取 $2$ 个不同的数, 设事件 $A$ 为“取到的 $2$ 个数之和为偶数”, 事件 $B$ 为“取到的 $2$ 个数均为偶数”, 求概率 $P(B|A)$.
</p>
</myexample>
<mysolution>
    <p>将取到的两个数用 $(a,b)$ 表示, 则 \[
        A= \{(1,3),(1,5),(2,4),(3,5)\},\quad 
        AB= \{(2,4)\},\]
    所以 \[
        P(B|A)= \frac{n(BA)}{n(A)}= \frac14.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>甲、乙两市都位于长江下游, 根据往年的气象记录, 知道任一天中, 甲市下雨的概率为 $20\%$, 乙市下雨的概率为 $18\%$, 两地同时下雨的概率为 $12\%$. 任取一天, 设事件 $A$ 为“甲市下雨”, 事件 $B$ 为“乙市下雨”, 求概率 $P(A|B)$ 和 $P(B|A)$.
</p>
</myexample>
<mysolution>
    <p>由题意, $P(A)= 0.2$, $P(B)= 0.18$, $P(AB)= 0.12$, 所以 \[\begin{gathered}
        P(A|B)= \frac{P(AB)}{P(B)}= \frac{0.12}{0.18}= \frac23,\\
        P(B|A)= \frac{P(BA)}{P(A)}= \frac{0.12}{0.2}= \frac35.
    \end{gathered}\]
</p>
</mysolution>
