---
# bookCollapseSection: true
title: 集合的运算
weight: 2
# bookHidden: true
prevPage: ../set-def
prevPageTitle: 集合的定义
nextPage: ../proposition-iff
nextPageTitle: 命题与充要条件
---

# 集合的运算

集合的基本运算为求交集、并集或补集, 这三种运算可以用来生成新的集合, 也可以用于进一步简化数学语言的叙述.

## 集合的交、并、补

<p>
两个集合 $A$, $B$ 的交集是由它们的公共元素组成的集合, 记为 $A\cap B$, 读作“$A$ 交 $B$”. 由定义, \[
    A\cap B= \{x\mid x\in A\ \text{且}\ x\in B\},\]
而且显然有 \[
    A\cap B\subseteq A,\quad A\cap B\subseteq B,\]
即取交集后的范围通常会小一些. 两个集合的交集可以用维恩图表示如下, 其中两圆围成的区域对应集合 $A$, $B$, 阴影部分为 $A\cap B$.
</p>
<img alt="交集的维恩图" src="/figs/2022/2022-08/2022-0821-1420.svg"></img>

<p>
两个集合 $A$, $B$ 的并集是由它们的所有元素组成的集合, 记为 $A\cup B$, 读作“$A$ 并 $B$”. 由定义, \[
    A\cup B= \{x\mid x\in A\ \text{或}\ x\in B\},\]
而且显然有 \[
    A\subseteq A\cup B,\quad B\subseteq A\cup B,\]
即取并集后的范围通常会大一些. 两个集合的并集用维恩图可以表示如下, 其中阴影部分为 $A\cup B$.
</p>
<img alt="并集的维恩图" src="/figs/2022/2022-08/2022-0821-1430.svg"></img>

<myremark>
    <p>(1) 注意分辨交集符号 $\cap$ 与并集符号 $\cup$;</p>
    <p>(2) 数学中的“或”与生活中的“或”的意义不完全一样, “$x\in A$ 或 $x\in B$”表示两者之一成立即可, 也可以同时成立.</p>
</myremark>

<p>
通常的数学问题都是在某个范围内考虑的, 例如, 求解平面几何问题只在考虑某个确定的平面, 而不考虑平面所在的空间; 求方程的整数解只考虑整数集 $\mathbf{Z}$, 而不考虑有理数集 $\mathbf{Q}$ 或实数集 $\mathbf{R}$. 这种事先规定的讨论问题的范围构成的集合, 称为全集. 设全集为 $U$, 则集合 $A$ 在 $U$ 中的补集由所有属于 $U$ 但不属于 $A$ 的元素构成, 记为 $\complement_U A$, 读作“$A$ 在 $U$ 中的补集”或更简洁的“$A$ 补”. 由定义, \[
    \complement_U A= \{x\mid x\in U\ \text{且}\ x\notin A\},\]
用维恩图可以表示如下, 其中矩形、圆围成的区域分别对应集合 $U$, $A$, 阴影部分为 $\complement_U A$.
</p>
<img alt="补集的维恩图" src="/figs/2022/2022-08/2022-0821-1530.svg"></img>

<p>
例如, 设全集为 $U=\{1,2,3,4,5\}$, $A=\{1,2,5\}$, $B=\{2,3\}$, 则
\[A\cap B=\{2\},\quad A\cup B=\{1,2,3,5\},\quad 
  \complement_U A=\{3,4\}.\]
本例对应的维恩图如下所示.
</p>
<img alt="交、并、补的维恩图" src="/figs/2022/2022-08/2022-0821-1540.svg"></img>


<myexample>
    <p>(1) 若集合 $A=\{1,2,3\}$, $B=\{1,3,4\}$, 求 $A\cap B$ 的子集个数;</p>
    <p>(2) 设集合 $A=\{x\mid 0.5< x< 2\}$, $B=\{x\mid x^2\leqslant 1\}$, 求 $A\cup B$.</p>
</myexample>

<mysolution>
    <p>(1) $A\cap B= \{1,3\}$, 子集共 $2^2=4$ 个.</p>
    <p>(2) $B=\{x\mid -1\leqslant x\leqslant 1\}$, $A\cup B=\{x\mid -1\leqslant x< 2\}$.</p>
</mysolution>

<myremark>
    <p>二次不等式的解法, 参看初中代数提要的<a href="../../ms-function/quadratic-function-inequality#二次不等式的解法">二次函数与二次不等式</a>.</p>
</myremark>

<myexample>
    <p> 已知集合 $A=\{x\mid x^2-px+15=0\}$, $B=\{x\mid x^2-ax-b=0\}$, $A\cup B=\{2,3,5\}$, $A\cap B=\{3\}$, 求 $p$, $a$, $b$ 的值.</p>
</myexample>

<mysolution>
    <p>由 $3\in A$ 知 $p=8$, $A=\{3,5\}$, 所以 $B=\{2,3\}$. 由韦达定理, $a=5$, $-b=6$ 即 $b=-6$.</p>
</mysolution>

<myexercise>
    <p>设集合 $A=\{x\mid y=\sqrt{x-1}\}$, $B=\{y\mid y=x^2 +2\}$, 求 $A\cap B$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>$A=\{x\mid x\geqslant 1\}$, $B=\{x\mid x\geqslant 2\}$, 则 $A\cap B=\{x\mid x\geqslant 2\}$. (注意, $A$ 描述的是根号下 $x$ 的取值范围, $B$ 描述的是二次函数的取值范围.)</p>
</details>

## 区间

<p>
为了简化形如 $\{x\mid -1< x< 1\}$ 的集合的表示, 可以将其改写为区间形式. 区间表示的是一段连续的实数范围, 共九种形式, 分为有限区间和无限区间.
</p>

<p>
有限区间共四种形式. 以下设 $a< b$, 则
</p>

- 集合 $\\{x\mid a< x< b\\}$ 简记为开区间 $(a,b)$;
- 集合 $\\{x\mid a\leqslant x\leqslant b\\}$ 简记为闭区间 $[a,b]$;
- 集合 $\\{x\mid a< x\leqslant b\\}$ 简记为左开右闭区间 $(a,b]$;
- 集合 $\\{x\mid a\leqslant x< b\\}$ 简记为左闭右开区间 $[a,b)$.

<p>
上面的四种表示中的 $a$, $b$ 均称为区间的端点. 结合数轴很容易理解这些表示, 对应取值范围的端点就是区间的端点, 再根据范围是否包含端点选取小括号或中括号.
</p>

<myremark>
    <p>注意区间 $(-1,1)$、点的坐标 $(-1,1)$ 与集合 $\{-1,1\}$ 的区别. 对于记号 $(-1,1)$, 通常需要指明它到底是区间还是坐标. 区间 $(-1,1)$ 表示所有大于 $-1$ 且小于 $1$ 的实数, 而集合 ${-1,1}$ 中仅含两个实数: $1$ 与 $-1$.</p>
</myremark>

<p>
无限区间共五种形式. 为了写出无限区间的端点, 可以假想数轴的“尽头”对应两个数, 分别记为 $-\infty$ 和 $+\infty$, 读作“负无穷大”和“正无穷大”. 以下设 $a\in\mathbf{R}$, 则
</p>

- 集合 $\\{x\mid x< a\\}$ 简记为开区间 $(-\infty,a)$;
- 集合 $\\{x\mid x\leqslant a\\}$ 简记为左开右闭区间 $(-\infty,a]$;
- 集合 $\\{x\mid a<x\\}$ 简记为开区间 $(a,+\infty)$;
- 集合 $\\{x\mid a\leqslant x\\}$ 简记为左闭右开区间 $[a,+\infty)$;
- 实数集 $\mathbf{R}$ 也可以写成开区间 $(-\infty,+\infty)$.

<p>
上面的前四种表示中的 $a$ 也称为区间的端点. 结合数轴也容易理解这些表示, 例如, 开区间 $(-\infty,a)$ 可以借助数轴表示为下图.
</p>
<img alt="左无穷开区间的数轴表示" src="/figs/2022/2022-08/2022-0821-1620.svg"></img>


<myexample>
    <p>设集合 $A=\{-2,0,2\}$, 分别在下列条件下求 $A\cap B$:</p>
    <p>(1) $B=\{x\mid x^2-x-2=0\}$;</p>
    <p>(2) $B=\{x\mid x^2-x-2\leqslant 0\}$;</p>
    <p>(2) $B=\{x\mid x^2-x-2> 0\}$.</p>
</myexample>

<mysolution>
    <p>(1) $B=\{-1,2\}$, $A\cap B=\{2\}$.</p>
    <p>(2) $B=[-1,2]$, $A\cap B=\{0,2\}$.</p>
    <p>(3) $B=(-\infty,-1)\cup(2,+\infty)$, $A\cap B=\{-2\}$.</p>
</mysolution>

<myexample>
    <p>设全集为 $\mathbf{R}$, 集合 $A=\{u\mid u^2 -9< 0\}$, $B=\{x\mid -1< x\leqslant 5\}$, 求 $A\cap (\complement_{\mathbf{R}} B)$.</p>
</myexample>

<mysolution>
    <p>因为 \[\begin{gathered}
        A=\{u\mid -3< u< 3\}=(-3,3),\\
        \complement_{\mathbf{R}} B=(-\infty,-1]\cup (5,+\infty),
    \end{gathered}\]
    所以 $A\cap (\complement_{\mathbf{R}} B)= (-3,-1]$.</p>
</mysolution>

<myexercise>
    <p>(1) 设集合 $A=\{x\mid x^2-2x< 0\}$, $B=\{x\mid 1\leqslant x\leqslant 4\}$, 求 $A\cap B$;</p>
    <p>(2) 设集合 $A=\{-1,a\}$, $B=\{2a,b\}$. 若 $A\cap B=\{1\}$, 求 $A\cup B$;</p>
    <p>(3) 设集合 $A=\{-1,a\}$, $B=\{2a,a^2\}$. 若 $A\cap B=\{-1\}$, 求 $A\cup B$.</p>
    
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $A=(0,2)$, $A\cap B=[1,2)$.</p>
    <p>(2) \(1\in A\) 且 \(1\in B\), 则 \(a=1\), $A=\{-1,1\}$, $B=\{2,b\}$, 所以 $b=1$, $B=\{2,1\}$, 故 $A\cup B=\{-1,1,2\}$.</p>
    <p>(3) $-1\in B\Rightarrow 2a=-1$, $a=-\dfrac12$, 故 $A\cup B=\Big\{-1,-\dfrac12,\dfrac14\Big\}$.</p>
</details>

## 交、并、补的性质和运算律

<p>
这里介绍与交、并、补有关的两个性质和两个运算律.
</p>

<p>设集合 $A$, $B$ 满足 $A\cap B= A$, 结合交集运算的维恩图可知, $A$ 的范围要小一些, 即 $A\subseteq B$. 而若 $A\subseteq B$, 则仍由维恩图可知, $A\cap B= A$. 由此可得, \[
    A\cap B= A\Leftrightarrow A\subseteq B.\]
借助于并集运算的维恩图表示, 还可以得到 \[
    A\cup B= A\Leftrightarrow B\subseteq A.\]
</p>

<p id="德摩根律">
此外, 设全集为 $U$, 对集合 $A$, $B$, 由维恩图可得, \[\begin{aligned}
    \complement_U (A\cap B)&= \complement_U A\cup \complement_U B,\\
    \complement_U (A\cup B)&= \complement_U A\cap \complement_U B.
\end{aligned}\]
这两个运算律称为德摩根 (De Morgan) 律. 从上面两个式子可以看出, 取补集的效果类似于取相反数: 在去掉括号时, 连接 $A$, $B$ 的符号发生改变. 德摩根律的正确性可以参看下图. 图中全集 $U$ 被分割成 $4$ 个互不相交的集合, 分别记为 $S_1$, $S_2$, $S_3$, $S_4$, 则 \[\begin{gathered}
    A\cap B= S_2,\quad \complement_U (A\cap B)= S_1\cup S_3\cup S_4,\\
    \complement_U A= S_3\cup S_4,\quad \complement_U B= S_1\cup S_4,
\end{gathered}\]
由此得到德摩根律的第一式. 可类似地得到第二式.
</p>
<img alt="交、并、补的维恩图" src="/figs/2022/2022-08/2022-0824-1940.svg"></img>

<myexample>
    <p>设集合 $A=\{x\mid 1< x< 3\}$, $B=\{x\mid 2m< x< 1-m\}$, 分别在下列条件下求实数 $m$ 的取值范围:</p>
    <p>(1) $A\cup B=B$;&emsp; (2) $A\cap B=\varnothing$.</p>
</myexample>

<mysolution>
    <p>(1) 由题意, $A\subseteq B$, 表明 \[
        2m\leqslant 1< 3\leqslant 1-m,\]
    解得 $m\in(-\infty,-2]$.</p>
    <p>(2) 若 $B=\varnothing$, 则 \[
        2m\geqslant 1-m,\quad m\geqslant \frac13.\]
    若 $B\neq\varnothing$, 则 \[
        2m< 1-m\leqslant 1\quad \text{或}\quad 3\leqslant 2m< 1-m,\]
    解得 \[
        0\leqslant m< \dfrac13\quad \text{或}\quad m\in\varnothing.\]</p>
    <p>综上知, $m\in[0,+\infty)$.</p>
</mysolution>

<myremark>
    <p>解此例时, 结合数轴表示各集合可以更容易列出各不等式.</p>
</myremark>

<myexercise>
    <p>设集合 $A=\{1,2,3\}$, $B=\{1,x\}$, 若 $A\cup B=A$, 求实数 $x$ 的值;</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>\(B\subseteq A\), 则 \(x=2\) 或 \(3\).</p>
</details>
