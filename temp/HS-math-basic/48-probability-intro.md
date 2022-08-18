\sectioncounter{47}
</p>

<p>
\section{排列、组合与古典概型}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
排列与组合对应两种计数方式. 将一些研究对象排成一列, 排列的方法数称为排列数. 将 $n$ 个研究对象排成一列, 共有
\[n\cdot (n-1)\cdot\, \cdots\, \cdot 2\cdot 1 = n!\]
种排法 ($n!$ 称为 $n$ 的阶乘, 规定 $0!=1$); 从 $n$ 个研究对象中选取 $m$ 个 ($m< n$) 排成一列, 共有 $\dfrac{n!}{(n-m)!}$ 种排法, 并记为 $\mathrm{A}_n^m$. 从一些研究对象中取出一部分, 选取的方法数称为组合数. 从 $n$ 个研究对象中选取 $m$ 个 ($m< n$), 共有 $\dfrac{n!}{m!\,(n-m)!}$ 种取法, 并记为 $\mathrm{C}_n^m$.
</p>

<p>
在计数时, 有两个常用的计数原理 (均可以结合树状图来理解). (1) 加法原理: 若完成一件事有 $m$ 个不同方案, 各方案分别有 $n_1, n_2,\cdots, n_m$ 种不同方法, 则完成这件事有
\[n_1+ n_2+\cdots +n_m\]
种不同方法. (2) 乘法原理: 若完成一件事有 $m$ 个不同步骤, 各步骤分别有 $n_1, n_2,\cdots, n_m$ 种不同方法, 则完成这件事有
\[n_1 n_2\cdots n_m\]
种不同方法. (可以结合排列数的公式体会乘法原理.)
</p>

<p>
概率表示事件发生的可能性, 其大小描述了可能性的大小. 事件 $A$ 的概率记为 $P(A)$, 且 $P(A)\in [0,1]$. 古典概型为最基本概率模型. 如果一次试验中可能出现的结果 (基本事件) 有 $n$ 个, 而且所有结果出现的可能性都相等, 那么每一个基本事件的概率都是 $\dfrac1n$. 如果某个事件 $A$ 由 $m$ 个基本事件组成, 那么事件 $A$ 发生的概率为
\[P(A)=\frac{m}n
    = \frac{\text{$A$ 包含的基本事件的个数}}{\text{基本事件的总数}}.\]
这种概率模型称为古典概型.
</p>

<p>
从古典概型的定义可以知道, 计算事件发生的概率之前必须把所有基本事件描述清楚, 并判断所考虑的事件由哪些基本事件组成, 此时常用组合计数. 在计算概率时, 可充分利用列表或画图的方式描述基本事件的个数. 有时所考虑的事件本身比较复杂, 可尝试先计算其互斥事件的概率.
</p>

<p>
\lianxi
<myexercise>
    <p>    从 $1$, $2$, $3$, $6$ 这四个数中一次随机地取 $2$ 个数, 求所取两个数的乘积为 $6$ 的概率.
</p>
</myexercise>
<mysolution>
    <p>
    由 $6= 1\times 6= 2\times 3$ 知, 所求的概率为 $\dfrac2{\mathrm{C}_4^2}= \dfrac13$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    从 $\{1, 2, 3, 4, 5\}$ 中随机选取一个数 $a$, 从 $\{2, 3, 4\}$ 中随机选取一个数 $b$, 求 $b>a$ 的概率.
</p>
</myexercise>
<mysolution>
    <p>
    当 $b>a$ 时, 若 $b=2$, 则 $a=1$; 若 $b=3$, 则 $a=1,2$; 若 $b=4$, 则 $a=1,2,3$, 故所求的概率为 $\dfrac{1+2+3}{5\times 3}= \dfrac2{5}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    现有在外观上没有区别的 $5$ 件产品, 其中 $3$ 件合格, $2$ 件不合格, 从中任意抽检 $2$ 件, 求只有一件合格的概率.
</p>
</myexercise>
<mysolution>
    <p>
    $\dfrac{\mathrm{C}_3^1 \mathrm{C}_2^1}{\mathrm{C}_5^2}= \dfrac35$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    由数字 $0,1,2,3,4,5$ 可以组成多少个三位数 (各位上的数字可以重复)?
</p>
</myexercise>
<mysolution>
    <p>
    百位不能为 $0$, 所求个数为 $5\times 6\times 6 = 180$.
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{古典概型问题}
<span id="example-"></span>
<myexample>
    <p>
    在集合 $A=\Big\{x\Big| x=\dfrac{n\pi}6,\ n=1,2,\ldots,10\Big\}$ 中任取一个元素, 求所取元素满足方程 $\cos x=\dfrac12$ 的概率.
</p>
</myexample>
<mysolution>
    <p>
    集合 $A$ 中满足 $\cos x=\dfrac12$ 的有 $\dfrac{\pi}3,\dfrac{5\pi}3$, 故所求的概率为 $\dfrac2{10}= \dfrac15$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    现有 $4$ 道甲类题, $2$ 道乙类题, 从中任取 $2$ 道题解答.
</p>

<p>
    (1) 求所取的 $2$ 道题都是甲类题的概率;
</p>

<p>
    (2) 求所取的 $2$ 道题不是同一类题的概率.
</p>
</myexample>
<mysolution>
    <p>
    (1) $\dfrac{\mathrm{C}_4^2}{\mathrm{C}_6^2}= \dfrac6{15}= \dfrac25$;\quad
    (2) $\dfrac{\mathrm{C}_4^1+\mathrm{C}_2^1}{\mathrm{C}_6^2}= \dfrac8{15}$.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    某小组共有 A, B, C, D, E 五位同学, 他们的身高 (单位: m) 及体重指标
    (单位: $\text{kg/m}^2$) 如下表所示:
    \[\begin{array}{c|ccccc}
        &A &B &C &D &E \\\hline
        \text{身高} &1.69 &1.73 &1.75 &1.79 &1.82\\
        \text{体重指标} &19.2 &25.1 &18.5 &23.3 &20.9
      \end{array}\]
</p>

<p>
    (1) 从该小组身高低于 $1.80\,\text{m}$ 的同学中任选 $2$ 人, 求选到的 $2$ 人身高都在 $1.78\,\text{m}$ 以下的概率;\qquad
    (2) 从该小组同学中任选 $2$ 人, 求选到的 $2$ 人的身高都在 $1.70\,\text{m}$ 以上且体重指标都在 $[18.5, 23.9)$ 内的概率.
</p>
</myexample>
<mysolution>
    <p>
    (1) $\dfrac{\mathrm{C}_3^2}{\mathrm{C}_4^2}= \dfrac36= \dfrac12$;\quad
    (2) $\dfrac{\mathrm{C}_3^2}{\mathrm{C}_5^2}= \dfrac3{10}$.
</p>
</mysolution>
</p>

<p>
\lianxi
<myexercise>
    <p>    某地区有 $21$ 所小学、$14$ 所初中、$7$ 所高中, 现采取分层抽样的方法从这些学校中抽取 $6$ 所学校对学生进行视力调查.
</p>

<p>
    (1) 求应从小学、初中、高中分别抽取的学校数量;
</p>

<p>
    (2) 若从抽取的 $6$ 所学校中随机抽取 $2$ 所学校做进一步数据分析, 求这 $2$ 所学校均为小学的概率.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 按比例抽取, 故应抽取 $3$ 所小学, $2$ 所初中, $1$ 所高中.
</p>

<p>
    (2) $\dfrac{\mathrm{C}_3^2}{\mathrm{C}_6^2}= \dfrac3{15}= \dfrac15$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    抛掷两枚骰子, 若朝上的点数为 $b, c$, 求方程 $x^2 +bx+c=0$ 有两个不等实根的概率.
</p>
</myexercise>
<mysolution>
    <p>
    $\Delta= b^2- 4c> 0$, 即 $b^2>4c$. 因为 $c\geqslant 1$, 所以 $b^2>4$, $b>2$. 当 $b=3$ 时, $c= 1,2$; 当 $b=4$ 时, $c= 1,2,3$; 当 $b=5,6$ 时, $c= 1,2,\cdots,6$, 故所求的概率为
    \[\frac{2+3+2\times 6}{6\times 6}= \frac{17}{36}.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{统计与概率的综合}
<span id="example-"></span>
<myexample>
    <p>
    某学校共有教师 $360$ 人, 分为三个批次参加研修培训, 其中男教师、女教师人数如下表所示:
    \[\begin{array}{c|ccc}
        \text{性别} & \text{第一批次} & \text{第二批次} & \text{第三批次}\\\hline
        \text{女教师} & 86 & x & y \\
        \text{男教师} & 94 & 66 & z
      \end{array}\]
    已知在全体教师中随机抽取 $1$ 名, 抽到第二批次和第三批次女教师的概率分别是 $0.15$ 和 $0.1$.
</p>

<p>
    (1) 求 $x, y, z$ 的值;\qquad
    (2) 为了调查研修效果, 现从三个批次中按 $1:60$ 的比例抽取教师进行问卷调查, 求各批次应选取的人数.\qquad
    (3) 若从 (2) 中选取的教师中随机选出两名教师进行访谈, 求这两名教师分别来自两个批次的概率.
</p>
</myexample>
<mysolution>
    <p>
    (1) 由题意, $\dfrac{x}{360}= 0.15$, $\dfrac{y}{360}= 0.1$, 且
    \[86+x+y+ 94+66+z= 360,\]
    所以 $x=54$, $y=36$, $z=24$.
</p>

<p>
    (2) 各批次应选取的人数分别为
    \[\frac{86+94}{60}= 3,\quad
    \frac{x+66}{60}= 2,\quad
    \frac{y+z}{60}= 1.\]
</p>

<p>
    (3) 分类计数可知, 所求的概率为
    \[\frac{\mathrm{C}_3^1\mathrm{C}_2^1+ \mathrm{C}_2^1\mathrm{C}_1^1+ \mathrm{C}_1^1\mathrm{C}_3^1}{\mathrm{C}_6^2}
    = \frac{6+2+3}{15}= \frac{11}{15}.\]
</p>
</mysolution>
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    从 $1,2,3,4,5$ 中任意取出 $2$ 个不同的数, 求它们的和为 $5$ 的概率.
</p>
</myexercise>
<mysolution>
    <p>
    由 $5= 1+4= 2+3$ 知, 所求的概率为 $\dfrac2{\mathrm{C}_5^2}= \dfrac15$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    先后抛掷两枚均匀的骰子, 朝上一面的点数分别记为 $x,y$, 求 $y=2x$ 的概率.
</p>
</myexercise>
<mysolution>
    <p>
    当 $x=1$ 时, $y=2$; 当 $x=2$ 时, $y=4$; 当 $x=3$ 时, $y=6$, 故所求的概率为 $\dfrac3{6^2}= \dfrac1{12}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    从 $\{0,1,2,3,4,5\}$ 内取 $3$ 个数, 可以组成多少个三位数?
</p>
</myexercise>
<mysolution>
    <p>
    百位不能为 $0$, 则所求个数为 $5\times 5\times 4= 100$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    乘积 $(x_1+x_2+x_3)(y_1+y_2+y_3+y_4)$ 展开后, 共有多少项?
</p>
</myexercise>
<mysolution>
    <p>
    $3\times 4= 12$.
</p>
</mysolution>
</p>

<p>
\subsection{课后练习}
<myexercise>
    <p>    分别从集合 $A=\{1, 2, 3, 4\}$ 和集合 $B=\{5, 6, 7, 8\}$ 中各取一个数, 求这两个数的积为偶数的概率.
</p>
</myexercise>
<mysolution>
    <p>
    积为奇数的概率为 $\dfrac{2\times 2}{4\times 4}= \dfrac14$, 故积为偶数的概率为 $1-\dfrac14= \dfrac34$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    从长度分别为 $1, 2, 3, 4$ 的四条线段中任意取三条, 求以这三条线段为边可以构成三角形的概率.
</p>
</myexercise>
<mysolution>
    <p>
    要构成三角形, 需较小两边之和大于最大边, 故仅 $2,3,4$ 满足题意, 所求的概率为 $\dfrac1{\mathrm{C}_4^3}= \dfrac14$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    求正十边形中对角线的条数.
</p>
</myexercise>
<mysolution>
    <p>
    从 $10$ 个顶点中任取 $2$ 个, 有取法 $\mathrm{C}_{10}^2= 45$ 种, 取到边的可能有 $10$ 种, 故对角线有 $45-10= 35$ 条. 
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在一个正方体的顶点中任取 $4$ 个, 求这 $4$ 个顶点恰可连成三棱锥的概率.
</p>
</myexercise>
<mysolution>
    <p>
    从 $8$ 个顶点中任取 $4$ 个, 有取法
    \[\mathrm{C}_8^4= \frac{8\times 7\times 6\times 5}{1\times 2\times 3\times 4}= 70\ (\text{种}).\]
    当且仅当 $4$ 个顶点共面时, 它们不可连成三棱锥, 此时这 $4$ 个顶点可能在 $6$ 个面或 $6$ 个对角面上. 故所求的概率为
    \[1- \frac{6+6}{70}= \frac{29}{35}.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    甲、乙两人玩猜数字游戏, 先由甲心中想一个数字, 记为 $a$, 再由乙猜甲刚才所想的数字, 将乙猜的数字记为 $b$, 其中 $a, b\in\{1, 2, 3, 4, 5, 6\}$. 若 $|a-b|\leqslant1$, 就称甲、乙“心相近”. 求他们“心相近”的概率.
</p>
</myexercise>
<mysolution>
    <p>
    当 $|a-b|\leqslant1$ 时, 若 $a=1$, 则 $b=1,2$; 若 $a=2$, 则 $b=1,2,3$; 若 $a=3$, 则 $b=2,3,4$; 若 $a=4$, 则 $b=3,4,5$; 若 $a=5$, 则 $b=4,5,6$; 若 $a=6$, 则 $b=5,6$, 故所求的概率为
    \[\frac{2\times 2+ 4\times 6}{6\times 6}= \frac79.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    连续抛掷一枚质地均匀的骰子两次得到的点数依次为 $m$ 和 $n$. 若记向量 $\bm{a}=(m, n)$ 与向量 $\bm{b}=(1, -2)$ 的夹角为 $\theta$, 求 $\theta$ 为锐角的概率.
</p>
</myexercise>
<mysolution>
    <p>
    $\theta$ 为锐角等价于 $\bm{a}\cdot\bm{b}> 0$, 即
    \[m-2n>0,\quad m>2n.\]
    当 $n=1$ 时, $m=3,4,5,6$; 当 $n=2$ 时, $m=5,6$, 故所求的概率为 $\dfrac{4+2}{6\times 6}= \dfrac16$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    某中学共有学生 $2000$ 人, 各年级男生、女生人数如下表所示:
    \[\begin{array}{c|ccc}
        \text{姓别} & \text{高一年级} &\text{高二年级} &\text{高三年级}\\\hline
        \text{女生} & 373 & x & y \\
        \text{男生} & 377 & 370 & z
      \end{array}\]
    已知在全校学生中随机抽取 $1$ 名, 抽到高二年级女生的概率是 $0.19$.
</p>

<p>
    (1) 求 $x$ 的值;\qquad
    (2) 现用分层抽样的方法在全校抽取 $48$ 名学生, 则应在高三年级抽取多少名?\qquad
    (3) 已知 $y,z\geqslant 245$, 求高三年级女生比男生多的概率.
</p>
</myexercise>
<mysolution>
    <p>
    (1) $\dfrac{x}{2000}= 0.19$, 则 $x=380$.
</p>

<p>
    (2) 高一、高二、高三年级的人数分别为 $750,750,500$, 比例为 $3:3:2$, 故应在高三年级抽取
    \[\frac{48}{3+3+2}\times 2= 16\ (\text{人}).\]
</p>

<p>
    (3) $y+z= 500$, 结合高三年级女生比男生多知, 
    \[y=251,252,\cdots,255,\]
    故所求的概率为 $\dfrac5{10}= \dfrac12$.
</p>
</mysolution>