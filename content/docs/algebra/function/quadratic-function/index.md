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

<myexample>
<p>已知某二次函数满足: 当 $x=2$ 时, $y=-1$; 当 $x=-1$ 时, $y=-1$, 且最大值为 $8$, 求此二次函数的解析式.
</p>
</myexample>
<mysolution>
    <p>方法一(通用解法): 设此二次函数的解析式为 $f(x)=Ax^2+Bx+C$. 由题意, $f(2)=f(-1)=-1$, $A< 0$ 且顶点纵坐标 $\dfrac{4AC-B^2}{4A}=8$. 解前述方程可得答案.
</p>
<p>方法二(特殊解法): 由题意, 点 $(2,-1)$, $(-1,-1)$ 均在二次函数图象上, 而这两个点纵坐标相同, 所以图象的对称轴为 $x=\dfrac{2+(-1)}2=\dfrac12$. 再由二次函数最大值为 $8$, 可直接设顶点式 $f(x)=A\biggl(x-\dfrac12\biggr)^2+8$, 再把点 $(2,-1)$ 代入, 可解得 $A$ 的值.
</p>
</mysolution>
</p>
<p></p>
<p>\begin{example}\label{exa:201026-2120}
  已知二次函数 $y=-x^2+2ax+1-a$ 当 $0\leqslant x\leqslant 1$ 时有最大值 $2$, 求 $a$ 的值.
</p>
</myexample>
<mysolution>
    <p>函数 $y=-x^2+2ax+1-a$ 图象的对称轴为 $x=a$, 且开口向下.
</p>
<p>(1) 当 $a\leqslant 0$ 时, $y_{\max}= y(0)$ 即 $2=1-a$, 解得 $a=-1$.
</p>
<p>(2) 当 $0< a\leqslant 1$ 时, $y_{\max}= y(a)$ 即 $2=a^2+1-a$, 解得 $a=\dfrac{-1\pm\sqrt5}2$. 因为 $\sqrt5\approx 2.236$, 所以 $a\approx 0.618$ 或 $-1.618$. 由 $0< a\leqslant \dfrac12$ 知, $a=\dfrac{\sqrt5-1}2$.
</p>
<p>(3) 当 $a>1$ 时, $y_{\max}= y(1)$ 即 $2=a$, 所以 $a=2$.
</p>
<p>综上所述, $a=-1$, $\dfrac{\sqrt5-1}2$ 或 $2$.
</p>
</mysolution>
<myremark>
    <p>(1) 一般二次函数的值域讨论, 有四种情形. 但例 \ref{exa:201026-2120} 中只考虑最大值, 且图象开口向下, 所以可以精简为三种情形 (轴在定义域内的两种情形并为一种).
</p>
<p>(2) 建议记住三个常用的算术平方根的近似值: $\sqrt2\approx 1.414$, $\sqrt3\approx 1.732$, $\sqrt5\approx 2.236$. 如果未记住 $\sqrt5$ 的近似值, 也可估计 $\sqrt5\in(2,3)$, 然后对所的式子进一步估值 (如例 \ref{exa:201026-2120} (2) 中的式子).
</p>
</myremark>
</p>
<p>\begin{example}\label{exa:201026-2130}
  设二次函数 $y=\dfrac12 x^2-x-\dfrac12$, 若当 $-1\leqslant x\leqslant m$ 时, $-1\leqslant y\leqslant m$, 求 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>函数 $y=\dfrac12 x^2-x-\dfrac12$ 图象开口向上, 对称轴为 $x=1$. 由题意, $m\geqslant -1$.
</p>
<p>方法一: (1) 当 $-1\leqslant m\leqslant 1$ 时, 
  \[\left\{\!\!\begin{array}{l}
    y_{\min}= y(m),\\
    y_{\max}= y(-1),
    \end{array}\right.\ \text{即}
    \left\{\!\!\begin{array}{l}
    -1= \dfrac12 m^2-m-\dfrac12,\\
    m= 1,
    \end{array}\right.\]
  解得 $m=1$.
</p>
<p>(2) 当 $1< m\leqslant 3$ 时, 
  \[\left\{\!\!\begin{array}{l}
    y_{\min}= y(1),\\
    y_{\max}= y(-1),
    \end{array}\right.\ \text{即}
    \left\{\!\!\begin{array}{l}
    -1= -1,\\
    m= 1,
    \end{array}\right.\]
  解得 $m=1$ (舍).
</p>
<p>(3) 当 $m>3$ 时, 
  \[\left\{\!\!\begin{array}{l}
    y_{\min}= y(1),\\
    y_{\max}= y(m),
    \end{array}\right.\ \text{即}
    \left\{\!\!\begin{array}{l}
    -1= -1,\\
    m= \dfrac12 m^2-m-\dfrac12,
    \end{array}\right.\]
  解得 $m=2\pm\sqrt3$. 由 $m>3$ 知 $m=2+\sqrt3$.
</p>
<p>综上所述, $m=1$ 或 $\dfrac{2+\sqrt3}2$.
</p>
<p>方法二: 因为 
  \[y=\frac12 x^2-x-\frac12= \frac12(x-1)^2-1,\]
  所以由 $-1\leqslant y\leqslant m$ 知 $m\geqslant 1$. 可以只讨论 $1\leqslant m\leqslant 3$ 和 $m>3$ 两种情形. 具体计算同方法一.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201026-2130} 仍为常见的求值域问题, 只需注意将定义域与对应的值域和题中的范围对比. 


<myexample>
<p>已知二次函数 $y= x^2-2ax+1$, 当 $2< x< 3$ 时, 函数值 $y$ 随 $x$ 的增大而减小, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>$y= x^2-2ax+1$ 的图象为开口向上的抛物线, 对称轴为 $x= -\dfrac{-2a}{2\cdot 1}= a$. 由题意, 当 $2< x< 3$ 时, $x$ 在对称轴的左侧, 所以 $3\leqslant a$, 即 $a\in [3,+\infty)$.
</p>
</mysolution>
<myremark>
    <p>(1) 二次函数 $y= Ax^2+Bx+C$ ($A\neq 0$) 的单调性可以通过观察其图象 (抛物线) 的开口方向 (由 $A$ 的正负号决定) 和对称轴 $x= -\dfrac{B}{2A}$ 的位置得出.
</p>
<p>(2) 写二次函数的对称轴时, 只需按照公式的格式写出对应的式子 (见解答第 1 行), 无需明确地写出公式. 如果对称轴容易口算, 也可直接写出, 如本题可直接写“对称轴为 $x= a$”.
</p>
</myremark>
</p>
<p><myexample>
<p>对二次函数 $y=x^2-2x+2$, 当 $t\leqslant x\leqslant t+1$ 时, 求函数值 $y$ 的最大值与最小值.
</p>
</myexample>
<mysolution>
    <p>$y=x^2-2x+2= (x-1)^2+1$ 的图象为开口向上的抛物线, 对称轴为 $x=1$. 下面考虑定义域与对称轴的相对位置, 再确定对应函数值的最大 (小) 值.
</p>
<p>(1) 若 $t+1\leqslant 1$ 即 $t\leqslant 0$, 则当 $x=t$ 时, $y=t^2-2t+2$ 为最大值; 当 $x=t+1$ 时, $y=t^2+1$ 为最小值.
</p>
<p>(2) 若 $\dfrac{t+(t+1)}2\leqslant 1< t+1$ 即 $0< t\leqslant \dfrac12$, 则当 $x=t$ 时, $y=t^2-2t+2$ 为最大值; 当 $x=1$ 时, $y=1$ 为最小值.
</p>
<p>(3) 若 $t\leqslant 1< \dfrac{t+(t+1)}2$ 即 $\dfrac12< t\leqslant 1$, 则当 $x=t+1$ 时, $y=t^2+1$ 为最大值; 当 $x=1$ 时, $y=1$ 为最小值.
</p>
<p>(4) 若 $1< t$ 即 $t> 1$, 则当 $x=t+1$ 时, $y=t^2+1$ 为最大值; 当 $x=t$ 时, $y=t^2-2t+2$ 为最小值.
</p>
<p>下图为情形 (1) (2) 对应的示意图:
</p>
<p><center>
  \includegraphics{2020-1007-1710-crop}
  </center>
</p>
</mysolution>
<myremark>
    <p>(1) 除了直接用公式, 二次函数的对称轴也可以通过配方得出, 如解答第 1 行.
</p>
<p>(2) 求二次函数部分图像的最大 (小) 值, 需要考虑定义域与对称轴的相对位置, 共四种: 对称轴在定义域右侧 (情形 (1)); 对称轴在定义域内偏右 (情形 (2)); 对称轴在定义域内偏左 (情形 (3)); 对称轴在定义域左侧 (情形 (4)), 其中情形 (2) (3) 均需考虑定义域的中点.
</p>
<p>(3) 分类讨论时需注意“不重不漏”, 且应明确写出参数的范围 (如各种情形的第 1 行).
</p>
</myremark>

<p>\subsection{二次函数的值域 (取值范围)}
</p>
<p>求关于 $x$ 的二次函数 $f(x)= Ax^2+Bx+C$ ($A\neq 0$) 的值域时需利用定义域 ($x$ 的取值范围) 和单调性 (从左往右观察其图象时, 图象是上升还是下降), 而该函数的单调性可以通过观察其图象 (抛物线) 的开口方向和对称轴的位置得出, 其中由 $A$ 的正负号决定, 对称轴的公式为 $x= -\dfrac{B}{2A}$. 注意, 写对称轴时, 只需按照公式的格式写出对应的式子, 无需明确地写出公式. 如果对称轴容易口算, 也可直接写出, 如函数 $f(x)= x^2-2ax+1$ 的对称轴为 $x= a$.
</p>
<p>具体地, 对二次函数 $y=f(x)= Ax^2+Bx+C$ ($A\neq 0$), 其中 $x\in[m,n]$, 参考下图 (为方便起见, 图中故意将不同定义域对应的函数图象画得与原图象分离)
</p>
<p><center>
  \includegraphics[scale=2.5]{2020-1018-0900-crop}
  </center>
</p>
<p>(仅列出开口向上即 $A>0$ 的情形, 开口向下的情形结论类似)
</p>
<p>(1) 若对称轴在定义域右侧, 即 $n\leqslant -\dfrac{B}{2A}$, 则
\[y_{\min}=f(n),\quad y_{\max}=f(m),\]
即 $y\in[f(n), f(m)]$;
</p>
<p>(2) 若对称轴在定义域内部偏右, 即 $\dfrac{m+n}2\leqslant -\dfrac{B}{2A}< n$, 则
\[y_{\min}=f\biggl(-\dfrac{B}{2A}\biggr),\quad y_{\max}=f(m),\]
即 $y\in\biggl[f\biggl(-\dfrac{B}{2A}\biggr), f(m)\biggr]$;
</p>
<p>(3) 若对称轴在定义域内部偏左, 即 $m\leqslant -\dfrac{B}{2A}< \dfrac{m+n}2$, 则
\[y_{\min}=f\biggl(-\dfrac{B}{2A}\biggr),\quad y_{\max}=f(n),\]
即 $y\in\biggl[f\biggl(-\dfrac{B}{2A}\biggr), f(n)\biggr]$;
</p>
<p>(4) 若对称轴在定义域左侧, 即 $-\dfrac{B}{2A}< m$, 则
\[y_{\min}=f(m),\quad y_{\max}=f(n),\]
即 $y\in[f(m), f(n)]$.
</p>
<p>讨论时应注意“不重不漏”(不重复且不遗漏). 实际解题时, 不用写得很详细, 只写主要步骤即可, 见下一小节的例子.
</p>
<p>\subsection{含参数的二次函数的值域}
</p>
<p>一般遇到的二次函数值域问题, 有时函数表达式含参数 (代表已知数的字母, 但取值不固定), 有时定义域含参数, 偶尔两者兼有. 无论哪种情形, 都可以用上一小节的结论来解题, 即“看图说话”.
</p>
<p>\begin{example}\label{exa:201018-1010}
  已知二次函数 $f(x)=x^2$, $x\in[-1,a)$, 求 $f(x)$ 的值域.
</p>
</myexample>
<mysolution>
    <p>由题意, $a>-1$, 故考虑 $a$ 从 $-1$ 开始不断增大时, 定义域与对称轴 $x=0$ 的位置关系.
</p>
<p>(1) 若 $-1< a\leqslant 0$, 则 $f(x)\in(f(a),f(-1)]= (a^2,1]$;
</p>
<p>(2) 若 $0< a\leqslant 1$, 则 $f(x)\in[f(0),f(-1)]= [0,1]$;
</p>
<p>(3) 若 $a> 1$, 则 $f(x)\in[f(0),f(a))= [0,a^2)$.
</p>
<p>综上所述,
  \[f(x)\in\begin{cases}
    (a^2,1], & a\in(-1,0],\\
    [0,1],   & a\in(0,1],\\
    [0,a^2), & a\in(1,+\infty).
    \end{cases}\]
</p>
</mysolution>
<myremark>
    <p>(1) 例 \ref{exa:201018-1010} 只有上一小节的结论中 (1)---(3), 且容易看出对称轴在定义域正中间的时候, $a=1$, 所以按 $a\in(-1,0]$, $(0,1]$, $(1,+\infty]$ 三种情况讨论.
</p>
<p>(2) 最后的结论可以写为分段的形式, 方便查看, 其中大括号后先写值域, 再写参数范围; 也直接罗列 (见例 \ref{exa:201018-1100}).
</p>
</myremark>
</p>
<p>讨论时, 既可以将对称轴视为运动的, 也可以将定义域视为运动的. 一般建议将含参数的部分视为运动的. 在不熟悉解题过程之前, 解题时应画草图帮助思考.
</p>
<p>\begin{example}\label{exa:201018-1100}
  已知二次函数 $f(x)=x^2-2x+2$, $x\in[t,t+1]$, 求 $f(x)$ 的值域.
</p>
</myexample>
<mysolution>
    <p>$f(x)$ 的对称轴为 $x=1$, 考虑其与定义域的位置可知
</p>
<p>(1) 若 $t+1\leqslant 1$ 即 $t\leqslant 0$, 则 
  \[f(x)\in[f(t+1),f(t)]= [t^2+1,t^2-2t+2];\]
</p>
<p>(2) 若 $\dfrac{t+(t+1)}2\leqslant 1< t+1$ 即 $0< t\leqslant \dfrac12$, 则 
  \[f(x)\in[f(1),f(t)]= [1,t^2-2t+2];\]
</p>
<p>(3) 若 $t\leqslant 1\leqslant \dfrac{t+(t+1)}2$ 即 $\dfrac12< t\leqslant 1$, 则 
  \[f(x)\in[f(1),f(t+1)]= [1,t^2+1];\]
</p>
<p>(4) 若 $t> 1$, 则 
  \[f(x)\in[f(t),f(t+1)]= [t^2-2t+2,t^2+1].\]
</p>
<p>综上所述, 若 $t\in(-\infty,0]$, 则 $f(x)\in[t^2+1,t^2-2t+2]$; 
</p>
<p>若 $t\in\biggr(0,\dfrac12\biggr]$, 则 $f(x)\in[1,t^2-2t+2]$;
</p>
<p>若 $t\in\biggr(\dfrac12,1\biggr]$, 则 $f(x)\in[1,t^2+1]$; 
</p>
<p>若 $t\in (1,+\infty)$, 则 $f(x)\in[t^2-2t+2,t^2+1]$.
</p>
</mysolution>
</p>
<p>熟悉以上解题步骤后, 可以直接脑补草图, 并根据对称轴与定义域 (及其中点) 的位置关系写解题过程.
</p>
<p><myexample>
<p>已知二次函数 $f(x)=x^2-2ax-1$ ($a\in\realnum$), $x\in[0,2]$, 求 $f(x)$ 的值域.
</p>
</myexample>
<mysolution>
    <p>$f(x)$ 的对称轴为 $x=a$, 故
</p>
<p>(1) 若 $a\leqslant 0$, 则 
  \[f(x)\in[f(0),f(2)]= [-1,3-4a];\]
</p>
<p>(2) 若 $0< a\leqslant 1$, 则 
  \[f(x)\in[f(a),f(2)]= [-a^2-1,3-4a];\]
</p>
<p>(3) 若 $1< a \leqslant 2$, 则 
  \[f(x)\in[f(a),f(0)]= [-a^2-1,-1];\]
</p>
<p>(4) 若 $a> 2$, 则 
  \[f(x)\in[f(2),f(0)]= [3-4a,-1].\]
</p>
<p>综上所述, 
  \[f(x)\in\begin{cases}
    [-1,3-4a],     & a\in(-\infty,0],\\
    [-a^2-1,3-4a], & a\in (0,1],\\
    [-a^2-1,-1],   & a\in (1,2],\\
    [3-4a,-1],     & a\in (2,+\infty).
  \end{cases}\]
</p>
</mysolution>

<myexample>
<p>设 $a>0$, 函数 $f(x)= ax^2+bx+c$ 的图形关于直线 $x=1$ 对称, 比较 $f(0)$, $f(1)$, $f(\sqrt2)$, $f(\sqrt3)$ 的大小.
</p>
</myexample>
<mysolution>
    <p>由二次函数的单调性可知, 只需考虑 $0$, $1$, $\sqrt2$, $\sqrt3$ (横坐标) 到 $1$ (对称轴) 的距离. 因为
    \[\sqrt2\approx 1.414,\quad \sqrt3\approx 1.732,\]
    结合二次函数大致图形可知
    \[f(1)< f(\sqrt2)< f(\sqrt3)< f(0).\]
</p>
</mysolution>
