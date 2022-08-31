---
# bookCollapseSection: true
title: 对数函数
weight: 4
bookHidden: true
prevPage: /docs/algebra/pow-exp-log/logarithm-calculation
prevPageTitle: 对数运算
nextPage: /docs/algebra/pow-exp-log/composite-inverse
nextPageTitle: 复合函数与反函数
---

# 对数函数

<myexample>
<p>比较下列各组数的大小:
</p>
<p>(1) $a=\log_3 4$, $b= \cos 2$, $c= 2^{-\frac12}$;
</p>
<p>(2) $a= \log_5 2$, $b= \log_{0.5} 0.2$, $c= 0.5^{0.2}$.
</p>
</myexample>
<mysolution>
    <p>比较指数式、对数式的大小, 通常先利用对应函数单调性估值, 然后对范围相近的数, 利用同底函数单调性比大小. 对三角函数式, 也可采用类似的方法.
</p>
<p>(1) 分别考虑函数 $f(x)= \log_3 x$, $g(x)= \cos x$, $h(x)= 2^x$ 的图形可知, 
    \[\begin{gathered}
        a= f(4)\in [f(3),+\infty)= [\log_3 3,+\infty)= [1,+\infty),\\
        b= g(2)\in \biggl[g(\pi),g\biggl(\frac\pi2\biggr)\biggr]= \biggl[\cos\pi,\cos\frac\pi2\biggr]= [-1,0],\\
        c= h\biggl(-\frac12\biggl)\in (0,h(0)]= (0, 2^0]= (0,1],
    \end{gathered}\]
    所以 $b< c< a$.    
</p>
<p>(2) 分别考虑函数 $f(x)= \log_5 x$, $g(x)= \log_{0.5} x$, $h(x)= 0.5^x$ 的图形可知, 
    \[\begin{gathered}
        a= f(2)\in [f(1),f(5)]= [\log_5 1,\log_5 5]= [0,1],\\
        b= g(0.2)\in [g(0.5),+\infty)= [\log_{0.5} 0.5,+\infty)= [1,+\infty),\\
        c= h(0.2)\in (0,h(0)]= (0, 0.5^0]= (0,1].
    \end{gathered}\]
    可以看到, 上述估值比较粗糙, 以至于 $a$, $c$ 的取值范围重叠了. 但两者无法化同底 (必须同为指数式或对数式才能化同底), 所以需要更细致的估值. 进一步细化可知 (顺带也可算出 $b$ 的更精确的取值范围),
    \[\begin{gathered}
        a= f(2)\in [f(1),f(\sqrt{5})]= [\log_5 1,\log_5 \sqrt{5}]= \biggl[0,\frac12\biggr],\\
        b= g(0.2)\in [g(0.25),g(0.125)]= \biggl[\log_{\frac12} \frac14,\log_{\frac12} \frac18\biggr]= [2,3],\\
        c= h(0.2)\in [h(1),h(0)]= [0.5^1, 0.5^0]= [0.5,1],
    \end{gathered}\]
    由此可得, $a< c< b$.
</p>
</mysolution>

<myexample>
<p>比较大小: $a=\log_2 3$, $b= \log_4 5$, $c= \log_8 7$.
</p>
</myexample>
<mysolution>
    <p>先估值, 确定各数的大致取值范围; 若取值范围重叠, 则化同底或细化取值范围 (参考“2021 年 1 月 29 日答疑记录”第一个例题).
</p>
<p>考虑函数 $f(x)=\log_2 x$, $g(x)= \log_4 x$, $h(x)= \log_8 x$ 的图形可知,
    \[\begin{gathered}
        a= f(3)\in [f(2),f(4)]= [\log_2 2, \log_2 4]= [1,2],\\
        b= g(5)\in [g(4),g(16)]= [\log_4 4, \log_4 16]= [1,2],\\
        c= h(7)\in [h(1),h(8)]= [\log_8 1, \log_8 8]= [0,1],
    \end{gathered}\]
    由此看出, $a$, $b$ 的取值范围重叠了, 需额外处理.
</p>
<p>方法一 (化同底): 利用换底公式, 
    \[\begin{aligned}
        a-b&= \frac{\ln 3}{\ln 2}- \frac{\ln 5}{\ln 4}
        = \frac{\ln 3}{\ln 2}- \frac{\ln 5}{2\ln 2}\\
        &= \frac{2\ln 3-\ln 5}{2\ln 2}
        = \frac{\ln 9-\ln 5}{2\ln 2}>0,
    \end{aligned}\]
    所以 $a>b>c$. 也可以都化成以 $10$ 为底, 计算过程类似. 若化成以 $2$ 为底, 则
    \[b= \frac{\log_2 5}{\log_2 4}= \frac{\log_2 5}{2}
        = \log_2 \sqrt5,\]
    同样可以得到 $a>b$ (因为 $3>\sqrt{5}$).
</p>
<p>方法二 (细化范围): 与区间 $[1,2]$ 的中点 $\dfrac32$ 比较, 可知
    \[\begin{gathered}
        a= f(3)\in [f(2\sqrt2),f(4)]= [\log_2 2\sqrt2, \log_2 4]= \biggl[\frac32,2\biggr],\\
        b= g(5)\in [g(4),g(8)]= [\log_4 4, \log_4 8]= \biggl[1,\frac32\biggr],
    \end{gathered}\]
    所以 $a>b>c$.
</p>
</mysolution>
<myremark>
    <p>类似地, 可估值
    \[\log_2 13\in[3,4],\quad \log_3 10\in [2,3],\quad 
        \log_4 65\in [3,4],\]
    更准确地 (为什么?),
    \[\log_2 13\in[3.5,4],\quad \log_3 10\in [2,2.5],\quad 
        \log_4 65\in [3,3.5].\]
</p>
</myremark>

<myexample>
<p>牛顿提出的物体在常温环境下温度 (单位: ${}^\circ\mathrm{C}$) 随时间 (单位: 分) 的变化规律为: 如果物体的初始温度是 $\theta_1$, 环境温度是 $\theta_0$, 则经过时间 $t$ 后物体的温度 $\theta$ 满足
    \[\theta= \theta_0+ (\theta_1-\theta_0)\mathrm{e}^{-kt},\]
    其中 $k$ 为正的常数. 已知由实验测得一杯初始温度为 $98^\circ\mathrm{C}$ 的液体在 $19^\circ\mathrm{C}$ 室温中, 温度变化如下:
</p>
<p><center>
        从 $98^\circ\mathrm{C}$ 下降到 $90^\circ\mathrm{C}$ 所用时间为 1 分 58 秒;\\
        从 $98^\circ\mathrm{C}$ 下降到 $85^\circ\mathrm{C}$ 所用时间为 3 分 24 秒;\\
        从 $98^\circ\mathrm{C}$ 下降到 $90^\circ\mathrm{C}$ 所用时间为 4 分 57 秒.
    </center>
</p>
<p>(1) 依照牛顿提出的温度变化规律, 写出该液体温度与时间的函数关系, 并选取一组数据求出相应的 $k$ 值 (精确到 $0.01$).
</p>
<p>(2) 在前述条件下, 该液体从 $98^\circ\mathrm{C}$ 冷却到 $75^\circ\mathrm{C}$ 大约需要多少时间 (精确到分)?
</p>
<p>(参考数据: $\ln 79\approx 4.369$, $\ln 71\approx 4.263$, $\ln 66\approx 4.190$, $\ln 61\approx 4.111$, $\ln 56\approx 4.025$)
</p>
</myexample>
<mysolution>
    <p>(1) 由已知, 
    \[\theta= 19+ (98-19)\mathrm{e}^{-kt}
        = 19+ 79\mathrm{e}^{-kt}.\]
    不妨选第一组数据, 因为 1 分 58 秒是 $\dfrac{59}{30}$ 分, 所以
    \[90= 19+ 79\mathrm{e}^{-k\cdot \frac{59}{30}},\]
    解得
    \[k= -\frac{30}{59}\ln\frac{71}{79}
        = \frac{30}{59}(\ln 79- \ln71).\]
    将 $\ln 79\approx 4.369$, $\ln 71\approx 4.263$ 代入,
    \[k\approx \frac{30}{59}(4.369- 4.263)
        \approx 0.05.\]
</p>
<p>(2) 由 (1), 
    \[\theta\approx 19+ 79\mathrm{e}^{-0.05t}.\]
    将 $\theta= 75$ 代入,
    \[75\approx 19+ 79\mathrm{e}^{-0.05t},\]
    解得
    \[t\approx -20\ln\frac{56}{79}
        = 20(\ln 79- \ln56).\]
    将 $\ln 79\approx 4.369$, $\ln 56\approx 4.025$ 代入,
    \[t\approx 20(4.369- 4.025)= 6.88.\]
    故大约需要 7 分钟.
</p>
</mysolution>

<myexample>
<p>比较下列各组数的大小: 
</p>
<p>(1) $a=\log_3 7$, $b= 2^{1.1}$, $c= 0.8^{3.1}$;
</p>
<p>(2) $a=\log_3 \pi$, $b= \log_\pi 3$, $c= \log_\pi 0.3$;
</p>
</myexample>
<mysolution>
    <p>此题仍应先估值, 而且需尽量准确. 
</p>
<p>(1) 分别考虑对应函数的图形单调性可知,
    \[\begin{gathered}
        a= \log_3 7\in [\log_3 3, \log_3 9]= [1,2],\\
        b= 2^{1.1}\in [2^1,2^2]= [2,4],\\
        c= 0.8^{3.1}\in [0.8^4,0.8^3]\in [0,1],
    \end{gathered}\]
    所以 $c< a< b$.
</p>
<p>(2) 分别考虑对应函数的图形单调性可知,
    \[\begin{gathered}
        a= \log_3 \pi\in [\log_3 3, \log_3 9]= [1,2],\\
        b= \log_\pi 3\in [\log_\pi 1,\log_\pi \pi]= [0,1],\\
        c= \log_\pi 0.3\in (-\infty,\log_\pi 1]\in (-\infty,0],
    \end{gathered}\]
    所以 $c< b< a$.
</p>
</mysolution>
</p>
<p><myexample>
<p>解不等式 $\log_a \dfrac25< 1$.
</p>
</myexample>
<mysolution>
    <p>不等式化为 $\log_a \dfrac25< \log_a a$. 考虑函数 $f(x)= \log_a x$ 的单调性和定义域可知:
</p>
<p>(1) 若 $0< a< 1$, 则 $\dfrac25> a>0$;
</p>
<p>(2) 若 $a>1$, 则 $\dfrac25< a$, 即有 $1< a$ (需与前提取交集).
</p>
<p>综上所述, $a\in\biggl(0,\dfrac25\biggl)\cup (1,+\infty)$.
</p>
</mysolution>

<myexample>
<p>设函数 $f(x)= \log_{\frac12} x$, 求下列命题中真命题的个数:
</p>
<p>(1) 函数 $f(|x|)$ 为偶函数.
</p>
<p>(2) 若 $f(a)= |f(b)|$, 其中 $a$, $b>0$ 且 $a\neq b$, 则 $ab=1$.
</p>
<p>(3) 函数 $f(-x^2+2x)$ 在 $(1,3)$ 上为单调递增函数.
</p>
<p>(4) 若 $0< a< 1$, 则 $|f(1+a)|< |f(1-a)|$.   
</p>
</myexample>
<mysolution>
    <p>(1) 设 $g(x)=f(|x|)$, 则 
    \[g(-x)= f(|-x|)= f(|x|)= g(x),\]
    所以函数 $f(|x|)$ 为偶函数 (此结论无需考虑 $f(x)$ 的具体表达式).
</p>
<p>(2) $f(x)= |f(b)|$ 化为 $\log_{\frac12} a= |\log_{\frac12} b|$, 由此可知 $\log_{\frac12} a\geqslant 0$, 即 $a\in(0,1]$. 若 $b\in(0,1]$, 则 $\log_{\frac12} a= \log_{\frac12} b$, 必有 $a=b$, 与已知矛盾. 若 $b\in(1,+\infty)$, 则 
    \[\log_{\frac12} a= -\log_{\frac12} b,\quad\text{即}\quad
        \log_{\frac12} ab=0,\]
    所以 $ab=1$.
</p>
<p>(3) 函数 $f(-x^2+2x)= \log_{\frac12}(-x^2+2x)$, 定义域为 $(0,2)$, 所以在 $(1,3)$ 并非处处有定义, 无法判断定义域. (如果只考虑 $x\in(1,2)$, 则可由复合函数的单调性知, 函数 $f(-x^2+2x)$ 为单调递增函数.)
</p>
<p>(4) 方法一: 因为 $0< a< 1$, 所以 $1-a\in(0,1)$, $1+a\in(1,2)$,
    \[\begin{aligned}
        |f(1+a)|- |f(1-a)|
        &= |\log_{\frac12} (1+a)|- |\log_{\frac12} (1-a)|\\
        &= -\log_{\frac12} (1+a)- \log_{\frac12} (1-a)\\
        &= -\log_{\frac12} (1-a^2)< 0,
    \end{aligned}\] 
    即 $|f(1+a)|- |f(1-a)|< 0$, 因此 $|f(1+a)|< |f(1-a)|$.
</p>
<p>方法二: 直接画函数 $h(x)= |\log_{\frac12} x|$ 的图形, 并由图形单调性可知,
    \[|f(1+a)|< |f(1-a)|.\]
</p>
<p><center>
        \includegraphics[scale=1]{2020-1223-1940-crop}
    </center>
</p>
<p>综上所述, (1)(2)(4) 是真命题, 共 $3$ 个.
</p>
</mysolution>

<myexample>
<p>已知 $\log_a \dfrac23< 1$, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>不等式化为 $\log_a \dfrac23< \log_a a$.
</p>
<p>(1) 若 $a\in(0,1)$, 由 $\log_a x$ 单调递减可知, $a< \dfrac23$, 所以 $a\in\biggl(0,\dfrac23\biggr)$.
</p>
<p>(2) 若 $a\in(1,+\infty)$, 由 $\log_a x$ 单调递增可知, $a>\dfrac23$, 所以 $a\in(1,+\infty)$.
</p>
<p>综上所述, $a\in\biggl(0,\dfrac23\biggr)\cup(1,+\infty)$.
</p>
</mysolution>

<myexample>
<p>“$\ln a>\ln b$”是“$3^a>3^b$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>有 $y=\ln x$ 的定义域为 $(0,+\infty)$ 且单调递增, 可知 $\ln a>\ln b$ 表明 $a>b>0$. 再由 $y=3^x$ 的定义域为 $\realnum$ 且单调递增, 可知 $3^a>3^b$ 表明 $a>b$. 因此“$\ln a>\ln b$”是“$3^a>3^b$”的必要不充分条件.
</p>
</mysolution>

<myexample>
<p>解不等式 $\log_{(1+k)} (1-k)< 1$.
</p>
</myexample>
<mysolution>
    <p>不等式化为 $\log_{(1+k)} (1-k)< \log_{(1+k)} (1+k)$. 考虑函数 $f(x)= \log_{(1+k)} x$ 的定义域和单调性可知,
</p>
<p>(1) 若 $0< 1+k< 1$, 则 $1-k> 1+k>0$, 解得 $-1< k< 0$ (注意和前提取交集);
</p>
<p>(2) 若 $1+k>1$, 则 $0< 1-k< 1+k$, 解得 $0< k< 1$.
</p>
<p>综上所述, $k\in(-1,0)\cup (0,1)$.
</p>
</mysolution>

<myexample>
<p>求函数 $y=\sqrt{\log_{\frac12} (x-1)}$ 的定义域.
</p>
</myexample>
<mysolution>
    <p>由题意,
    \[\left\{\!\!\begin{array}{l}
        \log_{\frac12} (x-1)\geqslant 0,\\
        x-1>0,
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        x\leqslant 2,\\
        x>1,
    \end{array}\right.\]
    所以 $x\in(1,2]$.
</p>
</mysolution>

<myexample>
<p>科学研究表明, 我们对声音的感觉与它的强度有关. 声音的强度用 $I$ (单位: 瓦/平方米) 表示, 但在实际测量时, 常用声音强弱的等级 $L$ (单位: 分贝) 来表示，它们满足关系 
    \[L= a\lg\dfrac{I}{I_0}\quad (a\ \text{是常数}),\]
    其中 $I_0= 1\times 10^{-12}$ 瓦/平方米, 这是人们通常能听到的声音的最小强度, 是听觉的开端. 例如, 冰箱运行时声音的强度是 $1\times 10^{-8}$ 瓦/平方米, 它的强弱等级是 $40$ 分贝.
</p>
<p>(1) 求 $a$ 的值;\quad (2) 求下列表格中 $m$, $n$ 的值:
</p>
<p><center>
        \begin{tabular}{|c|c|c|c|}
        \hline
            \multirow{2}{*}{声音的大小}& \multicolumn{3}{c|}{声音的来源}\\
        \cline{2-4}
            & 风吹落叶沙沙声 & 轻声耳语 & 嘈杂的马路\\
        \hline
            强度 $I$ (瓦/平方米) & $1\times 10^{-11}$
                & $1\times 10^{-10}$ & $m$ \\
        \hline
            强弱等级 $L$ (分贝) & $10$ & $n$ & $90$\\
        \hline
        \end{tabular}
    </center>
</p>
<p>(3) 为了保证休息和睡眠, 环境声音的强弱等级不宜超过 $50$ 分贝, 试求此时声音强度 $I$ 的范围.
</p>
</myexample>
<mysolution>
    <p>(1) 将冰箱运行时声音的强度信息代入已知等式,
    \[40= a\lg\frac{10^{-8}}{10^{-12}},\quad\text{解得}\quad
        a= 10.\]
</p>
<p>(2) 将轻声细语的强度信息代入已知等式,
    \[n= 10\lg\frac{10^{-10}}{10^{-12}}
        = 10\lg10^{4}= 10\cdot 4=  40.\]
    将嘈杂的马路的声音强度信息代入已知等式,
    \[90= 10\lg\frac{m}{10^{-12}},\quad\text{解得}\quad
        m= 10^{-3}.\]
</p>
<p>(3) 由题意,
    \[10\lg\frac{I}{10^{-12}}\leqslant 5,\quad\text{解得}\quad
        I\leqslant 10^{-7}.\]
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)=\log_a(2x-1)+1$ ($a>0$ 且 $a\neq 1$) 的图形过定点 $A$, 而点 $A$ 也在函数 $g(x)= 2^x+b$ 的图形上, 求 $g(\log_2 3)$ 的值.
</p>
</myexample>
<mysolution>
    <p>图形过定点问题应先考虑如何消去参数 (题中的 $a$) 的影响. 因为不论 $a$ 为何值, 总有 $\log_a 1= 0$, 所以定点 $A$ 的坐标为 $(1,1)$. 再代入函数 $g(x)= 2^x+b$ 知, 
    \[1=2^1+b,\quad\text{解得}\quad b=-1.\]
    因此
    \[g(\log_2 3)= 2^{\log_2 3}-1= 3-1= 2.\]
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= |\lg x|$, $f(a)=f(b)$ 且 $a< b$, 解不等式 $\log_a x+\log_b(2x-1)>0$.
</p>
</myexample>
<mysolution>
    <p>由函数 $f(x)= |\lg x|$ 的图形可知, $0< a< 1< b$, 所以 $f(a)=f(b)$ 化为 
    \[\begin{gathered}
      |\lg a|= |\lg b|,\quad -\lg a= \lg b,\\
      \lg ab=0,\quad ab=1,\quad\text{即}\quad b=\frac1a.
      \end{gathered}\]
    所以 
    \[\log_b(2x-1)= \frac{\log_a (2x-1)}{\log_a b}= -\log_a (2x-1),\]
    原不等式化为
    \[\log_a x- \log_a(2x-1)>0,\quad \log_a x>\log_a(2x-1),\]
    即 $x>2x-1>0$, 解得 $x\in\biggl(\dfrac12,1\biggr)$.
</p>
</mysolution>

<myexample>
<p>若函数 $y=\log_a x$ ($a>0$ 且 $a\neq 1$) 的图形过点 $(3,1)$, 求 $\log_2 3 \cdot f(8)$ 的值.
</p>
</myexample>
<mysolution>
    <p>将 $(3,1)$ 代入 $y=\log_a x$ 得 $1= \log_a 3$, 所以 $a=3$,
    \[\log_2 3 \cdot f(8)= \log_2 3\cdot \log_3 8
        = \frac{\ln 3}{\ln 2}\cdot\frac{\ln 8}{\ln 3}
        = \frac{3\ln 2}{\ln 2}= 3.\]
</p>
</mysolution>

<myexample>
<p>设 $a= 2^{-\frac13}$, $b=\log_2\dfrac13$, $c= \log_{\frac12}\dfrac13$, 比较这三者的大小.
</p>
</myexample>
<mysolution>
    <p>分别考虑函数 $f(x)= 2^x$, $g(x)= \log_2 x$, $h(x)= \log_{\frac12} x$ 的单调性, 可知 
    \[\begin{gathered}
        a= f\biggl(-\dfrac13\biggr)\in (0,1),\quad 
        b= g\biggl(\dfrac13\biggr)\in (-\infty,0),\\
        c= h\biggl(\dfrac13\biggr)\in (1,+\infty),
    \end{gathered}\]
    所以 $b< a< c$.
</p>
</mysolution>
</p>
<p>上述两个例题中的解法是对数、指数式比较大小时常用的方法, 分别为“化同底”和“先与 $0$, $1$ 比”.

<p>对数函数 $y= \log_a x$ ($x$, $a>0$ 且 $a\neq 1$) 的大致图形如下:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1050-crop}\qquad
        \includegraphics[scale=1]{2020-1206-1100-crop}
    </center>
</p>
<p>由图可知, 对数函数 $y= \log_a x$ 的特征有
</p>
<p>(1) 当 $0< a< 1$ 时, 函数单调递减; 当 $a>1$ 时, 函数单调递增;
</p>
<p>(2) 恒过点 $(1,0)$ (因为 $\log_a 1=0$), 且以 $y$ 轴为渐近线.
</p>
<p><myremark>
    <p>(1) 指数函数 $y= a^x$ 的定义域为 $\realnum$, 即对 $x$ 没有限制, 而对数函数 $y= \log_a x$ 的自然定义域是 $(0,+\infty)$.
</p>
<p>(2) 幂函数 $y= x^a$ 中自变量 $x$ 为底数, 指数函数 $y= a^x$ 中自变量 $x$ 为指数. 
</p>
</myremark>

\begin{example}\label{exa:201209-1910}
    已知 $0< a< 1$, $\log_a m< \log_a n< 0$, 比较 $m$, $n$ 与 $1$ 的大小.
</p>
</myexample>
<mysolution>
    <p>由 $0=\log_a 1$ 知不等式化为 $\log_a m< \log_a n< \log_a 1$. 因为 $0< a< 1$, 所以对数函数 $f(x)= \log_a x$ 在 $(0,+\infty)$ 上单调递减, 则 $m>n>1$.
</p>
</mysolution>
<myremark>
    <p>若例 \ref{exa:201209-1910} 中的不等式“$\log_a m< \log_a n< 0$”改为“$\log_a m> \log_a n> 0$”, 则答案建议写为: $0< m< n< 1$ (即对数函数中的真数一定为正数).
</p>
</myremark>
</p>
<p><myexample>
<p>(1) 已知 $a$, $b\in\realnum$, 则“$a< b$”是“$\log_2 a< \log_2 b$”的什么条件?
</p>
<p>(2) 已知 $x\in\realnum$, 则“$x< 0$”是“$\ln(x+1)< 0$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>(1) 由例 \ref{exa:201209-1910} 的解答及注可知, $\log_2 a< \log_2 b$ 等价于 $0< a< b$, 所以“$a< b$”是“$\log_2 a< \log_2 b$”的必要不充分条件.
</p>
<p>(2) $\ln(x+1)< 0$ 等价于 $0< x+1< 1$ 即 $-1< x< 0$, 所以“$x< 0$”也是“$\ln(x+1)< 0$”的必要不充分条件
</p>
</mysolution>

<p>关于比较多个数的大小的一般方法, 可参考“2020 年 11 月 21 日答疑记录”末尾的说明.
</p>
<p><myexample>
<p>比大小: (1) $a=0.4^2$, $b=3^{0.4}$, $c=\log_4 0.3$;
</p>
<p>(2) $a=2^{1.2}$, $b=\biggl(\dfrac12\biggr)^{-0.8}$, $c=2\log_4 2$;
</p>
<p>(3) $a=\log_3 \mathrm{e}$, $b=\ln 3$, $c=\log_3 2$.
</p>
</myexample>
<mysolution>
    <p>(1) 分别考查函数 $f(x)=0.4^x$, $g(x)=3^x$, $h(x)=\log_4 x$ 的图形可知, $a=f(2)\in(0,1)$ (实际上 $a=0.16$), $b=g(0.4)\in(1,3)$, $c=h(0.3)\in(-\infty,0)$, 所以 $c< a< b$.
</p>
<p>(2) 分别考查函数 $f(x)=2^x$, $g(x)= \log_5 x$ 的图形可知, $a=f(1.2)\in(2,4)$, $b=2^{0.8}=f(0.8)\in(1,2)$, $c=\log_5 4=g(4)\in(0,1)$, 所以 $c< b< a$.
</p>
<p>(3) 分别考查函数 $f(x)=\log_3 x$, $g(x)=\ln x$ 的图形可知, $a=f(\mathrm{e})\in(0,1)$ (注意 $\mathrm{e}=2.718\cdots$), $b=g(3)\in(1,2)$ ($\ln x$ 的底数是 $\mathrm{e}$), $c=f(2)\in(0,1)$, 而 $f(2)< f(\mathrm{e})$, 所以 $c< a< b$.
</p>
</mysolution>

