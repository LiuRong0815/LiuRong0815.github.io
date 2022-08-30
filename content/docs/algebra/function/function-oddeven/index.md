---
# bookCollapseSection: true
title: 函数的奇偶性
weight: 3
bookHidden: true
prevPage: /docs/algebra/function/function-monotone
prevPageTitle: 函数的单调性
nextPage: /docs/algebra/function/function-graph
nextPageTitle: 函数的图象
---

# 函数的奇偶性


<p>\subsection{二次函数的图象}
</p>
<p><myexample>
<p>已知二次函数 $y=ax^2+bx+10$ 当 $x=3$ 时的函数值与当 $x=2017$ 时的函数值相等, 求当 $x=2020$ 时的函数值.
</p>
</myexample>
<mysolution>
    <p>由题意, 函数图象的对称轴 $x=-\dfrac{b}{2a}=\dfrac{3+2017}2=2010$.
</p>
<p>方法一: 上式化为 $b=-2020a$, 所以当 $x=2020$ 时, 
  \[\begin{aligned}
    y&= a\cdot 2020^2+b\cdot 2020+10\\
     &= a\cdot 2020^2-2020a\cdot 2020+10
      = 10.\end{aligned}\]
</p>
<p>方法二: 画草图易知, 点 $x=2020$ 关于对称轴 $x=1010$ 的对称点为 $x=0$, 此时函数值为 二次函数的常数项, 即 $0$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知抛物线 $y=(x-c)(x-d)-4$ 与 $x$ 轴的交点为 $(6,0)$ 和 $(1,0)$, 求 $c$, $d$ 的值.
</p>
</myexample>
<mysolution>
    <p>方法一: 由已知可直接写出抛物线的两根式为 
  \[y=(x-6)(x-1),\]
  所以
  \[(x-c)(x-d)-4=(x-6)(x-1)\]
  即
  \[(x-c)(x-d)= x^2-7x+10=(x-2)(x-5),\]
  所以 $c=2$, $d=5$ 或 $c=5$, $d=2$.
</p>
<p>方法二: 将点 $(6,0)$ 和 $(1,0)$ 的坐标代入抛物线表达式,
  \[\left\{\!\!\begin{array}{l}
      (6-c)(6-d)-4=0,\\
      (1-c)(1-d)-4=0,
    \end{array}\right.\ \text{即}\ 
    \left\{\!\!\begin{array}{l}
      c+d=7,\\
      cd=10,
    \end{array}\right.\]
  所以 $c=2$, $d=5$ 或 $c=5$, $d=2$.
</p>
</mysolution>

<p>\begin{example}\label{exa:201115-1045}
    函数 $f(x)= x+\dfrac1x$ ($x\neq 0$) 是奇函数还是偶函数? 写出其单调区间.
</p>
</myexample>
<mysolution>
    <p>因为 
    \[f(-x)= (-x)+\frac1{-x}= -\biggl(x+\frac1x\biggr)= -f(x),\]
    所以 $f(x)$ 是奇函数.
</p>
<p>当 $x$ 是充分小的正数时, $f(x)\approx \dfrac1x$; 当 $x$ 是充分大的正数时, $f(x)\approx x$. 再结合
    \[f\biggl(\frac14\biggr)= f(4)= \frac{17}4,\ 
      f\biggl(\frac13\biggr)= f(3)= \frac{10}3,\ 
      f\biggl(\frac12\biggr)= f(2)= \frac{5}2,\ 
      f(1)= 2,\]
    可以描点作图如下 (第三象限的图形与第一象限的图形关于原点对称):
    <center>
        \includegraphics[scale=1]{2020-1115-1100-crop}
    </center>
    由图可以看出 $f(x)$ 的单调递增区间为 $(-\infty,-1]$ 和 $[1,+\infty)$, 单调递减区间为 $(-1,0)$ 和 $(0,1)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201115-1045} 中的函数 $f(x)= x+\dfrac1x$ ($x\neq 0$) 一般形象地称为“对勾函数”, 第一象限图形的最低点 $(1,2)$ 可由均值不等式得到. $f(x)$ 的图形有两条渐近线: $y=x$ 和 $x=0$ (即 $y$ 轴), 符合双曲线的特点 (有两条渐近线). 观察 $f(x)$ 的图形可知, 若 $x\geqslant 3$, 则 $f(x)\geqslant f(3)$, 即此时 $f_{\min}=f(3)$. 类似地, 若 $x\geqslant \dfrac12$, 则 $f_{\min}=f(1)$. 
</p>
<p>一般地, $f(x)= x+\dfrac{k}x$ ($k>0$, $x\neq 0$) 均可称为“对勾函数”. 由与前面类似的分析可得, $f(x)$ 是奇函数, 有两条渐近线 $y=x$ 和 $x=0$, 第一象限图形的最低点为 $(\sqrt{k},2\sqrt{k})$, 单调递增区间为 $(-\infty,-\sqrt{k}]$ 和 $[\sqrt{k},+\infty)$, 单调递减区间为 $(-\sqrt{k},0)$ 和 $(0,\sqrt{k})$.
</p>

<p>\begin{example}\label{exa:201115-1210}
    已知 $f(x)= ax^7-bx^5+cx^3+2$, 且 $f(-5)=m$, 求 $f(-5)+f(5)$ 的值.
</p>
</myexample>
<mysolution>
    <p>直接代入知,
    \[\begin{aligned}
    f(-5)+f(5)
      ={}& [a\cdot (-5)^7- b\cdot (-5)^5+ c\cdot (-5)^3+2] \\
         & + [a\cdot 5^7- b\cdot 5^5+c\cdot 5^3+2]\\
      ={}& 4.\end{aligned}\]
</p>
</mysolution>
</p>
<p>例 \ref{exa:201115-1210} 中的“$f(-5)=m$”是多余的条件. 如果注意到 $g(x)=ax^7-bx^5+cx^3$ 是奇函数, 则可以简洁地得到更一般地结论:
\[f(-x)+f(x)= [g(-x)+g(x)]+2\cdot 2= 4.\]
</p>

<p>\subsection{利用函数性质解题}
</p>
<p>常见的函数性质有: 单调性, 奇偶性, 对称性, 周期性等. 解题时, 适当运用这些性质可以达到事半功倍的效果.
</p>
<p>\begin{example}\label{exa:201129-0950}
    若 $a>\dfrac1a$, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>方法一: 不等式化为 
    \[a-\frac1a>0\Rightarrow \frac{a^2-1}a>0\Rightarrow (a^2-1)a>0,\]
    所以
    \[\left\{\!\!\begin{array}{l}
        a^2-1>0,\\
        a>0,
        \end{array}\right.\ \text{或}\quad
      \left\{\!\!\begin{array}{l}
        a^2-1< 0,\\
        a< 0,
        \end{array}\right.\]
    解得 $a>1$ 或 $a< -1$, 即 $a\in(-\infty,-1)\cup(1,+\infty)$.
</p>
<p>方法二: 画出函数 $f(a)=a$ 和 $g(a)=\dfrac1a$ 的图形. 不等式表明 $f(a)>g(a)$, 对应前者图形在后者图形上方的情形 (即直线在上方, 双曲线在下方). 由图可知 $a\in(-\infty,-1)\cup(1,+\infty)$.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1129-0950-crop}
    </center>
</p>
<p>方法三: 也可以将不等式化为 $a-\dfrac1a>0$, 令 $h(a)= a-\dfrac1a$, 再作图求解. 只需留意函数 $h(a)$ 在 $(-\infty,0)$ 和 $(0,+\infty)$ 上均单调递增, 且与横轴的交点为 $(-1,0)$ 和 $(1,0)$ (参考“2020 年 11 月 8 日答疑记录”的例 \ref{exa:201206-1410}).
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 例 \ref{exa:201129-0950} 的方法一是代数解法, 变形后的式子 $(a^2-1)a>0$ 是三次不等式, 仍需要分类讨论, 各自求解后再取并集.
</p>
<p>(2) 方法二和方法三均利用了函数图形 (前者两个, 后者一个), 用这种方法时需要根据题意构造容易画出大致图形的函数, 也就是要事先了解函数的特点 (单调性、奇偶性、对称性、与坐标轴的交点, 等等).
</p>
</myremark>
</p>
<p>\begin{example}\label{exa:201129-1010}
    设定义在 $(-1,1)$ 上的奇函数 $f(x)$ 是增函数, 且 $f(a)+f(2a-1)< 0$, 求 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 是奇函数, 所以不等式化为 
    \[f(a)< -f(2a-1)=f(1-2a).\]
    结合 $f(x)$ 是定义在 $(-1,1)$ 上的增函数知
    \[\left\{\!\!\begin{array}{l}
        -1< a< 1,\\
        -1< 1-2a< 1,\\
        a< 1-2a,
        \end{array}\right.\ \text{解得}\quad
      0< a< \frac13,\]
    即 $a\in\biggl(0,\dfrac13\biggr)$.
</p>
</mysolution>
</p>
<p>例 \ref{exa:201129-1010} 中主要利用“$f(x)$ 是增函数”将抽象的不等式 (没有具体解析式的不等式) 
\[f(a)< f(1-2a)\]
化为具体的不等式 
\[a< 1-2a.\]
再如, 若 $f(x)$ 是减函数, 则由 $f(a)< f(2a+1)$ 可知 $a>2a+1$. 在去掉“$f$”时, 也需要注意 $f$ 的作用范围 (即题中 $f(x)$ 的定义域).
</p>

<p>\begin{example}\label{exa:201206-1300}
    已知函数 $f(x)$ 为奇函数, 且当 $x>0$ 时, $f(x)= x^2+\dfrac1x$, 求当 $x< 0$ 时 $f(x)$ 的解析式.
</p>
</myexample>
<mysolution>
    <p>方法一: 若 $x< 0$, 则 $-x>0$, 由题意, 此时 
    \[f(-x)= (-x)^2+\frac1{-x}= x^2-\frac1x.\]
    因为 $f(x)$ 为奇函数, 所以 $f(-x)= -f(x)$, 代入上式可得
    \[-f(x)= x^2-\frac1x,\quad\text{即}\quad f(x)=-x^2+\frac1x.\]
    此即为当 $x< 0$ 时 $f(x)$ 的解析式.
</p>
<p>方法二 (将方法一的步骤压缩): 因为 $f(x)$ 为奇函数, 所以当 $x< 0$ 时, 
    \[f(x)= -f(-x)= -\biggl(x^2-\frac1x\biggr)= -x^2+\frac1x.\]
</p>
</mysolution>


<myexample>
<p>设奇函数函数 $f(x)$ 在 $(-\infty,+\infty)$ 上单调递减, 且 $f(1)=-1$, 求不等式 $-1\leqslant f(x-1)\leqslant 1$ 的解集.
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 为奇函数, 所以由 $f(1)=-1$ 可知 $f(-1)=1$, 不等式化为
    \[f(1)\leqslant f(x-1)\leqslant f(-1).\]
    又因为 $f(x)$ 在 $(-\infty,+\infty)$ 上单调递减, 所以
    \[1\geqslant x-1\geqslant -1,\quad\text{解得}\quad 
        0\leqslant x\leqslant 2,\]
    即所求解集为 $[0,2]$.
</p>
</mysolution>
</p>
<p>\begin{example}\label{exa:201204-2125}
    已知定义在 $\realnum$ 上的奇函数 $f(x)$ 满足 $f(x+4)=f(x)$ 且 $f(1)=1$, 求 $f(3)+f(4)+f(5)$ 的值.
</p>
</myexample>
<mysolution>
    <p>对定义在 $\realnum$ 上的奇函数 $f(x)$, 恒有 $f(-x)=-f(x)$. 令 $x=0$ 得 $f(0)=-f(0)$, 所以 $f(0)=0$. 结合 $f(x+4)=f(x)$ 知,
    \[\begin{aligned}
        \text{令 $x=0$:}&\ f(4)=f(0)=0,\\
        \text{令 $x=1$:}&\ f(5)=f(1)=1,\\
        \text{令 $x=-1$:}&\ f(3)=f(-1)=-f(1)=-1.
    \end{aligned}\]
    所以 $f(3)+f(4)+f(5)= (-1)+0+1=0$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 由上面的解法可知, 条件“$f(1)=1$”是多余的, 因为只需要推出 $f(4)=0$ 和 $f(3)=-f(1)$ 即可得到最终结论.
</p>
<p>(2) 例 \ref{exa:201204-2125} 中还证明了一个结论 (可当作定理直接使用): 若 $f(x)$ 为定义在 $\realnum$ 上的奇函数, 则 $f(0)=0$.
</p>
</myremark>

<myexample>
<p>(1) 若 $f(x)$ 为奇函数, 当 $x>0$ 时, $f(x)=x(1-\sqrt[3]{x})$, 求当 $x< 0$ 时, $f(x)$ 的解析式;
</p>
<p>(2) 若 $f(x)$ 为偶函数, 当 $-1\leqslant x< 0$ 时, $f(x)=\sqrt[5]{x}+1$, 求当 $0< x\leqslant 1$ 时, $f(x)$ 的解析式;
</p>
</myexample>
<mysolution>
    <p>以下过程较简略, 更详细的过程可参考“2020 年 11 月 14 日答疑记录”的例 \ref{exa:201206-1300} 方法一.
</p>
<p>(1) 因为 $f(x)$ 为奇函数, 所以当 $x< 0$ 时,
    \[f(x)= -f(-x)= -(-x)(1-\sqrt[3]{-x})= x(1+\sqrt[3]{x}).\]
</p>
<p>(2) 因为 $f(x)$ 为偶函数, 所以当 $0< x\leqslant 1$ 时,
    \[f(x)= f(-x)= \sqrt[5]{-x}+1= -\sqrt[5]{x}+1.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>若函数 $f(x)$ 在 $\realnum$ 上为偶函数, 且当 $x>0$ 时, $f(x)=-x+1$, 求 $f(x)< -1$ 的解集.
</p>
</myexample>
<mysolution>
    <p>函数 $f(x)$ 在 $\realnum$ 上为偶函数, 表明其图形关于 $y$ 轴对称. 直接根据对称性画图可知, $x\in(-\infty,-2)\cup(2,+\infty)$.
</p>
<p><center>
        \includegraphics[scale=1]{2020-1206-1320-crop}
    </center>
</p>
</mysolution>

