---
# bookCollapseSection: true
title: 不等式的性质
weight: 1
# bookHidden: true
prevPage: /docs/prerequisite/inequality
prevPageTitle: 不等式
nextPage: /docs/prerequisite/inequality/abs-quadratic-inequality
nextPageTitle: 绝对值不等式与二次不等式
---

# 不等式的性质

不等式的性质与等式的性质既有相似之处, 又有一些区别, 两者可以类比记忆. 不等式的性质是解不等式和证明不等式的基础. 

<p>这里首先回顾等式的几个性质:
</p>
<p>(1) 若 $a=b$, $b=c$, 则 \[
    b=a,\quad a=c.\]
一般称前者为“反身性”, 后者为“传递性”.
</p>
<p>(2) 若 $a=b$, $c=d$, 则 \[
    a\pm c= b\pm d,\quad ac=bd.\]
若还有 $c=d\neq 0$, 则 $\dfrac{a}c= \dfrac{b}d$. 这是等式的四则运算性质.
</p>

## 不等式的定义

<p>用不等号连接两个代数式就得到不等式, 如 $a>b$, $x^2\leqslant x+1$ 等. 不等式主要用来表示两个式子的大小关系, 用到的不等号有 \[
    >,\quad <,\quad \geqslant,\quad \leqslant,\quad \neq.\]
“$\geqslant$”表示“大于或者等于”, “$\leqslant$”表示“小于或者等于”, 例如, “$5\geqslant 3$”表示“$5>3$ 或者 $5=3$”. 像这种用逻辑连接词“或者”连接的两个命题, 只须其中一个为真, 整个命题即为真. 所以 “$5\geqslant 3$” 是真命题.
</p>
<p>有时也用不等号连接多个式子, 形成更复杂的不等式, 例如, $a< 1< b$, 表示“$a< 1$ 且 $1< b$”. 像这种用逻辑连接词“且”连接的两个命题, 只有当两个命题同时为真时, 整个命题才为真. 应该注意, 连接多个式子形成不等式时, 不等号应该是同方向的. 例如, 可以写 $1< 2\leqslant 3$, 但是一般不写 $1< 3 \geqslant 2$.
</p>
<p>数轴上的点表示的数从左至右逐渐增大, 而不等式“$x_1< x_2$”的几何意义是数轴上点 $x_1$ 在点 $x_2$ 的左侧, 结合两个实数作差的规定可知 \[
    a>b\Leftrightarrow a-b>0,\quad a< b\Leftrightarrow a-b< 0.\]
这两个等价关系是所有不等式性质的基础.
</p>
<p>不等式与实数的运算密切相关, 所以一些与 $0$ 有关的大小关系也可以参照实数的运算来理解. 例如, 不等式 $ab>0$ 和 $\dfrac{a}b$ 均等价于 $a$, $b$ 同号, 而 $abc>0$ 可以理解为 $a$, $b$, $c$ 全为正数或两负一正. 此外, \[
    a>0, b> 0 \Leftrightarrow \left\{\!\!\begin{array}{l}
        a+b>0,\\[6pt]
        ab>0,
    \end{array}\right.\]
</p>

<myexample>
    <p>设 $x+y+z=0$, 分别在下列条件下证明: \[
        \dfrac1x+\dfrac1y+\dfrac1z< 0.\]
    </p>
    <p>(1) $x>0$, $y,z< 0$;
    </p>
    <p>(2) $xyz>0$.</p>
</myexample>
<myproof>
    <p>(1) 由已知, $x+y= -z$, 所以 \[
        \frac1x+ \frac1y= \frac{x+y}{xy}= \frac{-z}{xy}< 0,\]
    而 $\dfrac1z< 0$, 所以 $\dfrac1x+\dfrac1y+\dfrac1z< 0$.
    </p>
    <p>(2) 由 $xyz>0$ 知, $x,y,z$ 均为正数或一正两负, 结合 $x+y+z=0$ 知, $x,y,z$ 一正两负. 不妨设 $x>0$, $y,z< 0$, 后续过程同 (1).</p>
</myproof>

<myremark>
    <p>(1) 由已知条件大致确定未知数的正负号, 再由求证结论中 $x$, $y$, $z$ 的对称性 (地位均等) 假设三者的正负号, 可以简化推理.
    </p>
    <p>(2) 当 $xyz>0$ 时, 也可以通过直接计算证明原不等式: 因为 $x+y= -z$, 所以 \[\begin{aligned}
        \frac1x+ \frac1y+ \frac1z
        &= \frac{x+y}{xy}+ \frac1z
         = \frac{-z}{xy}+ \frac1z\\
        &= \frac{xy-z^2}{xyz}
         = \frac{xy-(x+y)^2}{xyz}\\
        &= -\frac{x^2-xy+y^2}{xyz}.
    \end{aligned}\]
    由配方可知, \[
        x^2-xy+y^2= \Bigl(x-\frac12 y\Bigr)^2+ \frac34 y^2\geqslant 0,\]
    等号成立必须 $x- \dfrac12 y= 0$ 且 $y=0$, 与 $xyz>0$ 不符, 所以 $x^2-xy+y^2>0$. 结合 $xyz>0$ 知, \[
        -\frac{x^2-xy+y^2}{xyz}< 0,\]
    即原不等式成立.
    </p>
</myremark>


## 常见的不等式性质

所有不等式的性质都可以由前述两个等价关系以及实数的运算法则得到. 以下介绍的不等式性质都只用于含“$>$”“$<$”“$\geqslant$”“$\leqslant$”的不等式, 且均略去含等号的情形.

<p>类比等式的反身性和传递性, 对不等式有: 若 $a>b$, $b>c$, 则 \[
    b< a,\quad a>c.\]
前一式成立是因为 $a>b$ 表明 $a-b>0$, 即 $a-b$ 为正数, 添负号后为负数, 即 $b-a< 0$, 表明 $b< a$. 后一式成立是因为 $a>b$, $b>c$ 表明 $a-b$ 与 $b-c$ 均为正数, 相加后仍为正数, 即 $a-c> 0$, 表明 $a> c$. 从这两个式子可以看出, 不等式也有传递性, 但没有反身性.
</p>

<p>不等式也有四则运算性质, 但是与等式的四则运算性质有一些区别.
</p>
<p>若 $a> b$, 则 \[
    a\pm c> b\pm c,\]
这是因为 \[
    (a\pm c)- (b\pm c)= a-b> 0.\]
从数轴上来看, 点 $a+c$, $b+c$ 由点 $a$, $b$ 同时向左 (或向右, 取决于 $c$ 的正负号) $|c|$ 得到, 所以保持原有大小关系. 而若 $a> b$, $c> d$, 则 \[
    a+c> b+d,\]
理由是 \[
    (a+c)- (b+d)= (a-b)+ (c-d)> 0.\]
注意, 此时无法判断 $a-c$ 与 $b-d$ 的大小关系, 因为 \[
    (a-c)- (b-d)= (a-b)- (c-d)\]
为两个正数的差, 无法确定正负号. 这也表明, <strong>同向不等式可以求和, 但是不能作差</strong>.
</p>
<p>当 $a> b$ 时, 任取实数 $c$, 则 \[
    ac-bc= (a-b)c.\]
此时已有 $a-b>0$, 所以 $ac$ 与 $bc$ 的大小取决于 $c$ 的正负号, 即 \[\begin{aligned}
    &a> b, c> 0 \Leftrightarrow ac> bc,\\
    &a> b, c= 0 \Leftrightarrow ac= bc,\\
    &a> b, c< 0 \Leftrightarrow ac< bc.
\end{aligned}\]
上述第 $3$ 个不等式表明<strong>不等式两边乘负数, 不等号要改变方向</strong>. 这个性质与等式的性质有很大的差异. 在不等式两边乘相同的式子时, 必须提前判断该式子的符号, 或者只用值为正数的式子乘不等式两边.
</p>
<p>上面的性质可以进一步推广. 若 $a>b>0$, $c>d>0$, 则 $ac>bd$, 理由是 \[
    ac>bc>bd.\]
在上面的假设下, 还有 $a^2> b^2$, 以及更一般的 \[
    a^n> b^n,\quad n\in\mathbf{N}^*.\]
再运用反证法可知, \[
    \sqrt[n]{a}> \sqrt[n]{b},\quad n\in\mathbf{N}^*,\]
这是因为若上式不成立, 则要么 $\sqrt[n]{a}= \sqrt[n]{b}$, 要么 $0< \sqrt[n]{a}< \sqrt[n]{b}$, 前者表明 $a=b$, 后者表明 $a< b$, 均与已知 $a>b>0$ 矛盾.
</p>
<p>现将上述常用的不等式性质汇总如下: \[\begin{aligned}
    &a> b, b> c \Leftrightarrow a> c,\\
    &a> b \Leftrightarrow a\pm c> b\pm c,\\
    &a> b, c> d \Leftrightarrow a+c> b+d,\\
    &a> b, c> 0 \Leftrightarrow ac> bc,\\
    &a>b>0, c>d>0 \Leftrightarrow ac> bd, a^n> b^n, \sqrt[n]{a}> \sqrt[n]{b},
\end{aligned}\]
</p>


## 比较两个式子的大小

<p>因为 $a$ 与 $b$ 的大小关系可以等价描述为 \[\begin{aligned}
    &a> b \Leftrightarrow a-b> 0,\\
    &a= b \Leftrightarrow a-b= 0,\\
    &a< b \Leftrightarrow a-b< 0.
\end{aligned}\]
所以比较 $a$ 与 $b$ 的大小的基本方法是转化为比较 $a-b$ 与 $0$ 的大小, 即把“比较两个变量的大小”转化为“比较一个变量与定值的大小”, 从而降低了难度. 这种方法称为<strong>作差法</strong>. 在比较 $a-b$ 与 $0$ 的大小时, 一般是判断 $a-b$ 的正负号, 或计算其取值范围并与 $0$ 比较. 若已知 $a-b$ 为二次式或等价于二次式, 则可以利用配方来判断其正负号.
</p>
<p>在已知 $a$ 与 $b$ 均为正时, 还可以比较 $\dfrac{a}{b}$ 与 $1$ 的大小. 因为 \[
    \frac{a}{b}- 1= \frac{a-b}{a}\]
的正负号取决于 $a-b$ 的正负号, 所以 \[\begin{aligned}
    &a> b> 0 \Rightarrow \frac{a}{b}> 1,\\
    &a= b>0 \Rightarrow \frac{a}{b}= 1,\\
    &0< a< b \Rightarrow \frac{a}{b}< 1.
\end{aligned}\]
这种方法称为<strong>作商法</strong>, 是作差法的一种特殊形式, 有时可以简化计算.
</p>

<myexample>
    <p>(1) 设 $a_1$, $a_2< 1$, 比较 $a_1a_2$ 与 $a_1+a_2-1$ 的大小;
    </p>
    <p>(2) 设 $a,b,c>0$, 比较 $\dfrac{b}a$ 与 $\dfrac{b+c}{a+c}$ 的大小;
    </p>
    <p>(3) 比较 $x^2+y^2+1$ 与 $2(x+y-1)$ 的大小.
    </p>
</myexample>
<mysolution>
    <p>(1) 直接作差, 并分解因式, \[
        a_1a_2-(a_1+a_2-1)= (a_1-1)(a_2-1).\]
    由 $a_1$, $a_2< 1$ 知, $a_1-1< 0$, $a_2-1< 0$, 则上式为正, 即 \[
        a_1a_2> a_1+a_2-1.\]
    </p>
    <p>(2) 作差并整理, \[
        \frac{b}a- \frac{b+c}{a+c}
        = \frac{c(b-a)}{a(a+c)}.\]
    由已知, $a(a+c)>0$ 且 $c>0$, 所以当 $b-a< 0$ 即 $b< a$ 时, 
    \[\frac{b}a- \frac{b+c}{a+c}< 0,\quad
    \frac{b}a< \frac{b+c}{a+c};\]
    当 $b=a$ 时, $\dfrac{b}a= \dfrac{b+c}{a+c}$; 当 $b>a$ 时, $\dfrac{b}a> \dfrac{b+c}{a+c}$.
    </p>
    <p>(3) 作差并配方, \[\begin{aligned}
       &x^2+y^2+1- 2(x+y-1)\\
        ={}& x^2-2x+y^2-2y+3\\
        ={}& (x-1)^2+(y-1)^2+1>0,
    \end{aligned}\]
    所以 $x^2+y^2+1> 2(x+y-1)$.
    </p>
</mysolution>

<myexercise>
    <p>(1) 设 $x>0$, 比较 $\dfrac{x^2+1}x$ 与 $2$ 的大小;
    </p>
    <p>(2) 若 $a,b>0$, 比较 $a-\dfrac1a$ 与 $b-\dfrac1b$ 的大小.
    </p>
</myexercise>
<mysolution>
    <p>(1) 作差并整理, \[
        \frac{x^2+1}x- 2= \frac{(x-1)^2}{x}\geqslant 0,\]
    所以 $\dfrac{x^2+1}x\geqslant 2$.
    </p>
    <p>(2) 作差并整理, \[\begin{aligned}
        a-\frac1a- \biggl(b-\frac1b\biggl)
        &= a-b+ \frac{a-b}{ab}\\
        &= (a-b)\biggl(1+\frac1{ab}\biggr).
    \end{aligned}\]
    由已知, $1+\dfrac1{ab}>0$, 则当 $a-b>0$ 即 $a>b$ 时, \[
        a-\frac1a- \biggl(b-\frac1b\biggl)>0,\quad
        a-\frac1a> b-\frac1b;\]
    当 $a=b$ 时, $a-\dfrac1a= b-\dfrac1b$; 当 $a< b$ 时, $a-\dfrac1a< b-\dfrac1b$.
    </p>
</mysolution>

<myexample>
    <p>设 $a$, $b$ 为非零实数, 且 $a< b$, 判断下列不等式是否恒成立: \[
        a^2>ab,\quad a^2< b^2,\quad \dfrac1{ab^2}< \dfrac1{a^2b}.\]
    </p>
</myexample>
<mysolution>
    <p>(1) 由 $a< b$ 知 $a-b< 0$, 所以
    \[a^2>ab\Leftrightarrow a^2-ab> 0\Leftrightarrow a(a-b)>0
        \Leftrightarrow a< 0,\]
    但题中并未指明 $a$ 的符号, 所以 $a^2>ab$ 不恒成立.
    </p>
    <p>与 (1) 类似, \[a^2< b^2\Leftrightarrow a^2-b^2< 0
        \Leftrightarrow (a+b)(a-b)< 0
        \Leftrightarrow a+b>0,\]
    但题中并未指明 $a+b$ 的符号, 所以 $a^2< b^2$ 不恒成立.
    </p>
    <p>(3) 用同样的方法, \[\begin{aligned}
        \dfrac1{ab^2}< \dfrac1{a^2b}
        &\Leftrightarrow \dfrac1{ab^2}-\dfrac1{a^2b}< 0
         \Leftrightarrow \frac{a-b}{a^2b^2}< 0\\
        &\Leftrightarrow a-b< 0,
    \end{aligned}\]
    与题意相符, 故恒成立.
    </p>
</mysolution>
