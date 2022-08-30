---
# bookCollapseSection: true
title: 反函数
weight: 5
bookHidden: true
prevPage: /docs/algebra/pow-exp-log/logarithm-function
prevPageTitle: 对数函数
nextPage: /docs/algebra/pow-exp-log/function-equation
nextPageTitle: 利用函数图象研究方程
---

# 复合函数与反函数

<p>本次答疑主要讲解复合函数的值域和单调区间的求法. 函数 $f(x)$ 和 $g(x)$ 可以复合成函数 $f(g(x))$, $g(f(x))$, $f(f(x))$ 等, 也可以复合成函数 $f(g(f(x)))$, $g(g(f(x)))$, $g(g(g(g(x))))$ 
%(此时一般记为 $g\circ g\circ g\circ g(x)$) 
等. 例如, 若 $f(x)=x^2$, $g(x)=x+1$, 则
\[\begin{gathered}
    f(g(x))= (x+1)^2,\quad g(f(x))= x^2+1,\\
        f(f(x))= (x^2)^2= x^4,\quad g(g(x))= (x+1)+1= x+2.
\end{gathered}\]
“复合函数”可以简单理解为“函数套函数”. 
</p>
<p>有时为了理解方便起见, 对函数 $y=f(g(x))$, 可设 $u=g(x)$ 而将其表示为 $y=f(u)$, 即借助中间变量 $u$ 表示为较简单的形式. 例如,
\[\begin{aligned}
    y=\sqrt{x^2-2x-3}&\colon y=f(u)=\sqrt{u},\ u=g(x)= x^2-2x-3;\\
    y=\log_{\frac13} (-x^2-2x+8)&\colon y=f(u)=\log_{\frac13}{u},\ u=g(x)= -x^2-2x+8;\\
    y=\frac1{x^2-3x}&\colon y=f(u)=\frac1{u},\ u=g(x)= x^2-3x;\\
    y=3^{|x|}&\colon y=f(u)=3^{u},\ u=g(x)= |x|.
\end{aligned}\]
这时我们可称 $g(x)$ 为“里层函数”, 而 $f(u)$ 为“外层函数”. 在求值域时, 可以先根据定义域 ($x$ 的取值范围) 求里层函数 (即 $g(x)$) 的值域, 从而得到 $u$ 的取值范围 (即 $f(u)$ 的定义域), 再由 $f(u)$ 的表达式求其值域, 最终得到 $f(g(x))$ 的值域, 即有如下求值流程:
\[x\xrightarrow{\ g\ } u=g(x)\xrightarrow{\ f\ } y=f(u)= f(g(x))\]
或简化为
\[x\xrightarrow{\ g\ } g(x)\xrightarrow{\ f\ } f(g(x)).\]
例如, 求函数 $y=\sqrt{x^2-2x-3}$ 的值域时, 先由 
\[x^2-2x-3\geqslant 0\quad\text{解得}\quad x\in(-\infty,-1]\cup[3,+\infty)\quad \text{(自然定义域)},\]
所以 $u=x^2-2x-3\in[0,+\infty)$, 再由 $y=\sqrt{u}$ 单调递增可知 $y\in[0,+\infty)$.
</p>
<p>判断复合函数的单调性则稍微复杂一些, 不过结论很容易记忆: <strong>同增异减</strong>. 具体来说, 就是若里层函数与外层函数</p>
<p>(1) 单调性相同, 则复合函数单调递增; 
</p>
<p>(2) 单调性不同, 则复合函数单调递减. 
</p>
<p>理解这一结论时, 需要先弄清楚单调性的定义. 依定义, 若 $f(x)$ 为单调递增函数, 则当 $x$ 增大时, $f(x)$ 也随之增大; 从函数图形来看, 从左往右看时, 图形是上升的. 这一定义表明, 当 $x$ 减小时, $f(x)$ 也随之减小, 即 $x$ 与 $f(x)$ 的\myemph{增减性相同}. 类似地, 若 $f(x)$ 为递减函数, 则 $x$ 与 $f(x)$ 的<strong>增减性相反</strong>. (单调性还有另一种表现形式, 见“2020 年 11 月 14 日答疑记录”的第二个例题及其后的补充说明.) 结合函数单调性和复合函数的定义, 可得\[\begin{aligned}
    f\nearrow,\ g\nearrow&\colon x\nearrow\xrightarrow{\ g\ } 
        g(x)\nearrow\xrightarrow{\ f\ } f(g(x))\nearrow,\\
    f\nearrow,\ g\searrow&\colon x\nearrow\xrightarrow{\ g\ } 
        g(x)\searrow\xrightarrow{\ f\ } f(g(x))\searrow,\\
    f\searrow,\ g\nearrow&\colon x\nearrow\xrightarrow{\ g\ } 
        g(x)\nearrow\xrightarrow{\ f\ } f(g(x))\searrow,\\
    f\searrow,\ g\searrow&\colon x\nearrow\xrightarrow{\ g\ } 
        g(x)\searrow\xrightarrow{\ f\ } f(g(x))\nearrow.
\end{aligned}\]
此即“同增异减”. 例如, 对函数 $y=\sqrt{x^2-2x-3}$, 其自然定义域为 $(-\infty,-1]\cup[3,+\infty)$, 而 $u=x^2-2x-3$ 分别在 $(-\infty,-1]$ 上单调递减, 在 $[3,+\infty)$ 上单调递增, 所以由 $y=\sqrt{u}$ 单调递增可知 $y=\sqrt{x^2-2x-3}$ 在 $(-\infty,-1]$ 上单调递减, 在 $[3,+\infty)$ 上单调递增.
</p>
<p>在求复合函数的值域和单调区间时, 通常需要结合函数图形, 即需要画对应图形的草图. 以下为了过程简便都省略了草图.
</p>
<p><myexample>
<p>求下列函数的定义域、值域和单调区间:
</p>
<p>(1) $y=\log_{\frac13} (-x^2-2x+8)$;\qquad
    (2) $y=\log_{\frac12}(x^2-2x-3)$;\qquad
    (3) $y=3^{|x|}$;
</p>
<p>(4) $y=\sqrt{4-x^2}$;\qquad 
    (5) $y=\dfrac1{x^2-3x}$, $x\in(0,2]$.
</p>
</myexample>
<mysolution>
    <p>(1) 由 $-x^2-2x+8> 0$ 知 $x\in(-4,2)$, 所以 $u= -x^2-2x+8\in (0,9]$. 由关于 $u$ 的函数 $y=\log_{\frac13} u$ 单调递减 (结合函数图形) 知, 
    \[y=\log_{\frac13} (-x^2-2x+8)= \log_{\frac13} u\in \biggl[\log_{\frac13} 9, +\infty\biggl)= [-2,+\infty).\]
</p>
<p>因为二次函数 $u= -x^2-2x+8$ 在 $(-4,-1)$ 上单调递增, 在 $[-1,2)$ 上单调递减, 所以 $y=\log_{\frac13} (-x^2-2x+8)$ 在 $(-4,-1)$ 上单调递减, 在 $[-1,2)$ 上单调递增.
</p>
<p>(2) 用与 (1) 中相同的方法可得, $x\in(-\infty,-1)\cup (3,+\infty)$, 
    \[x^2-2x-3\in (0,+\infty),\quad 
        y= \log_{\frac12}(x^2-2x-3)\in (-\infty,+\infty),\]
    且函数在 $(-\infty,-1)$ 上单调递增, 在 $(3,+\infty)$ 上单调递减.
</p>
<p>(3) 显然 $x\in\realnum$ (不用限制 $x$ 的取值范围). 由 $|x|$ 的图形 (参考“2020 年 9 月 26 日答疑记录”的第二部分) 可知, $u=|x|\in(0,+\infty)$ 且在 $(-\infty,0)$ 上单调递减, 在 $(0,+\infty)$ 上单调递增, 所以 $y=3^u\in(1,+\infty)$ 且 $y=3^{|x|}$ 在 $(-\infty,0)$ 上单调递减, 在 $(0,+\infty)$ 上单调递增.
</p>
<p>(4) 用知识点讲解中的方法可知, $y=\sqrt{4-x^2}$ 定义域为 $[-2,2]$, 值域为 $[0,2]$, 且在 $[-2,0]$ 上单调递减, 在 $(0,2]$ 上单调递增.
</p>
<p>(5) 因为 $x\in(0,2]$, 所以 $x^2-3x\in\biggl[-\dfrac94,0\biggr)$. 由 $f(x)=\dfrac1x$ 的图形可知, $y=\dfrac1{x^2-3x}\in\biggl(-\infty,-\dfrac49\biggr]$, 且在 $\biggl(0,\dfrac32\biggr)$ 上单调递增, 在 $\biggl[\dfrac32,2\biggr)$ 上单调递减.
</p>
</mysolution>

<myexample>
<p>求下列函数的定义域、值域和单调区间:
</p>
<p>(1) $y=\dfrac{\sqrt{x}-1}{\sqrt{x}+1}$;\qquad
    (2) $y=\dfrac{1-3^x}{1+3^x}$.
</p>
</myexample>
<mysolution>
    <p>(1) $x$ 需满足 $\sqrt{x}+1\neq 0$, 即 $x\in[0,+\infty)$. 先将函数用“分离常数法”变形,
    \[y=\frac{(\sqrt{x}+1)-2}{\sqrt{x}+1}
        = 1-\frac{2}{\sqrt{x}+1}.\]
    因为 $\sqrt{x}\in[0,+\infty)$, 所以 
    \[\begin{gathered}
        \sqrt{x}+1\in[1,+\infty),\quad 
            \frac2{\sqrt{x}+1}\in(0,2],\\
        -\frac2{\sqrt{x}+1}\in[-2,0),\quad
        1-\frac2{\sqrt{x}+1}\in[-1,1),
    \end{gathered}\]
    即 $y\in[-1,1)$, 且按上述过程可知函数在 $[0,+\infty)$ 上单调递增.
</p>
<p>(2) $1+3^x\neq0$ 即 $x\in\realnum$. 由 
    \[y= \frac{-(1+3^x)+2}{1+3^x}= -1+\frac2{1+3^x}\]
    并仿 (1) 的过程知 $y\in(-1,1]$, 且在 $\realnum$ 上单调递减.
</p>
</mysolution>
</p>
<p>分离常数法是对形如 $\dfrac{ax+b}{cx+d}$ 的式子变形的常用方法, 以下再举一些例子:
\[\begin{aligned}
    \frac{2x+1}{x+1}&= \frac{2(x+1)-1}{x+1}= 2-\frac1{x+1},\\
    \frac{x+2}{2x+1}&= \frac{\dfrac12(2x+1)+\dfrac32}{2x+1}= \frac12+\frac{\dfrac32}{2x+1},\\
    \frac{2x+1}{3x-1}&= \frac{\dfrac23(3x-1)+\dfrac53}{3x-1}= \frac23-\frac{\dfrac53}{x+1}.
\end{aligned}\]
除了可以用来求函数的值域, 该方法还可以用来画函数图形 (一般需要利用图形变换).
</p>
