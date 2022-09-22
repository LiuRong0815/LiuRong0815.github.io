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

<p>函数的图象可以形象地描述自变量与因变量的对应关系. 定义在数集 $D$ 上的函数 $f$ 的图象为点集 \[
    \{(x,y)\mid x\in D,y= f(x)\}.\]
因为函数自变量的任一取值只能与因变量某一确定取值对应, 所以函数图象与平行于 $y$ 轴的任一直线至多只有一个交点 (否则一对多, 与函数定义不符).
</p>
<p>作函数图象最基本的方法是描点画图, 但是若描的点太少或并非图象的关键点, 则无法得到准确图象. 对于复杂的函数, 仍需借助函数的性质, 如单调性和奇偶性, 以更准确地作出其图象: 单调性对应图象的增减性, 奇偶性对应图象的对称性. 分段函数的图象则需分段作出.
</p>

## 函数图象的变换

<p>利用<a href="/docs/prerequisite/ms-function/graph-tranform/#函数图象的变换-2022-0918-1730">函数图象的变换</a>, 可以从已知函数的图象直接得到新函数的图象. 下面简要回顾函数图象的变换与解析式变化的对应关系.
</p>
<p>以向左平移函数图象为例: 将函数 $y=f(x)$ 的图象 $G$ 向左平移 $1$ 个单位长度, 得到图形 $G_1$. 任取 $G_1$ 上一点 $P_1(x,y)$, 向右平移 $1$ 个单位长度后, 得 $G$ 上的对应点 $P(x+1,y)$, 则 $y= f(x+1)$. 这就是新图象 $G'$ 上点的横、纵坐标之间的关系. 因此函数 $f(x+1)$ 的图象由 $f(x)$ 的图象向左平移 $1$ 个单位长度得到.
</p>
<p>设 $a>0$, 由同样的分析可知, \[\begin{aligned}
    &\text{向左平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x+a);\\
    &\text{向右平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x-a);\\
    &\text{向上平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x)+a;\\
    &\text{向下平移 $a$ 个单位长度:}\ f(x)\rightarrow f(x)-a.
\end{aligned}\]
以上结论通常简记为“左加右减, 上加下减”. 示意图如下 ($a>0$):
</p>
<p><center>
        \includegraphics[scale=1]{2020-1215-1900-crop}\qquad
        \includegraphics[scale=1]{2020-1215-1910-crop}
    </center>
</p>
<p>注意, 这些结论均是对 $x$ 或 $f(x)$ (即 $y$) 的整体变换. 例如 $f(2x)$ 的图形往左平移 $1$ 个单位长度, 得到 $f(2(x+1))$ 即 $f(2x+2)$ 的图形; 而由 $f(3x)$ 的图形要得到 $f(3x-1)$ 的图形, 需将前者往右平移 $\dfrac13$ 个单位长度.
</p>
<p>作函数 $y= f(x)$ 的图象 $G$ 关于 $x$ 轴的对称图形 $G_2$. 任取 $G_2$ 上一点 $P_2(x,y)$, 关于 $x$ 对称后, 得 $G$ 上的对应点 $P(x,-y)$, 则 $-y= f(x)$ 即 $y= -f(x)$. 所以 $G_2$ 对应的函数解析式为 $y= -f(x)$, 即函数 $-f(x)$ 的图象由 $f(x)$ 的图象关于 $x$ 作对称图形得到 (简记为“上下翻转”). 类似地, 函数 $f(-x)$ 的图象由 $f(x)$ 的图象关于 $y$ 作对称图形得到 (简记为“左右翻转”). 示意图如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1215-1920-crop}\qquad
        \includegraphics[scale=1]{2020-1215-1930-crop}
    </center>
</p>
<p>上述六种图形变换可以叠加. 例如, $f(x)$ 的图象先上下翻转可得 $-f(x)$ 的图象, 再左右翻转可得 $-f(-x)$ 的图象 (这也是 $f(x)$ 的图象关于原点的对称图形); $f(x)$ 的图象先左右翻转可得 $f(-x)$ 的图象, 再向右平移 $4$ 个单位长度 (将 $x$ 替换为 $x-4$) 可得 $f(4-x)$ 的图象.
</p>

<myremark>
    <p>利用对应点的坐标关系, 是分析图象变换对函数解析式的影响的通用方法. 用这种方法还可以得到解析式中的绝对值对图象的影响: $|f(x)|$ 的图象是将 $f(x)$ 的图象在 $x$ 轴下方的部分翻折到 $x$ 轴上方得到的, $f(|x|)$ 的图象是将 $f(x)$ 的图象在 $y$ 轴右侧的部分翻折到 $y$ 轴左侧得到的 (后一种情况也可以按照偶函数来理解).
    </p>
</myremark>

<p>利用图像变换可以很容易作出分式线性函数 $f(x)= \dfrac{ax+b}{cx+d}$ 的图象. 例如, 对函数 $f(x)= \dfrac{2x+1}{x+1}$, 因为 \[\begin{aligned}
    f(x)&= \frac{2x+1}{x+1}= \frac{2(x+1)-1}{x+1}
        &= 2-\frac1{x+1}.
\end{aligned}\]
所以 $f(x)$ 的图象可由 $y= -\dfrac1x$ 的图象向左平移 $1$ 个单位长度, 再向上平移 $2$ 的单位长度得到. 上述变形方法称为分离常数法.
</p>

<myexample>
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
<p>指出下列函数的单调性和值域:
    \begin{twocolpro}
    (1) $f(x)=x^2+|x|-2$; & (2) $g(x)= \dfrac{3x+1}{x-1}$.
    \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 方法一: 根据绝对值的定义可知,
    \[f(x)=\begin{cases}
        x^2+x-2,& x\geqslant 0,\\
        x^2-x-2,& x< 0.
        \end{cases}\]
    函数的图形如下 (分别作 $y$ 轴左侧和右侧的图形):
</p>
<p><center>
        \includegraphics[scale=1.1]{2020-1126-1945-crop}
    </center>
</p>
<p>由图得, $f(x)$ 在 $(-\infty,0)$ 上单调递减, 在 $[0,+\infty)$ 上单调递增, 值域为 $[-2,+\infty)$.
</p>
<p>方法二: 因为 $f(-x)=f(x)$, 所以 $f(x)$ 为偶函数, 图形关于 $y$ 轴对称. 令 $x\geqslant 0$ 知, $f(x)=x^2+x-2$, 可作出 $f(x)$ 在 $y$ 轴右侧的图形, 再关于 $y$ 轴作对称图形即可. 答案同上. 
</p>
<p>(2) 将函数变形 (把分子写成“分母的倍数”加“常数”的形式, 再拆项),
    \[g(x)= \frac{3(x-1)+4}{x-1}= 3+\frac4{x-1},\]
    由此可知, $g(x)$ 的图形可由 $h(x)=\dfrac4x$ 的图形向右平移一个单位长度, 再向上平移三个单位长度得到:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1126-2225-crop}
    </center>
</p>
<p>所以, $g(x)$ 在 $(-\infty,1)$ 和 $(1,+\infty)$ 上均单调递减, 值域为 $(-\infty,3)\cup (3,+\infty)$.
</p>
</mysolution>

## 函数图象的应用

<myexample>
    <p>若 $a$, $b>0$, 则“$a>b$”是“$a-\dfrac1a> b-\dfrac1b$”的什么条件?
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

## 函数的周期性

<p>周期性描述的是函数图象不断重复自身. 设常数 $a\neq 0$, 若函数 $f(x)$ 满足 $f(x)= f(x+a)$, 则称 $f(x)$ 为周期函数, 且以 $a$ 为周期. 将 $f(x)= f(x+a)$ 中的 $x$ 换成 $x-a$, 可知该式等价于 \[
    f(x-a)= f(x)\Rightarrow f(x)= f(x+(-a)),\]
即 $-a$ 也是 $f(x)$ 的周期, 因此通常只考虑周期函数的正周期. 再将 $f(x)= f(x+a)$ 中的 $x$ 依次换成 $x+a$, $x+2a$, $\cdots$, 可知 \[
    f(x)= f(x+a)= f(x+2a)= f(x+3a)= \cdots,\]
即 $ka$ ($k\in\mathbf{Z}$) 均为 $f(x)$ 的周期, 因此 (如有可能) 通常优先考虑周期函数的最小正周期. 后面会介绍没有最小正周期的周期函数.
</p>

<myexample>
    <p>已知奇函数 $f(x)$ 定义在 $\mathbf{R}$ 上.
    </p>
    <p>(1) 若 $f(x+4)=f(x)$, 求 $f(3)+f(4)+f(5)$ 的值;
    </p>
    <p>(2) 若 $f(x+2)=-f(x)$, 求 $f(-6)$ 的值.
    </p>
</myexample>
<mysolution>
    <p>对定义在 $\mathbf{R}$ 上的奇函数 $f(x)$, 恒有 $f(-x)=-f(x)$. 令 $x=0$ 得 $f(0)=-f(0)$, 所以 $f(0)=0$.
    </p>
    <p>(1) 结合 $f(x+4)=f(x)$ 知, \[\begin{aligned}
        \text{令 $x=0$:}&\ f(4)=f(0)=0,\\
        \text{令 $x=1$:}&\ f(5)=f(1),\\
        \text{令 $x=-1$:}&\ f(3)=f(-1)=-f(1),
    \end{aligned}\]
    所以 $f(3)+f(4)+f(5)= (-1)+0+1=0$.
    </p>
    <p>(2) 由已知 $f(x)=-f(x+2)$, 所以 \[
        f(-6)=-f(-4)=f(-2)=-f(0)=0.\]
    </p>
</mysolution>

<myremark>
    <p>上述 $f(x+2)=-f(x)$ 描述的并非周期性, 但是因为 \[
        f(x+4)= f((x+2)+2)= f(x+2)= f(x),\]
    所以 $f(x)$ 仍为周期函数, 且以 $4$ 为一个周期.
    </p>
</myremark>

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



## 高斯函数与狄利克雷函数


<myexample>
    <p>若 $x$ 为实数, $[x]$ 表示不超过 $x$ 的最大整数, 
    则下面关于定义域在 $\mathbf{R}$ 上的函数 $f(x)=x-[x]$ 的说法正确的是\,?
    </p>
<p>(1) 奇函数;\qquad (2) 偶函数;\qquad 
    (3) 单调递增函数;\qquad (4) 周期函数.
  </p>
</myexample>
</p>
<p><mysolution>
    <p>    由 $f(x)$ 的图象可知, 只有 (4) 正确.
    \mymarginpar{函数 $y=[x]$ 的图象如下\\[4pt]
      \centering
      \begin{tikzpicture}[line cap=round,line join=round,scale=0.6]
        \draw[\myaxisarrow] (-2.5,0) -- (3.7,0) node[below] {$x$};
        \draw[\myaxisarrow] (0,-2.5) -- (0,2.7) node[left] {$y$};
        \foreach \i in {-2,1,2}
          {\draw[line width=0.5pt, densely dashed] (\i,0)--(\i,\i) (\i+1,0)--(\i+1,\i);}
        \foreach \i in {-2,...,2}
          {\draw[fill=black,line width=0.6pt] (\i,\i) circle (1.8pt) --(\i+1,\i);
           \draw[fill=white] (\i+1,\i) circle (1.8pt);}
        \foreach \i in {-2,-1}
          {\draw (\i,0) node[above] {$\i$};}
        \foreach \i in {1,2,3}
          {\draw (\i,0) node[below] {$\i$};}
        \draw (0,0) node[anchor=north east] {$O$} (0.1,1.5) node[right] {$y=[x]$};
      \end{tikzpicture}}
    <center>
    \begin{tikzpicture}[line cap=round,line join=round,scale=0.8]
      \draw[\myaxisarrow] (-2.5,0) -- (2.7,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-0.7) -- (0,1.6) node[left] {$y$};
      \foreach \i in {-1,1,2}
        {\draw[line width=0.5pt, densely dashed] (\i,0)--(\i,1);}
      \foreach \i in {-2,-1,0,1}
        {\draw[fill=black,line width=0.6pt] (\i,0) circle (1.5pt) --(\i+1,1);
         \draw[fill=white,line width=0.6pt] (\i+1,1) circle (1.5pt);}
      \foreach \i in {-2,-1,1,2}
        {\draw (\i,0) node[below] {$\i$};}
      \draw (0,0) node[anchor=north east] {$O$} (1.5,1.5) node[right] {$f(x)$};
    \end{tikzpicture}
    </center>
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
    <p>(1) 显然正确; 由 $x$ 与 $-x$ 要么同为有理数, 要么同为无理数知 $D(x)=D(-x)$, (2) 正确; 由 $D(x+1)=D(x)$ 知 (3) 错误 (任一有理数均为 $D(x)$ 的周期); 由 $D(0)=D(2)=1>0=D(\sqrt2)$ 知 (4) 正确.
  </p>
</mysolution>


  <myexercise>
    <p>函数 $y=|x+1|$ 的图象是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>     利用 $y=|x|$ 或 $y=x+1$ 的图象变换可得, 也可先写为分段函数再作图.
    <center>
    \begin{tikzpicture}[line cap=round,line join=round,scale=0.8]
      \draw[\myaxisarrow] (-2.6,0) -- (1.5,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-0.5) -- (0,2.2) node[left] {$y$};
      \draw[line width=0.6pt,smooth,samples=100] plot[domain=-2.6:0.6](\x,{abs(\x+1)});
      \draw (-1,0) node[below] {$-1$}
        (0,0) node[anchor=north east] {$O$}
        (0,1) node[anchor=south east] {$1$}
        (0.2,0.9) node[right] {$f(x)=|x+1|$};
    \end{tikzpicture}
    </center>
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>函数 $y=x^2+2x+1$ 的图象可以由 $y=x^2$ 的图象如何平移得到\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $y=(x+1)^2$, 其图象可由 $y=x^2$ 的图象向左平移 $1$ 个单位长度得到.
</p>
<p>\varexercise 函数 $y=x^2+2x$ 的图象可以由 $y=x^2$ 的图象如何平移得到\,?
</p>
<p>$y=(x+1)^2-1$, 其图象可由 $y=x^2$ 的图象向左平移 $1$ 个单位长度, 再向下平移 $1$ 个单位长度得到.
</p>
<p>\varexercise 函数 $y=x^2-2x$ 的图象可以由 $y=x^2$ 的图象如何平移得到\,?
</p>
<p>$y=(x-1)^2-1$, 其图象可由 $y=x^2$ 的图象向右平移 $1$ 个单位长度, 再向下平移 $1$ 个单位长度得到.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知函数 $f(x)$ 是定义在 $(-3,3)$ 上的偶函数, 
    当 $0\leqslant x< 3$ 时, 
    $f(x)$ 的图象如图 \ref{fig-190414-2055} 所示, 
    那么不等式 $x\cdot f(x)< 0$ 的解集是\,?
    \begin{figure}[htb]
    \small
    \centering
    \begin{tikzpicture}[scale=0.7]
      \draw[\myaxisarrow] (-3.5,0) -- (3.7,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1.5) -- (0,1.7) node[left] {$y$};
      \draw[line width=0.6pt,smooth,samples=100,domain=0:3] 
        plot(\x,{-cos(\x*90)});
      \draw[line width=0.5pt] (1,0) node[below,xshift=2pt] {$1$} --(1,0.15)
        (2,0) node[below] {$2$} --(2,0.15);
      \draw[fill=white] (3,0) circle(2pt) node[below] {$3$};
      \draw (0,0) node[anchor=north east] {$O$};
    \end{tikzpicture}
    \caption{}\label{fig-190414-2055}
    \end{figure}
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    补全 $f(x)$ 的图象, 见右图. $x\cdot f(x)< 0$ 表明 $x$ 和 $f(x)$ 异号, 所以 $x\in (-3,-1)\cup (0,1)$.
    \mymarginpar{\centering
      \begin{tikzpicture}[scale=0.7]
      \draw[\myaxisarrow] (-3.5,0) -- (3.7,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1.5) -- (0,1.7) node[left] {$y$};
      \draw[line width=0.6pt,smooth,samples=100,domain=-3:3] 
        plot(\x,{-cos(\x*90)});
      \foreach \i in {-2,-1,1,2}
      {\draw[line width=0.5pt] (\i,0)--(\i,0.15);}
      \draw[fill=white] (-3,0) circle(2pt) node[below] {$-3$}
        (3,0) circle(2pt) node[below] {$3$};
      \draw (-2,0) node[below] {$-2$} (2,0) node[below] {$2$} 
        (-1,0) node[below,xshift=-4pt] {$-1$} 
        (1,0) node[below,xshift=2pt] {$1$} 
        (0,0) node[anchor=north east] {$O$};
      \end{tikzpicture}}
  </p>
</mysolution>



<p>\lianxi
  \begin{exercise}[s]
    已知函数 $y=f(x+1)$ 的图象过点 $(3,2)$, 那么函数 $f(x)$ 的
    图象一定过哪个点\,?其关于 $x$ 轴的对称图形一定过哪个点\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $2=f(3+1)=f(4)$, 故 $f(x)$ 的图象一定过点 $(4,2)$, 其关于 $x$ 轴的对称图形一定过点 $(-4,2)$.
</p>
<p>\varexercise $f(x)$ 同上, 则 $y=f(2x)$ 的图象一定过哪个点?
</p>
<p>由 $2=f(4)=f(2\cdot 2)$ 知, $y=f(2x)$ 的图象一定过点 $(2,2)$.
  </p>
</mysolution>
</p>
<p>\subsubsection{函数图象的应用}
  <myexample>
<p>已知关于 $x$ 的方程 $|x^2 -4x+3|=mx$ 有四个不等实根, 求实数 $m$ 的取值范围.
  </p>
</myexample>
</p>
<p><mysolution>
    <p>    方法一: 先作出 $f(x)=|x^2-4x+3|$ 和 $g(x)=mx$ 的图象. 
    因为 $g(x)$ 的图象为过原点的直线, 由图象知, 当 $g(x)$ 与 $f(x)$ 在 $[1,3]$ 上的图象相切时, $f(x)=g(x)$ 恰有三个根. 此时 $-(x^2-4x+3)=mx$ 即 $x^2+(m-4)x+3=0$恰在 $[1,3]$ 上有两个相等实根, 且 $m>0$, 则
    \mymarginpar{\centering
      \begin{tikzpicture}[scale=0.7]
      \draw[\myaxisarrow] (-1,0) -- (4.7,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1) -- (0,4.2) node[left] {$y$};
      \draw[line width=0.6pt,smooth,samples=100,domain=-0.15:4.1] 
        plot(\x,{abs((\x)^2-4*\x+3)});
      \draw[line width=0.5pt,smooth,samples=100,domain=1:3,densely dashed] 
        plot(\x,{(\x)^2-4*\x+3});
      \draw[line width=0.5pt,smooth,samples=100,domain=-0.7:4.5] 
        plot(\x,{(4-2*sqrt(3))*\x});
      \draw (1,0) node[below,xshift=-3pt] {$1$} 
        (3,0) node[below,xshift=3pt] {$3$}
        (0,3) node[right] {$3$} (0,0) node[anchor=south east] {$O$}
        (3.4,3) node {$f(x)$} (4.4,1.7) node {$g(x)$};
      \end{tikzpicture}}
    \[(m-4)^2-4\cdot 3=0, \text{\ 且\ } -\frac{m-4}2\in[1,3],\]
    解得 $m=4-2\sqrt3$. 再由图象知, $f(x)=g(x)$ 有四个不等实根时, $m\in(0,4-2\sqrt3)$.
</p>
<p>方法二: 若 $m\leqslant 0$, 则 $x\leqslant 0$, 方程为 $x^2-4x+3=mx$, 
    \mymarginpar{形如 $y=x+\frac{k}x$ ($k>0$) 的函数有时也被称为“对勾函数”, 图象有两条渐近线, 为双曲线.}
    至多有两个不等实根, 与题意不符. 所以 $m>0$ 且 $x>0$, 方程改写为
    \[m=\Big|x+\frac3x-4\Big|,\quad x>0.\]
    作 $h(x)=\Big|x+\frac3x-4\Big|$ 的图象 (可由 $y=x+\frac3x$ 的图象经变换得到).
    \mymarginpar{由两种方法都可以得到, 若原方程恰有三个实根, 则 $m=4-2\sqrt3$.}
    <center>
    \begin{tikzpicture}[line cap=round,line join=round,scale=0.7]
      \draw[\myaxisarrow] (-1,0) -- (5.5,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1) -- (0,2.6) node[left] {$y$};
      \draw[line width=0.6pt,smooth,samples=100] 
        plot[domain=0.5:5](\x,{abs(\x+3/(\x)-4)});
      \draw[line width=0.6pt,smooth,samples=100,densely dashed]
        plot[domain=1:3](\x,{\x+3/(\x)-4});
      \draw[densely dashed] (3,-1)--(5.3,1.3) 
        (0,{4-2*sqrt(3)})--(4.2,{4-2*sqrt(3)});
      \draw (0,0) node[anchor=north east] {$O$} 
        (1,0) node[below,xshift=-4pt] {$1$}
        (3,0) node[below,xshift=4pt] {$3$}
        (0,{4-2*sqrt(3)}) node[left] {$4-2\sqrt3$}
        (1,2) node[right] {$h(x)$};
    \end{tikzpicture}
    </center>
    故 $h(x)=m$ 有四个不等实根时, $m\in(0,4-2\sqrt3)$.
  </p>
</mysolution>

<myexercise>
    <p>已知定义域为 $(-\infty ,0)\cup (0,+\infty)$ 的函数 $f(x)$ 是偶函数,
    且在 $(-\infty ,0)$ 上是单调增函数. 若 $f(-3)=0$, 
    则不等式 $\frac{x}{f(x)}< 0$ 的解集是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    作 $f(x)$ 图象的大致示意图. 
    \mymarginpar{\centering
    \begin{tikzpicture}[line cap=round,line join=round,scale=0.4]
      \draw[\myaxisarrow] (-4.5,0) -- (4.5,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-2.5) -- (0,4) node[left] {$y$};
      \draw[line width=0.6pt,smooth,samples=100] 
        plot[domain=-4:4](\x,{(9-(\x)^2)/3});
      \draw[fill=white] (0,0) node[anchor=north east] {$O$} 
        (-3,0) circle (3pt) node[below,xshift=5pt] {$-3$}
        (3,0) circle (3pt) node[below,xshift=-3pt] {$3$}
        (0,3) circle (3pt);
    \end{tikzpicture}}
    $\frac{x}{f(x)}< 0$ 表明 $x$, $f(x)$ 异号, 所以 $x\in(-3,0)\cup (3,+\infty)$.
  </p>
</mysolution>

<myexercise>
    <p>如图 \ref{fig-190414-2120}, 
    函数 $f(x)$ 的图象由两条射线和三条线段组成. 
    若对任意的 $x\in \mathbf{R}$, 都有 $f(x)>f(x-1)$, 
    则正实数 $a$ 的取值范围是\,?
    \begin{figure}[htb]
    \small
    \centering
    \begin{tikzpicture}[scale=0.7]
      \draw[\myaxisarrow] (-4.3,0) -- (4.3,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1.3) -- (0,1.7) node[left] {$y$};
      \draw[line width=0.5pt] (-4,-1)--(-2,1)--(-1,1)--(1,-1)--(2,-1)--(4,1);
      \draw[line width=0.5pt,dash pattern= on 2pt off 2pt] 
        (-2,0)--(-2,1) (-1,0)--(-1,1)--(0,1) 
        (0,-1)--(1,-1)--(1,0) (2,0)--(2,-1);
      \draw (-3.3,0) node[above] {$-3a$} (-2,0) node[below] {$-2a$}
        (-1,0) node[below] {$-a$} (1,0) node[above] {$a$}
        (2,0) node[above] {$2a$} (3.2,0) node[below] {$3a$}
        (0,1) node[right] {$a$} (0,-1) node[left] {$-a$}
        (0,0) node[anchor=north east] {$O$}
        (3,1) node {$f(x)$};
    \end{tikzpicture}
    \caption{}\label{fig-190414-2120}
    \end{figure}
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    由 $f(x)$ 在 $[-2a,4a]$ 上的图象知, $0< 6a< 1$, 故 $a\in\Big(0,\frac16\Big)$.
  </p>
</mysolution>
