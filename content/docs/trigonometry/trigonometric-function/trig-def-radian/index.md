---
# bookCollapseSection: true
title: 任意角的三角函数与弧度制
weight: 1
bookHidden: true
prevPage: /docs/trigonometry/trigonometric-function
prevPageTitle: 三角函数
nextPage: /docs/trigonometry/trigonometric-function/trig-induce
nextPageTitle: 三角函数的诱导公式
---

# 任意角的三角函数与弧度制

<p>\subsection{弧度制}
</p>
<p>角的大小用来描述角的两边 (始边和终边) 张开的幅度. 度量角的大小的方法中, 常见的为如下两种:
</p>
<p>(1) 将射线绕定点旋转一周所形成的角 (称为周角) 等分为 $360$ 份, 每一份的大小记为 $1^\circ$. 所以周角的大小是 $360^\circ$, 并这种方法称为角度制. 
</p>
<p>(2) 将角的顶点放在圆心, 利用所截弧长来定义角的大小. 当圆心角固定时, 若半径越大, 则所对弧长也越大, 所以定义弧长与半径的比例为圆心角的大小, 并称这种方法为弧度制. 此时周角的大小是 $\dfrac{2\pi r}r= 2\pi\,\mathrm{rad}$. $\mathrm{rad}$ 是弧度制的单位, 念作“弧度”(radian), 通常略去不写.
</p>
<p>根据相似形对应线段或弧成比例, 对固定的圆心角, 弧长与半径的比例为定值, 所以第二种方法是合理的. 
</p>
<p><center>
        \includegraphics[scale=1]{2020-1218-1940-crop}
    </center>
</p>
<p>高中数学更常用的是弧度制. 由定义, $360^\circ =2\pi$, 并应熟记特殊角 $0^\circ$, $30^\circ$, $45^\circ$, $60^\circ$, $90^\circ$, $120^\circ$, $135^\circ$, $150^\circ$, $180^\circ$ 的角度和弧度.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1220-0920-crop}\quad
        \includegraphics[scale=1]{2020-1220-0930-crop}
    </center>
</p>
<p>容易得到弧度与角度互换公式: 
\[1\,\mathrm{rad}= \Big(\frac{180}{\pi}\Big)^{\circ} \approx 57.3^{\circ}, \quad
    1^{\circ}= \frac{\pi}{180}\,\mathrm{rad}.\]
若圆心角 $\alpha$ (弧度制, 可能为负) 所对的弧长为 $l$, 则 $|\alpha|=\dfrac{l}{r}$, 其中 $r$ 是圆的半径. 此外还有弧长公式 $l=|\alpha|r$, 和扇形面积公式
\[S= \dfrac{1}{2}lr= \dfrac{1}{2}|\alpha| r^2\quad 
    \text{(类似于三角形面积公式)}.\]
</p>
<p><myexample>
<p>求终边落在直线 $y=-x$ 上的角 $\alpha$ 的集合.
</p>
</myexample>
<mysolution>
    <p>直线 $y=-x$ 为第二、四象限的角平分线, 作图易知, 所求集合为
    \[\{\alpha\mid\ 135^\circ+k\cdot 180^\circ\}
        = \biggl\{\alpha\biggm| \frac{3\pi}4+k\pi\biggr\}.\]
    以上两个集合, 只写其中一个即可 (用弧度制相对来说更简洁).
</p>
</mysolution>
</p>
<p>\begin{example}\label{exa:201220-1030}
    已知某扇形的半径为 $10$, 面积为 $\dfrac{50\pi}3$, 求该扇形的圆心角大小.
</p>
</myexample>
<mysolution>
    <p>设该扇形的圆心角弧度大小为 $\alpha$, 半径为 $r$, 则其面积 \[S=\frac12\alpha r^2,\quad\text{即}\quad 
        \frac{50\pi}3= \frac12 \alpha\cdot 10^2.\]
    解得 $\alpha=\dfrac\pi3$.
</p>
</mysolution>
<myremark>
    <p>例 \ref{exa:201220-1030} 也可以用角度制来解: 设该扇形的圆心角角度大小为 $\alpha$, 半径为 $r$, 则其面积 $S=\dfrac{\alpha}{360^\circ} \pi r^2$, 可求得 $\alpha=60^\circ$. 用角度制计算相对更简单一些.
</p>
</myremark>
</p>
<p>\subsection{任意角三角函数的定义}
</p>
<p>如下方左图, 设 $\alpha$ 是任意一个角, 顶点为坐标原点, 
  始边为 $x$ 正半轴, $P(x, y)$ 是终边上任意一点 (异于原点), 
  它与原点的距离是 $r= \sqrt{x^2+ y^2}> 0$, 那么 
  \[\sin\alpha= \frac{y}{r},\quad
    \cos\alpha= \frac{x}{r},\quad 
    \tan\alpha= \frac{y}{x}\ (x\neq 0).\]
  三角函数值只与角的大小有关, 而与终边上点 $P$ 的位置无关. 由定义容易判断各象限内的角的三角函数值的正负号. 若点 $P$ 恰在单位圆 (圆心为原点且半径为 $1$) 上, 取点 $A(1,0)$, 并作 $PM\perp OA$ 于点 $M$, 作 $TA\perp OA$ 并交射线 $OP$ 于点 $T$, 则此时 $r=1$, 且 (类似锐角三角函数的定义)
  \[\sin\alpha= y,\quad
    \cos\alpha= x,\quad 
    \tan\alpha= \frac{AT}{OA}= AT\ (x\neq 0).\]
  对 $\angle{POA}$ 来说, $MP$ 为正弦线, $OM$ 为余弦线, $AT$ 为正切线, 
  且各线段均为有向线段 (即规定了正方向, 所以表示时带正负号). 常用的三角函数值, 参考下方右图. 由此可以写出其他特殊角 ($120^\circ$, $135^\circ$, $150^\circ$ 等) 的各三角函数值, 如 $\sin 120^\circ= \dfrac{\sqrt3}2$, $\cos135^\circ= -\dfrac{\sqrt2}2$.
</p>
<p>\begin{small}
    \begin{minipage}[t]{0.35\linewidth}
    \centering
    \begin{tikzpicture}[scale=1.1]
      \draw[-{Stealth[scale=0.8]}] (-1.2,0) -- (1.4,0) node[below] {$x$};
      \draw[-{Stealth[scale=0.8]}] (0,-1.2) -- (0,1.3) node[left] {$y$};
      \draw (0,0) circle (1) node[anchor=45] {$O$} coordinate (O);
      \def\myangle{40};
      \pgfmathparse{tan(\myangle)};
      \coordinate (B) at (\myangle:1.6);
      \draw[fill=black] (1,0) circle (0.6pt) coordinate (A)
        +(0.1,0) node[below] {$A$};
      \draw[fill=black] (1,\pgfmathresult) coordinate (T) circle (0.6pt) 
        node[above] {$T$} ;
      \draw[fill=black] (\myangle:1) circle (0.6pt) coordinate (P)
       +(0,0.06) node[above] {$P$};
      \draw[fill=black] ($(O)!(P)!(A)$) coordinate (M) circle (0.6pt) 
        node[below] {$M$};
      \draw (O)--(B) (M)--(P) (A)--(T);      
    \end{tikzpicture}
    \end{minipage}
    \hskip 1cm%
    \begin{minipage}[t]{0.55\linewidth}
    \centering
    \begin{tikzpicture}[scale=1.4]
      \pgfmathparse{sqrt(3)};
      \draw (0,0) coordinate (A)-- node[below] {$\sqrt3$} 
        (1.732,0) coordinate (B)-- node[anchor=225] {$2$}
        (0,1) coordinate (C)--node[left] {$1$} (0,0);
      \draw (A)++(0,0.12)--++(0.12,0)--++(0,-0.12);
      \draw (C)+(0,-0.12) arc (270:330:0.12);
      \draw (B)+(-0.2,0) arc (180:150:0.2);
      \draw (A)+(0.25,0.65) node {$60^\circ$} +(1.1,0.15) node {$30^\circ$};
      \draw (2.3,0) coordinate (D)-- node[below] {$1$} 
        +(1,0) coordinate (E)-- node[anchor=225] {$\sqrt2$}
        +(0,1) coordinate (F)--node[left] {$1$} (2.3,0);
      \draw (D)++(0,0.12)--++(0.12,0)--++(0,-0.12);
      \draw (E)+(-0.15,0) arc (180:135:0.15);
      \draw (D)+(0.55,0.15) node {$45^\circ$};
    \end{tikzpicture}
    \end{minipage}
    \end{small}
</p>
<p><myexample>
<p>$\sin6\underline{\qquad}0$. (填“$>$”或“$< $”)
</p>
</myexample>
<mysolution>
    <p>注意题中的 $6$ 是弧度制, 而 $360^\circ=2\pi\approx 6.28$, 所以 $6$ 弧度在第四象限. 由正弦的定义, $\sin 6< 0$.
</p>
</mysolution>
<myremark>
    <p>类似地, $1$ 弧度在第一象限, $2$ 弧度和 $3$ 弧度都在第二象限, 所以
    \[\sin 1,\ \sin 2,\ \sin 3>0,\quad 
        \cos 1>0,\quad \cos 2,\ \cos 3< 0.\]
    此外, 画图可知 $\sin 1< \sin 2$.
</p>
</myremark>
</p>
<p><myexample>
<p>已知角 $\alpha$ 的终边经过点 $P(-x,-12)$, 
    且 $\cos\alpha=-\dfrac5{13}$, 求 $x$ 的值.
</p>
</myexample>
<mysolution>
    <p>由余弦定义, 
    \[\cos\alpha= \frac{-x}{\sqrt{(-x)^2+(-12)^2}}= -\frac5{13},\quad
    \text{解得}\ x=\pm5.\]
    经检验, $x=5$  (或由余弦值为负知点 $P$ 在第二、三象限, 所以 $-x< 0$ 即 $x>0$).
</p>
</mysolution>

<p>同角三角函数有两个常用基本关系式: 
  \[\sin^2 x+ \cos^2 x= 1,\quad 
    \tan x= \frac{\sin x}{\cos x}.\]
  后一个式子也可以认为是正切的定义. 前一个式子等价于勾股定理, 由该式可知
  \[\begin{gathered}
    (\sin x\pm \cos x)^2= 1\pm 2\sin x\cos x,\\
        \sin^2 x= 1-\cos^2 x= (1+\cos x)(1-\cos x).
  \end{gathered}\] 
</p>
<p><myexample>
<p>已知 $\cos\alpha= -\dfrac35$, 且 $\tan\alpha>0$, 求 $\dfrac{\sin\alpha\cos^2\alpha}{1-\sin\alpha}$.
</p>
</myexample>
<mysolution>
    <p>方法一: 由题意, $\alpha$ 在第三象限, 所以 $\sin\alpha= -\dfrac45$, 
    \[\frac{\sin\alpha\cos^2\alpha}{1-\sin\alpha}
        = \frac{-\dfrac45\cdot\bigg(-\dfrac35\biggr)^2}{1- \biggl(-\dfrac45\biggr)}
        = -\frac{4}{25}.\]
</p>
<p>方法二: 也可以利用 $\cos^2\alpha= 1-\sin^2\alpha=(1+\sin\alpha)(1-\sin\alpha)$ 得,
    \[\frac{\sin\alpha\cos^2\alpha}{1-\sin\alpha}
        =\frac{\sin\alpha(1-\sin^2\alpha)}{1-\sin\alpha}
        = \sin\alpha(1+\sin\alpha)
        = -\frac{4}{25}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>化简 $\dfrac{\cos\theta}{1+\cos\theta}- \dfrac{\cos\theta}{1-\cos\theta}$.
</p>
</myexample>
<mysolution>
    <p>通分后合并可知,
    \[\begin{aligned}
        \frac{\cos\theta}{1+\cos\theta}- \frac{\cos\theta}{1-\cos\theta}
        &= \frac{\cos\theta(1- \cos\theta- (1+ \cos\theta))}{(1- \cos\theta)(1+ \cos\theta)}\\
        &= \frac{\cos\theta(-2\cos\theta)}{1- \cos^2\theta}
         = -\frac{2\cos^2\theta}{\sin^2\theta}\\
        &= - \frac2{\tan^2\theta}.
    \end{aligned}\]
    其中最后一个等号及其后的式子可以不写.
</p>
</mysolution>
</p>
<p>凡正余弦的二次式, 均可以化成正切函数来表示, 例如:
  \[\sin x\cos x+ \cos^2 x
    = \frac{\sin x\cos x+ \cos^2 x}{\sin^2 x+ \cos^2 x}
    = \frac{\tan x+ 1}{\tan^2 x+ 1}.\]
  与此类似的还有
  \[\frac{\sin x+\cos x}{\sin x-\cos x}
    = \frac{\tan x+1}{\tan x-1}.\]
  这两种变形方法常用来解决正余弦值和正切值的转化问题.
</p>
<p><myexample>
<p>已知 $\dfrac{\sin\theta+ \cos\theta}{\sin\theta- 2\cos\theta}= \dfrac12$, 求 $\tan\theta$.
</p>
</myexample>
<mysolution>
    <p>方法一: 原式分子、分母同除以 $\cos\theta$, 得 $\dfrac{\tan\theta+ 1}{\tan\theta- 2}= \dfrac12$, 所以 $\tan\theta= -4$.
</p>
<p>方法二: 将原式化为整式, 
    \[2(\sin\theta+ \cos\theta)=\sin\theta- 2\cos\theta,\]
    所以 $\sin\theta= -4\cos\theta$, 即 $\tan\theta= -4$.
</p>
</mysolution>
</p>
<p><myexample>
<p>设角 $\alpha$ 的终边过点 $P(3,4)$, 求 $\dfrac{\sin\alpha+ 2\cos\alpha}{\sin\alpha- \cos\alpha}$.
</p>
</myexample>
<mysolution>
    <p>方法一: 由题意, $\tan\alpha= \dfrac43$, 所以
    \[\frac{\sin\alpha+ 2\cos\alpha}{\sin\alpha- \cos\alpha}
        = \frac{\tan\alpha+ 2}{\tan\alpha- 1}
        = 10.\]
</p>
<p>方法二: 由题意, $\dfrac{\sin\alpha}{\cos\alpha}= \dfrac43$, 即 $\sin\alpha= \dfrac43\cos\alpha$, 所以
    \[\frac{\sin\alpha+ 2\cos\alpha}{\sin\alpha- \cos\alpha}
        = \frac{\dfrac43\cos\alpha+ 2\cos\alpha}{\dfrac43\cos\alpha- \cos\alpha}
        = 10.\]
</p>
</mysolution>

<myexample>
<p>判断 $\sin3\cdot \cos2\cdot \tan4$ 的正负号.
</p>
</myexample>
<mysolution>
    <p>题中的 $2$, $3$, $4$ 均为弧度. 因为 $180^\circ= \pi\approx 3.14$, $90^\circ= \dfrac\pi2\approx 1.57$, 所以 $2$, $3$ 弧度均在第二象限, $4$ 弧度在第三象限, 从而
    \[\sin3>0,\ \cos2< 0,\ \tan4>0,\quad\text{即}\quad
        \sin3\cdot \cos2\cdot \tan4< 0.\]
</p>
</mysolution>

<myexample>
<p>一个质点在半径为 $2$ 的圆 $O$ 上, 以点 $P$ 为起始点, 沿逆时针方向运动, 每 $3\,\mathrm{s}$ 转一圈, 求该质点到 $x$ 轴的距离 $y$ 关于时间 $t$ 的函数解析式.
</p>
</myexample>
<mysolution>
    <p>设质点运动到点 $Q(x,y)$ 时对应角 $\alpha$, 由三角函数定义,
    \[\left\{\!\!\begin{array}{l}
        \cos\alpha= \dfrac{x_Q}{r},\\[6pt]
        \sin\alpha= \dfrac{y_Q}{r},
    \end{array}\right.\ \text{即}\quad
    \left\{\!\!\begin{array}{l}
        x_Q= r\cos\alpha,\\
        y_Q= r\sin\alpha,
    \end{array}\right.\]
    所求距离 $y=|y_Q|= |r\sin\alpha|= 2|\sin\alpha|$. 因为起点 $P$ 对应角 $-\dfrac\pi4$, 而质点每 $3\,\mathrm{s}$ 转一圈, 即角增加的速度为 $\dfrac{2\pi}3/\mathrm{s}$, 所以 $\alpha= -\dfrac\pi4+ \dfrac{2\pi}3 t$, 因此
    \[y= 2\biggl|\sin\biggl(-\dfrac\pi4+ \dfrac{2\pi}3 t\biggr)\biggr|.\]
    <center>
        \includegraphics[scale=1.2]{2021-0207-0730-crop}
    </center>
</p>
</mysolution>
</p>
<p>一般地, 若一个质点在半径为 $r$ 的圆 $O$ 上, 以点 $P$ (对应角 $\varphi$) 为起始点, 沿逆时针方向匀速运动, 每 $T\,\mathrm{s}$ 转一圈, 则该质点的坐标 $(x,y)$ 可用运动时间 $t$ 表示为
\[\left\{\!\!\begin{array}{l}
    x= r\cos\biggl(\varphi+ \dfrac{2\pi}T t\biggr),\\[6pt]
    y= r\sin\biggl(\varphi+ \dfrac{2\pi}T t\biggr).
\end{array}\right.\]
这是匀速圆周运动的公式, $T$ 称为运动周期.
</p>

<myexample>
<p>已知 $\tan\theta= 2$, 求 $\sin^2\theta- \sin\theta\cos\theta- \cos^2\theta$ 的值.
</p>
</myexample>
<mysolution>
    <p>方法一: 由 $\tan\theta= 2$ 画正、余弦线可求得 $\sin\theta= \dfrac2{\sqrt5}$, $\cos\theta= \dfrac1{\sqrt5}$ 或 $\sin\theta= -\dfrac2{\sqrt5}$, $\cos\theta= -\dfrac1{\sqrt5}$. 将前一组值代入所求式子, 
    \[\sin^2\theta- \sin\theta\cos\theta- \cos^2\theta
        = \biggl(\dfrac2{\sqrt5}\biggr)^2- \dfrac2{\sqrt5}\cdot\dfrac1{\sqrt5}- \biggl(\dfrac1{\sqrt5}\biggr)^2
        = \frac15.\]
    将后一组值代入也可以得到同样的结果.
</p>
<p>方法二: 利用 $1=\sin^2\theta+ \cos^2\theta$ 且由 $\tan\theta= 2$ 知 $\cos\theta\neq0$, 可将原式改写为
    \[\frac{\sin^2\theta- \sin\theta\cos\theta- \cos^2\theta}{\sin^2\theta+ \cos^2\theta}
    = \frac{\tan^2\theta- \tan\theta- 1}{1+\tan^2\theta},\]
    再将 $\tan\theta= 2$ 代入可知结果为 $\dfrac15$.
</p>
</mysolution>

<myexample>
<p>已知 $\sin\alpha+\cos\alpha= -\dfrac{\sqrt5}2$, 且 $\dfrac{5\pi}4< \alpha< \dfrac{3\pi}2$, 求 $\cos\alpha- \sin\alpha$ 的值.
</p>
</myexample>
<mysolution>
    <p>因为 $\sin^2\alpha+ \cos^2\alpha=1$, 所以
    \[\begin{gathered}
        (\sin\alpha+\cos\alpha)^2
        = 1+ 2\sin\alpha\cos\alpha,\\
        (\cos\alpha- \sin\alpha)^2
        = 1- 2\sin\alpha\cos\alpha,
    \end{gathered}\]
    两式相加可得, 
    \[(\sin\alpha+\cos\alpha)^2+ (\cos\alpha- \sin\alpha)^2= 2.\]
    将 $\sin\alpha+\cos\alpha= -\dfrac{\sqrt5}2$ 代入, 
    \[\biggl(-\dfrac{\sqrt5}2\biggr)^2+ (\cos\alpha- \sin\alpha)^2= 2,\quad\text{即}\quad
    |\cos\alpha- \sin\alpha|= \frac{\sqrt3}2.\]
    又因为 $\dfrac{5\pi}4< \alpha< \dfrac{3\pi}2$, 由正、余弦线可知, $\cos\alpha> \sin\alpha$, 所以
    \[\cos\alpha- \sin\alpha= \frac{\sqrt3}2.\]
</p>
</mysolution>

<myexample>
<p>下列关于弧度制的说法中, 正确的有哪些?
</p>
<p>(1) 设单位圆上一段弧 $\wideparen{AB}$ 所对的圆心角是 $\alpha\,\mathrm{rad}$, $\wideparen{AB}$ 的长度为 $l$, 则 $|\alpha|=l$.
</p>
<p>(2) 在半径为 $r$ 的圆中, 弧长为 $l$ 的弧所对的圆心角为$\alpha\,\mathrm{rad}$; 半径为 $R$ 的圆中, 弧长为 $L$ 的弧所对的圆心角也为 $\alpha\,\mathrm{rad}$, 则必有 $lR= Lr$.
</p>
<p>(3) $1\,\mathrm{rad}= \biggl(\dfrac{\pi}{360}\biggr)^\circ$.
</p>
<p>(4) $\sin2 > \cos2$.
</p>
</myexample>
<mysolution>
    <p>本题需要利用弧度的定义: 圆心角 $\alpha$ (可能为负角) 的弧度大小 $|\alpha|$ 为其所对的弧长 $l$ 与半径 $r$ 的比值, 即 $|\alpha|= \dfrac{l}r$.
</p>
<p>(1) 单位圆的半径 $r=1$, 所以此时 $|\alpha|= \dfrac{l}1= l$.
</p>
<p>(2) 由定义,
    \[\dfrac{l}r= |\alpha|= \dfrac{L}R,\quad\text{即}\quad lR=Lr.\]
</p>
<p>(3) 圆周角 $360^\circ$ 对应弧度 $\dfrac{2\pi r}{r}= 2\pi$, 所以
    \[360^\circ= 2\pi\,\mathrm{rad},\quad\text{即}\quad 1\,\mathrm{rad}= \biggl(\dfrac{180}{\pi}\biggr)^\circ.\]
</p>
<p>(4) 由 (3) 可知, $1\,\mathrm{rad}$ 比 $60^\circ$ 略少一点, 所以 $2\,\mathrm{rad}$ 约为 $120^\circ$, 在第二象限. 因此 $\sin2>0>\cos2$.
</p>
</mysolution>

<myexample>
<p>判断 $\sin 1$, $\cos 1$, $\tan 1$ 的大小关系.
</p>
</myexample>
<mysolution>
    <p>由弧度制的定义, $2\pi= 360^\circ$, 因此
    \[1=\frac{360^\circ}{2\pi}= \frac{180^\circ}{\pi},\]
    即 $1$ 弧度比 $60^\circ$ 略小一点 (因为 $\pi\approx 3.14$). 画三角函数线可知, $\sin1>\cos1$. 再由 
    \[\tan1= \frac{\sin 1}{\cos 1} > 1,\quad \sin 1< 1,\]
    可知 $\cos1< \sin 1< \tan 1$.
</p>
</mysolution>
<myremark>
    <p>一般地, 若 $\alpha\in\biggl(0,\dfrac\pi2\biggr)$, 则必有 $\tan\alpha> \sin\alpha$. 思考: 此时 $\sin\alpha$ 与 $\cos\alpha$ 的大小关系如何判断? $\tan\alpha$ 与 $\cos\alpha$ 的大小关系呢?
</p>
</myremark>

<myexample>
<p>下列各式中哪些是正确的?
</p>
<p>(1) $\sin\dfrac\pi5> \sin\dfrac{6\pi}5$;\quad 
    (2) $\cos\biggl(-\dfrac\pi3\biggr)< \cos\dfrac\pi6$;
</p>
<p>(3) $\tan\dfrac\pi4> \tan\dfrac{5\pi}4$;\quad 
    (4) $\sin\dfrac\pi3> \sin\dfrac\pi6$.
</p>
</myexample>
<mysolution>
    <p>画正弦线、余弦线如下:
</p>
<p><center>
        \includegraphics[scale=1.1]{2020-1227-1300-crop}\qquad
        \includegraphics[scale=1.1]{2020-1227-1310-crop}\\[5pt]
        \includegraphics[scale=1.1]{2020-1227-1320-crop}\qquad
        \includegraphics[scale=1.1]{2020-1227-1330-crop}
    </center>
</p>
<p>由此可知 (正切值由正弦值比余弦值得到)
    \[\begin{gathered}
        \sin\dfrac\pi5>0> \sin\dfrac{6\pi}5,\quad 
        \cos\biggl(-\dfrac\pi3\biggr)=\frac12< \frac{\sqrt3}2=\cos\dfrac\pi6,\\
        \tan\dfrac\pi4= 1= \tan\dfrac{5\pi}4,\quad 
        \sin\dfrac\pi3= \frac{\sqrt{3}}2> \frac12=\sin\dfrac\pi6.
    \end{gathered}\]
</p>
</mysolution>

<myexample>
<p>圆心角为 $2\alpha$ 的扇形, 它的半径为 $R$, 内切圆的半径为 $r$, 求 $R$ 与 $r$ 的关系.
</p>
</myexample>
<mysolution>
    <p>如图所示, 在扇形 $AOB$ 中, $\angle AOB= 2\alpha$, $OA=R$, 圆 $M$ 与扇形 $AOB$ 相切于点 $N$, $P$, $Q$. 连接 $ON$, 由对称性知, $ON$ 必过点 $M$, 且 $\angle BON= \dfrac12\angle BOA= \alpha$. 再连接 $MP$, 则 $MP\perp OB$ 且 $MP=r$. 考虑 $\mathrm{Rt}\triangle OMP$ 可知,
    \[\dfrac{MP}{MO}= \sin\alpha,\quad\text{即}\quad
        OM= \frac{r}{\sin\alpha}.\]
    因为 $ON= OM+MP$, 所以 $R=\biggl(1+\dfrac1{\sin\alpha}\biggr)r$.
</p>
<p><center>
        \includegraphics[scale=1.4]{2021-0214-0900-crop}
    </center>
</p>
<p></p>
</mysolution>

<myexample>
<p>下图为一个观览车示意图, 该观览车半径 $r=4.8\,\text{m}$, 圆上最低点与地面距离为 $0.8\,\text{m}$, $60\,\mathrm{s}$ 转动一周. 图中 $OA$ 与地面垂直, 以 $OA$ 为始边, 逆时针转动 $\theta$ 角到 $OB$, 设点 $B$ 与地面距离为 $h$.
</p>
<p>(1) 求 $h$ 与 $\theta$ 之间的函数关系解析式.
</p>
<p>(2) 设从 $OA$ 开始转动, 经过 $t\,\mathrm{s}$ 到达 $OB$, 求 $h$ 与 $t$ 之间的函数关系解析式.
</p>
</myexample>
<mysolution>
    <p>(1) 以 $O$ 为原点, 分别沿水平方向和竖直方向作 $x$ 轴和 $y$ 轴, 建立平面直角坐标系. 设 $OB$ 与 $x$ 轴正方向的夹角为 $\varphi$, 则由三角函数值的定义, 点 $B$ 的纵坐标为 $r\sin\varphi$. 由图可知, \[\varphi= \theta- 90^\circ,\]
    而点 $O$ 与地面的距离为 $r+0.8= 5.6\,\mathrm{m}$, 所以 \[
        h= 5.6+4.8\sin(\theta-90^\circ)
         = 5.6-4.8\cos\theta.\]
</p>
<p>(2) 由题意, $OB$ 旋转的速度为 $6^\circ\,\mathrm{s}$, 所以 $\theta= 6t$, 代入上式可知, \[h= 5.6-4.8\cos6t.\]
</p>
</mysolution>

