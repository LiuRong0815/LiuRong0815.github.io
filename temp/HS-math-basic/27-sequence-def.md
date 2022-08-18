\sectioncounter{26}
</p>

<p>
\section{数列的概念}
</p>

<p>
\subsection{知识梳理}
按一定次序排成的一列数 $a_1$, $a_2$, $\cdots$, $a_n$, $\cdots$ 叫做数列, 记成 $\{a_n\}$, 其中 $a_n$ 是数列的第 $n$ 项.
通常 $n$ 为正整数, 即 $n\in\mathbb{Z}^+$. 有时 $n$ 也从 $0$ 开始取值. 由有限项构成的数列称为有穷数列, 否则称为无穷数列. 数列还可以依增减性分类. 数列 $\{a_n\}$ 的第一项称为首项, 最后一项 (如果有的话) 称为末项.
</p>

<p>
数列 $\{a_n\}$ 的每一项 $a_n$ 可以视为 $n$ 的函数. 
若此函数可以用一个式子表示, 则把该式称为 $\{a_n\}$ 的通项公式.
例如通项公式 $a_n=2^n$ 对应数列 $2$, $4$, $8$, $16$, $\cdots$, 
$b_n= 1+\cos n\pi$ 对应数列 $0$, $2$, $0$, $2$, $\cdots$. 有些数列可有多个通项公式, 如前述后一数列的通项公式也可以写为 $a_n= 1+(-1)^n$. 联系相邻两项的式子称为数列的两项递推式, 简称为递推式. 例如 $\{a_n=2^n\}$ 的递推式为 $a_{n+1}= 2a_n$. 由特殊的递推式可求得通项公式. 
</p>

<p>
设数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 则
\[S_n=a_1+a_2+\cdots+a_n.\]
从这个式子可以得到前 $n$ 项和 $S_n$ 与第 $n$ 项 $a_n$ 的另一个常见关系
\[a_n=\begin{cases}
      S_1, & n=1,\\
      S_n-S_{n-1}, & n\geqslant 2.
    \end{cases}\]
</p>

<p>
\lianxi
<myexercise>
    <p>    数列 $\{a_n\}$ 的通项公式为 $a_n =\dfrac{(-1)^n}{3^n}$, 求该数列的首项.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= -\dfrac13$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    数列 $\{a_n\}$ 的通项公式为 $a_n =3n-2$, 求 $a_4$, $a_8$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a_4= 10$, $a_8= 22$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    数列 $\{a_n\}$ 的通项公式为 $a_n=\dfrac{n+1}{2n+3}$, 求该数列的前 $5$ 项.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= \dfrac25$, $a_2= \dfrac37$, $a_3= \dfrac49$, $a_4= \dfrac5{11}$, $a_5= \dfrac6{13}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    $32$ 是数列 $\{n^2 +4n\}$ 中的第几项\,?
</p>
</myexercise>
<mysolution>
    <p>
    令 $n^2 +4n= 32$, 解得 $n=4$ (舍负).
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求数列 $\{n^2 -8n+5\}$ 中各项的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    由二次函数图象知, 当 $n=4$ 时, $n^2 -8n+5= -1$ 最小.
</p>

<p>
    \varexercise 若数列通项 $a_n= n^2 -7n+5$, 则 $a_3$, $a_4$ 均最小.
</p>

<p>
    \varexercise 若数列通项 $a_n= 2n^2 -7n+5$, 则 $a_2$ 最小.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{数列的通项公式}
<span id="example-"></span>
<myexample>
    <p>
    若数列 $\{a_n\}$ 的通项公式是 $a_n =(-1)^n (2n+3)$, 求 $a_4 +a_7 +a_{10}$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    $a_4= 11$, $a_7=-17$, $a_{10}= 23$, 所以 $a_4+a_7+a_{10}= 17$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    求数列 $\biggl\{a_n= \ln\dfrac{n}{n+1}\biggr\}$ 的前 $n$ 项和 $S_n$.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[\begin{aligned}
        S_n
        &= a_1+a_2+\cdots +a_n\\
        &= \ln\frac12+ \ln\frac23+ \cdots + \ln\frac{n}{n+1}\\
        &= \ln\biggl(\frac12\cdot \frac23\cdot\,\cdots\,\cdot \frac{n}{n+1}\biggr)\\
        &= \ln\frac1{n+1}= -\ln(n+1).
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\subsubsection{数列的前 $n$ 项和与通项公式的关系}
<span id="example-"></span>
<myexample>
    <p>
    已知数列 $\{a_n\}$ 的前 $n$ 项和 $S_n=2n^2 +2n$, 数列 $\{b_n\}$ 的前 $n$ 项和 $T_n =2-b_n$.
</p>

<p>
    (1) 求数列 $\{a_n\}$ 与 $\{b_n\}$ 的通项公式;
</p>

<p>
    (2) 设 $c_n=a_n^2b_ n$, 验证: 当且仅当 $n\geqslant 3$ 时, $c_{n+1}< c_n$.
</p>
</myexample>
<mysolution>
    <p>
    (1) $a_1= S_1= 4$. 当 $n\geqslant 2$ 时, 
    \[a_n= S_n-S_{n-1}= 4n.\]
    所以 $a_n=4n$. 由 $b_1= T_1= 2-b_1$ 知 $b_1=1$. 当 $n\geqslant 2$ 时, 
    \[b_n= T_n-T_{n-1}= (2-b_n)- (2-b_{n-1}),\]
    整理得 $b_n= \dfrac12 b_{n-1}$, 所以 $b_n= \dfrac1{2^{n-1}}$.
</p>

<p>
    (2) 由 (1) 知,
    \[c_n= \frac{(4n)^2}{2^{n-1}}= \frac{n^2}{2^{n-5}}.\]
    因为 $c_1= 16$, $c_2= 32$, $c_3= 36$, $c_4= 32$, 所以当 $n=1$, $2$ 时, $c_{n+1}> c_n$. 而当 $n\geqslant 3$ 时,
    \[\begin{aligned}
        c_{n+1}-c_n
        &= \frac{(n+1)^2}{2^{n-4}}- \frac{n^2}{2^{n-5}}
         = \frac{-n^2+2n+1}{2^{n-4}}\\
        &= \frac{-(n-1)^2+2}{2^{n-4}}< 0,
    \end{aligned}\]
    表明 $c_{n+1}< c_n$. 综上可知结论成立.
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    已知数列 $\{a_n\}$ 的前 $n$ 项和 $S_n=2n^2 -3n$, 求其通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= S_1= -1$. 当 $n\geqslant 2$ 时, 
    \[a_n= S_n-S_{n-1}= 4n-5.\]
    故 $a_n= 4n-5$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 且 $S_n =3^n +1$, 求 $a_n $ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= S_1= 4$. 当 $n\geqslant 2$ 时, 
    \[a_n= S_n-S_{n-1}= 2\cdot 3^{n-1}.\]
    故 
    \[a_n= \begin{cases}
        4, & n=1,\\
        2\cdot 3^{n-1}, & n\geqslant 2.
    \end{cases}\]
</p>
</mysolution>
</p>

<p>
\subsubsection{由特殊的递推关系式求通项}
<span id="example-"></span>
<myexample>
    <p>
    若数列 $\{a_n\}$ 满足 $a_{n+1}= \dfrac1{1-a_n}$, 且 $a_8 =2$, 求 $a_1$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    由已知, $a_n= 1- \dfrac{1}{a_{n+1}}$, 则
    \[\begin{aligned}
        a_7&= 1- \frac{1}{a_8}= \frac12,\\
        a_6&= 1- \frac{1}{a_7}= -1,\\
        a_5&= 1- \frac{1}{a_6}= 2= a_8,
    \end{aligned}\]
    说明数列各项满足 $a_n= a_{n+3}$, 所以 $a_1=a_4=a_7= \dfrac12$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    数列 $\{a_n\}$ 满足 $a_{n+1}=\begin{cases}
      2a_n, & 0\leqslant a_n< \dfrac12,\\
      2a_n-1, & \dfrac12\leqslant a_n< 1.\end{cases}$
    若 $a_1=\dfrac67$, 求 $a_{2021}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    直接按定义计算得: $a_2= \dfrac57$, $a_3= \dfrac37$, $a_4= \dfrac67= a_1$, 说明数列各项满足 $a_n= a_{n+3}$, 所以 $a_{2021}= a_2= \dfrac57$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    某数列 $\{a_n\}$ 的前四项分别为 $0$, $\sqrt{2}$, $0$, $\sqrt2$, 
    下列各式中可作为 $\{a_n\}$ 的通项公式的是\,? (填序号)
</p>

<p>
    (1) $a_n= \dfrac{\sqrt2}2 [1+(-1)^n]$;\qquad
    (2) $a_n= \sqrt{1+(-1)^n}$;
</p>

<p>
    (3) $a_n= \begin{cases}
      \sqrt2, & \text{$n$ 为偶数},\\
      0, & \text{$n$ 为奇数}.\end{cases}$
</p>
</myexercise>
<mysolution>
    <p>
    (1) (2) (3) 均可.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 中, $a_n = 2n^2 -10n+3$, 求它的最小项.
</p>
</myexercise>
<mysolution>
    <p>
    对应的二次函数 $f(x)= 2x^2-10x+3$ 图象的对称轴为 $x= \dfrac52$, 开口向上, 所以 $a_2$, $a_3$ 均为最小值. 
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 若 $S_n= n^2 +3n+1$, 求 $a_n$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= S_1= 5$. 当 $n\geqslant 2$ 时, 
    \[a_n= S_n-S_{n-1}= 2n+2.\]
    故 
    \[a_n= \begin{cases}
        5, & n=1,\\
        2n+2, & n\geqslant 2.
    \end{cases}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 的前 $n$ 项和 $S_n =n^2$ ($n\in\mathbb{N}^*$), 求 $a_8$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a_8= S_8-S_7= 15$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    设数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n =2a_n -2^n$, 求 $a_1$, $a_2$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= S_1= 2a_1-2$, 则 $a_1=2$. 而
    \[a_1+a_2= S_2= 2a_2-4,\]
    解得 $a_2=6$. (类似地, 此题可求出 $a_n=(n+1)2^{n-1}$.)
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    写出数列 $1$, $2$, $\sqrt7$, $\sqrt{10}$, $\cdots$ 的一个通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    $a_n=\sqrt{3n-2}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    写出数列 $2$, $-6$, $12$, $-20$, $30$, $-42$, $\cdots$ 的一个通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    $a_n= (-1)^{n+1} n(n+1)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 的前 $n$ 项和 $S_n= n^2 -9n$, 若 $5< a_k < 8$, 求 $k$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $a_1= S_1= -8$. 当 $n\geqslant 2$ 时, 
    \[a_n= S_n-S_{n-1}= 2n-10.\]
    不等式化为 $5< 2k-10< 8$, 解得 $\dfrac{15}2< k< 9$, 故 $k=8$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    数列 $\{a_n\}$ 满足 $\dfrac{a_1}2+ \dfrac{a_2}{2^2}+\cdots+ \dfrac{a_n}{2^n} =2n+5$, $n\in\mathbb{N}^*$, 求 $a_n$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $\dfrac{a_1}2= 2+5$, 即 $a_1=14$. 而当 $n\geqslant 2$ 时,
    \[\dfrac{a_1}2+ \dfrac{a_2}{2^2}+\cdots
    + \dfrac{a_{n-1}}{2^{n-1}}+ \dfrac{a_n}{2^n}=2n+3,\]
    与已知式作差得 $\dfrac{a_n}{2^n}= 2$, 即 $a_n= 2^{n+1}$. 所以
    \[a_n= \begin{cases}
        14, & n=1,\\
        2^{n+1}, & n\geqslant 2.
    \end{cases}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知二次函数 $y=f(x)$ 的图象经过坐标原点, 其导函数为 $f'(x)=6x-2$. 
    数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 点 $(n,S_n)$ ($n\in\mathbb{N}^*$) 均在函数 $y=f(x)$ 的图象上, 求数列 $\{a_n\}$ 的通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $f(x)= 3x^2-2x$, 而 $S_n= 3n^2-2n$, 则 $a_1= S_1= 1$. 当 $n\geqslant 2$ 时, 
    \[a_n= S_n-S_{n-1}= 6n-5.\]
    所以 $a_n= 6n-5$.
</p>
</mysolution>