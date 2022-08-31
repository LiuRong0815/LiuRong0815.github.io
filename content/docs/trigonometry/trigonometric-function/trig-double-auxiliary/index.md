---
# bookCollapseSection: true
title: 倍角公式与辅助角公式
weight: 4
bookHidden: true
prevPage: /docs/trigonometry/trigonometric-function/trig-sum-diff
prevPageTitle: 三角函数的和差角公式
nextPage: /docs/trigonometry/trigonometric-function/trig-sum-prod
nextPageTitle: 和差化积公式与积化和差公式
---

# 倍角公式与辅助角公式

<myexample>
<p>已知 $\cos\dfrac\alpha8= -\dfrac45$, $8\pi< \alpha< 12\pi$, 求 $\sin\dfrac\alpha4$, $\cos\dfrac\alpha4$, $\tan\dfrac\alpha4$ 的值.
</p>
</myexample>
<mysolution>
    <p>因为 $\pi< \dfrac\alpha8< \dfrac{3\pi}2$, 所以  $\sin\dfrac\alpha8= -\dfrac35$, 由二倍角公式,
    \[\begin{gathered}
        \sin\dfrac\alpha4
        = \sin\Bigl(2\cdot\dfrac\alpha8\Bigr)
        = 2\sin\dfrac\alpha8 \cos\dfrac\alpha8
        = \frac{24}{25},\\
        \cos\dfrac\alpha4
        = 2\cos^2\dfrac\alpha8- 1
        = \frac{7}{25},\\
        \tan\dfrac\alpha4
        = \frac{\sin\dfrac\alpha4}{\cos\dfrac\alpha4}
        = \frac{24}{7}.
    \end{gathered}\]
</p>
</mysolution>
<myremark>
    <p>上题中, $\cos\dfrac\alpha4$ 也可以用公式 $\sin^2 x+\cos^2 x=1$ 求出, 但需要额外判断正负号. $\tan\dfrac\alpha4$ 也可以用二倍角公式计算, 但此处用定义更方便一些.
</p>
</myremark>
</p>
<p><myexample>
<p>已知 $\sin(\alpha-\pi)= \dfrac35$, 求 $\cos2\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>由诱导公式, $\sin(\alpha-\pi)= -\sin\alpha$, 所以  $\sin\alpha= -\dfrac35$,
    \[\cos2\alpha= 1-2\sin^2\alpha= \frac{7}{25}.\]
</p>
</mysolution>
<myremark>
    <p>凡三角函数式中含与 $\dfrac\pi2$ (即 $90^\circ$) 的倍数相关的和式, 应先用诱导公式化简.
</p>
</myremark>
</p>
<p><myexample>
<p>已知 $\sin2\alpha= -\sin\alpha$, $\alpha\in\Bigl(\dfrac\pi2,\pi\Bigr)$, 求 $\tan\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>已知式化为 $2\sin\alpha\cos\alpha= -\sin\alpha$, 即 $\cos\alpha= -\dfrac12$, 结合 $\alpha\in\Bigl(\dfrac\pi2,\pi\Bigr)$ 知 $\tan\alpha= -\sqrt3$ (结果表明 $\alpha= \dfrac{2\pi}3$).
</p>
</mysolution>
</p>
<p><myexample>
<p>已知 $\tan2\alpha= \dfrac13$, 求 $\tan\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>由二倍角公式, $\dfrac{2\tan\alpha}{1-\tan^2\alpha}= \dfrac13$, 解得 $\tan\alpha= -3\pm\sqrt{10}$.
</p>
</mysolution>

<myexample>
<p>已知 $\sin\alpha= \dfrac{\sqrt5}{5}$, 求 $\sin^4\alpha- \cos^4\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>由平方差公式和 $\sin^2\alpha+ \cos^2\alpha=1$ 知,
    \[\begin{aligned}
        \sin^4\alpha- \cos^4\alpha
        &= (\sin^2\alpha+ \cos^2\alpha)(\sin^2\alpha- \cos^2\alpha)\\
        &= \sin^2\alpha- \cos^2\alpha
         = 2\sin^2\alpha- 1\\
        &= -\frac35.
    \end{aligned}\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知 $\sin\dfrac\alpha2+ \cos\dfrac\alpha2= \dfrac12$, 求 $\cos2\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>将已知式平方得,
    \[\sin^2\dfrac\alpha2+ \cos^2\dfrac\alpha2
        + 2\sin\dfrac\alpha2 \cos\dfrac\alpha2= \dfrac14,\]
    即 $1+\sin\alpha= \dfrac14$, 所以 $\sin\alpha= -\dfrac34$, 而
    \[\cos2\alpha= 1- 2\sin^2\alpha= -\frac18.\]
</p>
</mysolution>
<myremark>
    <p>上题的解法主要是利用平方, 将 $\dfrac\alpha2$ 的三角函数式化为 $\alpha$ 的三角函数式. 下题也是相同的解法.
</p>
</myremark>
</p>
<p><myexample>
<p>若 $\sin2\alpha= \dfrac14$, $\dfrac\pi4< \alpha< \dfrac\pi2$, 求 $\cos\alpha- \sin\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>因为 $\dfrac\pi4< \alpha< \dfrac\pi2$, 所以画三角函数线知 $\cos\alpha< \sin\alpha$ 即 $\cos\alpha- \sin\alpha< 0$. 而
    \[(\cos\alpha- \sin\alpha)^2= 1- 2\cos\alpha\sin\alpha
        = 1-\sin2\alpha= \frac34,\]
    所以 $\cos\alpha- \sin\alpha= -\dfrac{\sqrt3}{2}$
</p>
</mysolution>
</p>
<p>\subsection{辅助角公式}
</p>
<p>辅助角公式主要用于将形如 $a\sin x\pm b\cos x$ 的式子化为 $r\sin(x\pm\theta)$ 或 $r\cos(x\pm\theta)$ 的形式, 以更方便地得到原式的单调性、最值等信息. 公式的变形过程主要逆向使用和角、差角的正弦、余弦公式
\begin{gather*}
    \sin(\alpha\pm \beta)= \sin\alpha\cos\beta\pm \cos\alpha\sin\beta,\\
    \cos(\alpha\pm \beta)= \cos\alpha\cos\beta\mp \sin\alpha\sin\beta,
\end{gather*}
所以实际应用辅助角公式时, 根据式子的形式, 可以有不同的变形结果. 例如, 
\[\begin{aligned}
    \frac{1}{2}\sin x+ \frac{\sqrt3}{2}\cos x
    &= \sin x\cos60^\circ+ \cos x\sin60^\circ
     = \sin(x+60^\circ),\\
    \frac{\sqrt2}{2}\cos x+ \frac{\sqrt2}{2}\sin x
    &= \cos45^\circ\cos x+ \sin45^\circ\sin x
     = \cos(x-45^\circ).
\end{aligned}\]
后一式也可以写为 $\cos(45^\circ-x)$.
</p>
<p>一般地, 对形如 
\[a\sin x+ b\cos x\quad (a>0, b>0)\]
的式子, 可先提出系数 $r=\sqrt{a^2+b^2}$, 将原式化为 $r\Bigl(\dfrac{a}r\sin x+ \dfrac{b}r\cos x\Bigr)$. 此时 $a$, $b$, $r$ 可以分别构成某个直角三角形的直角边和斜边, 因此 $\dfrac{a}r$ 和 $\dfrac{b}r$ 可以表示为同一个锐角 (设为 $\theta$) 的正弦、余弦值 (或余弦、正弦值, 依题意而定). 由此可得,
\[\begin{aligned}
    r\Bigl(\dfrac{a}r\sin x+ \dfrac{b}r\cos x\Bigr)
    &= r\Bigl(\cos\theta\sin x+ \sin\theta\cos x\Bigr)\\
    &= r\sin(x+\theta),
\end{aligned}\]
此即辅助角公式. 当 $a$, $b$ 中有负数时, 也可以作类似的变形.
</p>
<p>辅助角公式是和角、差角的正弦、余弦公式的逆向运用, 所以提出 $r$ 后, 需参考后者的形式适当变形, 重点是将两个系数化为同一个锐角的正弦、余弦值. 比如
\[\begin{aligned}
    \sin x+ \sqrt3\cos x
    &= 2\Bigl(\frac12\sin x+ \frac{\sqrt3}2\cos x\Bigr)\\
    &= 2(\cos60^\circ\sin x+ \sin60^\circ\cos x),
\end{aligned}\]
然后就可以逆用和角的正弦公式. 上述最后一式也可写为
\[2(\sin30^\circ\sin x+ \cos30^\circ\cos x),\]
或者写为
\[2(\sin30^\circ\sin x+ \sin60^\circ\cos x).\]
但是很明显, 只有前一种写法能逆用差角的余弦公式, 后一种写法无法继续合并.
</p>

<p>在和角的三角函数公式中令 $\beta=\alpha$, 可得二倍角的三角函数公式
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

<myexample>
<p>如图, 在平面直角坐标系中, 以 $Ox$ 正半轴为始边作两个锐角 $\alpha$, $\beta$, 它们的终边分别与单位圆交于点 $A$, $B$, 横坐标分别为 $\dfrac{\sqrt2}{10}$, $\dfrac{2\sqrt5}{5}$. 求 $\tan(\alpha+\beta)$ 和 $\alpha+2\beta$ 的值.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0307-1150-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>由三角函数值的定义, 点 $A$ 的坐标为 $(\cos\alpha,\sin\alpha)$, 点 $B$ 的坐标为 $(\cos\beta,\sin\beta)$. 结合已知可得,
    \[\cos\alpha= \dfrac{\sqrt2}{10},\ 
        \sin\alpha= \dfrac{7\sqrt2}{10},\quad
    \cos\beta= \dfrac{2\sqrt5}{5},\ 
        \sin\beta= \dfrac{\sqrt5}{5},\]
    所以 $\tan\alpha= 7$, $\tan\beta= \dfrac12$, 而
    \[\tan(\alpha+\beta)
        = \frac{\tan\alpha+ \tan\beta}{1- \tan\alpha\tan\beta}
        = -3.\]
</p>
<p>同理, 由 $\tan(\alpha+2\beta)= \tan((\alpha+\beta)+ \beta)$ 可以算出 $\tan(\alpha+2\beta)= -1$. 而已知表明,
    \[\alpha\in \Bigl(\frac\pi4,\frac\pi2\Bigr),\ 
        \beta\in \Bigl(0,\frac\pi4\Bigr),\quad\text{即}\quad 
    \alpha+2\beta\in \Bigl(\frac\pi4,\pi\Bigr),\]
    所以 $\alpha+2\beta= \dfrac{3\pi}4$.
</p>
</mysolution>
<myremark>
    <p>通过求角的三角函数值可以确定角的大小, 但是需要根据题中角的取值范围选择合适的三角函数值, 以保证能得到唯一确定的角的大小. 例如, 若角的取值范围是 $(0,\pi)$, 则优先考虑余弦值; 若角的取值范围是 $\Bigl(-\dfrac\pi2,\dfrac\pi2\Bigr)$, 则优先考虑正弦值. 对前述两个取值范围, 均可以考虑正切值 (为什么?).
</p>
</myremark>

<myexample>
<p>若 $|\cos\theta|= \dfrac15$, $\dfrac{5\pi}{2}< \theta< 3\pi$, 求 $\sin\dfrac\theta2$ 的值.
</p>
</myexample>
<mysolution>
    <p>由题意, $\cos\theta< 0$, 所以 $\cos\theta= -\dfrac15$, 即
    \[1- 2\sin^2\frac\theta2= -\dfrac15,\quad\text{即}\quad
        \sin^2\frac\theta2= \frac35.\]
    因为 $\dfrac{5\pi}{4}< \dfrac\theta2< \dfrac{3\pi}2$, 所以 $\sin\dfrac\theta2< 0$, 故 $\sin\dfrac\theta2= -\dfrac{\sqrt{15}}{5}$.
</p>
</mysolution>
</p>
<p><myexample>
<p>比较大小: $a= \dfrac{\sqrt2}{2}(\sin17^\circ+ \cos17^\circ)$, $b= 2\cos^2 13^\circ- 1$, $c=\dfrac{\sqrt3}{2}$.
</p>
</myexample>
<mysolution>
    <p>由于 $a$, $b$ 均不能计算具体值, 所以应将三者转化为同名 (即同为正弦或同为余弦) 三角函数式, 利用对应函数的单调性比较大小. 因为
    \[\begin{aligned}
        a&= \frac{\sqrt2}{2}(\sin17^\circ+ \cos17^\circ)\\
        &= \cos45^\circ\sin17^\circ+ \sin45^\circ\cos17^\circ\\
        &= \sin(17^\circ+ 45^\circ)= \sin62^\circ,
    \end{aligned}\]
    而 $b= \cos 26^\circ= \sin 64^\circ$, $c= \sin 60^\circ$, 由正弦函数在 $(0^\circ, 90^\circ)$ 上单调递增可知, $b>a>c$.
</p>
</mysolution>
<myremark>
    <p>上题对 $b$ 的变形用了辅助角公式 $\cos\alpha= \sin(90^\circ- \alpha)$. 此外, 也可以将 $a$, $b$, $c$ 分别化为 $\cos28^\circ$, $\cos26^\circ$, $\cos30^\circ$, 利用余弦函数在 $(0^\circ, 90^\circ)$ 上单调递减仍可得上述结果.
</p>
</myremark>

<myexample>
<p>(1) 化简: $\dfrac1{\sin10^\circ}- \dfrac{\sqrt3}{\cos10^\circ}$;\quad
    (2) 验证: $\dfrac{1- \cos2\theta}{1+ \cos2\theta}= \tan^2\theta$.
</p>
</myexample>
<mysolution>
    <p>(1) 通分后用辅助角公式和二倍角公式, 原式化为
    \[\begin{aligned}
        & \frac{\cos10^\circ- \sqrt3\sin10^\circ}{\sin10^\circ\cos10^\circ}
        = \frac{2\Bigl(\dfrac12 \cos10^\circ- \dfrac{\sqrt3}{2}\sin10^\circ\Bigr)}{\dfrac12\sin20^\circ}\\
        ={}& \frac4{\sin20^\circ}(\sin30^\circ\cos10^\circ- \cos30^\circ\sin10^\circ)\\
        ={}& \frac4{\sin20^\circ}\sin(30^\circ- 10^\circ)
         = 4.
    \end{aligned}\]
</p>
<p>(2) 将二倍角公式 $\cos2\theta= 1-2\sin^2\theta= 2\cos^2\theta-1$ 分别代入分式的分子和分母, 可得
    \[\dfrac{1- (1-2\sin^2\theta)}{1+ (2\cos^2\theta-1)}
        = \frac{\sin^2\theta}{\cos^2\theta},\]
    此即为 $\tan^2\theta$.
</p>
</mysolution>

