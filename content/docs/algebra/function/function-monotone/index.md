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

<p>对函数也可以在其定义域的一部分上定义单调性. 设函数 $f(x)$ 的定义域为 $D$, $A\subseteq D$, 任取 $x_1$, $x_2\in A$ 满足 $x_1< x_2$, 则 \[\begin{aligned}
    &f(x_1)< f(x_2)\Leftrightarrow f(x)\ \text{在 $A$ 上单调递增},\\
    &f(x_1)> f(x_2)\Leftrightarrow f(x)\ \text{在 $A$ 上单调递减}.
\end{aligned}\]
将上面的 $A$ 取成 $D$ 时, 就得到函数 $f(x)$ 在其定义域 $D$ 上单调递增或单调递减的定义.
</p>
<p>由定义, 函数单调递增可以从代数式的角度理解为: 单调递增表示自变量的大小与对应函数值的大小一致, 单调递减表示自变量的大小与对应函数值的大小恰好相反.
</p>
<p>由函数图象可知, 初中常见函数的单调性的决定因素如下: 
</p>
<p>(1) 一次函数 $f(x)=kx+b$ ($k\neq 0$): $k< 0$ 时单调递减, $k> 0$ 时单调递增;
</p>
<p>(2) 反比例函数 $f(x)=\dfrac{k}x$ ($k\neq 0$): $k>0$ 时分段单调递减, $k< 0$ 时分段单调递增;
</p>
<p>(3) 二次函数 $f(x)=ax^2+bx+c$ ($a\neq 0$): $a$ 决定图象开口方向, $-\frac{b}{2a}$ 决定对称轴位置.
</p>

二次函数的单调性由其图象的开口方向和对称轴共同决定. 例如, 对函数 $f(x)= x^2-2x$, 其图象开口向上且对称轴为 $x=1$, 所以 $f(x)$ 在区间 $(-\infty,1]$ 上单调递减, 在区间 $[1,+\infty)$ 上单调递增.

<myremark>
    <p>(1) 反比例函数 $f(x)= \dfrac1x$ 在区间 $(-\infty,0)$ 和 $(0,+\infty)$ 上均单调递减, 而在其定义域 $(-\infty,0)\cup (0,+\infty)$ 上并非单调递减, 例如, $-1< 1$ 但是 $f(-1)< f(1)$ (若 $f(x)$ 单调递减, 则应有 $f(-1)> f(1)$). 所以讨论反比例函数的单调性时, 仅能用“分段单调”来描述.
    </p>
    <p>(2) 对高中常见的函数, 都可以将其定义域分成多个区间, 使该函数在各个区间上仅单调递增或仅单调递减. 但是有些函数无法像这样划分其定义域, 即它们的图象在其定义域的任意子区间上都是“振荡的”.
    </p>
</myremark>

<myexample>
    <p>(1) 设二次函数 $f(x)= x^2-(a-1)x+5$ 在区间 $\Big(\frac12,1\Big)$ 上单调递增, 求 $f(2)$ 的取值范围.
    </p>
    <p>(2) 若函数 $f(x)=-x^2+2ax$ 与 $g(x)=\frac{a}x$ 都在区间 $[1,2]$ 上单调递减, 求实数 $a$ 的取值范围.
    </p>
</myexercise>

<mysolution>
    <p>(1) 二次函数 $f(x)$ 图象开口向上, 且对称轴为 $x=\dfrac{a-1}2$, 则 \[
        \frac{a-1}2\leqslant \frac12\Rightarrow a\leqslant 2,\]
    所以 $f(2)= 11-2a\in[7,+\infty)$.
    </p>
    <p>(2) 二次函数 $f(x)$ 对称轴为 $x=a$, 开口向下, 则 $a\leqslant 1$. 由 $g(x)$ 图象知 $a>0$, 所以 $a\in(0,1]$.
    </p>
</mysolution>

<myremark>
    <p>由 $a\leqslant 2$ 得到 $11-2a$ 的取值范围, 可以利用不等式的性质变形, 即 \[
        -2a\geqslant -4,\quad 11-2a\geqslant 7,\]
    也可以直接利用 $h(a)= 11-2a$ 单调递减, 即 \[
        h(a)\in [h(2),+\infty)= [7,+\infty).\]
    </p>
</myremark>

<myexample>
    <p>(1) 已知函数 $f(x)=ax^2 +4(1-a)x+1$ 在区间 $[1,+\infty)$ 上单调递增, 求实数 $a$ 的取值范围.
    </p>
</myexample>

<mysolution>
    <p>(1) 若 $a=0$, 则 $f(x)=4x+1$ 为单调递增函数. 若 $a\neq 0$, 则 \[\left\{\!\!\begin{array}{l}
        a>0,\\[6pt]
        -\dfrac{4(1-a)}{2a}\geqslant 1
    \end{array}\right.\Rightarrow
        a\in [2,+\infty).\]
    综上所述, $a\in \{0\}\cup [2,+\infty)$.
    </p>
</mysolution>


## 单调性的判断方法

若函数图象容易作出, 则通常利用图象来判断函数的单调性.

<myexample>
    <p>判断下列函数的单调性:
    </p>
    <p>$f_1(x)= |x+2|$;&emsp; $f_2(x)= |x^2-1|$;&emsp;
       $f_3(x)= 1+\dfrac1{x+2}$.
    </p>
</myexample>

<mysolution>
    <p>利用<a href="/docs/prerequisite/ms-function/graph-tranform">图象变换</a>, 可以分别作出 $f_1(x)$, $f_2(x)$, $f_3(x)$ 的图象, 并得到:
    </p>
    <p> $f_1(x)$ 在区间 $(-\infty,-2]$ 上单调递减, 在 $[-2,+\infty)$ 上单调递增;
    </p>
    <img alt="f_1(x)= |x+4| 的图象" src="/figs/2022/2022-09/2022-0914-2200.svg"></img>
    <p> $f_2(x)$ 在区间 $(-\infty,-1]$ 和 $[0,1]$ 上均单调递减, 在 $[-1,0]$ 和 $[-4,+\infty)$ 上均单调递增;
    </p>
    <img alt="f_2(x)= |x^2-1| 的图象" src="/figs/2022/2022-09/2022-0914-2210.svg"></img>
    <p> $f_3(x)$ 在区间 $(-\infty,-2)$ 和 $(-2,+\infty)$ 上均单调递减.
    </p>
    <img alt="f_3(x)= 1+\dfrac1{x+2}" src="/figs/2022/2022-09/2022-0914-2220.svg"></img>
</mysolution>


不少函数的图象是由其单调性决定的, 即只有事先判断函数在其定义域各部分的单调性, 才能较准确地作出函数图象, 所以由图象判断单调性并非总是可行. 判断单调性的一般方法仍旧是根据定义来计算: 设函数 $f(x)$ 定义在 $D$ 上, 任取 $x_1$, $x_2\in D$ 满足 $x_1< x_2$, 若 $f(x_1)< f(x_2)$ 恒成立, 则说明 $f(x)$ 单调递增; 若 $f(x_1)> f(x_2)$ 恒成立, 则说明 $f(x)$ 单调递减. 在判断函数值的大小关系时, 一般用<a href="/docs/prerequisite/inequality/inequality-property/#比大小">作差法</a>.

<p>例如, 由定义判断函数 $f(x)= -x+1$ 的单调性, 可以任取实数 $x_1< x_2$, 则 \[
    f(x_1)- f(x_2)= (-x_1+1)- (-x_2+1)= x_2-x_1.\]
由 $x_1< x_2$ 知 $x_2-x_1> 0$, 所以 $f(x_1)< f(x_2)$, 即 $f(x)$ 单调递减. 这个结论与由图象得到的单调性相同. 从计算过程可以看出, 当函数解析式较简单时, 可以由定义判断单调性.
</p>
<p>由单调性的定义和<a href="/docs/prerequisite/inequality/inequality-property/#不等式的性质">不等式的性质</a>, 可以进一步得到结论: 设函数 $f(x)$, $g(x)$ 均定义在数集 $D$ 上, 实数 $k$ 为常数, 则
</p>
<p>(1) $f(x)$ 与 $f(x)+k$ 的单调性相同;
</p>
<p>(2) 若 $f(x)$ 单调递增 (减), 则当 $k>0$ 时, $kf(x)$ 也单调递增 (减); 当 $k< 0$ 时, $kf(x)$ 单调递减 (增);
</p>
<p>(3) 若 $f(x)$, $g(x)$ 均单调递增 (减), 则 $f(x)+g(x)$ 也单调递增 (减).
</p>
<p>下面用定义证明 (3): 设 $f(x)$, $g(x)$ 均单调递增, 任取 $x_1$, $x_2\in D$ 且 $x_1< x_2$, 则 $f(x_1)< f(x_2)$, $g(x_1)< g(x_2)$, 所以 \[
    f(x_1)+ g(x_1)< f(x_2)+ g(x_2),\]
即 $f(x)+g(x)$ 也单调递增. 同理可证其他情形.
</p>

<myremark>
    <p>上述结论也可以从图象的角度来直观理解, 例如, $f(x)+k$ 的图象可由 $f(x)$ 的图象上下平移得到, 故两者单调性相同. 同理, $kf(x)$ 的图象是由 $f(x)$ 的图象相对于 $x$ 轴拉伸或压缩得到的, $f(x)+g(x)$ 的图象可看成由 $f(x)$ 与 $g(x)$ 的图象“叠加”而成.
    </p>
</myremark>



## 单调性的等价表示

<p>前面提到, 对函数 $f(x)$ 而言, 单调递增表示 $x$ 越大, $f(x)$ 也越大 (或 $x$ 越小, $f(x)$ 也越小); 单调递减表示 $x$ 越大, $f(x)$ 反而越小 (或 $x$ 越小, $f(x)$ 反而越大). 若只设 $x_1\neq x_2$, 则利用实数乘除运算的符号法则, 单调性有如下等价表示: \[\begin{aligned}
    f(x)\ \text{单调递增}\ 
        &\Leftrightarrow \frac{f(x_1)-f(x_2)}{x_1-x_2}>0
        \Leftrightarrow [f(x_1)-f(x_2)](x_1-x_2)>0,\\
    f(x)\ \text{单调递减}\ 
        &\Leftrightarrow \frac{f(x_1)-f(x_2)}{x_1-x_2}< 0
        \Leftrightarrow [f(x_1)-f(x_2)](x_1-x_2)< 0.
\end{aligned}\]
上面两个式子从左往右推导是比较容易的, 下面举例说明如何从右往左推导. 例如, 若 $\dfrac{f(x_1)-f(x_2)}{x_1-x_2}>0$, 且取 $x_1< x_2$, 则 \[
    x_1- x_2< 0,\quad f(x_1)- f(x_2)< 0,\]
所以 $f(x_1)< f(x_2)$, 表明 $f(x)$ 单调递增. 
</p>

<myexercise>
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



## 分段函数的单调性

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

<myexample>
    <p>(1) 已知函数 \[f(x)=\begin{cases}
        (a-3)x+5, & x\leqslant 1,\\[6pt]
        \frac{2a}x, & x>1 \end{cases}\]
    是 $\mathbf{R}$ 上的单调递减函数, 求 $a$ 的取值范围.
    </p>
    <p>(2) 已知函数 $f(x)=\begin{cases}
      (a^2-3)x+5, & x\leqslant 1,\\[6pt]
      \frac{3a}x, & x>1 \end{cases}$ 
    是 $\mathbf{R}$ 上的单调递增函数, 求 $a$ 的取值范围.
</p>
</myexample>

<mysolution>
    <p>(1) 由题意, $f(x)$ 分段递减且在 $x=1$ 附近单调递减, 则 \[\left\{\!\!\begin{array}{l}
        a-3< 0,\ 2a>0,\\
        (a-3)+5\geqslant 2a
    \end{array}\right.\Rightarrow
        a\in (0,2].\]
    </p>
    <p>(2) 此时, $f(x)$ 分段递增且在 $x=1$ 附近单调递增, 则 \[\left\{\!\!\begin{array}{l}
        a^2-3> 0,\ 3a< 0,\\
        (a^2-3)+5\leqslant 3a
    \end{array}\right.\Rightarrow
        a\in \varnothing.\] 
    </p>
</mysolution>

<myexercise>
    <p>(1) 已知函数 $f(x)=\begin{cases}
        (a^2-3)x+5, & x\leqslant 1,\\[6pt]
        \frac{3a}x, & x>1 \end{cases}$ 
    是 $\mathbf{R}$ 上的单调递减函数, 求 $a$ 的取值范围.
    </p>
    <p>(2) 
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) 由题意, $f(x)$ 分段递减且在 $x=1$ 附近单调递减, 则 \[\left\{\!\!\begin{array}{l}
        a^2-3< 0,\ 3a>0,\\
        (a^2-3)+5\geqslant 3a
    \end{array}\right.\Rightarrow
        a\in (0,1].\]
    </p>
</details>

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


## 单调性的简单应用

利用单调性可以解简单的抽象函数构成的不等式或方程.

<myexercise>
    <p>若定义在 $[-1,1]$ 上的函数 $f(x)$ 是单调递增, 且 $f(x-1)< f(1-3x)$, 求 $x$ 的取值范围.
    </p>
</myexercise>

<mysolution>
    <p>由题 $-1\leqslant x-1< 1-3x\leqslant 1$, 解得 $x\in\Big[0,\frac12\Big)$.
</p>
<p>\varexercise 若 $f(x)=x^3+x$, 解不等式 $f(x-1)< f(1-3x)$.
</p>
<p>因为 $f(x)$ 在 $\mathbf{R}$ 上单调递增, 所以 $x-1< 1-3x$ 即 $x\in\Bigl(-\infty,\frac12\Bigr)$.
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

<myexercise>
    <p>求“一次函数 $f(x)= ax+b$ ($a\neq 0$) 在 $[-1,1]$ 上恒正”的充要条件。
    </p>
</myexercise>

<mysolution>
    <p>    $f(-1)>0$ 且 $f(1)>0$, 即 $-a+b>0$ 且 $a+b>0$.
  </p>
</mysolution>

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
