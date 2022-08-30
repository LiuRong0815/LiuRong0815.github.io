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
