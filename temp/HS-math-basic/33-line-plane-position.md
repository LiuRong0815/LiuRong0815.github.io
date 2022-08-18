\sectioncounter{32}
</p>

<p>
\section{平面与直线的位置关系}
</p>

<p>
\subsection{知识梳理}
在立体几何中, 一般用大写英文表示点, 如点 $A$,$B$,$C$ 等; 用小写英文表示直线, 如直线 $l$,$m$,$n$ 等; 用小写希腊字母表示平面, 如平面 $\alpha$,$\beta$,$\gamma$ 等. 点 $A$ 在直线 $l$ 上记为 $A\in l$, 点 $A$ 在平面 $\alpha$ 内记为 $A\in \alpha$, 直线 $l$ 在平面 $\alpha$ 内记为 $l\subset \alpha$. 注意, 直线和平面都视为点集, 所以不能写 $l\in\alpha$.
</p>

<p>
与直线和平面相关的公理有四个, 分别为
</p>

<p>
公理 1: 如果一条直线上的两点在一个平面内, 那么这条直线上所有的点都在这个平面内.
</p>

<p>
公理 2: 如果两个平面有一个公共点, 那么它们有且只有一条通过这个点的公共直线.
</p>

<p>
公理 3: 经过不在同一条直线上的三点, 有且只有一个平面.
</p>

<p>
公理 4: 平行于同一条直线的两条直线互相平行.
\mymarginpar{公理 4 表明线线平行关系有传递性, 且与平面内的情形相同.}
</p>

<p>
</p>

<p>
直线 $a$,$b$ 的位置关系有且只有三种:
</p>

<p>
(1) 直线 $a$ 与 $b$ 相交 (图 \ref{fig:2021-0828-1110} (a)): 有且只有一个公共点, 设为点 $P$, 则 $a\cap b= P$ (不记为 $a\cap b= \{P\}$);
</p>

<p>
(2) 直线 $a$ 与 $b$ 平行 (图 \ref{fig:2021-0828-1110} (b)): 在同一个平面内但无公共点, 记为 $a\parallel b$;
</p>

<p>
(3) 直线 $a$ 与 $b$ 异面 (图 \ref{fig:2021-0828-1110} (c)): 不同在任何一个平面内.
</p>

<p>
\begin{figure}[htb]
    \small\centering
  <embed src="figs/2021-0828-1110-crop.svg">
  <embed src="figs/2021-0828-1115-crop.svg">
  <embed src="figs/2021-0828-1120-crop.svg">
    \caption{}\label{fig:2021-0828-1110}
\end{figure}
</p>

<p>
已知两条异面直线 $a$,$b$, 过空间中任一点 $O$ 作直线 $a'\parallel a$, $b'\parallel b$, 则 $a'$ 和 $b'$ 所成的角叫做异面直线 $a$, $b$ 所成的角 (或夹角) (不超过 $90^\circ$, 大小唯一). 特别地, 若两条异面直线夹角为直角, 则称其互相垂直. 两条互相垂直的异面直线 $a$, $b$, 记为 $a\perp b$.
</p>

<p>
直线 $a$ 与平面 $\alpha$ 的位置关系有且只有三种:
</p>

<p>
(1) 直线 $a$ 在平面 $\alpha$ 内 (图 \ref{fig:2021-0828-1530} (a)): 有两个公共点, 记为 $a\subset \alpha$;
</p>

<p>
(2) 直线 $a$ 与平面 $\alpha$ 相交 (图 \ref{fig:2021-0828-1530} (b)): 有且只有一个公共点, 设公共点为 $P$, 则 $a\cap \alpha= P$ (不记为 $a\cap \alpha= \{P\}$); 特例, 若直线 $a$ 与平面 $\alpha$ 内所有直线垂直, 则称 $a$ 与 $\alpha$ 垂直, 记为 $a\perp \alpha$;
</p>

<p>
(3) 直线 $a$ 与平面 $\alpha$ 平行 (图 \ref{fig:2021-0828-1530} (c)): 没有公共点, 记为 $a\parallel \alpha$.
</p>

<p>
\begin{figure}[htb]
    \small\centering
  <embed src="figs/2021-0828-1530-crop.svg">
  <embed src="figs/2021-0828-1535-crop.svg">
  <embed src="figs/2021-0828-1540-crop.svg">
    \caption{}\label{fig:2021-0828-1530}
\end{figure}
</p>

<p>
平面 $\alpha$,$\beta$ 的位置关系有且只有两种:
</p>

<p>
(1) 平面 $\alpha$,$\beta$ 平行 (图 \ref{fig:2021-0828-1550} (a)): 没有公共点, 记为 $\alpha\parallel\beta$;
</p>

<p>
(2) 平面 $\alpha$,$\beta$ 相交 (图 \ref{fig:2021-0828-1550} (b)): 有一个公共点, 则必有一条公共直线, 设为 $l$, 记为 $\alpha\cap\beta= l$.
</p>

<p>
\begin{figure}[htb]
    \small\centering
  <embed src="figs/2021-0828-1550-crop.svg">
  <embed src="figs/2021-0828-1555-crop.svg">
    \caption{}\label{fig:2021-0828-1550}
\end{figure}
</p>

<p>
设两个半平面 $\alpha$,$\beta$ 有公共棱 $l$, 则 $\alpha$,$\beta$ 和 $l$ 组成的图形称为二面角, 记为 $\alpha\text{--}l\text{--}\beta$ (图 \ref{fig:2021-0828-1650}). 有时也在面 $\alpha$,$\beta$ 内除公共棱外分别取点 $A$,$B$, 把此二面角记为 $A\text{--}l\text{--}B$. 在 $l$ 上取定一个点, 过此点在 $\alpha$,$\beta$ 内分别作 $l$ 的垂线 (射线), 两垂线所成的角为二面角的平面角. 
\mymarginpar{线线角、线面角均不超过 $90^\circ$, 面面角不超过 $180^\circ$.}
若二面角 $\alpha\text{--}l\text{--}\beta$ 的平面角为 $90^\circ$, 则称 $\alpha$,$\beta$ 垂直, 记为 $\alpha\perp \beta$.
</p>

<p>
\begin{figure}[htb]
    \small\centering
  <embed src="figs/2021-0828-1650-crop.svg">
    \caption{}\label{fig:2021-0828-1650}
\end{figure}
</p>

<p>
\lianxi
<myexercise>
    <p>    用集合符号表示“点 $P$ 在直线 $l$ 外, 直线 $l$ 在平面 $\alpha$ 内”.
</p>
</myexercise>
<mysolution>
    <p>
    $P\notin l$, $l\subset \alpha$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $OA\parallel O_1 A_1$, $OB\parallel O_1 B_1$, 判断 $\angle AOB$ 与 $\angle A_1 O_1 B_1$ 的大小关系.
</p>
</myexercise>
<mysolution>
    <p>
    相等或互补.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求正方体 $ABCD\text{--}A_1 B_1 C_1 D_1$ 中对角线 $AD_1$ 与 $BD$ 所成角的大小.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $AD_1\parallel BC_1$, 
    \mymarginpar{<center>
  <embed src="figs/2021-0828-1700-crop.svg">
    </center>}
    所以 $\angle DBC_1$ 为 $AD_1$ 与 $BD$ 所成角. 考虑 $\triangle DBC_1$ 知, $DB=BC_1=C_1D$, 所以 $\angle  DBC_1= 60^\circ$ 为所求的大小.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    判断下列四个命题是否正确:
</p>

<p>
    (1) 若 $a\perp b$, $b\perp c$, 则 $a\parallel c$;\qquad
    (2) 若 $a\parallel b$, $b\perp c$, 则 $a\perp c$;
</p>

<p>
    (3) 若 $a\perp b$, $a$ 不平行于 $c$, 则 $c$ 一定不垂直于 $b$;
</p>

<p>
    (4) 若 $a\parallel b$, $b$ 不垂直于 $c$, 则 $a$ 一定不垂直于 $c$.    
</p>
</myexercise>
<mysolution>
    <p>
    作图可知, (1)(3) 错误, (2)(4) 正确, 其中 (4) 可用反证法说明.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
</p>

<p>
\subsubsection{线面位置关系的判断}
<span id="example-"></span>
<myexample>
    <p>
    判断下列四个命题是否正确:
</p>

<p>
    (1) 若两条直线互相平行, 则这两条直线确定一个平面;
</p>

<p>
    (2) 若四点不共面, 则这四点中任意三点都不共线;
</p>

<p>
    (3) 若两条直线没有公共点, 则这两条直线是异面直线;
</p>

<p>
    (4) 两条异面直线不可能垂直于同一个平面.
</p>
</myexample>
<mysolution>
    <p>
    (1) 正确, 这是公理“不共线的三点确定一个平面”的推论.
</p>

<p>
    (2) 正确, 用反证法和上述公理可以说明.
</p>

<p>
    (3) 错误, 它们可能互相平行.
</p>

<p>
    (4) 正确, 用反证法, 如果两条直线都垂直于同一个平面, 则它们互相平行, 不是异面直线.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    若空间中四条直线 $l_1$,$l_2$,$l_3$,$l_4$ 满足 $l_1\perp l_2$, $l_2\perp l_3$, $l_3\perp l_4$, 判断下列结论是否正确:
</p>

<p>
    (1) $l_1\perp l_4$;\qquad (2) $l_1\parallel l_4$;\qquad
    (3) $l_1$ 与 $l_4$ 既不垂直也不平行; 
</p>

<p>
    (4) $l_1$ 与 $l_4$ 的位置关系不确定.
</p>
</myexercise>
<mysolution>
    <p>
    (1)(2)(3) 错误, (4) 正确, 垂直关系没有传递性.
</p>
</mysolution>
</p>

<p>
\subsubsection{求异面直线所成的角}
<span id="example-"></span>
<myexample>
    <p>
    已知正四面体 $A\text{--}BCD$ 中, $E$ 是 $AB$ 的中点, 求异面直线 $CE$ 与 $BD$ 所成角的余弦值.
</p>
</myexample>
<mysolution>
    <p>
    取 $AD$ 中点 $F$, 连接 $EF$, $CF$, 
    \mymarginpar{<center>
  <embed src="figs/2021-0828-1740-crop.svg">
    </center>}则 $EF\parallel BD$, 所以 $\angle CEF$ 为 $CE$ 与 $BD$ 所成角. 设题中正四面体的棱长为 $2a$, 则 
    \[CE=CF= \sqrt3a,\quad EF=\frac12 BD= a.\]
    由余弦定理, 
    \mymarginpar{求角的余弦值, 通常需要构造含该角的三角形, 然后利用余弦定理.}
    所求余弦值
    \[\cos\angle CEF= \frac{CE^2+EF^2- CF^2}{2CE\cdot EF}
        = \frac{\sqrt3}{6}.\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知四棱锥 $P\text{--}ABCD$ 的所有侧棱长都为 $\sqrt5$, 底面 $ABCD$ 是边长为 2 的正方形, 求 $CD$ 与 $PA$ 所成角的余弦值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $CD\parallel BA$, 所以 $\angle PAB$ 为 $CD$ 与 $PA$ 所成角. 在 $\triangle PAB$ 中, 
    \[PA=PB=\sqrt5,\quad AB=2,\]
    所以作 $AB$ 边上的高或由余弦定理均可知, $\cos\angle PAB= \dfrac{\sqrt5}{5}$.
</p>
</mysolution>
</p>

<p>
\subsubsection{线线平行与垂直的证明}
<span id="example-"></span>
<myexample>
    <p>
    如图 \ref{fig-190629-1900} 所示, 在三棱锥 $A\text{--}BCD$ 中, $E$,$F$,$G$,$H$ 分别边 $AB$,$BC$,$CD$,$DA$ 的中点. 求证:
</p>

<p>
    (1) 四边形 $EFGH$ 是平行四边形;
</p>

<p>
    (2) 若 $AC=BD$, 则四边形 $EFGH$ 是菱形;
</p>

<p>
    (3) 若 $AC\perp BD$, 则四边形 $EFGH$ 是矩形.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由中点信息知, $EF=\dfrac12 AC=HG$, $EF\parallel AC\parallel HG$, 所以四边形 $EFGH$ 是平行四边形.
</p>

<p>
    (2) 由 $EF= \dfrac12 AC= \dfrac12 BD= EH$ 知, 平行四边形 $EFGH$ 是菱形.
</p>

<p>
    (3) \mymarginpar{由 (3)(4) 的证明可知, 若 $AC\perp BD$ 且 $AC=BD$, 则四边形 $EFGH$ 是正方形.}
    由 $EF\parallel AC$, $EH\parallel BD$ 知, $EF\perp EH$, 则平行四边形 $EFGH$ 是矩形.
</p>
</mysolution>
</p>

<p>
    \begin{figure}[htb]
    \small
    \centering
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[scale=0.6]
        \draw (2,2.7,0) coordinate (A) node[above] {$A$};
        \draw (0,0,0) coordinate (B) node[left] {$B$};
        \draw (3.7,0,2.6) coordinate (C) node[below] {$C$};
        \draw (4,0,0) coordinate (D) node[right] {$D$};
        \draw ($(A)!0.5!(B)$) coordinate (E) node[anchor=south east] {$E$};
        \draw ($(C)!0.5!(B)$) coordinate (F) node[anchor=north east] {$F$};
        \draw ($(C)!0.5!(D)$) coordinate (G) node[anchor=north west] {$G$};
        \draw ($(A)!0.5!(D)$) coordinate (H) node[anchor=south west] {$H$};
</p>

<p>
        \draw (C)--(A)--(B)--(C)--(D)--(A) (E)--(F) (G)--(H);
        \draw[densely dashed] (B)--(D) (E)--(H) (F)--(G);
      \end{tikzpicture}
      \caption{}\label{fig-190629-1900}
    \end{minipage}
    \hskip 0.5cm  
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[scale=0.6]
        \draw (0,0,0) coordinate (D) node[left] {$D$};
        \draw (0,0,3) coordinate (A) node[below] {$A$};
        \draw (4,0,0) coordinate (C) node[right] {$C$};
        \draw (0,2,0) coordinate (D1) node[above] {$D_1$};
        \draw (A)++(D1) coordinate (A1) node[left] {$A_1$};
        \draw (A)++(C) coordinate (B) node[below] {$B$};
        \draw (C)++(D1) coordinate (C1) node[right] {$C_1$};
        \draw (A)++(C)++(D1) coordinate (B1) +(-0.1,-0.2) node[right] {$B_1$};
</p>

<p>
        \draw ($(A)!0.5!(B)$) coordinate (E) node[below] {$E$};
        \draw ($(C)!0.5!(B)$) coordinate (F) +(-0.2,-0.2) node[right] {$F$};
        \draw ($(A1)!0.5!(B1)$) coordinate (E1) node[below] {$E_1$};
        \draw ($(C1)!0.5!(B1)$) coordinate (F1) +(-0.2,-0.2) node[right] {$F_1$};
</p>

<p>
        \draw (A1)--(A)--(B)--(C)--(C1)--(D1)--(A1)--(C1)--(B1)--(A1) (B1)--(B) (E1)--(F1);
        \draw[densely dashed] (D1)--(D)--(A) (A)--(C) (C)--(D) (E)--(F);     
      \end{tikzpicture}
      \caption{}\label{fig-190629-1920}
    \end{minipage}
    \end{figure}
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    如果 $a$, $b$ 是异面直线, $b$, $c$ 也是异面直线, 判断直线 $a$ 与 $c$ 的位置关系.
</p>
</myexercise>
<mysolution>
    <p>
    无法确定, 相交、平行或异面均有可能.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig-190629-1920} 所示, 在长方体 $ABCD\text{--}A_1 B_1 C_1 D_1$ 中, $E$, $F$ 分别是 $AB$, $BC$ 的中点, $E_1$, $F_1$ 分别是 $A_1B_1$, $B_1C_1$ 的中点, 求证: $EF\parallel E_1 F_1$.
</p>
</myexercise>
<mysolution>
    <p>
    由中点信息可知, $EF\parallel AC\parallel A_1C_1\parallel E_1F_1$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    已知空间四点中任意三点都不共线, 过每三点作平面, 可确定几个平面?
</p>
</myexercise>
<mysolution>
    <p>
    参考四面体知, 可确定 $6$ 个平面.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在空间中, 两条直线垂直于同一条直线, 判断这两条直线的位置关系.
</p>
</myexercise>
<mysolution>
    <p>
    平行或异面 (不可能相交).
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $a$,$b\subset\alpha$, $l\cap a=A$, $l\cap b=B$, 判断直线 $l$ 与平面 $\alpha$ 的位置关系.
</p>
</myexercise>
<mysolution>
    <p>
    $l\subset \alpha$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在长方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 点 $E$,$F$ 分别为 $AA_1$ 和 $CC_1$ 的中点, 求证: $D_1E\parallel BF$.
</p>
</myexercise>
<mysolution>
    <p>
    取 $DD_1$ 的中点 $G$, 连接 $AG$, $GF$, 
    \mymarginpar{<center>
  <embed src="figs/2021-0828-2020-crop.svg">
    </center>}
    则可证四边形 $AGD_1E$,$ABFG$ 均为平行四边形, 所以 $D_1E\parallel GA\parallel BF$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig-210828-2040} 所示, 在正四面体 $A\text{--}BCD$ 中, 点 $E$ 在 $AB$ 上, $AE=2BE$, 求 $CE$ 与 $AD$ 所成角的余弦.
</p>
</myexercise>
<mysolution>
    <p>
    \mymarginpar{<center>
  <embed src="figs/2021-0828-2030-crop.svg">
    </center>}
    在 $BD$ 上取点 $F$, 使 $DF= 2BF$, 连接 $EF$,$FC$, 则 $EF\parallel AD$, $\angle CEF$ 为 $CE$ 与 $AD$ 所成角. 设正四面体 $A\text{--}BCD$ 的棱长为 $3a$, 则 
    \[BE= a,\quad BC= 3a,\quad EF=\dfrac13 AD= a,\]
    而 $\angle CBE= 60^\circ$, 所以由余弦定理, $CE=\sqrt7a$. 同理, $CF= \sqrt7a$. 考虑 $\triangle CEF$, 仍由余弦定理知, $\cos\angle CEF= \dfrac{\sqrt7}{14}$.
</p>
</mysolution>
</p>

<p>
    \begin{figure}[htb]
    \small
    \centering
    \begin{minipage}[b]{0.45\linewidth}
      \centering
  <embed src="figs/2021-0828-2040-crop.svg">
      \caption{}\label{fig-210828-2040}
    \end{minipage}
    \hskip 0.5cm  
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[scale=0.75]
        \draw (2.5,3,0) coordinate (A) node[above] {$A$};
        \draw (0,0,0) coordinate (B) node[left] {$B$};
        \draw (4,0,0) coordinate (C) node[right] {$C$};
        \draw (2,0,-1.5) coordinate (D) +(0,0.3) node[right] {$D$};
        \draw ($(A)!0.5!(B)$) coordinate (E) node[left] {$E$};
        \draw ($(C)!0.5!(B)$) coordinate (F) node[below] {$F$};
        \draw ($(C)!0.5!(D)$) coordinate (G) +(-0.2,-0.1) node[anchor=south west] {$G$};
        \draw ($(A)!0.5!(D)$) coordinate (H) node[anchor=south east] {$H$};
</p>

<p>
        \draw (C)--(A)--(B)--(C) (E)--(F);
        \draw[densely dashed] (A)--(D)--(B) (D)--(C) (E)--(H)--(G)--(F) (E)--(G) (F)--(H);  
      \end{tikzpicture}
      \caption{}\label{fig-190629-2020}
    \end{minipage}
    \end{figure}
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig-190629-2020} 所示, $E$,$F$,$G$,$H$ 分别是空间四边形 $ABCD$ 各边上的点, 且 $\dfrac{AE}{EB}= \dfrac{AH}{HD}=m$, $\dfrac{CF}{FB}= \dfrac{CG}{GD}=n$.
</p>

<p>
    (1) 求证: $E$,$F$,$G$,$H$ 四点共面.
</p>

<p>
    (2) 当 $m$, $n$ 满足什么条件时, 四边形 $EFGH$ 是平行四边形\,?
</p>
</myexercise>
<mysolution>
    <p>
    (1) 由已知比例式, $EH\parallel BD\parallel FG$, 则 $E$, $F$, $G$, $H$ 四点共面.
</p>

<p>
    (2) 只需 $EH= FG$, 此时 $m=n$.
</p>
</mysolution>