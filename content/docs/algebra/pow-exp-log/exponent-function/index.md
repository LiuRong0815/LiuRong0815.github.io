---
# bookCollapseSection: true
title: 指数函数
weight: 2
bookHidden: true
prevPage: /docs/algebra/pow-exp-log/power-function
prevPageTitle: 幂函数
nextPage: /docs/algebra/pow-exp-log/logarithm-calculation
nextPageTitle: 对数运算
---

# 指数函数

<p>\begin{example}\label{exa:201201-2020}
    已知函数
    \[f(x)= \begin{cases}
        (4a-3)x+a+\dfrac12, & x< 0,\\
        a^x, & x\geqslant 0.
    \end{cases}\]
</p>
<p>(1) 若函数的图形经过点 $\biggl(3,\dfrac18\biggr)$, 求 $a$ 的值.
</p>
<p>(2) 若对任意的 $x_1\neq x_2$, 都有 $\dfrac{f(x_1)-f(x_2)}{x_1-x_2}< 0$ 成立, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 由题意, $f(3)= \dfrac18$ 即 $a^3=\dfrac18$, 所以 $a=\dfrac12$.
</p>
<p>(2) $\dfrac{f(x_1)-f(x_2)}{x_1-x_2}< 0$ 表明 $x_1$, $x_2$ 的大小关系与 $f(x_1)$, $f(x_2)$ 的大小关系恰好反过来 (即若 $x_1< x_2$, 则 $f(x_1)>f(x_2)$), 也就是 $f(x)$ 单调递减. 再由 $f(x)$ 的解析式知 (参考“2020 年 10 月 31 日答疑记录”的第三个例子)
    \[\left\{\!\!\begin{array}{l}
        4a-3< 0,\ 0< a< 1,\\
        a+\dfrac12\geqslant a^0,
        \end{array}\right.\ \text{解得}\quad 0< a< \frac12,\]
    所以 $a\in\biggl(0,\dfrac12\biggr)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201201-2020} 中 $\dfrac{f(x_1)-f(x_2)}{x_1-x_2}< 0$ 表明 $f(x)$ 单调递减, 类似的结论 (需理解并熟记) 还有
\[\begin{gathered}
    \dfrac{f(x_1)-f(x_2)}{x_1-x_2}>0
    \Leftrightarrow (f(x_1)-f(x_2))(x_1-x_2)>0
    \Leftrightarrow \text{$f(x)$ 单调递增,}\\
    \dfrac{f(x_1)-f(x_2)}{x_1-x_2}< 0
    \Leftrightarrow (f(x_1)-f(x_2))(x_1-x_2)< 0
    \Leftrightarrow \text{$f(x)$ 单调递减.}
\end{gathered}\]
</p>

<p>常用的幂 (指数) 的运算法则有 (以下均假设 $a>0$, $m$, $n\in\realnum$):
\[\begin{gathered}
    a^m\cdot a^n= a^{m+n},\quad \frac{a^m}{a^n}= a^{m-n},\quad 
        (a^m)^n= a^{mn},\quad (ab)^m= a^mb^m,\\
    a^0= 1,\quad a^{-n}= \frac1{a^n},\quad a^{\frac1m}=\sqrt[m]{a}.
    \end{gathered}\]
以上法则中, 前四个可以按 $m$, $n$ 为正整数记忆, 后三个可以由前三个得到. 最后两个可以简记为: 指数中的负号表示“取倒数”, 分数表示“开方”. 此外, 这些法则还可以嵌套使用, 比如
\[a^{-\frac1m}= \frac1{\sqrt[m]{a}},\quad
    a^{\frac{m}n}= (a^m)^\frac1n= \sqrt[n]{a^m}.\]
</p>
<p>常用的对数运算法则见“2020 年 11 月 8 日答疑记录”的第二部分.
</p>
<p><myexample>
<p>计算: 
    (1) $2\sqrt{3}\times 3\sqrt[3]{1.5}\times \sqrt[6]{12}$;\qquad
    (2) $32^{-\frac35}- \biggl(2\dfrac{10}{27}\biggr)^{-\frac23}+ 0.5^{-2}$.
</p>
</myexample>
<mysolution>
    <p>根据指数的运算法则,
    \[\begin{aligned}
        2\sqrt{3}\times 3\sqrt[3]{1.5}\times \sqrt[6]{12}
        &= 2\times 3^{\frac12}\times 3\times 
            \biggl(\frac32\biggr)^{\frac13}\times
            (2^2\times 3)^{\frac16}\\
        &= 2^{1-\frac13+\frac26}\times 3^{\frac12+1+\frac13+\frac16}\\
        &= 2\times 3^2= 18,\\
        32^{-\frac35}- \biggl(2\frac{10}{27}\biggr)^{-\frac23}+ 0.5^{-2}
        &= 2^{5\times(-\frac35)}+ \biggl(\frac{64}{27}\biggr)^{-\frac23}+ 2^{(-1)\times(-2)}\\
        &= 2^{-3}+ \frac{3^{3\times\frac23}}{2^{6\times\frac23}}+ 2^2\\
        &= \frac18- \frac9{16}+ 4= \frac{57}{16}.
    \end{aligned}\]
</p>
</mysolution>


</p>
<p>计算指数式, 一般先化为整数表示, 即小数化最简分数, 根式化分数指数, 同时注意分解质因数, 然后合并同底数的指数即可.
</p>


<p>指数函数 $y= a^x$ ($x\in\realnum$, $a>0$ 且 $a\neq 1$) 的大致图形如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1030-crop}\qquad
        \includegraphics[scale=1]{2020-1206-1040-crop}
    </center>
</p>
<p>由图可知, 指数函数 $y= a^x$ 的特征有
</p>
<p>(1) 当 $0< a< 1$ 时, 函数单调递减; 当 $a>1$ 时, 函数单调递增;
</p>
<p>(2) 恒过点 $(0,1)$ (因为 $a^0=1$), 且以 $x$ 轴为渐近线.
</p>

