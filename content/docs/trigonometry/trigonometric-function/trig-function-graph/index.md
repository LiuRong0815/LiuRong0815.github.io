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

