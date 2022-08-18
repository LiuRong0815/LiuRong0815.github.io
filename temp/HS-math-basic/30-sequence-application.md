\sectioncounter{29}
</p>

<p>
\section{数列的综合应用}
</p>

<p>
\subsection{知识梳理}
常见的数列求和方法除了等差数列的倒序相加法, 等比数列的错位相减法, 还有裂项相消法. 如求数列 $\Big\{\dfrac1{n(n+1)}\Big\}$ 的前 $n$ 项和 $S_n$:
\[\begin{aligned}
    S_n
    &= \frac1{1\times2}+\frac1{2\times3}+\cdots+\frac1{n(n+1)} \\
    &= \Big(1-\frac12\Big)+\Big(\frac12-\frac13\Big)+\cdots
       +\Big(\frac1{n}-\frac1{n+1}\Big)                    \\
    &= 1-\frac1{n+1}
     = \frac{n}{n+1}.
\end{aligned}\]
类似可求得数列 $\Big\{\dfrac1{n(n+2)}\Big\}$ 的前 $n$ 项和为 $\dfrac{n+1}{2(n+2)}$ (参考下方练习题). 此外, 数列 $\{a_n+b_n\}$ 求和可转化为数列 $\{a_n\}$ 和 $\{b_n\}$ 求和.
</p>

<p>
在解找规律问题时, 通常会用等差数列或等比数列的通项公式或求和公式.
</p>

<p>
\lianxi
<myexercise>
    <p>    求数列 $\{n+2^n\}$ 的前 $n$ 项和 $S_{n}$.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\{n\}$ 为等差数列, $\{2^n\}$ 为等差数列, 所以
    \[\begin{aligned}
        S_{10}
        &= (1+2+\cdots n)+ (2^1+2^2+\cdots 2^n)\\
        &= \frac{(1+n)n}{2}+ \frac{2(1-2^n)}{1-2}\\
        &= \frac{(1+n)n}{2}+ 2^{n+1}-2.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求数列 $\Big\{\dfrac1{n(n+3)}\Big\}$ 前 $n$ 项和 $S_n$.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\dfrac1{n(n+3)}= \dfrac13\biggl(\dfrac1n- \dfrac1{n+3}\biggr)$, 所以
    \[\begin{aligned}
        S_n
        &= \frac13\biggl[\biggl(\frac11-\frac14\biggr)
            +\biggl(\frac12-\frac15\biggr)
            +\biggl(\frac1{n}-\frac1{n+3}\biggr)\biggr]\\
        &= \frac13\biggl(1+\frac12+\frac13- \frac1{n+1}
            - \frac1{n+2}- \frac1{n+3}\biggr)\\
        &= \frac13\biggl(\frac{11}6- \frac1{n+1}
            - \frac1{n+2}- \frac1{n+3}\biggr).
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 满足: $a_1=1$, $a_n=n+a_{n-1}$ ($n\geqslant 2$), 求其通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, 当 $n\geqslant 2$ 时,
    \[\begin{aligned}
        a_n
        &= n+ a_{n-1}= n+ (n-1+a_{n-2})\\
        &= \cdots = n+(n-1)+\cdots + 2+ a_1\\
        &= n+(n-1)+\cdots +2+1\\
        &= \frac{n(n+1)}2,
    \end{aligned}\]
    与 $a_1= 1$ 相符, 故 $a_n= \dfrac{n(n+1)}2$, $n\geqslant 1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知一个直角三角形的三边长可构成等差数列, 其中最小边长为 $3$, 求该直角三角形的斜边长.
</p>
</myexercise>
<mysolution>
    <p>
    设三边为 $3$, $3+d$, $3+2d$ ($d>0$), 则 $3+2d$ 为斜边, 且
    \[(3+2d)^2= 3^2+ (3+d)^2,\]
    解得 $d=1$, 故斜边为 $5$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, 若 $\overrightarrow{OB} =a_1 \overrightarrow{OA} +a_{200}\overrightarrow{OC}$, 且 $A$, $B$, $C$ 三点共线(该直线不过原点 $O$), 求 $S_{200}$.
</p>
</myexercise>
<mysolution>
    <p>
    由 $A$, $B$, $C$ 三点共线可设 $\overrightarrow{AB}= \lambda\overrightarrow{AC}$, 则
    \[\overrightarrow{OB}= (1-\lambda)\overrightarrow{OA}
        + \lambda\overrightarrow{OC}.\]
    对比已知式,
    \[a_1+a_{200}= (1-\lambda)+ \lambda= 1,\]
    所以
    \[S_{200}= \frac{(a_1+ a_{200})\cdot 200}2= 100.\]
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
</p>

<p>
\subsubsection{利用裂项相消法求数列的和}
<span id="example-"></span>
<myexample>
    <p>
    在等比数列 $\{a_n\}$ 中, 已知 $S_3= \dfrac72$, $S_6= \dfrac{63}2$.
</p>

<p>
    (1) 求 $\{a_n\}$ 的通项公式;
</p>

<p>
    (2) 记 $b_n =\log_4 a_3 +\log_4 a_4 +\cdots+\log_4 a_{n+2}$, 且 $c_n =\dfrac1{b_n}$, 试比较 $\{c_n\}$ 的前 $n$ 项和 $T_n$ 与 $4$ 的大小.
</p>
</myexample>
<mysolution>
    <p>
    (1) 设 $\{a_n\}$ 的公比为 $q$, 则
    \[S_3= \frac{a_1(1-q^3)}{1-a}= \frac72,\quad
    S_6= \frac{a_1(1-q^6)}{1-a}= \frac{63}2,\]
    相除得
    \[\frac{q^6- 1}{q^3-1}= 9,\quad q^3+1= 9,\]
    解得 $q=2$, 则 
    \[a_1= \frac12,\quad a_n= 2^{n-2}.\]
</p>

<p>
    (2) 由 (1) 知,
    \[\log_4 a_n= \log_4 2^{n-2}= \frac{n-2}2,\]
    所以
    \[\begin{aligned}
        b_n&= \frac{3-2}2+ \frac{4-2}2+\cdots +\frac{n+2-2}2\\
        &= \frac12+ \frac22+\cdots +\frac{n}2
         = \frac{(1+n)n}{4}.
    \end{aligned}\]
    而 $c_n= \dfrac1{b_n}= \dfrac4{n(n+1)}$, 则
    \[\begin{aligned}
        T_n&= c_1+ c_2+\cdots c_n\\
        &= 4\biggl(\frac1{1\times2}+ \frac1{2\times3}+\cdots 
            +\frac1{n(n+1)}\biggr)\\
        &= 4\biggl(1-\frac1{1+n}\biggr)< 4.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    在等差数列 $\{a_n\}$ 中, $a_7=4$, $a_{19}= 2a_9$.
</p>

<p>
    (1) 求 $\{a_n\}$ 的通项公式;
</p>

<p>
    (2) 设 $b_n =\dfrac1{n a_n}$, 求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 设 $\{a_n\}$ 的公差为 $d$, 则 $a_{19}= 2a_9$ 化为
    \[a_7+ 12d= 2(a_7+2d),\]
    解得 $d= \dfrac12$, 所以
    \[a_n= a_7+(n-7)d= \frac{n+1}2.\]
</p>

<p>
    (2) 由 (1), $b_n= \frac2{n(n+1)}$, 则
    \[\begin{aligned}
        T_n&= 2\biggl(\frac1{1\times2}+ \frac1{2\times3}
            +\cdots +\frac1{n(n+1)}\biggr)\\
        &= \frac{2n}{1+n}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\subsubsection{利用错位相减法求数列的和}
<span id="example-"></span>
<myexample>
    <p>
    设数列 $\{a_n\}$ 的前 $n$ 项和 $S_n$ 满足 $S_n=2-a_n$.
</p>

<p>
    (1) 求 $\{a_n\}$ 的通项公式;
</p>

<p>
    (2) 若数列 $\{b_n\}$ 满足 $b_1=1$, 且 $b_{n+1} =b_n +a_n$, 
    求 $\{b_n\}$ 的通项公式;
</p>

<p>
    (3) 设 $c_n= n(3-b_n)$, 求数列 $\{c_n\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexample>
<mysolution>
    <p>
    (1) 当 $n=1$ 时, $a_1= S_1= 2-a_1$, 即 $a_1=1$. 当 $n\geqslant 2$ 时,
    \[a_n= S_n- S_{n-1}= a_{n-2}- a_n,\]
    即 $a_n= \dfrac{a_{n-1}}2$, 表明 $\{a_n\}$ 为等比数列, 公比 $q= \dfrac12$, 则
    \[a_n= a_1 q^{n-1}= \biggl(\frac12\biggr)^{n-1}.\]
</p>

<p>
    (2) 由已知, 当 $n\geqslant 2$ 时,
    \[\begin{aligned}
        b_n&= b_{n-1}+ a_{n-1}= b_{n-2}+ a_{n-2}+ a_{n-1}\\
        &= \cdots= b_1+ a_1+ a_2+\cdots a_{n-2}+ a_{n-1}\\
        &= 1+ \frac{a_1(1-q^{n-1})}{1-q}
         = 3- \biggl(\frac12\biggr)^{n-2},
    \end{aligned}\]
    与 $b_1= 1$ 相符, 故 $b_n= 3- \biggl(\frac12\biggr)^{n-2}$, $n\geqslant 1$.
</p>

<p>
    (3) 由 $2$ 知,
    \[c_n= n(3-b_n)= \frac{n}{2^{n-2}},\]
    则
    \[\begin{aligned}
        T_n
        &= \frac1{2^{-1}}+ \frac2{2^{0}}+\cdots 
            +\frac{n}{2^{n-2}}\\
        \frac12 T_n
        &= \phantom{\frac1{2^{-1}}+ {}} \frac1{2^{0}}+\cdots 
            + \frac{n-1}{2^{n-2}}+ \frac{n}{2^{n-1}},
    \end{aligned}\]
    作差,
    \[\begin{aligned}
        \frac12 T_n &= 2+ \biggl(1+\frac12+ \cdots
            + \frac1{2^{n-2}}\biggr)- \frac{n}{2^{n-1}}\\
        &= 4- \frac1{2^{n-2}}- \frac{n}{2^{n-1}}\\
        &= 4- \frac{n+2}{2^{n-1}},
    \end{aligned}\]
    所以 $T_n= 8- \frac{4(n+2)}{2^n}$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    求数列 $\Big\{\dfrac{n+1}{2^n}\Big\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexercise>
<mysolution>
    <p>
    因为
    \[\begin{aligned}
        T_n
        &= \frac2{2}+ \frac3{2^2}+\cdots \frac{n+1}{2^n}\\
            \frac12 T_n
        &= \phantom{\frac2{2}+ {}} \frac2{2^2}+\cdots 
            + \frac{n}{2^n}+ \frac{n+1}{2^{n+1}},
    \end{aligned}\]
    作差,
    \[\begin{aligned}
        \frac12 T_n 
        &= 1+ \biggl(\frac1{2^2}+ \cdots
            \frac1{2^n}\biggr)- \frac{n+1}{2^{n+1}}\\
        &= 1+ \biggl(\frac12- \frac1{2^n}\biggr)- \frac{n+1}{2^{n+1}}\\
        &= \frac32- \frac{n+3}{2^{n+1}},
    \end{aligned}\]
    所以 $T_n= 3- \frac{n+3}{2^n}$.
</p>
</mysolution>
</p>

<p>
\subsubsection{找规律}
<span id="example-"></span>
<myexample>
    <p>
    如图 \ref{fig-190626-2000} 所示, 有一个形如六边形的点阵, 它的中心是 1 个点 (算第 1 层), 第 2 层每边有 2 个点, 
    第 3 层每边有 3 个点, 依次类推.
</p>

<p>
    (1) 设第 $n$ 层的点数为 $a_n$, 求其表达式.
</p>

<p>
    (2) 如果该六边形点阵共有 169 个点, 那么它一共有多少层\,?
</p>
</myexample>
<mysolution>
    <p>
    (1) 由图可知, $a_1= 1$; 当 $n\geqslant 2$ 时, $a_n= 6(n-1)$.
</p>

<p>
    (2) 设共有 $n$ 层, 由 $\{a_n\}$ ($n\geqslant 2$) 为等差数列知,
    \[\begin{gathered}
        a_1+a_2+a_3+\cdots +a_n= 169,\\
        1+ 6+ 12+\cdots +6(n-1)= 169,\\
        1+ 3n(n-1)= 169,\quad n=8,
    \end{gathered}\]
    所以共有 $8$ 层.
</p>
</mysolution>
</p>

<p>
    \begin{figure}[htb]
    \small
    \centering
    \begin{tikzpicture}[scale=0.4]
    %%% 绕圈画
      \def\layer{5}
      \draw[fill=black] (0,0) circle (1pt);
      \foreach \h in {2,...,\layer}
         \foreach \x in {0,...,5}
         {\draw[fill=black] ({60*\x}:{\h-1}) circle (1pt);
         \foreach \m in {2,...,\h}
            {\draw ({60*\x}:{\h-1}) coordinate (A);
            \draw ({60*(\x+1)}:{\h-1}) coordinate (B);
            \draw[fill=black] ($(A)!{(\m-1)/(\h-1)}!(B)$) 
                circle (1pt);}
         }
    \end{tikzpicture}
    \caption{}\label{fig-190626-2000}
    \end{figure}
</p>

<p>
\lianxi
\begin{exercise}[s]
    根据图 \ref{fig-190626-2200} 中的 $5$ 个图形及相应点的个数的变化规律, 求第 $n$ 个图中的点数.
</p>
</myexercise>
<mysolution>
    <p>
    第 $n$ 个图中的点数为
    \[1+ n(n-1)= n^2-n+1.\]
</p>
</mysolution>
</p>

<p>
    \begin{figure}[htb]
    \small
    \centering
    \begin{tikzpicture}[scale=0.4]
      \def\fignum{5}
      \foreach \n in {1,...,\fignum}
         \foreach \m [evaluate=\m] in {1,...,\n}
         \foreach \l [evaluate=\l] in {1,...,\n}
         {\draw[fill=black] ({\n*\n*\n/12+\n*\n/2-7*\n/12},0)+({90+(\l-1)*360/\n}:{\m-1}) circle (1pt);}
    \end{tikzpicture}
    \caption{}\label{fig-190626-2200}
    \end{figure}
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    已知等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$, $a_5=5$, $S_5=15$, 求数列 $\biggl\{\dfrac1{a_na_{n+1}}\biggr\}$ 的前 $100$ 项和.
</p>
</myexercise>
<mysolution>
    <p>
    由已知,
    \[S_5= \frac{(a_1+a_5)5}2= 15,\quad a_1= 1.\]
    设公差为 $d$, 则
    \[a_5-a_1= 4d=4,\quad d=1,\]
    所以 $a_n= a_1+ (n-1)d= n$, 数列 $\biggl\{\dfrac1{a_na_{n+1}}\biggr\}= \biggl\{\dfrac1{n(n+1)}\biggr\}$ 的前 $100$ 项和为
    \[\frac1{1\times 2}+ \frac1{2\times 3}+ \cdots
    + \frac1{n(n+1)}= \frac{n}{n+1}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知正项数列 $\{a_n\}$ 满足 $a_n^2-(2n-1)a_n -2n=0$.
</p>

<p>
    (1) 求 $\{a_n\}$ 的通项公式;
</p>

<p>
    (2) 令 $b_n =\dfrac1{(n+1)a_n}$, 求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 由题意,
    \[(a_n- 2n)(a_n+ 1)= 0,\quad a_n= 2n.\]
</p>

<p>
    (2) 由 (1), $\{b_n\}= \biggl\{\dfrac1{2n(n+1)}\biggr\}$, 则 $T_n= \dfrac{2n}{n+1}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    下表中的数阵的特点是每行每列都成等差数列. 记第 $i$ 行第 $j$ 列的数为 $a_{i,j}$, 求 $a_{9,9}$, 并计算 $82$ 在表中出现的次数.
    \[\begin{array}{ccccccc}
        2 &3 &4 &5 &6 &7 & \cdots\\ 
        3 &5 &7 &9 &11 &13 & \cdots\\ 
        4 &7 &10 &13 &16 &19 & \cdots\\
        5 &9 &13 &17 &21 &25 & \cdots\\ 
        6 &11 &16 &21 &26 &31 & \cdots\\
        7 &13 &19 &25 &31 &37 & \cdots\\ 
        \vdots& \vdots& \vdots& \vdots& \vdots& \vdots& \ddots
      \end{array}\]
</p>
</myexercise>
<mysolution>
    <p>
    第 $i$ 行首项为 $a_{i,1}= i+1$, 公差为 $i$, 所以
    \[a_{i,j}= a_{i,1}+ (j-1)i= ij+1,\]
    则 $a_{9,9}= 82$. 设 $a_{i,j}=82$, 因此
    \[ij+1= 82,\quad ij=81= 3^4.\]
    因为 $i$,$j$ 均为正整数, 所以 $i=1$,$3$,$3^2$,$3^3$,$3^4$, 即 $82$ 在表中出现 $5$ 次.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    求数列 $\{3+2^n\}$ 的前 $n$ 项和 $S_n$.
</p>
</myexercise>
<mysolution>
    <p>
    分别计算常数列 $\{3\}$ 和等比数列 $\{2^n\}$ 的前 $n$ 项和可得, 
    \[S_n= 3n+ 2^{n+1}-2.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若数列 $\{a_n\}$ 的前 $n$ 项和 $S_n$ 满足 $S_n+S_m =S_{n+m}$ 且 $a_1=1$, 求 $a_{10}$.
</p>
</myexercise>
<mysolution>
    <p>
    令 $m=1$, 则 $S_n+S_1= S_{n+1}$, 即
    \[a_{n+1}= S_{n+1}- S_n= S_1= a_1= 1,\]
    所以 $a_{10}=1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知数列 $\{a_n\}$ 的首项为 $3$, $\{b_n\}$ 为等差数列, 且 $b_n =a_{n+1}-a_n$. 若 $b_3=-2$, $b_{10}=12$, 求 $a_8$.
</p>
</myexercise>
<mysolution>
    <p>
    设 $\{b_n\}$ 的公差为 $d$, 则
    \[7d= b_{10}-b_3= 14,\quad d=2,\]
    所以
    \[b_n= b_3+(n-3)d= 2n-8.\]
    再由 $b_n= a_{n+1}- a_n$ 得
    \[b_1= a_2-a_1,\quad b_2= a_3-a_2,\quad\cdots,\quad
     b_7= a_8-a_7,\]
     累加得
     \[\begin{gathered}
        b_1+b_2+\cdots +b_7= a_8-a_1,\\
        a_8= a_1+ \frac{(b_1+b_7)7}2= 3.
     \end{gathered}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若数列 $\{a_n\}$ 的通项公式为 $a_n=\dfrac1{\sqrt{n}+ \sqrt{n+1}}$, 求其前 $8$ 项和 $S_8$.
</p>
</myexercise>
<mysolution>
    <p>
    $a_n=\sqrt{n+1}- \sqrt{n}$, 则
    \[\begin{aligned}
        S_8
        &= (\sqrt2-1)+ (\sqrt3-\sqrt2)+\cdots +(\sqrt9-\sqrt8)\\
        &= \sqrt9-1= 2.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    计算 
    \[1+\dfrac1{1+2}+\dfrac1{1+2+3}+\cdots +\dfrac1{1+2+3+\cdots +n}.\]
</p>
</myexercise>
<mysolution>
    <p>
    第 $n$ 个式子的分母为 $\dfrac{(1+n)n}2$, 则和式的值为 $\dfrac{2n}{n+1}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\triangle ABC$ 的内角 $A$, $B$, $C$ 所对的边分别为 $a$, $b$, $c$.
</p>

<p>
    (1) 若 $a$, $b$, $c$ 成等差数列, 求证: $\sin A+\sin C= 2\sin(A+C)$;
</p>

<p>
    (2) 若 $a$, $b$, $c$ 成等比数列, 求 $\cos B$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 因为 $a+c= 2b$, 则由正弦定理和诱导公式,
    \[\sin A+\sin C= 2\sin B= 2\sin(A+C).\]
</p>

<p>
    (2) 因为 $b^2=ac$, 则由余弦定理和均值不等式,
    \[\begin{aligned}
        \cos B
        &= \frac{a^2+c^2- b^2}{2ac}
         = \frac12\biggl(\frac{a}c+ \frac{c}a\biggr)- \frac12\\
        &\geqslant \frac12\cdot 2- \frac12= \frac12,
    \end{aligned}\]
    等号成立当且仅当 $a=c$, 所以 $\cos B$ 的最小值为 $\dfrac12$, 对应 $B=\dfrac\pi3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    记 $S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和, $b_n$ 为数列 $\{S_n\}$ 的前 $n$ 项积, 且 $\dfrac2{S_n}+ \dfrac1{b_n}=2$.
</p>

<p>
    (1) 求证: 数列 $\{b_n\}$ 是等差数列;
</p>

<p>
    (2) 求数列 $\{a_n\}$ 的通项公式.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 当 $n\geqslant 2$ 时, $b_{n-1}S_n= b_n$, 代入已知等式并消去 $S_n$,
    \[\dfrac{2b_{n-1}}{b_n}+ \dfrac1{b_n}=2,\quad
    b_n- b_{n-1}= \frac12,\]
    表明数列 $\{b_n\}$ 是等差数列.
</p>

<p>
    (2) 由题意,
    \[a_1= S_1= b_1,\quad \dfrac2{S_1}+ \dfrac1{b_1}=2,\]
    则 $a_1= S_1= b_1= \frac32$, 所以
    \[b_n= b_1+(n-1)\frac12= \frac{n+2}2,\]
    当 $n\geqslant 2$ 时,
    \[S_n= \frac{b_n}{b_{n-1}}= \frac{n+2}{n+1},\]
    与 $S_1= \dfrac32$ 相符, 故
    \[S_n= \frac{n+2}{n+1},\quad n\geqslant 1.\]
    因此当 $n\geqslant 2$ 时,
    \[\begin{aligned}
        a_n
        &= S_n-S_{n-1}= \frac{n+2}{n+1}- \frac{n+1}{n}\\
        &= -\frac1{n(n+1)},
    \end{aligned}\]
    与 $a_1= \dfrac32$ 不符, 故
    \[a_n= \begin{cases}
        \frac32, & n=1,\\
        -\frac1{n(n+1)}, & n\geqslant 2.
    \end{cases}\]
</p>
</mysolution>