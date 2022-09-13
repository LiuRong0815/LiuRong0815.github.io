---
# bookCollapseSection: true
title: 函数的图象
weight: 4
bookHidden: true
prevPage: /docs/algebra/function/function-oddeven
prevPageTitle: 函数的奇偶性
nextPage: /docs/algebra/function/quadratic-function
nextPageTitle: 二次函数
---

# 函数的图象


<p>\begin{example}\label{exa:201206-1410}
    若 $a$, $b>0$, 则“$a>b$”是“$a-\dfrac1a> b-\dfrac1b$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>方法一: 由例 \ref{exa:201204-1920} 中的变形过程可知
    \[a-\dfrac1a> b-\dfrac1b\Rightarrow
        (a-b)\biggl(1+\frac1{ab}\biggr)>0.\]
    再由 $a$, $b>0$ 得 $ab>0$, 即 $1+\dfrac1{ab}>0$, 所以上式等价于 $a-b>0$. 这表明“$a>b$”是“$a-\dfrac1a> b-\dfrac1b$”的充要条件.
</p>
<p>方法二: 构造函数 $f(x)=x-\dfrac1x$ ($x>0$), 则不等式 $a-\dfrac1a> b-\dfrac1b$ 化为 $f(a)>f(b)$. 因为 $\dfrac1x$ 在 $(0,+\infty)$ 上单调递减, 所以 $-\dfrac1x$ 在 $(0,+\infty)$ 上单调递增. 而 $x$ 在 $(0,+\infty)$ 上也单调递增, 所以 $f(x)=x-\dfrac1x$ ($x>0$) 单调递增. 这表明 $f(a)>f(b)\Leftrightarrow a>b$, 所求为充要条件.
</p>
</mysolution>

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

<p>先考虑函数 $y=f(x)$ 与 $y=f(x+1)$ 的图形. 因为点 $A(n,f(n))$ 满足 $y=f(x)$ (此时 $x=n$), 而点 $A'(n-1,f(n))$ 满足 $y=f(x+1)$ (此时 $x=n-1$), 且点 $A$ 向左平移一个单位长度可得点 $A'$, 所以将 $y=f(x)$ 图形上的所有点向左平移一个单位长度可得 $y=f(x+1)$ 的图形.
</p>
<p>再考虑函数 $y=f(x)$ 与 $y=f(x)+1$ 的图形. 因为点 $B(n,f(n))$ 满足 $y=f(x)$ (此时 $x=n$), 而点 $B'(n,f(n)+1)$ 满足 $y=f(x+1)$ (此时 $x=n$), 且点 $B$ 向上平移一个单位长度可得点 $B'$, 所以将 $y=f(x)$ 图形上的所有点向上平移一个单位长度可得 $y=f(x)+1$ 的图形.
</p>
<p>设 $a>0$, 由同样的分析可以知道, 
\[\begin{aligned}
    &\text{向左平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x+a);\\
    &\text{向右平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x-a);\\
    &\text{向上平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x)+a;\\
    &\text{向下平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x)-a.
\end{aligned}\]
以上结论可以简记为“左加右减, 上加下减”. 示意图如下($a>0$):
</p>
<p><center>
        \includegraphics[scale=1]{2020-1215-1900-crop}\qquad
        \includegraphics[scale=1]{2020-1215-1910-crop}
    </center>
</p>
<p>注意, 这些结论均是对 $x$ 或 $f(x)$ (即 $y$) 的整体变换. 例如 $f(2x)$ 的图形往左平移 $1$ 个单位长度, 得到 $f(2(x+1))$ 即 $f(2x+2)$ 的图形; 而由 $f(3x)$ 的图形要得到 $f(3x-1)$ 的图形, 需将前者往右平移 $\dfrac13$ 个单位长度.
</p>
<p>接着考虑函数 $y=f(x)$ 与 $y=-f(x)$ 的图形. 因为点 $C(n,f(n))$ 满足 $y=f(x)$ (此时 $x=n$), 而点 $C'(n,-f(n))$ 满足 $y=f(x+1)$ (此时 $x=n$), 且点 $C$ 与 $C'$ 关于 $x$ 轴对称, 所以作 $y=f(x)$ 图形上的所有点关于 $x$ 轴的对称点可得 $y=-f(x)$ 的图形 (两个图形上对应点横坐标相同, 纵坐标互为相反数, 简记为“上下翻转”). 类似地, 作 $y=f(x)$ 图形上的所有点关于 $y$ 轴的对称点可得 $y=f(-x)$ 的图形 (两个图形上对应点横坐标互为相反数, 纵坐标相同, 简记为“左右翻转”). 示意图如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1215-1920-crop}\qquad
        \includegraphics[scale=1]{2020-1215-1930-crop}
    </center>
</p>
<p>上述六种图形变换可以叠加. 例如, $f(x)$ 的图形先上下翻转可得 $-f(x)$ 的图形, 再左右翻转可得 $-f(-x)$ 的图形; $f(x)$ 的图形先左右翻转可得 $f(-x)$ 的图形, 再向右平移 $4$ 个单位长度 (将 $x$ 替换为 $x-4$) 可得 $f(4-x)$ 的图形.
</p>
<p><myexample>
<p>已知 $f(x)=\begin{cases}
        \dfrac12 x,& -2\leqslant x\leqslant 0,\\
        -x^2+2x,& 0< x\leqslant 2,
    \end{cases}$ 画出下列函数的图形:
</p>
<p>(1) $f(x)$;\qquad (2) $f(x-2)$;\qquad (3) $-f(x)$;\qquad 
    (4) $f(-x)$;\qquad (5) $-f(-x)$.
</p>
</myexample>
<mysolution>
    <p>各函数图形依次如下:
</p>
<p><center>
        \includegraphics[scale=1.2]{2020-1215-1940-crop}\qquad
        \includegraphics[scale=1.2]{2020-1215-1950-crop}\qquad
        \includegraphics[scale=1.2]{2020-1215-2000-crop}
    </center>
</p>
<p><center>
        \includegraphics[scale=1.2]{2020-1215-2010-crop}\qquad
        \includegraphics[scale=1.2]{2020-1215-2020-crop}
    </center>
</p>
</mysolution>


<myexample>
<p>已知函数 $f(x)= \dfrac{2x+1}{x+1}$, 求该函数在区间 $[1,4]$ 上的最大值与最小值.
</p>
</myexample>
<mysolution>
    <p>用分离常数法, 
    \[f(x)= \frac{2x+1}{x+1}= \frac{2(x+1)-1}{x+1}
        = 2-\frac1{x+1}.\]
    因为 $x\in[1,4]$, 所以 $\dfrac1{x+1}$ 单调递减, $-\dfrac1{x+1}$ 单调递增, $2-\dfrac1{x+1}$ 也单调递增, 从而 
    \[f_{\min}= f(1)= \dfrac32,\quad f_{\max}= f(4)= \dfrac95.\]
</p>
</mysolution>

<myexample>
<p>已知 $f(x)=\begin{cases}
      2x, & x>0,\\
      f(x+1), & x\leqslant 0,
    \end{cases}$ 那么 $f\Bigl(-\frac43\Bigr)=$\,? 试作出其图象.
  </p>
</myexample>
</p>
<p><mysolution>
    <p>    $f\Bigl(-\frac43\Bigr)=f\Bigl(-\frac13\Bigr)= f\Bigl(\frac23\Bigr)= \frac43$. 图象如右图.
    \mymarginpar{\centering
      \begin{tikzpicture}[line cap=round,line join=round,scale=0.7]
        \draw[\myaxisarrow] (-3,0) -- (2,0) node[below] {$x$};
        \draw[\myaxisarrow] (0,-0.5) -- (0,3) node[left] {$y$};
        \draw[fill=black] (0,0)--(1.3,2.6) 
          (-1,0)--(0,2) node[right] {$2$} circle (1.5pt) (-2,0)
          --(-1,2) circle (1.5pt);
        \draw[fill=white] (0,0) node[anchor= north east] {$O$} circle (1.5pt) (-1,0) node[below] {$-1$} circle (1.5pt) 
          (-2,0) node[below] {$-2$}  circle (1.5pt);
      \end{tikzpicture}}
  </p>
</mysolution>


<p>\lianxi
  \begin{exercise}[s]
    设函数 $D(x)=\begin{cases}
      1, & x\text{ 为有理数,}\\
      0, & x\text{ 为无理数,}\end{cases}$
    则下列结论中正确的是\,?(填序号)
</p>
<p>(1) $D(x)$ 的值域为 $\{0,1\}$;\qquad
    (2) $D(x)$ 是偶函数;
</p>
<p>(3) $D(x)$ 不是周期函数;\qquad
    (4) $D(x)$ 不是单调函数.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    (1) 显然正确; 由 $x$ 与 $-x$ 要么同为有理数, 要么同为无理数知 $D(x)=D(-x)$, (2) 正确; 由 $D(x+1)=D(x)$ 知 (3) 错误 (任一有理数均为 $D(x)$ 的周期); 由 $D(0)=D(2)=1>0=D(\sqrt2)$ 知 (4) 正确.
  </p>
</mysolution>

