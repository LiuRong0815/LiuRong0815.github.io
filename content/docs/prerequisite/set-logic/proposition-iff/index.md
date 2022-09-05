---
# bookCollapseSection: true
title: 命题与充要条件
weight: 3
# bookHidden: true
prevPage: ../set-operation
prevPageTitle: 集合的运算
nextPage: ../logical-quantifier
nextPageTitle: 逻辑量词
---

# 命题与充要条件

可以判断真假 (成立与否) 的陈述句称为命题 (proposition). 一些命题描述的是两个条件的因果关系, 这种因果关系也称为条件的充分性或必要性. 

## 命题的真假

<p>判断为真的命题称为<strong>真命题</strong>, 判断为假的命题称为<strong>假命题</strong>. 例如, 下面是三个命题的真假性:
</p>
<p>命题 $P$: $1+2+3+\cdots +10= 55$ (真命题);
</p>
<p>命题 $Q$: 若 $x>1$, 则 $-x<-1$ (真命题);
</p>
<p>命题 $R$: 对所有的 $x\in\mathbf{R}$, $x^2-1>0$ (假命题). 
</p>

<p>如果命题可以写成“若 $p$, 则 $q$”的形式, 则将条件 $p$ 称为前提, 条件 $q$ 称为结论. 有时将这种命题简记为 $p\Rightarrow q$, 并称由条件 $p$ 可得条件 $q$. 上述命题 $Q$ 的前提是 $x>1$, 结论是 $-x<-1$, 且可以改写成 \[
    x>1\Rightarrow -x<-1.\]
命题 $P$ 和命题 $R$ 则不便于改写成“若 $p$, 则 $q$”的形式.
</p>

<myremark>
    <p>有些命题在改写成“若 $p$, 则 $q$”的形式时, 还需额外写出讨论范围. 例如, 命题“三角形中, 大边对大角”, 可以改写成: 在 $\triangle ABC$ 中, 若 $\angle A> \angle B$, 则 $BC> AC$.</p>
</myremark>

<p>在判断命题的真假 (true or false) 时, 对真命题需要证明, 对假命题则只需要举出一个反例. 例如, 由不等式的性质知“若 $x>2$, $y>1$, 则 $x+y>3$”是真命题; “若 $x>2$, $y>1$, 则 $x-y>1$”是假命题, 因为可取 $x=3$, $y=5$ 满足前提但不满足结论. 后一个假命题也表明, <strong>同向不等式不能相减</strong>.</p>

<myexample>
    <p>(1) 已知 $p(x)\colon x^2 +2x-m>0$ 是与实数 $x$ 有关的命题, 若 $p(1)$ 是假命题, $p(2)$ 是真命题, 求 $m$ 的取值范围;
    </p>
    <p>(2) 已知命题“关于 $x$ 的方程 $x^2 +x+a=0$ 有实根”为真命题, 求 $a$ 的取值范围.
    </p>
</myexample>

<mysolution>
    <p>(1) 由题意, $1+2-m\leqslant 0$ 且 $4+4-m>0$, 解得 $m\in[3,8)$.
    </p>
    <p>(2) 判别式 $\Delta= 1-4a\geqslant 0$, 则 $a\in\Bigl(-\infty,-\dfrac14\Bigr]$.
    </p>
</mysolution>

<myexercise>
    <p>判断命题“若 $a>b$, $ab\neq 0$, 则 $\dfrac1a< \dfrac1b$”的真假.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>举反例 (如 $a=1$, $b=-1$) 可知该命题为假命题. 也可利用反比例函数 $y=\dfrac1x$ 分段递减的性质.</p>
</details>

## 充分条件、必要条件

<p>若由条件 $p$ 能推出条件 $q$, 则称 $p$ 为 $q$ 的充分条件 (sufficient condition), $q$ 为 $p$ 的必要条件 (necessary condition). (可简记为“充分”即是“前提”, “必要”即是“结论”.) 若条件 $p$, $q$ 能互相推出, 则称 $p$ 为 $q$ 的充要条件 (necessary and sufficient condition), 也称 $p$, $q$ 等价, 此时 $q$ 也为 $p$ 的充要条件.
</p>

<p>例如, 设 $p\colon x>2$, $q\colon x>1$, 则 $p\Rightarrow q$ 但 $q\nRightarrow p$, 所以 $p$ 是 $q$ 的充分不必要条件, 而 $q$ 是 $p$ 的必要不充分条件. 再设 $r\colon 2>x>1$, 则可知 \[
    p\nRightarrow r,\ r\nRightarrow p,\quad 
    q\nRightarrow r,\ r\Rightarrow q,\]
即 $p$ 为 $r$ 的既不充分也不必要条件, 而 $r$ 是 $q$ 的充分不必要条件. 判断多个条件之间的充分性或必要性时, 可以列出推理关系, 帮助理清思路.
</p>

<p>判断两个条件 $p$, $q$ 相互的充分性或必要性时, 可以先确定两个条件对应的集合, 再由集合的包含关系判断充分性或必要性. 若条件 $p$, $q$ 描述的对象 (记为 $x$) 分别组成集合 $A$, $B$, 且不妨设 $A\subseteq B$, 则由 $x\in A$ 可得 $x\in B$, 即满足条件 $p$ 的所有对象均满足条件 $q$, 因此 $p\Rightarrow q$, 此时 $p$ 是 $q$ 的充分条件, $q$ 是 $p$ 的必要条件. 一个不严谨的记法是: <strong>小集合是充分的, 大集合是必要的</strong>.
</p>

![充分、必要条件推理集合示意图](/figs/2022/2022-08/2022-0825-1930.svg)

<p>上例中 $p$ 对应区间 $A=(2,+\infty)$, $q$ 对应区间 $B=(1,+\infty)$, 而 $A\subseteq B$ (参考数轴表示), 所以 $p$ 是 $q$ 的充分不必要条件.
</p>

<myremark>
    <p>(1) 有时条件 $p$, $q$ 对应的集合 $A$, $B$ 没有包含关系, 表明这两个条件之间并无充分性或必要性. 例如, $p\colon x^2-1=0$ 对应集合 $\{-1,1\}$, $q\colon x^2-x=0$ 对应集合 $\{0,1\}$, 由于这两个集合没有包含关系, 所以 $p$ 为 $q$ 的既不充分也不必要条件.
    </p>
    <p>(2) 并非所有的充分性、必要性都可以直接用集合的包含关系来判断, 有时需要利用推理或计算.</p>
</myremark>

<myexample>
    <p>已知 $p$, $q$ 都是 $r$ 的必要条件, $s$ 是 $r$ 的充分条件, $q$ 是 $s$ 的充分条件, 分别判断 $r$ 与 $q$, $p$ 与 $q$ 的充分性和必要性.
    </p>
</myexample>

<mysolution>
    <p>作出推理关系图, 可知 $r$ 是 $q$ 的充要条件, $p$ 是 $q$ 的必要条件.
    </p>
    <img alt="用推理关系图判断充分性、必要性" src="/figs/2022/2022-08/2022-0826-1940.svg"></img>
</mysolution>

<myexample>
    <p>判断下列各组条件的充分性和必要性:
    </p>
    <p>(1) $p_1\colon x=-1$, $q_1\colon x^2-5x-6=0$;
    </p>
    <p>(2) $p_2\colon x$, $y$ 为无理数, $q_2\colon x+y$ 为无理数;
    </p>
    <p>(3) $p_3\colon a>b$, $q_3\colon a|a|>b|b|$.
    </p>
</myexample>

<mysolution>
    <p>(1) $x^2-5x-6=0$ 的解集为 $\{-1,6\}$, 故 $p_1$ 是 $q_1$ 的充分不必要条件.
    </p>
    <p>(2) 若 $x=\sqrt2$, $y=-\sqrt2$, 则 $x+y=0$ 为有理数; 若 $x+y=\sqrt2$ 为无理数, 则可能 $x=\sqrt2$ 为无理数, $y=0$ 非无理数. 由这两个反例知,“$x$, $y$ 为无理数”与“$x+y$ 为无理数”没有必然的因果关系, 所以 $p_2$ 是 $q_2$ 的既不充分也不必要条件.
    </p>
    <p>(3) 作函数 \[
        y= x|x|= \begin{cases}
            x^2,& x\geqslant 0,\\
            -x^2,& x< 0 \end{cases}\]
    的图象知, 函数是单调递增的, 所以 $a>b\Leftrightarrow a|a|>b|b|$, 即 $p_3$ 是 $q_3$ 的充要条件.</p>
</mysolution>

<myexample>
    <p>已知 $p\colon x^2-8x-20\leqslant 0$, $q\colon 1-m\leqslant x\leqslant 1+m$.
    </p>
    <p>(1) 当 $m=1$ 时, 判断 $p$ 与 $q$ 充分性和必要性;
    </p>
    <p>(2) 若 $p$ 是 $q$ 的必要不充分条件, 求实数 $m$ 的取值范围.
    </p>
</myexample>

<mysolution>
    <p>解不等式得, $p\colon -2\leqslant x\leqslant 10$.
    </p>
    <p>(1) 当 $m=1$ 时, $q\colon 0\leqslant x\leqslant 2$, 则 $p$ 是 $q$ 的必要不充分条件.
    </p>
    <p>(2) 由题意, \[
        1-m\leqslant -2< 10\leqslant 1+m,\]
    且等号不能同时成立, 解得 $m\in[9,+\infty)$.
    </p>
</mysolution>

<myexercise>
    <p>判断下列各组条件的充分性和必要性:
    </p>
    <p>(1) $p_1\colon x^3>0$, $q_1\colon x^2 \geqslant -x$;
    </p>
    <p>(2) $p_2\colon \sqrt M>\sqrt N$, $q_2\colon M>N$;
    </p>
    <p>(3) $p_3\colon |x|\geqslant 1$, $q_3\colon x>2$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $p_1\colon x\geqslant 0$, $q_1\colon x\leqslant -1$ 或 $x\geqslant 0$, 则 $p_1$ 是 $q_1$ 的充分不必要条件.</p>
    <p>(2) $p_2$ 等价于 $M>N\geqslant 0$, 为 $q_2$ 的充分不必要条件. (二次根式应注意被开方数一定大于或等于 $0$.)</p>
    <p>(3) $p_3$ 等价于 $x\leqslant -1$ 或 $x\geqslant 1$, 为 $q_2$ 的既不充分也不必要条件.</p>
</details>

<myexercise>
    <p>条件“$a=-1$”是“函数 $y=ax^2+2x-1$ 的图象与 $x$ 轴只有一个交点”的什么条件?</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>对函数 $y=ax^2+2x-1$, 若 $a=0$, 则其为一次函数 $y= 2x-1$, 图象与 $x$ 轴只有一个交点; 若 $a\neq 0$, 则其为二次函数, 只需 $\Delta= 2^2-4a\cdot(-1)=0$, 解得 $a=-1$. 反之, 容易验证当 $a=0$ 或 $-1$ 时, 函数 $y=ax^2+2x-1$ 的图象与 $x$ 轴只有一个交点. 
    </p>
    <p>所以条件“$a=-1$”是“函数 $y=ax^2+2x-1$ 的图象与 $x$ 轴只有一个交点”的充分不必要条件. (形如 $y= Ax^2+Bx+C$ 的函数, <strong>必须</strong>先考虑 $A$ 是否为零, 即要先确定该函数的次数.)</p>
</details>


## 原命题、逆命题、否命题、逆否命题

<p>形如“若 $p$, 则 $q$”的命题可以写出对应的逆命题、否命题和逆否命题. 四种命题的形式如下:
</p>

<p>原命题: 若 $p$, 则 $q$;&emsp; &emsp; 
逆命题: 若 $q$, 则 $p$;
</p>

<p>否命题: 若 $\neg p$, 则 $\neg q$;&emsp; &emsp; 
逆否命题: 若 $\neg q$, 则 $\neg p$.
</p>

<p>上面的 $\neg p$ 指的是否定条件 $p$, 读作“非 $p$”, 例如, 否定 $x=1$ 得到 $x\neq 1$. 但是, 否定一个条件并非简单地将判断词改成其反义词: 否定 $x> 1$ 并不得到 $x< 1$, 而是得到 $x\leqslant 1$. 否定条件 $p$, 其实是求出 $p$ 对应集合的补集, 此时的全集视当前讨论的对象而定. 因为 $x> 1$ 对应区间 $(1,+\infty)$, 结合数轴知, 该区间的补集为 $(-\infty,1]$, 所以否定 $x> 1$ 得到 $x\leqslant 1$.
</p>

<p><strong>原命题与否命题的真假没有必然联系</strong>. 例如, “若 $x=1$, 则 $x^2=1$”的否命题为“若 $x\neq 1$, 则 $x^2\neq 1$”, 前者真, 后者假; 而“若 $x=1$, 则 $x^3=1$”的否命题为“若 $x\neq 1$, 则 $x^3\neq 1$”, 两者都是真命题. 
</p>

<p>同样也有例子说明原命题和逆命题的真假没有必然联系. 但是<strong>原命题和其逆否命题却是同真假的</strong>, 利用维恩图很容易看出这一点. 若原命题“若 $p$, 则 $q$”为真, 设条件 $p$, $q$ 分别对应集合 $A$, $B$, 当前讨论的对象范围为全集 $U$, 则由 $p\Rightarrow q$ 知 $A\subseteq B$, 从而 $\complement_U B\subseteq \complement_U A$,所以 $\neg q\Rightarrow \neg p$, 即逆否命题“若 $\neg q$, 则 $\neg p$”为真. 同理可说明, 若原命题“若 $p$, 则 $q$”为假, 则逆否命题“若 $\neg q$, 则 $\neg p$”也为假.
</p>

![原命题与逆否命题同真假集合示意图](/figs/2022/2022-08/2022-0825-2030.svg)

<myexample>
    <p>判断命题“若 $ab=0$, 则 $b=0$”和其否命题的真假.
    </p>
</myexample>

<mysolution>
    <p>因为 $ab=0$ 等价于 $a=0$ 或 $b=0$, 是 $b=0$ 的必要条件, 所以原命题为假.
    </p>
    <p>否命题: 若 $ab\neq 0$, 则 $b\neq 0$. 因为 $ab\neq0$ 等价于 $a\neq 0$ 且 $b\neq 0$, 是 $b=0$ 的充分条件, 所以原命题为真.
    </p>
</mysolution>
