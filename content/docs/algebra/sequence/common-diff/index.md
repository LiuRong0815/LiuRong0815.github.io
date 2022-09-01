---
# bookCollapseSection: true
title: 等差数列
weight: 2
bookHidden: true
prevPage: /docs/algebra/sequence/sequence-def
prevPageTitle: 数列的定义
nextPage: /docs/algebra/sequence/common-ratio
nextPageTitle: 等比数列
---

# 等差数列

<myexample>
<p>已知两个等差数列 $\{a_n\}$ 和 $\{b_n\}$ 的前 $n$ 项和分别为 $S_n$ 和 $T_n$, 且 $\dfrac{S_n}{T_n}= \dfrac{3n+39}{n+3}$, 计算 $\dfrac{a_3}{b_3}$, $\dfrac{a_n}{b_n}$.
</p>
</myexample>
<mysolution>
    <p>由等差数列求和公式, \[
        S_n= \frac12(a_1+a_n)n,\quad
        T_n= \frac12(b_1+b_n)n,\]
    所以已知等式化为 \[
        \dfrac{S_n}{T_n}= \frac{a_1+a_n}{b_1+b_n}
        = \frac{3n+39}{n+3}.\]
    再利用等差数列的性质, \[
        2a_3= a_1+ a_5,\quad 2b_3= b_1+ b_5,\]
    所以在前式中令 $n= 5$ 可得 \[
        \frac{a_3}{b_3}= \frac{a_1+ a_5}{b_1+ b_5}
        = \frac{3\cdot 5+ 39}{5+ 3}= \frac{27}{4}.\]
</p>
<p>类似地, \[
        2a_n= a_1+ a_{2n-1},\quad 2b_n= b_1+ b_{2n-1},\]
    所以 \[
        \frac{a_n}{b_n}= \frac{a_1+ a_{2n-1}}{b_1+ b_{2n-1}}
        = \frac{3\cdot (2n-1)+ 39}{(2n-1)+ 3}= \frac{3n+18}{n+1}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知等差数列 ${a_n}$, $S_n$ 为其前 $n$ 项和, $a_5= 10$, $S_7=56$.
</p>
<p>(1) 求数列 $\{a_n\}$ 的通项公式;
</p>
<p>(2) 若 $b_n= a_n+(\sqrt3)^{a_n}$, 求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexample>
<mysolution>
    <p>(1) 由等差数列求和公式, \[\begin{gathered}
        S_7=56= \frac12(a_1+a_7)\cdot 7,\\
        a_1+a_7= 16.
    \end{gathered}\]
    设公差为 $d$, 则 \[\left\{\!\!\begin{array}{l}
        a_5= a_1+4d= 10,\\
        a_1+a_7= 2a_1+ 6d= 16,
    \end{array}\right.\]
    解得 $a_1= 2$, $d= 2$, 所求通项公式为 \[
        a_n= a_1+ (n-1)d= 2n,\quad n\in\mathbf{N}^+.\]
</p>
<p>(2) 由 $a_n= 2n$ 知, \[
        b_n= a_n+(\sqrt3)^{a_n}= 2n+ 3^n,\]
    所以分别按等差数列和等比数列求和公式, \[\begin{aligned}
        T_n&= (2\cdot 1+ 3^1)+ (2\cdot 2+ 3^2)+ \cdots + (2n+ 3^n)\\
        &= 2(1+2+\cdots+ n)+ (3^1+ 3^2+\cdots + 3^n)\\
        &= 2\cdot \frac12(1+n)n+ \frac{3(1-3^n)}{1-3}\\
        &= (1+n)n+ \frac32(3^n-1).
    \end{aligned}\]
</p>
</mysolution>

