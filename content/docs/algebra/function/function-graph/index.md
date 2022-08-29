---
# bookCollapseSection: true
title: 函数的图象
weight: 4
bookHidden: true
prevPage: /docs/algebra/function/function-oddeven
prevPageTitle: 函数的奇偶性
nextPage: /docs/algebra/function/function-equation
nextPageTitle: 利用函数图象研究方程
---

# 函数的图象


<p>\subsection{二次方程根的分布 (选学)}
<myexample>
<p>若方程 $2(m+1)x^2+4mx+3m-2=0$ 有两个负实根, 求实数 $m$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由题意, 已知的方程为二次方程, 即 $2(m+1)\neq 0$. 设方程的两根为 $x_1$, $x_2$, 则这两个根均为负数的充要条件是
  \[\left\{\!\!\begin{array}{l}
      x_1+x_2=-\dfrac{4m}{2(m+1)}< 0,\\
      x_1x_2=\dfrac{3m-2}{2(m+1)}>0,
    \end{array}\right.\quad\text{解得}\quad
    m< -1\ \text{或}\ m>\frac23,\]
  所求的 $m$ 的取值范围是 $(-\infty,-1)\cup\biggl(\dfrac23,+\infty\biggr)$.
</p>
</mysolution>
</p>
<p>设关于 $x$ 的二次方程 $Ax^2+Bx+C=0$ ($A\neq0$) 的两根为 $x_1$, $x_2$, 则有以下结论 (为什么?):
</p>
<p>(1) 两根为正的充要条件是
  \[\left\{\!\!\begin{array}{l}
      x_1+x_2>0,\\
      x_1x_2>0,
    \end{array}\right.\quad\text{即}\quad
    \left\{\!\!\begin{array}{l}
      -\dfrac{B}A>0,\\
      \dfrac{C}A>0;
    \end{array}\right.\]
</p>
<p>(2) 两根为负的充要条件是
  \[\left\{\!\!\begin{array}{l}
      x_1+x_2< 0,\\
      x_1x_2>0,
    \end{array}\right.\quad\text{即}\quad
    \left\{\!\!\begin{array}{l}
      -\dfrac{B}A< 0,\\
      \dfrac{C}A>0;
    \end{array}\right.\]
</p>
<p>(3) 两根一正一负的充要条件是
  \[x_1x_2< 0\quad\text{即}\quad\frac{C}A< 0.\]
</p>

<p>\begin{example}\label{201109-2120}
    已知函数 $f(x)= 4x^2-kx-8$ 在 $[5,20]$ 上单调变化, 求实数 $k$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>$f(x)$ 为二次函数, 单调性由开口方向、对称轴和定义域共同决定. 由题意, $f(x)$ 的对称轴 $x=\dfrac{k}8$ 不在区间 $[5,20]$ 内, 所以
    \[\frac{k}8\leqslant 5\ \text{或}\ \frac{k}8\geqslant 20,\quad
        \text{解得}\ k\leqslant 40\ \text{或}\ k\geqslant 160,\]
    即 $k\in(-\infty,40]\cup [160,+\infty)$.
</p>
</mysolution>
<myremark>
    <p>例 \ref{201109-2120} 中的二次函数在区间 $[5,20]$ 上若单调递增, 则 $\dfrac{k}8\leqslant 5$; 若单调递减, 则 $\dfrac{k}8\geqslant 20$ (为什么?).
</p>
</myremark>
