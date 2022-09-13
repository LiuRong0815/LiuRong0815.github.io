---
# bookCollapseSection: true
title: 函数的单调性
weight: 2
bookHidden: true
prevPage: /docs/algebra/function/function-def
prevPageTitle: 函数的定义
nextPage: /docs/algebra/function/function-oddeven
nextPageTitle: 函数的奇偶性
---

# 函数的单调性

<p>函数的单调性描述的是其图象的变化趋势. 当沿 $x$ 轴正向观察函数 $f(x)$ 的图象时, 若图象上升, 则称 $f(x)$ 单调递增 (单增), 并称 $f(x)$ 为增函数; 若图象下降, 则称 $f(x)$ 单调递减 (单减), 并称 $f(x)$ 为减函数.
</p>

<img alt="增函数" src="/figs/2022/2022-09/2022-0913-2045.svg"></img>

<img alt="减函数" src="/figs/2022/2022-09/2022-0913-2050.svg"></img>

<p>函数也可以在其定义域的一部分上单调递增或单调递减. 设函数 $f(x)$ 的定义域为 $D$, $A\subseteq D$, 任取 $x_1$, $x_2\in A$ 满足 $x_1< x_2$, 则 \[\begin{aligned}
    &f(x_1)< f(x_2)\Leftrightarrow f(x)\ \text{在 $A$ 上单调递增},\\
    &f(x_1)> f(x_2)\Leftrightarrow f(x)\ \text{在 $A$ 上单调递减}.
\end{aligned}\]
将上面的 $A$ 取成 $D$ 时, 就得到函数 $f(x)$ 在其定义域 $D$ 上单调递增或单调递减的定义.
</p>
<p>初中常见函数的单调性的决定因素如下: 
</p>
<p>(1) 一次函数 $f(x)=kx+b$ ($k\neq 0$): $k< 0$ 时单调递减, $k> 0$ 时单调递增;
</p>
<p>(2) $f(x)=\frac{k}x$: $k>0$ 时分段 单调递减, $k< 0$ 时分段 单调递增;
</p>
<p>$f(x)=ax^2+bx+c$: $a$ 决定抛物线开口方向, $-\frac{b}{2a}$ 决定对称轴位置;
</p>

## 单调性的判断方法与等价表示

<p>若只设 $x_1\neq x_2$, 则
  \[\begin{aligned}
    &\frac{f(x_1)-f(x_2)}{x_1-x_2}>0\Leftrightarrow
     (f(x_1)-f(x_2))(x_1-x_2)>0\Leftrightarrow
     f(x)单调递增;\\
    &\frac{f(x_1)-f(x_2)}{x_1-x_2}< 0\Leftrightarrow
     (f(x_1)-f(x_2))(x_1-x_2)< 0\Leftrightarrow
     f(x)单调递减.
  \end{aligned}\]
</p>

## 常见函数的单调性

## 分段函数的单调性


<myexercise>
    <p>函数 $f(x)= x^2-2x$ 的单调递增区间为\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    对称轴 $x=1$, 单调递增区间为 $[1,+\infty)$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>若 $f(x)$ 是定义在 $[-1,1]$ 上的单调递增函数, 
    且 $f(x-1)< f(1-3x)$, 求 $x$ 的取值范围.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    由题 $-1\leqslant x-1< 1-3x\leqslant 1$, 解得 $x\in\Big[0,\frac12\Big)$.
</p>
<p>\varexercise 若 $f(x)=x^3+x$, 解不等式 $f(x-1)< f(1-3x)$.
</p>
<p>因为 $f(x)$ 在 $\mathbf{R}$ 上单调递增, 所以 $x-1< 1-3x$ 即 $x\in\Bigl(-\infty,\frac12\Bigr)$.
</p>
<p>\varexercise 若 $f(x)=x-\sin x$, 解不等式 $f(x-1)< \pi$.
</p>
<p>因为 $f'(x)=1-\cos x\geqslant 0$, 所以 $f(x)$ 在 $\mathbf{R}$ 上单调递增, 而 $f(\pi)=\pi$, 故不等式化为 $f(x-1)< f(\pi)$, 即 $x-1< \pi$, 解得 $x\in(-\infty,\pi+1)$.
  </p>
</mysolution>


<myexample>
<p>判断下列函数在区间 $(0,2)$ 上的单调性:
</p>
<p>(1) $y=-x+1$;\qquad (2) $y=\sqrt{x}$;\qquad  (3) $y=x^2-2x+5$;
</p>
<p>(4) $y=\frac2x$;\qquad (5) $f(x)=-2|x+4|$.
  </p>
</myexample>
</p>
<p><mysolution>
    <p>    (1) 单调递减; (2) 单调递增; (3) $(0,1]单调递增$, $(1,2)单调递减$; (4) 单调递减; (5) 单调递减.
    \mymarginpar{含一个绝对值的函数作图时, 既可以先化为分段函数,也可以利用图象变换.}
  </p>
</mysolution>
</p>

<p>\subsubsection{函数单调性的应用}
  <myexample>
<p>已知函数 $f(x)=\begin{cases}
      (a-3)x+5, & x\leqslant 1,\\
      \frac{2a}x, & x>1 \end{cases}$ 
    是 $\mathbf{R}$ 上的单调递减函数, 求 $a$ 的取值范围.
  </p>
</myexample>
</p>
<p><mysolution>
    <p>    $f(x)$ 分段递减且在 $x=1$ 附近单调递减, 则 $a-3< 0$, $a>0$ 且 $(a-3)+5\leqslant 2a$, 解得 $a\in[2,3)$.
</p>
<p>\varexercise 已知函数 $f(x)=\begin{cases}
      (a^2-3)x+5, & x\leqslant 1,\\
      \frac{3a}x, & x>1 \end{cases}$ 
    是 $\mathbf{R}$ 上的单调递减函数, 求 $a$ 的取值范围.
</p>
<p>此时 $a^2-3< 0$, $a>0$ 且 $(a^2-3)+5\leqslant 3a$, 解得 $a\in[1,\sqrt3)$.
</p>
<p>\varexercise 若上题中 $f(x)$ 是 $\mathbf{R}$ 上的单调递增函数, 求 $a$ 的取值范围.
</p>
<p>类似可得 $a^2-3>0$, $a< 0$ 且 $(a^2-3)+5\geqslant 3a$, 解得 $a\in(-\infty,-\sqrt3)$.
  </p>
</mysolution>
</p>
<p>\lianxi
  \begin{exercise}[s]
    如果二次函数 $f(x)=x^2 -(a-1)x+5$ 在区间 $\Big(\frac12,1\Big)$ 上单调递增,
    求 $f(2)$ 的取值范围.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    轴 $x=\frac{a-1}2$, 则 $\frac{a-1}2\leqslant \frac12$ 即 $a\leqslant 2$, 所以 $f(2)= 11-2a\in[7,+\infty)$.
  </p>
</mysolution>


<myexercise>
    <p>若函数 $f(x)=-x^2+2ax$ 与 $g(x)=\frac{a}{x+1}$ 都是 $[1,2]$ 上的单调递减函数, 则实数 $a$ 的取值范围是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(x)$ 轴为 $x=a$, 开口向下, 则 $a\leqslant 1$. 由 $g(x)$ 图象知 $a>0$, 所以 $a\in(0,1]$.
  </p>
</mysolution>

<myexercise>
    <p>函数 $f(x)=|x^2-1|$ 的单调递减区间是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    作图知, 单调递减区间是 $(-\infty,-1]$ 和 $[0,1]$.
    \mymarginpar{不能答“单调递减区间是 $(-\infty,-1]\cup [0,1]$”.}
  </p>
</mysolution>

<myexercise>
    <p>已知函数 $f(x)=ax^2 +4(1-a)x+1$ 在 $[1,+\infty )$ 上是单调递增函数,
    那么实数 $a$ 的取值范围是\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    若 $a=0$, 则 $f(x)=4x+1$ 为单调递增函数. 若 $a\neq 0$, 则 $a>0$ 且 $-\frac{4(1-a)}{2a}\geqslant 1$, 解得 $a\geqslant 2$. 综上可知, $a\in \{0\}\cup [2,+\infty)$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>已知定义在 $\mathbf{R}$ 上的函数 $f(x)$ 对任意 $m\neq n$, 
    总有 $\frac{f(m)-f(n)}{m-n}>0$. 
    若 $f(-3)=a$, $f(-1)=b$, 求 $f(x)$ 在 $[-3,-1]$ 上的最大值
    (用 $a$, $b$ 表示).
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    题意表明 $f(x)单调递增$, 所以 $f_{\max}= f(-1)=b$.
  </p>
</mysolution>
</p>
<p><myexercise>
    <p>下列函数满足“$\forall\,x_1$, $x_2\in (0,+\infty)$, 
    $(x_1- x_2)\big(f(x_1)-f(x_2)\big)< 0$”的有\,?(填序号)
</p>
<p>(1) $f(x)= \frac1x$; (2) $g(x)=(x-1)^2$; (3) $h(x)= \ln(x+1)$.
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    题意表明 $f(x)$ 在 $(0,+\infty) 单调递减$, 故只有 $f(x)$ 符合题意.
  </p>
</mysolution>

<myexercise>
    <p>一次函数 $f(x)=ax+b$ 在 $[-1,1]$ 上恒正的充要条件是什么\,?
  </p>
</myexercise>
</p>
<p><mysolution>
    <p>    $f(-1)>0$ 且 $f(1)>0$, 即 $-a+b>0$ 且 $a+b>0$.
  </p>
</mysolution>






<p>\begin{example}\label{exa:201115-1130}
    若函数 $f(x)= \begin{cases}
        x-1, & x\leqslant 1,\\
        x^2+a, & x>1
    \end{cases}$ 在 $\realnum$ 上单调递增, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由题意,
    \[1-1\leqslant 1^2+a\ \text{即}\ a\geqslant -1,\]
    所以 $a\in[-1,+\infty)$.
</p>
</mysolution>

<myexercise>
    <p>设函数 $f(x)=\begin{cases}
      x^2+1, & x\geqslant 0,\\
      1, & x< 0,\end{cases}$
    解不等式: $f(3-x^2)>f(2x)$.
</p>
</myexercise>
<mysolution>
    <p>    $f(x)$ 单调递增, 则原不等式等价于
    \[3-x^2> 2x,\quad x\in (-3,1).\]
</p>
</mysolution>

</p>
<p>解分段函数单调性问题时, 只需每段函数均单调, 且分段点处的函数值满足题中单调性. 具体来说,
\[\begin{aligned}
    &f(x)= \begin{cases}
            g(x), & x\leqslant a,\\
            h(x), & x>a
        \end{cases}\ \text{在 $\realnum$ 上单调递增}\\
    \Leftrightarrow{}& \left\{\!\!\begin{array}{l}
        \text{$g(x)$ 在 $(-\infty,a]$ 上, $h(x)$ 在 $(a,+\infty)$ 上均单调递增},\\
        g(a)\leqslant h(a)
        \end{array}\right.\\
    &f(x)= \begin{cases}
            g(x), & x\leqslant a,\\
            h(x), & x>a
        \end{cases}\ \text{在 $\realnum$ 上单调递减}\\
    \Leftrightarrow{}& \left\{\!\!\begin{array}{l}
        \text{$g(x)$ 在 $(-\infty,a]$ 上, $h(x)$ 在 $(a,+\infty)$ 上均单调递减},\\
        g(a)\geqslant h(a)
        \end{array}\right.\\
\end{aligned}\]
建议结合如下函数草图记忆上述结论:
<center>
    \includegraphics[scale=1]{2020-1115-1130-1-crop}\qquad
    \includegraphics[scale=1]{2020-1115-1130-2-crop}
</center>
</p>
<p>如果例 \ref{exa:201115-1130} 改为“函数 $f(x)= \begin{cases}
    x-1, & x\leqslant 1,\\
    x^2+2ax, & x>1
\end{cases}$ 在 $\realnum$ 上单调递增”, 则应限制
\[\begin{cases}
    -a\leqslant 1 & (\text{二次函数对称轴在定义域左侧}),\\
    1-1\leqslant 1^2+ 2a\cdot1 & (\text{分段点处的函数值递增}).
    \end{cases}\]
</p>
<p></p>

<myexample>
<p>若对于任意实数 $a\in[-1,1]$, 函数 $y=x^2+(a-4)x+4-2a$ 的值恒大于零, 求 $x$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>此题可理解为 (反客为主): 关于 $a$ 的函数 
    \[y=f(a)=x^2+(a-4)x+4-2a\]
    在 $[-1,1]$ 上恒大于零. 此时
    \[f(a)= (x-2)a+ x^2-4x+4\]
    为关于 $a$ 的一次函数, 在 $[-1,1]$ 上的图形为一条线段, 所以只需两个端点纵坐标均大于零, 即
    \[\left\{\!\!\begin{array}{l}
        f(-1)= (x-2)\cdot(-1)+ x^2-4x+4>0,\\
        f(1)= (x-2)\cdot 1+ x^2-4x+4>0,
    \end{array}\right.\]
    解得
    \[\left\{\!\!\begin{array}{l}
        x< 1\ \text{或}\ x>2,\\
        x< 2\ \text{或}\ x>3,
    \end{array}\right.\]
    所以 $x\in(-\infty,1)\cup (3,+\infty)$.
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
