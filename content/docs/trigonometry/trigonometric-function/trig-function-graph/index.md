---
# bookCollapseSection: true
title: 三角函数图象
weight: 6
bookHidden: true
prevPage: /docs/trigonometry/trigonometric-function/trig-sum-prod
prevPageTitle: 和差化积公式与积化和差公式
nextPage: /docs/trigonometry/sine-cosine-law
nextPageTitle: 正弦定理与余弦定理
---

# 三角函数图象

<p>根据三角函数线可以分别描点画图，从而作出正弦函数 $y=\sin x$ 和余弦函数 $y=\cos x$ 的图形. 具体做法如下:
</p>
<p>(1) 由正弦线和余弦线可知, 正、余弦值的最小正周期为 $2\pi$, 且在 $[0,2\pi]$ (一个周期) 内的取值为
</p>
<p>{\extrarowheight=7pt\small
    <center>
      \begin{tabular}{c|ccccccccc}
        $x$ & $0$ & $\dfrac\pi6$ & $\dfrac\pi4$ & $\dfrac\pi3$ 
            & $\dfrac\pi2$ & $\dfrac{2\pi}3$ & $\dfrac{3\pi}4$ 
            & $\dfrac{5\pi}6$ & $\pi$ \\
        $y=\sin x$ & $0$ & $\dfrac12$ & $\dfrac{\sqrt2}2$ 
        & $\dfrac{\sqrt3}2$ & $1$ & $\dfrac{\sqrt3}2$ 
        & $\dfrac{\sqrt2}2$  & $\dfrac12$ & $0$\\
        $x$ & & $\dfrac{7\pi}6$ & $\dfrac{5\pi}4$ & $\dfrac{4\pi}3$ 
            & $\dfrac{3\pi}2$ & $\dfrac{5\pi}3$ & $\dfrac{7\pi}4$ 
            & $\dfrac{11\pi}6$ & $2\pi$\\
        $y=\sin x$ & & $-\dfrac12$ & $-\dfrac{\sqrt2}2$ 
            & $-\dfrac{\sqrt3}2$ & $-1$ & $-\dfrac{\sqrt3}2$ 
            & $-\dfrac{\sqrt2}2$  & $-\dfrac12$ & $0$
      \end{tabular}
    </center>
    <center>
      \begin{tabular}{c|ccccccccc}
        $x$ & $0$ & $\dfrac\pi6$ & $\dfrac\pi4$ & $\dfrac\pi3$ 
            & $\dfrac\pi2$ & $\dfrac{2\pi}3$ & $\dfrac{3\pi}4$ 
            & $\dfrac{5\pi}6$ & $\pi$ \\
        $y=\cos x$ & $1$ & $\dfrac{\sqrt3}2$ 
            & $\dfrac{\sqrt2}2$  & $\dfrac12$ & $0$ 
            & $-\dfrac12$ & $-\dfrac{\sqrt2}2$ 
            & $-\dfrac{\sqrt3}2$ & $-1$\\
        $x$ & & $\dfrac{7\pi}6$ 
            & $\dfrac{5\pi}4$ & $\dfrac{4\pi}3$ & $\dfrac{3\pi}2$ 
            & $\dfrac{5\pi}3$ & $\dfrac{7\pi}4$ & $\dfrac{11\pi}6$ 
            & $2\pi$\\
        $y=\cos x$ & & $-\dfrac{\sqrt3}2$ & $-\dfrac{\sqrt2}2$
            & $-\dfrac12$ & $0$ & $\dfrac12$ & $\dfrac{\sqrt2}2$ 
            & $\dfrac{\sqrt3}2$ & $1$
      \end{tabular}
    </center>
    }
</p>
<p>(2) 由此可以画出 $y=\sin x$ 和 $y=\cos x$ 的图形, 即
</p>
<p><center>\small
    \begin{tikzpicture}[scale=0.7]
      \draw[\myaxisarrow] (-3.5,0) -- (10,0) node[below] {$x$};
      \draw[\myaxisarrow] (0,-1.5) -- (0,1.5) node[left] {$y$};
      \draw[line width=0.4pt, smooth, color=red, samples=100, domain=-3.14:9.42] 
        plot(\x,{sin(\x*180/pi)});
      \draw[line width=0.6pt, smooth, color=blue, samples=100, domain=-3.14:9.42] 
        plot(\x,{cos(\x*180/pi)});
</p>
<p>\draw[densely dashed] (-3.5,1)--(9.7,1) (-3.5,-1)--(9.7,-1);
      \draw (0,1) node[anchor=45] {$1$} (0,-1) node[anchor=45] {$-1$};
      \draw (0.4,-0.4) node {$O$};
      \draw (2*pi,-0.2) node[below] {$2\pi$};
      \draw (pi,-0.2) node[below] {$\pi$};
      \draw (3*pi,-0.2) node[below] {$3\pi$};
      \draw (-pi,-0.2) node[below] {$-\pi$};
      \draw (pi,1) node[above] {$y=\sin x$};
      \draw (2.3,-1.2) node[below] {$y=\cos x$};
    \end{tikzpicture}
  </center>
</p>
<p>图中画了两个周期内 (即 $[-\pi,3\pi]$ 上) 的图形, 该图形可根据正、余弦函数的周期性, 通过 $[0,2\pi]$ 上的图形平移得到. 正、余弦函数的图形都是“波浪线”, 有无穷多个对称轴和对称中心, 且这两者的周期均为 $\pi$ 即原始周期 $2\pi$ 的一半. 还可以由图看出, 对称轴对应的函数值为 $\pm1$, 而对称中心对应的函数值为 $0$.
</p>
<p>由图形可以列出以下性质表 (结合图形记忆, 表中 $k\in\integralnum$):
  {\extrarowheight=7pt\small
  <center>
    \begin{tabular}{cccccc}
           & 定义域 & 值域 & 最小正周期 & 对称中心 (点) & 对称轴 \\
       \hline
      $y=\sin x$ & $\realnum$ & $[-1,1]$ & $2\pi$ & 
        $(k\pi,0)$ & $x=\dfrac{\pi}2+k\pi$\\
      $y=\cos x$ & $\realnum$ & $[-1,1]$ & $2\pi$ & 
        $\Big(\dfrac{\pi}2+k\pi,0\Big)$ & $x=k\pi$
    \end{tabular}
  </center>
  <center>
    \begin{tabular}{ccc}
           & 奇偶性 & 单调性 \\
       \hline
      $y=\sin x$ & 奇 &
        $\Bigl[-\dfrac{\pi}2+2k\pi,\dfrac{\pi}2+2k\pi\Bigr]\nearrow$,
        $\Bigl[\dfrac{\pi}2+2k\pi,\dfrac{3\pi}2+2k\pi\Bigr]\searrow$   \\
      $y=\cos x$ & 偶 & 
        $\Bigl[-\pi+2k\pi,2k\pi\Bigr]\nearrow$, 
        $\Bigl[2k\pi,\pi+2k\pi\Bigr]\searrow$
    \end{tabular}
  </center>}


<myexample>
<p>求下列函数的周期:
</p>
<p>(1) $y=\cos\dfrac{x}2$;\quad (2) $y=\cos2x$;\quad 
    (3) $y=\biggl|\cos\dfrac{x}2\biggr|$;\quad (4) $y=|\cos2x|$.
</p>
</myexample>
<mysolution>
    <p>本题主要利用结论: $y=\sin\omega x$, $y=\cos\omega x$ 的 (最小正) 周期 $T= \dfrac{2\pi}{|\omega|}$.
</p>
<p>(1) $y=\cos\dfrac{x}2$ 的周期为 $\dfrac{2\pi}{1/2}= 4\pi$.
</p>
<p>(2) $y=\cos2x$ 的周期为 $\dfrac{2\pi}{2}= \pi$.
</p>
<p>(3) $y=\cos\dfrac{x}2$ 的周期为 $\dfrac{2\pi}{1/2}= 4\pi$, 图形仍为“波浪线”, 将其在 $x$ 轴下方的图形翻折到上方后可得 $y=\biggl|\cos\dfrac{x}2\biggr|$ 的图形, 所以后者的周期为 $2\pi$.
</p>
<p>(4) 方法同上, 可知 $y=|\cos2x|$ 的周期为 $\dfrac\pi2$.
</p>
<p></p>
</mysolution>
</p>
<p><myexample>
<p>设函数 $f(x)= \sin\biggl(2x- \dfrac\pi2\biggr)$, $x\in\realnum$, 判断 $f(x)$ 的周期性和奇偶性.
</p>
</myexample>
<mysolution>
    <p>由诱导公式, $f(x)= -\cos2x$, 所以其为偶函数且周期为 $\pi$.
</p>
</mysolution>
</p>
<p><myexample>
<p>判断下列各函数中, 哪些最小正周期为 $\pi$ 且图形关于点 $\biggl(\dfrac{7\pi}{12},0\biggr)$ 对称:
</p>
<p>(1) $y=\sin\biggl(\dfrac{x}2+ \dfrac\pi6\biggr)$;\quad
    (2) $y=\sin\biggl(2x+ \dfrac\pi6\biggr)$;\quad
    (3) $y=\cos\biggl(\dfrac{x}2- \dfrac\pi6\biggr)$;\quad
    (4) $y=\sin\biggl(\dfrac{x}2- \dfrac\pi6\biggr)$.
</p>
</myexample>
<mysolution>
    <p>上述四个函数图形均为“波浪线”, 最小正周期为 $\pi$ 表明 $x$ 的系数 (的绝对值) 为 $2$ (由周期公式可得), 图形关于点 $\biggl(\dfrac{7\pi}{12},0\biggr)$ 对称表明该点在图形上. 根据这两个条件验证, 可知只有 (4) 符合题意.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)=2\sin(\omega x+ \varphi)$, 且对于任意的 $x$, 都有 
    \[f\biggl(\dfrac\pi6+x\biggr)= f\biggl(\dfrac\pi6-x\biggr),\]
    求 $f\biggl(\dfrac\pi6\biggr)$ 的值.
</p>
</myexample>
<mysolution>
    <p>式子 $f\biggl(\dfrac\pi6+x\biggr)= f\biggl(\dfrac\pi6-x\biggr)$ 表明 $f(x)$ 的图形以 $x=\dfrac\pi6$ 为对称轴. 根据三角函数图形的特征, 对称轴对应的是正、余弦函数的最值, 所以 $f\biggl(\dfrac\pi6\biggr)=\pm1$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \cos\biggl(\dfrac{x}2+ \dfrac\pi3\biggr)$, 求其图形的对称中心.
</p>
</myexample>
<mysolution>
    <p>三角函数图形的对称中心是图形与 $x$ 轴的交点, 所以特征是对应的函数值为 $0$. 令 $\cos\biggl(\dfrac{x}2+ \dfrac\pi3\biggr)= 0$, 整体考虑, 可以解得
    \[\dfrac{x}2+ \dfrac\pi3= \frac\pi2+ k\pi,\quad\text{即}\quad
        x= \frac\pi3+ 2k\pi,\]
    所以所求对称中心为 $\biggl(\dfrac\pi3+ 2k\pi,0\biggr)$, $k\in\integralnum$.
</p>
</mysolution>
</p>
<p><myexample>
<p>函数 $y=\sin\biggl(\dfrac12 x- \varphi\biggr)$ ($0\leqslant \varphi\leqslant \pi$) 是 $\realnum$ 上的偶函数, 求 $\varphi$ 的值.
</p>
</myexample>
<mysolution>
    <p>题中的函数图形关于 $y$ 轴即 $x=0$ 对称, 而三角函数图形的对称轴对应的正、余弦值为 $\pm1$, 所以
    \[\sin\biggl(\dfrac12 \cdot 0- \varphi\biggr)= \pm1,
        \quad\text{即}\quad \sin\varphi=\pm1.\]
    由 $0\leqslant \varphi\leqslant \pi$ 可知, 必有 $\varphi= \dfrac\pi2$.
</p>
</mysolution>
</p>
<p><myexample>
<p>求函数 $y= 2\sin\biggl(x-\dfrac\pi4\biggr)$ 的对称轴.
</p>
</myexample>
<mysolution>
    <p>因为三角函数图形的对称轴对应的正、余弦值为 $\pm1$, 所以令 (注意没有系数 $2$) $\sin\biggl(x-\dfrac\pi4\biggr)=\pm1$, 解得
    \[x-\dfrac\pi4= \dfrac\pi2+k\pi,\quad\text{即}\quad
        x= \dfrac{3\pi}4+k\pi,\]
    因此所求对称轴为 $x= \dfrac{3\pi}4+k\pi$, $k\in\integralnum$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>本次答疑反复用到三角函数图形的对称轴、对称中心的特征:
</p>
<p>(1) 对称轴对应的正、余弦值为 $\pm1$;
</p>
<p>(2) 对称中心是图形与 $x$ 轴的交点, 对应的函数值为 $0$.
</p>
</myremark>

<myexample>
<p>已知 $f(x)= \dfrac12\sin\biggl(2x- \dfrac\pi3\biggr)$, $x\in\realnum$.
</p>
<p>(1) 求 $f(x)$ 的最小正周期;
</p>
<p>(2) 求 $f(x)$ 在 $\biggl[-\dfrac\pi4,\dfrac\pi4\biggl]$ 上的最大、最小值.
</p>
</myexample>
<mysolution>
    <p>(1) 最小正周期 $T= \dfrac{2\pi}{|2|}= \pi$.
</p>
<p>(2) 由 $x\in \biggl[-\dfrac\pi4,\dfrac\pi4\biggl]$ 可知, $2x-\dfrac\pi3\in \biggl[-\dfrac{5\pi}6, \dfrac\pi6\biggr]$. 作正弦线 (或由正弦函数图形) 可知,
    \[\sin\biggl(2x- \dfrac\pi3\biggr)\in \biggl[-1,\frac12\biggr],
        \quad\text{即}\quad f(x)\in \biggl[-\frac12,\frac14\biggr].\]
    所以所求最大值为 $\dfrac14$, 最小值为 $-\dfrac12$.
</p>
</mysolution>
</p>
<p><myexample>
<p>求函数 $y=\tan\biggl(\dfrac{x}2+ \dfrac\pi3\biggr)$, $x\in\biggl[0,\dfrac\pi3\biggr)\cup \biggl(\dfrac\pi3,\pi\biggr]$ 的值域.
</p>
</myexample>
<mysolution>
    <p>由 $x\in\biggl[0,\dfrac\pi3\biggr)\cup \biggl(\dfrac\pi3,\pi\biggr]$ 可知 $\dfrac{x}2+ \dfrac\pi3\in \biggl[\dfrac\pi3,\dfrac\pi2\biggr)\cup \biggl(\dfrac\pi2,\dfrac{5\pi}6\biggr]$. 结合正切函数图形和正、余函数弦可知,
    \[y\in\biggl(-\infty, -\tan\frac{5\pi}6\biggr]\cup \biggl[\tan\frac\pi3,+\infty\biggr)
        = \biggl(-\infty, -\frac{\sqrt3}3\biggr]\cup [\sqrt3,+\infty).\]
</p>
<p><center>
        \includegraphics[scale=1.05]{2021-0114-1940-crop}
    </center>
</p>
</mysolution>
</p>
<p>\subsection{三角函数的周期}
</p>
<p>结合三角函数值, 考虑三角函数 $y_1=\sin x$, $y_2=\sin 2x$, $y_3=\sin \dfrac{x}2$ 在一个周期内的图形,
</p>
<p><center>
        \includegraphics[scale=1.2]{2021-0114-1950-crop}
    </center>
</p>
<p>可以知道, 由于 $y_1=\sin x$ 中 $x$ 从 $0$ 变化到 $2\pi$ 时, 函数值的变化恰好为一个完整的周期 ($0\nearrow 1\searrow 0\searrow -1\nearrow 0$), 所以对 $y_2=\sin 2x$ 而言, $x$ 只需从 $0$ 变化到 $\pi$ 就能使得 $2x$ 从 $0$ 变化到 $2\pi$, 确保函数值的变化为一个完整的周期. 同样的, 对 $y_3=\sin \dfrac{x}2$ 而言, $x$ 则需从 $0$ 变化到 $4\pi$ 才能使得 $\dfrac{x}2$ 从 $0$ 变化到 $2\pi$, 从而确保函数值的变化为一个完整的周期. 这说明,  $y_2=\sin 2x$ 的 (最小正) 周期为 $\pi$, 而 $y_3=\sin \dfrac{x}2$ 的 (最小正) 周期为 $4\pi$.
</p>
<p>一般地, 对 $y=\sin\omega x$ ($\omega\neq 0$) 而言, 只需 $\omega x$ 从 $0$ 变化到 $2\pi$, 就能使得函数值的变化为一个完整的周期, 此时 $x$ 从 $0$ 变化到 $\dfrac{2\pi}{\omega}$. 所以 $y=\sin\omega x$ 的 (最小正) 周期为 $T= \dfrac{2\pi}{|\omega|}$ (因为 $\omega$ 可能为负值).
</p>
<p>更一般地, 若 $f(x)$ 的最小正周期为 $T$, 则 $f(ax)$ 的最小正周期为 $\dfrac{T}{|a|}$, 其中 $a\neq 0$. 所以当 $\omega\neq 0$ 时, $y=\cos\omega x$ 的 (最小正) 周期为 $T= \dfrac{2\pi}{|\omega|}$, 而 $y=\tan\omega x$ 的 (最小正) 周期为 $T= \dfrac{\pi}{|\omega|}$.
</p>
<p>此外, 从前面的图形还可以看出, $y_2=\sin 2x$ 的图形可由 $y_1=\sin x$ 的图形沿 $x$ 轴方向关于 $y$ 轴“压缩”得到, 而 $y_3=\sin \dfrac{x}2$ 的图形则可由 $y_1=\sin x$ 的图形沿 $x$ 轴方向关于 $y$ 轴“拉伸”得到.
</p>
<p>一般地, 当 $a\in(0,1)$ 时, 函数 $f(ax)$ 的图形可由 $f(x)$ 的图形关于 $y$ 轴“拉伸”得到; 当 $a\in(1,+\infty)$ 时, 函数 $f(ax)$ 的图形可由 $f(x)$ 的图形关于 $y$ 轴“压缩”得到. 类似于前面的分析可知,“拉伸”或“压缩”的系数均为 $\dfrac1a$.

<p>三角函数图形变换包括上、下、左、右平移和关于 $x$ 轴、$y$ 轴拉伸或压缩, 其中平移变换可参考“2020 年 12 月 6 日答疑记录”, 关于 $y$ 轴的拉伸或压缩变换可参考“2021 年 1 月 4 日答疑记录”.
</p>
<p>例如, 函数 $y=\sin 2x$ 的图形可由函数 $y=\sin x$ 的图形关于 $y$ 轴压缩得到: 
<center>
    纵坐标不变, 横坐标变为原来的 $\dfrac12$ 倍;
</center>
函数 $y=\sin \dfrac12x$ 的图形可由函数 $y=\sin x$ 的图形关于 $y$ 轴拉伸得到: 
<center>
    纵坐标不变, 横坐标变为原来的 $2$ 倍;
</center>
函数 $y=2\sin\biggl(2x+\dfrac{\pi}3\biggr)$ 的图形可由函数 $y=\sin x$ 的图形变换得到, 即
\[\begin{aligned}
    \text{向左平移 $\dfrac{\pi}3$}&\colon y=\sin x\to y=\sin\biggl(x+\frac{\pi}3\biggr),\\
    \text{横坐标变为原来的 $\dfrac12$ 倍}&\colon y=\sin\biggl(x+\frac{\pi}3\biggr)\to y=\sin\biggl(2x+\frac{\pi}3\biggr),\\
    \text{纵坐标变为原来的 $2$ 倍}&\colon y=\sin\biggl(2x+\frac{\pi}3\biggr)\to y=2\sin\biggl(2x+\frac{\pi}3\biggr).
\end{aligned}\]
如果上述最后一个图形变换过程为“先压缩, 后平移”, 则步骤应改为 (为什么?)
\[\begin{aligned}
    \text{横坐标变为原来的 $\dfrac12$ 倍}&\colon y=\sin x\to y=\sin 2x,\\
    \text{向左平移 $\dfrac{\pi}6$}&\colon y=\sin2\to y=\sin\biggl(2x+\frac{\pi}3\biggr).
\end{aligned}\]
</p>
<p>分析三角函数图形变换过程可知, 能改变图形周期的只有“关于 $y$ 轴的拉伸或压缩”(即改变 $x$ 的系数). 由此可以得到, 函数 $y=A\sin(\omega x+\varphi)$ 与 $y=A\cos(\omega x+\varphi)$ 的周期均为 $T=\dfrac{2\pi}{|\omega|}$. 此外, 由函数图形变换还可以知道, 前述两个函数的对称轴对应的正弦 (或余弦) 值为 $\pm1$, 而对称中心对应的正弦 (或余弦) 值为 $0$. 例如函数 $y=2\sin\biggl(2x+\dfrac{\pi}3\biggr)$ 的图形对称轴的横坐标满足
\[2x+\dfrac{\pi}3= \frac\pi2+k\pi,\quad\text{即}\quad
    x= \frac\pi{12}+ \frac{k\pi}2,\ k\in\mathbf{Z},\]
而对称中心的横坐标满足
\[2x+\dfrac{\pi}3= k\pi,\quad\text{即}\quad
    x= -\frac\pi6+ \frac{k\pi}2,\ k\in\mathbf{Z}.\]
</p>
<p>函数的单调性也可以利用图形变换得到. 例如函数 $y=2\sin\biggl(2x+\dfrac{\pi}3\biggr)$ 的单增区间中的 $x$ 值使得正弦值从 $-1$ 连续地变到 $1$, 所以此时
\[2x+\dfrac{\pi}3\in\biggl[-\frac\pi2+2k\pi, 
    \frac\pi2+2k\pi\biggr],\quad\text{即}\quad
    x\in\biggl[-\frac{5\pi}{12}+k\pi, \frac{\pi}{12}+k\pi\biggr],\ k\in\mathbf{Z}.\]
同理可知, 该函数的单减区间为
\[\biggl[\frac\pi{12}+k\pi, \frac{7\pi}{12}+k\pi\biggr],\quad k\in\mathbf{Z}.\]
应注意, 函数 $y=2\sin\biggl(-2x+\dfrac{\pi}3\biggr)$ 的单增区间中的 $x$ 值仍使得正弦值从 $-1$ 连续地变到 $1$, 但是此时 (为什么?)
\[-2x+\dfrac{\pi}3\in\biggl[\frac\pi2+2k\pi, 
    \frac{3\pi}2+2k\pi\biggr],\quad\text{即}\quad
    x\in\biggl[\frac\pi{12}+k\pi, \frac{7\pi}{12}+k\pi\biggr],\ k\in\mathbf{Z}.\]
可类似地求上述两个函数的对称轴.

<myexample>
<p>已知 $\alpha$, $\beta>0$, 则“$\alpha+\beta< \dfrac\pi2$”是“$\sin\alpha< \cos\beta$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>若 $\alpha+\beta< \dfrac\pi2$, 则 $0< \alpha< \dfrac\pi2-\beta< \dfrac\pi2$, 由 $y=\sin x$ 在 $\biggl[0,\dfrac\pi2\biggr]$ 上单调递增可知, 
    \[\sin\alpha< \sin\biggl(\dfrac\pi2-\beta\biggr)= \cos\beta.\]
</p>
<p>反之, 取 $\alpha=\pi$, $\beta=2\pi$ 可知这一组值满足 $\sin\alpha< \cos\beta$, 而 $\alpha+\beta= 3\pi>\dfrac\pi2$.
</p>
<p>综上可知,“$\alpha+\beta< \dfrac\pi2$”是“$\sin\alpha< \cos\beta$”的充分不必要条件.
</p>
</mysolution>

<myexample>
<p>求函数 $f(x)= \sin\biggl(2x+\dfrac{\pi}3\biggr)$ 的单调递减区间.
</p>
</myexample>
<mysolution>
    <p>由正弦函数图形, 当 $f(x)$ 单调递减时,
    \[2x+\dfrac{\pi}3\in \biggl[\frac{\pi}{2}+2k\pi, \frac{3\pi}{2}+2k\pi\biggr],\quad\text{即}\quad
    x\in\biggl[\frac{\pi}{12}+k\pi, \frac{7\pi}{12}+k\pi\biggr],\]
    所以函数 $f(x)$ 的单调递减区间为 $\biggl[\dfrac{\pi}{12}+k\pi, \dfrac{7\pi}{12}+k\pi\biggr]$, $k\in\mathbf{Z}$.
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \sin\biggl(\dfrac12x+ \varphi\biggr)$ ($0\leqslant \varphi\leqslant \dfrac\pi2$), 且满足 $\underline{\qquad}$. 从以下三个条件中任选一个, 补充在横线处:
</p>
<p>(1) $-\dfrac{3\pi}4$ 是函数 $f(x)$ 的一个零点;
</p>
<p>(2) 当 $x=-\dfrac\pi4$ 时, $f(x)= \dfrac{\sqrt2}2$;
</p>
<p>(3) $f(x)$ 的图形的一条对称轴是直线 $x=\dfrac\pi4$,\\
    然后解答下列问题:
</p>
<p>(1) 求函数 $f(x)$ 的周期;
</p>
<p>(2) 求函数 $f(x)$ 的单调增区间;
</p>
<p>(3) 求函数 $f(x)$ 在 $[0,2\pi]$ 上的最大值和最小值.
</p>
</myexample>
<mysolution>
    <p>先以选择条件 (1) 为例, 写出解答过程. 此时
    \[f\biggl(-\dfrac{3\pi}4\biggr)= \sin\biggl(-\frac{3\pi}8+ \varphi\biggr)=0,\]
    则
    \[-\frac{3\pi}8+ \varphi= k\pi,\quad\text{即}\quad \varphi= \frac{3\pi}8+k\pi,\ k\in\integralnum.\]
    因为 $0\leqslant \varphi\leqslant \dfrac\pi2$, 所以 $k=0$ 而 $\varphi= \dfrac{3\pi}8$, 即 $f(x)= \sin\biggl(\dfrac12x+ \dfrac{3\pi}8\biggr)$.
</p>
<p>(1) 由三角函数周期公式, $f(x)$ 的周期为 $T= \dfrac{2\pi}{1/2}= 4\pi$.
</p>
<p>(2) 当 $f(x)$ 单调递增时, 
    \[\dfrac12x+ \dfrac{3\pi}8\in \biggl[-\frac\pi2+2k\pi, \frac\pi2+2k\pi\biggr],\quad\text{即}\quad
    x\in\biggl[-\frac{7\pi}4+4k\pi, \frac\pi4+4k\pi\biggr],\]
    所以 $f(x)$ 的单调递增区间为 $\biggl[-\dfrac{7\pi}4+4k\pi, \dfrac\pi4+4k\pi\biggr],\ k\in\mathbf{Z}$.
</p>
<p>(3) 因为 $x\in[0,2\pi]$, 所以 $\dfrac12x+ \dfrac{3\pi}8\in\biggl[\dfrac{3\pi}8, \dfrac{11\pi}8\biggr]$. 画正弦线或正弦函数图形可知, $f(x)= \sin\biggl(\dfrac12x+ \dfrac{3\pi}8\biggr)$ 在 $[0,2\pi]$ 上的最大值为 $1$, 最小值为 $\sin\dfrac{11\pi}8$.
</p>
<p>若选择条件 (2), 则
    \[f\biggl(-\dfrac\pi4\biggr)=  \sin\biggl(-\frac\pi8+ \varphi\biggr)= \dfrac{\sqrt2}2,\]
    所以
    \[-\frac\pi8+ \varphi= \frac{\pi}4+k\pi\ \text{或}\ \frac{3\pi}4+k\pi,\]
    即
    \[\varphi= \frac{3\pi}8+2k\pi\ \text{或}\ \frac{7\pi}8+2k\pi,\quad k\in\integralnum.\]
    又因为 $0\leqslant \varphi\leqslant \dfrac\pi2$, 所以 $k=0$ 而 $\varphi= \dfrac{3\pi}8$, 其余过程同前述推导.
</p>
<p>若选择条件 (3), 则由对称轴的特征可知,
    \[f\biggl(\dfrac{\pi}4\biggr)= \sin\biggl(\frac{\pi}8+ \varphi\biggr)=\pm1,\]
    则
    \[\frac{\pi}8+ \varphi= \frac\pi2+k\pi,\quad\text{即}\quad \varphi= \frac{3\pi}8+k\pi,\ k\in\integralnum.\]
    同样可得 $\varphi= \dfrac{3\pi}8$.
</p>
</mysolution>

<myexample>
<p>“$m=\dfrac{5\pi}{12}$”是“函数 $f(x)= \cos\biggl(2x+\dfrac\pi6\biggr)$ 的图形关于直线 $x=m$ 对称”的什么条件?
</p>
</myexample>
<mysolution>
    <p>函数 $f(x)= \cos\biggl(2x+\dfrac\pi6\biggr)$ 的图形对称轴的横坐标满足
    \[2x+\dfrac\pi6= k\pi,\quad\text{即}\quad
        x= -\frac\pi{12}+\frac{k\pi}2,\ k\in\mathbf{Z}.\]
    因为 $m=\dfrac{5\pi}{12}$ 仅对应 $k=1$ 的情形, 所以“$m=\dfrac{5\pi}{12}$”是“函数 $f(x)= \cos\biggl(2x+\dfrac\pi6\biggr)$ 的图形关于直线 $x=m$ 对称”的充分而不必要条件.
</p>
</mysolution>

<myexample>
<p>“$\alpha= k\pi+\beta$, $k\in\mathbf{Z}$”是“$\tan\alpha= \tan\beta$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)= \tan x$ 的最小正周期为 $\pi$, 所以大部分时候, 由 $\alpha= k\pi+\beta$ 可得 $\tan\alpha= \tan\beta$. 但是, $f(x)= \tan x$ 中 $x\neq \dfrac\pi2+k\pi$, 因此当 $\alpha= \dfrac\pi2+k\pi$ 时, $\tan\alpha$ 无意义.
</p>
<p>反之, 若 $\tan\alpha= \tan\beta$, 则必有
    \[\alpha= k\pi+\beta\neq \dfrac\pi2+k'\pi,\quad k\in\mathbf{Z}.\]
    所以“$\alpha= k\pi+\beta$, $k\in\mathbf{Z}$”是“$\tan\alpha= \tan\beta$”的必要不充分条件. 
</p>
</mysolution>
<myremark>
    <p>利用正弦线、余弦线可知,
    \[\begin{gathered}
        \sin\alpha= \sin\beta \Leftrightarrow
            \alpha= \beta+2k\pi\ \text{或}\ \pi-\beta+2k\pi,\ 
            k\in\mathbf{Z};\\
        \cos\alpha= \cos\beta \Leftrightarrow
            \alpha= \beta+2k\pi\ \text{或}\ -\beta+2k\pi,\ 
            k\in\mathbf{Z}.
    \end{gathered}\]
</p>
</myremark>

<myexample>
<p>已知函数 $f(x)= \sin(\omega x+\varphi)$, 其中 $\omega>0$, $\varphi\in\biggl(0,\dfrac\pi2\biggr)$, 再从如下条件中任意选两个作为已知条件:
</p>
<p>(1) $f(x)$ 的最小正周期为 $\pi$;
</p>
<p>(2) $f(x)$ 的图形关于点 $\biggl(-\dfrac\pi6,0\biggr)$ 对称;
</p>
<p>(3) $f(x)$ 的图形关于直线 $x= \dfrac\pi{12}$ 对称.
</p>
<p>求 $f(x)$ 的单调递增区间, 以及其在 $\biggl[0,\dfrac\pi2\biggr]$ 上的值域.
</p>
</myexample>
<mysolution>
    <p>不妨选条件 (1) 和 (3). 由 (1), $\dfrac{2\pi}{\omega}= \pi$, 所以 $\omega=2$. 由 (3) 和对称轴对应图形的最高点或最低点, 
    \[f\biggl(\dfrac\pi{12}\biggr)= \pm 1,\quad\text{即}\quad
        \sin\biggl(2\cdot \frac\pi{12}+ \varphi\biggr)= \pm 1,\]
    解得
    \[\frac\pi{6}+ \varphi= \frac\pi2+ k\pi,\quad\text{即}\quad
        \varphi= \frac\pi3+ k\pi,\ k\in\mathbf{Z}.\]
    因为 $\varphi\in\biggl(0,\dfrac\pi2\biggr)$, 所以 $k=0$, $\varphi= \dfrac\pi3$. 因此 $f(x)= \sin\biggl(2x+\dfrac\pi3\biggr)$.
</p>
<p>$f(x)$ 的单调递增区间满足 
    \[2x+\dfrac\pi3\in \biggl[-\frac\pi2+2k\pi, \frac\pi2+2k\pi\biggr],\]
    解得
    \[x\in\biggl[-\frac{5\pi}{12}+k\pi, \frac{\pi}{12}+k\pi\biggr],\quad k\in\mathbf{Z}.\]
    由 $x\in\biggl[0,\dfrac\pi2\biggr]$ 知 $2x+\dfrac\pi3\in \biggl[\dfrac\pi3,\dfrac{4\pi}3\biggr]$. 再作正弦线可知, $f(x)\in \biggl[-\dfrac{\sqrt3}2, 1\biggr]$.
</p>
</mysolution>
<myremark>
    <p>上题若选条件 (1) 和 (2), 则计算过程类似, 且也能得到相同的答案; 若选条件 (2) 和 (3), 只能算出 $\varphi=\dfrac\pi3$, 无法算出 $\omega$ 为确定值.
</p>
</myremark>

<myexample>
<p>求分别满足下列条件的 $a$ 的取值范围:
</p>
<p>(1) $\forall\, x\in\mathbf{R}$, $\sin x+a>0$ 恒成立;
</p>
<p>(2) $\forall\, x\in[0,\pi]$, $\sin x+a< 0$ 恒成立;
</p>
<p>(3) $\forall\, x\in\biggl[0,\dfrac\pi 2\biggr]$, $\cos \biggl(2x+ \dfrac\pi3\biggr)+ a< 0$ 恒成立.
</p>
</myexample>
<mysolution>
    <p>仍用最值来计算.
</p>
<p>(1) 不等式左边最小值大于零, 即
    \[-1+a>0,\quad\text{解得}\quad a\in(1,+\infty).\]
</p>
<p>(2) 不等式左边最大值小于零, 即
    \[1+a< 0,\quad\text{解得}\quad a\in(-\infty,-1).\]
</p>
<p>(3) 不等式左边最大值小于零. 由 $x\in\biggl[0,\dfrac\pi 2\biggr]$ 可得
    \[2x+ \dfrac\pi3\in\biggl[\dfrac\pi3,\dfrac{4\pi}3\biggr],\]
    所以 $\cos \biggl(2x+ \dfrac\pi3\biggr)\in\biggl[-1,\dfrac12\biggr]$, 即
    \[\frac12+a< 0,\quad\text{解得}\quad a\in\biggl(-\infty,-\frac12\biggr).\]
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \sin x-\sqrt3\cos x$, 求其最小正周期和 $f\Bigl(\dfrac\pi3\Bigr)$ 的值, 以及 $f(x)$ 在 $\Bigl[\dfrac\pi2,\dfrac{3\pi}2\Bigr]$ 上的值域.
</p>
</myexample>
<mysolution>
    <p>由辅助角公式,
    \[\begin{aligned}
        f(x)&= 2\biggl(\frac12\sin x- \frac{\sqrt3}2\cos x\biggr)\\
        &= 2\Bigl(\cos\frac\pi3\sin x- \sin\frac\pi3\cos x\Bigr)\\
        &= 2\sin\Bigl(x- \frac\pi3\Bigr),
    \end{aligned}\]
    所以 $f(x)$ 的最小正周期为 $2\pi$, $f\Bigl(\dfrac\pi3\Bigr)=0$. 当 $x\in\Bigl[\dfrac\pi2,\dfrac{3\pi}2\Bigr]$ 时,
    \[x- \frac\pi3\in \Bigl[\dfrac\pi6,\dfrac{7\pi}6\Bigr],\quad
        \text{可知}\quad 
        \sin\Bigl(x- \frac\pi3\Bigr)\in \Bigl[-\dfrac12,1\Bigr],\]
    故 $f(x)\in[-1,2]$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \sin x\cos x+ \sqrt3\cos^2 x$, 求其单调递减区间和 $f\Bigl(\dfrac\pi3\Bigr)$ 的值.
</p>
</myexample>
<mysolution>
    <p>逆用二倍角公式知,
    \[\begin{aligned}
        f(x)&= \frac12\sin 2x+ \sqrt3\cdot\frac{1+\cos2x}{2}\\
        &= \cos\frac\pi3\sin2x+ \sin\frac\pi3\cos 2x+ \frac{\sqrt3}2\\
        &= \sin\Bigl(2x+ \frac\pi3\Bigr)+ \frac{\sqrt3}2,
    \end{aligned}\]
    则 $f\Bigl(\dfrac\pi3\Bigr)= \dfrac{\sqrt3}2$. $f(x)$ 的单调递减区间满足
    \[\begin{gathered}
        2x+ \frac\pi3\in \Bigl[-\frac\pi2+2k\pi, 
            \frac\pi2+2k\pi\Bigr],\quad k\in\mathbf{Z},\\
        x\in \Bigl[-\frac{5\pi}{12}+k\pi, 
            \frac{\pi}{12}+2k\pi\Bigr],\quad k\in\mathbf{Z}.
    \end{gathered}\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= 2\cos\Bigl(x-\dfrac\pi3\Bigr)\sin x$, 求其最小正周期和对称轴方程.
</p>
</myexample>
<mysolution>
    <p>先展开再合并,
    \[\begin{aligned}
        f(x)&= 2\Bigl(\cos x\cos\dfrac\pi3+ \sin x\sin\dfrac\pi3\Bigr)\sin x\\
        &= (\cos x+\sqrt3\sin x)\sin x\\
        &= \frac12\sin 2x+ \sqrt3\cdot\frac{1-\cos2x}{2}\\
        &= \cos\frac\pi3\sin 2x+ \sin\frac\pi3\cos 2x+ \frac{\sqrt3}2\\
        &= \sin\Bigl(2x+ \frac\pi3\Bigr)+ \frac{\sqrt3}2.
    \end{aligned}\]
    由此可知, $f(x)$ 的最小正周期为 $\pi$, 对称轴满足
    \[\begin{gathered}
        2x+ \frac\pi3= \frac\pi2+k\pi,\quad k\in\mathbf{Z},\\
        x= \frac\pi{12}+k\pi,\quad k\in\mathbf{Z}.
    \end{gathered}\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $g(x)= \sin\Bigl(x-\dfrac\pi6\Bigr)$, $h(x)= \cos x$, 分别设
</p>
<p>(1) $f(x)= g(x)+h(x)$;\quad (2) $f(x)= g(x)h(x)$,\\
    求 $f(x)$ 的最小正周期和在 $\Bigl[0,\dfrac\pi2\Bigr]$ 上的值域.
</p>
</myexample>
<mysolution>
    <p>本题的解法与上题相同, 均为先拆开后合并.
</p>
<p>(1) 由题意,
    \[\begin{aligned}
        f(x)&= \sin\Bigl(x-\dfrac\pi6\Bigr)+ \cos x\\
        &= \frac{\sqrt3}{2}\sin x- \frac12\cos x+ \cos x\\
        &= \sin\frac\pi3\sin x+ \cos\frac\pi3\cos x\\
        &= \cos\Bigl(x-\frac\pi3\Bigr),
    \end{aligned}\]
    所以最小正周期为 $2\pi$. 当 $x\in\Bigl[0,\dfrac\pi2\Bigr]$ 时,
    \[x-\frac\pi3\in \Bigl[-\frac\pi3,\dfrac\pi6\Bigr],\quad
        \text{可知}\quad
        f(x)\in\biggl[\frac12,\frac{\sqrt3}{2}\biggr].\]
</p>
<p>(2) 本小题略微复杂一点,
    \[\begin{aligned}
        f(x)&= \sin\Bigl(x-\dfrac\pi6\Bigr)\cos x\\
        &= \biggl(\frac{\sqrt3}{2}\sin x- \frac12\cos x\biggr)\cos x\\
        &= \frac{\sqrt3}{2}\cdot \frac{\sin x}2- \frac12\cdot \frac{1+\cos 2x}2\\
        &= \frac12\Bigl(\cos\frac\pi6\sin2x- \sin\frac\pi6\cos2x\Bigr)- \frac14,\\
        &= \frac12\sin\Bigl(2x-\frac\pi6\Bigr)- \frac14,
    \end{aligned}\]
    所以最小正周期为 $\pi$. 当 $x\in\Bigl[0,\dfrac\pi2\Bigr]$ 时,
    \[2x-\frac\pi6\in \Bigl[-\frac\pi6,\dfrac{5\pi}6\Bigr],\quad
        \text{可知}\quad
        f(x)\in\Bigl[-\frac12,\frac14\Bigr].\]
</p>
</mysolution>

<myexample>
<p>将函数 $f(x)= \sin\Bigl(x+ \dfrac\pi3\Bigr)$ 的图形上所有点的横坐标变为原来的 $2$ 倍, 纵坐标不变; 再向右平移 $\dfrac\pi6$ 个单位长度后得到函数 $g(x)= \sin(\omega x+ \varphi)$ ($\omega>0$, $|\varphi|< \dfrac\pi2$) 的图形, 确定 $\omega$ 和 $\varphi$ 的值.
</p>
</myexample>
<mysolution>
    <p>前一次变换得到 $f_1(x)= \sin\Bigl(\dfrac12 x+ \dfrac\pi3\Bigr)$, 后一次变换得到
    \[\begin{aligned}
        g(x)
        &= f_1\Bigl(x- \dfrac\pi6\Bigr)
         = \sin\Bigl(\dfrac12 \Bigl(x- \frac\pi6\Bigr)+ \dfrac\pi3\Bigr)\\
        &= \sin\Bigl(\frac12x+ \frac{\pi}{4}\Bigr),
    \end{aligned}\]
    所以 $\omega= \dfrac12$, $\varphi= \dfrac\pi4$.
</p>
</mysolution>
</p>
<p><myexample>
<p>将函数 $f(x)= \sin2x- \sqrt3\cos2x$ 的图形向左平移 $\dfrac\pi6$ 个单位长度, 得到函数 $g(x)$ 的图形, 求 $g\Bigl(\dfrac{5\pi}{6}\Bigr)$ 的值.
</p>
</myexample>
<mysolution>
    <p>此题虽然可以直接代入求值, 但先化简再求值, 会减小计算量. 由辅助角公式,
    \[f(x)= 2\Bigl(\frac12\sin2x- \frac{\sqrt3}2\cos2x\Bigr)
        = 2\sin(2x- \frac\pi3),\]
    所以 $g(x)= f\Bigl(x+\dfrac\pi6\Bigr)= 2\sin2x$, 而 $g\Bigl(\dfrac{5\pi}{6}\Bigr)= -\sqrt3$.
</p>
</mysolution>
</p>
<p><myexample>
<p>函数 $f(x)= A\sin(\omega x+ \varphi)$ ($A>0$, $\omega>0$, $|\varphi|< \dfrac\pi2$) 的部分图形如下图所示, 求 $\omega$ 的值和 $f(x)$ 在 $\Bigl[\dfrac\pi3, \pi\Bigr]$ 上的零点.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0314-1740-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>由图可知, $A=2$, 最小正周期 $T$ 满足 
    \[\dfrac{T}{2}= \dfrac\pi3-\Bigl(-\dfrac\pi6\Bigr),\quad
    \text{即}\quad T= \pi,\]
    所以 $\omega= \dfrac{2\pi}{T}= 2$. 由图可知 $f(x)$ 有零点 $\dfrac12\Bigl[\Bigl(-\dfrac\pi6\Bigr)+ \dfrac\pi3\Bigr]= \dfrac\pi{12}$, 所以零点的一般表达式为
    \[\dfrac\pi{12}+ k\cdot\frac{T}{2}
        = \dfrac\pi{12}+ \frac{k\pi}2,\quad k\in\integralnum.\]
    当 $x\in\Bigl[\dfrac\pi3, \pi\Bigr]$ 时, $k=1$, 对应零点 $\dfrac{7\pi}{12}$.
</p>
</mysolution>
<myremark>
    <p>上题也可以先求 $\varphi$, 再求零点的表达式, 最后根据题意确定零点. 具体过程为: 因为 $f\Bigl(\dfrac\pi3\Bigr)=2$, 所以 $\sin\Bigl(2\cdot \dfrac\pi3+\varphi\Bigr)=1$, 即
    \[\begin{gathered}
        \dfrac{2\pi}3+\varphi= \dfrac\pi2+2k\pi,\quad k\in\integralnum,\\
        \varphi= -\dfrac\pi6+2k\pi,\quad k\in\integralnum,\\
    \end{gathered}\]
    由 $|\varphi|< \dfrac\pi2$ 知 $\varphi= -\dfrac\pi6$, 则
    \[f(x)= 2\sin\Bigl(2x-\dfrac\pi6\Bigr),\]
    对应零点满足
    \[2x-\dfrac\pi6= k\pi,\ \text{即}\ 
        x= \dfrac\pi{12}+ \frac{k\pi}2,\quad k\in\integralnum,\]
    仍然可得所求零点为 $\dfrac{7\pi}{12}$.
</p>
<p>这种解法虽然是一般解法, 但是相对来说更繁琐一点.
</p>
</myremark>

<myexample>
<p>已知函数 $f(x)= \cos^4 x- 2\sin x\cos x- \sin^4 x$, 求 $f(x)$ 的最小正周期.
</p>
</myexample>
<mysolution>
    <p>先化简 $f(x)$ 的解析式,
    \[\begin{aligned}
        f(x)&= (\cos^4 x- \sin^4 x)- 2\sin x\cos x\\
        &= (\cos^2 x+ \sin^2 x)(\cos^2 x- \sin^2 x)- \sin 2x\\
        &= \cos2x- \sin2x
         = \sqrt2\cos(2x+45^\circ),
    \end{aligned}\]
    所以 $f(x)$ 的最小正周期为 $\dfrac{2\pi}{2}= \pi$.
</p>
</mysolution>

<myexample>
<p>求函数 $y= |\sin x|$ 的单调递增区间.
</p>
</myexample>
<mysolution>
    <p>函数 $y= |\sin x|$ 的图形可由函数 $y= \sin x$ 的图形变换得到. 具体来说, 考虑绝对值的作用可知, 只需将后者在 $x$ 轴下方的部分对称地“翻折”到 $x$ 轴上方, 即关于 $x$ 轴作对称图形. 由函数图形可知, 所求单调递增区间为 $\Bigl[k\pi, \dfrac\pi2+ k\pi\Bigr]$, $k\in\mathbf{Z}$.
</p>
</mysolution>

<myexample>
<p>已知函数 $f(x)= \cos\Bigl(2x-\dfrac\pi3\Bigr)- 2\sin^2 x+1$.
</p>
<p>(1) 求函数 $f(x)$ 的最小正周期.
</p>
<p>(2) 求函数 $f(x)$ 在区间 $\Bigl[0,\dfrac\pi2\Bigr]$ 上的最大值和最小值.
</p>
</myexample>
<mysolution>
    <p>(1) 先将 $f(x)$ 化简, \[
        \begin{aligned}
            f(x)
            &= \cos2x\cos\frac\pi3+ \sin2x\sin\frac\pi3- (1-\cos2x)+ 1\\
            &= \frac12\cos2x+ \frac{\sqrt3}2\sin2x+ \cos2x\\
            &= \sqrt3\biggl(\frac{\sqrt3}2\cos2x+ \frac12\sin2x\biggr)\\
            &= \sqrt3\sin\Bigl(2x+\frac\pi3\Bigr),
        \end{aligned}\]
    由此可知, 所求最小正周期为 $\dfrac{2\pi}2= \pi$.
</p>
<p>(2) 当 $x\in\Bigl[0,\dfrac\pi2\Bigr]$ 时, \[
        2x+\frac\pi3\in\Bigl[\frac\pi3,\frac{4\pi}3\Bigr],\]
    结合 $f(x)$ 的解析式可知, 此时 $f(x)\in\biggl[-\dfrac32,\sqrt3\biggr]$, 即最大值为 $\sqrt3$, 最小值为 $-\dfrac32$.
</p>
</mysolution>


<myexample>
<p>已知函数 $f(x)= 2\sqrt{3} \sin\dfrac{x}2 \cos\dfrac{x}2 - 2\cos^2\dfrac{x}2$, 求 $f(x)$ 的单调递减区间及对称轴方程.
</p>
</myexample>
<mysolution>
    <p>先用二倍角公式化简, \[\begin{aligned}
        f(x)&= \sqrt{3} \sin x - (1+\cos x)\\
        &= 2\biggl(\dfrac{\sqrt{3}}2\sin x- \dfrac12\cos x\biggr)-1\\
        &= 2\sin\biggl(x-\dfrac\pi6\biggr)-1.
    \end{aligned}\]
    所以当 $f(x)$ 单调递减时, \[\begin{aligned}
        x-\dfrac\pi6&\in \biggl[\dfrac\pi2+2k\pi, \dfrac{3\pi}2+2k\pi\biggr],\\
        x&\in \biggl[\dfrac{2\pi}3+2k\pi, \dfrac{5\pi}3+2k\pi\biggr],
    \end{aligned}\]
    即所求单调递减区间为 \[
        \biggl[\dfrac{2\pi}3+2k\pi, \dfrac{5\pi}3+2k\pi\biggr],\quad
        k\in\mathbf{Z},\]
    而 $f(x)$ 的对称轴满足 \[
        x-\dfrac\pi6=\dfrac\pi2+ k\pi\Rightarrow
        x= \dfrac{2\pi}3+ k\pi,\ k\in\mathbf{Z}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知函数 $f(x)= \sin(\omega x+\varphi)$ ($\omega> 0$, $|\varphi|< \dfrac\pi2$) 的周期为 $\pi$, 直线 $x=\dfrac\pi6$ 是 $f(x)$ 图形的一条对称轴.
</p>
<p>(1) 求 $f(x)$ 的解析式和单调递减区间;
</p>
<p>(2) 若 $x\in\biggl[0,\dfrac\pi3\biggr]$, 求 $f(x)$ 的值域.
</p>
</myexample>
<mysolution>
    <p>(1) 因为 $f(x)$ 的周期为 $\pi$, 所以 \[
        \frac{2\pi}{|\omega|}= \pi\Rightarrow |\omega|= 2,\]
    结合 $\omega> 0$ 知, $\omega= 2$. 由 $x=\dfrac\pi6$ 是对称轴知, \[\begin{gathered}
        \sin\biggl(\dfrac\pi6\cdot \omega +\varphi\biggr)
            = \sin\biggl(\dfrac\pi6\cdot 2 +\varphi\biggr)= \pm1,\\
        \dfrac\pi3 +\varphi= \dfrac\pi2+ k\pi,\\
        \varphi= \dfrac\pi6+ k\pi,\quad k\in\mathbf{Z}.
    \end{gathered}\]
    因为 $|\varphi|< \dfrac\pi2$, 所以 $\varphi= \dfrac\pi6$, 即 \[
        f(x)= \sin\biggl(2x+\dfrac\pi6\biggr).\]
    当 $f(x)$ 单调递减时, \[\begin{aligned}
        2x+\dfrac\pi6&\in \biggl[\dfrac\pi2+2k\pi, \dfrac{3\pi}2+2k\pi\biggr],\\
        x&\in \biggl[\dfrac{\pi}6+k\pi, \dfrac{2\pi}3+k\pi\biggr],
    \end{aligned}\]
    即所求单调递减区间为 \[
        \biggl[\dfrac{\pi}6+k\pi, \dfrac{2\pi}3+k\pi\biggr],\quad
        k\in\mathbf{Z},\]
</p>
<p>(2) 当 $x\in\biggl[0,\dfrac\pi3\biggr]$ 时, \[
        2x\in\biggl[0,\dfrac{2\pi}3\biggr]\Rightarrow
        2x+\dfrac\pi6\in\biggl[\dfrac\pi6,\dfrac{5\pi}6\biggr],\]
    所以由单位圆中的正弦线可知, \[
        f(x)\in \biggl[\sin\dfrac\pi6, \sin\dfrac\pi2\biggr]
        = \biggl[\frac12, 1\biggr]\]
</p>
</mysolution>

