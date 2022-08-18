\sectioncounter{28}
</p>

<p>
\section{等比数列}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
若数列 $\{a_n\}$ 相邻两项中, 后一项除以前一项为定值 $q$, 即 $\dfrac{a_{n+1}}{a_n}=q$, 则称 $\{a_n\}$ 为等比数列. 由定义, $q\neq0$ 且 $a_n\neq 0$. 还可知递推式 $a_{n+1}=a_n q$, 再用累乘法可得通项公式 $a_n=a_1 q^{n-1}$. 注意, 等比数列的通项公式为指数式, 其中指数为项数的一次式 (反之如何?).
\mymarginpar{当 $|q|>1$ 时, $|a_n|$ 递增;\\
当 $|q|< 1$ 时, $|a_n|$ 递减;\\
当 $q< 0$ 时, $\{a_n\}$ 为摆动数列.}
</p>

<p>
直接由通项公式可验证 $\dfrac{a_n}{a_m}=q^{n-m}$, 即 $a_n=a_m q^{n-m}$. 注意, 公式中 $m$, $n$ 无大小之分, 如
\[a_6= a_2q^4,\quad a_5= a_9 q^{-4}.\]
若 $m+n=p+q$, 则 $a_m a_n=a_p a_q$. 特别地, 
\[2m=p+q \Leftrightarrow a_m^2=a_p a_q.\]
称 $a$, $b$, $c$ 成等比数列是指 $\dfrac{b}{a}= \dfrac{c}b$, 也就是 $b^2=ac$, 其中 $b$ 称为 $a$, $c$ 的等比中项. 两个数的等比中项一般有两个 (为什么?).
</p>

<p>
由错位相减法可得等比数列 $\{a_n\}$ (公比 $q\neq 1$) 的前 $n$ 项和公式, 即把
\[\begin{aligned}
    S_n&= a_1+a_2+\cdots+a_n,\\
    qS_n&= \phantom{a_1+{}}a_1q+\cdots+a_{n-1}q+a_nq
\end{aligned}\]
相减可得
\[(1-q)S_n= a_1-a_nq,\quad S_n=a_1\frac{1-q^n}{1-q}.\]
若 $q=1$, 则易知 $S_n=na_1$.
</p>

<p>
\lianxi
<myexercise>
    <p>    正项等比数列 $\{a_n\}$ 中 $a_2=9$, $a_4=4$, 求其通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    $q>0$ 且 $q^2= \dfrac{a_4}{a_2}= \dfrac49$, 则 $q= \dfrac23$,
    \[a_n= a_2 q^{n-2}
        = 9\cdot\biggl(\frac23\biggr)^{n-2}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $-1$, $a$, $b$, $c$, $-9$ 成等比数列, 求 $b$, $ac$.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $a^2= -b$, $b^2= ac$, $c^2= 9c$, 则
    \mymarginpar{$-1$, $b$, $-9$ 也成等比数列.}
    \[b< 0,\quad b^4= a^2c^2= 9b^2,\]
    所以 $b=-3$, $ac=b^2=9$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    根据 $x$ 的不同取值, 求数列 $\{a_n\}=\{x^n\}$ 的前 $n$ 项和 $S_n$.
</p>
</myexercise>
<mysolution>
    <p>
    若 $x=0$, 则 $a_n= 0$, $S_n=0$;
</p>

<p>
    若 $x=1$, 则 $a_n= 1$, $S_n=n$;
</p>

<p>
    若 $x\neq0,1$, 则 $\{a_n\}$ 为等比数列, 首项 $a_1= x$, 公比 $q=x$, 则
    \[S_n= a_1\frac{1-q^n}{1-q}= \frac{x(1-x^n)}{1-x}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若等比数列的通项公式为 $a_n=4\cdot 3^{1-n}$, 判断数列 $\{a_n\}$ 的增减性.
</p>
</myexercise>
<mysolution>
    <p>
    公比 $q= 3^{-1}\in(0,1)$, 首项 $a_n= 4>0$, 则数列 $\{a_n\}$ 递减.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知实数 $k$ 和 $5k-2$ 的等比中项是 $2k$, 求 $k$.
</p>
</myexercise>
<mysolution>
    <p>
    $(2k)^2= k(5k-2)$, 则 $k=0$ 或 $2$. 检验可知, $k=2$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{等比数列的基本量运算}
<span id="example-"></span>
<myexample>
    <p>
    在等比数列 $\{a_n\}$ 中, $a_1+a_3 =10$, $a_4 +a_6 =\dfrac54$, 求 $a_n$.
</p>
</myexample>
<mysolution>
    <p>
    设公比为 $q$, 则
    \[a_4 +a_6= (a_1+a_3)q^3,\]
    解得 $q=\frac12$. 而
    \[a_1+a_3= a_1(1+q^2)= 10,\quad a_1= 4,\]
    所以 $a_1= 4$, 且
    \[a_n= a_1q^{n-1}= 2^{3-n}.\]
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    正项等比数列 $\{a_n\}$ 中 $3a_1$, $\dfrac12 a_3$, $2a_2$ 成等差数列, 求 $\dfrac{a_9+a_{10}}{a_7+a_8}$.
</p>
</myexample>
<mysolution>
    <p>
    设公比为 $q$. 由已知, $q>0$, $a_1>0$, 且
    \[2\cdot \frac12 a_3= 3a_1+2a_2,\]
    整理得 $q^2-2q-3=0$, 则 $q=3$. 因此
    \[\dfrac{a_9+a_{10}}{a_7+a_8}
        = \dfrac{q^2(a_7+a_8)}{a_7+a_8}
        = 9.\]
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    求等比数列 $x$, $3x+3$, $6x+6$, $\cdots$ 的第 $4$ 项.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, 
    \[(3x+3)^2= x(6x+6),\quad x=-1,-3.\]
    经检验, $x=-3$. 所以等比数列为 $-3$, $-6$, $-12$, $\cdots$, 公比为 $2$, 第 $4$ 项为 $-24$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在等比数列 $\{a_n\}$ 中, $a_2=1$, $a_8=a_6 +2a_4$, 求 $a_6$.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $a_4 q^4= a_4q^2+ 2a_4$, 则
    \[q^4- q^2- 2=0,\quad q^2=-1,2.\]
    显然 $q^2=2$, 则 $a^6= a_2 q^4= 4$.
</p>
</mysolution>
</p>

<p>
\subsubsection{等比数列的求和问题}
<span id="example-"></span>
<myexample>
    <p>
    已知等比数列 $\{a_n\}$ 的公比 $q\neq 1$, 首项 $a_1=\dfrac12$, 前 $n$ 项和为 $S_n$, 且 $a_4 +S_4$, $a_5+S_5$, $a_6+S_6$ 成等差数列.
</p>

<p>
    (1) 求 $\{a_n\}$ 的通项公式及 $S_n$;\qquad
    (2) 对 $n\in\mathbb{N}^*$, 在 $a_n$ 与 $a_{n+1}$ 之间插入 $3^n$ 个数, 使这 $(3^n+2)$ 个数成等差数列, 记插入的这 $3^n$ 个数的和为 $b_n$, 求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由题意, 
    \[2(a_5+S_5)= (a_4 +S_4)+ (a_6+S_6).\]
    将 $S_4= S_5- a_5$, $S_6= S_5+a_6$ 代入并整理,
    \[2a_6- 3a_5+a_4=0,\quad 2q^2-3q+1=0,\]
    解得 $q=1$ (舍) 或 $\dfrac12$, 所以
    \[a_n= a_1 q^{n-1}= \frac1{2^n},\quad
        S_n= 1-\frac1{2^n}.\]
</p>

<p>
    (2) 由等差数列求和公式,
    \[a_n+b_n+a_{n+1}= \frac12(a_n+a_{n+1})(3^n+2),\]
    所以
    \[b_n= \frac{3^n}2(a_n+ a_{n+1})
        = \frac12\biggl(\frac32\biggr)^2.\]
    因此 $\{b_n\}$ 为等比数列, 首项 $b_1= \dfrac34$, 公比为 $\dfrac32$, 故
    \[T_n= \frac34\cdot\frac{1-\biggl(\dfrac32\biggr)^n}{1-\dfrac32}
        = \biggl(\frac32\biggr)^{n+1}- \frac32.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    若等比数列 $\{a_n\}$ 满足 $a_2 a_4=\dfrac12$, 求 $a_1 a_3^2 a_5$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1 a_3= a_2^2$, $a_3 a_5= a_4^2$, 则
    \[a_1 a_3^2 a_5= (a_2 a_4)^2= \frac14.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在正项等比数列 $\{a_n\}$ 中, $a_3 a_{11} =16$, 求 $\log_2 a_2 +\log_2 a_{12}$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_2 a_{12}= a_3 a_{11}= 16$, 则
    \[\log_2 a_2 +\log_2 a_{12}= \log_2 (a_2a_{12})
        = \log_2 16= 4.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    等比数列 $\{a_n\}$ 中, $a_4=2$, $a_5=5$, 求数列 $\{\lg a_n\}$ 的前 $8$ 项和.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1a_2\cdot a_8= (a_4a_5)^4= 10^4$, 则
    \[\begin{aligned}
        &\lg a_1+ \lg a_2+\cdots \lg a_8\\
        ={}& \lg (a_1 a_2\cdots a_8)
        = \lg 10^4= 4.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知在等差数列 $\{a_n\}$ 中, $a_3+a_1=8$, 且 $a_4$ 为 $a_2$ 和 $a_9$ 的等比中项, 求数列 $\{a_n\}$ 的前 $n$ 项和 $S_n$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_3+a_1= 2a_2= 8$, 则 $a_2= 4$. 而 $a_4^2= a_2 a_9$, 设公差为 $d$, 则
    \[(4+2d)^2= 4(4+7d),\quad d=0,3.\]
    当 $d=0$ 时, 
    \[a_n=a_2= 4,\quad S_n= 4n;\]
    当 $d=3$ 时, 
    \[\begin{gathered}
        a_n= a_2+ (n-2)d= 3n-2,\\
        S_n= \frac{(a_1+a_n)n}2= \frac{n(3n-1)}2.
    \end{gathered}\]
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    在等比数列 $\{a_n\}$ 中, $a_3 =2$, $a_7=8$, 求 $a_5$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_5^2= a_3a_7= 16$, $a_5= \pm4$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知正项等比数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 若 $a_3=18$, $S_3=26$, 求数列 $\{a_n\}$ 的公比 $q$.
</p>
</myexercise>
<mysolution>
    <p>
    $S_3= a_1+a_2+a_3$, 则 $a_1+a_2= 8$, 所以
    \[\left\{\!\!\begin{array}{l}
        a_1+a_1q= 8,\\
        a_1 q^2= 18,
    \end{array}\right.\quad\text{即}\quad
    \frac{1+q}{q^2}= \frac49.\]
    结合 $q>0$ 解得 $q=3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在等比数列 $\{a_n\}$ 中, $S_n$ 为其前 $n$ 项和, 已知 $a_5 =2S_4 +3$, $a_6 =2S_5 +3$, 求此数列的公比 $q$.
</p>
</myexercise>
<mysolution>
    <p>
    将已知两式作差,
    \[a_6- a_5= 2a_5,\quad a_6= 3a_5,\]
    则 $q= \dfrac{a_6}{a_5}= 3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设等比数列 $\{a_n\}$ 的前 $5$ 项和为 $62$, $a_2 a_8 =2a_3 a_6$, 求 $a_1$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_2 a_8 =a_3 a_7= 2a_3 a_6$, 即 $a_7= 2a_6$. 设公比为 $q$, 则 $q= \dfrac{a_7}{a_6}= 2$. 因为前 $5$ 项和为
    \[a_1\frac{1- q^5}{1-q}= 62,\]
    解得 $a_1=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若正项等比数列 $\{a_n\}$ 中, $a_{10} a_{11} + a_9 a_{12} = 2\mathrm{e}^5$, 求 
    \[\ln a_1 +\ln a_2 +\cdots+\ln a_{20}.\]
</p>
</myexercise>
<mysolution>
    <p>
    $a_{10} a_{11}= a_9 a_{12}$, 则 $a_{10} a_{11}= \mathrm{e}^5$, 且
    \[\begin{aligned}
        &\ln a_1 +\ln a_2 +\cdots+\ln a_{20}\\
        ={}& \ln (a_1 a_2 \cdots \ln a_{20})
            = \ln[(a_{10}a_{11})^{10}]\\
        ={}& 10\ln(a_{10}a_{11})
            = 50.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知等比数列 $\{a_n\}$ 满足 $|a_2-a_3|=10$, $a_1 a_2 a_3 =125$.
</p>

<p>
    (1) 求 $\{a_n\}$ 的通项公式;
</p>

<p>
    (2) 是否存在正整数 $m$, 使得 $\dfrac1{a_1}+\dfrac1{a_2}+\cdots +\dfrac1{a_m} \geqslant 1$? 若存在, 请求出 $m$ 的最小值; 若不存在,请说明理由.
</p>
</myexercise>
<mysolution>
    <p>
    (1) $a_1a_2a_3= a_2^3= 125$, 则 $a_2=4$, 代入 $|a_2-a_3|=10$ 知, $a_3= -5$ 或 $15$.
</p>

<p>
    当 $a_3= -5$ 时, 公比 $q= -1$, $a_n= 5\cdot(-1)^n$;
    当 $a_3= 15$ 时, 公比 $q= 3$, $a_n= 5\cdot 3^{n-2}$.
</p>

<p>
    (2) 若 $a_n= 5\cdot(-1)^n$, 则 $\dfrac1{a_m}= \dfrac{(-1)^m}5$, 所以
    \[\frac1{a_1}+\frac1{a_2}+\cdots +\frac1{a_m}
    = -\frac15\ \text{或}\ 0,\]
    此时不存在符合题意的 $m$.
</p>

<p>
    若 $a_n= 5\cdot 3^{n-2}$, 则 $\biggl\{\dfrac1{a_m}\biggr\}= \biggl\{\dfrac1{5\cdot 3^{n-2}}\biggr\}$ 为等比数列, 首项为 $\dfrac35$, 公比为 $\dfrac13$, 所以
    \[\begin{aligned}
        \frac1{a_1}+\frac1{a_2}+\cdots +\frac1{a_m}
        &= \frac35\cdot\frac{1-\biggl(\dfrac13\biggr)^m}{1-\dfrac13}\\
        &= \frac{9}{10}\biggl[1-\biggl(\frac13\biggr)^m\biggr]
        < \frac{9}{10},
    \end{aligned}\]
    此时也不存在符合题意的 $m$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 且 $S_n=2a_n -3n$ ($n\in\mathbb{N}^*$).
</p>

<p>
    (1) 求证: 数列 $\{a_n +3\}$ 为等比数列;
</p>

<p>
    (2) 求数列 $\{S_n\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 当 $n=1$ 时, $S_1= 2a_1-3$, 即
    \[a_1= 2a_1-3,\quad a_1= 3.\]
    当 $n\geqslant 2$ 时, 
    \[S_n= 2a_n-3n,\quad S_{n-1}= 2a_{n-1}-3(n-1),\]
    作差,
    \[a_n= 2a_n- 2a_{n-1}- 3,\quad
        a_n= 2a_{n-1}+3,\]
    故 
    \[a_{n}+ 3= 2(a_{n-1}+3),\]
    表明 $\{a_n+3\}$ 为等比数列, 公比为 $2$, 首项为 $a_1+3= 6$.
</p>

<p>
    (2) 由 (1) 知,
    \[a_n+3= (a_1+3)\cdot 2^{n-1}= 3\cdot 2^n,\]
    所以 $a_n= 3\cdot 2^n-3$,
    \[S_n= 2a_n-3n= 3\cdot 2^{n+1}- 3n-6.\]
    因为 $\{2^{n+1}\}$ 为等比数列, $\{3n\}$ 为等差数列, 所以
    \[\begin{aligned}
        T_n&= 3\cdot\frac{4(1-2^n)}{1-2}
            - 3\cdot\frac{(1+n)n}{2}- 6n\\
        &= 12(2^n-1)- \frac32n^2- \frac{15}2n.
    \end{aligned}\]
</p>
</mysolution>