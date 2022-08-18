\sectioncounter{20}
</p>

<p>
\section{正弦定理与解三角形}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
设 $\triangle ABC$ 中, 角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 则由三角形面积公式和任意角正弦的定义可得三角形面积定理 (高中常用):
\[S= \frac{1}{2}ab\sin C=\frac{1}{2}bc\sin A=\frac{1}{2}ca\sin B.\]
如图 \ref{fig:2021-0228-1520} 所示, 作 $AB$ 边上的高, 考虑 $\mathrm{Rt}\triangle ACD$ 可知
\[\frac{CD}{CA}= \sin A= \sin(\pi-A),\]
所以 $CD= b\sin A$, 且
\[S_{\triangle ABC}= \frac12 AB\cdot CD
    = \frac12 bc\sin A.\]
同理可得另外两个公式.
</p>

<p>
\begin{figure}[hb]
    \small\centering
  <embed src="figs/2021-0228-1240-crop.svg">
  <embed src="figs/2021-0228-1520-crop.svg">
    \caption{}\label{fig:2021-0228-1520}
\end{figure}
</p>

<p>
将三角形面积定理换一种写法就得到正弦定理: 
\[\frac{a}{\sin A}= \frac{b}{\sin B}= \frac{c}{\sin C},\]
作 $\triangle ABC$ 外接圆, 用纯几何法可证明 $\dfrac{a}{\sin A}= 2R$, 其中常数 $R$ 表示外接圆半径. 应用时也常写 $a= 2R\sin A$, 以及
\[\frac{\sin A}a= \frac{\sin B}b= \frac{\sin C}c.\]
有些关于 $a$, $b$ 或 $\sin A$, $\sin B$ 的式子可以利用正弦定理互相转化, 如
\[\sin^2 A= \sin^2 B\Leftrightarrow a\sin A= b\sin B
    \Leftrightarrow a^2=b^2.\]
</p>

<p>
用纯几何法或正弦定理可以证明: 在三角形中, 大边对大角, 大角对大边. 有些解三角形的题会求得多个解, 可以考虑用前述结论排除不合题意的解. 在解题时, 有时也由 $A+ B+ C= \pi$ 得
\[\sin(A+ B)= \sin C,\quad \sin\frac{A+B}{2}= \cos\frac{C}{2},\]
以化简已知的式子 (这类式子可以直接使用).
</p>

<p>
\lianxi
<myexercise>
    <p>    设锐角三角形 $ABC$ 中 $a=2b\sin A$, 求角 $B$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    $\sin A= 2\sin B\sin A$, 即 $\sin B= \dfrac12$. 由 $B$ 为锐角知, $B=\dfrac\pi6$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中 $A=60^\circ$, $a=\sqrt3$, 求 $\dfrac{a+b+c}{\sin A+ \sin B+ \sin C}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    设 $R$ 为 $\triangle ABC$ 外接圆的半径, 则
    \[a= 2R\sin A,\quad b=2R\sin B,\quad c=2R\sin C,\]
    由此可知所求式子可化为 $2R$, 即 $\dfrac{a}{\sin A}= \dfrac{\sqrt3}{\sin 60^\circ}= 2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 若 $a=2$, $b=3$, $C=\dfrac\pi6$, 
    求 $\triangle ABC$ 的面积.
</p>
</myexercise>
<mysolution>
    <p>
    $S= \dfrac12 ab\sin C= \dfrac32$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 已知 $a=5\sqrt2$, $c=10$, $A=30^\circ$, 求角 $B$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由 $\dfrac{a}{\sin A}= \dfrac{c}{\sin C}$ 知 $\sin C= \dfrac{\sqrt2}{2}$, 则 $C=45^\circ$ 或 $135^\circ$, 而 $B=105^\circ$ 或 $15^\circ$.
</p>

<p>
    方法二: 如图 \ref{fig:2021-0310-1940} 所示, 
    \mymarginpar{用作图法解题时, 应先作出已知角所在的直角三角形, 且其斜边为已知边. 以此为基础, 可确定原三角形的边角信息.}
    作角 $A$ 及边 $AB$, 而 $BD\perp AC$, 可知 $BD= c\sin A= 5$. 由 $BC= a= 5\sqrt2$ 得 $\angle CBD= 45^\circ$, 而 $\angle ABD= 60^\circ$, 所以
    \[\angle ABC= \angle ABD\pm \angle CBD= 105^\circ\ 
        \text{或}\ 15^\circ.\]
</p>

<p>
    \begin{figure}[hb]
        \small\centering
  <embed src="figs/2021-0310-1940-crop.svg">
        \caption{}\label{fig:2021-0310-1940}
    \end{figure}
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 若 $\dfrac{a}{\cos A}= \dfrac{b}{\cos B} 
       = \dfrac{c}{\cos C}$, 确定 $\triangle ABC$ 的形状.
</p>
</myexercise>
<mysolution>
    <p>
    由正弦定理, 已知式化为
    \[\dfrac{\sin A}{\cos A}= \dfrac{\sin B}{\cos B}
        = \dfrac{\sin C}{\cos C},\quad\text{即}\quad
        \tan A= \tan B= \tan C.\]
    由 $A$, $B$, $C\in (0,\pi)$ 知, $A=B=C= \dfrac\pi3$, 故 $\triangle ABC$ 为等边三角形.  
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{正弦定理的直接应用}
<span id="example-"></span>
<myexample>
    <p>
    在 $\triangle ABC$ 中, 已知 $a=3$, $b=2\sqrt6$, $B=2A$.
</p>

<p>
    (1) 求 $\cos A$ 的值;\qquad  (2) 求 $c$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由 $\dfrac{a}{\sin A}= \dfrac{b}{\sin B}$ 得 $\dfrac{2}{\sin A}= \dfrac{2\sqrt6}{\sin 2A}$, 解得 $\cos A= \dfrac{\sqrt6}{3}$.
</p>

<p>
    (2) 由 (1) 知,  $\sin A= \dfrac{\sqrt3}{3}$, 
    \mymarginpar{此处已知 $\sin B$ 求 $\cos B$ 时, 应计算 $\cos 2A$, 而不用 $\cos^2 B+\sin^2 B=1$, 以避开正负号的讨论.}
    所以利用二倍角公式, $\sin 2A= \dfrac{2\sqrt2}{3}$, $\cos 2A= \dfrac13$. 由 $A+B+C= \pi$ 可得 
    \[\sin C= \sin(A+B)= \sin A\cos B+ \cos A\sin B
        = \dfrac{5\sqrt3}{9},\]
    而 $c= \dfrac{a}{\sin A}\sin C= 5$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    在 $\triangle ABC$ 中 $b\cos C+c\cos B=2b$, 求 $\dfrac{a}{b}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由正弦定理, 
    \mymarginpar{大部分解三角形的题都可以分别用正弦定理和余弦定理求解, 但计算量一般有差异. 建议提前预估计算量, 然后选择合适的定理.}
    已知式子化为
    \[\sin B\cos C+\sin C\cos B= 2\sin B,\]
    即 $\sin(B+C)= 2\sin B$. 再由 $A+B+C= \pi$ 知 $\sin A= 2\sin B$, 故
    \[\dfrac{a}{b}= \dfrac{\sin A}{\sin B}= 2.\]
</p>

<p>
    方法二: 由余弦定理, 已知式化为
    \[b\cdot \frac{a^2+b^2-c^2}{2ab}+ 
        c\cdot \frac{a^2+c^2-b^2}{2ac}= 2b,\]
    整理得 $2a^2=4ab$, 即 $\dfrac{a}{b}= 2$.
</p>
</mysolution>
</p>

<p>
\subsubsection{利用正弦定理判断三角形的形状}
<span id="example-"></span>
<myexample>
    <p>
    若 $a\cos A=b\cos B$, 判断 $\triangle ABC$ 的形状.
</p>
</myexample>
<mysolution>
    <p>
    方法一: 由正弦定理, 已知式化为
    \[\sin A\cos A= \sin B\cos B,\quad\text{即}\quad
        \sin 2A= \sin 2B,\]
    所以 $2A=2B$ 或 $2A+2B=\pi$, 整理得 $A=B$ 或 $A+B=\dfrac\pi2$, 故 $\triangle ABC$ 为等腰三角形或直角三角形.
</p>

<p>
    方法二: 由余弦定理, 已知式化为
    \[a\cdot \frac{b^2+c^2-a^2}{2bc}
        = b\cdot \frac{a^2+c^2-b^2}{2ac},\]
    整理得 $(a^4-b^4)+ (b^2c^2-a^2c^2)= 0$, 再因式分解,
    \[(a^2-b^2)(a^2+b^2- c^2)= 0,\]
    所以 $a^2=b^2$ 或 $a^2+b^2= c^2$, 结论同上.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    若 $\triangle ABC$ 中 $b\cos C+c\cos B=a\sin A$, 确定 $\triangle ABC$ 的形状.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由正弦定理和 $A+B+C=\pi$, 已知式化为 $\sin A= \sin^2 A$, 所以 $\sin A=1$ 即 $A=\dfrac\pi2$, 说明 $\triangle ABC$ 为直角三角形.
</p>

<p>
    方法二: 由余弦定理, 
    \mymarginpar{结论 $b\cos C+c\cos B= a$ 也可由作图得到.}
    已知式左边可化为 $a$, 可知 $\sin A=1$, 结论同上.
</p>
</mysolution>
</p>

<p>
\subsubsection{正弦定理及面积公式的综合应用}
<span id="example-"></span>
<myexample>
    <p>
    已知 $a$, $b$, $c$ 分别为 $\triangle ABC$ 的三个内角 $A$, $B$, $C$ 的对边, 向量 $\bm{m}=(\sin A,1)$, $\bm{n}=(\cos A, \sqrt3)$, 且 $\bm{m}\parallel \bm{n}$.
</p>

<p>
    (1) 求角 $A$ 的大小;\qquad
    (2) 若 $a=2$, $b=2\sqrt2$, 求 $\triangle ABC$ 的面积.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由 $\bm{m}\parallel \bm{n}$ 知
    \[\sin A\cdot \sqrt3= 1\cdot\cos A,\quad\text{即}\quad
        \tan A= \dfrac{\sqrt3}{3},\]
    所以 $A=\dfrac\pi6$.
</p>

<p>
    (2) 方法一: 由正弦定理求得 $\sin B= \dfrac{\sqrt2}{2}$, 所以 $B= \dfrac\pi4$ 或 $\dfrac{3\pi}{4}$. 
</p>

<p>
    若 $B= \dfrac\pi4$, 则 $C= \dfrac{7\pi}{12}$,
    \[\sin C= \sin\Bigl(\frac\pi3+ \frac\pi4\Bigr)
        = \frac{\sqrt6+\sqrt2}{4},\]
    则 $S_{\triangle ABC}= \dfrac12 ab\sin C= \sqrt3+1$.
</p>

<p>
    若 $B= \dfrac{3\pi}{4}$, 则 $C= \dfrac{\pi}{12}$,
    \[\sin C= \sin\Bigl(\frac\pi3- \frac\pi4\Bigr)
        = \frac{\sqrt6-\sqrt2}{4},\]
    则 $S_{\triangle ABC}= \dfrac12 ab\sin C= \sqrt3-1$.
</p>

<p>
    方法二: 如图 \ref{fig:2021-0310-2200} 所示, 作角 $A$ 及边 $AC$, 而 $CD\perp AB$, 可知 
    \[CD= b\sin A= \sqrt2,\quad AD= b\cos A= \sqrt6.\]
    由 $BC= a= 2$ 知 $BD=2$, 所以
    \[AB= AC\pm BD= \sqrt6\pm 2.\]
    因此 $S_{\triangle ABC}= \dfrac12 AB\cdot BD= \sqrt3\pm1$.
</p>

<p>
    \begin{figure}[hb]
        \small\centering
  <embed src="figs/2021-0310-2200-crop.svg">
        \caption{}\label{fig:2021-0310-2200}
    \end{figure}
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    在 $\triangle ABC$ 中 $c\cos B+b\cos C=4a\cos A$.
</p>

<p>
    (1) 求 $\cos A$ 的值;
</p>

<p>
    (2) 若 $\triangle ABC$ 的面积是 $\sqrt{15}$, 求 $\overrightarrow{AB}\cdot\overrightarrow{AC}$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 方法一: 由正弦定理, 已知式化为
    \[\sin(B+C)= 4\sin A\cos A,\quad\text{即}\quad
        \cos A= \frac14.\]
</p>

<p>
    方法二: 由余弦定理, 
    \mymarginpar{此处无需变换 $\cos A$.}
    已知式化为
    \[\frac{2a^2}{2a}= 4a\cos A,\quad\text{仍有}\quad
    \cos A= \frac14.\]
</p>

<p>
    (2) 由已知, 
    \[S_{\triangle ABC}= \dfrac12 bc\sin A=\sqrt{15},\quad
        \sin A= \frac{\sqrt{15}}{4},\]
    所以 $bc=8$,
    \[\overrightarrow{AB}\cdot\overrightarrow{AC}
        = cb\cos A= 2.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    在 $\triangle ABC$ 中, 已知 $b=4$, $c=8$, $B=30^\circ$, 求 $a$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由正弦定理可知 $\sin C=1$, 
    \mymarginpar{此题可以解出 $A=60^\circ$, 再用正弦定理; 或用作图法.}
    即 $C=90^\circ$, 所以 $\triangle ABC$ 为直角三角形, 且 $c$ 为斜边, 故 $a=4\sqrt3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在锐角三角形 $ABC$ 中 $2a\sin B=\sqrt3 b$, 求角 $A$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    由正弦定理可知 $\sin A= \dfrac{\sqrt3}{2}$, 而 $A$ 为锐角, 所以 $A= \dfrac\pi3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\dfrac{\sin A}a= \dfrac{\cos B}b= \dfrac{\cos C}c$, 
    确定 $\triangle ABC$ 的形状.
</p>
</myexercise>
<mysolution>
    <p>
    已知式化为
    \[\dfrac{\sin A}{\sin A}= \dfrac{\cos B}{\sin B}
        = \dfrac{\cos C}{\sin C},\quad\text{即}\quad
        1= \tan B= \tan C,\]
    所以 $B=C=\dfrac\pi4$, $A=\dfrac\pi2$, 即 $\triangle ABC$ 为等腰直角三形.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, $A=60^\circ$, $AC=4$, $BC=2\sqrt3$, 
    求 $\triangle ABC$ 的面积.
</p>
</myexercise>
<mysolution>
    <p>
    由正弦定理可知 $\sin B= 1$, 即 $B=90^\circ$, 容易求得 $\triangle ABC$ 的面积为 $2\sqrt3$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    在 $\triangle ABC$ 中, $a=3$, $b=5$, $\sin A=\dfrac13$, 
    求 $\sin B$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\sin B= \sin A\cdot \dfrac{b}{a}= \dfrac59$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, $BC=\sqrt3$, $AC=\sqrt2$, $A=\dfrac\pi3$, 
    求角 $B$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    由 $\dfrac{BC}{\sin A}= \dfrac{AC}{\sin B}$ 
    \mymarginpar{解三角形时, 需要检验所得答案是否合题意, 即检验是否存在相应的三角形. 本题也可由 $BC>AC$ 知 $A>B$, 从而排除一个解.}
    知 $\sin B= \dfrac{\sqrt2}{2}$, 所以 $B= \dfrac\pi4$ 或 $\dfrac{3\pi}{4}$. 由 $A= \dfrac\pi3$ 和 $A+B+C=\pi$ 知, $B= \dfrac\pi4$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中, 若 $\tan A=\dfrac13$, $C=150^\circ$, $BC=1$, 求 $AB$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\sin A= \dfrac1{\sqrt{10}}$, $\sin C= \dfrac12$, 所以由 $\dfrac{AB}{\sin C}= \dfrac{BC}{\sin A}$ 知 $AB= \dfrac{\sqrt{10}}{2}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\triangle ABC$ 中, 内角 $A$, $B$, $C$ 所对的边长分别为 
    $a$, $b$, $c$, $a\sin B\cos C+c\sin B\cos A= \dfrac12 b$,
    且 $a>b$, 求角 $B$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由正弦定理, 已知等式化为
    \[\begin{gathered}
        \sin A\sin B\cos C+ \sin C\sin B\cos A= \dfrac12 \sin B,\\
        \sin(A+C)= \dfrac12,\quad\text{即}\quad
        \sin B=\frac12,
    \end{gathered}\]
    所以 $B=\dfrac\pi6$ 或 $\dfrac{5\pi}{6}$. 由 $a>b$ 知 $A>B$, 所以 $B< \dfrac\pi2$, 即 $B= \dfrac\pi6$.
</p>

<p>
    方法二: 由余弦定理, 已知等式化为
    \[\sin B\cdot \frac{2b^2}{2b}= \frac12b,\quad\text{即}\quad
        \sin B=\frac12,\]
    同理可得 $B= \dfrac\pi6$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\triangle ABC$ 中 $B=2A$, $a=1$, $b=\sqrt3$, 求 $c$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由 $\dfrac{a}{\sin A}= \dfrac{b}{\sin B}$ 得
    \[\frac1{\sin A}= \frac{\sqrt3}{\sin 2A},\quad\text{即}\quad
        \cos A= \dfrac{\sqrt3}{2},\]
    所以 $A=\dfrac\pi6$, $B=\dfrac\pi3$, 而 $C=\dfrac\pi2$, 即 $\triangle ABC$ 是以 $c$ 为斜边的直角三角形, 故 $c=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\triangle ABC$ 中 $A= \dfrac\pi3$, $b=2a\cos B$, $c=1$, 
    求 $\triangle ABC$ 的面积.
</p>
</myexercise>
<mysolution>
    <p>
    由正弦定理, $b=2a\cos B$ 化为
    \[\sin B= 2\sin A\cos B,\quad\text{即}\quad
        \tan B= \sqrt3,\]
    所以 $B= \dfrac\pi3$, 而 $C=\dfrac\pi3$, 
    \mymarginpar{边长为 $a$ 的等边三角形的面积为 $\dfrac{\sqrt3}{4}a^2$, 此结论可以直接使用.}
    表明 $\triangle ABC$ 为等边三角形. 故由三角形面积定理, $S_{\triangle ABC}= \dfrac{\sqrt3}{4}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\triangle ABC$ 中 $3a\cos C=2c\cos A$, $\tan A=\dfrac13$, 求角 $B$ 的大小.
</p>
</myexercise>
<mysolution>
    <p>
    由正弦定理, 
    \mymarginpar{此题不宜用余弦定理求解, 因为所得的边的关系不便于继续应用条件 $\tan A= \dfrac13$.}
    $3a\cos C=2c\cos A$ 化为
    \[3\sin A\cos C= 2\sin C\cos A,\]
    即 $\dfrac32\tan A= \tan C$, 故 $\tan C= \dfrac12$. 而
    \[\tan(A+C)= \frac{\tan A+\tan C}{1- \tan A\tan C}= 1,\]
    表明 $A+C= \dfrac\pi4$, 因此 $B= \dfrac{3\pi}4$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在 $\triangle ABC$ 中 $c=-3b\cos A$, $\tan C=\dfrac34$.
</p>

<p>
    (1) 求 $\tan B$ 的值;\qquad
    (2) 若 $c=2$, 求 $\triangle ABC$ 的面积.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 由正弦定理, $c=-3b\cos A$ 化为 $\sin C= -\sin B\cos A$, 而
    \[\sin C= \sin(A+B)= \sin A\cos B+\cos A\sin B,\]
    所以 $-4\sin B\cos A= \sin A\cos B$, 即 $\tan  A= -4\tan B$. 因为
    \[\tan C= \tan(\pi-(A+B))= \dfrac34,\]
    所以
    \[\frac{-4\tan B+\tan B}{1+ 4\tan^2 B}= -\frac34,\quad
        \text{解得}\quad \tan B= \frac12.\]
</p>

<p>
    (2) 由 (1) 知, $\sin B= \dfrac1{\sqrt5}$, $\tan A= -2$, $\sin A= \dfrac2{\sqrt5}$. 而 $\sin C=\frac35$, 故
    \[\begin{gathered}
        a= \sin A\cdot \frac{c}{\sin C}= \frac{4\sqrt5}{3},\\
        S_{\triangle ABC}= \frac12 ac\sin B= \frac43.
    \end{gathered}\]
</p>
</mysolution>