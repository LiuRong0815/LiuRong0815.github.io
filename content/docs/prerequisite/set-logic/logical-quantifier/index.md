---
# bookCollapseSection: true
title: 逻辑量词
weight: 4
# bookHidden: true
prevPage: ../proposition-iff
prevPageTitle: 命题与充要条件
# nextPage: ../../inequality
# nextPageTitle: 不等式
---

# 逻辑量词

<p>除了有能写成“若 $p$, 则 $q$”形式的命题, 还有能写成“对所有 $x\in M$, $p(x)$ 成立”或“存在 $x\in M$, $p(x)$ 成立”形式的命题, 其中 $p(x)$ 是与 $x$ 有关的条件. 后一种形式命题中的“所有”是全称量词, “存在”是存在量词, 两者统称为逻辑量词, 分别协助限定了条件 $p(x)$ 成立的范围. 
</p>
<p>为了简化叙述, 将全称量词“所有”(for all) 简记为符号“$\forall$”, 存在量词“存在”(exists) 简记为符号“$\exists$”. 前面的两种命题可以进一步简化为 \[
    \forall\, x\in M, p(x);\quad
    \exists\, x\in M, p(x).\]
从逻辑量词的形状可以看出, “$\forall$”可由字母 A 上下翻转得到, “$\exists$”可由字母 E 左右翻转得到.
</p>
<myremark>
    <p>全称量词“所有”有时也写成“任意”“每一个”“任给”等, 存在量词“存在”有时也写成“有些”“至少有一个”等.</p>
</myremark>

<myexample>
    <p>若命题“$\exists\, x_0\in \mathbf{R}$, $x_0^2+ 2ax_0+2-a=0$”是真命题, 求实数 $a$ 的取值范围.
    </p>
</myexample>

<mysolution>
    <p>已知表明, 二次方程 $x^2+ 2ax+2-a=0$ 有实根 $x_0$, 则 \[
        \Delta= (2a)^2-4(2-a)\geqslant 0,\]
    解得 $a\in(-\infty,-2]\cup[1,+\infty)$.
    </p>
</mysolution>

<myexample>
    <p>已知下列命题是真命题, 求对应的实数 $m$ 的取值范围:
    </p>
    <p>(1) $\forall\, x\in [0,1]$, $x^2+2x>m$;
    </p>
    <p>(2) $\exists\, x\in [0,1]$, $x^2+2x>m$.
    </p>
</myexample>

<mysolution>
    <p>由抛物线 $y= x^2+2x$ 开口向上且对称轴为 $x=-1$ 知, 二次函数 $y= x^2+2x$ 在 $x\in [0,1]$ 时的最大值为 $1^2+ 2\cdot 1= 3$, 最小值为 $0^2+2\cdot 0= 0$.
    </p>
    <p>(1) 此时所有 $x^2+2x$ 均大于 $m$, 故只须最小值大于 $m$, 即 $0>m$. 所以 $m\in(-\infty,0)$.
    </p>
    <p>(1) 此时某个 $x^2+2x$ 大于 $m$, 故只须最大值大于 $m$, 即 $4>m$. 所以 $m\in(-\infty,4)$.
    </p>
</mysolution>

<myremark>
    <p>上述解法可以推广, 即与函数有关的恒成立或存在性问题, 一般可以转化为求函数的取值范围问题.</p>
</myremark>

## 含逻辑量词命题的否定

<p>容易理解, 形如“$\forall\, x\in M$, $p(x)$”的命题的否定为 \[
    \exists\, x\in M, \neg p(x),\] 
而形如“$\exists\, x\in M$, $p(x)$”的命题的否定为 \[
    \forall\, x\in M, \neg p(x).\]
例如, 命题“$\forall\, x>1$, $x^2>1$”的否定为“$\exists\, x>1$, $x^2\leqslant 1$”; 命题“$\exists\, x\in \mathbf{R}$, $x^2 +x+1=0$”的否定为“$\forall\, x\in \mathbf{R}$, $x^2 +x+1\neq 0$”.
</p>
<myremark>
    <p>否命题与含逻辑量词命题的否定不一样, 两者是分别对不同形式的命题进行变化.</p>
</myremark>

<p>含逻辑量词命题与其否定的真假恰好相反, 有时判断含逻辑量词命题的真假可以转化为判断其否定的真假. 判断含“$\forall$”或“$\exists$”的命题的真假时, 前者需要检验所考虑范围中的所有变量, 后者只需尝试寻找一个合题意的变量.
</p>

<myexample>
    <p>判断下列命题的真假, 并写出其否定:
    </p>
    <p>(1) $\forall\, x\in \mathbf{R}$, $x^2-2x+2>0$;
    </p>
    <p>(2) 存在一个无理数, 它的平方是有理数;
    </p>
    <p>(3) $\exists\, x>0$, $x+ \dfrac1x< 2$.
    </p>
</myexample>

<mysolution>
    <p>(1) 配方可得, \[
        x^2-2x+2= (x-1)^2+1>0,\]
    所以原命题正确. 其否定为 \[
        \exists\, x\in \mathbf{R}, x^2-2x+2\leqslant 0.\]
    </p>
    <p>(2) 无理数 $\sqrt2$ 的平方为 $1$, 是有理数, 所以原命题正确. 其否定为: 所有的无理数的平方都是无理数.
    </p>
    <p>(3) 当 $x>0$ 时, $x+ \dfrac1x< 2$ 等价于 \[
        x^2+1< 2x\Leftrightarrow (x-1)^2< 0,\]
    显然不成立, 所以原命题错误. 其否定为 \[
        \forall\, x>0, x+ \dfrac1x\geqslant 2.\]
    </p>
</mysolution>

<myexercise>
    <p>若命题“$\exists\,x\in \mathbf{R}$, $x^2 +2x+m\leqslant 0$”是假命题, 求实数 $m$ 的取值范围.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>命题“$\forall\,x\in \mathbf{R}$, $x^2 +2x+m> 0$”是真命题, 则 $\Delta=2^2-4m< 0$, $m\in(1,+\infty)$.
    </p>
</details>

## 逻辑连接词

<p>有些条件是由两个条件用“且”“或”连接而成的. 例如, 条件 $p\colon x< 0$ 或 $x>1$ 就是由 $x< 0$ 与 $x>1$ 用“或”连接而成的. “且”“或”以及表示否定的“非”均为逻辑联结词, 且有对应的符号: “且” 的符号为 $\wedge$, “或”的符号为 $\vee$, “非”的符号为 $\neg$. 这两个符号可以类比求交集的符号“$\cap$”和求并集的符号“$\cup$”来记忆.
</p>
<p>考虑 $p$ 对应集合的补集知, $\neg p\colon 0\leqslant x\leqslant 1$. 用<a href="/docs/prerequisite/set-logic/set-operation/#德摩根律">德摩根律</a>可以解释否定此类条件的更一般的规律. 设条件 $s\colon x< 0$, 条件 $t\colon x>1$, 则条件 $p$ 可以写成“$s\vee t$”. 此时, 将条件 $s$, $t$ 分别视为其对应的集合 $S$, $T$, 由德摩根律可知, \[\begin{aligned}
    \neg p
    &= \neg(s\vee t)= \complement (S\cup T)\\
    &= \complement\, S\cap \complement\, T
     = \neg s\wedge \neg t.
\end{aligned}\]
上面省略了当前讨论范围对应的全集. 同样地, \[
    \neg(s\wedge t)= \neg s\vee \neg t.\]
由此可知, 否定用“且”“或”连接的两个条件时, 分别否定每个条件, 再将“且”与“或”互换即可. 例如, 对前面的条件 $p\colon x< 0$ 或 $x>1$, 有 \[
    \neg p\colon \neg(x< 0)\wedge \neg(x>1),\]
进一步化简可知, $\neg p\colon 0\leqslant x\leqslant 1$.
</p>
<p>进而可知, 形如“$\forall\, x\in M$, $p(x)\wedge q(x)$”的命题的否定为 \[
    \exists\, x\in M, \neg p(x)\vee \neg q(x),\] 
而形如“$\exists\, x\in M$, $p(x)\vee q(x)$”的命题的否定为 \[
    \forall\, x\in M, \neg p(x)\wedge \neg q(x).\]
可以类似地写出其他含逻辑量词和逻辑连接词的命题的否定形式.
</p>
