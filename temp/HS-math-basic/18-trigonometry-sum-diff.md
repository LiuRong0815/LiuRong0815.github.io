\sectioncounter{17}
\section{和角、差角的三角函数}
</p>

<p>
\subsection{知识梳理}
利用距离公式可以推出两角和的余弦公式
\mymarginpar{该公式也可利用向量内积运算推出: 在图 \ref{fig:2021-0219-0930} 中, $\overrightarrow{OA}= (1,0)$, 可类似地写出 $\overrightarrow{OB}$, $\overrightarrow{OP}$, $\overrightarrow{OQ}$ 的坐标; 再由 $\angle AOB= \angle QOP= \alpha+\beta$ 和内积的定义知
\[\overrightarrow{OA}\cdot \overrightarrow{OB}
    =\overrightarrow{OP}\cdot \overrightarrow{OQ},\]
将各向量坐标代入并整理即可.}
\[\cos(\alpha+\beta)= \cos\alpha\cos\beta- \sin\alpha\sin\beta,\]
大致步骤如下:
</p>

<p>
如图 \ref{fig:2021-0219-0930} 所示, 点 $A$, $B$, $P$, $Q$ 均在单位圆上, 且 $\angle AOP=\alpha$, $\angle POB=\beta$, $\angle AOQ=-\beta$, 则由三角函数的定义 (参考“16 弧度制与任意角的三角函数”), 各点坐标为
\[\begin{gathered}
    A(1,0),\quad
    B(\cos(\alpha+\beta),\sin(\alpha+\beta)),\\
    P(\cos\alpha,\sin\alpha),\quad
    Q(\cos\beta,-\sin\beta).
\end{gathered}\]
因为 $\angle AOB= \angle QOP= \alpha+\beta$, 所以 $\triangle AOB\cong \triangle QOP$, $|AB|=|PQ|$, 即
\[\begin{aligned}
    &\sqrt{[1-\cos(\alpha+\beta)]^2+[\sin(\alpha+\beta)]^2}\\
    ={}& \sqrt{(\cos\alpha- \cos\beta)^2+ (\sin\alpha+ \sin\beta)^2},
\end{aligned}\]
平方后展开并整理可得两角和的余弦公式.
</p>

<p>
\begin{figure}[hb]
    \centering
  <embed src="figs/2021-0219-0930-crop.svg">
    \caption{}\label{fig:2021-0219-0930}
\end{figure}
</p>

<p>
再利用诱导公式并结合
\[\begin{aligned}
    \cos(\alpha-\beta)&= \cos(\alpha+(-\beta)),\\
    \sin(\alpha+\beta)&= \cos(90^\circ-(\alpha+\beta))
        = \cos((90^\circ-\alpha)-\beta)),\\
    \sin(\alpha-\beta)&= \sin(\alpha+(-\beta))
\end{aligned}\]
可推出和角、差角的正弦、余弦公式
\begin{gather*}
    \sin(\alpha\pm \beta)= \sin\alpha\cos\beta\pm \cos\alpha\sin\beta,\\
    \cos(\alpha\pm \beta)= \cos\alpha\cos\beta\mp \sin\alpha\sin\beta.  
\end{gather*}
而由正切的定义, $\tan(\alpha+\beta)= \dfrac{\sin(\alpha+\beta)}{\cos(\alpha+\beta)}$, 可得
\[\tan(\alpha\pm \beta)
    = \frac{\tan\alpha\pm \tan\beta}{1\mp \tan\alpha\tan\beta}.\]
这六个公式都可以逆向使用, 即从右边推出左边.
</p>

<p>
和角、差角的三角函数公式的一个简单应用是求 $15^\circ$ 即 $\dfrac{\pi}{12}$ 的整数倍的三角函数值.
例如, 
\[\begin{aligned}
    \sin15^\circ
    &= \sin(45^\circ-30^\circ)
     = \sin45^\circ\cos30^\circ- \cos45^\circ\sin30^\circ \\
    &= \frac{\sqrt2}2\cdot\frac{\sqrt3}2- \frac{\sqrt2}2\cdot\frac12
     = \frac{\sqrt6-\sqrt2}4.
\end{aligned}\]
同理可求 $\sin75^\circ$, $\cos105^\circ$ 等. 此外还有如下用法
\[\cos x= \cos(x+y-y)= \cos(x+y)\cos y+\sin(x+y)\sin y.\]
</p>

<p>
\lianxi
<myexercise>
    <p>    已知 $\tan \alpha=4$, $\tan \beta=3$, 求 $\tan(\alpha+\beta)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由和角的正切公式,
    \[\tan(\alpha\pm \beta)
    = \frac{\tan\alpha\pm \tan\beta}{1\mp \tan\alpha\tan\beta}
    = \frac{4+3}{1-4\cdot 3}= -\frac{7}{11}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    计算: $\sin43^\circ \cos13^\circ- \sin 13^\circ\cos 43^\circ$.
</p>
</myexercise>
<mysolution>
    <p>
    原式整理为 $\sin(43^\circ- 13^\circ)= \sin 30^\circ$, 值为 $\dfrac12$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\sin\alpha= \dfrac23$, $\alpha\in\Big(\dfrac\pi2, \pi\Big)$, $\cos\beta=-\dfrac35$, $\beta\in\Big(\pi, \dfrac{3\pi}2\Big)$, 求 $\sin(\alpha+\beta)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $\cos\alpha= -\dfrac{\sqrt5}{3}$, $\sin\beta= -\dfrac45$, 所以
    \[\begin{aligned}
        \sin(\alpha+\beta)
        &= \sin\alpha\cos\beta+\cos\alpha\sin\beta\\
        &= \frac23\cdot\biggl(-\frac35\biggr)
            + \biggl(-\frac{\sqrt5}{3}\biggr)\cdot
              \biggl(-\frac45\biggr)\\
        &= \frac{4\sqrt5- 6}{15}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\cos\Big(\theta+ \dfrac\pi6\Big)= \dfrac5{13}$, $\theta\in\Big(0, \dfrac\pi2\Big)$, 求 $\cos\theta$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\theta+ \dfrac{\pi}{6}\in\Big(\dfrac{\pi}{6}, \dfrac{2\pi}3\Big)$, 所以 $\sin\Big(\theta+ \dfrac\pi6\Big)= \dfrac{12}{13}$,
    \[\begin{aligned}
        \cos\theta
        &= \cos\biggl(\theta+ \frac\pi6- \frac\pi6\biggr)\\
        &= \cos\biggl(\theta+ \frac\pi6\biggr) \cos\frac\pi6
            + \sin\biggl(\theta+ \frac\pi6\biggr) \sin\frac\pi6\\
        &= \dfrac5{13}\cdot\frac{\sqrt3}{2}
            + \dfrac{12}{13}\cdot\frac12
         = \frac{5\sqrt3+12}{26}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    化简: $\sin^2\Big(\alpha- \dfrac\pi6\Big) 
      + \sin^2\Big(\alpha+ \dfrac\pi6\Big) -\sin^2 \alpha$.
</p>
</myexercise>
<mysolution>
    <p>
    因为 
    \[\begin{aligned}
        \sin^2\Bigl(\alpha- \dfrac\pi6\Bigr)
        &= \Bigl(\sin\alpha\cos\dfrac\pi6
            - \cos\alpha\sin\frac\pi6\Bigr)^2\\
        &= \biggl(\frac{\sqrt3}{2}\sin\alpha
            - \frac12\cos\alpha\biggr)^2\\
        &= \frac34\sin^2\alpha- \frac{\sqrt3}{2}\sin\alpha\cos\alpha+ \frac14\cos^2\alpha,
    \end{aligned}\]
    同理可得,
    \[\sin^2\Bigl(\alpha+ \dfrac\pi6\Bigr)
        = \frac34\sin^2\alpha+ \frac{\sqrt3}{2}\sin\alpha\cos\alpha+ \frac14\cos^2\alpha,\]
    所以
    \[\text{原式}= \frac32\sin^2\alpha+ \frac12\cos^2\alpha- \sin^2\alpha= \frac12.\]
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{和角、差角的三角函数公式的应用}
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    已知 $\triangle ABC$ 为斜三角形 (即内角无直角), $B=\dfrac\pi3$ 且 $\tan A\tan C=2+\sqrt3$, 求 $\tan A$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    由题意, $A+C= \pi-B= \frac{2\pi}{3}$, 所以
    \[\tan\frac{2\pi}{3}= \tan(A+C)
        = \frac{\tan A+\tan C}{1-\tan A\tan C}.\]
    结合 $\tan A\tan C=2+\sqrt3$ 整理得
    \[\left\{\!\!\begin{array}{l}
        \tan A+\tan C= 3+\sqrt3,\\
        \tan A\tan C= 2+\sqrt3,
    \end{array}\right.\]
    解得 $\tan A=1$ 或 $2+\sqrt3$.
</p>

<p>
    \varexercise 若“$B=\dfrac\pi3$”改为“角 $A$, $B$, $C$ 成等差数列”, 则
    \[\left\{\!\!\begin{array}{l}
        2B= A+C,\\
        A+B+C= \pi,
    \end{array}\right.\ \text{解得}\ 
    \left\{\!\!\begin{array}{l}
        A+C= \frac{2\pi}{3},\\
        B=\dfrac\pi3,
    \end{array}\right.\]
    答案不变.
</p>

<p>
    \varexercise 此题进一步可求出三个内角为 $\dfrac\pi4$, $\dfrac{\pi}{3}$, $\dfrac{5\pi}{12}$ (即 $45^\circ$, $60^\circ$, $75^\circ$):
</p>

<p>
    (1) 若 $\tan A=1$, 则 $A= \dfrac{\pi}{4}$, $C= \frac{2\pi}{3}- A= \dfrac{5\pi}{12}$;
</p>

<p>
    (2) 若 $\tan A=2+\sqrt3$, 则
    \[\tan C= \tan\biggl(\frac{2\pi}3- A\biggr)
        = \frac{-\sqrt3-\tan A}{1-\sqrt 3\tan A}= 1,\]
    此时 $C= \dfrac{\pi}{4}$, $A= \dfrac{5\pi}{12}$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    在 $\triangle ABC$ 中, $\tan B=\dfrac12$, $\tan C=\dfrac13$,
    求 $\sin A$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为
    \[\tan(B+C)
    = \frac{\tan B+\tan C}{1-\tan B\tan C}
    = \frac{\dfrac12+ \dfrac13}{1- \dfrac12\cdot\dfrac13}
    = 1,\]
    所以 $B+C= \dfrac\pi4$, $A= \dfrac{3\pi}{4}$, 故 $\sin A= \dfrac{\sqrt2}{2}$.
</p>

<p>
    \varexercise 若 $\tan B=1$, $\tan C=2$, 同理可得 $\tan(B+C)=-3$. 将 $B+C= \pi-A$ 代入并利用诱导公式, $\tan A= 3$, 说明 $A$ 为锐角. 画三角函数线知, $\sin A= \dfrac{3\sqrt{10}}{10}$.
</p>
</mysolution>
</p>

<p>
\subsubsection{和角、差角的三角函数公式结合整体思想}
<span id="example-"></span>
<myexample>
    <p>
    已知 $\cos \alpha=\dfrac17$, $\cos(\alpha-\beta)=\dfrac{13}{14}$, 且 $0< \beta< \alpha< \dfrac\pi2$, 求 $\beta$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    先求 $\cos\beta$ 的值. 
    \mymarginpar{结合正弦、余弦线可知: 若 $0< \alpha< \pi$, 则由 $\cos\alpha$ 可以唯一确定 $\alpha$; 若 $-\dfrac\pi2< \alpha< \dfrac\pi2$, 则由 $\sin\alpha$ 可以唯一确定 $\alpha$.}
    因为 $0< \beta< \alpha< \dfrac\pi2$, 所以 $\alpha-\beta\in \biggl(0,\dfrac\pi2\biggr)$, $\sin\alpha= \frac{4\sqrt3}{7}$, 则 $\sin(\alpha-\beta)= \dfrac{3\sqrt3}{14}$, 
    \[\begin{aligned}
        \cos\beta
        &= \cos(\alpha- (\alpha-\beta))\\
        &= \cos\alpha\cos(\alpha-\beta)
            + \sin\alpha\sin(\alpha-\beta)\\
        &= \frac17\cdot\dfrac{13}{14}
            + \frac{4\sqrt3}{7}\cdot\dfrac{3\sqrt3}{14}
         = \frac12,
    \end{aligned}\]
    因此 $\beta= \dfrac{\pi}{3}$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    若 $\cos(\alpha+\beta)=\dfrac45$, $\sin(\alpha-\beta)=\dfrac35$, 
    且 $\dfrac{3\pi}2< \alpha+\beta< 2\pi$, 
    $\dfrac\pi2< \alpha-\beta< \pi$, 求 $\cos 2\beta$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $\sin(\alpha+\beta)= -\dfrac35$, $\cos(\alpha-\beta)= -\dfrac45$, 所以
    \[\begin{aligned}
        \cos2\beta
        &= \cos((\alpha+\beta)- (\alpha-\beta))\\
        &= \cos(\alpha+\beta)\cos(\alpha-\beta)
            + \sin(\alpha+\beta)\sin(\alpha-\beta)\\
        &= \frac45\cdot\biggl(-\frac45\biggr)
            + \biggl(-\frac35\biggr)\cdot\frac35
         = -1.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    求 $\cos 43^\circ\cos 77^\circ+\sin 43^\circ\cos 167^\circ$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由诱导公式,
    \[\cos 167^\circ= \cos (90^\circ+ 77^\circ)= -\sin77^\circ,\]
    所以
    \[\begin{aligned}
        \text{原式} 
        &= \cos43^\circ\cos77^\circ- \sin43^\circ\sin77^\circ\\
        &= \cos(43^\circ+77^\circ)= \cos120^\circ\\
        &= -\frac12.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $\tan\alpha$, $\tan\beta$ 是方程 $x^2 -3x-1=0$ 的两个根, 求 $\tan(\alpha+\beta)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由韦达定理, 
    \[\left\{\!\!\begin{array}{l}
        \tan\alpha+ \tan\beta= 3,\\
        \tan\alpha\tan\beta= -1.
    \end{array}\right.\]
    由和角的正切公式可知, $\tan(\alpha+\beta)= \dfrac32$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\sin\Big(x+\dfrac\pi4\Big)=\dfrac35$, 
    $\sin\Big(x-\dfrac\pi4\Big)=\dfrac45$, 求 $\tan x$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 将已知的式子展开,
    \[\left\{\!\!\begin{array}{l}
        \sin x\cos\frac\pi4+ \cos x\sin\frac\pi4= \frac35,\\[6pt]
        \sin x\cos\frac\pi4- \cos x\sin\frac\pi4= \frac45,
    \end{array}\right.\]
    即
    \[\left\{\!\!\begin{array}{l}
        \sin x+\cos x= \frac{3\sqrt2}{5},\\[6pt]
        \sin x-\cos x= \frac{4\sqrt2}{5},
    \end{array}\right.\]
    解得 $\sin x= \dfrac{7\sqrt2}{10}$, $\cos x= -\dfrac{\sqrt2}{10}$, 所以 $\tan x= -7$.
</p>

<p>
    方法二: 由已知, 
    \[\begin{aligned}
        \dfrac45
        &= \sin\Big(x-\dfrac\pi4\Big)
         = \sin\biggl(x+\frac\pi4- \frac\pi2\biggr)\\
        &= -\cos\biggl(x+\frac\pi4\biggr),
    \end{aligned}\]
    所以 $\cos\biggl(x+\frac\pi4\biggr)= -\dfrac45$, $\tan\biggl(x+\frac\pi4\biggr)= -\dfrac34$. 而 
    \[\tan\biggl(x+\frac\pi4\biggr)
        = \frac{\tan x+\tan\dfrac\pi4}{1- \tan x\tan\dfrac\pi4}= \frac{\tan x+ 1}{1-\tan x},\]
    所以
    \[\frac{\tan x+ 1}{1-\tan x}= -\dfrac34,
        \quad\text{解得}\quad \tan x= -7.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\tan(\alpha+\beta)=\dfrac25$, 
    $\tan\Big(\beta-\dfrac\pi4\Big)= \dfrac14$, 
    求 $\tan\Bigl(\alpha+\dfrac\pi4\Bigr)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[\begin{aligned}
        \tan\Bigl(\alpha+\dfrac\pi4\Bigr)
        &= \tan\Bigl[(\alpha+\beta)- \Bigl(\beta-\dfrac\pi4\Bigr)\Bigr]\\
        &= \frac{\dfrac25- \dfrac14}{1+ \dfrac25\cdot\dfrac14}
         = \dfrac{3}{22}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
</p>

<p>
<myexercise>
    <p>    已知 $\sin \alpha=\dfrac13$, 其中 $\alpha\in\Big(0,\dfrac\pi2\Big)$, 求 $\cos\Big(\alpha+\dfrac\pi6\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\cos\alpha= \dfrac{2\sqrt2}{3}$, 所以
    \[\begin{aligned}
        \cos\Big(\alpha+\dfrac\pi6\Big)
        &= \cos\alpha\cos\frac\pi6- \sin\alpha\sin\frac\pi6\\
        &= \frac{2\sqrt2}{3}\cdot\frac{\sqrt3}{2}
            - \frac13\cdot\frac12\\
        &= \frac{2\sqrt6-1}{6}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\tan \alpha=\dfrac12$, 求 $\tan\Big(\alpha+\dfrac\pi4\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    直接展开可得值为 $3$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $x\in\Big(0,\dfrac\pi4\Big)$ 且 $\sin x\cos x=\dfrac18$, 
    求 $\sqrt2\sin\Big(x-\dfrac\pi4\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    先展开,
    \[\sqrt2\sin\Big(x-\dfrac\pi4\Big)= \sin x- \cos x.\]
    因为
    \[(\sin x- \cos x)^2= 1- 2\sin x\cos x= \frac34,\]
    而 $x\in\Big(0,\dfrac\pi4\Big)$ 表明 $\sin x< \cos x$, 所以 $\sin x- \cos x= -\dfrac{\sqrt3}{2}$ 即为所求.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\tan(\alpha+\beta)=\dfrac25$, $\tan\beta=\dfrac13$, 
    求 $\tan\Big(\alpha+\dfrac\pi4\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 
    \[\begin{aligned}
        \tan\alpha
        &= \tan((\alpha+\beta)- \beta)
         = \frac{\tan(\alpha+\beta)- \tan\beta}{1+ \tan(\alpha+\beta)\tan\beta}\\
        &= \frac{\dfrac25- \dfrac13}{1+ \dfrac25\cdot\dfrac13}
         = \frac{1}{17},
    \end{aligned}\]
    所以
    \[\tan\Big(\alpha+\dfrac\pi4\Big)
        = \frac{\tan\alpha+1}{1-\tan\alpha}
        = \frac98.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知函数 $f(x)= A\sin\Big(x+ \dfrac\pi3\Big)$, $x\in\mathbb{R}$, 且 $f\Big(\dfrac{5\pi}{12}\Big)= \dfrac{3\sqrt2}2$.
</p>

<p>
    (1) 求 $A$ 的值;
</p>

<p>
    (2) 若 $f(\theta)-f(-\theta)= \sqrt3$, $\theta\in\Big(0,\dfrac\pi2\Big)$, 求 $f\Big(\dfrac\pi6-\theta\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 由题意,
    \[f\Big(\dfrac{5\pi}{12}\Big)
        = A\sin\Big(\dfrac{5\pi}{12}+ \dfrac\pi3\Big)
        = \dfrac{3\sqrt2}2,\]
    解得 $A=3$.
</p>

<p>
    (2) 因为 $f(x)= 3\sin\Big(x+ \dfrac\pi3\Big)$, 而
    \[\begin{aligned}
        f(\theta)-f(-\theta)
        &= 3\sin\Big(\theta+ \dfrac\pi3\Big)
            - 3\sin\Big(-\theta+ \dfrac\pi3\Big)\\
        &= 3\biggl[\sin\Big(\theta+ \dfrac\pi3\Big)
            + 3\sin\Big(\theta- \dfrac\pi3\Big)\biggr]\\
        &= 6\sin\theta\cos\frac\pi3
         = 3\sin\theta,
    \end{aligned}\]
    所以 $3\sin\theta= \sqrt3$, 解得 $\sin\theta= \dfrac1{\sqrt3}$. 由 $\theta\in\Big(0,\dfrac\pi2\Big)$ 知, $\cos\theta= \dfrac{\sqrt2}{\sqrt3}$, 因此
    \[f\Big(\dfrac\pi6-\theta\Big)
        = 3\sin\Big(\dfrac\pi2- \theta\Big)
        = 3\cos\theta= \sqrt6.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    如图 \ref{fig-190501-1110} 所示, 在平面直角坐标系 $xOy$ 中, 角 $\alpha\in\Big(\dfrac\pi4,\dfrac\pi2\Big)$ 的顶点是坐标原点, 始边为 $x$ 轴正半轴, 终边与单位圆 $O$ 交于点 $A(x_A, y_B)$. 将 $\alpha$ 的终边绕原点按逆时针方向旋转 $\dfrac\pi4$, 
    交单位圆于点 $B(x_B,y_B)$.
</p>

<p>
    (1) 若 $x_A= \dfrac35$, 求 $x_B$ 的值;
</p>

<p>
    (2) 过点 $A$, $B$ 作 $x$ 轴的垂线, 垂足分别为 $C$, $D$, 记 $\triangle AOC$ 及 $\triangle BOD$ 的面积分别为 $S_1$, $S_2$, $S_1=\dfrac43 S_2$, 求 $\tan\alpha$ 的值.
    \begin{figure}[hb]
    \small
    \centering
    \begin{tikzpicture}
      \draw[\myaxisarrow] (-1.3,0) -- (1.5,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1.3) -- (0,1.7) node[left] {$y$};
      \draw (0,0) node[anchor=135] {$O$} coordinate (O);
      \draw (O) circle (1);
      \def\Aangle{58};\def\Ax{cos \Aangle};\def\Ay{sin \Aangle};
      \draw (\Ax,\Ay)  coordinate (A) node[right,yshift=3pt] {$A$};
      \draw ($1.2*(A)$)  coordinate (A');
      \draw (\Ax,0)  coordinate (C) node[below] {$C$};
      \draw[rotate=45] (\Ax,\Ay) node[above left] {$B$} coordinate (B);
      \draw ($1.2*(B)$)  coordinate (B');
      \draw let \p1=(B) in (\x1,0) coordinate (D) 
        node[below,xshift=-3pt] {$D$};
      \draw (O)--(A') (A)--(C);
      \draw (O)--(B') (B)--(D);
    \end{tikzpicture}
    \caption{}\label{fig-190501-1110}
    \end{figure}
</p>
</myexercise>
<mysolution>
    <p>
    (1) 由正弦、余弦的定义, $x_A= \cos\alpha$, $x_B= \cos\biggl(\alpha+\dfrac\pi4\biggr)$. 因为 $x_A= \dfrac35$ 且 $\alpha\in\Big(\dfrac\pi4,\dfrac\pi2\Big)$, 所以 $\cos\alpha= \dfrac45$,
    \[\begin{aligned}
        \cos\biggl(\alpha+\dfrac\pi4\biggr)
        &= \cos\alpha\cos\frac\pi4- \sin\alpha\sin\frac\pi4\\
        &= \frac{\sqrt2}{2}(\cos\alpha- \sin\alpha)
         = -\frac{\sqrt2}{10},
    \end{aligned}\]
    即 $x_B= -\dfrac{\sqrt2}{10}$.
</p>

<p>
    (2) 因为 $\alpha\in\Big(\dfrac\pi4,\dfrac\pi2\Big)$, 所以 $\alpha+\dfrac\pi4\in\Big(\dfrac\pi2,\dfrac{3\pi}4\Big)$, 则
    \[\begin{aligned}
        S_1&= \frac12|OC|\cdot|CA|
            = \frac12\cos\alpha\sin\alpha,\\
        S_2&= \frac12|OD|\cdot|DB|
            = -\frac12\cos\biggl(\alpha+\dfrac\pi4\biggr)\sin\biggl(\alpha+\dfrac\pi4\biggr),
    \end{aligned}\]
    而 $S_1=\dfrac43 S_2$ 化为 (约去 $\dfrac12$)
    \[\cos\alpha\sin\alpha
        = -\frac43\cos\biggl(\alpha+\dfrac\pi4\biggr)\sin\biggl(\alpha+\dfrac\pi4\biggr).\]
</p>

<p>
    方法一: 由
    \[\begin{aligned}
        \cos\biggl(\alpha+\dfrac\pi4\biggr)
        &= \frac{\sqrt2}{2}(\cos\alpha- \sin\alpha),\\
        \sin\biggl(\alpha+\dfrac\pi4\biggr)
        &= \frac{\sqrt2}{2}(\cos\alpha+ \sin\alpha)
    \end{aligned}\]
    知上式化为
    \[\cos\alpha\sin\alpha
    = \frac23(\sin^2\alpha- \cos^2\alpha),\]
    整理后因式分解,
    \[(2\cos\alpha- \sin\alpha)(\cos\alpha+ 2\sin\alpha)= 0,\]
    解得 $\sin\alpha= 2\cos\alpha$ 或 $\-\dfrac12\cos\alpha$. 因此
    \[\tan\alpha= \frac{\sin\alpha}{\cos\alpha}
        = 2\ \text{或}\ -\frac12,\]
    而 $\alpha\in\Big(\dfrac\pi4,\dfrac\pi2\Big)$ 表明 $\tan\alpha=2$.
</p>

<p>
    方法二: 由二倍角公式和诱导公式, 前式化为
    \[\sin2\alpha
    = -\frac43\sin\biggl(2\alpha+\dfrac\pi2\biggr)
    = -\frac43\cos2\alpha,\]
    则 $\tan2\alpha= -\frac43= \frac{2\tan\alpha}{1-\tan^2\alpha}$, 整理后因式分解,
    \[(2\tan\alpha+ 1)(\tan\alpha- 2)= 0,\]
    所以 $\tan\alpha= 2$ 或 $-\frac12$. 仍由 $\alpha\in\Big(\dfrac\pi4,\dfrac\pi2\Big)$ 知 $\tan\alpha=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    观察下列三个等式:
</p>

<p>
    (1) $\sin30^\circ+ \sin150^\circ+ \sin270^\circ= 0$;
</p>

<p>
    (2) $\sin5^\circ+ \sin125^\circ+ \sin245^\circ= 0$;
</p>

<p>
    (3) $\sin23^\circ+ \sin143^\circ+ \sin263^\circ= 0$.\\
    寻找规律, 写出一个一般性的结论, 并给出证明.
</p>
</myexercise>
<mysolution>
    <p>
    归纳可得,
    \mymarginpar{将式中的 $\sin$ 换为 $\cos$, 结论仍成立.}
    \[\sin\alpha+ \sin(\alpha+ 120^\circ)+ 
        \sin(\alpha+ 240^\circ)= 0.\]
    大致证明过程: 
    \[\begin{aligned}
        \sin(\alpha+ 120^\circ)
        &= \sin\alpha\cos120^\circ+ \cos\alpha\sin120^\circ\\
        &= -\frac12\sin\alpha+ \frac{\sqrt3}{2}\cos\alpha,\\
        \sin(\alpha+ 240^\circ)
        &= \sin\alpha\cos240^\circ+ \cos\alpha\sin240^\circ\\
        &= -\frac12\sin\alpha- \frac{\sqrt3}{2}\cos\alpha,
    \end{aligned}\]
    两式与 $\sin\alpha$ 相加, 可知结论成立.
</p>
</mysolution>
</p>

<p>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%