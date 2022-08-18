\sectioncounter{27}
</p>

<p>
\section{等差数列}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
若数列 $\{a_n\}$ 相邻两项中, 后一项减前一项为定值 $d$, 即 $a_{n+1}-a_n=d$, 则称 $\{a_n\}$ 为等差数列, $d$ 为公差 (difference). 由定义可知递推式 $a_{n+1}=a_n+d$, 再用累加法可得通项公式 $a_n=a_1+(n-1)d$. 由此可知, $a_n$ 由 $a_1$,$d$,$n$ 共同决定. 注意, 等差数列的通项公式 $a_n$ 是项数 $n$ 的一次式 (反之如何?). 逆用通项公式可得求项数公式
\[n=\frac{a_n-a_1}d+1.\]
例如, 对等差数列 $3$, $5$, $7$, $9$, $\cdots$ 而言, $101$ 对应的项数为
\[\frac{101-3}2+1= 50.\]
</p>

<p>
直接由通项公式可验证 $a_n-a_m=(n-m)d$, 即 
\[a_n=a_m+(n-m)d.\]
注意公式中 $m$, $n$ 无大小之分, 如
\[a_7= a_4+3d,\quad a_6= a_9-3d.\]
还可得通项公式可以从任意项开始计算, 如
\[a_n= a_5+(n-5)d.\]
\mymarginpar{类似地, 若 $d\neq 0$, 则
\[\begin{aligned}
    & l+m+n= p+q+r\\
    \Leftrightarrow &a_l+a_m+a_n= a_p+a_q+a_r.
\end{aligned}\]
但是一般来说,
\[\begin{aligned}
    & m+n= p+q+r\\
    \nLeftrightarrow &a_m+a_n= a_p+a_q+a_r.
\end{aligned}\]}若 $m+n=p+q$, 则可由通项公式验证 $a_m+a_n=a_p+a_q$. 若 $d\neq 0$, 则反之亦然. 特别地, 
\[2m=p+q \Leftrightarrow 2a_m=a_p+a_q.\]
称 $a$, $b$, $c$ 成等差数列是指 $b-a=c-b$, 也就是 $2b=a+c$,
此时称 $b$ 为 $a$, $c$ 的等差中项.
</p>

<p>
由倒序相加法可知等差数列 $\{a_n\}$ 的前 $n$ 项和公式, 即把
\[\begin{aligned}
    S_n&= a_1+a_2+\cdots+a_{n-1}+a_n,\\
    S_n&= a_n+a_{n-1}+\cdots+a_2+a_1
\end{aligned}\]
相加可得
\[2S_n= n(a_1+a_n),\ \text{即\ } S_n=\frac{(a_1+a_n)n}2.\]
此公式的推导和形式同梯形面积公式, 可类比记忆. 注意, 等差数列的前 $n$ 项和 $S_n$ 是项数 $n$ 的二次式 (反之如何?).
</p>

<p>
\lianxi
<myexercise>
    <p>    在等差数列 $\{a_n\}$ 中, 若 $a_3=-1$, $d=2$, 求 $a_8$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_8= a_3+5d= 9$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\{a_n\}$ 是公差为 $d$ 的等差数列, 验证数列 $\{a_{2n}\}$ 为等差数列.
</p>
</myexercise>
<mysolution>
    <p>
    数列 $\{a_{2n}\}$ 的第 $n$ 项为 $a_{2n}$, 第 $n+1$ 项为 $a_{2(n+1)}= a_{2n+2}$, 后者减前者, 得常数 $2d$, 所以 $\{a_n\}$ 是公差为 $2d$ 的等差数列.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在等差数列 $\{a_n\}$ 中, 若 $a_4=10$, $a_{10}=4$, 求 $a_7$.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: $a_{10}- a_{4}= 6d= -6$, 则 $d=-1$, $a_7= a_4+3d= 7$.
</p>

<p>
    \mymarginpar{方法一是通用解法, 方法二利用特殊的下标关系.}
    方法二: $a_4+a_{10}= 2a_7$, 则 $a_7= 7$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    等差数列 $\{a_n\}$ 前 $n$ 项和为 $S_n$, 若 $a_5=8$, 求 $S_9$.
</p>
</myexercise>
<mysolution>
    <p>
    $S_9= \dfrac{(a_1+a_9)\cdot 9}2
    = \dfrac{2a_5\cdot 9}2= 9a_5= 72$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$ 公差为 $d$, $a_1=10$, 且 $a_1$, $2a_2+2$, $5a_3$ 成等比数列, 求 $a_n$.
</p>
</myexercise>
<mysolution>
    <p>
    $(2a_2+2)^2= a_1\cdot 5a_3$, 即
    \[[2(10+d)+2]^2= 10\cdot 5(10+2d),\]
    \mymarginpar{等比数列中不含 $0$, 所以需要检验.}
    解得 $d= -1$ 或 $4$, 经检验, 均合题意. 所以 $a_n= 11-n$ 或 $6+4n$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{等差数列的基本量运算}
<span id="example-"></span>
<myexample>
    <p>
    已知等差数列 $\{a_n\}$ 中, $a_1=1$, $a_3=-3$.
</p>

<p>
    (1) 求 $a_n$;\qquad
    (2) 若其前 $k$ 项和 $S_k=-35$, 求 $k$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    (1) $a_3- a_1= 2d$, 则 $d=-2$, $a_n= 3-2n$.
</p>

<p>
    (2) 由等差数列求和公式, 
    \[S_k= \frac{(a_1+a_k)k}2
        = \frac{(1+3-2k)k}2= -35,\]
    解得 $k=-5$ (舍) 或 $7$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知等差数列 $\{a_n\}$ 中的前三项和为 $12$, 且 $2a_1$, $a_2$, $a_3+1$ 成等比数列, 求数列 $\{a_n\}$ 的公差 $d$.
</p>
</myexample>
<mysolution>
    <p>
    由题意, $a_1+a_2+a_3= 12$, 即 $3a_2= 12$, $a_2= 4$. 而 $a_2^2= 2a_1(a_3+1)$, 即
    \[4^2= 2(4-d)(5+d),\quad d=3,-4.\]
    经检验, 均合题意.
</p>
</mysolution>
</p>

<p>
\lianxi
</p>

<p>
<myexercise>
    <p>    若等差数列 $\{a_n\}$ 中, $a_3=10$, 且 $a_3$, $a_7$, $a_{10}$ 成等比数列, 求公差 $d$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_7^2= a_3a_{10}$, 即
    \[(10+4d)^2= 10(10+7d),\quad d= -\frac58.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知等差数列 $\{a_n\}$ 中, $a_2=6$, $a_5=15$, 若 $b_n=a_{2n}$, 求 $b_5$.
</p>
</myexercise>
<mysolution>
    <p>
    设 $\{a_n\}$ 的公差为 $d$, 则 $a_5-a_2= 3d$, $d=3$, 
    \[b_5= a_{10}= a_5+5d= 30.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{等差数列的求和问题}
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    设等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$.
</p>

<p>
    (1) 若 $a_2=1$, $a_4=5$, 求 $S_5$;
</p>

<p>
    (2) 若 $a_2=2$, $S_6=30$, 求 $a_8$.
</p>
</myexample>
<mysolution>
    <p>
    设 $\{a_n\}$ 的公差为 $d$. 
</p>

<p>
    (1) 方法一: $a_4-a_2= 2d$, 则 $d=2$,
    \[a_1= a_2-d= -1,\quad a_5= a_4+d= 7,\]
    则 $S_5= \dfrac{(a_1+a_5)\cdot 5}2= 15$.
</p>

<p>
    方法二: $a_2+a_4= 2a_3= 6$, 则 $a_3= 3$, 
    \[S_5= \frac{(a_1+a_5)\cdot 5}2
        = \frac{2a_3\cdot 5}2= 15.\]
</p>

<p>
    (2) 方法一: 由题意, $a_2= a_1+d= 2$,
    \[S_6= \dfrac{(a_1+a_6)\cdot 6}2= 3(2a_1+5d)=30,\]
    解得 $a_1= 0$, $d= 2$, 所以 $a_8= a_1+ 7d= 14$.
</p>

<p>
    方法二: 因为 $a_2= 2$,
    \[S_6= \dfrac{(a_1+a_6)\cdot 6}2
        = 3(a_2+a_5)=30,\]
    所以 $a_5=8$. 而 $a_2+a_8= 2a_5$, 则 $a_8= 14$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    在等差数列 $\{a_n\}$ 中, 已知 $S_8=24$, $S_{16}=32$, 求 $S_{24}$.
</p>
</myexample>
<mysolution>
    <p>
    方法一: 由题意,
    \[\left\{\!\!\begin{array}{l}
        \frac{(a_1+a_8)\cdot 8}2= 24,\\
        \frac{(a_1+a_{16})\cdot 16}2= 32,
    \end{array}\right.\quad\text{即}\quad
    \left\{\!\!\begin{array}{l}
        a_1+a_8= 6,\\
        a_1+a_{16}= 4,
    \end{array}\right.\]
    作差知, $8d=-2$. 所以
    \[a_1+a_{24}= a_1+(a_{16}+16d)= 2,\]
    而 $S_{24}= \dfrac{(a_1+a_{24})\cdot 24}2= 24$.
</p>

<p>
    \mymarginpar{方法一为通用做法, 方法二和方法三均为特殊解法. 注意, 即使是方法一, 也无需解出 $a_1$ 和 $d$.}
    方法二: 因为
    \[S_{16}-S_8= a_9+a_{10}+\cdots +a_{16}= 8,\]
    即 $4(a_9+a_{16})= 8$, 所以
    \[S_{24}= \dfrac{(a_1+a_{24})\cdot 24}2
        =\dfrac{(a_9+a_{16})\cdot 24}2
        = 24.\]
</p>

<p>
    方法三: 因为
    \[\begin{aligned}
        S_8&= a_1+a_2+\cdots +a_8,\\
        S_{16}- S_8&= a_9+a_{10}+\cdots +a_{16},\\
        S_{24}- S_{16}&= a_{17}+a_{18}+\cdots +a_{24},\\
    \end{aligned}\]
    所以 $S_8$, $S_{16}- S_8$, $S_{24}- S_{16}$ 也成等差数列, 则
    \[S_8+ (S_{24}- S_{16})= 2(S_{16}- S_8),\]
    解得 $S_{24}= 3(S_{16}- S_8)= 24$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知等差数列 $\{a_n\}$ 满足: $a_1=2$, 且 $a_1$, $a_2$, $a_5$ 成等比数列.
</p>

<p>
    (1)求数列 $\{a_n\}$ 的通项公式.\qquad   
    (2)记 $S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和, 是否存在正整数 $n$, 使得 $S_n>60n+800$?
</p>
</myexercise>
<mysolution>
    <p>
    (1) 设 $\{a_n\}$ 的公差为 $d$. 因为 $a_2^2= a_1a_5$, 即
    \[(2+d)^2= 2(2+4d),\]
    解得 $d=0$ 或 $4$. 经检验, 均合题意, 故 $a_n=2$ 或 $4n-2$.
</p>

<p>
    (2) 当 $a_n= 2$ 时, $S_n= 2n$, 不满足 $S_n>60n+800$.
</p>

<p>
    当 $a_n= 4n-2$ 时, $S_n= 2n^2$, 不等式 $S_n>60n+800$ 化为
    \[2n^2> 60n+800,\quad n< -10\ \text{或}\ n>40,\]
    取 $n>40$ 即可.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    在等差数列 $\{a_n\}$ 中, 若 $a_3+a_{13}=18$, 求 $a_8$.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: $a_3+a_{13}= 2a_{8}= 18$, 则 $a_8= 9$.
</p>

<p>
    方法二: 设公差为 $d$, 原式改写为
    \[(a_1+2d)+ (a_1+12d)= 18,\]
    整理得 $a_1+7d= 9$, 即 $a_8= 9$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在等差数列 $\{a_n\}$ 中, $a_4=7$, $a_8=15$, 求数列 $\{a_n\}$ 的前 $n$ 项和 $S_n$.
</p>
</myexercise>
<mysolution>
    <p>
    设公差为 $d$, 则 $a_8- a_4= 4d= 8$, $d=2$, 所以
    \[\begin{gathered}
        a_n= a_4+(n-4)d= 2n-1,\\
        S_n= \frac{(a_1+a_n)n}2= n^2.
    \end{gathered}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 已知 $S_{10}=100$, $S_{100}=10$, 求 $S_{110}$.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由题意,
    \[\left\{\!\!\begin{array}{l}
        \frac{(a_1+a_{10})\cdot 10}2= 100,\\
        \frac{(a_1+a_{100})\cdot 100}2= 10,
    \end{array}\right.\quad\text{即}\quad
    \left\{\!\!\begin{array}{l}
        a_1+a_{10}= 20,\\
        a_1+a_{100}= \frac15,
    \end{array}\right.\]
    作差知, $90d=-\dfrac{99}5$. 所以
    \[a_1+a_{110}= a_1+(a_{100}+10d)= -2,\]
    而 $S_{110}= \dfrac{(a_1+a_{110})\cdot 110}2= -110$.
</p>

<p>
    方法二: 因为
    \[S_{100}-S_{10}= a_{11}+a_{12}+\cdots +a_{100}= -90,\]
    即 $45(a_{11}+a_{100})= -90$, 所以
    \[S_{110}= \frac{(a_{1}+a_{110})\cdot 110}2
        =\frac{(a_{11}+a_{100})\cdot 110}2
        = -110.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, $a_1+a_3+a_5=105$, $a_2+a_4+a_6=99$, 求使 $S_n$ 达到最大值的 $n$.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $3a_3= 105$, $3a_4=99$, 则 $a_3= 35$, $a_4= 33$. 设公差为 $d$, 作差知, $d=-2$, 则
    \[a_n= a_3+(n-1)d= 41-2n.\]
    \mymarginpar{更常见的做法是直接计算 $S_n$, 其为关于 $n$ 的二次函数, 再计算对称轴得到最值对应的 $n$.}
    由 $a_1= 39>0$ 且 $a_n$ 关于 $n$ 递减知, 当 $S_n$ 最大时, $a_n\geqslant 0$ 且 $a_{n+1}\leqslant 0$, 解得 $n=20$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    已知数列 $\{a_n\}$ 是等差数列, $a_3=1$, $a_4+a_{10}=18$, 求 $a_1$.
</p>
</myexercise>
<mysolution>
    <p>
    设公差为 $d$, 则
    \[(a_3+d)+ (a_3+7d)= 18,\]
    解得 $d=2$, $a_1= a_3- 2d= -3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在等差数列 $\{a_n\}$ 中, 若 $a_3 +a_7 =37$, 求 $a_2 +a_4 +a_6 +a_8$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_2 +a_8= a_4 +a_6= a_3 +a_7 =37$, 则所求为 $74$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 若 $a_2=-9$, $a_3+a_7=-6$, 求 $S_n$ 取最小值时的 $n$.
</p>
</myexercise>
<mysolution>
    <p>
    设公差为 $d$, 则
    \[(a_2+d)+ (a_2+5d)= -6,\]
    解得 $d=2$, 所以
    \[a_n= a_2+(n-2)d= 2n-13.\]
    由 $a_1= -11>0$ 且 $a_n$ 关于 $n$ 递增知, 当 $S_n$ 最小时, $a_n\leqslant 0$ 且 $a_{n+1}\geqslant 0$, 解得 $n=6$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$ 的公差 $d\neq 0$, $a_1=2$ 且 $a_1$, $a_3$, $a_6$ 成等比数列, 求 $a_n$.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $a_3^2= a_1a_6$, 即
    \[(a_1+2d)^2= a_1(a_1+5d),\]
    解得 $d=0$ (舍) 或 $\dfrac12$, 则 $a_n= \dfrac{n+3}2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 若 $a_2 a_4 a_6 a_8=120$,
    \[\dfrac1{a_4 a_6 a_8}+ \dfrac1{a_2 a_6 a_8}+ 
        \dfrac1{a_2 a_4 a_8}+ \dfrac1{a_2 a_4 a_6}
        =\dfrac7{60},\]
    求 $S_9$.
</p>
</myexercise>
<mysolution>
    <p>
    已知分式化为 
    \[a_2+a_4+a_6+a_8= 14,\quad\text{即}\quad
        4a_5= 14,\]
    所以 
    \[S_9= \frac{(a_1+a_9)\cdot 9}2
        = \frac{2a_5\cdot 9}2
        = \frac{63}{2}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等差数列 $\{a_n\}$, $\{b_n\}$ 的前 $n$ 项和分别为 $S_n$, $T_n$ 满足 $\dfrac{S_n}{T_n}= \dfrac{2n+4}{3n+1}$, 若 $a_m=b_m$, 求 $m$.
</p>
</myexercise>
<mysolution>
    <p>
    由等差数列求和公式,
    \[\frac{S_n}{T_n}
        = \frac{\dfrac12(a_1+a_n)n}{\dfrac12(b_1+b_n)n}
        = \frac{a_1+a_n}{b_1+b_n},\]
    即 $\dfrac{a_1+a_n}{b_1+b_n}= \dfrac{2n+4}{3n+1}$. 令 $n= 2m-1$, 则
    \[\dfrac{a_1+a_{2m-1}}{b_1+b_{2m-1}}
        = \dfrac{2(2m-1)+4}{3(2m-1)+1}.\]
    因为 
    \[a_1+a_{2m-1}= 2a_m= 2b_m= b_1+b_{2m-1},\]
    代入上式解得, $m=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $k$ 是常数, $S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和且 $S_n=kn^2+n$, $n\in\mathbb{N}^*$.
</p>

<p>
    (1) 求 $a_1$ 及 $a_n$;\qquad
    (2) 若对于任意的 $m\in\mathbb{N}^*$, $a_m$, $a_{2m}$, $a_{4m}$ 成等比数列, 求 $k$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) $a_1= S_1= k+1$. 当 $n\geqslant 2$ 时,
    \[a_n= S_n-S_{n-1}= 2kn-k+1.\]
    所以 $a_n= 2kn-k+1$, $n\geqslant 1$.
</p>

<p>
    (2) 不妨取 $m=1$, 则 $a_1$, $a_2$, $a_4$ 成等比数列, 所以 $a_2^2= a_1a_4$, 即
    \[(3k+1)^2= (k+1)(7k+1),\]
    \mymarginpar{因为取了特殊的 $m$ 值, 所以必须验证一般情形.}解得 $k=0$ 或 $1$. 容易验证, 这两个值均符合题意.
</p>
</mysolution>