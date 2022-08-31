---
# bookCollapseSection: true
title: 三角函数的和差角公式
weight: 3
bookHidden: true
prevPage: /docs/trigonometry/trigonometric-function/trig-induce
prevPageTitle: 三角函数的诱导公式
nextPage: /docs/trigonometry/trigonometric-function/trig-double-auxiliary
nextPageTitle: 倍角公式与辅助角公式
---

# 三角函数的和差角公式

<myexample>
<p>已知 $\alpha$, $\beta$ 都是锐角, $\cos\alpha=\dfrac17$, $\cos(\alpha+\beta)= -\dfrac{11}{14}$, 求 $\cos\beta$ 的值.
</p>
</myexample>
<mysolution>
    <p>由题意, $\alpha\in\Bigl(0,\dfrac\pi2\Bigr)$, $\alpha+\beta\in(0,\pi)$, 所以 $\sin\alpha=\dfrac{4\sqrt3}7$, $\sin(\alpha+\beta)= \dfrac{5\sqrt3}{14}$, 而
    \[\begin{aligned}
        \cos\beta
        &= \cos((\alpha+\beta)-\alpha)\\
        &= \cos(\alpha+\beta)\cos\alpha- \sin(\alpha+\beta)\sin\alpha\\
        &= \biggl(-\dfrac{11}{14}\biggr)\cdot \dfrac17
            + \dfrac{5\sqrt3}{14}\cdot \dfrac{4\sqrt3}7
         = \frac12.
    \end{aligned}\]
</p>
</mysolution>
<myremark>
    <p>上题可以顺带求出 $\beta= \dfrac\pi3$. 题中的解法主要是利用 $\alpha$ 和 $\alpha+\beta$ 表示 $\beta$, 以直接利用差角的余弦公式写出 $\cos\beta$ 的表达式.类似的还有
    \[\alpha= (45^\circ+\alpha)-45^\circ,\quad
      \alpha= \frac{\alpha+\beta}{2}+ \frac{\alpha-\beta}{2}.\]
</p>
</myremark>
</p>
<p><myexample>
<p>已知 $\sin(30^\circ+ \alpha)= \dfrac35$, $60^\circ< \alpha< 150^\circ$, 求 $\cos\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>由题意, $90^\circ< 30^\circ+\alpha< 180^\circ$, 所以 $\cos(30^\circ+ \alpha)= -\dfrac45$, 而
    \[\begin{aligned}
        \cos\alpha
        &= \cos((30^\circ+\alpha)- 30^\circ)\\
        &= \cos(30^\circ+\alpha)\cos30^\circ)
            + \sin(30^\circ+\alpha)\sin30^\circ\\
        &= -\dfrac45\cdot \frac{\sqrt3}{2}+ \dfrac35\cdot\frac12
         = \frac{3-4\sqrt3}{10}.
    \end{aligned}\]
</p>
</mysolution>
<myremark>
    <p>上题的另一种做法是将已知式拆为 $\dfrac12\cos\alpha+ \dfrac{\sqrt3}2\sin\alpha= \dfrac35$, 再与 $\sin^2\alpha+ \cos^2\alpha= 1$ 联立求解. 但此方法的计算量明显大一些, 而且由二次方程会得到两组解, 因此还需要讨论相应的取值范围, 以舍掉增根.
</p>
</myremark>

<p>利用距离公式可以推出两角和的余弦公式
\[\cos(\alpha+\beta)= \cos\alpha\cos\beta- \sin\alpha\sin\beta,\]
大致步骤如下:
</p>
<p>如图所示, 点 $A$, $B$, $P$, $Q$ 均在单位圆上, 且 $\angle AOP=\alpha$, $\angle POB=\beta$, $\angle AOQ=-\beta$, 则由三角函数的定义 (参考“16 弧度制与任意角的三角函数”), 各点坐标为
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
<p><center>
    \includegraphics[scale=1.5]{2021-0219-0930-crop}
</center>
</p>
<p>再利用诱导公式并结合
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

<p>和角、差角的三角函数公式的一个简单应用是求 $15^\circ$ 即 $\dfrac{\pi}{12}$ 的整数倍的三角函数值, 需事先利用常见特殊角表示所求的角, 例如
\[\begin{gathered}
    75^\circ= 45^\circ+30^\circ= 120^\circ-45^\circ,\\
    105^\circ= 60^\circ+45^\circ= 135^\circ-30^\circ,\\
    \dfrac{\pi}{12}= \frac\pi3-\frac\pi4= \frac\pi4-\frac\pi6,\\
    \dfrac{7\pi}{12}= \frac\pi3+\frac\pi4= \frac{3\pi}4-\frac\pi6.
\end{gathered}\]
</p>
<p><myexample>
<p>求值: $\cos\dfrac\pi{12}$, $\sin105^\circ$.
</p>
</myexample>
<mysolution>
    <p>利用和角、差角的正弦、余弦公式,
    \[\begin{aligned}
        \cos\dfrac\pi{12}
        &= \cos\Bigl(\frac\pi3-\frac\pi4\Bigr)\\
        &= \cos\frac\pi3\cos\frac\pi4+ \sin\frac\pi3\sin\frac\pi4\\
        &= \frac{\sqrt6+\sqrt2}{4}.
    \end{aligned}\]
    同理可得, $\sin105^\circ= \dfrac{\sqrt6+\sqrt2}{4}$.
</p>
</mysolution>

<myexample>
<p>已知 $\tan(\alpha+\beta)= \dfrac25$, $\tan\Bigl(\beta- \dfrac\pi4\Bigr)= \dfrac14$, 求 $\tan\Bigl(\alpha+ \dfrac\pi4\Bigr)$ 的值.
</p>
</myexample>
<mysolution>
    <p>整体考虑并用差角的正切公式,
    \[\begin{aligned}
        \tan\Bigl(\alpha+ \dfrac\pi4\Bigr)
        &= \tan\Bigl[\Bigl(\alpha+ \beta\Bigr)- \Bigl(\beta- \dfrac\pi4\Bigr)\Bigr]\\
        &= \frac{\tan(\alpha+\beta)- \tan\Bigl(\beta- \dfrac\pi4\Bigr)}{1+ \tan(\alpha+\beta)\tan\Bigl(\beta- \dfrac\pi4\Bigr)}\\
        &= \frac3{22}.
    \end{aligned}\]
</p>
</mysolution>

<myexample>
<p>已知 $\tan\alpha$, $\tan\beta$ 是方程 $2x^2+3x-5= 0$ 的两个实数根, 求 $\tan(\alpha+\beta)$ 的值.
</p>
</myexample>
<mysolution>
    <p>由二次方程根与系数的关系, 
    \[\tan\alpha+\tan\beta= -\frac32,\quad
        \tan\alpha\tan\beta= -\frac52,\]
    所以 
    \[\tan(\alpha+\beta)
        = \frac{\tan\alpha+ \tan\beta}{1- \tan\alpha\tan\beta}
        = -\frac37.\]
</p>
</mysolution>

