---
# bookCollapseSection: true
title: 二次函数
weight: 6
bookHidden: true
prevPage: /docs/algebra/function/function-graph
prevPageTitle: 函数的图象
nextPage: /docs/algebra/pow-exp-log
nextPageTitle: 幂函数、指数函数、对数函数
---

# 二次函数

<myexample>
<p>如图所示, 已知边长为 $8$ 米的正方形钢板有一个角被锈蚀, 其中 $AE=4$ 米, $CD=6$ 米. 为了合理利用这块钢板, 将在五边形 $ABCDE$ 内截取一个矩形 $BNPM$, 使点 $P$ 在边 $DE$ 上.
</p>
<p>(1) 设 $MP=x$ 米, $PN=y$ 米, 将 $y$ 表示成 $x$ 的函数, 并求其定义域;
</p>
<p>(2) 求矩形 $BNPM$ 面积 $S$ 的取值范围.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1240-crop}
    </center>
</p>
<p></p>
</myexample>
<mysolution>
    <p>(1) 由题意, $\triangle DHP\backsim \triangle DEF$, 所以
    \[\frac{DH}{HP}= \frac{DF}{FE},\quad\text{即}\quad
        \frac{y-6}{8-x}= \frac{2}{4}.\]
    整理得, $y=\dfrac{20-x}2$, 且由图可知 $x\in[4,8]$.
</p>
<p>(2) 由 (1) 得, 
    \[S= xy= \frac12 x(20-x)\quad (\text{平方米}),\]
    且在 $[4,8]$ 上单调递增, 所以 $S\in[16,24]$ (平方米).
</p>
</mysolution>

<myexample>
<p>如图, 有一直角墙角, 两边的长度足够长, 在点 $P$ 处有一棵树与两墙的距离分别是 $a$\,m ($0< a< 12$) 和 $4$\,m, 不考虑树的粗细. 现在想用 $16$\,m 长的篱笆, 借助墙角围成一个矩形的花圃 $ABCD$, 且将这棵树围在花圃内. 设此矩形花圃的最大面积为 $S= f(a)$ (单位: m$^2$), 则该函数的图形大致为 (\qquad).
</p>
<p>\begin{minipage}[c]{0.3\textwidth}
    <center>
        \includegraphics[scale=1]{2020-1208-1920-crop}
    </center>
    \end{minipage}
    \begin{minipage}[c]{0.7\textwidth}
        \small\centering
        \begin{tikzpicture}[scale=0.7]
          \draw[\myaxisarrow] (-0.7,0) -- (4,0) node[below] {$a$};
          \draw[\myaxisarrow] (0,-0.7) -- (0,3) node[left] {$S$};
          \draw (0,0) node[anchor=45] {$O$};
</p>
<p>\draw[line width=0.5pt] (0,2) -- (3,2);
          \draw (1.75,-1) node {(A)};
        \end{tikzpicture}\qquad
        \begin{tikzpicture}[scale=0.7]
          \draw[\myaxisarrow] (-0.7,0) -- (4,0) node[below] {$a$};
          \draw[\myaxisarrow] (0,-0.7) -- (0,3) node[left] {$S$};
          \draw (0,0) node[anchor=45] {$O$};
</p>
<p>\draw[line width=0.5pt,smooth,samples=100,domain=0:3] 
            plot(\x,{-(\x)^2 / 3 + 0.75*\x + 1.5});
          \draw (1.75,-1) node {(B)};
        \end{tikzpicture}\\
        \begin{tikzpicture}[scale=0.7]
          \draw[\myaxisarrow] (-0.7,0) -- (4,0) node[below] {$a$};
          \draw[\myaxisarrow] (0,-0.7) -- (0,3) node[left] {$S$};
          \draw (0,0) node[anchor=45] {$O$};
</p>
<p>\draw[line width=0.5pt] (0,2) -- (2,2);
          \draw[line width=0.5pt,smooth,samples=100,domain=1.98:3] 
            plot(\x,{-(\x)^2 / 3 + 0.75*\x + 1.83});
          \draw (1.75,-1) node {(C)};
        \end{tikzpicture}\qquad
        \begin{tikzpicture}[scale=0.7]
          \draw[\myaxisarrow] (-0.7,0) -- (4,0) node[below] {$a$};
          \draw[\myaxisarrow] (0,-0.7) -- (0,3) node[left] {$S$};
          \draw (0,0) node[anchor=45] {$O$};
</p>
<p>\draw[line width=0.5pt,smooth,samples=100,domain=0:3] 
            plot(\x,{-(3 - \x)^2 / 3 + 0.75*(3 - \x) + 1.5});
          \draw (1.75,-1) node {(D)};
        \end{tikzpicture}
    \end{minipage}
</p>
<p></p>
</myexample>
<mysolution>
    <p>设 $AB=x$\,m, 则 $CD=(16-x)$\,m. 因为矩形 $ABCD$ 要围住点 $P$, 所以
    \[\left\{\!\!\begin{array}{l}
        AD\geqslant a,\\
        DC\geqslant 4,
      \end{array}\right.\ \text{即}\quad
      \left\{\!\!\begin{array}{l}
        x\geqslant a,\\
        16-x\geqslant 4, 
      \end{array}\right.\ \text{解得}\quad
      x\in[a,12].\]
    设矩形 $ABCD$ 的面积为 $g(x)$, 则 $g(x)=x(16-x)$, $ x\in[a,12]$. 易知 $g(x)$ 是二次函数, 其 (完整) 图形的对称轴为 $x=8$. 由此可知,
</p>
<p>(1) 若 $0< a\leqslant 8$, 则 $g_{\max}= g(8)= 64$, 即 $S=f(a)=64$;
</p>
<p>(2) 若 $a>8$, 则 $g_{\max}= g(a)= a(16-a)$, 即 $S=f(a)=a(16-a)$.
</p>
<p>画出 $f(a)$ 对应的图形可知, 大致为 (C).
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= x^2+ax-b$, 正数 $a$, $b$ 满足 $a+\dfrac4b\leqslant 3$. 若对任意的 $x\in[1,+\infty)$, $f(x)\geqslant 0$ 恒成立, 求 $a$, $b$ 的值.
</p>
</myexample>
<mysolution>
    <p>由题意, 在 $[1,+\infty)$ 上 $f_{\min}\geqslant 0$. 因为 $a$ 为正数, $f(x)$ 的图形的对称轴为 $x=-\dfrac{a}2< 0$ 且图形开口向上, 所以此时 $f_{\min}=f(1)=1+a-b$. 因此
    \[\left\{\!\!\begin{array}{l}
        a+\dfrac4b\leqslant 3,\\
        1+a-b\geqslant 0,
      \end{array}\right.\ \text{即}\quad
      \left\{\!\!\begin{array}{l}
        a\leqslant 3-\dfrac4b,\\
        a\geqslant b-1.
      \end{array}\right.\]
    由不等式的传递性, 
    \[3-\frac4b\geqslant b-1,\quad\text{移项整理得}\quad
    0\geqslant (b-2)^2.\]
    因为 $(b-2)^2\geqslant 0$ 恒成立, 所以只能 $(b-2)^2=0$, 即 $b=2$. 回代可知 $a=2$, 所以 $a=b=2$.
</p>
</mysolution>

<p>恒成立问题一般化为值域问题来求解. 例如, 设 $D$ 为函数 $f(x)$ 的定义域, 则
\[\begin{gathered}
    \forall\, x\in D, f(x)\leqslant m\Leftrightarrow f_{\max}\leqslant m,\\
    \forall\, x\in D, f(x)\geqslant m\Leftrightarrow f_{\min}\geqslant m.
\end{gathered}\]
</p>
