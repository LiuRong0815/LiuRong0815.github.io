---
# bookCollapseSection: true
title: 分式不等式与高次不等式
weight: 3
# bookHidden: true
prevPage: /docs/prerequisite/inequality/abs-quadratic-inequality
prevPageTitle: 绝对值不等式与二次不等式
# nextPage: /docs/prerequisite/inequality/mean-value-inequality
# nextPageTitle: 均值不等式
---

# 分式不等式与高次不等式

二次不等式的解法也可以用于求解简单的分式不等式. 求解一般的分式不等式和高次不等式时, 需将二次不等式的解法推广为“穿根法”.

## 简单的分式不等式的解法

<p>关于 $x$ 的形如 $\dfrac{Ax+B}{Cx+D}>(\geqslant)\,0$ 的分式不等式, 可以利用分子和分母的正负号关系转化为二次不等式来解. 具体地, \[\begin{aligned}
    \frac{Ax+B}{Cx+D}>0 & \Leftrightarrow (Ax+B)(Cx+D)>0,\\
    \frac{Ax+B}{Cx+D}\geqslant 0 & \Leftrightarrow \left\{\!\!
    \begin{array}{l}
        (Ax+B)(Cx+D)\geqslant 0,\\
        Cx+D\neq 0.
    \end{array}\right.
\end{aligned}\]
前一个等价关系中右边不用限制分母非零, 因为乘积非零等价于两个因子均非零; 后一个等价关系中右边必须限制分母非零, 因为乘积为零等价于两个因子均可能为零. 例如, 不等式 $\dfrac{x-2}{x-3}>0$ 等价于 $(x-2)(x-3)>0$, 则 $x\in (-\infty,2)\cup (3,+\infty)$. 注意,
\[\frac{x-2}{x-3}\geqslant 0\Leftrightarrow \left\{\!\!\begin{array}{l}
    (x-2)(x-3)\geqslant 0,  \\
    x-3\neq 0,
\end{array}\right.\]
解得 $x\in (-\infty,2]\cup (3,+\infty)$.
</p>

<p>关于 $x$ 的形如 $\dfrac{Ax+B}{Cx+D}>(\geqslant)\,E$ 的分式不等式, 也可以先移项、合并, 变成与 $0$ 比大小, 即写为 \[
    \frac{Ax+B-E(Cx+D)}{Cx+D}>(\geqslant)\,0,\]
从而进一步化为二次不等式来求解.
</p>

<myexample>
    <p>解下列不等式:
    </p>
    <p>(1) $\dfrac{2x-3}{x-5}>1$;&emsp; (2) $\dfrac{2-x}{x-5}\geqslant 2$.
    </p>
</myexample>

<mysolution>
    <p>(1) 原不等式化为 \[
        \frac{2x-3}{x-5}-1>0\Rightarrow \frac{x+2}{x-5}>0,\] 
    所以等价于 $(x+2)(x-5)>0$, 解得 $x\in (-\infty,-2)\cup (5,+\infty)$.
    </p>
    <p>(2) 移项、合并后, 原不等式化为 \[
        \frac{12-3x}{x-5}\geqslant 0,\] 
    等价于 \[\left\{\!\!\begin{array}{l}
        (12-3x)(x-5)\geqslant 0,\\
        x-5\neq 0,
    \end{array}\right. \text{解得}\ 
        x\in [4,5).\]
    </p>
</mysolution>

<myexercise>
    <p>解不等式 $\dfrac{x-1}x\geqslant 2$.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>移项、合并后, 再去负号、去分母, 可得 $\dfrac{x+1}{x}\leqslant 0$, 进一步解得 $x\in [-1,0)$.
    </p>
</details>

<myexample>
    <p>若 $a>b$, 且 $a-\dfrac1a> b-\dfrac1b$, 求 $ab$ 的取值范围.
    </p>
</myexample>
<mysolution>
    <p>作差并整理, \[\begin{aligned}
        a-\frac1a- \biggl(b-\frac1b\biggl)
        &= a-b+ \frac{a-b}{ab}\\
        &= (a-b)\biggl(1+\frac1{ab}\biggr)\\
        &>0.
    \end{aligned}\]
    由 $a>b$ 知 $a-b>0$, 上式两边同时除以 $a-b$ 得 $1+\dfrac1{ab}>0$. 将 $ab$ 视为整体, 解得 $ab\in(-\infty,-1)\cup (0,+\infty)$.
    </p>
</mysolution>

<myremark>
    <p>对不等式 $1+\dfrac1x> 0$, 常见的错误解法是直接在不等式两边同乘 $x$, 并得到 $x> -1$. 这种解法错误的原因是默认 $x$ 为正数, 而忽略了不等式两边乘负数时要变号. 正确的解法是按前述方法先将不等式化为与 $0$ 比大小, 再转化为等价的整式不等式. 还有一个方法是<a href="/docs/prerequisite/ms-function/linear-inverse/#利用反比例函数解不等式">直接利用反比例函数图象</a>. 用这两种解法均可以得到 $\dfrac1x< 1$ 的解集为 $(-\infty,-1)\cup (0,+\infty)$.
    </p>
</myremark>

## 高次不等式的解法

<p>利用零点分段法从代数角度理解二次不等式的解法, 可以推广得到高次不等式的解法. 对 $(x+1)(x-2)>0$, 以因式的零点 $-1$, $2$ 为分界点划分数轴, 并列出下表 \[\begin{array}{c|ccc}
    \hline
    x & (-\infty,-1) & (-1,2) & (2,+\infty) \\
    \hline
    x+1 & - & + & + \\
    x-2 & - & - & + \\
    (x+1)(x-2) & + & - & +\\
    \hline
\end{array}\]
可知解集为 $(-\infty,-1)\cup (2,+\infty)$. 注意表中略去了零点所在列. 同样地, 考虑 \[
    (x+1)(x-2)(x-3)>0,\]
以因式的零点 $-1$, $2$, $3$ 为分界点划分数轴, 可以列出下表 \[\begin{array}{c|cccc}
    \hline
    x & (-\infty,-1) & (-1,2) & (2,3) & (3,+\infty) \\
    \hline
    x+1 & - & + & + & + \\
    x-2 & - & - & + & + \\
    x-3 & - & - & - & + \\
    (x+1)(x-2)(x-3) & - & + & - & +\\
    \hline
\end{array}\]
因此解集为 $(-1,2)\cup (3,+\infty)$. 
</p>
<p>上述两个不等式均为多个互异的一次式的乘积与 $0$ 比大小, 且各因式的一次项系数为正. 观察对应的正负值表可以看出:
</p>
<p>(1) 每个一次因式仅在其零点处变号, 从而使得乘积式在每个零点处均变号; 
</p>
<p>(2) 在以 $+\infty$ 为右端点的区间上, 各因式均为正数, 所以乘积式也必为正数. 
</p>
<p>正是因为这两个特征, 在求解高次不等式时, 可以根据乘积式的正负号, 结合数轴从右往左大致描出对应函数的图象, 然后写出不等式的解集. 例如, 由不等式 \[
    (x+1)(x-2)(x-3)>0\]
可以描出下图, 并得到解集 $(-1,2)\cup (3,+\infty)$.
</p>

![不等式 $(x+1)(x-2)(x-3)>0$ 的穿线法](/figs/2022/2022-09/2022-0907-2140.svg)

<p>上述方法称为<strong>穿根法</strong>, 利用了乘积式在各零点两侧异号的特点. 某些分式不等式与高次不等式等价, 也可以用穿根法求解. 例如, 不等式 $\dfrac{(x+1)(x-2)}{x-3}>0$ 等价于 \[
    (x+1)(x-2)(x-3)>0,\]
解集亦为 $(-1,2)\cup (3,+\infty)$.
</p>


