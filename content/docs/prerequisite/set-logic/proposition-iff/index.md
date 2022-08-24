---
# bookCollapseSection: true
title: 命题与充要条件
weight: 3
bookHidden: true
prevPage: ../../set-operation
prevPageTitle: 集合的运算
nextPage: ../logical-quantifier
nextPageTitle: 逻辑量词
---

# 命题与充要条件

<p>
可以判断真假的陈述句称为命题 (proposition), 判断为真的语句称为<strong>真命题</strong>, 判断为假的语句称为<strong>假命题</strong>. 
</p>

<p>
在判断命题的真假 (true or false) 时, 对真命题需要证明, 对假命题则只需要举出一个反例. 例如由不等式的性质知“若 $x>2$, $y>1$, 则 $x+y>3$”是真命题, 但“若 $x>2$, $y>1$, 则 $x-y>1$”是假命题, 因为可取 $x=3$, $y=5$ 满足前提但不满足结论. 后一个假命题也表明, <strong>同向不等式不能相减</strong>.</p>


## 充分条件、必要条件

<p>
若条件 $p$ 能推出条件 $q$, 则称 $p$ 为 $q$ 的充分条件 (sufficient condition), $q$ 为 $p$ 的必要条件 (necessary condition). 
  \mymarginpar{可简记为“充分”即是“已知”,“必要”即是“结论”.}
若条件 $p$, $q$ 能互推, 则称 $p$ 为 $q$ 的\myindex{充要条件} (necessary and sufficient condition), 也称 $p$, $q$ 等价, 此时 $q$ 也为 $p$ 的充要条件. 例如, 设 $p\colon x>2$, $q\colon x>1$, 则 $p\Rightarrow q$ 但 $q\nRightarrow p$, 所以 $p$ 是 $q$ 的充分不必要条件, 而 $q$ 是 $p$ 的必要不充分条件. 
</p>

<p>
判断条件 $p$ 对 $q$ 的充分性或必要性时, 可以先确定与两个条件描述对象等价的集合, 
  再由集合的包含关系判断充分性或必要性. 上例中 $p$ 对应区间 $A=(2,+\infty)$, 
  $q$ 对应区间 $B=(1,+\infty)$, 而 $A\subseteq B$ (参考数轴表示),
  所以 $p$ 是 $q$ 的充分不必要条件. 
  \mymarginpar{或简记为 (说法不严谨):\\
    <strong>小集合是充分的, 大集合是必要的</strong>.}  判断多个条件之间的充分性或必要性时, 可以作出推理关系图, 见下面的练习 3.
</p>


## 原命题、逆命题、否命题、逆否命题
<p>
  形如“若 $p$, 则 $q$”的命题可以写出其逆命题、否命题和逆否命题. 四种命题的形式如下:
  \mymarginpar{逆命题和否命题也是互为逆否命题.}
  <center>
    原命题: 若 $p$, 则 $q$;\quad 逆命题: 若 $q$, 则 $p$;\\
    否命题: 若 $\neg p$, 则 $\neg q$;\quad 逆否命题: 若 $\neg q$, 则 $\neg p$.
  </center>
  写否命题时, 一般只需要把原命题的判断词改为其否定形式, 比如“$=$”改为“$\neq$”,“$>$”改为“$\leqslant$”.   注意, <strong>原命题和否命题的真假没有必然联系</strong>.  \mymarginpar{同样也有例子说明原命题和逆命题的真假没有必然联系, 但是<strong>原命题和其逆否命题却是同真假的</strong>.}  例如,“若 $x=1$, 则 $x^2=1$”的否命题为“若 $x\neq 1$, 则 $x^2\neq 1$”, 前者真后者假 (为什么?); 而“若 $x=1$, 则 $x^3=1$”的否命题为“若 $x\neq 1$, 则 $x^3\neq 1$”, 两者都是真命题. 
</p>

<p>
  \lianxi
  <myexercise>
    <p>    将命题“斜率相等的两直线平行”改为“若 $p$, 则 $q$”的形式为\,? 
    它的逆否命题是\,?
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原命题: 若两直线斜率相等, 则它们平行. 逆否命题: 若两直线平行, 则它们斜率相等.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    判断下列命题的真假.
</p>

<p>
    (1) 命题“在 $\triangle ABC$ 中, 若 $AB>AC$, 则 $\angle C>\angle B$”和其否命题.
</p>

<p>
    (2) 命题“若 $ab=0$, 则 $b=0$”和其逆否命题.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    (1) 否命题: 在 $\triangle ABC$ 中, 若 $\angle C>\angle B$, 则 $AB>AC$.
</p>

<p>
    由“大边对大角, 大角对大边”知, 原命题和其否命题均为真命题.
</p>

<p>
    (2) 逆否命题: 若 $b\neq 0$, 则 $ab\neq 0$.
</p>

<p>
    举反例可知, 原命题和其逆否命题均为假命题.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知 $p$, $q$ 都是 $r$ 的必要条件, $s$ 是 $r$ 的充分条件, 
    $q$ 是 $s$ 的充分条件, 
    那么 $r$ 是 $q$ 的 $\underline{\qquad\qquad}$ 条件, 
    $p$ 是 $q$ 的 $\underline{\qquad\qquad}$ 条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    作出推理关系图, 
    \mymarginpar{
    <center>
    \begin{tikzpicture}[scale=1]
      \draw (0,1) node (s) {$s$};
      \draw (1,1) node (r) {$r$};
      \draw (0,0) node (q) {$q$};
      \draw (2,1) node (p) {$p$};
      \graph {(r)->(q)->(s)->(r)->(p)};
    \end{tikzpicture}
    </center>}
  可知 $r$ 是 $q$ 的充要条件, $p$ 是 $q$ 的必要条件.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知 $p(x)\colon x^2 +2x-m>0$, 若 $p(1)$ 是假命题, $p(2)$ 是真命题,
    则实数 $m$ 的取值范围是\,?
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    由题: $1+2-m\leqslant 0$ 且 $4+4-m>0$, 解得 $m\in[3,8)$.
  </p>
</mysolution>
</p>


<p>
  \lianxi
  \begin{exercise}[s]
    下列有关命题的说法中正确的是\,?(填序号)
</p>

<p>
    (1) 命题“若 $x^2 =1$, 则 $x=1$”的否命题为“若 $x^2 =1$, 则 $x\neq 1$”;
</p>

<p>
    (2)“$x=-1$”是“$x^2-5x-6=0$”的必要不充分条件;
</p>

<p>
    (4)“$(x-3)(x-4)=0$”是“$x-3=0$”的充分不必要条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    (1) 错误, 否命题为“若 $x^2\neq 1$, 则 $x\neq 1$”.
</p>

<p>
    (2) 错误, $x^2-5x-6=0\Leftrightarrow x=-1$ 或 $6$, 故“$x=-1$”是“$x^2-5x-6=0$”的充分不必要条件.
</p>

<p>
    (4) 错误, $(x-3)(x-4)=0\Leftrightarrow x-3=0$ 或 $x-4=0$, 故“$(x-3)(x-4)=0$”是“$x-3=0$”的必要不充分条件.
  </p>
</mysolution>
</p>

<p>
  \subsubsection{充要条件的判定}
  <span id="example-"></span>
<myexample>
    <p>
    设 $a$, $b\in \mathbb{R}$, 则“$a>b$”是“$a|a|>b|b|$”
    的$\underline{\qquad\qquad}$条件.
  </p>
</myexample>
</p>

<p>
  <mysolution>
    <p>
    方法一: 分 $a>b\geqslant 0$, $a\geqslant 0>b$, $0>a>b$ 讨论.
</p>

<p>
    方法二: 作 $f(x)= x|x|= \begin{cases}
      x^2,& x\geqslant 0,\\
      -x^2,& x< 0 \end{cases}$ 的图象知, $f(x)$ 为增函数.
    \mymarginpar{两种方法均可得, $a>b\Leftrightarrow a|a|>b|b|$.}
</p>

<p>
    \varexercise $a>b\Leftrightarrow a|a^3|>b|b^3|$.
</p>

<p>
    \varexercise 一般化, $a>b\Leftrightarrow a|a^{2n+1}|>b|b^{2n+1}|$, 其中 $n$ 为正整数.
  </p>
</mysolution>
</p>

<p>
  <span id="example-"></span>
<myexample>
    <p>
    已知 $p\colon x+2\geqslant 0$ 且 $x-10\leqslant 0$, 
    $q\colon 1-m\leqslant x\leqslant 1+m$, $m>0$.
</p>

<p>
    (1) 若 $m=1$, 则 $p$ 是 $q$ 的什么条件\,?
</p>

<p>
    (2) 若 $p$ 是 $q$ 的必要不充分条件, 求实数 $m$ 的取值范围.
  </p>
</myexample>
</p>

<p>
  <mysolution>
    <p>
    $p\colon -2\leqslant x\leqslant 10$.
</p>

<p>
    (1) 若 $m=1$, 则 $q\colon 0\leqslant x\leqslant 2$, $p$ 是 $q$ 的必要不充分条件.
</p>

<p>
    (2) 由题: $1-m\leqslant -2< 10\leqslant 1+m$, 且等号不能同时成立, 则 $m\in[9,+\infty)$.
  </p>
</mysolution>
</p>

<p>
  \subsubsection{课堂评价}
  <myexercise>
    <p>   “$1< x< 2$”是“$x< 2$”成立的$\underline{\qquad\qquad}$条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
   “必要不充分”.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知条件 $p\colon 2^x \geqslant \Bigl(\dfrac12\Bigr)^x$, 
    $q\colon x^2 \geqslant -x$, 则 $p$ 是 $q$ 的$\underline{\qquad\qquad}$条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $p\colon x\geqslant 0$, $q\colon x\leqslant -1$ 或 $x\geqslant 0$, 则 $p$ 是 $q$ 的充分不必要条件.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>   “$x< 0$”是“$\ln(x+1)< 0$”的$\underline{\qquad\qquad}$条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $\ln(x+1)< 0\Leftrightarrow -1< x< 0$, 填“必要不充分”. 
    \mymarginpar{注意对数不等式的解法.}
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知命题“关于 $x$ 的方程 $x^2 +x+a=0$ 有实根”为真命题, 求 $a$ 的取值范围.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    判别式 $\Delta= 1-4a\geqslant 0$, 则 $a\in\Bigl(-\infty,-\frac14\Bigr]$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>   “$\sqrt M>\sqrt N$”是“$M>N$”的$\underline{\qquad\qquad}$条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    前者等价于 $M>N\geqslant 0$, 为后者的充分不必要条件.
    \mymarginpar{对数式应注意真数一定大于 $0$.}
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知命题 $p$: 正数 $a$ 的平方不等于 $0$, 
    命题 $q$: 若 $a$ 不是正数, 则它的平方等于 $0$. 
    那么命题 $p$ 是命题 $q$ 的$\underline{\qquad\qquad}$.
    (填“逆命题”“否命题”“逆否命题”或“否定”.)
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $p$: 若 $a$ 是正数, 则它的平方不等于 $0$. 填“否命题”.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>   “$|x|\geqslant 1$”是“$x>2$”的$\underline{\qquad\qquad}$条件.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $|x|\geqslant 1\Leftrightarrow x\leqslant -1$ 或 $x\geqslant 1$, 填“不要不充分”.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    判断命题“若 $a>b$, $ab\neq 0$, 则 $\frac1a< \frac1b$”的真假.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    举反例 (如 $a=1$, $b=-1$) 可知该命题为假命题. 也可利用函数 $f(x)=\frac1x$ 分段递减的性质.
  </p>
</mysolution>
</p>
