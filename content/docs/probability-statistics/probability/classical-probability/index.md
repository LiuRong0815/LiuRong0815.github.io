---
# bookCollapseSection: true
title: 古典概型
weight: 2
bookHidden: true
prevPage: /docs/probability-statistics/probability/random-event
prevPageTitle: 随机事件的概率
nextPage: /docs/probability-statistics/probability/geometric-probability
nextPageTitle: 几何概型
---

# 古典概型

<p>两个事件 $A$, $B$ 互斥是指这两个事件“互相排斥”, 即 $A$ 与 $B$ 不会同时发生, 用符号表示为 $A\cap B= \varnothing$, 或 $AB= \varnothing$. 因此 \[P(A\cup B)= P(A)+ P(B).\] 如在抽取扑克牌时, 事件“抽到红牌”与“抽到黑牌”为互斥事件, 因为没有扑克牌既是红牌又是黑牌. 两个事件 $A$, $B$ 对立是指这两个事件“非此即彼”, 即 $A$ 与 $B$ 不会同时发生, 但是必有一个发生. 设总体为 $\Omega$, 则此时 \[
    A\cap B= \varnothing,\quad A\cup B=\Omega,\]
因此有 $P(A)+P(B)= P(\Omega)= 1$. “对立”是“互斥”的特殊情况.
</p>
<p>两个事件 $A$, $B$ 相互独立是指其中一个事件是否发生不影响另一个事件发生的概率. 设总体为 $\Omega$, 而事件 $A$ 已发生, 则此时事件 $B$ 发生的概率为 \[
    \frac{n(AB)}{n(A)}
    = \frac{n(AB)/n(\Omega)}{n(B)/n(\Omega)}
    = \frac{P(AB)}{P(A)}.\]
上式等于不考虑事件 $A$ 是否发生时, 事件 $B$ 发生的概率 $P(B)$, 所以 \[
    \frac{P(AB)}{P(A)}= P(B),\quad\text{即}\quad
        P(AB)= P(A)P(B).\]
若假设事件 $B$ 已发生, 同样可以推出 $P(AB)= P(A)P(B)$. 反过来, 由 $P(AB)= P(A)P(B)$ 也可以推出事件 $A$, $B$ 中一个事件是否发生不影响另一个事件发生的概率. 所以要检验两个事件 $A$, $B$ 是否相互独立, 只需要检验 $P(AB)= P(A)P(B)$ 是否成立.
</p>
<p>两个事件 $A$, $B$ 是否互斥与它们是否相互独立没有必然联系, 两者描述的是两个事件不同的关系.
</p>
<p><myexample>
<p>从一副扑克牌 ($52$ 张, 不含大、小王) 中任意抽取一张, 记事件 $A$ 为“抽到K”, 事件 $B$ 为“抽到红牌” (红牌指红桃或方块), 事件 $C$ 为“抽到 J”, 判断下列每对事件是否互斥、是否相互独立, 并说明原因.
</p>
<p>(1) $A$ 与 $B$;\quad (2) $A$ 与 $C$.
</p>
</myexample>
<mysolution>
    <p>题中的扑克牌有四种花色: 黑桃、黑梅、红桃、红方, 各有标记 1---10, J, Q, K, 所以共 $52$ 张. 总体 $\Omega$ 为“从一副扑克牌中任意抽取一张”, 则 $n(\Omega)= 52$.
</p>
<p>(1) 因为事件 $AB$ 为“抽到红色 K”, 即“抽到红桃 K 和红方 K”, 所以 $AB\neq\varnothing$, 事件 $A$ 与 $B$ 不互斥. 又因为 \[\begin{gathered}
        P(A)= \frac{4}{52}= \frac1{13},\quad
        P(B)= \frac{2\times 13}{52}= \frac12,\\
        P(AB)= \frac{2}{52}= \frac{1}{26},
    \end{gathered}\] 所以 $P(AB)= P(A)P(B)$, 事件 $A$, $B$ 相互独立.
</p>
<p>(2) 因为事件 $AC$ 为“同时抽到 J 和 K”, 所以 $AB=\varnothing$, 事件 $A$ 与 $C$ 互斥. 又因为 \[\begin{gathered}
        P(A)= \frac1{13},\quad
        P(C)= \frac{4}{52}= \frac1{13},\\
        P(AC)= \frac{0}{52}= 0,
    \end{gathered}\] 所以 $P(AC)\neq P(A)P(C)$, 事件 $A$, $C$ 不相互独立.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知甲箱子里装有 $3$ 个白球, $2$ 个黑球, 乙箱子里装有 $2$ 个白球, $2$ 个黑球. 从这两个箱子里分别随机摸出 $1$ 个球, 求恰有 $1$ 个白球的概率.
</p>
</myexample>
<mysolution>
    <p>总体 $\Omega$ 为“从这两个箱子里分别随机摸出 $1$ 个球”, 则 $n(\Omega)= 5\times 4= 20$. “恰有 $1$ 个白球”表示
</p>
<p>(1) 从甲箱子中摸出 $1$ 个白球, 从乙箱子中摸出 $1$ 个黑球;
</p>
<p>(2) 从甲箱子中摸出 $1$ 个黑球, 从乙箱子中摸出 $1$ 个白球,\\
    对应的样本点个数为 \[3\times 2+ 2\times 2= 10,\] 所以所求概率为 $\dfrac{10}{n(\Omega)}= \dfrac12$.
</p>
</mysolution>
</p>
<p><myexample>
<p>甲、乙两名射手射击同一目标, 命中的概率分別为 $0.8$ 和 $0.7$. 若各射击一次, 求命中目标的概率。
</p>
</myexample>
<mysolution>
    <p>方法一: 事件“命中目标”可分为三种情况, 即 (1) 甲中但乙未中; (2) 甲未中但乙中; (3) 甲、乙均命中. 这三个事件互斥, 故所求概率为 \[
        0.8\times (1-0.7)+ (1-0.8)\times 0.7+ 0.8\times 0.7= 0.94.\]
</p>
<p>方法二: 事件“命中目标”的对立事件为“未命中目标”, 后者的概率为 \[
        (1-0.8)\times (1-0.7)= 0.06,\]
    所以所求概率为 $1- 0.06= 0.94$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>计算一个事件的概率, 除了直接计算 (如方法一), 有时也考虑先计算其对立事件 (如方法二). 应事先预估两者的计算量, 并选择合适的计算方法.
</p>
</myremark>
</p>
<p><myexample>
<p>乒乓球比赛规定: 一局比赛, 双方比分在 $10:10$ 平前, 一方连续发球 $2$ 次后, 对方再连续发球 $2$ 次, 依次轮换; 每次发球, 胜方得 $1$ 分, 负方得 $0$ 分.
</p>
<p>在甲、乙的比赛中, 设甲发球后得 $1$ 分的概率为 $\dfrac35$, 乙发球后得 $1$ 分的概率为 $\dfrac23$, 且每次发球的胜负结果相互独立. 甲、乙的一局比赛中, 甲先发球, 求开始第四次发球时, 甲、乙的比分为 $1:2$ 的概率.
</p>
</myexample>
<mysolution>
    <p>由题意, 前四次发球者分别为: 甲, 甲, 乙, 乙. 因为开始第四次发球时, 甲、乙的比分为 $1:2$, 所以前三次发球后, 甲胜一次, 乙胜两次. 设事件 $A$ 为“仅第一次发球后甲胜”, 事件 $B$ 为“仅第二次发球后甲胜”, 事件 $C$ 为“仅第三次发球后甲胜”, 则 \[\begin{aligned}
        P(A)&= \frac35\times \biggl(1-\frac35\biggr)\times \frac23
            = \frac{12}{75},\\
        P(B)&= \biggl(1-\frac35\biggr)\times \frac35\times \frac23
            = \frac{12}{75},\\
        P(C)&= \biggl(1-\frac35\biggr)\times \biggl(1-\frac35\biggr)\times \biggl(1-\frac23\biggr)
            = \frac{4}{75},\\
    \end{aligned}\]
    而事件 $A$, $B$, $C$ 相互独立, 所以所求概率为 \[
        P(A)+P(B)+P(C)= \frac{28}{75}.\]
</p>
</mysolution>

<myexample>
<p>从甲袋中摸出 $1$ 个红球的概率是 $\dfrac13$, 从乙袋中摸出 $1$ 个红球的概率是 $\dfrac12$. 现从两袋中各摸出 $1$ 个球, 求下列事件发生的概率:
</p>
<p>(1) 两个球都是红球;\quad
    (2) 两个球不都是红球;
</p>
<p>(3) 两个球中至少有 $1$ 个红球;\quad
    (4) 两个球中恰有 $1$ 个红球.
</p>
</myexample>
<mysolution>
    <p>记“从甲袋中摸出 $1$ 个红球”为事件 $A$,“从乙袋中摸出 $1$ 个红球”为事件 $B$, 则 $P(A)= \dfrac13$, $P(B)= \dfrac12$, 且 $A$, $B$ 为独立事件.
</p>
<p>(1)“两个球都是红球”为事件 $AB$, 则 \[
        P(AB)= P(A)P(B)= \frac16.\]
</p>
<p>(2)“两个球不都是红球”为事件 $\overline{A}\,\overline{B}$, 则 \[
        P(\overline{A}\,\overline{B})
        = P(\overline{A})P(\overline{B})
        = (1-P(A))(1-P(B))
        = \frac13.\]
    式中 $\overline{A}$ 表示事件 $A$ 的对立事件.
</p>
<p>(3)“两个球中至少有 $1$ 个红球”的互斥事件为“两个球都不是红球”, 即 $\overline{A}\,\overline{B}$, 则所求概率为 \[
        1- P(\overline{A}\,\overline{B})
        = 1- \frac13
        = \frac23.\]
</p>
<p>(4)“两个球中恰有 $1$ 个红球”为事件 $\overline{A}\,B\cup A\,\overline{B}$, 则 \[
        P(\overline{A}\,B\cup A\,\overline{B})
        = P(\overline{A}\,B)+ P(A\,\overline{B})
        = \frac12.\]
</p>
</mysolution>
</p>
<p><myremark>
    <p>上题中的答案均可作树形图后计算得到, 且用树形图求解更方便.
</p>
</myremark>

