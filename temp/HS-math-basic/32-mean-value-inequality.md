\sectioncounter{31}
</p>

<p>
\section{均值不等式及其应用}
</p>

<p>
\subsection{知识梳理}
对任意的 $a,b\in\mathbb{R}$, 由差的平方公式, $a^2-2ab+b^2=(a-b)^2\geqslant 0$, 所以
\[a^2+b^2\geqslant 2ab,\ \text{即}\ 
    \frac{a^2+b^2}2\geqslant ab.\]
从推导可知, 等号成立当且仅当 (充要条件) $a=b$. 再把其中的 $a$, $b$ 分别用 $\sqrt{x}$, $\sqrt{y}$ ($x,y\geqslant0$) 代替, 可得
\[\frac{x+y}2\geqslant \sqrt{xy},\ \text{等号成立当且仅当}\ x=y.\]
上面的不等式左边是正数 $x,y$ 的算术平均值 (平均数), 右边是 $x,y$ 的几何平均值, 所以该式通常称为{\heiti 均值不等式}\index{junzhibudengshi@均值不等式}, 有时也称其为{\heiti 基本不等式}\index{jibenbudengshi@基本不等式}.
</p>

<p>
由均值不等式可以得到两个关于正数 $x$, $y$ 的简单而常用的结论:
</p>

<p>
(1) 若 $xy=L$ 为定值, 则 $x+y$ 有最小值 $2\sqrt{L}$;
</p>

<p>
(2) 若 $x+y=M$ 为定值, 则 $xy$ 有最大值 $\dfrac{M^2}4$.
</p>

<p>
如对 $x>0$, $x+\dfrac1x\geqslant 2$, 而对 $x>-1$,
\[x+\frac1{x+1}= (x+1)+\frac1{x+1}-1
    \geqslant 2-1=1.\]
使用均值不等式时, 必须检验等号成立的条件. 如对 $x>2$, 由 $x+\dfrac1x\geqslant 2$ 不能得到 $x+\dfrac1x$ 的值域为 $[2,+\infty)$. 因为此时等号成立的条件是 $x=1$, 不符合 $x>2$. 正确的解法是判断前式在 $x>2$ 时单增 (如利用导数), 所以值域为 $\Big(\dfrac52,+\infty\Big)$.
</p>

<p>
\lianxi
<myexercise>
    <p>    已知 $xy=4$ ($x>0$, $y>0$), 求 $x+y$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    $x+y\geqslant 2\sqrt{xy}= 4$, 等号成立当且仅当 $x=y=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $x, y\in(0,+\infty)$ 且 $x+y=1$, 求 $xy$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    $1= x+y\geqslant 2\sqrt{xy}$, 则 $xy\leqslant \dfrac14$, 等号成立当且仅当 $x=y= \dfrac12$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $a,b$ 为正数, 求 $\dfrac{b}a +\dfrac{a}b$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    $\dfrac{b}a +\dfrac{a}b\geqslant 2\sqrt{\dfrac{b}a\cdot \dfrac{a}b}=2$, 等号成立当且仅当 $a=b$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $x>-3$, 求 $x+\dfrac2{x+3}$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    $(x+3)+\dfrac2{x+3}\geqslant 2\sqrt2$, 等号成立当且仅当 $x= \sqrt2-3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    当函数 $y=x^2 +\dfrac9{x^2}$ 取最小值时, 求对应的 $x$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $x^2 +\dfrac9{x^2}\geqslant 2\sqrt{9}= 6$, 等号成立当且仅当 $x= \pm3$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
</p>

<p>
\subsubsection{利用均值不等式解决恒成立问题}
<span id="example-"></span>
<myexample>
    <p>
    若 $x,y>0$ 且 $\dfrac{2y}x+ \dfrac{8x}y> m^2+2m$ 恒成立, 求 $m$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>
    由 $\dfrac{2y}x+ \dfrac{8x}y\geqslant 2\sqrt{16}= 8$, 等号成立当且仅当 $2x= y$. 知
    \[8> m^2+2m,\quad m\in(-4,2).\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    若正实数 $x,y$ 满足 $x+y=2$, 且 $\dfrac1{xy}\geqslant M$ 恒成立, 求 $M$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $x+y\geqslant 2\sqrt{xy}$ 知, $2\geqslant 2\sqrt{xy}$, 所以 $xy\leqslant 1$, 等号成立当且仅当 $x= y= 1$, 则 $\dfrac1{xy}\geqslant 1$, 因此 $M$ 的最大值为 $1$.
</p>
</mysolution>
</p>

<p>
\subsubsection{利用均值不等式求最值}
<span id="example-"></span>
<myexample>
    <p>
    若正实数 $x,y$ 满足 $2x+y+6=xy$, 求 $xy$ 和 $2x+y$ 各自的最大值.
</p>
</myexample>
<mysolution>
    <p>
    由 $2x+y\geqslant 2\sqrt{2xy}$ 和已知,
    \[xy-6\geqslant 2\sqrt{2xy},\quad xy\geqslant 18,\]
    等号成立当且仅当 $2x=y= 6$, 且
    \[2x+y\geqslant 2\sqrt{2(2x+y+6)},\quad 2x+y\geqslant 12,\]
    等号成立当且仅当 $2x=y= 6$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知二次函数 $f(x)=ax^2 -4x+c$ ($x\in\mathbb{R}$) 的值域为 $[0,+\infty)$, 求 $\dfrac1c +\dfrac9a$ 的最小值.
</p>
</myexample>
<mysolution>
    <p>
    由已知, 函数 $f(x)$ 的图形与 $x$ 轴相切, 则
    \[\Delta= (-4)^2- 4ac= 0,\quad ac=4,\]
    所以
    \[\frac1c +\frac9a\geqslant 2\sqrt{\frac{9}{ac}}= 3,\]
    等号成立当且仅当 $a=9c$ 即 $a= 6$, $c= \dfrac23$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    设正数 $a,b$ 满足 $a^2+4b^2+\dfrac1{ab}= 4$, 求 $a,b$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由均值不等式,
    \mymarginpar{这里用了两次均值不等式, 所以需要写出两个等号成立的条件.}
    \[a^2+4b^2+\frac1{ab}\geqslant 4ab+ \frac1{ab}
    \geqslant 4,\]
    等号成立当且仅当 $a^2= 4b^2$ 且 $4ab= \dfrac1{ab}$, 解得 $a=1$, $b= \dfrac12$.
</p>
</mysolution>
</p>

<p>
\subsubsection{均值不等式综合题}
<span id="example-"></span>
<myexample>
    <p>
    已知在锐角 $\triangle ABC$ 中, 角 $A,B,C$ 所对的边长分别为 $a,b,c$, $(b^2 +c^2 -a^2)\tan A=\sqrt3 bc$.
</p>

<p>
    (1) 求角 $A$ 的大小;\qquad
    (2) 若 $a=2$, 求 $\triangle ABC$ 面积 $S$ 的最大值.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由已知和余弦定理,
    \[2bc\cos A\cdot \tan A= \sqrt3bc,\quad 
    \sin A= \frac{\sqrt3}2,\]
    则在锐角 $\triangle ABC$ 中, $A= 60^\circ$.
</p>

<p>
    (2) 仍由余弦定理.,
    \[\begin{aligned}
        a^2&= b^2+c^2- 2bc\cos A,\\
        4&= b^2+c^2- bc.
    \end{aligned}\]
    因为 $b^2+c^2\geqslant 2bc$, 所以
    \[4+bc\geqslant 2bc,\quad bc\leqslant 4,\]
    则
    \[S= \frac12bc\sin A= \frac{\sqrt3}{4}bc
    \leqslant \sqrt3,\]
    等号成立当且仅当 $b=c=2$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    设 $m\in\mathbb{R}$, 动直线 $l_1\colon x+my=0$ 和 $l_2\colon mx-y-m+3=0$ 分别过定点 $A,B$, $l_1$ 和 $l_2$ 交于点 $P(x,y)$, 求 $|PA|\cdot |PB|$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $A(0,0)$, $B(1,3)$ 且 $l_1\perp l_2$, 则 $\triangle PAB$ 为直角三角形, 且 $\angle P= 90^\circ$, 所以
    \mymarginpar{发现 $l_1\perp l_2$ 是解本题的关键.}
    \[|PA|^2+ |PB|^2= |AB|^2= 10.\]
    由 $|PA|^2+ |PB|^2\geqslant 2|PA|\cdot |PB|$ 知,
    \[|PA|\cdot |PB|\leqslant 5,\]
    等号成立当且仅当 $|PA|=|PB|= \sqrt5$.
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
</p>

<p>
<myexercise>
    <p>    若实数 $x,y$ 满足 $xy=1$, 求 $x^2 + 4y^2$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    $x^2 +4y^2\geqslant 4xy= 4$, 等号成立当且仅当 $x=\sqrt2$, $y=\dfrac{\sqrt2}2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $\mathrm{Rt}\,\triangle ABC$ 的面积为 $1$, 且 $C=90^\circ$, 求该三角形周长的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    设角 $A,B,C$ 的对应边长为 $a,b,c$, 则 $ab=1$, 所以
    \[\begin{gathered}
        a+b\geqslant 2\sqrt{ab}= 2,\\
        c= \sqrt{a^2+b^2}\geqslant \sqrt{2ab}= \sqrt{2},\\
        a+b+c\geqslant 2+\sqrt2,
    \end{gathered}\]
    等号成立当且仅当 $a=b=1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    半径为 $1$ 的圆内接一个矩形, 求该矩形的面积和周长各自的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    设该矩形的两个邻边长为 $a,b$. 由题意, 矩形的对角线为圆的直径, 所以
    \[\begin{gathered}
        a^2+b^2= 2^2= 4,\\
        ab\leqslant \frac{a^2+b^2}{2}= 2,
    \end{gathered}\]
    即矩形面积的最大值为 $2$, 此时 $a=b=\sqrt2$. 因为
    \[(a+b)^2= a^2+b^2+2ab\geqslant 4+4= 8,\]
    所以 $a+b\geqslant 2\sqrt2$, 即矩形周长 $2(a+b)$ 的最大值为 $4\sqrt2$, 此时仍有 $a=b=\sqrt2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设正数 $a,b$ 满足 $a^2+2ab+4b^2= 3$, 求 $ab$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $a^2+4b^2\geqslant 4ab$ 和已知,
    \[3- 2ab\geqslant 4ab,\quad ab\leqslant \frac12,\]
    等号成立当且仅当 $a^2= 4b^2$, 结合已知等式解得, $a=1$, $b=\dfrac12$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    已知 $2x+3y=2$ 且 $x,y>0$, 求 $xy$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    $2x+3y\geqslant 2\sqrt{6xy}$, 则 $xy\leqslant \dfrac16$, 等号成立当且仅当 $x=\dfrac12$, $y= \dfrac13$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $x>3$, 求 $x+\dfrac2{x-3}$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    直接凑出均值不等式的形式,
    \[x+\frac2{x-3}= (x-3)+\dfrac2{x-3}+3
    \geqslant 2\sqrt2+3,\]
    等号成立当且仅当 $x=3+\sqrt2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $x>0$, 求 $\dfrac{x}{x^2+4}$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    $\dfrac{x}{x^2+4}\leqslant \dfrac{x}{4x}= \dfrac14$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求函数 $y=x+\dfrac4x$ ($x\neq0$) 的值域.
</p>
</myexercise>
<mysolution>
    <p>
    当 $x>0$ 时, $y\geqslant 4$. 当 $x< 0$ 时, $-x>0$,
    \[-y= (-x)+ \frac4{-x}\geqslant 4,\quad y\leqslant -4,\]
    所以 $y\in (-\infty,-4]\cup [4,+\infty)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    过定点 $P(1,2)$ 的直线 $l$ 在 $x$ 正半轴与 $y$ 正半轴上的截距分别为 $a,b$, 求 $ab$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $a,b>0$ 且可设 $l\colon \dfrac{x}a+ \dfrac{y}b= 1$, 则
    \[\frac1a+ \frac2b= 1\geqslant 2\sqrt{\frac2{ab}},\quad
    ab\geqslant 8.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $a,b>0$, 若 $\sqrt3$ 是 $3^a$ 与 $3^b$ 的等比中项, 求 $\dfrac1a +\dfrac1b$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    由已知,
    \[3^a\cdot 3^b= (\sqrt3)^2= 3,\quad a+b=1.\]
    由 $a+b\geqslant 2\sqrt{ab}$ 知 $ab\leqslant \dfrac14$, 所以
    \[\frac1a+\frac1b= \frac{a+b}{ab}
    = \frac{1}{ab}\geqslant 4,\]
    等号成立当且仅当 $a=b= \frac12$.
</p>

<p>
    \varexercise 若改求 $\dfrac1a+ \dfrac2b$ 的最小值, 则由
    \[(a+b)\biggl(\frac1a+\frac2b\biggr)
    = 3+\frac{b}{a}+ \frac{2a}{b}\geqslant 3+2\sqrt2\]
    可知, $\dfrac1a+ \dfrac2b\geqslant 3+2\sqrt2$, 等号成立当且仅当 $b=\sqrt2a$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $a,b>0$, 且函数 $f(x)=4x^3 -ax^2 -2bx+2$ 在 $x=1$ 处有极值, 求 $ab$ 的最大值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $f'(x)= 12x^2- 2ax- 2b$ 且 $f'(1)= 0$, 所以
    \[12- 2a- 2b= 0,\quad a+b= 6.\]
    再由均值不等式可知 $ab\leqslant 9$, 等号成立当且仅当 $a=b=3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知二次函数 $f(x)=ax^2 +bx+c$ 的导函数 $f'(x)$ 满足 $f'(0)>0$. 若对任意实数 $x$, 有 $f(x)\geqslant 0$, 求 $\dfrac{f(1)}{f'(0)}$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    $f'(x)= 2ax+b$. 由 $f'(0)>0$ 知 $b>0$. 由 $f(x)\geqslant 0$ 恒成立知,
    \[\Delta= b^2-4ac= 0,\quad b^2= 4ac,\]
    所以
    \[\begin{aligned}
        \frac{f(1)}{f'(0)}
        &= \frac{a+b+c}{b}= \frac{a+c}{b}+ 1\\
        &\geqslant \frac{2\sqrt{ac}}{\sqrt{4ac}}+ 1= 2,
    \end{aligned}\]
    等号成立当且仅当 $a=c$, $b=2c$.
</p>
</mysolution>
