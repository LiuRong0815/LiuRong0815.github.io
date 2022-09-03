---
# bookCollapseSection: true
title: 分式不等式与高次不等式
weight: 3
bookHidden: true
prevPage: /docs/prerequisite/inequality/abs-quadratic-inequality
prevPageTitle: 绝对值不等式与二次不等式
nextPage: /docs/prerequisite/inequality/mean-value-inequality
nextPageTitle: 均值不等式
---

# 分式不等式与高次不等式

<p>\subsection{简单的分式不等式的解法}
</p>
<p>关于 $x$ 的形如 $\dfrac{Ax+B}{Cx+D}>(\geqslant)\,0$ 的分式不等式, 可以利用分子和分母的正负号关系转化为二次不等式来解. 具体地,
\begin{align}\label{eq-201009-1907}
  \frac{Ax+B}{Cx+D}>0 & \Leftrightarrow (Ax+B)(Cx+D)>0,\\
  \label{eq-201009-1917}
  \frac{Ax+B}{Cx+D}\geqslant 0 & \Leftrightarrow \left\{\!\!
    \begin{array}{l}
      (Ax+B)(Cx+D)\geqslant 0,\\
      Cx+D\neq 0.
    \end{array}\right.
\end{align}
\eqref{eq-201009-1907} 式中右边不用限制分母非零, 因为乘积非零隐含两个因子均非零; 而 \eqref{eq-201009-1917} 式中右边必须限制分母非零, 因为乘积为零隐含两个因子均可能为零. 
</p>
<p><myexample>
<p>解下列不等式:
  \begin{twocolpro}
    (1) $\dfrac{x-2}{x-5}>0$; & (2) $\dfrac{x-2}{x-5}\geqslant 0$.
  \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 原不等式等价于 $(x-2)(x-5)>0$, 所以 $x\in (-\infty,2)\cup (5,+\infty)$.
</p>
<p>(2) 原不等式等价于
  \[\left\{\!\!\begin{array}{l}
        (x-2)(x-5)\geqslant 0,\\
        x-5\neq 0,
      \end{array}\right. \text{解得}\ 
      x\in (-\infty,2]\cup (5,+\infty).\]
</p>
</mysolution>
</p>

<myexercise>
    <p>若 $a>b$, 且 $a-\dfrac1a> b-\dfrac1b$, 求 $ab$ 的取值范围.
    </p>
</myexercise>
<mysolution>
    <p>作差并整理, \[\begin{aligned}
        a-\frac1a- \biggl(b-\frac1b\biggl)
        &= a-b+ \frac{a-b}{ab}\\
        &= (a-b)\biggl(1+\frac1{ab}\biggr)>0.
    \end{aligned}\]
    由 $a>b$ 知 $a-b>0$, 上式两边同时除以 $a-b$ 得
    \[1+\frac1{ab}>0.\]
    将 $ab$ 视为整体, 解得 $ab\in(-\infty,-1)\cup (0,+\infty)$.
    </p>
</mysolution>

<p>解二次不等式时, 需要考虑对应抛物线的图象, 尤其应注意开口方向. 也可以先将不等式各因子化为最高次项系数为正的形式, 然后再根据抛物线的图象写出相应的解集.
</p>
<p><myexample>
<p>解下列不等式:
  \begin{twocolpro}
    (1) $\dfrac{2-x}{x-5}>0$; & (2) $\dfrac{2-x}{x-5}\geqslant 0$.
  \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 原不等式等价于 $(2-x)(x-5)>0$ 即 $(x-2)(x-5)< 0$ , 所以 $x\in (2,5)$.
</p>
<p>(2) 原不等式等价于
  \[\left\{\!\!\begin{array}{l}
        (2-x)(x-5)\geqslant 0,\\
        x-5\neq 0,
      \end{array}\right. \text{解得}\ 
      x\in [2,5).\]
</p>
</mysolution>
</p>
<p>关于 $x$ 的形如 $\dfrac{Ax+B}{Cx+D}>(\geqslant)\,E$ 的分式不等式, 也可以改写为
\[\frac{Ax+B}{Cx+D}-E>(\geqslant)\,0\quad \text{即}\quad
  \frac{Ax+B-E(Cx+D)}{Cx+D}>(\geqslant)\,0,\]
从而化为前面形式的不等式来求解.
</p>
<p><myexample>
<p>解下列不等式:
  \begin{twocolpro}
    (1) $\dfrac{2x-3}{x-5}>1$; & (2) $\dfrac{2-x}{x-5}\geqslant 2$.
  \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 原不等式化为
  \[\frac{2x-3}{x-5}-1>0\quad \text{即}\quad \frac{x+2}{x-5}>0,\] 
  所以等价于 $(x+2)(x-5)>0$, 解得 $x\in (-\infty,-2)\cup (5,+\infty)$.
</p>
<p>(2) 原不等式化为
  \[\frac{2-x}{x-5}-2\geqslant 0\quad \text{即}\quad \frac{12-3x}{x-5}\geqslant 0,\] 
  所以等价于
  \[\left\{\!\!\begin{array}{l}
        (12-3x)(x-5)\geqslant 0,\\
        x-5\neq 0,
      \end{array}\right. \text{解得}\ 
      x\in [4,5).\]
</p>
</mysolution>
