---
# bookCollapseSection: true
title: 三角函数的诱导公式
weight: 2
bookHidden: true
prevPage: /docs/trigonometry/trigonometric-function/trig-def-radian
prevPageTitle: 任意角的三角函数与弧度制
nextPage: /docs/trigonometry/trigonometric-function/trig-sum-diff
nextPageTitle: 三角函数的和差角公式
---

# 三角函数的诱导公式

<p>诱导公式指的是已知角加上 $90^\circ$ (或 $\dfrac{\pi}2$) 的整数倍后, 所得角与已知角的三角函数值的关系. 最容易理解的是
\[\sin(2\pi+\alpha)= \sin\alpha,\quad
    \cos(2\pi+\alpha)= \cos\alpha.\]
常用的还有
\[\begin{gathered}
    \sin(-x)= -\sin x\ (\text{奇函数}),\quad 
    \cos(-x)= \cos x\ (\text{偶函数}),\\
    \sin(90^\circ-x)= \cos x,\quad \cos(90^\circ-x)= \sin x,\\
    \sin(180^\circ-x)= \sin x,\quad \cos(180^\circ-x)= -\cos x.
\end{gathered}\]
分别对应如下图形 (为观察方便, 正弦线、余弦线的位置与通常的定义略有区别):
<center>
    \includegraphics[scale=1.1]{2020-1225-1900-crop}\quad
    \includegraphics[scale=1.1]{2020-1225-1910-crop}\quad
    \includegraphics[scale=1.1]{2020-1225-1920-crop}
</center>
</p>
<p>诱导公式的记忆口诀为: 奇变偶不变, 符号看象限, 其中
</p>
<p>(1) “奇”“偶”指所加 $90^\circ$ (或 $\dfrac{\pi}2$) 倍数的奇偶性; 
</p>
<p>(2) “变”指函数名中“正”变“余”或“余”变“正”；
</p>
<p>(3) “象限”指把已知角视为锐角时所得角对应的象限;
</p>
<p>(4) “符号”是此时原式的符号. \\
例如:
\begin{gather*}
    \sin(2x-\pi)= -\sin2x,\quad \tan(x+180^\circ)= \tan x, \\
    \cos(3x-270^\circ)= -\sin 3x,\quad
    \sin\Big(4x-\frac{\pi}2\Big)= -\cos 4x.
\end{gather*}
可结合如下图形理解诱导公式:
<center>
    \includegraphics[scale=1.1]{2020-1225-1930-crop}
</center>
</p>
<p>由上图可知:
\[\begin{gathered}
    \sin\biggl(\frac\pi2+\alpha\biggr)= \cos\alpha,\quad
        \cos\biggl(\frac\pi2+\alpha\biggr)= -\sin\alpha,\\
    \sin(\pi+\alpha)= -\sin\alpha,\quad
        \cos(\pi+\alpha)= -\cos\alpha,\\
    \sin\biggl(\frac{3\pi}2+\alpha\biggr)= -\cos\alpha,\quad
        \cos\biggl(\frac{3\pi}2+\alpha\biggr)= \sin\alpha,
    \end{gathered}\]
恰好验证了诱导公式.
</p>
<p><myexample>
<p>化简: $\dfrac{\sin\biggl(\alpha-\dfrac{11}2\pi\biggr)
        \cos\biggl(\dfrac{\pi}2-\alpha\biggr)
        \tan(2\pi-\alpha)}{\cos\biggl(\dfrac{\pi}2+\alpha\biggr)
        \cos(\alpha-2\pi)\tan(\alpha-5\pi)}$.
</p>
</myexample>
<mysolution>
    <p>由诱导公式,
    \[\begin{gathered}
        \sin\biggl(\alpha-\dfrac{11}2\pi\biggr)
        = \sin\biggl(\alpha-\dfrac{3}2\pi\biggr)
        = \sin\biggl(\alpha+\dfrac{\pi}2\biggr)
        = \cos\alpha,\\
        \cos\biggl(\dfrac{\pi}2-\alpha\biggr)= \sin\alpha,\qquad
        \tan(2\pi-\alpha)= \tan(-\alpha)= -\tan\alpha,\\
        \cos\biggl(\dfrac{\pi}2+\alpha\biggr)= -\sin\alpha,\qquad
        \cos(\alpha-2\pi)= \cos\alpha,\\
        \tan(\alpha-5\pi)= \tan(\alpha+\pi)= \tan\alpha,
    \end{gathered}\]
    所以
    \[\text{原式}= \frac{\cos\alpha\sin\alpha(-\tan\alpha)}{
        -\sin\alpha\cos\alpha\tan\alpha}= 1.\]
</p>
</mysolution>
</p>
<p>用诱导公式解题时, 应先利用本节第一个公式, 将式中 $\pi$ 的系数的绝对值尽可能变小, 最好是将含 $\pi$ 的项化为 $[-\pi,\pi]$ 内的数.
</p>

<p>计算具体的三角函数值, 一般是先利用诱导公式尽量化为较简单的角 (绝对值不超过 $\pi$, 也即 $180^\circ$) 的三角函数.
</p>
<p><myexample>
<p>化简下列各式:
</p>
<p>(1) $\sin\dfrac{7\pi}2+ \cos\dfrac{5\pi}2+ \cos(-5\pi)+ \tan\dfrac{5\pi}4$;
</p>
<p>(2) $a^2\sin810^\circ- b^2\cos900^\circ+ 2ab\tan1125^\circ$;
</p>
<p>(3) $\dfrac{\sin(\pi+ \alpha)\cos(2\pi- \alpha)\tan(- \alpha)}{\tan(-\pi- \alpha)\sin(-\pi- \alpha)}$.
</p>
</myexample>
<mysolution>
    <p>(1) 先利用周期性 (注意 $y=\sin x$, $y=\cos x$ 的周期均为 $2\pi$, 而 $y=\tan x$ 的周期为 $\pi$), 将题中各式化为绝对值较小的角的三角函数, 即
    \[\begin{aligned}
        \sin\frac{7\pi}2 &= \sin\biggl(\frac{7\pi}2 -4\pi\biggr)
            = \sin\biggl(-\frac{\pi}2\biggr)= -1,\\
        \cos\frac{5\pi}2 &= \cos\biggl(\frac{5\pi}2 -2\pi\biggr)
            = \cos\frac{\pi}2 = 0,\\
        \cos(-5\pi) &= \cos(-5\pi+ 6\pi)= \cos\pi= -1,\\
        \tan\frac{5\pi}4 &= \tan\biggl(\frac{5\pi}4 -\pi\biggr)
            = \tan\frac\pi4= 1,
    \end{aligned}\]
    所以,
    \[\text{原式}= -1+0-1+1= -1.\]
</p>
<p>(2) 方法同上, 周期均用角度表示, 即
    \[\begin{aligned}
        \sin810^\circ &= \sin(810^\circ -720^\circ)
            = \sin90^\circ= 1,\\
        \cos900^\circ &= \cos(900^\circ- 720^\circ)
            = \cos180^\circ = -1,\\
        \tan1125^\circ &= \tan(1125^\circ- 1080^\circ)
            = \tan45^\circ= 1,
    \end{aligned}\]
    所以,
    \[\text{原式}= a^2- b^2\cdot(-1)+2ab= (a+b)^2.\]
</p>
<p>(3) 直接用诱导公式可得
    \[\begin{gathered}
        \sin(\pi+ \alpha) = -\sin\alpha,\quad
        \cos(2\pi- \alpha) = \cos\alpha,\quad
        \tan(-\alpha) = -\tan\alpha,\\
        \tan(-\pi- \alpha) = \tan(-\alpha)= -\tan\alpha,\quad
        \sin(-\pi- \alpha) = \sin(\pi-\alpha)= \sin\alpha,
    \end{gathered}\]
    所以,
    \[\text{原式}= \frac{-\sin\alpha\cdot \cos\alpha\cdot (-\tan\alpha)}{-\tan\alpha\cdot \sin\alpha}= -\cos\alpha.\]
</p>
<p></p>
</mysolution>

<myexample>
<p>计算下列各式的值:
</p>
<p>(1) $\cos\dfrac\pi5+ \cos\dfrac{2\pi}5+ \cos\dfrac{3\pi}5+ \cos\dfrac{4\pi}5$;
</p>
<p>(2) $\sin240^\circ\cos330^\circ+ \sin(-690^\circ)\cos(-660^\circ)$.
</p>
</myexample>
<mysolution>
    <p>(1) 本小题的各个角都不是特殊角 (如 $30^\circ$, $135^\circ$ 等), 所以不应试图求出各三角函数值, 而应考虑它们的数量关系. 画图并观察可知, 
    \[\frac\pi5+ \frac{4\pi}5= \frac{2\pi}5+ \frac{3\pi}5= \pi,\]
    再由余弦线或诱导公式得
    \[\begin{gathered}
        \cos\frac{4\pi}5= \cos\biggl(\pi- \frac\pi5\biggr)= -\cos\frac\pi5,\\
        \cos\frac{3\pi}5= \cos\biggl(\pi- \frac{2\pi}5\biggr)= -\cos\frac{2\pi}5,
    \end{gathered}\]
    由此可知, 原式等于 $0$.
</p>
<p>(2) 本小题中的各个角都是特殊角, 所以应直接用诱导公式化为锐角. 因为
    \[\begin{aligned}
        \sin240^\circ &= \sin(180^\circ+ 60^\circ)
            = -\sin60^\circ = -\frac{\sqrt3}2,\\
        \cos330^\circ &= \cos(360^\circ -30^\circ)
            = \cos30^\circ = \frac{\sqrt3}2,\\
        \sin(-690^\circ) &= \sin(720^\circ- 690^\circ)
            = \sin30^\circ = \frac12,\\
        \cos(-660^\circ) &= \cos(720^\circ- 660^\circ)
            = \cos60^\circ = \frac12,
    \end{aligned}\]
    所以 
    \[\text{原式}= -\frac{\sqrt3}2\cdot \frac{\sqrt3}2
        + \frac12\cdot \frac12= -\frac12.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知 $\cos\biggl(\alpha+\dfrac\pi6\biggr)= -\dfrac13$, 求 $\sin\biggl(\alpha-\dfrac\pi3\biggr)$ 的值.
</p>
</myexample>
<mysolution>
    <p>此题应整体考虑, 即先观察两个角 $\alpha+\dfrac\pi6$, $\alpha-\dfrac\pi3$ 的特殊关系, 一般是看它们的和或差是否与特殊角 (如 $30^\circ$, $\dfrac\pi2$ 等) 有关, 或者是否有倍数关系 (后面会学倍角公式) 等. 可观察出 $\biggl(\alpha+ \dfrac\pi6\biggr)- \dfrac\pi2= \alpha-\dfrac\pi3$, 所以由诱导公式,
    \[\sin\biggl(\alpha-\dfrac\pi3\biggr)
        = \sin\biggl(\alpha+ \dfrac\pi6- \dfrac\pi2\biggr)
        = -\cos\biggl(\alpha+ \dfrac\pi6\biggr)
        = \dfrac13.\]
</p>
</mysolution>

