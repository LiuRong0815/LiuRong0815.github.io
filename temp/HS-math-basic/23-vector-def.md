\sectioncounter{22}
</p>

<p>
\section{平面向量的概念与线性运算}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
向量 (vector) 是既有大小又有方向的量, 作图时一般用带箭头的有向线段表示. 从点 $A$ (始端) 指向点 $B$ (末端) 的向量记为 $\overrightarrow{AB}$, 也可简单表示为 $\bm{a}$, 即 $\bm{a}=\overrightarrow{AB}$. 向量 $\overrightarrow{AB}$ 的长度也称 $\overrightarrow{AB}$ 的模, 记为 $|\overrightarrow{AB}|$. 数学中考虑的向量都是自由向量, 即不论始端在何处, 只要长度与方向分别一致, 就是相等的向量. 例如, 对平行四边形 $ABCD$, $\overrightarrow{AB}= \overrightarrow{DC}$, $\overrightarrow{AD}= \overrightarrow{BC}$. 长度为零的向量称为零向量, 记为 $\bm{0}$. 规定零向量的方向是任意的. 与 $\overrightarrow{AB}$ 大小相等但方向相反的向量 $\overrightarrow{BA}$ 也记为 $-\overrightarrow{AB}$.
方向相同或相反的两个向量是平行的, 规定零向量与任意向量平行.
</p>

<p>
两个向量的加法符合平行四边形法则, 即以 $OA$ 和 $OB$ 为邻边作平行四边形 $OACB$, 则 $\overrightarrow{OA}+\overrightarrow{OB}= \overrightarrow{OC}$. 向量的加法也可用三角形法则, 即 $\overrightarrow{AB}+\overrightarrow{BC}= \overrightarrow{AC}$. 两个向量 $\bm{a}$, $\bm{b}$ 的差 $\bm{a}-\bm{b}$ 定义为 $\bm{a}+(-\bm{b})$. 由此可知
\[\overrightarrow{OB}-\overrightarrow{OA}
    = \overrightarrow{OB}+\overrightarrow{AO}
    = \overrightarrow{AB},\]
即同起点的向量的差为由后者末端指向前者末端的向量. 此外, 还可以写出
\[\overrightarrow{AB}
    = \overrightarrow{PB}-\overrightarrow{PA}
    = \overrightarrow{QB}-\overrightarrow{QA}.\]
</p>

<p>
向量的数乘指把数与向量相乘, 如 $k\bm{a}$ 指大小为 $|k||\bm{a}|$ 
且与 $\bm{a}$ 共线的向量 (若 $k>0$ 则同向, 若 $k< 0$ 则反向).
由定义, $|k\bm{a}|=|k||\bm{a}|$. 注意, $\dfrac{\bm{a}}2= \dfrac12\bm{a}$ 也是向量的数乘. 单位向量指长度为 $1$ 的向量, 利用数乘运算可知, 
与非零向量 $\bm{a}$ 共线的单位向量为 $\pm\dfrac{\bm{a}}{|\bm{a}|}$.
向量的加法、减法和数乘运算统称为向量的线性运算.
</p>

<p>
解向量问题有时需要用到方程. 如已知 $\overrightarrow{AB}=\overrightarrow{BC}$, 则 $\overrightarrow{OB}- \overrightarrow{OA}
    = \overrightarrow{OC}- \overrightarrow{OB}$,
所以 $\overrightarrow{OB}= \dfrac12(\overrightarrow{OA}+\overrightarrow{OC})$. 此结论可一般化: 若 $m\overrightarrow{AB}=n\overrightarrow{BC}$ ($m+n\neq0$), 则 
\[\overrightarrow{OB}= \dfrac{m}{m+n}\overrightarrow{OA}
    +\dfrac{n}{m+n}\overrightarrow{OC}.\]
</p>

<p>
\lianxi
<myexercise>
    <p>    化简: $\overrightarrow{AB}+ \overrightarrow{CD}
    + \overrightarrow{DA}+ \overrightarrow{BC}$.
</p>
</myexercise>
<mysolution>
    <p>
    首尾顺次相接可得, 和为 $\bm{0}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    把平面上一切单位向量的始端放在同一点, 描述这些向量的末端所构成的图形.
</p>
</myexercise>
<mysolution>
    <p>
    单位圆周.
</p>

<p>
    \varexercise 若将“单位向量”改成“长度小于 $1$ 的向量”, 则构成单位圆内部.
</p>

<p>
    \varexercise 若将“单位向量”改成“长度大于 $1$ 且小于 $2$ 的向量”, 则构成内圆半径为 $1$, 外圆半径为 $2$ 的圆环内部.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    对于非零向量 $\bm{a}$, $\bm{b}$,“$\bm{a}\parallel\bm{b}$”
    是“$\bm{a}+\bm{b}=\bm{0}$”成立的什么条件?
</p>
</myexercise>
<mysolution>
    <p>
    必要不充分. 前者仅表示 $\bm{a}$, $\bm{b}$ 共线, 后者表示方向相反 (共线的一种特例) 且大小相等.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig:2021-0314-1600} 所示, 在正六边形 $ABCDEF$ 中, 化简: $\overrightarrow{AB}+ \overrightarrow{CD}+ \overrightarrow{EF}$.
</p>
</myexercise>
<mysolution>
    <p>
    设该正六边形中心为点 $O$, 则 $\overrightarrow{OC}= \overrightarrow{AB}$, $\overrightarrow{DO}= \overrightarrow{EF}$, 故所求的和向量为 $\bm{0}$.
</p>
</mysolution>
</p>

<p>
\begin{figure}[htb]
    \small
    \centering
    \begin{minipage}[b]{0.45\linewidth}
        \centering
  <embed src="figs/2021-0314-1600-crop.svg">
        \caption{}\label{fig:2021-0314-1600}
    \end{minipage}
    \hskip 0.5cm%
    \begin{minipage}[b]{0.45\linewidth}
        \centering
  <embed src="figs/2021-0314-1610-crop.svg">
        \caption{}\label{fig:2021-0314-1610}
    \end{minipage}
\end{figure}
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig:2021-0314-1610} 所示, 已知点 $P$ 是 $\triangle ABC$ 的边 $BC$ 上的一个四等分点 (靠近点 $B$), 记 $\overrightarrow{AB}=\bm{m}$, $\overrightarrow{AC}=\bm{n}$, 用 $\bm{m}$, $\bm{n}$ 表示 $\overrightarrow{AP}$.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\overrightarrow{PC}= 3\overrightarrow{BP}$, 所以
    \[\overrightarrow{AC}- \overrightarrow{AP}
    = 3(\overrightarrow{AP}- \overrightarrow{AB}),\]
    解得 $\overrightarrow{AP}= \dfrac34\bm{m}+ \dfrac14\bm{n}$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{向量的概念}
<span id="example-"></span>
<myexample>
    <p>
    判断下列命题是否正确, 不正确的说明理由:
</p>

<p>
    (1) 若向量 $\bm{a}$ 与 $\bm{b}$ 同向, 且 $|\bm{a}|>|\bm{b}|$, 则 $\bm{a}>\bm{b}$;
</p>

<p>
    (2) 若向量 $|\bm{a}|=|\bm{b}|$, 则 $\bm{a}$ 与 $\bm{b}$ 的长度相等且方向相同或相反;
</p>

<p>
    (3) 对于任意向量 $|\bm{a}|=|\bm{b}|$, 且 $\bm{a}$ 与 $\bm{b}$ 的方向相同, 则 $\bm{a}=\bm{b}$;
</p>

<p>
    (4) 若向量 $\overrightarrow{AB}$ 与向量 $\overrightarrow{CD}$ 是共线向量, 则 $A$, $B$, $C$, $D$ 四点共线.
</p>
</myexample>
<mysolution>
    <p>
    (1) 不正确, 向量无法比大小.
</p>

<p>
    (2) 不正确, $|\bm{a}|=|\bm{b}|$ 仅表示 $\bm{a}$ 与 $\bm{b}$ 的长度相等.
</p>

<p>
    (3) 正确, 由向量的定义可知.
</p>

<p>
    (4) 不正确, 只能得到 $AB\parallel CD$ (可能共线).
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    判断下列命题是否正确:
</p>

<p>
    (1) 若向量 $\bm{a}$ 与 $\bm{b}$ 平行, $\bm{b}$ 与 $\bm{c}$ 平行, 
    则 $\bm{a}$ 与 $\bm{c}$ 平行;
</p>

<p>
    (2) 若向量 $\bm{a}$ 与 $\bm{b}$ 相交, $\bm{b}$ 与 $\bm{c}$ 相交, 
    则 $\bm{a}$ 与 $\bm{c}$ 相交.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 不正确, 若 $\bm{b}= \bm{0}$, 则 $\bm{a}$, $\bm{c}$ 可以取任意方向.
</p>

<p>
    (2) 不正确.
</p>
</mysolution>
</p>

<p>
\subsubsection{向量的线性运算}
<span id="example-"></span>
<myexample>
    <p>
    如图 \ref{fig-190626-1845}, 在 $\triangle ABC$ 中, $D$, $E$ 分别为边 $BC$, $AC$ 的中点, $F$ 为边 $AB$ 上的点, 且 $\overrightarrow{AB} =3\overrightarrow{AF}$. 若 $\overrightarrow{AD}=x \overrightarrow{AF}+y \overrightarrow{AE}$, 求 $x+y$ 的值.
    \begin{figure}[htb]
    \small
    \centering
    \begin{tikzpicture}[scale=0.7]
      \draw (0,0) coordinate (A) node[left] {$A$};
      \draw (3,0) coordinate (B) node[right] {$B$};
      \draw (1.4,2.5) coordinate (C) node[above] {$C$};
      \draw ($(B)!0.5!(C)$) coordinate (D) node[right] {$D$};
      \draw[fill=black] ($(A)!0.5!(C)$) circle (1pt) coordinate (E) node[left] {$E$};
      \draw[fill=black] ($(A)!0.333!(B)$) circle (1pt) coordinate (F) node[below] {$F$};
      \draw (A)--(B)--(C)--(A) (A)--(D);
    \end{tikzpicture}
    \caption{}\label{fig-190626-1845}
    \end{figure}
</p>
</myexample>
<mysolution>
    <p>
    由题意, $\overrightarrow{AC}= 2\overrightarrow{AE}$,
    \[\overrightarrow{AD}
        = \frac12\overrightarrow{AB}+ \frac12\overrightarrow{AC}
        = \frac32\overrightarrow{AF}+ \overrightarrow{AE},\]
    所以 $x=\dfrac32$, $y=1$, $x+y= \dfrac32$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    在 $\triangle ABC$ 中, $\overrightarrow{BD}=2\overrightarrow{DC}$,
    若 $\overrightarrow{AD}=\lambda_1 \overrightarrow{AB}
      +\lambda_2 \overrightarrow{AC}$, 求 $\lambda_1 \lambda_2$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    已知式化为 
    \[\overrightarrow{AD}- \overrightarrow{AB}
        = 2(\overrightarrow{AC}- \overrightarrow{AD}),\]
    即 $\overrightarrow{AD}= \dfrac13\overrightarrow{AB}+ \dfrac23\overrightarrow{AC}$, 所以 $\lambda_1\lambda_2= \dfrac29$. 
</p>
</mysolution>
</p>

<p>
\subsubsection{向量共线问题}
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知非零向量 $\bm{e}_1$ 和 $\bm{e}_2$ 不共线.
</p>

<p>
    (1) 如果 $\overrightarrow{AB}=\bm{e}_1 +\bm{e}_2$,
    $\overrightarrow{BC}=2\bm{e}_1 +8\bm{e}_2$, 
    $\overrightarrow{CD}=3(\bm{e}_1 -\bm{e}_2)$, 
    判断 $A$, $B$, $D$ 三点是否共线;
</p>

<p>
    (2) 欲使 $k\bm{e}_1 +\bm{e}_2$ 与 $\bm{e}_1 +k\bm{e}_2$ 共线,
    试确定实数 $k$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    (1) $A$, $B$, $D$ 三点共线等价于 $\overrightarrow{AB}$, $\overrightarrow{BD}$ 共线, 而
    \[\overrightarrow{BD}
        = \overrightarrow{BC}+ \overrightarrow{CD}
        = 5(\bm{e}_1+ \bm{e}_2)
        = 5\overrightarrow{AB},\]
    所以 $A$, $B$, $D$ 三点共线.
</p>

<p>
    (2) 由题意, 存在 $\lambda$ 使得
    \mymarginpar{此过程可推广: 若 $x_1\bm{e}_1+ y_1\bm{e}_2$ 与 $x_2\bm{e}_1+ y_2\bm{e}_2$ 共线, 则两式对应系数成比例, 即 $x_1y_2= x_2y_1$; 反之亦然.}
    \[k\bm{e}_1+ \bm{e}_2= \lambda(\bm{e}_1 +k\bm{e}_2),\]
    所以 $k=\lambda$, $1=\lambda k$, 解得 $k=\pm1$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    如图 \ref{fig-190626-1900} 所示, 在 $\triangle ABC$ 中, $BD$ 为边 $AC$ 上的中线, $\overrightarrow{BG}=2 \overrightarrow{GD}$,
    设 $CE\parallel AG$, 若 $\overrightarrow{AE} =\dfrac15\overrightarrow{AB}
      + \lambda \overrightarrow{AC}$ ($\lambda\in\mathbb{R}$), 求 $\lambda$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $\overrightarrow{BG}=2 \overrightarrow{GD}$ 知,
    \[\overrightarrow{AG}
    = \frac13\overrightarrow{AB}+ \frac23\overrightarrow{AD}
    = \frac13\overrightarrow{AB}+ \frac13\overrightarrow{AC}),\]
    而
    \[\overrightarrow{CE}
    = \overrightarrow{AE}- \overrightarrow{AC}
    = \frac15\overrightarrow{AB}+ (\lambda-1)\overrightarrow{AC},\]
    所以由 $CE\parallel AG$ 知 $\dfrac15= \lambda- 1$, 解得 $\lambda= \dfrac65$.
</p>
</mysolution>
</p>

<p>
\begin{figure}[htb]
\small
\centering
\begin{minipage}[b]{0.45\linewidth}
    \centering
    \begin{tikzpicture}[scale=0.7]
      \draw (0,0) coordinate (A) node[below] {$A$};
      \draw (2,2.5) coordinate (B) node[above] {$B$};
      \draw (3,0) coordinate (C) node[below] {$C$};
      \draw ($(A)!0.5!(C)$) coordinate (D) node[below] {$D$};
      \draw ($(D)!0.333!(B)$) coordinate (G) node[right] {$G$};
      \draw ($0.2*(B)+1.2*(C)$) coordinate (E) node[above] {$E$};
      \draw (B)--(C)--(A)--(B)--(D) (C)--(E)--(A)--(G);
    \end{tikzpicture}
\caption{}\label{fig-190626-1900}
\end{minipage}
\hskip 0.5cm%
\begin{minipage}[b]{0.45\linewidth}
    \centering
    \begin{tikzpicture}[scale=0.7]
      \draw (0,0) coordinate (O) node[below] {$O$};
      \draw (3,0) coordinate (A) node[below] {$A$};
      \draw (-0.6,1.8) coordinate (P) node[left] {$P$};
      \draw ($(P)!0.25!(A)$) coordinate (B) node[above] {$B$};
      \draw (A)--(O)--(P) (P)--(A) (O)--(B);
    \end{tikzpicture}
\caption{}\label{fig-190626-1905}
\end{minipage}
\end{figure}
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    化简: $\overrightarrow{OP}- \overrightarrow{QP}+ 
    \overrightarrow{MS}- \overrightarrow{MQ}$.
</p>
</myexercise>
<mysolution>
    <p>
    已知式化为 $\overrightarrow{OP}+ \overrightarrow{PQ}+ 
    \overrightarrow{MS}+ \overrightarrow{QM}= \overrightarrow{OS}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在平行四边形 $ABCD$ 中, 对角线 $AC$ 与 $BD$ 交于点 $O$, $\overrightarrow{AB}+ \overrightarrow{AD}= \lambda\overrightarrow{AO}$, 求 $\lambda$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    作草图可知, $\overrightarrow{AB}+ \overrightarrow{AD}= \overrightarrow{AC}= 2\overrightarrow{AO}$, 即 $\lambda=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig-190626-1905} 所示, $\overrightarrow{AP}= \dfrac43 \overrightarrow{AB}$, 用 $\overrightarrow{OA}$, $\overrightarrow{OB}$ 表示 $\overrightarrow{OP}$.
</p>
</myexercise>
<mysolution>
    <p>
    已知等式化为
    \[\overrightarrow{OP}- \overrightarrow{OA}
    = \dfrac43\overrightarrow{OB}- \overrightarrow{OA}),\]
    解得 $\overrightarrow{OP}
    = -\dfrac13(\overrightarrow{OA}+ \dfrac43\overrightarrow{OB}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设点 $D$, $E$ 分别在 $\triangle ABC$ 的边 $AB$, $BC$ 上, $AD=\dfrac12 AB$, $BE=\dfrac23 BC$. 用 $\overrightarrow{AB}$ 和 $\overrightarrow{AC}$ 表示 $\overrightarrow{DE}$.
</p>
</myexercise>
<mysolution>
    <p>
    画草图并将点 $A$ 视为原点可知,
    \[\begin{aligned}
        \overrightarrow{DE}
        &= \overrightarrow{AE}- \overrightarrow{AD}
         = \frac13\overrightarrow{AB}+ \frac23\overrightarrow{AC}- \frac12\overrightarrow{AB}\\
        &= -\frac16\overrightarrow{AB}+ \frac23\overrightarrow{AC}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    在 $\triangle ABC$ 中, $D$ 是 $BC$ 的中点, 用 $\overrightarrow{AB}$, $\overrightarrow{AD}$ 表示 $\overrightarrow{AC}$.
</p>
</myexercise>
<mysolution>
    <p>
    由 $\overrightarrow{AD}= \dfrac12(\overrightarrow{AB}+ \overrightarrow{AC})$ 知 $\overrightarrow{AC}= 2\overrightarrow{AD}- \overrightarrow{AB}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    四边形 $ABCD$ 是平行四边形, $O$ 是对角线的交点, 化简: $\overrightarrow{DO}+ \overrightarrow{AO}$.
</p>
</myexercise>
<mysolution>
    <p>
    利用 $\overrightarrow{AO}= \overrightarrow{OC}$ 可将原式化为 $\overrightarrow{DC}$; 或利用 $\overrightarrow{DO}= \overrightarrow{OB}$ 可将原式化为 $\overrightarrow{AB}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, $\overrightarrow{AC}=\bm{a}$, 
    $\overrightarrow{BC}=\bm{b}$, 用 $\bm{a}$, $\bm{b}$ 
    表示 $\overrightarrow{BA}$.
</p>
</myexercise>
<mysolution>
    <p>
    $\overrightarrow{BA}= \overrightarrow{BC}+ \overrightarrow{CA}
    = \bm{b}- \bm{a}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在边长为 $1$ 的正方形 $ABCD$ 中, 设 $\overrightarrow{AB}= \bm{a}$, $\overrightarrow{BC}= \bm{b}$, $\overrightarrow{AC}= \bm{c}$, 求 $\bm{a}+ \bm{b}+ \bm{c}$, $\bm{a}+ \bm{c}- \bm{b}$, $\bm{c}- \bm{a}- \bm{b}$ 的长度.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\overrightarrow{AB}+ \overrightarrow{BC}= \overrightarrow{AC}$, 即 $\bm{a}+\bm{b}= \bm{c}$, 所以 
    \[\begin{aligned}
        |\bm{a}+ \bm{b}+ \bm{c}|
        &= |2\bm{c}|= 2\sqrt2,\\
        |\bm{a}+ \bm{c}- \bm{b}|
        &= |2\bm{a}|= 2,\\
        |\bm{c}- \bm{a}- \bm{b}|
        &= |\bm{0}|= 0.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设点 $O$, $A$, $B$, $P$ 为平面内四点, $2\overrightarrow{OA}= 2\overrightarrow{OA}+ \overrightarrow{BA}$, 判断点 $P$ 与线段 $AB$ 的位置关系.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[2(\overrightarrow{OP}- \overrightarrow{OA})
    = \overrightarrow{BA},\quad\text{即}\quad
    2\overrightarrow{AP}= \overrightarrow{BA},\]
    所以点 $A$, $B$, $P$ 共线, 且点 $P$ 在线段 $AB$ 的反向延长线上.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $O$ 是 $\triangle ABC$ 所在平面内一点, $D$ 为 $BC$ 边的中点,
    且 $2\overrightarrow{OA}+ \overrightarrow{OB}+ \overrightarrow{OC}=\bm{0}$, 判断 $\overrightarrow{AO}$ 与 $\overrightarrow{OD}$ 的关系.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\overrightarrow{OB}+ \overrightarrow{OC}= 2\overrightarrow{OD}$, 所以
    \[2\overrightarrow{OA}+ 2\overrightarrow{OD}= \bm{0}
    \quad\text{即}\quad \overrightarrow{AO}= \overrightarrow{OD}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\bm{e}_1$, $\bm{e}_2$ 是平面内两个不共线的向量, $\bm{a}=3\bm{e}_1 -2\bm{e}_2$,
    $\bm{b}=-2\bm{e}_1 +\bm{e}_2$, $\bm{c} =7\bm{e}_1 -4\bm{e}_2$, 
    用 $\bm{a}$, $\bm{b}$ 表示 $\bm{c}$.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由
    \[\left\{\!\!\begin{array}{l}
        \bm{a}=3\bm{e}_1 -2\bm{e}_2,\\
        \bm{b}=-2\bm{e}_1 +\bm{e}_2
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        \bm{e}_1= -\bm{a}- 2\bm{b},\\
        \bm{e}_2= -2\bm{a}- 3\bm{b},
    \end{array}\right.\]
    代入 $\bm{c}$ 的式子知, $\bm{c}= \bm{a}-2\bm{b}$.
</p>

<p>
    方法二: 设 $\bm{c}= m\bm{a}+ n\bm{b}$, 将已知条件代入,
    \[\begin{aligned}
        7\bm{e}_1 -4\bm{e}_2
        &= m(3\bm{e}_1 -2\bm{e}_2)- n(-2\bm{e}_1 +\bm{e}_2)\\
        &= (3m-2n)\bm{e}_1+ (n-2m)\bm{e}_2,
    \end{aligned}\]
    所以
    \[\left\{\!\!\begin{array}{l}
        3m-2n= 7,\\
        n-2m= -4,
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        m=1,\\
        n=-2,
    \end{array}\right.\]
    答案同上.
</p>
</mysolution>