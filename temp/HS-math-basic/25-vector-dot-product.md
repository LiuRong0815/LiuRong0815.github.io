\sectioncounter{24}
</p>

<p>
\section{平面向量的数量积}
</p>

<p>
\subsection{知识梳理}
将两个向量 $\bm{a}$, $\bm{b}$ 平移到同起点, 
所夹不超过 $180^\circ$ 的角称为这两个向量的夹角, 一般记为 
$\langle\bm{a},\bm{b}\rangle$. 当 $\bm{a}\parallel\bm{b}$ 时, 
夹角 $\langle\bm{a},\bm{b}\rangle= 0^\circ$ (同向) 或 $180^\circ$ (反向).
若 $\bm{a}$, $\bm{b}$ 夹角为 $90^\circ$, 则称这两个向量垂直,
记为 $\bm{a}\perp\bm{b}$.
</p>

<p>
向量 $\bm{a}$, $\bm{b}$ 的数量积 (内积) 定义为 
\[\bm{a}\cdot\bm{b}
    = |\bm{a}||\bm{b}|\cos\langle\bm{a},\bm{b}\rangle.\]
注意定义中等号左边的点乘号不可省略. 由内积定义, 
$\bm{a}\cdot\bm{a}= |\bm{a}|^2$, 简记为 $\bm{a}^2= |\bm{a}|^2$. 
而若 $\bm{a}\perp\bm{b}$, 则 $\bm{a}\cdot\bm{b}= 0$,
反之亦然, 即 $\bm{a}\perp\bm{b}\Leftrightarrow \bm{a}\cdot\bm{b}=0$.
\mymarginpar{类似可得,
\[\begin{gathered}
    \langle\bm{a},\bm{b}\rangle\ \text{为锐角}\Leftrightarrow
        \bm{a}\cdot\bm{b}>0,\\
    \langle\bm{a},\bm{b}\rangle\ \text{为钝角}\Leftrightarrow
        \bm{a}\cdot\bm{b}< 0.
\end{gathered}\]}
</p>

<p>
向量的数量积满足如下运算律
\[\begin{gathered}
    \bm{a}\cdot\bm{b}= \bm{b}\cdot\bm{a},\quad
    k(\bm{a}\cdot\bm{b})= (k\bm{a})\cdot\bm{b},\\
    \bm{a}\cdot(\bm{b}+\bm{c})
    = \bm{a}\cdot\bm{b}+ \bm{a}\cdot\bm{c},
\end{gathered}\]
其中 $k\in\mathbb{R}$. 应注意 $\bm{a}\cdot\bm{b}\cdot\bm{c}$ 没有意义,
即数量积是两个向量的运算, 更不能写 $\bm{a}^3$. 由运算律可知,
\[|\bm{a}+\bm{b}|^2= |\bm{a}|^2+2\bm{a}\cdot\bm{b}+|\bm{b}|^2,\quad
    |\bm{a}-\bm{b}|^2= |\bm{a}|^2-2\bm{a}\cdot\bm{b}+|\bm{b}|^2,\]
两式相加得 $|\bm{a}+\bm{b}|^2+ |\bm{a}-\bm{b}|^2= 2|\bm{a}|^2+2|\bm{b}|^2$
(几何意义?).
</p>

<p>
设 $\bm{i}$, $\bm{j}$ 分别为平面直角坐标系中沿 $x$ 轴正向和 $y$ 轴正向的单位向量, 
则 $|\bm{i}|=|\bm{j}|=1$ 且 $\bm{i}\cdot\bm{j}=0$.
若 $\bm{a}=(x_1,y_1)$, $\bm{b}=(x_2,y_2)$, 则
\[\bm{a}\cdot\bm{b}
    = (x_1\bm{i}+y_1\bm{j})(x_2\bm{i}+y_2\bm{j})
    = x_1x_2+y_1y_2.\]
特别地, $|\bm{a}|^2= x_1^2+y_1^2$, 
即有向量长度公式 $|\bm{a}|= \sqrt{x_1^2+y_1^2}$. 
逆用数量积的定义可得两个向量 $\bm{a}$, $\bm{b}$ 的夹角公式
\[\cos\langle\bm{a},\bm{b}\rangle
    = \frac{\bm{a}\cdot\bm{b}}{|\bm{a}||\bm{b}|}
    = \frac{x_1x_2+y_1y_2}{\sqrt{x_1^2+y_1^2}\sqrt{x_2^2+y_2^2}}.\]
</p>

<p>
</p>

<p>
\lianxi
<myexercise>
    <p>    已知向量 $\bm{a}$ 和向量 $\bm{b}$ 的夹角为 $30^\circ$, $|\bm{a}|=2$, $|\bm{b}|=\sqrt3$, 求 $\bm{a}\cdot \bm{b}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\bm{a}\cdot\bm{b}= |\bm{a}||\bm{b}|\cos\theta= 3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知向量 $\bm{a}=(1,-1)$, $\bm{b}=(2,x)$.若 $\bm{a}\cdot\bm{b}=1$, 求 $x$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\bm{a}\cdot\bm{b}= 2-x= 1$, 则 $x=1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\bm{a}$, $\bm{b}$ 的夹角为 $120^\circ$, $|\bm{a}|=1$, $|\bm{b}|=3$, 求 $|5\bm{a}-\bm{b}|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\bm{a}\cdot\bm{b}= 1\cdot 3\cos120^\circ = -\dfrac32$, 则
    \[\begin{aligned}
        |5\bm{a}- \bm{b}|^2
        &= 25\bm{a}^2- 10\bm{a}\cdot\bm{b}+ \bm{b}^2\\
        &= 25+ 15+ 9= 49,
    \end{aligned}\]
    故 $|5\bm{a}-\bm{b}|= 7$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知向量 $\bm{a}=(x,4)$, $\bm{b}=(2,1)$. 若向量 $\bm{a}$ 与 $\bm{b}$ 的夹角为钝角, 求 $x$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $\bm{a}\cdot\bm{b}< 0$, 即 $2x+4< 0$, 解得 $x< -2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $|\bm{a}|=2$, $|\bm{b}|=4$, 且 $(\bm{a}+\bm{b})\perp\bm{a}$, 
    求 $\bm{a}$ 与 $\bm{b}$ 的夹角大小.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $(\bm{a}+\bm{b})\cdot\bm{a}= 0$, 即 $\bm{a}\cdot\bm{b}= -|\bm{a}|^2$, 而
    \[\cos\langle\bm{a},\bm{b}\rangle
        = \frac{\bm{a}\cdot \bm{b}}{|\bm{a}| |\bm{b}|}
        = -\frac{|\bm{a}|}{|\bm{b}|}
        = -\frac12,\]
    表明 $\langle\bm{a},\bm{b}\rangle= 120^\circ$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{平面向量数量积的运算}
<span id="example-"></span>
<myexample>
    <p>
    (1) 已知 $|\bm{a}|=4$, $|\bm{b}|=5$, 且 $\bm{a}$ 与 $\bm{b}$ 的夹角为 $60^\circ$, 求 $(2\bm{a}+3\bm{b})\cdot(3\bm{a}-2\bm{b})$ 的值.
</p>

<p>
    (2) 已知 $|\bm{a}|=3$, $|\bm{b}|=2$, $\bm{a}$ 与 $\bm{b}$ 的夹角为 $60^\circ$,
    $\bm{c}=3\bm{a}+5\bm{b}$, $\bm{d}=m\bm{a}-3\bm{b}$.
    当 $m$ 为何值时, $\bm{c}\parallel\bm{d}$?
    当 $m$ 为何值时, $\bm{c}\perp\bm{d}$?
</p>
</myexample>
<mysolution>
    <p>
    (1) $\bm{a}\cdot\bm{b}= 4\cdot 5\cos60^\circ= 10$, 所求式展开为
    \[6(\bm{a}^2- \bm{b}^2)+ 5\bm{a}\cdot\bm{b}= 44.\]
</p>

<p>
    (2) $\bm{c}\parallel\bm{d}\Leftrightarrow 3\cdot(-3)= 5m$, 即 $m= -\dfrac95$.
    \mymarginpar{求 $\bm{c}\parallel\bm{d}$ 对应的 $m$ 值, 只需注意 $\bm{a}$, $\bm{b}$ 不共线, 即可用平面向量基本定理.}
    $\bm{c}\perp\bm{d}$ 等价于
    \[\begin{gathered}
        (3\bm{a}+5\bm{b})(m\bm{a}-3\bm{b})=0,\\
        3m\bm{a}^2- 15\bm{b}^2+ (5m-9)\bm{a}\cdot\bm{b}= 0.
    \end{gathered}\]
    将已知条件代入,
    \[3m\cdot 9- 15\cdot 4+ (5m-9)\cdot 3\cdot 2\cos60^\circ= 0,\]
    解得 $m= \dfrac{29}{14}$.
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    已知 $\bm{a}=(-3,1)$, $\bm{b}=(1,-2)$. 若 $(-2\bm{a}+\bm{b})\perp(k\bm{a}+\bm{b})$, 求 $k$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $(-2\bm{a}+\bm{b})\cdot (k\bm{a}+\bm{b})= 0$, 即
    \[\begin{gathered}
        (7,-4)\cdot (-3k+1,k-2)= 0,\\
        7(-3k+1)- 4(k-2)= 0,
    \end{gathered}\]
    解得 $k= \dfrac35$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 设 $\overrightarrow{AB}=(2,3)$, 
    $\overrightarrow{AC}=(1,k)$, 且 $\triangle ABC$ 是直角三角形, 求 $k$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\overrightarrow{BC}= (-1,k-3)$. 若 $\overrightarrow{AB}\perp \overrightarrow{AC}$, 则
    \[\overrightarrow{AB}\cdot \overrightarrow{AC}= 0\quad
        \text{即}\quad 2+3k=0,\]
    解得 $k= -\dfrac23$. 若 $\overrightarrow{AC}\perp \overrightarrow{BC}$, 则
    \[\overrightarrow{AC}\cdot \overrightarrow{BC}= 0\quad
        \text{即}\quad -1+k(k-3)=0,\]
    解得 $k= \dfrac{3\pm\sqrt{13}}2$. 若 $\overrightarrow{AB}\perp \overrightarrow{BC}$, 则
    \[\overrightarrow{AB}\cdot \overrightarrow{BC}= 0\quad
        \text{即}\quad -2+3(k-3)=0,\]
    解得 $k= \dfrac{11}3$.
</p>

<p>
    综上所述, $k= -\dfrac23$, $\dfrac{11}3$, $\dfrac{3\pm\sqrt{13}}2$.
</p>
</mysolution>
</p>

<p>
</p>

<p>
\subsubsection{利用向量的数量积求模和夹角}
<span id="example-"></span>
<myexample>
    <p>
    已知向量 $\bm{x}=\bm{a}-\bm{b}$, $\bm{y}=2\bm{a}+\bm{b}$, 且 $|\bm{a}|=|\bm{b}|=1$, $\bm{a}\perp\bm{b}$, 求 $\bm{x}$ 与 $\bm{y}$ 的夹角的余弦值.
</p>
</myexample>
<mysolution>
    <p>
    方法一: 由题意, $\bm{a}\cdot\bm{b}= 0$, 则
    \[\begin{gathered}
        |\bm{x}|^2= \bm{a}^2+ \bm{b}^2= 2,\\
        |\bm{y}|^2= 4\bm{a}^2+ \bm{b}^2= 5,\\
        \bm{x}\cdot\bm{y}= 2\bm{a}^2- \bm{b}^2= 1,\\
    \end{gathered}\]
    所以 
    \[\cos\langle\bm{a},\bm{b}\rangle
        = \frac{\bm{x}\cdot\bm{y}}{|\bm{x}| |\bm{y}|}
        = \frac{1}{\sqrt{2}\cdot\sqrt{5}}
        = \frac{\sqrt{10}}{10}.\]
</p>

<p>
    方法二: 由已知, 不妨设 $\bm{a}$, $\bm{b}$ 分别为沿 $x$ 轴正方向和 $y$ 轴正方向的单位向量, 
    \mymarginpar{利用已知条件, 将向量放在坐标系中考虑, 有时可以减少计算量. 此思路可以一般化: 设 $\bm{a}$, $\bm{b}$ 的模长分别为 $m$, $n$, 两者夹角为 $\theta$, 则可设
    \[\bm{a}= (m,0)\quad \bm{b}= (n\cos\theta, n\sin\theta).\]}
    即设 $\bm{a}= (1,0)$, $\bm{b}= (0,1)$, 则
    \[\bm{x}= (1,-1),\quad \bm{b}= (2,1),\]
    同样可得, $\cos\langle\bm{a},\bm{b}\rangle= \dfrac{\sqrt{10}}{10}$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知 $|\overrightarrow{OA}|=1$, $|\overrightarrow{OB}|=2$, 
    $\angle AOB= \dfrac{2\pi}3$, $\overrightarrow{OC}= 2\overrightarrow{OA} + \overrightarrow{OB}$, 求 $\overrightarrow{OA}$ 与 $\overrightarrow{OC}$ 的夹角大小.
</p>
</myexercise>
<mysolution>
    <p>
    视点 $O$ 为原点, $\overrightarrow{OA}$ 沿 $x$ 轴正方向, $\overrightarrow{OB}$ 沿 $\dfrac{2\pi}3$ 角方向, 则 $\overrightarrow{OA}= (1,0)$,
    \[\overrightarrow{OB}
        = |\overrightarrow{OB}| \biggl(\cos\frac{2\pi}3, \sin\frac{2\pi}3\biggr)
        = (-1,\sqrt3),\]
    而 $\overrightarrow{OC}= (1,\sqrt3)$, 所以
    \[\cos\langle\overrightarrow{OA}, \overrightarrow{OC}\rangle
        = \frac{\overrightarrow{OA}\cdot \overrightarrow{OC}}
            {|\overrightarrow{OA}| |\overrightarrow{OC}|}
        = \frac12,\]
    表明 $\langle\overrightarrow{OA}, \overrightarrow{OC}\rangle= \dfrac\pi3$.
</p>
</mysolution>
</p>

<p>
\subsubsection{向量数量积的综合应用}
<span id="example-"></span>
<myexample>
    <p>
    如图 \ref{fig-190626-1935}, 在矩形 $ABCD$ 中, $AB=\sqrt2$, $BC=2$, 
    点 $E$ 为 $BC$ 的中点, 点 $F$ 在边 $CD$ 上. 
    若 $\overrightarrow{AB}\cdot \overrightarrow{AF}=\sqrt2$,
    求 $\overrightarrow{AE}\cdot \overrightarrow{BF}$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    以点 $A$ 为原点, $AB$ 为 $x$ 轴, $AD$ 为 $y$ 轴, 则
    \[B(\sqrt2,0),\quad D(0,2),\quad E(\sqrt2,1).\]
    设 $F(x_F,2)$, 则 $\overrightarrow{AF}= (x_F,2)$. 由  $\overrightarrow{AB}= (\sqrt2,0)$ 知
    \[\overrightarrow{AB}\cdot \overrightarrow{AF}
        =\sqrt2 x_F= \sqrt2,\]
    所以 $x_F=1$, 而
    \[\overrightarrow{AE}\cdot \overrightarrow{BF}
        = (\sqrt2,1)\cdot (x_F-\sqrt2,2)
        = \sqrt2.\]
</p>
</mysolution>
</p>

<p>
    \begin{figure}[htb]
    \small
    \centering
    \begin{tikzpicture}[scale=1.2]
      \draw (0,0) coordinate (A) node[anchor=north east] {$A$};
      \draw (1.414,0) coordinate (B) node[anchor=north west] {$B$};
      \draw (0,2) coordinate (D) node[anchor= south east] {$D$};
      \draw ($(B)+(D)$) coordinate (C) node[anchor= south west] {$C$};
      \draw (A)--(B)--(C)--(D)--(A);
</p>

<p>
      \draw ($(B)!0.5!(C)$) coordinate (E) node[right] {$E$};
      \draw ($(D)+(1,0)$) coordinate (F) node[above] {$F$};
</p>

<p>
      \draw[-{Stealth[scale=0.8]}] (A)--(B);
      \draw[-{Stealth[scale=0.8]}] (A)--(E);
      \draw[-{Stealth[scale=0.8]}] (A)--(F);
      \draw[-{Stealth[scale=0.8]}] (B)--(F);
    \end{tikzpicture}
    \caption{}\label{fig-190626-1935}
    \end{figure}
</p>

<p>
\lianxi
<myexercise>
    <p>    已知非零向量 $\bm{a}$, $\bm{b}$ 满足 $(\bm{a}-2\bm{b})\perp\bm{a}$, $(\bm{b}-2\bm{a})\perp\bm{b}$, 求向量 $\bm{a}$ 与 $\bm{b}$ 的夹角大小.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[\left\{\!\!\begin{array}{l}
        (\bm{a}-2\bm{b})\cdot \bm{a}= 0,\\
        (\bm{b}-2\bm{a})\cdot \bm{b}= 0
    \end{array}\right.\ \text{即}\ 
    \left\{\!\!\begin{array}{l}
        \bm{a}^2= 2\bm{a}\cdot\bm{b},\\
        \bm{b}^2= 2\bm{a}\cdot\bm{b},
    \end{array}\right.\]
    所以 $|\bm{a}|= |\bm{b}|= \dfrac12$, 即所求夹角为 $60^\circ$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    $\triangle ABC$ 中 $D$ 是 $BC$ 的中点, $AD=8$, $BC=20$, 
    求 $\overrightarrow{AB}\cdot \overrightarrow{AC}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 画草图, 以 $\overrightarrow{AB}$ 和 $\overrightarrow{AC}$ 为基向量, 则
    \[\left\{\!\!\begin{array}{l}
        \overrightarrow{BC}= \overrightarrow{AC}-\overrightarrow{AB},\\
        2\overrightarrow{AD}= \overrightarrow{AC}+\overrightarrow{AB},
    \end{array}\right.\ \text{即}\ 
    \left\{\!\!\begin{array}{l}
        \overrightarrow{AB}= \overrightarrow{AD}- \frac12\overrightarrow{BC},\\[6pt]
        \overrightarrow{AC}= \overrightarrow{AD}+ \frac12\overrightarrow{BC},
    \end{array}\right.\]
    所以
    \[\overrightarrow{AB}\cdot \overrightarrow{AC}
        = \overrightarrow{AD}^2- \frac14\overrightarrow{BC}^2
        = -36.\]
</p>

<p>
    方法二: 以 $\overrightarrow{DA}$, $\overrightarrow{DB}$ 为基向量, 则
    \[\left\{\!\!\begin{array}{l}
        \overrightarrow{AB}= \overrightarrow{DB}- \overrightarrow{DA},\\
        \overrightarrow{AC}= \overrightarrow{DC}- \overrightarrow{DA}
            = -\overrightarrow{DB}- \overrightarrow{DA},
    \end{array}\right.\]
    相乘并利用 $|\overrightarrow{DB}|= \dfrac12|\overrightarrow{BC}|$ 可得, 
    \[\overrightarrow{AB}\cdot \overrightarrow{AC}
        = \overrightarrow{DA}^2- \overrightarrow{DB}^2
        = -36.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
</p>

<p>
<myexercise>
    <p>    设向量 $\bm{a}$, $\bm{b}$ 满足 $|\bm{a}+\bm{b}|=\sqrt{10}$, 
    $|\bm{a}-\bm{b}|= \sqrt6$, 求 $\bm{a}\cdot\bm{b}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    利用向量恒等式,
    \[\bm{a}\cdot\bm{b}
        = \frac14(|\bm{a}+\bm{b}|^2- |\bm{a}-\bm{b}|^2)
        = 1.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设向量 $\bm{a}$, $\bm{b}$ 满足 $|\bm{a}+\bm{b}|= |\bm{a}-\bm{b}|= \sqrt3$, $|\bm{a}|= 1$, 求 $|\bm{b}|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    利用向量恒等式
    \mymarginpar{本题和上题的两个向量恒等式也有实数版本 (即将向量换成数, 两式仍成立), 均建议熟记.}
    \[|\bm{a}+\bm{b}|^2+ |\bm{a}-\bm{b}|^2= |\bm{a}|^2+ |\bm{b}|^2,\]
    将已知条件代入解得, $|\bm{b}|=\sqrt2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若单位向量 $\bm{a}$, $\bm{b}$ 的夹角为 $120^\circ$, $\bm{c}= t\bm{a}+ (1-t)\bm{b}$ 且 $\bm{b}\cdot\bm{c}=0$, 求 $t$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $\bm{b}\cdot\bm{c}=0$ 知
    \[t\bm{a}\cdot\bm{b}+ (1-t)\bm{b}^2= 0,\]
    将 $\bm{a}\cdot\bm{b}= \cos120^\circ= -\dfrac12$, $|\bm{b}|= 1$ 代入, 解得 $t= \dfrac23$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知向量 $\bm{a}=(2,1)$, $\bm{a}\cdot\bm{b}=10$, $|\bm{a}+\bm{b}|=5\sqrt2$, 求 $|\bm{b}|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    将 $|\bm{a}+\bm{b}|=5\sqrt2$ 平方,
    \[\bm{a}^2+ 2\bm{a}\cdot\bm{b}+ \bm{b}^2= 50,\]
    而 $\bm{a}^2= 5$, $\bm{a}\cdot\bm{b}=10$, 代入可知, $|\bm{b}|= 5$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    若向量 $\bm{a}$ 与 $\bm{b}$ 夹角为 $60^\circ$ 且 $\bm{a}=(2,0)$, $|\bm{b}|=1$, 求 $|\bm{a}+\bm{b}|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\bm{a}\cdot \bm{b}= 2\cdot 1\cos60^\circ= 1$, 则
    \[|\bm{a}+\bm{b}|^2= \bm{a}^2+ 2\bm{a}\cdot\bm{b}+ \bm{b}^2= 7,\]
    故 $|\bm{a}+\bm{b}|= \sqrt7$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $x\in\mathbb{R}$, 向量 $\bm{a}=(x,1)$, $\bm{b}=(3,-2)$, 且 $\bm{a}\perp\bm{b}$, 求 $x$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $x\cdot 3+ 1\cdot(-2)= 0$, 即 $x= \dfrac23$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设向量 $\bm{a}$, $\bm{b}$ 之间的夹角为 $60^\circ$ 且 $|\bm{a}|=1$, $|\bm{b}|=3$, 求 $\bm{a}\cdot(\bm{a}+\bm{b})$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\bm{a}\cdot\bm{b}= \dfrac32$, 则 
    \[\bm{a}\cdot(\bm{a}+\bm{b})
        = \bm{a}^2+ \bm{a}\cdot\bm{b}
        = \frac52.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $|\bm{a}|=1$, $|\bm{b}|=2$, 且 $\bm{a}\perp(\bm{a}-\bm{b})$, 
    求向量 $\bm{a}$, $\bm{b}$ 的夹角大小.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $\bm{a}\cdot (\bm{a}-\bm{b})= 0$, 即 $\bm{a}\cdot\bm{b}= \bm{a}^2$, 所以
    \[\cos\langle\bm{a},\bm{b}\rangle
        = \frac{\bm{a}\cdot\bm{b}}{|\bm{a}| |\bm{b}|}
        = \frac{|\bm{a}|}{|\bm{b}|}
        = \frac12,\]
    表明 $\langle\bm{a},\bm{b}\rangle= \dfrac\pi3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    向量 $\bm{a}$, $\bm{b}$ 满足 $|\bm{a}|=1$, $\bm{b}=(2,1)$, 
    且 $\lambda\bm{a}+\bm{b}=0$ ($\lambda\in\mathbb{R}$), 求 $|\lambda|$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $\bm{b}= -\lambda\bm{a}$, 则
    \[|\bm{b}|= |-\lambda\bm{a}|= |\lambda| |\bm{a}|,\]
    所以 $|\lambda|= \sqrt5$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, $\overrightarrow{AB}\cdot \overrightarrow{AC}=\tan A$, $A=\dfrac\pi6$, 求 $\triangle ABC$ 的面积.
</p>
</myexercise>
<mysolution>
    <p>
    已知等式化为
    \[|\overrightarrow{AB}| |\overrightarrow{AC}|\cos A= \tan A,
    \quad\text{即}\quad 
    |\overrightarrow{AB}| |\overrightarrow{AC}|= \frac{\sin A}{\cos^2 A},\]
    所以
    \[S_{\triangle ABC}
        = \frac12|\overrightarrow{AB}| |\overrightarrow{AC}|\sin A
        = \frac12\tan^2 A
        = \frac16.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设向量 $\bm{a}$ 与 $\bm{b}$ 的夹角为 $120^\circ$, 且 $|\bm{a}|=4$, $|\bm{b}|=2$, 求下列各式的值:
</p>

<p>
    (1) $|\bm{a}+\bm{b}|$;\qquad
    (2) $|3\bm{a}-4\bm{b}|$;\qquad
    (3) $(\bm{a}-2\bm{b})\cdot(\bm{a}+\bm{b})$.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 因为 $\bm{a}\cdot\bm{b}= -4$, 所以
    \[|\bm{a}+\bm{b}|^2= \bm{a}^2+2\bm{a}\cdot\bm{b}+\bm{b}^2= 12,\]
    故 $|\bm{a}+\bm{b}|= 2\sqrt3$.
</p>

<p>
    (2) 方法同上, 可得 $|3\bm{a}-4\bm{b}|= 16$.
</p>

<p>
    (3) 直接展开得 $\bm{a}^2- \bm{a}\cdot\bm{b}- 2\bm{b}^2= 12$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知向量 $\bm{a}=(1,0)$, $\bm{b}=(1,1)$.
</p>

<p>
    (1) 求与向量 $2\bm{a}+\bm{b}$ 同向的单位向量的坐标;
</p>

<p>
    (2) 求向量 $\bm{b}-3\bm{a}$ 与 $\bm{a}$ 的夹角的余弦值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) $2\bm{a}+\bm{b}= (3,1)$, 故所求单位向量为
    \[\frac{2\bm{a}+\bm{b}}{|2\bm{a}+\bm{b}|}
        = \biggl(\frac3{\sqrt{10}}, \frac1{\sqrt{10}}\biggr)
        = \biggl(\frac{3\sqrt{10}}{10}, \frac{\sqrt{10}}{10}\biggr).\]
</p>

<p>
    (2) $\bm{b}-3\bm{a}= (-2,1)$, 故所求夹角余弦值为
    \[\frac{(\bm{b}-3\bm{a})\cdot \bm{a}}{|\bm{b}-3\bm{a}| |\bm{a}|}
        = \frac{-2}{\sqrt5\cdot 1}
        = -\frac{2\sqrt2}5.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 已知 $\overrightarrow{AB}\cdot \overrightarrow{AC}=9$, $\overrightarrow{AB}\cdot \overrightarrow{BC}=-16$.
</p>

<p>
    (1) 求 $AB$ 的长度;\qquad
    (2) 求 $\dfrac{\sin(A-B)}{\sin C}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 已知等式化为
    \[\overrightarrow{AB}\cdot \overrightarrow{CA}= -9,\quad 
    \overrightarrow{AB}\cdot \overrightarrow{CB}= 16,\]
    后者减前者,
    \[\overrightarrow{AB}\cdot (\overrightarrow{CA}- \overrightarrow{CB})= 25,\quad\text{即}\quad
    \overrightarrow{AB}^2= 25,\]
    所以 $|\overrightarrow{AB}|= 5$, 即 $AB=5$.
</p>

<p>
    (2) 设 $AB= c$, $AC=b$, $BC=a$, 则由 (1) 知 $c=5$, 而已知等式化为 (注意后一式)
    \[cb\cos A= 9,\quad ca\cos B= 16.\]
    利用正弦定理,
    \[\begin{aligned}
        \dfrac{\sin(A-B)}{\sin C}
        &= \dfrac{\sin A\cos B- \cos A\sin B}{\sin C}
         = \frac{a\cos B- b\cos A}c\\
        &= \frac{ca\cos B- cb\cos A}{c^2}
         = \frac{7}{25}.
    \end{aligned}\]
</p>
</mysolution>