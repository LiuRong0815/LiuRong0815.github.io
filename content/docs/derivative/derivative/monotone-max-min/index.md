---
# bookCollapseSection: true
title: 利用导数求函数的单调性与最值
weight: 4
bookHidden: true
prevPage: /docs/derivative/derivative/derivative-laws
prevPageTitle: 导数的运算法则
nextPage: /docs/probability-statistics
nextPageTitle: 概率与统计
---

# 利用导数求函数的单调性与最值

<p>利用导数的正负可以判断函数的单调性, 知识点见基础练习.
</p>
<p><myexample>
<p>下图是 $y=f(x)$ 的导函数 $f(x)$ 的图形, 判断下列四个命题是否正确:
</p>
<p>(1) $f(x)$ 有三个单调区间;\quad
    (2) $f(-2)< f(-1)$;\quad
    (3) $f(-1)< f(1)$;
</p>
<p>(4) $f(x)$ 在区间 $[-1,2]$ 上单调递增, 在 $(2,4]$ 上单调递增减.
</p>
<p><center>
        \includegraphics[scale=0.5]{2022-0425-2005}
    </center>
</p>
</myexample>
<mysolution>
    <p>由图可知, \[\begin{array}{c|cccc}
        x & (-2,-1) & (-1,2) & (2,4) & (4,5) \\
        \hline
        f'(x) & - & + & - & + \\
        f(x) & \searrow & \nearrow & \searrow & \nearrow
    \end{array}\]
    由此可知, $f(x)$ 至少有四个单调区间. 由于 $f(x)$ 在 $(-2,-1)$ 上 $\searrow$, 所以 $f(-2)> f(-1)$; 又由于 $f(x)$ 在 $(-1,2)$ 上 $\nearrow$, 所以 $f(-1)< f(1)$.
</p>
<p>综上所述, 命题 (3)(4) 正确.
</p>
</mysolution>
</p>
<p><myexample>
<p>对于定义在区间 $\biggl[-\dfrac12,4\biggr]$ 上的函数 $f(x)$, 其导函数$f'(x)$ 的图形如下图所示, 求函数 $f(x)$ 的单调递增区间和单调递减区间.
</p>
<p><center>
        \includegraphics[scale=0.45]{2022-0425-2040}
    </center>
</p>
</myexample>
<mysolution>
    <p>导数为正, 则函数递增; 导数为负, 则函数递减, 所以 $f(x)$ 的单调递增区间为 $[0,4]$, 单调递减区间为 $\biggl[-\dfrac12,0\biggr]$ (均可不含端点).
</p>
</mysolution>
</p>
<p><myexample>
<p>函数 $f(x)=ax^3+bx^2+cx+d$ 的图形如下图所示, 求 $3ax^2+2bx+c>0$ 的解集.
</p>
<p><center>
        \includegraphics[scale=0.45]{2022-0425-2045}
    </center>
</p>
</myexample>
<mysolution>
    <p>不等式即 $f'(x)>0$, 对应 $f(x)$ 单调递增区间, 由图可知, 解集为 $(-2,3)$.
</p>
</mysolution>

<myexample>
<p>判断下列函数的单调性并求极值:
</p>
<p>(1) $f(x)= \mathrm{e}^x-x$;\quad
    (2) $f(x)= \dfrac{\cos x}{x}$, $x\in\biggl(0,\dfrac\pi2\biggr)$.
</p>
</myexample>
<mysolution>
    <p>(1) 求导得 $f'(x)= \mathrm{e}^x-1$, 其零点为 $x=0$. 根据导数的单调性可列表 \[\begin{array}{c|ccc}
        x & (-\infty,0) & 0 & (0,+\infty)\\
        \hline
        f'(x) & - & 0 & + \\
        f(x) & \searrow & \text{极小} & \nearrow
    \end{array}\]
    所以 $f(x)$ 在 $(-\infty,0)$ 上单调递减, 在 $(0,+\infty)$ 上单调递增, 且有极小值 $f(0)= 1$ (也是最小值).
</p>
<p>(2) 求导得 \[
        f'(x)= \dfrac{(\cos x)'\cdot x- \cos x\cdot x'}{x}
        = -\dfrac{x\sin x+ \cos x}{x}.\]
    由 $x\in\biggl(0,\dfrac\pi2\biggr)$ 知, $f'(x)< 0$, 所以 $f(x)$ 在 $\biggl(0,\dfrac\pi2\biggr)$ 上单调递减, 无极值.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \dfrac12 ax^2 +2ax+ \ln x$ 在区间 $(0,+\infty)$ 上为增函数, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>求导得 \[
        f'(x)= ax +2a+ \frac1x
        = \frac1x (ax^2+ 2ax+1).\]
    由题意, 在区间 $(0,+\infty)$ 上恒有 $f'(x)>0$, 即 \[
        ax^2+ 2ax+1>0\Rightarrow x\in (0,+\infty).\]
    设 $g(x)= ax^2+ 2ax+1$, 则二次函数 $g(x)$ 的图形的对称轴为 $x=-1$, 且恒过定点 $(0,1)$. 由于 $g(x)>0$, 作草图知, $g(x)$ 的图形必定开口向上, 此时 $a>0$ 且已能确保 $g(x)>0$. 所以 $a$ 的取值范围为 $(0,+\infty)$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \dfrac13x^3-x^2+kx$, 且 $f(x)$ 的图形在点 $(2,f(2))$ 处的切线的斜率为 $-3$.
</p>
<p>(1) 求 $k$ 的值;\quad (2) 求 $f(x)$ 的单调区间.
</p>
</myexample>
<mysolution>
    <p>(1) 求导知 $f'(x)= x^2- 2x+ k$. 由题意, $f'(2)= -3$, 即 \[
        2^2- 2\cdot 2+ k= -3 \Rightarrow k= -3.\]
</p>
<p>(2) 由 (1) 得 \[
        f'(x)= x^2- 2x-3= (x-3)(x+1),\]
    其零点为 $x=-1$, $3$. 根据导数的图形可列表 \[\begin{array}{c|ccccc}
        x & (-\infty,-1) & -1 & (-1,3) & 3 & (3,+\infty)\\
        \hline
        f'(x) & + & 0 & - & 0 & + \\
        f(x) & \nearrow & \text{极大} & \searrow & \text{极小} &\nearrow
    \end{array}\]
    所以 $f(x)$ 在 $(-\infty,-1)$ 和 $(3,+\infty)$ 上均单调递减, 在 $(-1,3)$ 上单调递增.
</p>
</mysolution>
</p>
<p><myexample>
<p>若函数 $f(x)=x^3-3x^2+1$ 在区间 $(m,2m-1)$ 上单调递减, 求实数 $m$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>因为 \[
        f'(x)= 3x^2-6x= 3x(x-2),\]
    所以 $f(x)$ 的递减区间为 $(0,2)$, 即 \[
        0\leqslant m< 2m-1\leqslant 2,\]
    解得 $m\in\biggl(1,\dfrac32\biggr]$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \mathrm{e}^x-ax-1$.
</p>
<p>(1) 求 $f(x)$ 的单调递增区间.
</p>
<p>(2) 是否存在实数 $a$, 使得 $f(x)$ 在 $(-2,3)$ 上单调递减? 若存在, 求出 $a$ 的取值范围; 若不存在, 说明理由.
</p>
</myexample>
<mysolution>
    <p>(1) 求导得 $f'(x)= \mathrm{e}^x-a$. 下面考虑 $f'(x)$ 的正负号.
</p>
<p>当 $a\leqslant 0$ 时, $-a\geqslant 0$, 结合 $\mathrm{e}^x>0$ 知, 必有 $f'(x)>0$. 所以 $f(x)$ 在 $\mathbf{R}$ 上恒增.
</p>
<p>当 $a>0$ 时, $f'(x)= \mathrm{e}^x-a$ 在 $\mathbf{R}$ 上单调递增且有零点 $\ln a$, 可以列表 \[\begin{array}{c|ccc}
        x & (-\infty,\ln a) & \ln a & (\ln a,+\infty)\\
        \hline
        f'(x) & - & 0 & + \\
        f(x) & \searrow & 1 & \nearrow
    \end{array}\]
    所以 $f(x)$ 的单调递增区间为 $(\ln a,+\infty)$.
</p>
<p>(2) 若存在所求实数 $a$, 则在 $(-2,3)$ 上, $f'(x)< 0$, 即 \[
        \mathrm{e}^x-a< 0 \Rightarrow a>\mathrm{e}^x.\]
    因为当 $x\in(-2,3)$ 时, $\mathrm{e}^x\in (\mathrm{e}^{-2},\mathrm{e}^3)$, 所以必须有 $a\leqslant \mathrm{e}^3$. 故所求的 $a$ 确实存在, 且 $a\in[\mathrm{e}^3,+\infty)$.
</p>
</mysolution>
</p>
<p><myexample>
<p>下图是函数 $f(x)= x^3 +bx^2 +cx +d$ 的大致图形, 求 $x_1^2+x_2^2$ 的值.
</p>
<p><center>
        \includegraphics[scale=1.2]{2022-0427-2300-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>参考二次函数的两根式, 可知 $f(x)$ 必可写为 \[
        f(x)= A(x-0)(x-1)(x-2)
        = A(x^3- 3x^2+ 2x).\]
    对比已知的 $f(x)$ 表达式知, $A=1$, 所以 \[
        f(x)= x^3- 3x^2+ 2x,\quad
        f'(x)= 3x^2- 6x+ 2.\]
    图中的 $x_1$, $x_2$ 为 $f(x)$ 的图形的极值点, 也是 $f'(x)$ 的零点, 所以由韦达定理, \[
        x_1+x_2= 2,\quad x_1x_2= \frac23,\]
    因此 \[\begin{aligned}
        x_1^2+x_2^2
        &= (x_1+x_2)^2- 2x_1x_2\\
        &= 2^2- 2\cdot \frac23
         = \frac83.
    \end{aligned}\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= x\ln x$, 且 $0< x_1< x_2$, 判断下列结论是否正确:
</p>
<p>(1) $\dfrac{f(x_1)-f(x_2)}{x_1-x_2}< 0$;
</p>
<p>(2) $x_1+f(x_1)< x_2+f(x_2)$;
</p>
<p>(3) $x_2f(x_1)< x_1f(x_2)$.
</p>
</myexample>
<mysolution>
    <p>(1) 原不等式表明 $x_1-x_2$ 与 $f(x_1)-f(x_2)$ 的正负号相反, 即 $x_1$ 与 $x_2$ 的大小关系与 $f(x_1)$ 和 $f(x_2)$ 的大小关系相反, 所以等价于 $f(x)$ 单调递减. 因为当 $x>\dfrac1{\mathrm{e}}$ 时, $f'(x)= \ln x+1>0$, 此时 $f(x)$ 单调递增, 所以原不等式不成立.
</p>
<p>(2) 结合 $x_1< x_2$ 知, 原不等式表明 $x+f(x)$ 单调递增. 由 \[
        (x+f(x))'= 1+ \ln x+ 1= \ln x+2\]
    知, 当 $0< x< \mathrm{e}^{-2}$ 时, $(x+f(x))'< 0$, 此时 $x+f(x)$ 单调递减, 所以原不等式不成立.
</p>
<p>(3) 由题意, $x_1$, $x_2$ 均为正数, 原不等式化为 $\dfrac{f(x_1)}{x_1}< \dfrac{f(x_2)}{x_2}$. 再结合 $x_1< x_2$ 知, 不等式等价于 $\dfrac{f(x)}{x}= \ln x$ 单调递增, 这显然成立.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \mathrm{e}^x- \dfrac{x+1}{x-1}$.
</p>
<p>(1) 求曲线 $y= f(x)$ 在点 $(0,f(0))$ 处的切线方程;
</p>
<p>(2) 判断函数 $f(x)$ 的零点的个数;
</p>
<p>(3) 设 $x_0$ 是 $f(x)$ 的一个零点, 证明: 曲线 $y= \mathrm{e}^x$ 在点 $(x_0,\mathrm{e}^{x_0})$ 处的切线也是曲线 $y= \ln x$ 的切线.
</p>
</myexample>
<mysolution>
    <p>(1) 因为 \[\begin{aligned}
        f'(x)&= \mathrm{e}^x- \frac{(x+1)'\cdot (x-1)- 
            (x+1)\cdot (x-1)'}{(x-1)^2}\\
        &= \mathrm{e}^x+ \frac2{(x-1)^2},
    \end{aligned}\]
    则所求切线的斜率为 $f'(0)= 1+2= 3$, 而 $f(0)= 1-(-1)= 2$, 所以所求切线方程为 \[
        y- f(0)= f'(0)(x-0),\Rightarrow
        y=3x+2.\]
</p>
<p>(2) 由 $f'(x)= \mathrm{e}^x+ \dfrac2{(x-1)^2}>0$ 知, $f(x)$ 在区间 $(-\infty,1)$ 和 $(1,+\infty)$ 上均单调递增, 至多各一个零点. 因为 \[\begin{aligned}
        f(1.1)&= \mathrm{e}^{1.1}- \dfrac{1.1+1}{1.1-1}
            = \mathrm{e}^{1.1}- 21\\
        &< 3^2- 21< 0,\\
        f(2)&= \mathrm{e}^2- \dfrac{2+1}{2-1}
            = \mathrm{e}^2- 3\\
        &> 2^2-3>0,
    \end{aligned}\]
    所以 $f(x)$ 在 $(1,+\infty)$ 上有一个零点, 且在 $(1.1,2)$ 内部. 
</p>
<p>又因为 $f(0)=3>0$, 而 \[\begin{aligned}
        f(-3)&= \mathrm{e}^{-3}- \dfrac{-3+1}{-3-1}
            = \mathrm{e}^{-3}- \frac12\\
        &< 2^{-3}- \frac12< 0,
    \end{aligned}\]
    所以 $f(x)$ 在 $(-\infty,1)$ 上也有一个零点, 且在 $(-3,0)$ 内部.
</p>
<p>综上所述, $f(x)$ 有恰两个零点.
</p>
<p>(3) 因为 $y= \mathrm{e}^x$ 的导数为 $y'= \mathrm{e}^x$, 所以曲线 $y=\mathrm{e}^x$ 在点 $(x_0,\mathrm{e}^{x_0})$ 处的切线方程为 \[\begin{gathered}
        y- \mathrm{e}^{x_0}= \mathrm{e}^{x_0}(x-x_0),\\
        y= \mathrm{e}^{x_0} x- (x_0-1)\mathrm{e}^{x_0}.
    \end{gathered}\]
    由 $x_0$ 是 $f(x)$ 的一个零点知, $\mathrm{e}^{x_0}= \dfrac{x_0+1}{x_0-1}$, 代入上式, \[
        y= \mathrm{e}^{x_0} x- (1+ x_0).\]
</p>
<p>因为 $y= \ln x$ 的导数为 $y'= \dfrac1x$, 所以曲线 $y=\ln x$ 在其上一点 $(x_1,\ln x_1)$ 处的切线方程为 \[\begin{gathered}
        y- \ln x_1= \frac1{x_1}(x-x_1),\\
        y= \frac1{x_1} x- (1+\ln \frac1{x_1}).
    \end{gathered}\]
    对比上式和前一个切线方程知, 取 $\dfrac1{x_1}= \mathrm{e}^{x_0}$ 即 $x_1= \mathrm{e}^{-x_0}$, 两式表示同一条直线, 也表明两条切线重合. 此时 $x_1>0$, 即 $x_1$ 确实在 $y= \ln x$ 的定义域中. 所以结论成立.
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \mathrm{e}^x-ax$.
</p>
<p>(1) 讨论 $f(x)$ 的单调区间;
</p>
<p>(2) $\forall\,x\in (0,+\infty)$, 都有 $f(x)> 0$ 恒成立, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 见“2022 年 3 月 12 日答疑记录”第 5 题 (1) 的解法.
</p>
<p>(2) 对 $x\in (0,+\infty)$, $f(x)> 0$ 等价于 $\dfrac{\mathrm{e}^x}{x}>a$. 设 $g(x)= \dfrac{\mathrm{e}^x}{x}$, $x\in (0,+\infty)$, 只需求 $g(x)$ 的最小值. 因为 \[
        g'(x)= \dfrac{\mathrm{e}^x\cdot x- \mathrm{e}^x\cdot 1}{x^2}
        = \dfrac{\mathrm{e}^x(x- 1)}{x^2},\]
    可列表 \[\begin{array}{c|ccc}
        x & (0,1) & 1 & (1,+\infty) \\
        \hline
        g'(x) & - & 0 & + \\
        g(x) & \searrow & \text{极小} & \nearrow
    \end{array}\]
    所以 $g(x)$ 在 $(0,+\infty)$ 上最小值为 $g(1)= \mathrm{e}$, 即 $a$ 的取值范围为 $(-\infty,\mathrm{e})$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \dfrac13 ax^3 +2x^2 +(a-3)x-1$, $a\in\mathbf{R}$.
</p>
<p>(1) 若 $a=3$, 求函数 $f(x)$ 的零点个数;
</p>
<p>(2) 从下列两个条件中选择一个作为已知, 求实数 $a$ 的取值范围.
</p>
<p>条件一: 函数 $f(x)$ 是单调函数;
</p>
<p>条件二: 函数 $f(x)$ 有且只有一个大于零的极值点.
</p>
</myexample>
<mysolution>
    <p>(1) 当 $a=3$ 时, $f(x)= x^3 +2x^2 -1$, 则 \[
        f'(x)= 3x^2 +4x= x(3x+4),\]
    可列表 \[\begin{array}{c|ccccc}
        x & \biggl(-\infty, -\dfrac43\biggr) & -\dfrac43 
        & \biggl(-\dfrac43, 0\biggr) & 0 & (0,+\infty) \\
        \hline
        f'(x) & + & 0 & - & 0 & + \\
        f(x) & \nearrow & \text{极大} & \searrow & \text{极小} & \nearrow
    \end{array}\]
    由此可得, $f(x)$ 的极大值为 \[
        f\biggl(-\dfrac43\biggr)
        = -\frac{64}{27}+ \frac{32}{9}- 1
        = \frac{5}{27}>0,\]
    极小值为 $f(0)= -1$. 作三次函数 $f(x)$ 的草图可知, $f(x)$ 有三个零点.
</p>
<p>(2) 对 $f(x)$ 求导知, \[
        f'(x)= ax^2 +4x +(a-3).\]
</p>
<p>若选条件一, 则要么 $f'(x)\geqslant 0$ 恒成立, 要么 $f'(x)\leqslant 0$ 恒成立. 因为 $f'(x)$ 为二次函数, 所以 $a\neq 0$, 且此时 $f'(x)$ 的判别式 \[
        \Delta= 4^2- 4a(a-3)\leqslant 0,\]
    解得 $a\in(-\infty,-1]\cup [4,+\infty)$. 
</p>
<p>若选条件二, 则 $f'(x)$ 有且只有一个大于零的根. 若 $a=0$, 则 $f'(x)= 4x-3$, 根为 $x=\dfrac34$, 满足题意. 若 $a\neq 0$, 则 $f'(x)$ 为二次函数, 另外一个根小于或等于零. 此时 $f'(x)$ 的判别式 \[
        \Delta= 4^2- 4a(a-3)> 0,\]
    解得 $a\in(-1,4)$. 再由韦达定理, \[
        \frac{a-3}{a}\leqslant 0 \Rightarrow
        a\in(0,3]\subset (-1,4).\]
    综上所述, $a\in [0,3]$ 为所求.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \dfrac{x-1}{\mathrm{e}^x}$.
</p>
<p>(1) 求函数 $f(x)$ 的单调区间;
</p>
<p>(2) 求证: 当 $x\in(-\infty,0)$ 时, $f(x)< -\dfrac12 x^2+2x-1$.
</p>
</myexample>
<mysolution>
    <p>(1) 对 $f(x)$ 求导, \[
        f'(x)= \frac{1\cdot\mathrm{e}^x- (x-1)\mathrm{e}^x}{(\mathrm{e}^x)^2}
        = \frac{2-x}{\mathrm{e}^x},\]
    零点为 $x=2$, 所以可列表 \[\begin{array}{c|ccc}
        x & (-\infty, 2) & 2 & (2,+\infty) \\
        \hline
        f'(x) & + & 0 & - \\
        f(x) & \nearrow & \text{极大} & \searrow 
    \end{array}\]
    由此可得, $f(x)$ 在 $(-\infty,2)$ 上单调递增, 在 $(2,+\infty)$ 上单调递减.
</p>
<p>(2) 构造辅助函数 \[\begin{aligned}
        g(x)&= f(x)- \biggl(-\frac12 x^2+2x-1\biggr)\\
        &= \dfrac{x-1}{\mathrm{e}^x}+ \frac12 x^2-2x+1,
    \end{aligned}\]
    只需证明当 $x\in(-\infty,0)$ 时, $g(x)< 0$. 因为 \[\begin{aligned}
        g'(x)&= \frac{2-x}{\mathrm{e}^x}+ x- 2
         = (x- 2)\biggl(1- \frac1{\mathrm{e}^x}\biggr) \\
        &= \frac{1}{\mathrm{e}^x}(x-2)(\mathrm{e}^x -1),
    \end{aligned}\]
    其零点为 $x=0$, $2$, 而已知 $x\in(-\infty,0)$, 所以 \[
        x-2< 0,\quad \mathrm{e}^x-1< 0,\]
    表明 $g'(x)>0$. 因此 $g(x)$ 在 $x\in(-\infty,0)$ 时单调递增, 故 \[
        g(x)\leqslant g(0)
        = \dfrac{-1}{\mathrm{e}^0}+ \frac12\cdot 0-2\cdot 0+1= 0.\]
    所求证的结论成立.
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \mathrm{e}^x+ ax$, $a\in\mathbf{R}$.
</p>
<p>(1) 若 $a< 0$, 求函数 $f(x)$ 的单调区间;
</p>
<p>(2) 若 $a= 3$, 证明: 当 $x> 0$ 时, $f(x)> x^2+3x+1$ 恒成立.
</p>
</myexample>
<mysolution>
    <p>(1) 当 $a< 0$ 时, $f'(x)= \mathrm{e}^x+ a$ 有零点 $\ln(-a)$, 故可以列表可得单调区间: \[\begin{array}{c|ccc}
        x & (-\infty,\ln(-a)) & \ln(-a) & (\ln(-a),+\infty)\\
        \hline
        f'(x) & - & 0 & + \\
        f(x) & \searrow & \text{最小值} & \nearrow
    \end{array}\]
</p>
<p>(2) 当 $a= 3$ 时, 原不等式化为 \[\begin{gathered}
        \mathrm{e}^x+ 3x> x^2+3x+1 \Rightarrow
        \mathrm{e}^x- x^2> 1
    \end{gathered}.\]
    设辅助函数 $g(x)= \mathrm{e}^x- x^2$, 则 $g'(x)= \mathrm{e}^x- 2x$. 现在应该判断 $g'(x)$ 的正负号, 但通常的求 $g'(x)$ 的零点的方法在此失效, 所以改为确定其值域, 即还要再次求导. 因为 $g”(x)= \mathrm{e}^x- 2$ 的零点为 $\ln 2$, 所以结合已知的 $x> 0$ 列表如下: \[\begin{array}{c|ccc}
        x & (0,\ln 2) & \ln 2 & (\ln 2,+\infty)\\
        \hline
        g”(x) & - & 0 & + \\
        g'(x) & \searrow & \text{最小值} & \nearrow
    \end{array}\]
    由此得 \[
        g'_{\min}= g'(\ln 2)
        = \mathrm{e}^{\ln 2}- 2\ln 2
        = 2(1-\ln 2).\]
    因为 $\ln 2\in (0,1)$, 所以 $g'_{\min}> 0$, 说明 $g'(x)$ 恒正, 而 $g(x)$ 恒增. 故 \[
        g(x)> g(0)= \mathrm{e}^0- 0^2= 1,\]
    表明 $\mathrm{e}^x- x^2> 1$ 在 $x> 0$ 时恒成立, 这等价于要证明的结论.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \mathrm{e}^x+ \cos x$, $x\in [0,+\infty)$.
</p>
<p>(1) 求函数 $f(x)$ 在 $[0,\pi]$ (指 $x$ 的范围) 上的最值;
</p>
<p>(2) 若 $a> 1$, 求证: 函数 $f(x)$ 的图形上总存在位于直线 $y= ax+2$ 下方的点.
</p>
</myexample>
<mysolution>
    <p>(1) 因为 $f'(x)= \mathrm{e}^x- \sin x$, 且 $x\in[0,\pi]$, 所以 \[
        \mathrm{e}^x\in [1,\mathrm{e}^{\pi}], \sin x\in[0,1]
        \Rightarrow \mathrm{e}^x- \sin x\geqslant 0.\]
    从而 $f(x)$ 在 $[0,\pi]$ 上单调递增, \[
        f_{\min}= f(0)= 2,\quad 
        f_{\max}= f(\pi)= \mathrm{e}^{\pi}.\]
</p>
<p>(2) 方法一: 先给出几何方法, 依赖于函数图形 (可能无法拿全分). $f(x)$ 在点 $(0,f(0))= (0,2)$ 处的切线为 \[
        y- f(0)= f'(0)(x-0)\Rightarrow y= x+ 2.\]
    因为直线 $y= ax+2$ 过定点 $(0,2)$, 且 $a> 1$, 所以与上述切线对比可知, 此直线必为 $f(x)$ 的图形的割线, 即其与 $f(x)$ 的图形有两个交点. 画草图可知结论成立.
</p>
<p>方法二: 作辅助函数 $g(x)= f(x)- (ax+2)$, 题意表明 $g(x)$ 应该总能取到负值, 即要证明 $g_{\min}< 0$. 对 $g(x)$ 求导, \[
        g'(x)= f'(x)- a= \mathrm{e}^x- \sin x- a,\]
    然后判断其正负号. 由 $a> 1$ 知 $g'(0)= 1-a< 0$, 而 $g'(x)$ 的图形是连续的, 所以在 $x=0$ 附近一个小区间内也有 $g'(x)< 0$, 此时 $g(x)$ 单调递减. 结合 \[
        g(0)= f(0)- (a\cdot 0+ 2)= 0\]
    可知, 在 $x=0$ 附近 $g(x)< g(0)= 0$, 因此 $g_{\min}< 0$, 结论成立.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 对于图形连续的函数 $F(x)$, 作图可知, 若 $F(a)< 0$, 则在含 $a$ 的一个小区间内仍有 $F(x)< 0$; 若 $F(a)> 0$, 则在含 $a$ 的一个小区间内仍有 $F(x)> 0$. 这个性质是连续函数的保号性, 解题时可以直接使用.
</p>
<p>(2) 从上面两个例子可以看出, 要判断函数的正负号, 关键仍是确定其单调性.
</p>
</myremark>

<myexample>
<p>已知函数 $f(x)=2x^3 -ax^2 +2$.
</p>
<p>(1) 讨论 $f(x)$ 的单调性;
</p>
<p>(2) 当 $0< a< 3$ 时, 求 $f(x)$ 在区间 $[0,1]$ 上的最大值及最小值.
</p>
</myexample>
<mysolution>
    <p>(1) 对 $f(x)$ 求导可得, \[
        f'(x)= 6x^2 -2ax= 2x(3x-a).\]
</p>
<p>当 $a=0$ 时, $f'(x)= 6x^2\geqslant 0$, 则 $f(x)$ 单调递增.
</p>
<p>当 $a< 0$ 时, $f'(x)$ 的零点为 $\dfrac{a}3$ 和 $0$, 且 $\dfrac{a}3< 0$, 所以可列表 \[\begin{array}{c|ccccc}
        x & \biggl(-\infty, \dfrac{a}3\biggr) & \dfrac{a}3 
        & \biggl(\dfrac{a}3, 0\biggr) & 0 & (0,+\infty) \\
        \hline
        f'(x) & + & 0 & - & 0 & + \\
        f(x) & \nearrow & \text{极大} & \searrow & \text{极小} & \nearrow
    \end{array}\]
</p>
<p>当 $a>0$ 时, $f'(x)$ 的零点为 $\dfrac{a}3$ 和 $0$, 且 $\dfrac{a}3>0$, 所以可列表 \[\begin{array}{c|ccccc}
        x & (-\infty, 0) & 0 & \biggl(0,\dfrac{a}3\biggr)
         & \dfrac{a}3 & \biggl(\dfrac{a}3,+\infty\biggr) \\
        \hline
        f'(x) & + & 0 & - & 0 & + \\
        f(x) & \nearrow & \text{极大} & \searrow & \text{极小} & \nearrow
    \end{array}\]
</p>
<p>(2) 当 $0< a< 3$ 时, $\dfrac{a}3\in(0,1)$. 参照 (1) 中 $a>0$ 的情形考虑区间 $[0,1]$ 可知, $f(x)$ 在 $\biggl[0,\dfrac{a}3\biggr)$ 上单调递减, 在 $\biggl(\dfrac{a}3, 1\biggr]$ 上单调递增, 故最小值为 \[
        f\biggl(\dfrac{a}3\biggr)
        = 2\biggl(\frac{a}3\biggr)^3- a\cdot\biggl(\frac{a}3\biggr)^2-2
        = 2-\dfrac{a^2}{27},\]
    最大值为 $f(0)$ 和 $f(1)$ 中较大者. 因为 \[
        f(0)-f(1)= 2- (4-a)= a-2,\]
    所以当 $a\in(0,2]$ 时, $f(0)\leqslant f(1)$, 即 $f(x)$ 的最大值为 $f(1)= 4-a$; 当 $a\in(2,3]$ 时, $f(0)> f(1)$, 即 $f(x)$ 的最大值为 $f(0)=2$.
</p>
</mysolution>

<myexample>
<p>已知 $f(x)= -x^3+ ax^2+ ax+3$ 在定义域上单调递减, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由题意, 恒有 \[
        f'(x)= -3x^2+ 2ax+ a\leqslant 0.\]
    由二次函数图形可知, \[
        \Delta= (2a)^2- 4\cdot(-3)a\leqslant 0\Rightarrow
        a\in[-3,0].\]
</p>
</mysolution>
</p>
<p><myexample>
<p>在同一个直角坐标系中绘出 $y=f(x)$ 和 $y=f'(x)$ 的图形,
    <center>
        \includegraphics[scale=0.8]{2022-0504-1430-crop}\qquad
        \includegraphics[scale=0.8]{2022-0504-1435-crop}\\[6pt]
        \includegraphics[scale=0.8]{2022-0504-1440-crop}\qquad
        \includegraphics[scale=0.8]{2022-0504-1445-crop}\qquad
    </center>
    哪个图是不可能的?
</p>
</myexample>
<mysolution>
    <p>根据“导数的正负对应原函数的增减”, 
</p>
<p>在 (1) 中以曲线为 $f(x)$, 直线为 $f'(x)$ (如令 $f(x)= x^2$); 
</p>
<p>在 (2) 中以单增曲线为 $f(x)$, 第一象限的曲线为 $f'(x)$ (如令 $f(x)= \ln x$); 
</p>
<p>在 (3) 中以某一条曲线为 $f(x)$, 另一条曲线 $f'(x)$ (如令 $f(x)= 2^x$), 
</p>
<p>可以知道 (1), (2), (3) 都是可能的. 但是在 (4) 中无论以哪条曲线为 $f(x)$, 另一条曲线为 $f'(x)$, 都与前述结论不符.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= a\ln x+\dfrac{x^2}2-(a+1)x$, $a\in\mathbf{R}$.
</p>
<p>(1) 当 $a=-1$ 时, 求 $f(x)$ 在点 $(1,f(1))$ 处的切线方程;
</p>
<p>(2) 求 $f(x)$ 在区间 $[2,\mathrm{e}]$ 上的最小值;
</p>
<p>(3) 当 $0\leqslant a\leqslant 1$ 时, 求 $f(x)$ 的零点个数.
</p>
</myexample>
<mysolution>
    <p>(1) 此时, $f(x)= -\ln x+\dfrac{x^2}2$, 则 \[
        f(1)= \frac12,\quad f'(x)= -\frac1x+x\Rightarrow f'(1)= 0,\]
    所求切线方程为 \[
        y- f(1)= f'(1)(x-1)\Rightarrow
        y= \dfrac12.\]
</p>
<p>(2) 求导可得, \[\begin{aligned}
        f'(x)&= \frac{a}{x}+ x-(a+1)\\
        &= \frac1x[x^2- (a+1)x+a]\\
        &= \frac{x-1}x (x-a).
    \end{aligned}\]
    因为 $x\in[2,\mathrm{e}]$, 所以 $\dfrac{x-1}x>0$, 只需考虑 $x-a$ 的正负号.
</p>
<p>若 $a\leqslant 2$, 则 $x-a\geqslant 0$, $f'(x)\geqslant 0$, 所以 $f(x)$ 在 $[2,\mathrm{e}]$ 上单调递增, 而 \[
        f_{\min}= f(2)= a(\ln2- 2).\]
</p>
<p>若 $a\geqslant \mathrm{e}$, 则 $x-a\leqslant 0$, $f'(x)\leqslant 0$, 所以 $f(x)$ 在 $[2,\mathrm{e}]$ 上单调递减, 而 \[
        f_{\min}= f(\mathrm{e})
        = a+\dfrac{\mathrm{e}^2}2-(a+1)\mathrm{e}.\]
</p>
<p>若 $2< a< \mathrm{e}$, 则可列表 \[\begin{array}{c|ccc}
        x & [2,a) & a & (a,\mathrm{e}] \\
        \hline
        f'(x) & - & 0 & + \\
        f(x) & \searrow & \text{极小} & \nearrow 
    \end{array}\]
    所以 $f(x)$ 在 $[2,\mathrm{e}]$ 上的最小值 \[
        f_{\min}= f(a)= a\ln a- \frac{a^2}2-a.\]
</p>
<p>(3) (此问略难, 可以不做, 且原始题目不要求写过程) 若 $a=0$, 则 \[
        f(x)= \dfrac{x^2}2-x= \frac{x}2(x-2),\]
    有两个零点 $0$, $2$. 结合函数的定义域 $(0,+\infty)$ 知, $f(x)$ 仅有一个零点.
</p>
<p>若 $a= 1$, \[
        f(x)= \ln x+\dfrac{x^2}2-2x,\]
    定义域为 $(0,+\infty)$, 且由 (2) 得 \[
        f'(x)= \frac{(x-1)^2}x\geqslant 0,\]
    所以 $f(x)$ 单调递增. 再考虑 $f(x)$ 的函数值变化趋势. 当正数 $x\to 0$ 时, \[
        \ln x\to -\infty,\quad \dfrac{x^2}2-2x\to 0,\]
    所以 $f(x)\to -\infty$. 当正数 $x\to +\infty$ 时, \[
        \ln x\to +\infty,\quad \dfrac{x^2}2-2x\to +\infty,\]
    所以 $f(x)\to +\infty$. 由连续函数的图形可知, $f(x)$ 仅有一个零点.
</p>
<p>若 $0< a< 1$, 仍由 (2) 得 \[
        f'(x)= \frac1x (x-a)(x-1),\]
    可列表 \[\begin{array}{c|ccccc}
        x & (0,a) & a 
        & (a,1) & 1 & (1,+\infty) \\
        \hline
        f'(x) & + & 0 & - & 0 & + \\
        f(x) & \nearrow & \text{极大} & \searrow & \text{极小} & \nearrow
    \end{array}\]
    极大值为 \[
        f(a)= a\ln a- \frac{a^2}2-a< 0,\]
    且仍有当正数 $x\to +\infty$ 时, $f(x)\to +\infty$. 根据单调性作草图可知, $f(x)$ 仅有一个零点.
</p>
<p>综上所述, 当 $0\leqslant a\leqslant 1$ 时, $f(x)$ 仅有一个零点.
</p>
</mysolution>

