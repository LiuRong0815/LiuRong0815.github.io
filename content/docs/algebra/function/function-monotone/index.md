---
# bookCollapseSection: true
title: 函数的单调性
weight: 2
bookHidden: true
prevPage: /docs/algebra/function/function-def
prevPageTitle: 函数的定义
nextPage: /docs/algebra/function/function-oddeven
nextPageTitle: 函数的奇偶性
---

# 函数的单调性

<p>\begin{example}\label{exa:201115-1130}
    若函数 $f(x)= \begin{cases}
        x-1, & x\leqslant 1,\\
        x^2+a, & x>1
    \end{cases}$ 在 $\realnum$ 上单调递增, 求实数 $a$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>由题意,
    \[1-1\leqslant 1^2+a\ \text{即}\ a\geqslant -1,\]
    所以 $a\in[-1,+\infty)$.
</p>
</mysolution>

<myexercise>
    <p>设函数 $f(x)=\begin{cases}
      x^2+1, & x\geqslant 0,\\
      1, & x< 0,\end{cases}$
    解不等式: $f(3-x^2)>f(2x)$.
</p>
</myexercise>
<mysolution>
    <p>    $f(x)$ 单调递增, 则原不等式等价于
    \[3-x^2> 2x,\quad x\in (-3,1).\]
</p>
</mysolution>

</p>
<p>解分段函数单调性问题时, 只需每段函数均单调, 且分段点处的函数值满足题中单调性. 具体来说,
\[\begin{aligned}
    &f(x)= \begin{cases}
            g(x), & x\leqslant a,\\
            h(x), & x>a
        \end{cases}\ \text{在 $\realnum$ 上单调递增}\\
    \Leftrightarrow{}& \left\{\!\!\begin{array}{l}
        \text{$g(x)$ 在 $(-\infty,a]$ 上, $h(x)$ 在 $(a,+\infty)$ 上均单调递增},\\
        g(a)\leqslant h(a)
        \end{array}\right.\\
    &f(x)= \begin{cases}
            g(x), & x\leqslant a,\\
            h(x), & x>a
        \end{cases}\ \text{在 $\realnum$ 上单调递减}\\
    \Leftrightarrow{}& \left\{\!\!\begin{array}{l}
        \text{$g(x)$ 在 $(-\infty,a]$ 上, $h(x)$ 在 $(a,+\infty)$ 上均单调递减},\\
        g(a)\geqslant h(a)
        \end{array}\right.\\
\end{aligned}\]
建议结合如下函数草图记忆上述结论:
<center>
    \includegraphics[scale=1]{2020-1115-1130-1-crop}\qquad
    \includegraphics[scale=1]{2020-1115-1130-2-crop}
</center>
</p>
<p>如果例 \ref{exa:201115-1130} 改为“函数 $f(x)= \begin{cases}
    x-1, & x\leqslant 1,\\
    x^2+2ax, & x>1
\end{cases}$ 在 $\realnum$ 上单调递增”, 则应限制
\[\begin{cases}
    -a\leqslant 1 & (\text{二次函数对称轴在定义域左侧}),\\
    1-1\leqslant 1^2+ 2a\cdot1 & (\text{分段点处的函数值递增}).
    \end{cases}\]
</p>
<p></p>
<p>\begin{example}\label{exa:201115-1140}
    设定义在 $(-1,1)$ 上的奇函数 $f(x)$ 是增函数, 解关于 $a$ 的不等式 
    \[f(a)+f(2a-1)< 0.\]
</p>
</myexample>
<mysolution>
    <p>因为 $f(x)$ 是奇函数, 所以已知不等式化为
    \[f(a)< -f(2a-1)= f(1-2a).\]
    再结合 $f(x)$ 在 $(-1,1)$ 上是增函数可知
    \[\left\{\!\!\begin{array}{l}
        -1< a< 1,\ -1< 1-2a< 1\\
        a< 1-2a,
        \end{array}\right.\ \text{解得}\quad a\in\biggl(0,\frac13\biggr).\]
</p>
</mysolution>
<myremark>
    <p>例 \ref{exa:201115-1140} 中的不等式 $f(a)+f(2a-1)< 0$ 可以称为“抽象不等式”(因为没有具体的表达式), 这类不等式一般先化为“$f(a)< f(b)$”的形式, 再利用函数的单调性去掉“$f$”而转化为具体不等式“$a< b$”或“$a>b$”.
</p>
</myremark>


<p><myexample>
<p>已知函数 $f(x)=\dfrac{ax^2+b}x$, 且 $f(1)=2$, $f(2)=\dfrac52$.
</p>
<p>(1) 确定函数 $f(x)$ 的解析式, 并判断其奇偶性;
</p>
<p>(2) ({\bfseries 选学}) 用定义证明函数 $f(x)$ 在区间 $(-\infty,-1)$ 上单调递增;
</p>
<p>(3) 求满足 $f(1+2t^2)- f(3+t^2)< 0$ 的实数 $t$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>(1) 由题意,
    \[\left\{\!\!\begin{array}{l}
        a+b=2,\\
        \dfrac{4a+b}2= \dfrac52,
       \end{array}\right.\ \text{解得}\quad
       \left\{\!\!\begin{array}{l}
        a=1,\\
        b=1,
       \end{array}\right.\]
    所以 $f(x)=\dfrac{x^2+1}x$. 因为
    \[f(-x)= \frac{(-x)^2+1}{-x}
        = -\frac{x^2+1}x= -f(x),\]
    且 $f(x)$ 的定义域为 $(-\infty,0)\cup (0,+\infty)$, 关于原点对称, 所以 $f(x)$ 为奇函数.
</p>
<p>(2) 任取 $x_1< x_2< -1$, 则
    \[\begin{aligned}
        f(x_1)-f(x_2)
        &= \frac{x_1^2+1}{x_1}- \frac{x_2^2+1}{x_2}
         = \frac{x_2(x_1^2+1)- x_1(x_2^2+1)}{x_1x_2}\\
        &= \frac{x_1^2 x_2- x_1 x_2^2+x_2- x_1}{x_1x_2}
         = \frac{x_1 x_2(x_1- x_2)- (x_1- x_2)}{x_1x_2}\\
        &= (x_1- x_2)\frac{x_1 x_2- 1}{x_1x_2}.
        \end{aligned}\]
    由 $x_1< x_2< -1$ 知,
    \[x_1- x_2< 0,\quad x_1 x_2> 1\ \text{即}\ x_1 x_2- 1>0,\]
    所以 $f(x_1)-f(x_2)< 0$, 说明函数 $f(x)$ 在区间 $(-\infty,-1)$ 上单调递增.
</p>
<p>(3) 不等式化为 $f(1+2t^2)< f(3+t^2)$. 因为 $1+2t^2>1$, $3+t^2>1$, 且
    \[f(x)= \dfrac{x^2+1}x= x+\dfrac1x\quad (\text{对勾函数})\]
    在 $(1,+\infty)$ 上单调递增, 所以前述不等式等价于 
    \[1+2t^2< 3+t^2,\quad \text{解得}\ 
        t\in(-\infty,-\sqrt2)\cup(\sqrt2,+\infty).\]    
</p>
</mysolution>

<myexample>
<p>若对于任意实数 $a\in[-1,1]$, 函数 $y=x^2+(a-4)x+4-2a$ 的值恒大于零, 求 $x$ 的取值范围.
</p>
</myexample>
<mysolution>
    <p>此题可理解为 (反客为主): 关于 $a$ 的函数 
    \[y=f(a)=x^2+(a-4)x+4-2a\]
    在 $[-1,1]$ 上恒大于零. 此时
    \[f(a)= (x-2)a+ x^2-4x+4\]
    为关于 $a$ 的一次函数, 在 $[-1,1]$ 上的图形为一条线段, 所以只需两个端点纵坐标均大于零, 即
    \[\left\{\!\!\begin{array}{l}
        f(-1)= (x-2)\cdot(-1)+ x^2-4x+4>0,\\
        f(1)= (x-2)\cdot 1+ x^2-4x+4>0,
    \end{array}\right.\]
    解得
    \[\left\{\!\!\begin{array}{l}
        x< 1\ \text{或}\ x>2,\\
        x< 2\ \text{或}\ x>3,
    \end{array}\right.\]
    所以 $x\in(-\infty,1)\cup (3,+\infty)$.
</p>
</mysolution>

<myexample>
<p>指出下列函数的单调性和值域:
    \begin{twocolpro}
    (1) $f(x)=x^2+|x|-2$; & (2) $g(x)= \dfrac{3x+1}{x-1}$.
    \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>(1) 方法一: 根据绝对值的定义可知,
    \[f(x)=\begin{cases}
        x^2+x-2,& x\geqslant 0,\\
        x^2-x-2,& x< 0.
        \end{cases}\]
    函数的图形如下 (分别作 $y$ 轴左侧和右侧的图形):
</p>
<p><center>
        \includegraphics[scale=1.1]{2020-1126-1945-crop}
    </center>
</p>
<p>由图得, $f(x)$ 在 $(-\infty,0)$ 上单调递减, 在 $[0,+\infty)$ 上单调递增, 值域为 $[-2,+\infty)$.
</p>
<p>方法二: 因为 $f(-x)=f(x)$, 所以 $f(x)$ 为偶函数, 图形关于 $y$ 轴对称. 令 $x\geqslant 0$ 知, $f(x)=x^2+x-2$, 可作出 $f(x)$ 在 $y$ 轴右侧的图形, 再关于 $y$ 轴作对称图形即可. 答案同上. 
</p>
<p>(2) 将函数变形 (把分子写成“分母的倍数”加“常数”的形式, 再拆项),
    \[g(x)= \frac{3(x-1)+4}{x-1}= 3+\frac4{x-1},\]
    由此可知, $g(x)$ 的图形可由 $h(x)=\dfrac4x$ 的图形向右平移一个单位长度, 再向上平移三个单位长度得到:
</p>
<p><center>
        \includegraphics[scale=1]{2020-1126-2225-crop}
    </center>
</p>
<p>所以, $g(x)$ 在 $(-\infty,1)$ 和 $(1,+\infty)$ 上均单调递减, 值域为 $(-\infty,3)\cup (3,+\infty)$.
</p>
</mysolution>
