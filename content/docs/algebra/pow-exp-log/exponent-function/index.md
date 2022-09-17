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

<p>乘方是多个相同式子相乘的简写, 例如, \[
    a^2= a\cdot a,\quad b^3= b\cdot b\cdot b.\]
对于正整数 $m,n$, 可知 \[\begin{gathered}
    a^m \cdot a^n= a^{m+n},\\
    (a^m)^n= a^{mn},\quad
    (ab)^m= a^m b^m.
\end{gathered}\]
例如, \[
    (4^2)^3= 4^2\cdot 4^2\cdot 4^2= 4^{2\cdot 3}.\]
</p>
<p>当 $a\neq 0$ 且正整数 $m,n$ 满足 $m\geqslant n$ 时, \[
    \frac{a^m}{a^n}= a^{m-n},\quad
    \frac{a^n}{a^m}= \frac1{a^{m-n}},\]
例如, \[
    \frac{2^5}{2^3}= a^{5-3},\quad
    \frac{2^3}{2^5}= \frac1{2^{5-3}}.\]
特别地, 当 $m=n$ 时, 可得 \[
    a^0= a^{n-n}= \frac{a^n}{a^n}= 1\quad (a\neq 0).\]
</p>
<p>在公式 $a^m \cdot a^n= a^{m+n}$ 中令 $m= -n$, 则 \[
    a^{-n} \cdot a^n= a^{-n+n}= a^0= 1,\]
所以规定 $a^{-n}= \dfrac1{a^n}$. 在公式 $(a^m)^n= a^{mn}$ 中令 $m= \dfrac1n$, 则 \[
    (a^{\frac1n})^n= a^{\frac1n\cdot n}= a,\]
即 $a^{\frac1n}$ 的 $n$ 次方为 $a$, 所以规定 $a^{\frac1n}= \sqrt[n]{a}$.
</p>
<p>上述公式汇总如下: \[\begin{gathered}
    a^m \cdot a^n= a^{m+n},\quad a^0= 1,\\
    (a^m)^n= a^{mn},\quad
    (ab)^m= a^m b^m,\\
    a^{-n}= \dfrac1{a^n},\quad
    a^{\frac1n}= \sqrt[n]{a}.
\end{gathered}\]
虽然在前面均假设 $m,n$ 为正整数, 但是上面的 $6$ 个公式可以推广到 $m,n$ 为任意实数的情形 (记忆时仍不妨只考虑正整数的情形). 最后两个式子可记为“指数中的负号表示取倒数, 分母表示开根号”, 此外“指数中的分子表示乘方”, 例如, \[
    a^{-\frac34}= \frac1{a^{\frac34}}= \frac1{\sqrt[4]{a^3}}.\]
</p>


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

<p>幂函数、指数函数和对数函数相关的“图形过定点”问题, 一般是考虑利用恒等式
\[a^0=1\ (a\neq0),\quad \log_a 1=0\ (a>0,\ a\neq1)\]
将函数中含参数的部分化为常数.
</p>
<p><myexample>
<p>(1) 若 $a>0$ 且 $a\neq 1$, 求函数 $y=a^x+1$ 的图形所过的定点.
</p>
<p>(2) 若 $a>0$ 且 $a\neq 1$, 求函数 $y=\log_a x-1$ 的图形所过的定点.
</p>
</myexample>
<mysolution>
    <p>(1) 令 $x=0$ 知, 无论 $a$ 为何值, 总有 $y=2$, 即函数 $y=a^x+1$ 的图形过定点 $(0,2)$.
</p>
<p>(2) 令 $x=1$ 知, 无论 $a$ 为何值, 总有 $y=-1$, 即函数 $y=\log_a x-1$ 的图形过定点 $(1,-1)$.
</p>
</mysolution>
</p>
<p>用类似的方法可以求得
</p>
<p>$y=a^x-1$ 的图形过定点 $(0,0)$;
</p>
<p>$y=2a^x+1$ 的图形过定点 $(0,3)$; 
</p>
<p>$y=3a^{x-1}+3$ 的图形过定点 $(1,6)$; 
</p>
<p>$y=\log_a (2x+1)+4$ 的图形过定点 $(0,4)$; 等等.
</p>

<myexample>
<p>已知 $x+2y=1$, 求 $2^x+4^y$ 的最小值.
</p>
</myexample>
<mysolution>
    <p>因为 $x+2y=1$, 而由均值不等式,
    \[2^x+4^y\geqslant 2\sqrt{2^x\cdot 4^y}
        = 2\sqrt{2^{x+2y}}= 2\sqrt2,\]
   “$=$”成立当且仅当 $2^x=4^y$ 即 $x=2y=\dfrac12$, 所以 $2^x+4^y$ 的最小值为 $2\sqrt2$.
</p>
</mysolution>

<myexample>
<p>设函数 $f(x)=\begin{cases}
        \biggl(\dfrac12\biggr)^x-1, & x< 0,\\
        x^{\frac12}, & x\geqslant 0,
    \end{cases}$ 求不等式 $f(x)\geqslant 1$ 的解.
</p>
</myexample>
<mysolution>
    <p>(1) 若 $x< 0$, 则不等式化为 
    \[\biggl(\frac12\biggr)^x-1\geqslant 1,\quad \text{即}\quad
        \biggl(\frac12\biggr)^x\geqslant 2= \biggl(\frac12\biggr)^{-1}.\]
    由函数 $y=\biggl(\dfrac12\biggr)^x$ 单调递减可知, $x\in(-\infty,-1]$.
</p>
<p>(2) 若 $x\geqslant 0$, 则不等式化为 $x^{\frac12}\geqslant 1$. 由函数 $y=x^{\frac12}$ 在 $[0,+\infty)$ 上单调递增可知, $x\in[1,+\infty)$.
</p>
<p>综上所述, $x\in(-\infty,-1]\cup [1,+\infty)$.
</p>
</mysolution>

<p>解简单的指数、对数方程或不等式, 一般是利用指数、对数的单调性 (参考“2020 年 11 月 21 日答疑记录”). 具体来说, 有两种方法.
</p>
<p>方法一: 化为同底的指数或对数 (简记为“化同底”). 例如, 指数方程 $2^x=4$ 可化为 $2^x=2^2$, 由 $y=2^x$ 单调递增可知, $x=2$. 类似地, $\log_2 x= 2$ 可化为 $\log_2 x= \log_2 4$, 由 $y=\log_2 x$ 单调递增可知, $x=4$. 再如, $2^x>4$ 可化为 $2^x>2^2$, 则 $x>2$; $\log_{0.5} x> 2$ 可化为 $\log_{0.5} x> \log_{0.5} 0.5^2$, 由 $y=\log_{0.5} x$ 单调递减可知, $0< x< 0.25$. 注意, 对数函数有自然定义域, 即真数 (此处的 $x$) 大于零.
</p>
<p>方法二: 直接取对数或构造指数式. 此方法涉及指数和对数的运算法则 (参考“2020 年 11 月 8 日答疑记录”). 例如, 对方程 $2^x=4$ 两边取以 $2$ 为底的对数, 可得 $\log_2 2^x= \log_2 4$, 即 $x=2$. 类似地, 将 $\log_2 x< 2$ 化为 $2^{\log_2 x}< 2^2$, 可知 $0< x< 4$ (注意对数函数的自然定义域). 再如, 由 $2^x>3$ 可得 $x>\log_2 3$ (这个例子用前一个方法来解并不方便). 在这些例子中, 新构造的对数式或指数式的底均应与原式中的相同.
</p>
<p><myexample>
<p>解下列不等式: 
</p>
<p>(1) $\biggl(\dfrac12\biggr)^x>4$;\qquad
    (2) $\log_3 x> 2$;\qquad
    (3) $3^{x^2+x}>9$;\qquad
    (4) $\log_5 (x^2-4x)\leqslant 1$.
</p>
</myexample>
<mysolution>
    <p>(1) 方法一: 不等式化为 $\biggl(\dfrac12\biggr)^x> \biggl(\dfrac12\biggr)^{-2}$, 所以 $x\in(-\infty,-2)$.
</p>
<p>方法二: 不等式化为 $\log_{\frac12}\biggl(\dfrac12\biggr)^x< \log_{\frac12} 4= \log_{\frac12} \biggl(\dfrac12\biggr)^{-2}$, 所以 $x\in(-\infty,-2)$.
</p>
<p>(2) 方法一: 不等式化为 $\log_3 x> \log_3 9$, 所以 $x\in(9,+\infty)$.
</p>
<p>方法二: 不等式化为 $3^{\log_3 x}> 3^2$, 所以 $x\in(9,+\infty)$.
</p>
<p>(3) 方法一: 不等式化为 
    \[3^{x^2+x}>3^2,\quad\text{即}\quad x^2+x>2,\]
    解得 $x\in(-\infty,-2)\cup (1,+\infty)$.
</p>
<p>方法二: 不等式化为 $\log_3 3^{x^2+x}>\log_3 9$, 仍可解得 $x\in(-\infty,-2)\cup (1,+\infty)$.
</p>
<p>(4) 方法一: 不等式化为 
    \[\log_5 (x^2-4x)\leqslant \log_5 5,\quad\text{即}\quad 0< x^2-4x\leqslant 5,\]
    解得 $x\in[-1,0)\cup (4,5]$.
</p>
<p>方法二: 不等式化为 $5^{\log_5 (x^2-4x)}\leqslant 5^1$, 仍可解得 $x\in[-1,0)\cup (4,5]$.
</p>
</mysolution>

<myexample>
<p>设 $a=\biggl(\dfrac35\biggr)^{\frac25}$, $b=\biggl(\dfrac25\biggr)^{\frac35}$, $c=\biggl(\dfrac25\biggr)^{\frac25}$, 比较这三者的大小.
</p>
</myexample>
<mysolution>
    <p>方法一: 因为 $a$, $c$ 指数相同, 所以考虑幂函数 $f(x)=x^{\frac25}$. 由 $f(x)$ 单调递增可知, $f\biggl(\dfrac35\biggr)> f\biggl(\dfrac25\biggr)$, 即 $a>c$.
</p>
<p>因为 $b$, $c$ 底数相同, 所以考虑指数函数 $g(x)=\biggl(\dfrac25\biggr)^x$. 由 $g(x)$ 单调递减可知, $g\biggl(\dfrac35\biggr)< g\biggl(\dfrac25\biggr)$, 即 $b< c$.
</p>
<p>综上所述, $b< c< a$.
</p>
<p>方法二: 也可以先考虑 $a^5=\biggl(\dfrac35\biggr)^2$, $b^5=\biggl(\dfrac25\biggr)^3$, $c^5=\biggl(\dfrac25\biggr)^2$, 这三者的大小. 因为
    \[\biggl(\dfrac35\biggr)^2= \frac{45}{125},\quad
      \biggl(\dfrac25\biggr)^3= \frac{8}{125},\quad
      \biggl(\dfrac25\biggr)^2= \frac{20}{125},\]
    所以 $b^5< c^5< a^5$. 由 $h(x)= x^5$ 单调递增可知, $b< c< a$.
</p>
</mysolution>

<myexample>
<p>若实数 $a$, $b$ 满足 $a+b=2$, 求 $3^a+3^b$ 的最小值.
</p>
</myexample>
<mysolution>
    <p>由均值不等式, 
    \[3^a+3^b\geqslant 2\sqrt{3^a\cdot 3^b}
        = 2\sqrt{3^{a+b}}= 2\sqrt{3^2}= 6,\]
   “$=$”成立当且仅当 $3^a=3^b$ 即 $a=b=1$, 所以 $3^a+3^b$ 的最小值为 $6$. 
</p>
</mysolution>
<myremark>
    <p>二元函数求值域, 要么想办法先化为一元函数, 要么直接用均值不等式. 通常优先考虑后者, 但是要注意等号成立的条件. 此外, 上题也可利用 $b=2-a$ 将 $3^a+3^b$ 化为关于 $a$ 的一元函数 $3^a+3^{2-a}$, 但仍需利用均值不等式才能求其最小值. 
</p>
</myremark>

<myexample>
<p>函数 $f(x)= a^{x+1}+ 3$ ($a>0$, 且 $a\neq1$) 过定点  $\underline{\qquad}$.
</p>
</myexample>
<mysolution>
    <p>利用 $a^0=1$ 对任意 $a\neq0$ 成立可知, 
    \[f(-1)= a^0+3= 3,\]
    即 $f(x)$ 过定点 $(-1,3)$.
</p>
</mysolution>

<myexample>
<p>已知函数 
    \[f(x)= \begin{cases}
        -x+3-3a, & x< 0,\\
        a^x, & x\geqslant 0
    \end{cases}\quad (a>0\ \text{且}\ a\neq 1)\]
    在 $\mathbf{R}$ 上单调递减, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由分段函数的单调性判断方法 (参考“2020 年 10 月 31 日答疑记录”第三个例题及其后的说明),
    \[\left\{\!\!\begin{array}{l}
        0< a< 1,\\
        -0+3-3a\geqslant a^0,
    \end{array}\right.\ \text{解得}\quad
    0< a< \frac23.\]
    故所求取值范围为 $\biggl(0,\dfrac23\biggr)$.
</p>
</mysolution>

<myexample>
<p>若指数函数 $y=f(x)$ 的图形经过点 $(2,4)$, 求不等式 $f(2x-1)\leqslant \biggl(\dfrac12\biggr)^{1-3x}$ 的解集.
</p>
</myexample>
<mysolution>
    <p>由题意, $f(2)=4$. 设 $f(x)=a^x$ ($a>0$ 且 $a\neq 1$), 则 $a^2=4$, 解得 $a=2$. 因此不等式化为 (指数式化同底)
    \[2^{2x-1}\leqslant 2^{-(1-3x)},\quad\text{即}\quad
        2x-1\leqslant -(1-3x),\]
    解得 $x\in[0,+\infty)$.
</p>
</mysolution>

<myexample>
<p>若函数 $y= 2^{|x-1|}$ 在区间 $(k-1,k+1)$ 内不单调, 求 $k$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由 $y=2^|x|$ 的图形向右平移一个单位长度可得 $y= 2^{|x-1|}$ 的图形, 而前者为偶函数, 且当 $x\geqslant 0$ 时 $y=2^x$. 由此可以画出 $y= 2^{|x-1|}$ 的图形如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1223-2000-crop}
    </center>
</p>
<p>由图可知, $y= 2^{|x-1|}$ 在 $(-\infty,1)$ 上单调递减, 在 $(1,+\infty)$ 上单调递增. 因为题中要求函数 $y= 2^{|x-1|}$ 在区间 $(k-1,k+1)$ 内不单调, 所以
    \[1\in(k-1,k+1),\quad\text{解得}\quad k\in(0,2).\]
</p>
</mysolution>

<myexample>
<p>画出函数 $y= \dfrac{x a^x}{|x|}$ ($0< a< 1$) 的图形的大致形状.
</p>
</myexample>
<mysolution>
    <p>利用绝对值的定义, 原函数化为 $y= \begin{cases}
        -a^x, & x< 0,\\
        a^x, & x>0,
    \end{cases}$
    图形的大致形状如下:
</p>
<p><center>
        \includegraphics[scale=1.1]{2020-1227-1100-crop}
    </center>
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x) =\begin{cases}
        3^x, & x\leqslant 0,\\
        -2x+1, & x>0,
    \end{cases}$ 若 $f(x)\leqslant \dfrac13$, 求实数 $x$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 若 $x\leqslant 0$, 则 $f(x)\leqslant \dfrac13$ 化为
    \[3^x\leqslant \frac13= 3^{-1},\quad\text{解得}\quad
        x\leqslant -1.\]
</p>
<p>(2) 若 $x> 0$, 则 $f(x)\leqslant \dfrac13$ 化为
    \[-2x+1\leqslant \frac13,\quad\text{解得}\quad
        x\geqslant \frac13.\]
</p>
<p>综上所述, $x\in (-\infty,-1]\cup \biggl[\dfrac13,+\infty\biggr)$.
</p>
</mysolution>
</p>
<p>分段函数分段考虑, 下题也是如此.
</p>
<p><myexample>
<p>已知函数 $f(x)= \begin{cases}
        ax+2-3a, & x< 0,\\
        2^x-1, & x\geqslant 0.
    \end{cases}$ 若存在 $x_1$, $x_2\in\realnum$, $x_1\neq x_2$, 使得 $f(x_1)= f(x_2)$ 成立, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>题中 $f(x)$ 的图形在 $x< 0$ 的部分为半直线, 在 $x\geqslant 0$ 的部分为 $y=2^x$ 向下平移一个单位长度. 而条件“存在 $x_1\neq x_2$ 使得 $f(x_2)= f(x_2)$ 成立”表明存在水平的直线与 $f(x)$ 的图形有两个不同的交点. 分 $a< 0$, $a=0$ 和 $a>0$ 三种情况 (分别对应半直线不同的增减性) 画图如下:
</p>
<p><center>
        \includegraphics[scale=1.1]{2020-1227-1400-crop}\qquad
        \includegraphics[scale=1.1]{2020-1227-1410-crop}\qquad
        \includegraphics[scale=1.1]{2020-1227-1420-crop}
    </center>
</p>
<p>由图可知, 当 $a\leqslant 0$ 时, 图形均合题意; 而当 $a>0$ 时, 需 $2-3a>0$ 即 $a< \dfrac23$. 由此可知, 实数 $a$ 的取值范围为 $\biggl(-\infty,-\dfrac23\biggr)$.
</p>
</mysolution>

<myexample>
<p>随着天气的变化, 某种疾病的感染人数 $y$ 与月份 $x$ 满足关系式 $y=a \cdot 0.5^x +b$. 现已知某城市今年 1 月、2 月该疾病的感染人数分别为 1 万人、1.5 万人, 求 3 月份该疾病的感染人数.
</p>
</myexample>
<mysolution>
    <p>以“万人”为 $y$ 的单位, 则
    \[\left\{\!\!\begin{array}{l}
        1= a\cdot 0.5 +b,\\
        1.5= a\cdot 0.5^2 +b,
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        a= -2,\\
        b= 2,
    \end{array}\right.\]
    所以当 $x=3$ 时, $y= -2\cdot 0.5^3+2= 1.75$, 即 3 月份该疾病的感染人数为 $1.75$ 万人.
</p>
</mysolution>
