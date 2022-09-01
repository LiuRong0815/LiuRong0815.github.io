---
# bookCollapseSection: true
title: 常见导数公式
weight: 2
bookHidden: true
prevPage: /docs/derivative/derivative/derivative-def
prevPageTitle: 导数的定义与意义
nextPage: /docs/derivative/derivative/derivative-laws
nextPageTitle: 导数的运算法则
---

# 常见导数公式


<myexample>
<p>曲线 $y= x^2$ 在点 $P$ 处的切线的倾斜角为 $\dfrac\pi4$, 求点 $P$ 的坐标.
</p>
</myexample>
<mysolution>
    <p>设 $P(x_0,y_0)$, 因为 $y= x^2$ 的导数为 $y'= 2x$, 所以 \[
        2x_0= \tan\frac\pi4,\quad x_0= \frac12,\]
    而 $y_0= x_0^2= \dfrac14$. 点 $P$ 的坐标为 $\biggl(\dfrac12,\dfrac14\biggr)$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= ax^2+b$ 的图形开口向下, \[
        \lim_{\Delta x\to 0} \frac{f(a+\Delta x)- f(a)}{\Delta x}= 4,\]
    求 $a$ 的值.
</p>
</myexample>
<mysolution>
    <p>题中式子为导数 $f'(a)$ 的定义, 则 $f'(a)= 4$. 因为 $f'(x)= 2ax$, 所以 \[
        2a\cdot a= 4,\quad a= \pm2.\]
    因为函数 $f(x)= ax^2+b$ 的图形开口向下, 所以 $a< 0$, 则 $a=-2$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知曲线 $y= ax^2+b$ 在点 $(1,3)$ 处的切线的斜率为 $2$, 求 $a$, $b$ 的值.
</p>
</myexample>
<mysolution>
    <p>$y= ax^2+b$ 的导数为 $y'= 2ax$, 所以 \[
        3= a\cdot 1^2+b,\quad 2= 2a\cdot 1,\]
    解得 $a=1$, $b=2$.
</p>
</mysolution>
</p>
<p><myexample>
<p>求下列函数的导数:
</p>
<p>(1) $f(x)= (1+\sin x)(1- 4x)$;\quad 
    (2) $g(x)= \dfrac{x}{x+1}$.
</p>
</myexample>
<mysolution>
    <p>(1) 将 $f(x)$ 展开, \[
        f(x)= 1+\sin x- 4x- 4x\sin x,\]
    求导得 \[\begin{aligned}
        f'(x)&= \cos x- 4- (4\sin x+ 4x\cos x)\\
        &= \cos x- 4- 4\sin x- 4x\cos x.
    \end{aligned}\]
</p>
<p>(2) 直接用求导公式, \[\begin{aligned}
        g(x)&= \frac{x'(x+1)- x(x+1)'}{(x+1)^2}\\
        &= \frac{(x+1)- x}{(x+1)^2}
         = \frac{1}{(x+1)^2}.
    \end{aligned}\]
</p>
</mysolution>

<myexample>
<p>求下列函数的导数:
</p>
<p>(1) $y= 2x^2+ \dfrac1x- \dfrac3{x^2}$;\quad
    (2) $y= x\sin x$;\quad
    (3) $y= \mathrm{e}^x\ln x$;
</p>
<p>(4) $y= (2x^2-5x+2)\mathrm{e}^x$;\quad
    (5) $y= \dfrac{x-1}{x+1}$;\quad
    (6) $y= \dfrac{4+ \ln x}{x}$.
</p>
</myexample>
<mysolution>
    <p>(1) 先将函数改写为 $y= 2x^2+ x^{-1}- 3x^{-2}$, 则 \[
        y'= 4x- x^{-2}+ 6x^{-3}.\]
</p>
<p>(2) 直接用积的导数公式, \[
        y'= 1\cdot \sin x+ x\cdot \cos x
        = \sin+ x\cos x.\]
</p>
<p>(3) $y'= \mathrm{e}^x\ln x+ \dfrac{\mathrm{e}^x}x$.
</p>
<p>(4) 用积的导数公式, \[\begin{aligned}
        y&= (4x-5)\mathrm{e}^x+ (2x^2-5x+2)\mathrm{e}^x\\
        &= (2x^2-x-3)\mathrm{e}^x.
    \end{aligned}\]
</p>
<p>(5) 用商的导数公式, \[
        y= \dfrac{1\cdot(x+1)- (x-1)\cdot 1}{(x+1)^2}
        = \dfrac{2}{(x+1)^2}.\]
</p>
<p>(6) 用商的导数公式, \[
        y= \dfrac{\dfrac1x\cdot x- (4+\ln x)\cdot 1}{x^2}
        = \dfrac{-3-\ln x}{x^2}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>求下列函数的导数:
</p>
<p>(1) $y= \mathrm{e}^{-x}$;\quad
    (2) $y= \ln(3x)$;\quad
    (3) $y= (3x+1)\ln(3x)$.
</p>
</myexample>
<mysolution>
    <p>(1) 将函数改写为 $y= \dfrac{1}{\mathrm{e}^x}$, 再由商的导数公式, \[
        y'= \dfrac{0\cdot \mathrm{e}^x- 1\cdot \mathrm{e}^x}{(\mathrm{e}^x)^2}
        = -\dfrac{1}{\mathrm{e}^x}.\]
</p>
<p>(2) 将函数改写为 $y= \ln 3+ \ln x$, 再由和的导数公式, \[
        y'= 0+\frac1x= \frac1x.\]
</p>
<p>(3) 因为 $\ln(3x)= \ln 3+ \ln x$, 所以 \[\begin{aligned}
        y'&= 3(\ln3+ \ln x)+ (3x+1)\frac1x\\
        &= 3(\ln3+ 1)+ 3\ln x+\frac1x.
    \end{aligned}\]
</p>
</mysolution>

<myexample>
<p>求下列函数的导数:
</p>
<p>(1) $y=(2x^2+3)(3x-1)$;\quad 
    (2) $y=x-\sin\dfrac{x}2\cos\dfrac{x}2$;\quad 
    (3) $y= \dfrac{\ln x}{x^2+1}$.
</p>
</myexample>
<mysolution>
    <p>(1) 先将函数式展开, \[
        y= 6x^3-2x^2+9x-3,\]
    再求导, \[
        y'= 18x^2- 4x+9.\]
</p>
<p>(2) 函数可化为 $y=x- \dfrac12\sin x$, 则 \[
        y= 1- \dfrac12\cos x.\]
</p>
<p>(3) 由商的导数公式, \[
        y= \dfrac{\dfrac1x\cdot (x^2+1)- \ln x\cdot (2x)}{(x^2+1)^2}
        = \dfrac{x+\dfrac1x- 2x\ln x}{(x^2+1)^2}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>求曲线 $y=x\ln x$ 在点 $M(\mathrm{e},\mathrm{e})$ 处的切线方程.
</p>
</myexample>
<mysolution>
    <p>$y= x\ln x$ 的导数为 $y'= \ln x+1$, 所求切线的斜率 \[
        k= \ln \mathrm{e}+1= 2,\]
    则切线方程为 \[
        y- \mathrm{e}= 2(x- \mathrm{e})\Rightarrow
        y= 2x- \mathrm{e}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>设直线 $y=-3x+m$ 是曲线 $y=x^3-3x^2+3$ 的一条切线, 求实数 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>设切点为 $(x_0,y_0)$. 因为曲线对应函数的导数为 $y'= 3x^2-6x$, 切线斜率为 $-3$, 所以 \[
        3x_0^2-6x_0= -3,\quad x_0=1.\]
    因为切点在曲线上, 所以 \[
        y_0= x_0^3-3x_0^2+3= 1,\]
    而切点又在切线上, 则 \[
        y_0= -3x_0+m,\quad m= 4.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>设曲线 $y=x^{n+1}\ (n\in N^+)$ 在点 $(1,1)$ 处的切线与 $x$ 轴的交点的横坐标为 $x_n$, 令 $a_n= \lg x_n$, 求 $a_1+ a_2+ \cdots+ a_{99}$ 的值.
</p>
</myexample>
<mysolution>
    <p>因为 $y=x^{n+1}$ 的导数为 $y'=(n+1)x^n$, 所以在点 $(1,1)$ 处的切线斜率为 \[
        k= (n+1)\cdot 1^n= n+1,\]
    切线方程为 \[
        y-1= (n+1)(x-1).\]
    再求切线与 $x$ 轴的交点的横坐标, 在上式中令 $y=0$, 得 \[
        -1= (n+1)(x_n-1),\quad x_n= 1-\frac1{n+1}.\]
    因此 \[
        a_n= \lg x_n= \lg \biggl(1-\frac1{n+1}\biggr)
        = \lg\frac{n}{n+1},\]
    继而 \[\begin{aligned}
        &a_1+ a_2+ \cdots+ a_{99}\\
        ={}& \lg\frac12+ \lg\frac23+\cdots+ \lg\frac{99}{100}\\
        ={}& \lg\biggl(\frac12\cdot \frac23\cdot\,\cdots\,\cdot \frac{99}{100}\biggr)\\
        ={}& \lg\frac1{100}= -2.
    \end{aligned}\]
</p>
</mysolution>

