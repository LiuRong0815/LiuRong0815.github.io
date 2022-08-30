---
# bookCollapseSection: true
title: 对数函数
weight: 4
bookHidden: true
prevPage: /docs/algebra/pow-exp-log/logarithm-calculation
prevPageTitle: 对数运算
nextPage: /docs/algebra/pow-exp-log/composite-inverse
nextPageTitle: 复合函数与反函数
---

# 对数函数

<myexample>
<p>若函数 $y=\log_a x$ ($a>0$ 且 $a\neq 1$) 的图形过点 $(3,1)$, 求 $\log_2 3 \cdot f(8)$ 的值.
</p>
</myexample>
<mysolution>
    <p>将 $(3,1)$ 代入 $y=\log_a x$ 得 $1= \log_a 3$, 所以 $a=3$,
    \[\log_2 3 \cdot f(8)= \log_2 3\cdot \log_3 8
        = \frac{\ln 3}{\ln 2}\cdot\frac{\ln 8}{\ln 3}
        = \frac{3\ln 2}{\ln 2}= 3.\]
</p>
</mysolution>

<myexample>
<p>设 $a= 2^{-\frac13}$, $b=\log_2\dfrac13$, $c= \log_{\frac12}\dfrac13$, 比较这三者的大小.
</p>
</myexample>
<mysolution>
    <p>分别考虑函数 $f(x)= 2^x$, $g(x)= \log_2 x$, $h(x)= \log_{\frac12} x$ 的单调性, 可知 
    \[\begin{gathered}
        a= f\biggl(-\dfrac13\biggr)\in (0,1),\quad 
        b= g\biggl(\dfrac13\biggr)\in (-\infty,0),\\
        c= h\biggl(\dfrac13\biggr)\in (1,+\infty),
    \end{gathered}\]
    所以 $b< a< c$.
</p>
</mysolution>
</p>
<p>上述两个例题中的解法是对数、指数式比较大小时常用的方法, 分别为“化同底”和“先与 $0$, $1$ 比”.

<p>对数函数 $y= \log_a x$ ($x$, $a>0$ 且 $a\neq 1$) 的大致图形如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1050-crop}\qquad
        \includegraphics[scale=1]{2020-1206-1100-crop}
    </center>
</p>
<p>由图可知, 对数函数 $y= \log_a x$ 的特征有
</p>
<p>(1) 当 $0< a< 1$ 时, 函数单调递减; 当 $a>1$ 时, 函数单调递增;
</p>
<p>(2) 恒过点 $(1,0)$ (因为 $\log_a 1=0$), 且以 $y$ 轴为渐近线.
</p>
<p><myremark>
    <p>(1) 指数函数 $y= a^x$ 的定义域为 $\realnum$, 即对 $x$ 没有限制, 而对数函数 $y= \log_a x$ 的自然定义域是 $(0,+\infty)$.
</p>
<p>(2) 幂函数 $y= x^a$ 中自变量 $x$ 为底数, 指数函数 $y= a^x$ 中自变量 $x$ 为指数. 
</p>
</myremark>

\begin{example}\label{exa:201209-1910}
    已知 $0< a< 1$, $\log_a m< \log_a n< 0$, 比较 $m$, $n$ 与 $1$ 的大小.
</p>
</myexample>
<mysolution>
    <p>由 $0=\log_a 1$ 知不等式化为 $\log_a m< \log_a n< \log_a 1$. 因为 $0< a< 1$, 所以对数函数 $f(x)= \log_a x$ 在 $(0,+\infty)$ 上单调递减, 则 $m>n>1$.
</p>
</mysolution>
<myremark>
    <p>若例 \ref{exa:201209-1910} 中的不等式“$\log_a m< \log_a n< 0$”改为“$\log_a m> \log_a n> 0$”, 则答案建议写为: $0< m< n< 1$ (即对数函数中的真数一定为正数).
</p>
</myremark>
</p>
<p><myexample>
<p>(1) 已知 $a$, $b\in\realnum$, 则“$a< b$”是“$\log_2 a< \log_2 b$”的什么条件?
</p>
<p>(2) 已知 $x\in\realnum$, 则“$x< 0$”是“$\ln(x+1)< 0$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>(1) 由例 \ref{exa:201209-1910} 的解答及注可知, $\log_2 a< \log_2 b$ 等价于 $0< a< b$, 所以“$a< b$”是“$\log_2 a< \log_2 b$”的必要不充分条件.
</p>
<p>(2) $\ln(x+1)< 0$ 等价于 $0< x+1< 1$ 即 $-1< x< 0$, 所以“$x< 0$”也是“$\ln(x+1)< 0$”的必要不充分条件
</p>
</mysolution>

<p>关于比较多个数的大小的一般方法, 可参考“2020 年 11 月 21 日答疑记录”末尾的说明.
</p>
<p><myexample>
<p>比大小: (1) $a=0.4^2$, $b=3^{0.4}$, $c=\log_4 0.3$;
</p>
<p>(2) $a=2^{1.2}$, $b=\biggl(\dfrac12\biggr)^{-0.8}$, $c=2\log_4 2$;
</p>
<p>(3) $a=\log_3 \mathrm{e}$, $b=\ln 3$, $c=\log_3 2$.
</p>
</myexample>
<mysolution>
    <p>(1) 分别考查函数 $f(x)=0.4^x$, $g(x)=3^x$, $h(x)=\log_4 x$ 的图形可知, $a=f(2)\in(0,1)$ (实际上 $a=0.16$), $b=g(0.4)\in(1,3)$, $c=h(0.3)\in(-\infty,0)$, 所以 $c< a< b$.
</p>
<p>(2) 分别考查函数 $f(x)=2^x$, $g(x)= \log_5 x$ 的图形可知, $a=f(1.2)\in(2,4)$, $b=2^{0.8}=f(0.8)\in(1,2)$, $c=\log_5 4=g(4)\in(0,1)$, 所以 $c< b< a$.
</p>
<p>(3) 分别考查函数 $f(x)=\log_3 x$, $g(x)=\ln x$ 的图形可知, $a=f(\mathrm{e})\in(0,1)$ (注意 $\mathrm{e}=2.718\cdots$), $b=g(3)\in(1,2)$ ($\ln x$ 的底数是 $\mathrm{e}$), $c=f(2)\in(0,1)$, 而 $f(2)< f(\mathrm{e})$, 所以 $c< a< b$.
</p>
</mysolution>

