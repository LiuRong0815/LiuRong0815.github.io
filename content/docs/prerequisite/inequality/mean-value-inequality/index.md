---
# bookCollapseSection: true
title: 均值不等式
weight: 4
# bookHidden: true
prevPage: /docs/prerequisite/inequality/fraction-high-order-inequality
prevPageTitle: 分式不等式与高次不等式
nextPage: /
nextPageTitle: 本站介绍
---

# 均值不等式

均值不等式是数学中常用的一类基本不等式, 也被推广为多种不等式. 这里介绍均值不等式最简单的形式.

<p>对于任意 $a$, $b\in\mathbf{R}$, 恒有 $(a-b)^2\geqslant 0$, 展开后移项得 \[
    a^2+b^2\geqslant 2ab\quad\text{即}\quad 
    \frac{a^2+b^2}2\geqslant ab.\]
不等式中等号成立的充要条件是 $a=b$, 也记为: “$=$”成立当且仅当 $a=b$. 把上面两个式子中的 $a$ 和 $b$ 分别换成 $\sqrt{x}$ 和 $\sqrt{y}$ (此时必须限制 $x$, $y\geqslant 0$), 可知 \[
    x+y\geqslant 2\sqrt{xy}\quad\text{即}\quad 
    \frac{x+y}2\geqslant \sqrt{xy}.\]
上式中的 $\dfrac{x+y}2$ 与 $\sqrt{xy}$ 分别叫做非负实数 $x$ 与 $y$ 的<strong>算术平均值</strong>与<strong>几何平均值</strong>, 所以上面最后一个不等式也称为均值不等式, 即
\[\text{均值不等式:}\ \frac{x+y}2\geqslant \sqrt{xy},\quad x,y\geqslant 0.\]
该不等式有时也称为基本不等式. 以上不等式均为常用不等式, 且都可以互相推出.
</p>
<p>使用均值不等式时, 必须检验等号成立的条件. 如对 $x>2$, 由 $x+\dfrac1x\geqslant 2$ 不能得到 $x+\dfrac1x$ 的取值范围是 $[2,+\infty)$, 因为此时等号成立的条件是 $x=1$, 与已知 $x>2$ 不符. 求取值范围时, 正确的解法是先判断函数 $y=x+\dfrac1x$ 在 $x>2$ 时的单调性 (即函数值的增减性).
</p>

## 利用均值不等式求最值

<p>利用均值不等式 (或其等价形式) 可以很方便地求特殊形式的式子的最大 (小) 值. 例如, 若 $x>0$, 则 \[
    x+\dfrac1x\geqslant 2\sqrt{x\cdot\dfrac1x}=2,\]
“$=$”成立当且仅当 $x=\dfrac1x$ 即 $x=1$. 一般地, 可得如下结论 (均设 $x$, $y\geqslant 0$):
</p>
<p>(1) 若 $xy=L$ 为定值, 则 \[
    x+y\geqslant 2\sqrt{xy}=2\sqrt{L},\]
所以 $x+y$ 的最小值为 $2\sqrt{L}$, “$=$”成立当且仅当 $x=y=\sqrt{L}$;
</p>
<p>(2) 若 $x+y=M$ 为定值, 则 \[\begin{gathered}
    \sqrt{xy}\leqslant \frac{x+y}2=\frac{M}2,\\
    xy\leqslant \biggl(\frac{M}2\biggr)^2= \frac{M^2}4,
\end{gathered}\]
所以 $xy$ 的最大值为 $\dfrac{M^2}4$, “$=$”成立当且仅当 $x=y=\dfrac{M}2$. 这个结论也可以由二次函数的图象得出: $xy= x(M-x)$ 是 $x$ 的二次函数, 对称轴为 $x=\dfrac{M}2$, 图象开口向下, 故最大值为 $\dfrac{M^2}4$.
</p>

<myremark>
    <p>运用上述结论时, 应直接利用均值不等式 $x+y\geqslant 2\sqrt{xy}$ 推理, 且应注意该不等式成立的前提是 $x$, $y\geqslant 0$, 还必须检验等号成立的充要条件“$x=y$”.
    </p>
</myremark>

<myexample>
    <p>(1) 设正数 $x$, $y$ 满足 $xy=4$, 求 $x+2y$ 的最小值;
    </p>
    <p>(2) 设正数 $x$, $y$ 满足 $x+2y=4$, 求 $xy$ 的最大值;
    </p>
    <p>(3) 设 $a,b$ 为正数, 求 $\dfrac{b}a +\dfrac{3a}b$ 的最小值.
    </p>
</myexample>

<mysolution>
    <p>(1) $x+2y\geqslant 2\sqrt{2xy}= 4\sqrt2$, “$=$”成立当且仅当 $x=2y$, 结合 $xy=4$ 知 $x=2\sqrt2$, $y=\sqrt2$, 则 $x+y$ 的最小值为 $4$.
    </p>
    <p>(2) $4= x+2y\geqslant 2\sqrt{2xy}$, 则 $xy\leqslant 2$, 等号成立当且仅当 $x=2y$, 结合 $x+2y=4$ 知 $x= 2$, $y=1$ 所以 $xy$ 的最大值为 $2$.
    </p>
    <p>(3) 因为 \[
        \dfrac{b}a +\dfrac{3a}b
            \geqslant 2\sqrt{\dfrac{b}a\cdot \dfrac{3a}b}=2\sqrt3,\]
    等号成立当且仅当 $\dfrac{b}a= \dfrac{3a}b$ 即 $\sqrt3a=b$, 所以 $\dfrac{b}a +\dfrac{a}b$ 的最小值为 $2$.
    </p>
</mysolution>

<myremark>
    <p>(1) 以上各问列出等号成立的条件时, 均需与已知条件联立求解, 以确保所得变量取值合乎已知条件. 
    </p>
    <p>(2) 上述 (3) 中, 条件“$a,b$ 为正数”可以进一步放宽为“$ab>0$”. 
    </p>
</myremark>

<myexercise>
    <p>(1) 当函数 $y=x^2 +\dfrac9{x^2}$ ($x\neq 0$) 取最小值时, 求对应的 $x$ 的值.
    </p>
    <p>(2) 若实数 $x,y$ 满足 $xy=1$, 求 $x^2 + 4y^2$ 的最小值.
    </p>
    <p>(3) 条件“$x>0$”是“$x^2+\dfrac1{x^2}\geqslant 2$”的什么条件?
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $x^2 +\dfrac9{x^2}\geqslant 2\sqrt{9}= 6$, 等号成立当且仅当 $x= \pm3$.
    </p>
    <p>(2) $x^2 +4y^2\geqslant 4xy= 4$, 等号成立当且仅当 $x=\pm\sqrt2$, $y=\pm\dfrac{\sqrt2}2$.
    </p>
    <p>(3) 因为 $x^2$ 恒非负, 所以只要 $x\neq0$, 就有 $x^2>0$, 此时 $x^2+\dfrac1{x^2}\geqslant 2$. 这表明 $x^2+\dfrac1{x^2}\geqslant 2$ 的充要条件是 $x\neq 0$. 再与 $x>0$ 对比可知, “$x>0$”是“$x^2+\dfrac1{x^2}\geqslant 2$”的充分不必要条件.
    </p>
</details>

<p>有时, 要求取值范围的式子不能直接用均值不等式, 但可以通过变形化为能用均值不等式的形式, 或需要利用均值不等式做媒介得到新的不等式. 
</p>

<myexample>
    <p>(1) 若 $x>-3$, 求 $x+\dfrac2{x+3}$ 的最小值;
    </p>
    <p>(2) 若正实数 $x,y$ 满足 $2x+y+6=xy$, 求 $xy$ 和 $2x+y$ 各自的最大值.
    </p>
</myexample>

<mysolution>
    <p>(1) 利用 $x>-3$ 直接凑出均值不等式的形式, \[\begin{aligned}
         x+\dfrac2{x+3}
        &= (x+3)+\dfrac2{x+3}- 3\\
        &\geqslant 2\sqrt2-3,
    \end{aligned}\]
    等号成立当且仅当 $x= \sqrt2-3$, 即 $x+\dfrac2{x+3}$ 的最小值为 $2\sqrt2-3$.
    </p>
    <p>(2) 由 $2x+y\geqslant 2\sqrt{2xy}$ 和已知, \[\begin{gathered}
        xy-6\geqslant 2\sqrt{2xy}\Rightarrow xy\geqslant 18,\\
        2x+y\geqslant 2\sqrt{2(2x+y+6)}\Rightarrow 2x+y\geqslant 12,
    \end{gathered}\]
    等号成立当且仅当 $2x=y= 6$. 所以 $xy$ 的最大值为 $18$, $2x+y$ 的最大值为 $12$.
    </p>
</mysolution>

<myremark>
    <p>上例 (2) 中得到分别关于 $xy$ 和 $2x+y$ 的根式不等式, 平方后均可按二次不等式求解. 
    </p>
</myremark>

<myexercise>
    <p>(1) 若 $x>3$, 求 $x+\dfrac2{x-3}$ 的最小值;
    </p>
    <p>(2) 设正数 $a,b$ 满足 $a^2+2ab+4b^2= 3$, 求 $ab$ 的最大值.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) 因为 $x>3$ 表示 $x-3>0$, 所以 \[\begin{gathered}
        (x-3)+\dfrac2{x-3}\geqslant 2\sqrt2,\\
        x+\frac2{x-3}\geqslant 2\sqrt2+3,
    \end{gathered}\]
    等号成立当且仅当 $x=3+\sqrt2$, 即 $x+\dfrac2{x-3}$ 的最小值为 $2\sqrt2+3$.
    </p>
    <p>(2) 由 $a^2+4b^2\geqslant 4ab$ 和已知, \[
        3- 2ab\geqslant 4ab,\quad ab\leqslant \frac12,\]
    等号成立当且仅当 $a^2= 4b^2$ 即 $a=2b$, 结合已知等式解得, $a=1$, $b=\dfrac12$.
    </p>
</details>

<myexample>
    <p>(1) 设 $t>0$, 求 $\dfrac{t^2-4t+1}t$ 的最小值和对应的 $t$ 的值.
    </p>
    <p>(2) 若 $x>0$, 求 $\dfrac{16x}{x^2+1}$ 的最大值.
    </p>
</myexample>

<mysolution>
    <p>(1) 方法一: 因为 $t>0$, 所以由均值不等式, \[
        \frac{t^2-4t+1}t= t+\frac1t-4
        \geqslant 2\sqrt{t\cdot\frac1t}-4= -2,\]
    “$=$”成立当且仅当 $t=\dfrac1t$ 即 $t=1$. 所以最小值为 $-2$, 且对应的 $t=1$.
    </p>
    <p>方法二: 因为 $t>0$, 所以由均值不等式, $t^2+1\geqslant 2t$, 则 \[
        \frac{t^2-4t+1}t\geqslant \frac{2t-4t}t= -2,\]
    “$=$”成立当且仅当 $t=1$. 所以最小值为 $-2$, 且对应的 $t=1$.
    </p>
    <p>(2) 方法一: 因为 $x>0$, 所以对原式的分子和分母同除以 $x$, 以便于用均值不等式 (注意分母为正数且变小, 故分式增大), \[
        \frac{16x}{x^2+1}= \frac{16}{x+\dfrac1x}
        \geqslant \frac{16}{2\sqrt{x\cdot\dfrac1x}}
        =8,\]
    “$=$”成立当且仅当 $x=\dfrac1x$ 即 $x=1$. 因此所求最大值为 $8$.
    </p>
    <p>方法二: 直接对原式分母用均值不等式, 则 \[
        \dfrac{16x}{x^2+1}
        \leqslant \frac{16x}{2\sqrt{x^2\cdot 1}}= 8,\]
    “$=$”成立当且仅当 $x=\dfrac1x$ 即 $x=1$. 因此所求最大值为 $8$.
    </p>
</mysolution>

## 均值不等式与几何题

<p>均值不等式 $\dfrac{x+y}2\geqslant \sqrt{xy}$ ($x$, $y\geqslant 0$) 有明显的几何意义. 如下图所示, 线段 $AB$ 是半圆 $O$ 的直径, 任取半圆上一点 $C$, 作 $CD\perp AB$ 于点 $D$, 则 \[
    \triangle ADC\sim \triangle CDB\Rightarrow
    CD^2= AD\cdot DB.\]
因为半径 $CO\geqslant CD$, 且 \[
    CO= \frac12 AB= \frac{AD+DB}2,\quad
    CD= \sqrt{AD\cdot DB},\]
所以 $\dfrac{AD+DB}2\geqslant \sqrt{AD\cdot DB}$. 这就是均值不等式.
</p>

![均值不等式的几何意义-半圆](/figs/2022/2022-09/2022-0911-1440.svg)

利用均值不等式解几何题时, 关键是要根据题意, 写出其中几何量满足的条件, 所以需要对各几何图形的常见性质比较熟悉.

<myexercise>
    <p>(1) 设 $\mathrm{Rt}\,\triangle ABC$ 的面积为 $1$, 且 $C=90^\circ$, 求该三角形周长的最小值;
    </p>
    <p>(2) 一个矩形内接于半径为 $1$ 的圆, 求该矩形的面积和周长各自的最大值.
    </p>
</myexercise>

<mysolution>
    <p>(1) 设角 $A,B,C$ 的对应边长为 $a,b,c$, 则 $\dfrac12ab=1$ 即 $ab= 2$, 且由勾股定理, $c^2= a^2+b^2$. 所以 \[\begin{gathered}
        a+b\geqslant 2\sqrt{ab}= 2\sqrt2,\\
        c= \sqrt{a^2+b^2}\geqslant \sqrt{2ab}= 2,
    \end{gathered}\]
    等号成立当且仅当 $a=b=\sqrt2$, 此时 $\triangle ABC$ 为等腰直角三角形, 从而该三角形的周长 \[
        a+b+c\geqslant 2\sqrt2+ 2,\]
    即最小值为 $2\sqrt2+ 2$.
    </p>
    <p>(2) 设该矩形的两个邻边长为 $a,b$. 由题意, 矩形的对角线为圆的直径, 所以 \[\begin{gathered}
        a^2+b^2= 2^2= 4,\\
        ab\leqslant \frac{a^2+b^2}{2}= 2,
    \end{gathered}\]
    即矩形面积的最大值为 $2$, 此时 $a=b=\sqrt2$. 因为 \[
        (a+b)^2= a^2+b^2+2ab\geqslant 4+4= 8,\]
    所以 $a+b\geqslant 2\sqrt2$, 即矩形周长 $2(a+b)$ 的最大值为 $4\sqrt2$, 此时仍有 $a=b=\sqrt2$.
    </p>
</mysolution>

<myremark>
    <p>上例 (2) 的结论表明: 定圆的内接矩形中, 正方形的周长和面积均为最大. 这个结论后续可以进一步推广为: 定圆的内接 $n$ 边形中, 正 $n$ 边形的周长和面积均为最大.
    </p>
</myremark>

<myexercise>
    <p>设 $\mathrm{Rt}\,\triangle ABC$ 的周长为 $2+2\sqrt2$, 且 $C=90^\circ$, 求该三角形面积的最大值.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>设角 $A,B,C$ 的对应边长为 $a,b,c$, 则 \[
        a+b+c= 2+2\sqrt2,\quad c^2= a^2+b^2.\]
    因为 \[\begin{gathered}
        a+b\geqslant 2\sqrt{ab},\\
        c= \sqrt{a^2+b^2}\geqslant \sqrt{2ab},
    \end{gathered}\]
    代入周长表达式知, \[
        2+2\sqrt2\geqslant 2\sqrt{ab}+ \sqrt{2ab},\]
    解得 $ab\leqslant 2$, 等号成立当且仅当 $a=b=\sqrt2$, 此时 $\triangle ABC$ 为等腰直角三角形. 从而该三角形的面积 $\dfrac12ab\leqslant 1$, 即最大值为 $1$.
    </p>
</details>

## 均值不等式与恒成立问题

<p>与代数式有关的恒成立问题, 解法通常是先求代数式的取值范围. 例如, 设正实数 $x,y$ 满足 $x+y=2$, 且 $M\geqslant xy$ 恒成立, 由此来确定 $M$ 的最小值. 因为 \[
    x+y\geqslant 2\sqrt{xy}\Rightarrow 2\geqslant 2\sqrt{xy},\]
所以 $xy\in (0,1]$, 且 $xy=1$ 当且仅当 $x= y= 1$. 由 $M\geqslant xy$ 恒成立可知 $M\geqslant 1$, 即 $M$ 的最小值为 $1$.
</p>

<myexample>
    <p>(1) 若 $x$, $y>0$ 且 $\dfrac{2y}x+ \dfrac{8x}y> m^2+2m$ 恒成立, 求 $m$ 的取值范围.
    </p>
    <p>(2) 已知二次函数 $y=ax^2 -4x+c$ ($x\in\mathbf{R}$) 的值域为 $[0,+\infty)$, 求 $\dfrac1c +\dfrac9a$ 的最小值.
    </p>
</myexample>
<mysolution>
    <p>(1) 由 $\dfrac{2y}x+ \dfrac{8x}y\geqslant 2\sqrt{16}= 8$, 等号成立当且仅当 $2x= y$, 知 \[
        8> m^2+2m,\quad m\in(-4,2).\]
    </p>
    <p>(2) 由已知, 抛物线 $y=ax^2 -4x+c$ 与 $x$ 轴相切, 考虑判别式知, \[
        \Delta= (-4)^2- 4ac= 0,\quad ac=4,\]
    所以 \[
        \frac1c +\frac9a\geqslant 2\sqrt{\frac{9}{ac}}= 3,\]
    等号成立当且仅当 $a=9c$ 即 $a= 6$, $c= \dfrac23$.
    </p>
</mysolution>

<myexercise>
    <p>若 $\forall\, x>0$, $x+\dfrac2x+a>0$ 恒成立, 求 $a$ 的取值范围.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>由题意, 只需不等式左边的最小值大于零. 由均值不等式, \[
        x+\dfrac2x\geqslant 2\sqrt{x\cdot\dfrac2x}= 2\sqrt2,\]
    “$=$”成立当且仅当 $x=\dfrac2x$ 即 $x=\sqrt2$, 所以只需
    \[2\sqrt2+a>0\Rightarrow
        a\in(-2\sqrt2,+\infty).\]
    </p>
</details>

## 均值不等式的推广

<myexample>
    <p>若 $a>0$, $b>0$ 且 $a\neq b$, 比较 $\dfrac{a+b}2$, $\sqrt{ab}$, $\sqrt{\dfrac{a^2+b^2}2}$ 的大小.
    </p>
</myexample>
<mysolution>
    <p>由均值不等式, $\sqrt{ab}\leqslant \dfrac{a+b}2$. 但已知 $a\neq b$, 所以等号不成立, 即 $\sqrt{ab}< \dfrac{a+b}2$. 再考虑 $\dfrac{a+b}2$ 和 $\sqrt{\dfrac{a^2+b^2}2}$ 的大小. 因为 (带根号的式子, 先平方去掉根号) \[
        \biggl(\sqrt{\dfrac{a^2+b^2}2}\biggr)^2- \biggl(\dfrac{a+b}2\biggr)^2
        = \frac{(a-b)^2}{4}>0,\]
    所以 $\sqrt{\dfrac{a^2+b^2}2}> \dfrac{a+b}2$, 故 \[
        \sqrt{ab}< \dfrac{a+b}2< \sqrt{\dfrac{a^2+b^2}2}.\]
    </p>
</mysolution>

<myremark>
    <p>进一步可以证明, 若 $a$, $b>0$, 则 \[
        \frac{2ab}{a+b}\leqslant \sqrt{ab}
        \leqslant \dfrac{a+b}2
        \leqslant \sqrt{\dfrac{a^2+b^2}2},\]
    “$=$”成立当且仅当 $a=b$.
    </p>
</myremark>

<myexample>
    <p>设正数 $a,b$ 满足 $a^2+4b^2+\dfrac1{ab}= 4$, 求 $a,b$ 的值.
    </p>
</myexample>

<mysolution>
    <p>由均值不等式, \[
        a^2+4b^2+\frac1{ab}\geqslant 4ab+ \frac1{ab} \geqslant 4,\]
    等号成立当且仅当 $a^2= 4b^2$ 且 $4ab= \dfrac1{ab}$, 解得 $a=1$, $b= \dfrac12$. (这里用了两次均值不等式, 所以需要写出两个等号成立的条件.)
    </p>
</mysolution>
