\sectioncounter{18}
</p>

<p>
\section{二倍角的三角函数与辅助角公式}
</p>

<p>
\subsection{知识梳理}
在和角的三角函数公式中令 $\beta=\alpha$, 可得二倍角的三角函数公式
\begin{gather*}
    \sin2\alpha= 2\sin\alpha\cos\alpha, \quad
    \tan2\alpha= \frac{2\tan\alpha}{1- \tan^2\alpha},\\
    \cos2\alpha= \cos^2\alpha- \sin^2\alpha= 2\cos^2\alpha- 1= 1- 2\sin^2\alpha.
\end{gather*}
最后的式子中用到了 $\sin^2\alpha+\cos^2\alpha=1$, 该式也可改写为
\[\cos^2 \alpha= \frac{1+\cos2\alpha}2,\quad 
    \sin^2 \alpha= \frac{1-\cos2\alpha}2.\]
在解题时, 只要所考虑的两个角有二倍的关系即可使用这些公式, 例如
\[\sin x= 2\sin\frac{x}2\cos\frac{x}2,\quad
    \cos^2 2x= \frac{1+\cos4x}2.\]
</p>

<p>
和角、差角的三角函数公式的另一个重要应用是辅助角公式. 例如
\[\begin{aligned}
    \frac12\sin x+\frac{\sqrt3}2\cos x
    &= \cos\frac{\pi}3\sin x+\sin\frac{\pi}3\cos x
     = \sin\Big(x+\frac{\pi}3\Big),                       \\
    \cos x+\sqrt3\sin x
    &= 2\Big(\frac12\cos x+\frac{\sqrt3}2\sin x\Big)
     = 2\sin\Big(x+\frac{\pi}6\Big),
\end{aligned}\]
后一式也可以化为 $2\cos\Big(x-\dfrac{\pi}3\Big)$. 
把上述过程一般化可得辅助角公式: 
\[a\sin\alpha+ b\cos\alpha= \sqrt{a^2+ b^2}\sin(\alpha+ \theta),\]
其中 $ab\neq 0$ 且 $\cos\theta= \dfrac{a}{\sqrt{a^2+ b^2}}$,
$\sin\theta= \frac{b}{\sqrt{a^2+ b^2}}$. 利用辅助角公式的常见变形还有
\[\begin{gathered}
    \sin\alpha\pm\cos\alpha
    = \sqrt2\sin\biggl(\alpha\pm\frac\pi4\biggr),\\
    \cos\alpha\pm\sin\alpha
    = \sqrt2\cos\biggl(\alpha\mp\frac\pi4\biggr).
\end{gathered}\]
</p>

<p>
\lianxi
</p>

<p>
<myexercise>
    <p>    若 $\sin \alpha=\dfrac35$, 求 $\cos 2\alpha$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\cos 2\alpha= 1-2\sin^2\alpha= \dfrac7{25}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\cos \alpha= \dfrac5{13}$, $\alpha\in\Big(0,\dfrac\pi2\Big)$, 求 $\sin 2\alpha$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\sin\alpha= \dfrac{12}{13}$, $\sin2\alpha= \frac{120}{169}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求值: $\Big(\sin\dfrac{5\pi}{12}+ \cos\dfrac{5\pi}{12}\Big)
        \Big(\sin\dfrac{5\pi}{12}- \cos\dfrac{5\pi}{12}\Big)$.
</p>
</myexercise>
<mysolution>
    <p>
    原式化为 $\sin^2\dfrac{5\pi}{12}- \cos^2\dfrac{5\pi}{12}$, 而
    \[\sin^2\dfrac{5\pi}{12}
        = \frac12\biggl(1-\cos\frac{5\pi}{6}\biggr),\quad
    \cos^2\dfrac{5\pi}{12}
        = \frac12\biggl(1+\cos\frac{5\pi}{6}\biggr),\]
    所以原式等于 $-\cos\dfrac{5\pi}6= \dfrac{\sqrt3}2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\sin\dfrac\theta2+ \cos\dfrac\theta2= \dfrac{2\sqrt3}3$, 求 $\sin \theta$, $\cos 2\theta$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    将已知式子平方,
    \[\sin^2\frac\theta2+ 2\sin\frac\theta2\cos\frac\theta2
        + \cos^2\frac\theta2= \frac43,\]
    即得 $\sin\theta= \dfrac13$, 而
    \[\cos2\theta= 1-2\sin^2\theta= \frac79.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\sin\alpha- \sqrt3 \cos\alpha=m$, 求 $m$ 的最小值.
</p>
</myexercise>
<mysolution>
    <p>
    由辅助角公式, 
    \[\sin\alpha- \sqrt3 \cos\alpha=2\sin\biggl(\alpha- \dfrac\pi3\biggr),\]
    所以 $m$ 的最小值为 $-2$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{二倍角公式的简单应用}
<span id="example-"></span>
<myexample>
    <p>
    已知 $\sin \alpha= \dfrac{12}{13}$, $\alpha\in\Big(\dfrac\pi2,\pi\Big)$, 求 $\sin 2\alpha$, $\cos 2\alpha$, $\tan 2\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    $\cos\alpha= -\dfrac5{13}$, 则
    \[\begin{aligned}
        \sin2\alpha&= 2\sin\alpha\cos\alpha= -\frac{120}{169},\\
        \cos2\alpha&= 1- 2\sin^2\alpha= -\frac{119}{169},\\
        \tan2\alpha&= \frac{\sin\alpha}{\cos\alpha}
            = -\frac{120}{119}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    若 $\cos\Big(\theta+ \dfrac\pi4\Big)= \dfrac14$, 求 $\sin2\theta$ 的值.
</p>
</myexample>
<mysolution>
    <p>
    方法一: 将已知式子展开并整理, $\cos\theta- \sin\theta= \dfrac{\sqrt2}4$, 平方得,
    \[1-2\cos\theta\sin\theta= \frac18,\quad\text{即}\quad
        \sin2\theta= \frac78.\]
</p>

<p>
    方法二: 由二倍角公式,
    \[\cos\biggl(2\theta+ \frac\pi2\biggr)
        = 2\cos^2\biggl(\theta+ \frac\pi4\biggr)-1
        = -\frac78,\]
    再由诱导公式, $-\sin2\theta= -\frac78$, 即 $\sin2\theta= \frac78$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    若 $\alpha\in\Big(\dfrac\pi2,\pi\Big)$, $\sin\alpha=\dfrac{\sqrt5}5$, 求 $\sin\Big(\dfrac\pi4+2\alpha\Big)$ 和 
    $\cos\Big(\dfrac{5\pi}6- 2\alpha\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\sin\alpha= \dfrac1{\sqrt5}$, $\cos\alpha= -\dfrac2{\sqrt5}$, 则 $\sin2\alpha= -\dfrac45$, $\cos2\alpha= \dfrac35$,
    \[\begin{aligned}
        \sin\Big(\dfrac\pi4+2\alpha\Big)
        &= \frac{\sqrt2}{2}(\sin2\alpha+ \cos2\alpha)
         = -\frac{\sqrt2}{10},\\
        \cos\Big(\dfrac{5\pi}6- 2\alpha\Big)
        &= -\frac{\sqrt3}{2}\cos2\alpha+ \frac12\sin2\alpha
         = -\frac{3\sqrt3+4}{10}.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
\subsubsection{二倍角公式和辅助角公式的综合应用}
<span id="example-"></span>
<myexample>
    <p>
    已知函数 $f(x)=\cos x\sin\Big(x+\dfrac\pi3\Big)- \sqrt3 \cos^2 x+ \dfrac{\sqrt3}4$, $x\in\mathbb{R}$.
    求 $f(x)$ 在闭区间 $\Bigl[-\dfrac\pi4, \dfrac\pi4\Bigr]$ 上的最大值和最小值.
</p>
</myexample>
<mysolution>
    <p>
    函数解析式化为
    \[\begin{aligned}
        f(x)&= \cos x\biggl(\frac12\sin x+ \frac{\sqrt3}2\cos x\biggr)
            - \sqrt3\cos^2 x+ \dfrac{\sqrt3}4\\
        &= \frac12\sin x\cos x- \frac{\sqrt3}2\cos^2 x+ \dfrac{\sqrt3}4\\
        &= \frac14\sin2x- \frac{\sqrt3}4(1+\cos2x)+ \dfrac{\sqrt3}4\\
        &= \frac12\biggl(\frac12\sin2x- \frac{\sqrt3}{2}\cos2x\biggr)\\
        &= \frac12\sin\biggl(2x-\frac\pi3\biggr).
    \end{aligned}\]
    当 $x\in\Bigl[-\dfrac\pi4, \dfrac\pi4\Bigr]$ 时, 
    \[2x- \dfrac\pi3\in\Bigl[-\dfrac{5\pi}6, \dfrac\pi6\Bigr],
        \quad \sin\biggl(2x- \dfrac\pi3\biggr)\in \Bigl[-1, \dfrac12\Bigr],\]
    所以 $f(x)\in\Bigl[-\dfrac12, \dfrac14\Bigr]$.
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    函数 $f(x)=\sin^2\Big(x-\dfrac\pi6\Big)+ \cos^2\Big(x-\dfrac\pi3\Big) + \sin x\cos x$, $x\in\mathbb{R}$, 求其最大值及对应的 $x$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    因为 $\sin x\cos x= \dfrac12\sin2x$, 且
    \[\begin{aligned}
        \sin^2\Big(x-\dfrac\pi6\Big)
        &= \frac12\biggl[1- \cos\biggl(2x- \frac\pi3\biggr)\biggr]\\
        &= \frac12\biggl(1- \frac12\cos2x- \frac{\sqrt3}2\sin2x\biggr),\\
        \cos^2\Big(x-\dfrac\pi3\Big)
        &= \frac12\biggl[1+ \cos\biggl(2x- \frac{2\pi}3\biggr)\biggr]\\
        &= \frac12\biggl(1- \frac12\cos2x+ \frac{\sqrt3}2\sin2x\biggr),
    \end{aligned}\]
    所以
    \[f(x)= 1- \frac12\cos2x+ \frac12\sin2x
        = 1+ \frac{\sqrt2}{2}\sin\biggl(2x- \frac\pi4\biggr).\]
    由此可知 $f(x)$ 的最大值为 $1+\dfrac{\sqrt2}2$, 此时
    \[2x- \dfrac\pi4= \dfrac\pi2+ 2k\pi,\ \text{即}\ 
        x= \dfrac{3\pi}8+ k\pi,\quad k\in\mathbb{Z}.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
</p>

<p>
<myexercise>
    <p>    计算: $\sin 15^\circ\sin 75^\circ$.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 由诱导公式, 
    \[\text{原式}= \sin 15^\circ\cos 15^\circ
        = \frac12\sin 30^\circ= \frac14.\]
</p>

<p>
    方法二: 由和角、差角的正弦公式,
    \[\begin{aligned}
        \sin 15^\circ&= \sin(45^\circ- 30^\circ)
            = \frac{\sqrt6-\sqrt2}{4},\\
        \sin 75^\circ&= \sin(45^\circ+ 30^\circ)
        = \frac{\sqrt6+\sqrt2}{4},
    \end{aligned}\]
    同样可知, $\sin 15^\circ\sin 75^\circ= \dfrac14$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\sin2\alpha=\dfrac13$, 求 $\cos^2\Big(\alpha- \dfrac\pi4\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 直接用二倍角公式,
    \[\begin{aligned}
        \cos^2\Big(\alpha- \dfrac\pi4\Big)
        &= \frac12\biggl[1+ \cos\biggl(2\alpha- \frac\pi2\biggr)\biggr]\\
        &= \frac12(1+ \sin2\alpha)
         = \frac23.
    \end{aligned}\]
</p>

<p>
    方法二: 将 $\cos\Big(\alpha- \dfrac\pi4\Big)$ 展开得 $\dfrac{\sqrt2}2(\cos\alpha+ \sin\alpha)$, 再平方可知,
    \[\begin{aligned}
        \cos^2\Big(\alpha- \dfrac\pi4\Big)
        &= \frac12(1+2\sin\alpha\cos\alpha)\\
        &= \frac12(1+ \sin2\alpha)
         = \frac23.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $a=\sin15^\circ\cos15^\circ$, 
    $b=\cos^2 \dfrac\pi6-\sin^2 \dfrac\pi6$,
    $c=\dfrac{\tan30^\circ}{1-\tan^2 30^\circ}$, 
    判断 $a$, $b$, $c$ 的大小关系.
</p>
</myexercise>
<mysolution>
    <p>
    $a= \dfrac12\sin30^\circ= \dfrac14$, 
    $b= \cos\dfrac\pi3= \dfrac12$,
    $c= \dfrac12\tan60^\circ= \dfrac{\sqrt3}2$, 所以 $a< b< c$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若关于 $x$ 的方程 $\cos2x-2\sqrt3 \sin x\cos x=k$ 有解, 
    求 $k$ 的取值范围.
</p>
</myexercise>
<mysolution>
    <p>
    方程左边化为
    \[\cos2x- \sqrt3\sin2x= 2\cos\biggl(2x+ \frac\pi3\biggr)
        \in [-2,2],\]
    表明 $k\in [-2,2]$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
</p>

<p>
<myexercise>
    <p>    已知 $\alpha\in\Bigl(-\dfrac\pi2,0\Bigr)$ 且 
    $\cos\alpha= \dfrac45$, 求 $\tan2\alpha$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意, $\tan\alpha= -\dfrac34$, 
    \[\tan2\alpha= \frac{2\tan\alpha}{1- \tan^2\alpha}
        = -\frac{24}{7}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    若 $\sin\alpha+\cos\alpha= \dfrac{\sqrt3}2$, 求 $\sin2\alpha$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    将已知式两边平方, 
    \[1+ 2\sin\alpha\cos\alpha= \frac34,\quad\text{即}\quad
        \sin2\alpha= -\frac14.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知 $\sin2\alpha= \dfrac23$, 求 $\cos^2\Big(\alpha+ \dfrac\pi4\Big)$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: \mymarginpar{此题与课堂评价第 2 题类似.}
    直接用二倍角公式,
    \[\begin{aligned}
        \cos^2\Big(\alpha+ \dfrac\pi4\Big)
        &= \frac12\biggl[1+ \cos\biggl(2\alpha+ \frac\pi2\biggr)\biggr]\\
        &= \frac12(1- \sin2\alpha)
         = \frac16.
    \end{aligned}\]
</p>

<p>
    方法二: 将 $\cos\Big(\alpha+ \dfrac\pi4\Big)$ 展开得 $\dfrac{\sqrt2}2(\cos\alpha- \sin\alpha)$, 再平方可知,
    \[\begin{aligned}
        \cos^2\Big(\alpha+ \dfrac\pi4\Big)
        &= \frac12(1-2\sin\alpha\cos\alpha)\\
        &= \frac12(1- \sin2\alpha)
         = \frac23.
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $\sin2\alpha= -\dfrac32\sin\alpha$, $\alpha\in\Big(\dfrac\pi2, \pi\Big)$, 求 $\tan2\alpha$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    由题意,
    \[2\sin\alpha\cos\alpha= -\dfrac32\sin\alpha,\quad
        \text{即}\quad \cos\alpha= -\frac13.\]
    因为 $\alpha\in\Big(\dfrac\pi2, \pi\Big)$, 所以 $\tan\alpha= -2\sqrt2$,
    \[\tan2\alpha= \frac{2\tan\alpha}{1- \tan^2\alpha}
        = \frac{4\sqrt2}{7}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求函数 $y=\sin^2 x+\cos^2\Big(x-\dfrac\pi3\Big)$ 
    ($x\in\mathbb{R}$) 的值域.
</p>
</myexercise>
<mysolution>
    <p>
    已知函数化为
    \[\begin{aligned}
        y&= \frac12(1- \cos2x)+ \frac12\biggl[ 1
            - \cos\biggl(2x-\dfrac{2\pi}3\biggr)\biggr]\\
        &= 1+ \frac12\biggl(-\cos2x- \frac12\cos2x
            + \frac{\sqrt3}{2}\sin2x\biggr)\\
        &= 1+ \frac{\sqrt3}{2}\biggl(\frac12\sin2x
            - \frac{\sqrt3}{2}\cos2x\biggr)\\
        &= 1+ \frac{\sqrt3}{2}\sin\biggl(2x- \frac\pi3\biggr)\\
        &\in \biggl[1-\frac{\sqrt3}2, 1+\frac{\sqrt3}2\biggr].
    \end{aligned}\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求函数 $f(x)=\cos x(\sin x+\cos x)- \dfrac12$ 在 $\biggl[0,\dfrac\pi2\biggr]$ 上的值域.
</p>
</myexercise>
<mysolution>
    <p>
    先化简函数解析式,
    \[\begin{aligned}
        f(x)&= \cos x\sin x+ \cos^2 x- \dfrac12\\
        &= \frac12\sin2x+ \frac12(1+\cos2x)- \frac12\\
        &= \frac12(\sin2x+ \cos2x)
         = \frac{\sqrt2}{2}\sin\biggl(2x+ \frac\pi4\biggr).
    \end{aligned}\]
    因为 $x\in\biggl[0,\dfrac\pi2\biggr]$, 所以
    \[2x+ \frac\pi4\in \biggl[\frac\pi4, \dfrac{5\pi}4\biggr],\quad 
    \sin\biggl(2x+ \frac\pi4\biggr)\in \biggl[-\frac{\sqrt2}2, 1\biggr],\]
    即 $f(x)\in \biggl[-\dfrac12, \dfrac{\sqrt2}2\biggr]$.
</p>

<p>
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知圆 $x^2 +y^2 =2$ 的切线 $l_1$ 和 $l_2$ 相交于点 $(1,3)$, 求两切线夹角的正切值.
</p>
</myexercise>
<mysolution>
    <p>
    如图 \ref{fig:2021-0221-1600} 所示, 设切点为 $M$, $N$, 则 $OM\perp MP$, $ON\perp NP$ 且 $OP$ 平分 $\angle MPN$. 因为 $OM=\sqrt2$, $OP= \sqrt{10}$, 所以 $MP= 2\sqrt2$, $\tan\angle MPO= \frac12$,
    \[\begin{aligned}
        \tan\angle MPN
        &= \tan2\angle MPO
         = \frac{2\tan\angle MPO}{1- \tan^2\angle MPO}\\
        &= \frac{1}{1- \dfrac14}
         = \frac43.
    \end{aligned}\]
</p>

<p>
    \begin{figure}[hb]
        \small\centering
  <embed src="figs/2021-0221-1600-crop.svg">
        \caption{}\label{fig:2021-0221-1600}
    \end{figure}
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    观察下列三个等式:
</p>

<p>
    (1) $\sin^2 30^\circ+ \sin^2 90^\circ+ \sin^2 150^\circ= \dfrac32$;
</p>

<p>
    (2) $\sin^2 5^\circ+ \sin^2 65^\circ+ \sin^2 125^\circ= \dfrac32$;
</p>

<p>
    (3) $\sin^2 23^\circ+ \sin^2 83^\circ+ \sin^2 143^\circ= \dfrac32$.\\
    寻找规律, 写出一个一般性的结论, 并给出证明.
</p>
</myexercise>
<mysolution>
    <p>
    推测 \mymarginpar{将式中的 $\sin$ 换成 $\cos$, 结论仍成立.}
    \[\sin^2 \alpha+ \sin^2 (\alpha+ 60^\circ)
        + \sin^2 (\alpha+ 120^\circ)= \dfrac32.\]
    证明过程: 
    $\sin^2 \alpha= \dfrac12(1- \cos2x)$,
    \[\begin{aligned}
        \sin^2 (\alpha+ 60^\circ)
        &= \frac12\biggl[1- \cos(2\alpha+ 120^\circ)\biggr]\\
        &= \frac12\biggl(1+ \frac12\cos2\alpha+ \frac{\sqrt3}2\sin2\alpha\biggr),\\
        \sin^2 (\alpha+ 120^\circ)
        &= \frac12\biggl[1- \cos(2\alpha+ 240^\circ)\biggr]\\
        &= \frac12\biggl(1+ \frac12\cos2\alpha- \frac{\sqrt3}2\sin2\alpha\biggr),
    \end{aligned}\]
    三式相加可知结论成立.
</p>
</mysolution>
</p>

<p>
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%