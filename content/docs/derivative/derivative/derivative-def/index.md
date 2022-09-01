---
# bookCollapseSection: true
title: 导数的定义与意义
weight: 1
bookHidden: true
prevPage: /docs/derivative/derivative
prevPageTitle: 导数
nextPage: /docs/derivative/derivative/derivative-calc
nextPageTitle: 常见导数公式
---

# 导数的定义与意义


<p>导数的定义、公式等知识点, 可以参看基础练习第 12 节“导数的定义和计算”以及第 13 节“导数的意义”. 这里简要回顾导数的定义和函数图形的切线求法, 并补充少量极限知识.
</p>
<p>函数 $f(x)$ 的导函数 (简称导数) $f'(x)$ 定义为 \[
    f'(x)=\lim_{x_1\to x} \frac{f(x_1)-f(x)}{x_1-x}
    = \lim_{\Delta x\to 0} \frac{f(x+\Delta x)-f(x)}{\Delta x},\]
式中 $\Delta x= x_1- x$. 导数 $f'(x)$ 的几何含义是曲线 $y=f(x)$ 在点 $P(x,f(x))$ 处切线的斜率, 也是割线 $PQ$ 斜率当点 $Q$ 沿曲线 $y=f(x)$ 趋于点 $P$ 时的极限值.
</p>
<p><center>
  \small
  \centering
  \begin{tikzpicture}[line cap=round,line join=round,scale=0.5]
    \draw[\myaxisarrow] (-1.5,0) -- (4,0) node[below] {$x$};
    \draw[\myaxisarrow] (0,-1) -- (0,6) node[left] {$y$};
    \draw[line width=0.5pt,smooth,samples=100] 
      plot[domain=-0.5:3.8](\x,{(\x)^2/3+1});
    \draw[line width=0.6pt,smooth,samples=100] 
      plot[domain=-0.5:3.3](\x,{(2*\x+2)/3});
    \draw[line width=0.4pt,smooth,samples=100,densely dashed] 
      plot[domain=-0.5:3.8](\x,{3*\x/2-1/6});
    \draw (0,0) node[anchor=north west] {$O$}
      (1,1) node[right] {$P(x,y)$}
      (3.5,{61/(12)}) node[right] {$Q(x_1,y_1)$};
  \end{tikzpicture}
</center>
</p>
<p>利用定义计算基本初等函数的导数时, 常用定义中的后一式. 例如求函数 $f(x)=x^2$ 和 $g(x)= \dfrac1x$ 的导数时, \[\begin{gathered}
    \frac{f(x+\Delta x)-f(x)}{\Delta x}
    = \frac{1}{\Delta x}[(x+\Delta x)^2-x^2]
    = 2x+\Delta x,\\
    \frac{g(x+\Delta x)-g(x)}{\Delta x}
    = \frac{1}{\Delta x}\biggl(\frac1{x+\Delta x}- \frac1x\biggr)
    = -\frac1{x(x+\Delta x)},
\end{gathered}\]
则令 $\Delta x\to 0$ 可得 $f'(x)=2x$, $g'(x)= -\dfrac1{x^2}$, 即
    \[(x^2)'=2x,\quad (x^{-1})'=-x^{-2}.\]
从前面的计算也可以看出, 虽然导数定义中分母看似含“零因子”$\Delta x$, 但是均可在计算中或求极限时消去, 因为此时分子中也有与 $\Delta x$ 同时趋于 $0$ 的因子.
</p>
<p>设曲线 $C\colon y=f(x)$, 则 $C$ 上点 $x_0$ 处切线的斜率 $k=f'(x_0)$, 而切线的方程为 
\[y-f(x_0)= f'(x_0)(x-x_0).\]
上式表明, 函数的解析式和切点的横坐标决定了切线的方程. 在解切线相关问题时, 应先设出切点, 并列出导数, 再利用切点同时在曲线和切线上解题.
</p>
<p>高中数学中的函数基本都是连续函数 (图形不间断), 所以极限式 $\lim\limits_{x\to x_0} f(x)$ 的值可以理解为 $f(x_0)$, 如 \[
    \lim_{x\to 1} x^2= 1^2= 1,\quad
    \lim_{x\to 2} \ln x= \ln 2.\]
因此容易看出, \[\begin{gathered}
    \lim_{x\to x_0} [f(x)+ g(x)]= f(x_0)+g(x_0),\\
    \lim_{x\to x_0} C\cdot f(x)= C\cdot f(x_0),
\end{gathered}\]
式中 $C$ 为常数.
</p>
<p>\subsection{导数的应用}
</p>
<p><myexample>
<p>已知直线 $y=kx$ 是曲线 $y=\mathrm{e}^x$ 的切线, 求实数 $k$ 的值.
</p>
</myexample>
<mysolution>
    <p>函数 $y=\mathrm{e}^x$ 的导数为 $y'=\mathrm{e}^x$. 设题中切点为 $(x_0,y_0)$, 则由切点同时在曲线 $y=\mathrm{e}^x$ 和切线 $y=kx$ 上可知, \[
        y_0= kx_0= \mathrm{e}^{x_0},\]
    再利用切线的斜率为导数值, $k= \mathrm{e}^{x_0}$, 代入上式得 $x_0=1$. 所以 $k= \mathrm{e}$.
</p>
</mysolution>
</p>
<p><myexample>
<p>对下列函数, \[
        f_1(x)= \frac1x,\quad
        f_2(x)= x^4,\quad
        f_3(x)= \cos x,\quad
        f_4(x)= \ln x,\]
    哪些函数的图形在某点处的切线与直线 $y= \dfrac12 x+b$ 平行?
</p>
</myexample>
<mysolution>
    <p>由题意, 只需判断各函数的导数值是否可以取 $\dfrac12$. 因为 \[
        f_1'(x)= -\frac1{x^2},\quad
        f_2'(x)= 4x^3,\quad
        f_3'(x)= -\sin x,\quad
        f_4'(x)= \frac1x,\]
    所以分别解方程可知, $f_2(x)$, $f_3(x)$, $f_4(x)$ 满足题意.
</p>
</mysolution>
</p>
<p><myexample>
<p>设曲线 $y= \mathrm{e}^x$ 在点 $(0,1)$ 处的切线 $l_1$ 与曲线 $y= \dfrac1x\ (x>0)$ 在点 $P$ 处的切线 $l_2$ 垂直, 求 $l_2$ 的方程.
</p>
</myexample>
<mysolution>
    <p>$y= \mathrm{e}^x$ 的导数为 $y'= \mathrm{e}^x$, 所以其在点 $(0,1)$ 处的切线 $l_1$ 的斜率为 $\mathrm{e}^0= 1$. 由 $l_1\perp l_2$ 知, $l_2$ 的斜率为 $-1$. 设 $P(x_0,y_0)$, 由 $y= \dfrac1x$ 的导数为 $y'= -\dfrac1{x^2}$ 知, 其在点 $P$ 处的切线 $l_2$ 的斜率为 $-\dfrac1{x_0^2}$, 所以结合 $x>0$ 知, \[
        -\dfrac1{x_0^2}= -1,\quad x_0= 1.\]
    因此 $P(1,1)$, 切线 $l_2$ 的方程为 \[
        y-1= (-1)\cdot(x-1) \Rightarrow x+y-2=0.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)$ 在 $x=x_0$ 处的导数为 $12$, 求值: \[
        \lim_{\Delta x\to 0} \frac{f(x_0+\Delta x)- f(x_0)}{2\Delta x}.\]
</p>
</myexample>
<mysolution>
    <p>由导数的定义, \[
        \lim_{\Delta x\to 0} \frac{f(x_0+\Delta x)- f(x_0)}{\Delta x}
        = 12,\]
    结合极限的性质, \[
        \lim_{\Delta x\to 0} \frac{f(x_0+\Delta x)- f(x_0)}{2\Delta x}
        = 6.\]
</p>
</mysolution>
