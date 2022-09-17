---
# bookCollapseSection: true
title: 对数运算
weight: 3
bookHidden: true
prevPage: /docs/algebra/pow-exp-log/exponent-function
prevPageTitle: 指数函数
nextPage: /docs/algebra/pow-exp-log/logarithm-function
nextPageTitle: 对数函数
---

# 对数运算


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
<p>化简求值:  $\mathrm{e}^{-\ln 2}$, $\dfrac{\log_8 9}{\log_2 3}$.
</p>
</myexample>
<mysolution>
    <p>因为 $a^{\log_a b}= b$, 所以 ($\ln x$ 表示以 $\mathrm{e}$ 为底的自然对数)
    \[\mathrm{e}^{-\ln 2}= \mathrm{e}^{\ln \frac12}= \frac12.\]
    由换底公式,
    \[\frac{\log_8 9}{\log_2 3}
        = \frac{\ln 9}{\ln 8} \cdot \frac{\ln 3}{\ln 2}
        = \frac{2\ln 3}{3\ln 2} \cdot \frac{\ln 3}{\ln 2}
        = \frac23.\]
</p>
</mysolution>

<myexample>
<p>一个容器装有细沙 $a\,\text{cm}^3$, 细沙从容器底部一个细微的小孔慢慢地匀速漏出, $t\,\text{min}$ 后剩余的细沙量为 $y= a\mathrm{e}^{-bt}\,(\text{cm}^3)$, 经过 $8\,\text{min}$ 后发现容器内还有一半的沙子, 求需要再经过多少时间, 容器中的沙子只有开始时的八分之一.
</p>
</myexample>
<mysolution>
    <p>设经过 $t\,\text{min}$ 符合题意, 则由已知,
    \[\left\{\!\!\begin{array}{l}
        a\mathrm{e}^{-b\cdot 8}= \dfrac{a}2,\\[5pt]
        a\mathrm{e}^{-bt}= \dfrac{a}8,
        \end{array}\right.\ \text{即}
      \left\{\!\!\begin{array}{l}
        \mathrm{e}^{-8b}= \dfrac12,\\[3pt]
        \mathrm{e}^{-bt}= \dfrac18.
      \end{array}\right.\]
    因为 $\dfrac18= \biggl(\dfrac12\biggr)^3$, 所以
    \[\mathrm{e}^{-bt}= (\mathrm{e}^{-8b})^3= \mathrm{e}^{-24b},\]
    即 $-bt=-24b$, 解得 $t=24$. 这表明需要再经过 $(t-8)\,\text{min}= 16\,\text{min}$, 才能符合题意.
</p>
</mysolution>

<myexample>
<p>根据有关资料, 围棋状态空间复杂度的上限 $M$ 约为 $3^{361}$, 而可观测宇宙中普通物质的原子总数 $N$ 约为 $10^{80}$. 将 $\dfrac{M}{N}$ 表示为 $10$ 的正整数次方 ($\lg 3\approx 0.48$).
</p>
</myexample>
<mysolution>
    <p>根据对数的运算性质, 
    \[\begin{aligned}
        \lg \dfrac{M}{N}
        &= \lg M-\lg N= \lg 3^{361}- \lg 10^{80}
         = 361\lg 3- 80\\
        &\approx 361\cdot 0.48- 80
         = 93.28,
       \end{aligned}\]
    所以 $\dfrac{M}{N}\approx 10^{93}$.
</p>
</mysolution>

<myexample>
<p>设 $A=\{0,1,2\}$, $B= \{\log_m 1, \log_m 2, m\}$, 且 $A=B$, 求实数 $m$ 的值.
</p>
</myexample>
<mysolution>
    <p>由对数的定义, $B= \{0, \log_m 2, m\}$, 且 $m>0$ 且 $m\neq 1$, 所以由 $A=B$ 知只能 $m=2$. 此时 $\log_m 2=1$, 即 $B=\{0,1,2\}$, 符合题意.
</p>
</mysolution>
<myremark>
    <p>上题可以直接讨论 $m=0$, $1$ 或 $2$, 但是利用对数定义直接得到 $m=2$ 更方便. 另外, 集合问题一般需要回代求出的数值, 以检验其是否符合题意.
</p>
</myremark>

<myexample>
<p>(1) 化简: $3^{-\log_3 2}$, $\log_{\sqrt3} 81$;
</p>
<p>(2) 若 $a=\log_4 3$, 求 $2^a+2^{-a}$ 的值.
</p>
</myexample>
<mysolution>
    <p>(1) 前者直接用对数恒等式, 
    \[3^{-\log_3 2}= 3^{\log_3 \frac12}= \dfrac12.\]
    后者用对数定义 (因为 $3^4= 81$),
    \[\log_{\sqrt3} 81= \log_{\sqrt3} (\sqrt3)^8= 8,\]
    或者换底公式,
    \[\log_{\sqrt3} 81= \frac{\ln 81}{\ln\sqrt3}
        = \frac{4\ln 3}{\dfrac12\ln 3}= 8.\]
</p>
<p>(2) 因为 
    \[2^a= 2^{\log_4 3}= 4^{\frac12\log_4 3}
        = 4^{\log_4 \sqrt3}= \sqrt3,\]
    而 $2^{-a}= \dfrac1{2^a}= \dfrac{\sqrt3}3$, 所以
    \[2^a+2^{-a}= \sqrt3+ \dfrac{\sqrt3}3
        = \dfrac{4\sqrt3}3.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>若函数 $f(x)$ 满足 $f(2^x)= x$, 求 $f(4)$, $f(6)$ 的值.
</p>
</myexample>
<mysolution>
    <p>先求 $f(4)$ 的值. 此时 $2^x=4$, 解得 $x=2$, 所以 $f(4)=2$. 同理可求得 $f(6)= \log_2 6$.
</p>
</mysolution>
<myremark>
    <p>上例中可以求出 $f(x)= \log_2 x$. 更多的例子可参考“2020 年 10 月 21 日答疑记录”(尤其是第二部分).
</p>
</myremark>
</p>
<p><myexample>
<p>设 $a=\lg2$, $b= \lg3$, 用 $a$, $b$ 分别表示 $\lg 12$ 和 $\log_2 3$.
</p>
</myexample>
<mysolution>
    <p>分别用对数运算性质和和换底公式,
    \[\begin{aligned}
        \lg 12&= \lg(2^2\cdot 3)= 2\lg2+\lg3= 2a+b,\\
        \log_2 3&= \dfrac{\lg3}{\lg2}= \dfrac{b}{a}.
    \end{aligned}\]
</p>
</mysolution>
</p>
<p><myexample>
<p>化简: $(\lg2)^2+ \lg4\cdot\lg5+ (\lg5)^2$.
</p>
</myexample>
<mysolution>
    <p>因为 $\lg4= 2\lg2$, 利用完全平方公式,
    \[\begin{aligned}
        &(\lg2)^2+ \lg4\cdot\lg5+ (\lg5)^2\\
        ={}& (\lg2)^2+ 2\lg2\cdot\lg5+ (\lg5)^2\\
        ={}& (\lg2+\lg5)^2= 1.
    \end{aligned}\]
</p>
</mysolution>

<myexample>
<p>(1) 设 $a>0$, 求 $\lg a+\lg\dfrac1a$ 的值.
</p>
<p>(2) 设 $\log_3 2=b$, 用 $b$ 表示 $\log_3 8-\log_3 6$.
</p>
<p>(3) 设 $\log_2 c= m$, $\log_3 c= n$, 用 $m$, $n$ 表示 $\log_c 6$.
</p>
</myexample>
<mysolution>
    <p>(1) $\lg a+\lg\dfrac1a= \lg\biggl(a\cdot\dfrac1a\biggr)
    = \lg 1= 0$.
</p>
<p>(2) 由题意,
    \[\begin{aligned}
        \log_3 8-\log_3 6
        &= \log_3 \dfrac86= \log_3 \dfrac43
         = \log_3 4- \log_3 3\\
        &= 2\log_3 2- 1= 2a-1.
    \end{aligned}\]
</p>
<p>(3) 由换底公式,
    \[\log_2 c= m= \frac{\lg c}{\lg 2},\quad
      \log_3 c= n= \frac{\lg c}{\lg 3},\]
    则
    \[\frac{\lg 2}{\lg c}= \frac1m,\quad
      \frac{\lg 3}{\lg c}= \frac1n,\]
    所以
    \[\log_c 6= \frac{\lg6}{\lg c}= \frac{\lg2+\lg3}{\lg c}
        = \frac1m+ \frac1n.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>若函数 $f(x)= f\biggl(\dfrac1x\biggr)\cdot \lg x+ 1$, 求 $f(10)$ 的值.
</p>
</myexample>
<mysolution>
    <p>分别令 $x=10$, $\dfrac1{10}$, 可得
    \[\left\{\!\!\begin{array}{l}
        f(10)= f\biggl(\dfrac1{10}\biggr)\cdot \lg10+ 1,\\
        f\biggl(\dfrac1{10}\biggr)= f(10)\cdot \lg\frac1{10}+ 1, 
    \end{array}\right.\]
    即
    \[\left\{\!\!\begin{array}{l}
        f(10)= f\biggl(\dfrac1{10}\biggr)+ 1,\\
        f\biggl(\dfrac1{10}\biggr)= -f(10)+ 1.
    \end{array}\right.\]
    将后一式代入前一式, 可解得 $f(10)= 1$.
</p>
</mysolution>
<myremark>
    <p>上面的过程可一般化: 将式子中的 $x$ 换为 $\dfrac1x$, 并联立,
    \[\left\{\!\!\begin{array}{l}
        f(x)= f\biggl(\dfrac1x\biggr)\cdot \lg x+ 1,\\
        f\biggl(\dfrac1x\biggr)= -f(x)\cdot \lg x+ 1,
    \end{array}\right.\]
    其中用到了 $\lg\dfrac1x= -\lg x$. 仍用代入消元法可解得, 
    \[f(x)= \dfrac{\lg x+ 1}{1+(\lg x)^2}.\]
</p>
</myremark>

<myexample>
<p>一种放射性物质不断衰变为其他物质, 每经过一年, 该物质剩留的质量约是原来的 $75\%$. 估计经过多少年, 该物质的剩留量是原来的 $\dfrac13$? (结果保留 1 位有效数字, 参考数据: $\lg2\approx 0.3010$, $\lg3\approx 0. 4771$)
</p>
</myexample>
<mysolution>
    <p>设该物质初始质量为 $m$, 则经过 $t$ 年, 质量为 $m\cdot (75\%)^t$. 由题意, 
    \[m\cdot (75\%)^t= \frac13 m,\quad\text{解得}\quad
        t= \log_{75\%} \frac13,\]
    进一步有,
    \[\begin{aligned}
        t
        &= \frac{\lg \dfrac13}{\lg \dfrac34}
         = \frac{-\lg 3}{\lg3-2\lg2}\\
        &\approx \frac{-0.4771}{0.4771-2\times 0.3010}
        \approx 4,
    \end{aligned}\]
    故大约经过 $4$ 年符合题意.
</p>
</mysolution>

<myexample>
<p>某种病毒每经过 $30$ 分钟繁殖为原来数量的 $2$ 倍, 则 $1$ 个病毒经过 $5$ 小时能繁殖为多少个? 设该病毒原有 $a$ 个, 经过 $t$ 小时繁殖为 $y$ 个且 $y= a\mathrm{e}^{kt}$, 求常数 $k$ 的值.
</p>
</myexample>
<mysolution>
    <p>$5$ 小时共 $10$ 个 $30$ 分钟, 所以 $1$ 个病毒经过 $5$ 小时能繁殖为 $2^{10}= 1024$ 个.
</p>
<p>由题意, 当 $t$ 变为 $t+\dfrac12$ 时, $y$ 变为原来的 $2$ 倍, 所以
    \[a\mathrm{e}^{k(t+\frac12)}= 2\cdot a\mathrm{e}^{kt},\quad
        \text{解得}\quad k=2\ln 2.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>在不考虑空气阻力的情况下, 火箭的最大速度 $v\,\mathrm{m/s}$, 燃料的质量 $M\,\mathrm{kg}$ 和火箭 (除燃料外) 的质量 $m\,\mathrm{kg}$ 的函数关系式为 $v= 2000\ln\biggl(1+\dfrac{M}m\biggr)$. 当燃料质量是火箭质量的多少倍时, 火箭的最大速度可以达到 $12\,\mathrm{km/s}$?
</p>
</myexample>
<mysolution>
    <p>因为 $12\,\mathrm{km/s}= 12000\,\mathrm{m/s}$, 所以
    \[12000= 2000\ln\biggl(1+\dfrac{M}m\biggr),\quad
        \text{解得}\quad \frac{M}{m}= \mathrm{e}^6-1.\]
</p>
</mysolution>

<p>对数的主要运算法则如下 (以下均设底数 $a\in(0,1)\cup(1,+\infty)$, 真数 $x$, $y>0$):
\[\begin{gathered}
    a^x=y\Leftrightarrow x=\log_a y,\quad \text{由此可得}\ 
        a^{\log_a y}= y,\ x= \log_a a^x,\\
    \log_a x+ \log_a y= \log_a xy,\quad 
        \log_a x- \log_a y= \log_a \dfrac{x}y,\\
    \frac{\log_a x}{\log_a y}= \log_y x\ (\text{换底公式}),\quad
        \log_a x^\beta= \beta\log_a x\ (\beta\in\realnum). 
\end{gathered}\]
以上公式均可以逆用, 如 
\[\log_2 6= \log_2 2+\log_2 3= 1+\log_2 3.\]
此外还应注意恒等式 $\log_a a=1$ 和 $\log_a 1= 0$ (均由对数定义可得). 有两个取特殊底的对数是常用的: $\log_{10} x$ 记为 $\lg x$ (\myindex{常用对数}{常用对数}), $\log_{\mathrm{e}} x$ 记为 $\ln x$ (\myindex{自然对数}{自然对数}), 其中 $\mathrm{e}= 2.718\cdots$ 称为自然对数的底数.
</p>
<p><myexample>
<p>对数练习:
    \begin{fourcolpro}
        (1) $\lg 0.0001$; & (2) $\log_2 6- \log_2 3$;
            & (3) $\ln \sqrt{\mathrm{e}}$; 
            & (4) $\log_3 5-\log_3 15$;\\
        (5) $\lg\dfrac14- \lg25$; & (6) $\log_2(\log_2 16)$;
            & \multicolumn{2}{l}{(7) $(\log_4 3+ \log_8 3)
            (\log_3 2+\log_9 2)$.}
    \end{fourcolpro}
</p>
</myexample>
<mysolution>
    <p>(1) $\lg 0.0001= \lg 10^{-4}= -4$ (注意 $0.1=\dfrac1{10}= 10^{-1}$).
</p>
<p>(2) $\log_2 6- \log_2 3= \log_2 \dfrac63= \log_2 2= 1$.
</p>
<p>(3) $\ln \sqrt{\mathrm{e}}= \ln \mathrm{e}^{\frac12}= \dfrac12$. 
</p>
<p>(4) $\log_3 5-\log_3 15= \log_3 \dfrac{5}{15}= \log_3 \dfrac13= -1$.
</p>
<p>(5) $\lg\dfrac14- \lg25= \lg\dfrac1{100}= -2$.
</p>
<p>(6) $\log_2(\log_2 16)= \log_2 4= 2$.
</p>
<p>(7) 由换底公式 (不妨均化为自然对数),
    \[\begin{aligned}
           &(\log_4 3+ \log_8 3)(\log_3 2+\log_9 2)\\
        ={}& \biggl(\frac{\ln 3}{\ln 4}+ \frac{\ln 3}{\ln 8}\biggr)
            \biggl(\frac{\ln 2}{\ln 3}+ \frac{\ln 2}{\ln 9}\biggr)\\
        ={}& \biggl(\frac{\ln 3}{2\ln 2}+ \frac{\ln 3}{3\ln 2}\biggr)
            \biggl(\frac{\ln 2}{\ln 3}+ \frac{\ln 2}{2\ln 3}\biggr)\\
        ={}& \biggl(\frac12+\frac13\biggr)\frac{\ln 3}{\ln 2}
            \biggl(1+\frac12\biggr)\frac{\ln 2}{\ln 3}\\
        ={}& \frac56\cdot\frac32
            = \frac54.
    \end{aligned}\]
</p>
</mysolution>


<p>\begin{example}\label{exa:201201-2030}
    计算: $\log_4 3\cdot \log_9 2- \log_{\frac12} 32$.
</p>
</myexample>
<mysolution>
    <p>由对数的运算法则 (参考“2020 年 11 月 8 日答疑记录”对数练习小节), 
    \[\begin{aligned}
        \log_4 3\cdot \log_9 2- \log_{\frac12} 32
        &= \frac{\ln 3}{\ln 4}\cdot \frac{\ln 2}{\ln 9}
            - \frac{\ln 32}{\ln\dfrac12}\\
        &= \frac{\ln 3}{2\ln 2}\cdot \frac{\ln 2}{2\ln 3}
            - \frac{5\ln 2}{-\ln 2}\\
        &= \frac14+5= \frac{21}4.
    \end{aligned}\]
</p>
</mysolution>
</p>
<p>计算例 \ref{exa:201201-2020} 时, 其中的对数都化为以  $\mathrm{e}$ 为底, 也就是化为自然对数. 在计算时, 也可以都化为以 $10$ 为底, 即化为常用对数. 此外, 也可以由 $32= 2^5= \bigg(\dfrac12\biggr)^{-5}$ 知 $\log_{\frac12} 32= -5$.
</p>

<myexample>
<p>计算: (1) $\lg \sqrt[5]{100}$;\quad 
    (2) $\ln\sqrt[8]{\mathrm{e}}$;\quad
    (3) $9^{\log_3 4}$;\quad
    (4) $\log_9 27$;\quad (5) $\log_{\sqrt 6}36$.
</p>
</myexample>
<mysolution>
    <p>幂 (指数)、对数的运算法则见“2020 年 11 月 21 日答疑记录”的第二部分.
</p>
<p>(1) $\lg \sqrt[5]{100}= \lg 10^{\frac25}= \dfrac25$.\qquad
    (2) $\ln\sqrt[8]{\mathrm{e}}= \ln \mathrm{e}^{\frac18}= \dfrac18$.
</p>
<p>(3) $9^{\log_3 4}= \big(3^{\log_3 4}\bigr)^2= 4^2= 16$.\qquad
    (4) $\log_9 27= \dfrac{\ln 27}{\ln9}
        = \dfrac{3\ln3}{2\ln3}= \dfrac32$.
</p>
<p>(5) $\log_{\sqrt6}36= \dfrac{\ln 36}{\ln \sqrt6}
        = \dfrac{2\ln6}{\dfrac12\ln6}= 4$.
</p>
</mysolution>
