---
# bookCollapseSection: true
title: 幂函数
weight: 1
bookHidden: true
prevPage: /docs/algebra/pow-exp-log
prevPageTitle: 幂函数、指数函数、对数函数
nextPage: /docs/algebra/pow-exp-log/exponent-function
nextPageTitle: 指数函数
---

# 幂函数


<myexercise>
    <p>在同一平面直角坐标系中, 作出函数 $f(x)=x^a$ ($x>0$), $g(x)=\log_a x$ 的图象.
    </p>
<myexercise>

<p>幂函数 $y= x^a$ (均取由 $a$ 对应的自然定义域) 的大致图形如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1110-crop}
    </center>
</p>
<p>为了整洁起见, 图中并未画出 $a=0$ (对应 $y=1$) 和 $a=1$ (对应 $y=x$) 的情形, 且对 $0< a< 1$ 只画了 $x>0$ 对应的图形. 由图可知, 幂函数 $y= x^a$ 的特征有
</p>
<p>(1) 当 $a< 0$ 且为整数时, 图形有两支, 且以 $x$ 轴和 $y$ 轴为渐近线, 函数分别在 $(-\infty,0)$ 和 $(0,+\infty)$ 上单调递减; 
</p>
<p>(2) 当 $a>0$ 时, 在第一象限内, 函数单调递增, 且 $a$ 越大, 函数值增加速度越快;
</p>
<p>(3) 恒过点 $(1,1)$ (因为 $1^a=1$).
</p>


<myexample>
<p>比大小: (1) $a=1$, $b=0.3^2$, $c=2^{0.3}$;
</p>
<p>(2) $a= 3^{1.2}$, $b=1.2^0$, $c= \biggl(\dfrac13\biggr)^{-0.9}$;
</p>
<p>(3) $a=1.7^{\frac35}$, $b=0.7^{-\frac35}$, $c=0.7^{\frac35}$;
</p>
<p>(4) $a=\sqrt[3]{3}$, $b=6^{\frac13}$, $c=2^{-\frac13}$.
</p>
</myexample>
<mysolution>
    <p>(1) 因为 $b=0.09< 1$, 由指数函数 $y=2^x$ (或幂函数 $y=x^{0.3}$) 的图形知 $c=2^{0.3}>1$, 所以 $b< a< c$.
</p>
<p>(2) 因为 $b=1=3^0$, $c= \biggl(\dfrac13\biggr)^{-0.9}= 3^{0.9}$, 所以由指数函数 $y=3^x$ 的图形知 $b< c< a$.
</p>
<p>(3) 因为 $b=0.7^{-\frac35}= \biggl(\dfrac1{0.7}\biggr)^{\frac35}$, 而 $1.7> \dfrac1{0.7}$ (为什么?), 所以由幂函数 $y= x^{\frac35}$ 的图形知, $c< b< a$.
</p>
<p>(4) 因为 $a=3^{\frac13}$, $b=6^{\frac13}$, $c=\biggl(\dfrac12\biggr)^{\frac13}$, 由幂函数 $y= x^{\frac13}$ 的图形知, $c< a< b$.
</p>
</mysolution>
</p>
<p>判断多个数的大小, 一般的方法是:
</p>
<p>(1) 先确定这些数与 $0$, $1$ 等数的大小, 将它们分类到 $(-\infty,0)$, $(0,1)$, $(1,+\infty)$ 等区间中;
</p>
<p>(2) 对各区间中的幂、指数或对数, 再化为同底数或同指数, 根据相应函数的单调性来判断大小.

<myexample>
<p>比较大小: $a=\sqrt2$, $b=\sqrt[3]3$, $c=\sqrt[4]4$, $d=\sqrt[5]5$.
</p>
</myexample>
<mysolution>
    <p>此题无法直接作差, 而是应考虑利用乘方去掉根号, 并两两比较. 先适当化简, 因为 
    \[\sqrt[4]4= (2^2)^{\frac14}= 2^{\frac12}= \sqrt2,\]
    所以 $a=c$. 而
    \[(\sqrt2)^6= 2^3= 8,\quad (\sqrt[3]3)^6= 3^2= 9,\]
    所以 $a< b$. 又因为
    \[(\sqrt2)^{10}= 2^5= 32,\quad (\sqrt[5]5)^{10}= 5^2= 25,\]
    所以 $a>d$. 综上所述, $d< a=c< b$.
</p>
</mysolution>
