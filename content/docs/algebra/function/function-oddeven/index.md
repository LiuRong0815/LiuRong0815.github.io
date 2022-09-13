---
# bookCollapseSection: true
title: 函数的奇偶性
weight: 3
bookHidden: true
prevPage: /docs/algebra/function/function-monotone
prevPageTitle: 函数的单调性
nextPage: /docs/algebra/function/function-graph
nextPageTitle: 函数的图象
---

# 函数的奇偶性


<p>函数的\myindex{奇偶性} (odevity) 描述的是其图象的对称性. 
  \mymarginpar{一般地, 设函数 $f(x)$ 的定义域为 $\mathbf{R}$, 则\\
    \hbox{\quad} $f(x)$ 关于直线 $x=a$ 对称 \\
     $\Leftrightarrow f(a+x)=f(a-x)$\\
     $\Leftrightarrow f(x)=f(2a-x)$;\\
    \hbox{\quad} $f(x)$ 关于点 $(a,b)$ 对称\\
     $\Leftrightarrow f(a+x)+f(a-x)=2b$.}
  若图象关于 $y$ 轴对称, 则称其为<strong>偶函数</strong>;  若图象关于原点对称, 则称其为<strong>奇函数</strong>. 设函数为 $f(x)$, 则  \[\begin{aligned}
    &f(x)\text{\,为偶函数}\Leftrightarrow f(-x)=f(x)\Leftrightarrow f(-x)-f(x)=0;\\
    &f(x)\text{\,为奇函数}\Leftrightarrow f(-x)=-f(x)\Leftrightarrow f(-x)+f(x)=0.
  \end{aligned}\]
  由定义可以知道, 
</p>
<p>(1) 判断函数奇偶性之前, 应确保其定义域关于原点对称;
</p>
<p>(2) 函数按奇偶性可分为: 奇函数, 偶函数, 既奇又偶函数 (可以认为只有一个), 非奇非偶函数;
</p>
<p>(3) 若 $0$ 在奇函数 $f(x)$ 的定义域中, 则必有 $f(0)=0$ (并非充要条件);
</p>
<p>(4) $f(x)$ 为偶函数 $\Leftrightarrow$ $f(x)$, $f(|x|)$, $f(-x)$ 中有两者相等.
</p>
<p>

</p>
<p><myexercise>
    <p>函数 $f(x)=x^3 -x$ 是$\underline{\qquad}$函数. (填“奇”或“偶”.)
    \mymarginpar{一般地, 奇函数的和为奇函数, 偶函数的和为偶函数.}
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(-x)+f(x)=0$, 则 $f(x)$ 为奇函数.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>若 $f(x)=(m-2)x^2 +(m-1)x+3$ 是偶函数, 求实数 $m$ 的值.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    由 $f(x)=f(-x)$ 整理得 $m=1$.
    \mymarginpar{一般化, 若 $f(x)=ag(x)+bh(x)$, 而 $g(x)$ 为奇函数, $h(x)$ 为偶函数, 则\\
      \hbox{\qquad}  $f(x)$ 为奇函数 $\Leftrightarrow b=0$;\\
      \hbox{\qquad}  $f(x)$ 为偶函数 $\Leftrightarrow a=0$.}
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>设 $f(x)$ 是 $\mathbf{R}$ 上的奇函数, 当 $x\leqslant 0$ 时, $f(x)=2x^2-x$, 求 $f(1)$.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(1)=-f(-1)=-3$.
  </p>
</mysolution>

<myexample>
<p>已知 $f(x)$, $g(x)$ 分别是定义在 $\mathbf{R}$ 上的偶函数和奇函数,
    且 $f(x)-g(x)= x^3 +x^2 +1$, 那么 $f(1)+g(1)=$\,?
  </p>
</myexample>
</p>
<p><mysolution>
    <p>    由已知, $f(-x)-g(-x)=-x^3+x^2+1$ 即 $f(x)+g(x)=-x^3+x^2+1$, 所以 $f(1)+g(1)=1$.
</p>
<p>\varexercise 条件不变, 求 $f(1)$.
</p>
<p>由题, $f(1)-g(1)=3$, $f(1)+g(1)=1$, 解得 $f(1)=2$.
</p>
<p>\varexercise 条件不变, 求 $f(1)+g(2)$.
    \mymarginpar{$\mathbf{R}$ 上的任何函数可写为一个偶函数与一个奇函数之和.}
</p>
<p>解方程组
    \[\left\{\!\!\begin{array}{l}
        f(x)-g(x)= x^3 +x^2 +1,\\
        f(x)+g(x)=-x^3+x^2+1
      \end{array}\right. \quad \text{得\ } 
      \left\{\!\!\begin{array}{l}
        f(x)= x^2+1,\\
        g(x)= -x^3,
      \end{array}\right.\]
    所以 $f(1)+g(2)=2-8=-6$.
  </p>
</mysolution>
</p>
<p>\lianxi
  <myexercise>
    <p>若函数 $f(x)$ 为奇函数, 当 $x\geqslant 0$ 时, $f(x)=x^2+x$,
    则 $f(-2)$ 的值为\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(-2)=-f(2)=-6$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知 $f(x)$ 为奇函数, $g(x)=f(x)+9$, $g(-2)=3$,那么 $f(2)=$\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $g(-2)=f(-2)+9$ 即 $3=-f(2)+9$, 则 $f(2)=6$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知 $f(x)$ 是奇函数, $g(x)$ 是偶函数, 且 $f(-1)+g(1)=2$, 
    $f(1)+g(-1)=4$, 那么 $g(1)=$\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $-f(1)+g(1)=2$ 且 $f(1)+g(1)=4$, 则 $g(1)=3$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知 $\mathbf{R}$ 上的奇函数 $f(x)$ 满足 $f(x+2)=-f(x)$,
    那么 $f(-6)=$\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    由已知 $f(x)=-f(x+2)$, 所以 
    \mymarginpar{$\mathbf{R}$ 上的奇函数 $f(x)$ 必满足 $f(0)=0$.}
    \[f(-6)=-f(-4)=f(-2)=-f(0)=0.\]
  </p>
</mysolution>
</p>
<p>\subsubsection{单调性和奇偶性综合}
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

<myexercise>
    <p>若函数 $f(x)=(x+a)(x-4)$ 为偶函数, 则 $a=$\,?
    \mymarginpar{可以验证:\\
      \hbox{\quad} 多项式函数为奇函数\\
      $\Leftrightarrow$ 式中只有奇数次项;\\
      \hbox{\quad} 多项式函数为偶函数\\
      $\Leftrightarrow$ 式中只有偶数次项.}
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(-x)=f(x)$, 则 $a=4$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>下列函数中, 既是偶函数又在 $(0,+\infty)$ 上单调递减的是\,?
</p>
<p>(1) $y=\frac1x$;\qquad (2) $y= \mathrm{e}^{-x}$;\qquad
    (3) $y= -x^2+1$;\qquad (4) $y= \lg|x|$.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    (1) 奇函数且在 $(0,+\infty)$ 上 $\searrow$; 
    (2) 无奇偶性且在 $(0,+\infty)$ 上 $\searrow$; 
    (3) 偶函数且在 $(0,+\infty)$ 上 $\searrow$; 
    (4) 偶函数且在 $(0,+\infty)$ 上 $\nearrow$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>若函数 $f(x)= \frac1{2^x-1}+a$ 为奇函数, 则 $a=$\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(-x)+f(x)=0$, 则 $a=\frac12$.
    \mymarginpar{题中 $f(x)$ 的定义域中无 $0$, 故不能用 $f(0)=0$ 来求解.}
  </p>
</mysolution>


<myexercise>
    <p>定义域为 $\mathbf{R}$ 的四个函数 $y=x^3$, $y=2^x$, $y=x^2+1$, 
    $y=2\sin x$ 中, 奇函数的个数是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $y=x^3$, $y=2\sin x$ 为奇函数, 共两个.
  </p>
</mysolution>

<myexercise>
    <p>设函数 $f(x)= a\sin x+x^2$, 若 $f(1)=0$, 则 $f(-1)$ 的值为\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    因为 $y=\sin x$ 为奇函数, 所以
    \[f(1)=a\sin1+1,\quad (-1)=-a\sin1+1,\]
    相加得 $f(1)+f(-1)=2$, 则 $f(-1)=2$.
</p>
<p>\varexercise 设函数 $f(x)= a\sin x+b\tan x+x^2$, 若 $f(1)=0$, 则 $f(-1)$ 的值为\,?
</p>
<p>同上方法可知 $f(-1)=1$.
</p>
<p>\varexercise 设函数 $f(x)= \frac{a\sin x}{\mathrm{e}^x+\mathrm{e}^{-x}}+x^2$, 若 $f(1)=0$, 则 $f(-1)$ 的值为\,?
</p>
<p>仍然可得 $f(-1)=1$.
  </p>
</mysolution>

<myexercise>
    <p>若函数 $f(x)=kx^2+(k-1)x+2$ 是偶函数, 求 $f(x)$ 的单调递减区间.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    由题 $k=1$, $f(x)=x^2+2$, 则 $f(x)$ 的单调递减区间是 $(-\infty,0]$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知函数 $f(x)$ 为偶函数, 且当 $x< 0$ 时, $f(x)=x^2 -\frac1x$,
    求 $f(1)$.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(1)=f(-1)=2$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知偶函数 $f(x)$ 在区间 $[0,+\infty )$ 上单调递增. 
    若 $f(2x-1)< f\Big(\frac13\Big)$, 则 $x$ 的取值范围是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(|2x-1|)=f(2x-1)< f\Big(\frac13\Big)$, 则 $|2x-1|< \frac13$,  $x\in\Big(\frac13,\frac23\Big)$.
</p>
<p>\varexercise 若 $f(x)$ 改为奇函数, 其余条件不变, 则 $x$ 的取值范围是\,?
</p>
<p>此时 $f(x)$ 在 $\mathbf{R}$ 上 $\nearrow$, 则 $2x-1< \frac13$ 即 $x\in\Bigl(-\infty,\frac23\Bigr)$.
  </p>
</mysolution>



<p>\begin{example}\label{exa:201115-1045}
    函数 $f(x)= x+\dfrac1x$ ($x\neq 0$) 是奇函数还是偶函数? 写出其单调区间.
</p>
</myexample>
<mysolution>
    <p>因为 
    \[f(-x)= (-x)+\frac1{-x}= -\biggl(x+\frac1x\biggr)= -f(x),\]
    所以 $f(x)$ 是奇函数.
</p>
<p>当 $x$ 是充分小的正数时, $f(x)\approx \dfrac1x$; 当 $x$ 是充分大的正数时, $f(x)\approx x$. 再结合
    \[f\biggl(\frac14\biggr)= f(4)= \frac{17}4,\ 
      f\biggl(\frac13\biggr)= f(3)= \frac{10}3,\ 
      f\biggl(\frac12\biggr)= f(2)= \frac{5}2,\ 
      f(1)= 2,\]
    可以描点作图如下 (第三象限的图形与第一象限的图形关于原点对称):
    <center>
        \includegraphics[scale=1]{2020-1115-1100-crop}
    </center>
    由图可以看出 $f(x)$ 的单调递增区间为 $(-\infty,-1]$ 和 $[1,+\infty)$, 单调递减区间为 $(-1,0)$ 和 $(0,1)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201115-1045} 中的函数 $f(x)= x+\dfrac1x$ ($x\neq 0$) 一般形象地称为“对勾函数”, 第一象限图形的最低点 $(1,2)$ 可由均值不等式得到. $f(x)$ 的图形有两条渐近线: $y=x$ 和 $x=0$ (即 $y$ 轴), 符合双曲线的特点 (有两条渐近线). 观察 $f(x)$ 的图形可知, 若 $x\geqslant 3$, 则 $f(x)\geqslant f(3)$, 即此时 $f_{\min}=f(3)$. 类似地, 若 $x\geqslant \dfrac12$, 则 $f_{\min}=f(1)$. 
</p>
<p>一般地, $f(x)= x+\dfrac{k}x$ ($k>0$, $x\neq 0$) 均可称为“对勾函数”. 由与前面类似的分析可得, $f(x)$ 是奇函数, 有两条渐近线 $y=x$ 和 $x=0$, 第一象限图形的最低点为 $(\sqrt{k},2\sqrt{k})$, 单调递增区间为 $(-\infty,-\sqrt{k}]$ 和 $[\sqrt{k},+\infty)$, 单调递减区间为 $(-\sqrt{k},0)$ 和 $(0,\sqrt{k})$.
</p>

<p>\begin{example}\label{exa:201115-1210}
    已知 $f(x)= ax^7-bx^5+cx^3+2$, 且 $f(-5)=m$, 求 $f(-5)+f(5)$ 的值.
</p>
</myexample>
<mysolution>
    <p>直接代入知,
    \[\begin{aligned}
    f(-5)+f(5)
      ={}& [a\cdot (-5)^7- b\cdot (-5)^5+ c\cdot (-5)^3+2] \\
         & + [a\cdot 5^7- b\cdot 5^5+c\cdot 5^3+2]\\
      ={}& 4.\end{aligned}\]
</p>
</mysolution>
</p>
<p>例 \ref{exa:201115-1210} 中的“$f(-5)=m$”是多余的条件. 如果注意到 $g(x)=ax^7-bx^5+cx^3$ 是奇函数, 则可以简洁地得到更一般地结论:
\[f(-x)+f(x)= [g(-x)+g(x)]+2\cdot 2= 4.\]
</p>

<p>\subsection{利用函数性质解题}
</p>
<p>常见的函数性质有: 单调性, 奇偶性, 对称性, 周期性等. 解题时, 适当运用这些性质可以达到事半功倍的效果.
</p>
<p>\begin{example}\label{exa:201129-0950}
    若 $a>\dfrac1a$, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>方法一: 不等式化为 
    \[a-\frac1a>0\Rightarrow \frac{a^2-1}a>0\Rightarrow (a^2-1)a>0,\]
    所以
    \[\left\{\!\!\begin{array}{l}
        a^2-1>0,\\
        a>0,
        \end{array}\right.\ \text{或}\quad
      \left\{\!\!\begin{array}{l}
        a^2-1< 0,\\
        a< 0,
        \end{array}\right.\]
    解得 $a>1$ 或 $a< -1$, 即 $a\in(-\infty,-1)\cup(1,+\infty)$.
</p>
<p>方法二: 画出函数 $f(a)=a$ 和 $g(a)=\dfrac1a$ 的图形. 不等式表明 $f(a)>g(a)$, 对应前者图形在后者图形上方的情形 (即直线在上方, 双曲线在下方). 由图可知 $a\in(-\infty,-1)\cup(1,+\infty)$.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1129-0950-crop}
    </center>
</p>
<p>方法三: 也可以将不等式化为 $a-\dfrac1a>0$, 令 $h(a)= a-\dfrac1a$, 再作图求解. 只需留意函数 $h(a)$ 在 $(-\infty,0)$ 和 $(0,+\infty)$ 上均单调递增, 且与横轴的交点为 $(-1,0)$ 和 $(1,0)$ (参考“2020 年 11 月 8 日答疑记录”的例 \ref{exa:201206-1410}).
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 例 \ref{exa:201129-0950} 的方法一是代数解法, 变形后的式子 $(a^2-1)a>0$ 是三次不等式, 仍需要分类讨论, 各自求解后再取并集.
</p>
<p>(2) 方法二和方法三均利用了函数图形 (前者两个, 后者一个), 用这种方法时需要根据题意构造容易画出大致图形的函数, 也就是要事先了解函数的特点 (单调性、奇偶性、对称性、与坐标轴的交点, 等等).
</p>
</myremark>
</p>
<p>\begin{example}\label{exa:201129-1010}
    设定义在 $(-1,1)$ 上的奇函数 $f(x)$ 是增函数, 且 $f(a)+f(2a-1)< 0$, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 是奇函数, 所以不等式化为 
    \[f(a)< -f(2a-1)=f(1-2a).\]
    结合 $f(x)$ 是定义在 $(-1,1)$ 上的增函数知
    \[\left\{\!\!\begin{array}{l}
        -1< a< 1,\\
        -1< 1-2a< 1,\\
        a< 1-2a,
        \end{array}\right.\ \text{解得}\quad
      0< a< \frac13,\]
    即 $a\in\biggl(0,\dfrac13\biggr)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201129-1010} 中主要利用“$f(x)$ 是增函数”将抽象的不等式 (没有具体解析式的不等式) 
\[f(a)< f(1-2a)\]
化为具体的不等式 
\[a< 1-2a.\]
再如, 若 $f(x)$ 是减函数, 则由 $f(a)< f(2a+1)$ 可知 $a>2a+1$. 在去掉“$f$”时, 也需要注意 $f$ 的作用范围 (即题中 $f(x)$ 的定义域).
</p>

<p>\begin{example}\label{exa:201206-1300}
    已知函数 $f(x)$ 为奇函数, 且当 $x>0$ 时, $f(x)= x^2+\dfrac1x$, 求当 $x< 0$ 时 $f(x)$ 的解析式.
</p>
</myexample>
<mysolution>
    <p>方法一: 若 $x< 0$, 则 $-x>0$, 由题意, 此时 
    \[f(-x)= (-x)^2+\frac1{-x}= x^2-\frac1x.\]
    因为 $f(x)$ 为奇函数, 所以 $f(-x)= -f(x)$, 代入上式可得
    \[-f(x)= x^2-\frac1x,\quad\text{即}\quad f(x)=-x^2+\frac1x.\]
    此即为当 $x< 0$ 时 $f(x)$ 的解析式.
</p>
<p>方法二 (将方法一的步骤压缩): 因为 $f(x)$ 为奇函数, 所以当 $x< 0$ 时, 
    \[f(x)= -f(-x)= -\biggl(x^2-\frac1x\biggr)= -x^2+\frac1x.\]
</p>
</mysolution>


<myexample>
<p>设奇函数函数 $f(x)$ 在 $(-\infty,+\infty)$ 上单调递减, 且 $f(1)=-1$, 求不等式 $-1\leqslant f(x-1)\leqslant 1$ 的解集.
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 为奇函数, 所以由 $f(1)=-1$ 可知 $f(-1)=1$, 不等式化为
    \[f(1)\leqslant f(x-1)\leqslant f(-1).\]
    又因为 $f(x)$ 在 $(-\infty,+\infty)$ 上单调递减, 所以
    \[1\geqslant x-1\geqslant -1,\quad\text{解得}\quad 
        0\leqslant x\leqslant 2,\]
    即所求解集为 $[0,2]$.
</p>
</mysolution>
</p>
<p>\begin{example}\label{exa:201204-2125}
    已知定义在 $\realnum$ 上的奇函数 $f(x)$ 满足 $f(x+4)=f(x)$ 且 $f(1)=1$, 求 $f(3)+f(4)+f(5)$ 的值.
</p>
</myexample>
<mysolution>
    <p>对定义在 $\realnum$ 上的奇函数 $f(x)$, 恒有 $f(-x)=-f(x)$. 令 $x=0$ 得 $f(0)=-f(0)$, 所以 $f(0)=0$. 结合 $f(x+4)=f(x)$ 知,
    \[\begin{aligned}
        \text{令 $x=0$:}&\ f(4)=f(0)=0,\\
        \text{令 $x=1$:}&\ f(5)=f(1)=1,\\
        \text{令 $x=-1$:}&\ f(3)=f(-1)=-f(1)=-1.
    \end{aligned}\]
    所以 $f(3)+f(4)+f(5)= (-1)+0+1=0$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 由上面的解法可知, 条件“$f(1)=1$”是多余的, 因为只需要推出 $f(4)=0$ 和 $f(3)=-f(1)$ 即可得到最终结论.
</p>
<p>(2) 例 \ref{exa:201204-2125} 中还证明了一个结论 (可当作定理直接使用): 若 $f(x)$ 为定义在 $\realnum$ 上的奇函数, 则 $f(0)=0$.
</p>
</myremark>

<myexample>
<p>(1) 若 $f(x)$ 为奇函数, 当 $x>0$ 时, $f(x)=x(1-\sqrt[3]{x})$, 求当 $x< 0$ 时, $f(x)$ 的解析式;
</p>
<p>(2) 若 $f(x)$ 为偶函数, 当 $-1\leqslant x< 0$ 时, $f(x)=\sqrt[5]{x}+1$, 求当 $0< x\leqslant 1$ 时, $f(x)$ 的解析式;
</p>
</myexample>
<mysolution>
    <p>以下过程较简略, 更详细的过程可参考“2020 年 11 月 14 日答疑记录”的例 \ref{exa:201206-1300} 方法一.
</p>
<p>(1) 因为 $f(x)$ 为奇函数, 所以当 $x< 0$ 时,
    \[f(x)= -f(-x)= -(-x)(1-\sqrt[3]{-x})= x(1+\sqrt[3]{x}).\]
</p>
<p>(2) 因为 $f(x)$ 为偶函数, 所以当 $0< x\leqslant 1$ 时,
    \[f(x)= f(-x)= \sqrt[5]{-x}+1= -\sqrt[5]{x}+1.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>若函数 $f(x)$ 在 $\realnum$ 上为偶函数, 且当 $x>0$ 时, $f(x)=-x+1$, 求 $f(x)< -1$ 的解集.
</p>
</myexample>
<mysolution>
    <p>函数 $f(x)$ 在 $\realnum$ 上为偶函数, 表明其图形关于 $y$ 轴对称. 直接根据对称性画图可知, $x\in(-\infty,-2)\cup(2,+\infty)$.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1320-crop}
    </center>
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)$ 为 $(-1,1)$ 上的奇函数且单调递增, 解不等式 
    \[f(2x-1)+f(-x+1)>0.\]
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 为奇函数, 不等式化为
    \[f(2x-1)> -f(-x+1)= f(x-1).\]
    又因为 $f(x)$ 在 $(-1,1)$ 上单调递增, 所以
    \[1> 2x-1> x-1>-1,\quad\text{解得}\quad x\in(0,1).\]
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \dfrac{2x+m}{x^2+1}$ 在定义域 $\mathbf{R}$ 上是奇函数.
</p>
<p>(1) 求实数 $m$ 的值;
</p>
<p>(2) 讨论函数 $f(x)$ 在 $[2,3]$ 上的单调性, 并求对应的最大值和最小值.
</p>
</myexample>
<mysolution>
    <p>(1) 因为 $f(x)$ 是奇函数, 所以 
    \[f(-x)= -f(x),\quad\text{即}\quad
    \dfrac{2\cdot(-x)+ m}{(-x)^2+1}= -\dfrac{2x+m}{x^2+1},\]
    整理可得, $m=0$.
</p>
<p>(2) 由 (1) 和 $x\in[2,3]$ 可知,
    \[f(x)= \frac{2x}{x^2+1}= \frac{2}{x+\dfrac1x}.\]
    因为“对勾函数”$g(x)= x+\dfrac1x$ 在 $[2,3]$ 上单调递增, 所以 
    \[g(x)\in [g(2),g(3)]= \biggl[\dfrac52,\dfrac{10}3\biggr],\]
    从而
    \[f(x)= \frac{2}{g(x)}\in \biggl[\dfrac35,\dfrac45\biggr].\]
</p>
</mysolution>

<myexample>
<p>已知 $f(x)$ 是定义在 $\mathbf{R}$ 上的偶函数, 且当 $x\in(-\infty,0]$ 时, $f(x)= 2^x+\dfrac13$, 求 $f\biggl(\log_2 \dfrac32\biggr)$ 的值.
</p>
</myexample>
<mysolution>
    <p>因为 $\log_2 \dfrac32> \log_2 1=0$, 而已知的是当 $x\in(-\infty,0]$ 时的解析式, 且 $f(x)$ 是定义在 $\mathbf{R}$ 上的偶函数知, 
    \[f\biggl(\log_2 \dfrac32\biggr)
        = f\biggl(-\log_2 \dfrac32\biggr)
        = 2^{-\log_2 \frac32}+\dfrac13.\]
    结合对数运算法则 (参考“2020 年 11 月 8 日答疑记录”的第二部分), 
    \[2^{-\log_2 \frac32}= 2^{\log_2 \frac23}= \frac23,\]
    所以 $f\biggl(\log_2 \dfrac32\biggr)=1$.
</p>
</mysolution>

<myexample>
<p>举例说明下列命题为假命题: 
</p>
<p>(1) 若存在 $x_0$ 使得 $f(-x_0)= -f(x_0)$, 则 $f(x)$ 不是偶函数;
</p>
<p>(2) 若 $f(x)$ 在 $\mathbf{R}$ 上单调递减, 则一定存在 $x_0\in \mathbf{R}$ 使得 $f(x_0)< 1$.
</p>
</myexample>
<mysolution>
    <p>本题各小题均应找出适当的 $f(x)$, 使得其满足前提条件, 但不满足结论. 解题时需要充分了解各类函数的特点.
</p>
<p>(1) 此时需要找到偶函数 $f(x)$ 和某个 $x_0$, 使得 $f(-x_0)= -f(x_0)$. 因为对于偶函数 $f(x)$, 必有 $f(-x_0)= f(x_0)$, 所以 $f(x_0)= -f(x_0)$, 只能 $f(x_0)=0$. 分析表明, 只需找与 $x$ 轴有交点的偶函数, 并取交点横坐标为 $x_0$. 可取 $f(x)= x^2$, $x_0=0$, 或 $f(x)= x^2-1$, $x_0=\pm1$, 或 $f(x)= \cos x$, $x_0=\pm\dfrac\pi2$, 或 $f(x)= |x|$, $x_0=0$, 等等.
</p>
<p>(2) 此时需要找到在 $\mathbf{R}$ 上单调递减的函数 $f(x)$, 但其值恒大于等于 $1$. 因为幂函数、指数函数、对数函数、三角函数中, 只有单调递减的指数函数永远大于零, 所以应利用此类函数, 并适当变形得到所求的 $f(x)$. 可取 $f(x)= 0.5^x+1$, 或 $f(x)= 0.2^x+2$, 等等. 一般地, $f(x)= a^x+b$ ($0< a< 1$, $b\geqslant 1$) 均可行.
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= a- \dfrac1{2^x+1}$ 为奇函数.
</p>
<p>(1) 求 $a$ 的值, 并判断 $f(x)$ 的单调性;
</p>
<p>(2) 若不等式 $f(x-x^2)+ f(x+a)< 0$ 恒成立, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 由已知, $f(-x)= -f(x)$, 即
    \[a- \dfrac1{2^{-x}+1}= -\biggl(a- \dfrac1{2^x+1}\biggr),\]
    整理得
    \[\begin{aligned}
        a&= \frac12\biggl(\dfrac1{2^x+1}+ \dfrac1{2^{-x}+1}\biggr)
        = \frac12\cdot \dfrac{2^{-x}+1+ 2^x+1}{(2^x+ 1)(2^{-x}+ 1)}\\
        &= \frac12\cdot \dfrac{2^{-x}+1+ 2^x+1}{1+ 2^x+ 2^{-x}+ 1}
        = \frac12.
    \end{aligned}\]
    上式也可计算如下
    \[\begin{aligned}
        a&= \frac12\biggl(\dfrac1{2^x+1}+ \dfrac1{2^{-x}+1}\biggr)
        = \frac12\biggl(\dfrac1{2^x+1}+ \dfrac{2^x}{2^x\cdot 2^{-x}+2^x}\biggr)\\
        &= \frac12\cdot \biggl(\dfrac1{2^x+1}+ \dfrac{2^x}{1+2^{x}}\biggr)
        = \frac12.
    \end{aligned}\]
    因此 $f(x)= \dfrac12- \dfrac1{2^x+1}$.
</p>
<p>由复合函数单调性知, 当 $x\nearrow$ 时, $2^x+1\nearrow$ 且恒正, 所以 $\dfrac1{2^x+1}\searrow$, 而
    \[f(x)= \dfrac12- \dfrac1{2^x+1}\nearrow,\]
    即 $f(x)$ 为单增函数. 判断单调性也可以直接用定义: 任取 $x_1< x_2$, 计算可知
    \[f(x_1)-f(x_2)= \dfrac{2^{x_1}- 2^{x_2}}{(2^{x_1}+ 1)(2^{x_2}+ 1)}< 0.\]
</p>
<p>(2) 因为 $f(x)$ 为奇函数, 所以不等式化为
    \[f(x+a)< -f(x-x^2)= f(x^2-x).\]
    又因为 $f(x)$ 为单增函数, 所以
    \[x+a< x^2-x,\quad\text{即}\quad x^2-2x-a>0.\]
    上式恒成立的充要条件是
    \[\Delta= (-2)^2- 4\cdot(-a)< 0,\quad\text{解得}\quad
        a< -1,\]
    所求取值范围是 $(-\infty,-1)$.
</p>
</mysolution>

<p>\begin{example}\label{exa:201115-1140}
    设定义在 $(-1,1)$ 上的奇函数 $f(x)$ 是增函数, 解关于 $a$ 的不等式 
    \[f(a)+f(2a-1)< 0.\]
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 是奇函数, 所以已知不等式化为
    \[f(a)< -f(2a-1)= f(1-2a).\]
    再结合 $f(x)$ 在 $(-1,1)$ 上是增函数可知
    \[\left\{\!\!\begin{array}{l}
        -1< a< 1,\ -1< 1-2a< 1\\
        a< 1-2a,
        \end{array}\right.\ \text{解得}\quad a\in\biggl(0,\frac13\biggr).\]
</p>
</mysolution>
<myremark>
    <p>例 \ref{exa:201115-1140} 中的不等式 $f(a)+f(2a-1)< 0$ 可以称为“抽象不等式”(因为没有具体的表达式), 这类不等式一般先化为“$f(a)< f(b)$”的形式, 再利用函数的单调性去掉“$f$”而转化为具体不等式“$a< b$”或“$a>b$”.
</p>
</myremark>


<p><myexample>
<p>已知函数 $f(x)=\dfrac{ax^2+b}x$, 且 $f(1)=2$, $f(2)=\dfrac52$.
</p>
<p>(1) 确定函数 $f(x)$ 的解析式, 并判断其奇偶性;
</p>
<p>(2) ({\bfseries 选学}) 用定义证明函数 $f(x)$ 在区间 $(-\infty,-1)$ 上单调递增;
</p>
<p>(3) 求满足 $f(1+2t^2)- f(3+t^2)< 0$ 的实数 $t$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 由题意,
    \[\left\{\!\!\begin{array}{l}
        a+b=2,\\
        \dfrac{4a+b}2= \dfrac52,
       \end{array}\right.\ \text{解得}\quad
       \left\{\!\!\begin{array}{l}
        a=1,\\
        b=1,
       \end{array}\right.\]
    所以 $f(x)=\dfrac{x^2+1}x$. 因为
    \[f(-x)= \frac{(-x)^2+1}{-x}
        = -\frac{x^2+1}x= -f(x),\]
    且 $f(x)$ 的定义域为 $(-\infty,0)\cup (0,+\infty)$, 关于原点对称, 所以 $f(x)$ 为奇函数.
</p>
<p>(2) 任取 $x_1< x_2< -1$, 则
    \[\begin{aligned}
        f(x_1)-f(x_2)
        &= \frac{x_1^2+1}{x_1}- \frac{x_2^2+1}{x_2}
         = \frac{x_2(x_1^2+1)- x_1(x_2^2+1)}{x_1x_2}\\
        &= \frac{x_1^2 x_2- x_1 x_2^2+x_2- x_1}{x_1x_2}
         = \frac{x_1 x_2(x_1- x_2)- (x_1- x_2)}{x_1x_2}\\
        &= (x_1- x_2)\frac{x_1 x_2- 1}{x_1x_2}.
        \end{aligned}\]
    由 $x_1< x_2< -1$ 知,
    \[x_1- x_2< 0,\quad x_1 x_2> 1\ \text{即}\ x_1 x_2- 1>0,\]
    所以 $f(x_1)-f(x_2)< 0$, 说明函数 $f(x)$ 在区间 $(-\infty,-1)$ 上单调递增.
</p>
<p>(3) 不等式化为 $f(1+2t^2)< f(3+t^2)$. 因为 $1+2t^2>1$, $3+t^2>1$, 且
    \[f(x)= \dfrac{x^2+1}x= x+\dfrac1x\quad (\text{对勾函数})\]
    在 $(1,+\infty)$ 上单调递增, 所以前述不等式等价于 
    \[1+2t^2< 3+t^2,\quad \text{解得}\ 
        t\in(-\infty,-\sqrt2)\cup(\sqrt2,+\infty).\]    
</p>
</mysolution>
