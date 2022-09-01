---
# bookCollapseSection: true
title: 二项分布
weight: 1
bookHidden: true
prevPage: /docs/probability-statistics/probability-distribution
prevPageTitle: 概率分布
nextPage: /docs/probability-statistics/probability-distribution/normal-distribution
nextPageTitle: 正态分布
---

# 二项分布

<myexample>
<p>某篮球队员在比赛中每次罚球的命中率相同, 且在两次罚球中至多命中一次的概率为 $\dfrac{16}{25}$, 求该队员每次罚球的命中率.
</p>
</myexample>
<mysolution>
    <p>设该队员每次罚球的命中率为 $p$. 因为“在两次罚球中至多命中一次”的反面, 即互斥事件, 是“在两次罚球中两次都命中”, 所以前者的概率为 \[
        1- p^2= \dfrac{16}{25}\Rightarrow p= \frac35.\]
</p>
</mysolution>



<myexample>
<p>甲、乙两个篮球运动员互不影响地在同一位置投球, 命中率分别为 $\dfrac12$ 与 $p$, 且乙投球 $2$ 次均未命中的概率为 $\dfrac1{16}$.
</p>
<p>(1) 求乙投球的命中率 $p$;
</p>
<p>(2) 若乙投球 $2$ 次, 命中的次数记为 $Y$, 求 $Y$ 的分布列.
</p>
<p>(2) 若甲投球 $1$ 次, 乙投球 $2$ 次, 两人共命中的次数记为 $X$, 求 $X$ 的分布列.
</p>
</myexample>
<mysolution>
    <p>(1) 由题意, \[
        (1-p)^2= \dfrac1{16}\Rightarrow p= \dfrac34.\]
</p>
<p>(2) 作树形图可知, \[\begin{aligned}
        P(Y=0)&= (1-p)^2= \dfrac1{16},\\
        P(Y=1)&= p(1-p)+ (1-p)p= \dfrac38,\\
        P(Y=2)&= p^2= \dfrac9{16},
    \end{aligned}\]
    所求 $Y$ 的分布列为 \[\begin{array}{c|ccc}
        Y & 0 & 1 & 2\\
        \hline
        P(Y) & \dfrac1{16} & \dfrac38 & \dfrac9{16}\phantom{\biggr|}
    \end{array}\]
</p>
<p>(3) 记甲命中的次数为 $Z$, 则 $X= Z+Y$. 注意, $Z$, $Y$ 均为非负整数, 且 \[
        0\leqslant Z\leqslant 1,\quad
        0\leqslant Y\leqslant 2.\]
    作树形图可知, \[\begin{aligned}
        P(X=0)&= P(Z=0)P(Y=0)= \frac12\cdot\dfrac1{16}= \dfrac1{32},\\
        P(X=1)&= P(Z=1)P(Y=0)+ P(Z=0)P(Y=1)\\
            &= \frac12\cdot\dfrac1{16}+ \frac12\cdot\dfrac3{8}
             = \dfrac7{32},\\
        P(X=2)&= P(Z=0)P(Y=2)+ P(Z=1)P(Y=1)\\
            &= \frac12\cdot\dfrac9{16}+ \frac12\cdot\dfrac38
             = \dfrac{15}{32},\\
        P(X=3)&= P(Z=1)P(Y=2)= \frac12\cdot\dfrac9{16}= \dfrac9{32},\\
    \end{aligned}\]
    所求 $X$ 的分布列为 \[\begin{array}{c|cccc}
        X & 0 & 1 & 2 & 3\\
        \hline
        P(X) & \dfrac1{32} & \dfrac7{32} & \dfrac{15}{32} & \dfrac9{32}\phantom{\biggr|}
    \end{array}\]
</p>
</mysolution>

