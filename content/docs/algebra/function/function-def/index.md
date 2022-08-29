---
# bookCollapseSection: true
title: 函数的定义
weight: 1
bookHidden: true
prevPage: /docs/algebra/function
prevPageTitle: 函数的定义、性质与图象
nextPage: /docs/algebra/function/function-monotone
nextPageTitle: 函数的单调性
---

# 函数的定义


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

<p>本次答疑主要讲解常见的定义域的求法. 如果没有特殊说明, 函数的定义域是使函数的表达式有意义的自变量的取值范围. 现阶段常见的表达式对其中的变量限制如下:
\[\begin{aligned}
    \text{二次根式 $\sqrt{x}$}&\colon \text{被开方数非负, 即 $x\geqslant 0$;}\\
    \text{分式 $\dfrac1{x}$}&\colon \text{分母不为零, 即 $x\neq 0$;}\\
    \text{零次式 $x^0$}&\colon \text{底数不为零, 即 $x\neq 0$,}
\end{aligned}\]
其中的零次式 $x^0$ 定义为 $\dfrac{x}x$, 所以需要限制 $x\neq 0$. 这些限制可以组合使用, 如对 $\dfrac1{\sqrt{x}}$, 应限制
\[\begin{cases}
    \sqrt{x}\neq 0 & (\text{分母不为零}),\\
    x\geqslant 0   & (\text{被开方数非负}),
    \end{cases}\quad\text{解得}\quad x>0.\]
上述结论可以直接使用. 类似地, 对 $\sqrt{\dfrac1x}$, 同样应限制 $x>0$.
</p>
<p>\begin{example}\label{exa:201101-1415}
    求下列函数的定义域:
    \begin{twocolpro}
        (1) $f(x)=\dfrac{\sqrt{x-3}}{|x+1|-5}$;
        &(2) $f(x)=\dfrac{(x+1)^0}{|x|-x}$;\\
        (3) $f(x)=\dfrac1{1+\dfrac2x}$. &
    \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 由题意,
    \[\left\{\!\!\begin{array}{l}
        x-3\geqslant 0,\\
        |x+1|-5\neq0,
        \end{array}\right.\ \text{解得}\quad
        x\geqslant 3\ \text{且}\ x\neq4,\]
    所求定义域为 $[3,4)\cup(4,+\infty)$.
</p>
<p>(2) 由题意,
    \[\left\{\!\!\begin{array}{l}
        x+1\neq 0,\\
        |x|-x\neq0,
        \end{array}\right.\ \text{解得}\quad
        x< 0\ \text{且}\ x\neq -1,\]
    所求定义域为 $(-\infty,-1)\cup(-1,0)$.
</p>
<p>(3) 由题意,
    \[\left\{\!\!\begin{array}{l}
        1+\dfrac2x\neq 0,\\
        x\neq0,
        \end{array}\right.\ \text{解得}\quad
        x\neq 0\ \text{且}\ x\neq -2,\]
    所求定义域为 $(-\infty,-2)\cup (-2,0)\cup (0,+\infty)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201101-1415} 的 (2) 中, 由 $|x|-x\neq 0$ 可得 $x< 0$, 因为此时 $|x|\neq x$ 只在 $x< 0$ 时才成立.
</p>
<p>对于其他问题, 需要根据题意对自变量增加更多的限制, 例如三角形三边中任意两边之和大于第三边; 在实际问题中, 人数只能为非负整数, 等等.
</p>
<p>在求抽象函数 (无具体表达式) 的定义域时, 需要注意函数的作用范围和定义域的区别. 函数是一个数集到另一个数集的对应关系, 前一个数集就是函数的作用范围, 不随表达式的变化而变化. 
</p>
<p>例如, 对定义在 $(0,2)$ 上的函数 $f(x)$, 其定义域和作用范围均为 $(0,2)$ (两者相同). 再考虑 $f(2x)$, 此时函数 $f$ 的作用范围仍为 $(0,2)$ 且 $f$ 作用在 $2x$ 上, 所以 $2x$ 应在作用范围内, 即满足 $2x\in(0,2)$, 解得 $x\in(0,1)$, 表明 $f(2x)$ 的定义域 (即 $x$ 的取值范围) 为 $(0,1)$ (与作用范围不同). 注意, 这里 $f(x)$ 和 $f(2x)$ 中的 $x$ 含义不同, 其取值范围分别是对应函数的定义域.
</p>
<p>再如, 对定义在 $(0,2)$ 上的函数 $g(x+1)$, 其定义域 (即 $x$ 的取值范围) 是 $(0,2)$, 但函数 $g$ 作用在 $x+1$ 上, 由 $x+1\in(1,3)$ 知其作用范围为 $(1,3)$ (与定义域不同). 再考虑 $g(x)$, 此时 $g$ 作用在 $x$ 上, 所以 $x$ 应在作用范围内, 即满足 $x\in(1,3)$, 表明 $g(x)$ 的定义域为 $(1,3)$ (与作用范围相同).
</p>
<p>以上两个例子说明, 函数 $f(x)$ 的定义域与作用范围相同, 而函数 $f(ax+b)$ 的定义域与作用范围一般不同, 但是两个 $f$ 的作用范围相同, 即 $f(x)$ 中的 $x$ 与 $f(ax+b)$ 中的 $ax+b$ 都在同一取值范围内. 解题时<strong>只需关注函数的作用范围不变即可</strong> (即先求出该范围), 并注意定义域是当前表达式中 $x$ 的取值范围, 解题过程可适当简化.</p>
<p><myexample>
<p>已知函数 $f(x)$ 的定义域为 $[0,1)$, 求 $f(2x)$ 的定义域和 $f(x+3)$ 的定义域.
</p>
</myexample>
<mysolution>
    <p>对 $f(2x)$, 由已知 $2x\in[0,1)$, 所以 $x\in\biggl[0,\dfrac12\biggr)$, 即 $f(x)$ 的定义域为 $\biggl[0,\dfrac12\biggr)$.
</p>
<p>而对 $f(x+3)$, 有 $x+3\in[0,1)$, 所以 $x\in[-3,-2)$, 即 $f(x+3)$ 的定义域为 $[-3,-2)$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(2x)$ 的定义域为 $[0,1)$, 求 $f(x)$ 的定义域和 $f(x+3)$ 的定义域.
</p>
</myexample>
<mysolution>
    <p>对 $f(2x)$, 由已知 $x\in[0,1)$, 所以 $2x\in[0,2)$, 即 $f(x)$ 的定义域为 $[0,2)$.
</p>
<p>而对 $f(x+3)$, 有 $x+3\in[0,2)$, 所以 $x\in[-3,-1)$, 即 $f(x+3)$ 的定义域为 $[-3,-1)$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x+3)$ 的定义域为 $[0,1)$, 求 $f(x)$ 的定义域和 $f(2x)$ 的定义域.
</p>
</myexample>
<mysolution>
    <p>对 $f(x+3)$, 由已知 $x\in[0,1)$, 所以 $x+3\in[3,4)$, 即 $f(x)$ 的定义域为 $[3,4)$.
</p>
<p>而对 $f(2x)$, 有 $2x\in[3,4)$, 所以 $x\in\biggl[\dfrac32,2\biggr)$, 即 $f(x+3)$ 的定义域为 $\biggl[\dfrac32,2\biggr)$.
</p>
</mysolution>

<p>\subsection{求已知类型的函数解析式}
</p>
<p>当函数的类型已知时, 用待定系数法来解, 即只需按题意设函数解析式, 并写出其中的系数满足的条件, 再解相应的方程组即可.
</p>
<p>\begin{example}\label{exa:201105-2130}
    已知 $f(x)$ 是一次函数, 
    \[\left\{\!\!\begin{array}{l}
        2f(1)+3f(2)=5,\\
        2f(-1)-f(0)=-1,
      \end{array}\right.\]
    求 $f(x)$ 的解析式.
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 是一次函数, 所以可以设 $f(x)=kx+b$ ($k\neq 0$). 由题意,
    \[\left\{\!\!\begin{array}{l}
        2(k+b)+3(2k+b)=5,\\
        2(-k+b)-b=-1,
      \end{array}\right.\ \text{解得}\ 
      \left\{\!\!\begin{array}{l}
        k=\dfrac59,\\[3pt]
        b=\dfrac19,
      \end{array}\right.\]
    所以 $f(x)=\dfrac59 x+ \dfrac19$.
</p>
</mysolution>
</p>
<p>解例 \ref{exa:201105-2130} 时应注意, 为使 $f(x)$ 为一次函数, 其解析式的一次项系数非零, 即解题过程中的 $k\neq0$. 若 $f(x)$ 为二次函数, 也应注意其解析式的二次项系数非零. 其他形式可以类推.
</p>
<p>\begin{example}\label{exa:201105-2140}
    已知 $f(x)$ 为二次函数, $f(0)=1$, $f(x+1)=f(x)+2x$, 求 $f(x)$ 的解析式.
</p>
</myexample>
<mysolution>
    <p>由 $f(x)$ 为一元二次函数和 $f(0)=1$ 可设 
    \[f(x)=ax^2+bx+1\quad (a\neq 0),\]
    再代入 $f(x+1)=f(x)+2x$ 可得
    \[a(x+1)^2+b(x+1)+1=(ax^2+bx+1)+2x,\]
    即 $2ax+a+b=2x$, 所以
    \[\left\{\!\!\begin{array}{l}
        2a=2,\\
        a+b=0,
      \end{array}\right.\ \text{解得}\ 
      \left\{\!\!\begin{array}{l}
        a=1,\\
        b=-1,
      \end{array}\right.\]
    即 $f(x)= x^2-x+1$.
</p>
</mysolution>
</p>
<p>在解例 \ref{exa:201105-2140} 时, 设出解析式之后, 因为要确定两个系数 $a$, $b$, 所以也可以根据 $f(x+1)=f(x)+2x$ 取两个特殊的 $x$ 值, 得到两个方程从而解出 $a$ 和 $b$. 由于已有 $f(0)=1$, 所以不妨分别设 $x=0$ 和 $-1$, 可得 \[f(1)=0,\ f(-1)=2,\quad \text{即}\quad a+b=0,\ a-b=2.\]
用这种方法也可以方便地求出两个系数.
</p>
<p>\subsection{求未知类型的函数解析式}
</p>
<p>若函数解析式的类型未知, 则一般是用整体代换来解决. 例如已知 $f(x+1)=2x$ 求 $f(x)$ 时, 应理解前一表达式 (即 $f(x+1)=2x$) 中的 $f$ 是作用在 $x+1$ 上, 而后一表达式 (即 $f(x)$) 中的 $f$ 是作用在 $x$ 上. 想要求出后者相当于是弄清楚前者中的 $f$ 是如何作用在 $x+1$ 上并得出 $2x$ 的. 此时应把 $x+1$ 看成整体, 比如设 $x+1=t$, 再想办法把 $2x$ 用 $t$ 表示出来. 因为 $x=t-1$, 所以 $2x=2(t-1)$, 表明由 $f(x+1)=2x$ 可得 $f(t)=2(t-1)$, 又可写成 $f(x)=2(x-1)$. 
</p>
<p>由以上分析可知, 解题这类问题时, 主要步骤一般只有两步: 先把 $f$ 作用的式子看成整体, 再把得到的式子用该整体表示.
</p>
<p>\begin{example}\label{exa:201105-2150}
    设 $f(2x+1)=x^2-2x$, 求 $f(x)$ 和 $f(1)$.
</p>
</myexample>
<mysolution>
    <p>对 $f(2x+1)=x^2-2x$, 令 $2x+1=t$, 则 $x=\dfrac{t-1}2$, 所以
    \[\begin{aligned}
        f(t)&=f(2x+1)=x^2-2x= \biggl(\frac{t-1}2\biggr)^2- 2\cdot\frac{t-1}2\\
        &= \frac14 t^2- \frac32 t+ \frac54,
    \end{aligned}\]
    即 $f(x)= \dfrac14 x^2- \dfrac32 x+ \dfrac54$. 而
    \[f(1)= \frac14- \frac32+ \frac54=0.\]
</p>
</mysolution>
</p>
<p>例 \ref{exa:201105-2150} 中的 $f(1)$ 也可通过在 $f(2x+1)=x^2-2x$ 中令 $x=0$ 得到. 类似地, 若求 $f(3)$, 则可直接令 $x=1$.
</p>
<p>\begin{example}\label{exa:201105-2200}
    已知 $f\biggl(x+\dfrac1x\biggr)= x^2+\dfrac1{x^2}$, 求 $f(x)$.
</p>
</myexample>
<mysolution>
    <p>设 $x+\dfrac1x=t$, 则 
    \[x^2+\frac1{x^2}= \biggl(x+\dfrac1x\biggr)^2-2= t^2-2,\]
    所以 $f(t)= t^2-2$, 即 $f(x)=x^2-2$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201105-2200} 比较特殊, 解题时没有根据 $x+\dfrac1x=t$ 解出 $x$ 再代入 $x^2+\dfrac1{x^2}$, 而是直接利用恒等式做了替换. 类似的恒等式还有 (注意观察恒等式的特征)
\begin{gather*}
    x^2+\frac4{x^2}= \biggl(x+\dfrac2x\biggr)^2-4,\\
    x^4+\frac1{x^4}= \biggl(x^2+\dfrac1{x^2}\biggr)^2-2
        = \biggl(\biggl(x+\dfrac1x\biggr)^2-2\biggr)^2-2.
\end{gather*}
</p>
<p>\begin{example}\label{exa:201105-2210}
    若 $2f(x)+f\biggl(\dfrac1x\biggr)=3x$ ($x\neq 0$) 恒成立, 求 $f(x)$ 的解析式.
</p>
</myexample>
<mysolution>
    <p>把已知表达式中的所有 $x$ 都换成 $\dfrac1x$, 得 $2f\biggl(\dfrac1x\biggr)+f(x)=3\dfrac1x$, 再与已知表达式联立并消去 $f\biggl(\dfrac1x\biggr)$, 解得 $f(x)= 2x-\dfrac1x$ ($x\neq0$).
</p>
</mysolution>
</p>
<p>例 \ref{exa:201105-2210} 也是特殊题, 解这种题时, 一般是想办法凑出和已知表达式类似的式子 (通常是把 $x$ 换成其他式子), 联立并解出需要的 $f(x)$. 例如, 若已知 $2f(x)+f\biggl(-\dfrac1x\biggr)=3x$, 则可以把 $x$ 都换成 $-\dfrac1x$, 可得 
\[2f\biggl(-\dfrac1x\biggr)+f(x)= -\dfrac3x;\]
若已知 $2f(x)+f(1-x)=3x$, 则可以把 $x$ 都换成 $1-x$, 可得
\[2f(1-x)+f(x)=3(1-x).\]
以上都只进行了一次替换, 即可与已知表达式联立并解出 $f(x)$. 有的时候可能需要替换多次, 才能得到能联立的方程. 例如, 若已知 $f(x)+f\biggl(\dfrac1{1-x}\biggr)=3x$, 则可以把 $x$ 都换成 $\dfrac1{1-x}$, 再把 $x$ 都换成 $\dfrac{x-1}{x}$, 就可以得到关于 $f(x)$, $f\biggl(\dfrac1{1-x}\biggr)$ 和 $f\biggl(\dfrac{x-1}{x}\biggr)$ 的三元一次方程组 (具体过程可自行写出).
</p>

<p>\subsection{判断两个函数是否相同}
</p>
<p>因为函数是由其定义域和对应法则决定的, 所以判断两个函数是否相同也应从这两个方面考虑: 先看定义域是否相同, 若不同, 则两个函数不同; 若相同, 再看表达式能否化为相同的形式. 只有定义域和对应法则都相同的函数才是同一个函数. 另外需要注意, 函数是否相同与其所用的字母无关: 定义域是自变量的取值范围 (一个数集), 对应法则是运算规则, 两者都不涉及表达式中的字母选择. 例如, 
</p>
<p>$f(x)=2x+1$ ($x>1$) 与 $g(u)=2u+1$ ($u>1$) 是相同的函数 (仅所用字母不同); 
</p>
<p>$f(x)=2x+1$ ($x>1$) 与 $g(u)=2u+1$ ($u>2$) 是不同的函数 (定义域不同);
</p>
<p>$f(x)=2x+1$ ($x>1$) 与 $g(u)=3u+1$ ($u>1$) 也是不同的函数  (对应法则不同).
</p>
<p><myexample>
<p>下列各组函数中, \underline{\qquad} 的两个函数为相同的函数.
</p>
<p>(1) $f(x)= x^2-2x-1$, $g(s)=s^2-2s-1$;
</p>
<p>(2) $f(x)=\dfrac{x}x$, $g(x)=\dfrac1{x^0}$;\qquad
    (3) $f(x)=\sqrt{-x^3}$, $g(x)=x\sqrt{x}$;
</p>
<p>(4) $f(x)=x$, $g(x)=\sqrt{x^2}$;\qquad
    (5) $f(x)=\sqrt{x^3}$, $g(x)=x\sqrt{x}$.
</p>
</myexample>
<mysolution>
    <p>(1) $f(x)$ 与 $g(s)$ 定义域均为 $\realnum$, 且对应法则相同, 所以为相同的函数 (仅自变量所用字母不同).
</p>
<p>(2) $f(x)$ 与 $g(x)$ 定义域均为 $\{x\mid x\neq 0\}$, 且
    \[f(x)=1,\quad g(x)=\frac11=1,\]
    所以 $f(x)=g(x)$.
</p>
<p>(3) 对 $f(x)$, $-x^3\geqslant 0$, 解得 $x\leqslant 0$.
    对 $g(x)$, $x\geqslant 0$. 所以 $f(x)$ 与 $g(x)$ 的定义域不同, 两者为为不同的函数.
</p>
<p>(4) $f(x)$ 与 $g(x)$ 的定义域都是 $\realnum$, 但是 $g(x)=|x|\neq f(x)$.
</p>
<p>(5) $f(x)$ 与 $g(x)$ 的定义域都是 $[0,+\infty)$, 而
    \[f(x)=\sqrt{x^2\cdot x}=|x|\sqrt{x}\neq g(x),\]
    所以两者为不同的函数.
</p>
<p>综上可知, (1)(2) 的两个函数为相同的函数.
</p>
</mysolution>
<myremark>
    <p>$\sqrt{x^2}=|x|$ 的解释: 当 $x\geqslant 0$ 时, $\sqrt{x^2}=x$; 当 $x< 0$ 时, $\sqrt{x^2}=-x$, 恰好符合 $|x|$ 的定义. 另一种推导为
    \[\sqrt{x^2}= \sqrt{|x|^2}= |x|.\]
    类似的结论还有
    \[\sqrt[3]{x^3}=x\ (\text{没有绝对值符号}),\quad
      \sqrt[4]{x^4}=|x|.\]
</p>
</myremark>
</p>
<p>\subsection{分段函数}
</p>
<p>分段函数相关的问题, 分段考虑即可.
</p>
<p><myexample>
<p>已知函数 $f(x)=\begin{cases}
        2x+1, & x\geqslant 0,\\
        3x^2, & x< 0
    \end{cases}$ 且 $f(x_0)=3$, 求实数 $x_0$ 的值.
</p>
</myexample>
<mysolution>
    <p>题中没有给 $x_0$ 的取值范围, 所以需要分类讨论.
</p>
<p>(1) 若 $x_0\geqslant 0$, 则 $f(x_0)=3$ 化为 $2x_0+1=3$, 解得 $x_0=1$.
</p>
<p>(2) 若 $x_0< 0$, 则 $f(x_0)=3$ 化为 $3x_0^2=3$, 解得 $x_0=\pm1$. 结合前提 $x_0< 0$ 知, $x=-1$.
</p>
<p>综上所述, $x_0=1$ 或 $-1$.
</p>
</mysolution>
</p>
<p><myexample>
<p>求函数 $f(x)=\begin{cases}
        x^2-x+1, & x< 1,\\
        \dfrac1x, & x\geqslant 1
    \end{cases}$ 的值域.
</p>
</myexample>
<mysolution>
    <p>(1) 当 $x< 1$ 时, $f(x)=x^2-x+1$ 为二次函数, 对称轴为 $x=\dfrac12$, 所以此时 $f(x)\in\biggl[f\biggl(\dfrac12\biggr),+\infty\biggr)= \biggl[\dfrac34,+\infty\biggr)$.
</p>
<p>(2) 当 $x\geqslant 1$ 时, $f(x)=\dfrac1x$ 为反比例函数, 由其图象知, 此时 $f(x)\in(0,f(1)]= (0,1]$.
</p>
<p>综上所述, $f(x)$ 的值域为 $\biggl[\dfrac34,+\infty\biggr)\cup (0,1]= (0,+\infty)$.
</p>
</mysolution>
<myremark>
    <p>反比例函数 $f(x)= \dfrac1x$ ($x\neq 0$) 的图象如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1108-2300-crop}
    </center>
</p>
<p>从图象可以看出, 该函数 (1) 在 $(-\infty,0)$ 和 $(0,+\infty)$ 均单调递减; (2) 值域为 $(-\infty,0)\cup (0,+\infty)$; (3) 以 $x$ 轴和 $y$ 轴为两条渐近线.
</p>
</myremark>
