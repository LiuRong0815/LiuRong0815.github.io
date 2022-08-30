---
# bookCollapseSection: true
title: 利用函数图象研究方程
weight: 6
bookHidden: true
prevPage: /docs/algebra/pow-exp-log/composite-inverse
prevPageTitle: 复合函数与反函数
nextPage: /docs/algebra/sequence
nextPageTitle: 数列
---

# 利用函数图象研究方程

<p>求方程的根可以转化为求对应函数图形交点的横坐标, 或求对应函数的零点. 
  一般有如下两种转化方法:
  \[\begin{aligned}
    f(x)=0\text{\ 的根}&\Leftrightarrow 
      \text{$f(x)$ 的图形与 $x$ 轴交点的横坐标};\\
    f(x)+g(x)=0\text{\ 的根}&\Leftrightarrow 
      \text{$f(x)$ 与 $-g(x)$ 的图形交点的横坐标}.
  \end{aligned}\]
  前一种方法可视为后一种方法的特例, 而两种方法在使用时都需要考虑函数的单调性.
  此外还有 (画图更容易理解)
</p>
<p><strong>零点存在性定理</strong>: 若 $f(x)$ 在 $[a,b]$ 上连续, 且 $f(a)f(b)< 0$,   则 $f(x)$ 在 $(a,b)$ 上至少有一根. 
</p>
<p>\begin{example}\label{exa:201217-1900}
    已知函数 $f(x)= \begin{cases}
        \dfrac2x, & x\geqslant 2,\\
        x^2-3, & x< 2,
    \end{cases}$ 若关于 $x$ 的方程 $f(x)=k$ 有三个不等的实根, 求 $k$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>此题应考虑函数 $y=f(x)$ 与 $y=k$ 的图形的交点恰有三个的情形. 画出两者的图形示意图, 容易知道 $k\in(0,1)$.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1214-1900-crop}
    </center>
</p>
</mysolution>
</p>
<p>\begin{example}\label{exa:201214-1905}
    求函数 $f(x)=x^2-\log_{\frac12} x$ 的零点个数.
</p>
</myexample>
<mysolution>
    <p>由 $f(x)=x^2-\log_{\frac12} x=0$ 可得 $x^2=\log_{\frac12} x$, 故设 $g(x)=x^2$, $h(x)=\log_{\frac12} x$, 并考虑两者图形的交点个数. 画图可知, 只有一个交点.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1214-1910-crop}
    </center>
</p>
</mysolution>
<myremark>
    <p>可以进一步用零点存在性定理来估计例 \ref{exa:201214-1905} 中的 $f(x)$ 的零点所在的大致区间. 因为已经由图知道 $f(x)$ 的零点为正数, 所以只需考虑 $x\in(0,+\infty)$ 的情形. 又因为此时 $\log_{\frac12} x$ 单调递减, 而 $-\log_{\frac12} x$ 单调递增, 所以 $f(x)=x^2-\log_{\frac12} x$ 单调递增. 计算知, $f\biggl(\dfrac12\biggr)=-\dfrac34$, $f(1)=1$, 由零点存在性定理, 零点在区间 $\biggl(\dfrac12,1\biggl)$ 内.
</p>
</myremark>
</p>
<p><myexample>
<p>设函数 $f(x)= \begin{cases}
        x, & x< a,\\
        x^2, & x\geqslant a,
    \end{cases}$ 若对于任意实数 $b$, 关于 $x$ 的方程 $f(x)-b=0$ 总有实根, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由 $f(x)$ 的表达式可知, 其图形在 $(-\infty,a)$ 上为直线 $y=x$ 的一部分, 在 $[a,+\infty)$ 上为抛物线 $y=x^2$ 的一部分. 而方程 $f(x)-b=0$ 等价于 $f(x)=b$, 则 $a$ 的取值应使得 $y=f(x)$ 与 $y=b$ 的图形总有交点. 画图可知, 仅当 $a\in[0,1]$ 时满足题意.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1214-1920-crop}\qquad
        \includegraphics[scale=1]{2020-1214-1930-crop}\qquad
        \includegraphics[scale=1]{2020-1214-1940-crop}
    </center>
</p>
</mysolution>
</p>
<p><myexample>
<p>“$t\geqslant 0$”是“函数 $f(x)= x^2+tx-t$ 在 $(-\infty,+\infty)$ 内存在零点”的什么条件? 
</p>
</myexample>
<mysolution>
    <p>函数 $f(x)= x^2+tx-t$ 在 $(-\infty,+\infty)$ 内存在零点的充要条件是 $\Delta= t^2-4(-t)\geqslant 0$ 即 $t\in(-\infty,-4]\cup [0,+\infty)$, 所以“$t\geqslant 0$”是“函数 $f(x)= x^2+tx-t$ 在 $(-\infty,+\infty)$ 内存在零点”的充分不必要条件.
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \begin{cases}
        \dfrac1x, & x\geqslant 1,\\
        x^3, & x< 1,
    \end{cases}$ 若关于 $x$ 的方程 $f(x)=k$ 有两个不等的实根, 求 $k$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>此题与“2020 年 12 月 5 日答疑记录”的例 \ref{exa:201217-1900} 类似, 画图可知, $k\in(0,1)$.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1217-1900-crop}
    </center>
</p>
</mysolution>

