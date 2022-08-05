---
# bookCollapseSection: true
title: 一元二次方程的解法
weight: 2
prevPage: ../quadratic-factorization
prevPageTitle: 二次三项式的因式分解
nextPage: ../veita-theorem
nextPageTitle: 韦达定理
---

# 一元二次方程的解法

关于 $x$ 的一元二次方程 $ax^2+bx+c= 0$ ($a\neq 0$) 的解法通常有三种: 因式分解法、配方法、求根公式法. 较常用的是第一种和第三种.

## 因式分解法

因式分解法是指将方程 $ax^2+bx+c= 0$ 化为 \\[(Ax+B)(Cx+D)=0\\] 的形式, 则 \\[Ax+B=0\quad \text{或}\quad Cx+D=0,\\] 再解这两个一次方程. 例如, 解方程 $x^2-2x-3=0$, 可先将方程化为 \\[(x+1)(x-3)=0,\\] 则 \\[x+1=0\quad \text{或}\quad x-3=0,\\] 解得 $x=-1$ 或 $3$.

使用因式分解法时, 需要熟练掌握[二次三项式因式分解](../quadratic-factorization) 的常用方法.

## 配方法

除用于因式分解外, [配方法](../quadratic-factorization#配方法) 也可用于解一元二次方程. 仍以方程 $x^2-2x-3=0$ 为例, 用配方法求解, 则 \\[(x-1)^2=4,\quad\text{即}\quad x-1=\pm2,\\] 所以 $x=-1$ 或 $3$.

<myremark>
    <p>(1) 由 $x^2=n$ ($n>0$) 应得 $x=\pm\sqrt{n}$, 即不要遗漏负根;</p>
    <p>(2) 使用配方法解方程时, 变形过程与因式分解时的过程略有区别, 一般将方程改写为 $(x+m)^2=n$ ($n\geqslant0$) 的形式.</p>
</myremark>

<span id="求根公式"></span>
## 求根公式法

<p>一元二次方程 $ax^2+bx+c= 0$ ($a\neq 0$) 的求根公式源自配方法. 具体的变形过程为 \[\begin{aligned}
    x^2+\frac{b}a x+ \frac{c}a &= 0,\\
    x^2+\frac{b}a x+ \frac{b^2}{4a^2} &= \frac{b^2}{4a^2}- \frac{c}a,\\
    \biggl(x+\frac{b}{2a}\biggr)^2 &= \frac{b^2-4ac}{4a^2}.
    \end{aligned}\]
所以当 (且仅当) $b^2-4ac\geqslant 0$ 时, \[\begin{gathered}
    x+\dfrac{b}{2a}= \pm\dfrac{\sqrt{b^2-4ac}}{2a},\\
    x= \frac{-b\pm\sqrt{b^2-4ac}}{2a}.
\end{gathered}\]
通常记 $\Delta= b^2-4ac$, 上述求根公式又可写为 (更容易记忆的) $x= \dfrac{-b\pm\sqrt{\Delta}}{2a}$.</p>

上面引进的 $\Delta= b^2-4ac$ 也称为方程 $ax^2+bx+c= 0$ ($a\neq 0$) 的**判别式**, 因为前面变形过程的最后一行表明, $\Delta$ 的正负号可以判别方程实根的个数: 

- 当 $\Delta>0$ 时, 方程有两个不等实根
- 当 $\Delta=0$ 时, 方程有两个相等实根
- 当 $\Delta<0$ 时, 方程没有实根

例如, 方程 $x^2+x+1= 0$ 的判别式 $\Delta= -3<0$, 所以方程无实根; 方程 $x^2+x-2= 0$ 的判别式 $\Delta= 9>0$, 所以方程有两个不等实根; 方程 $x^2+2x+1= 0$ 的判别式 $\Delta= 0$, 所以方程有两个相等实根.

对关于 $x$ 的二次三项式 $ax^2+bx+c$, 令其为 $0$ 就转化成二次方程, 所以此时 $\Delta= b^2-4ac$ 也称为该二次三项式的判别式. 利用判别式 $\Delta$ 也可以判断二次三项式 $ax^2+bx+c$ 是否可以因式分解. 如果该式可以因式分解, 必可分解为 $(Ax+B)(Cx+D)$ 的形式, 令其等于 $0$, 可解出对应的 $x$ 值. 反之, 若 $ax^2+bx+c=0$ 有实根, 则 $\Delta\geqslant 0$, [配方法](../quadratic-factorization#配方法) 变形的最后一行可改写为 \\[a\biggl[\biggl(x+\frac{b}{2a}\biggr)^2- \frac{\Delta}{4a^2}\biggr],\\] 继而可以使用平方差公式. 所以“$ax^2+bx+c$ 可以因式分解”等价于“$ax^2+bx+c=0$ 有实根”, 即

- 当 $\Delta>0$ 时, $ax^2+bx+c$ 可以因式分解
- 当 $\Delta=0$ 时, $ax^2+bx+c$ 可以因式分解且为完全平方式
- 当 $\Delta<0$ 时, $ax^2+bx+c$ 不可以因式分解

例如, $x^2+x+1$ 的判别式 $\Delta= -3<0$, 所以无法因式分解; $x^2+x-2$ 的判别式 $\Delta= 9>0$, 所以 \\[
    x^2+x-2= (x+2)(x-1);\\]
$x^2+2x+1= 0$ 的判别式 $\Delta= 0$, 所以 \\[
    x^2+2x+1= (x+1)^2.\\]

<myremark>
    <p>(1) 以上讨论均限制实数范围. 高中数学将介绍复数 (包含了实数), 而关于 $x$ 的方程 $ax^2+bx+c= 0$ ($a\neq 0$) 一定有复数解, 所以 $ax^2+bx+c$ 一定可以在复数范围内因式分解;
    </p>
    <p>(2) 解一元二次方程时, 优先考虑因式分解法, 然后是求根公式法; 根据系数特点 (如二次项系数为 $1$ 且一次项系数为偶数), 有时也可考虑配方法.
    </p>
    <p>(3) 由前面的求根公式变形过程可知, 若关于 $x$ 的二次方程 \[
        ax^2+bx+c= 0\quad (a\neq 0)\]
    有两个根 $x_1,x_2$, 则 \[
        ax^2+bx+c= a(x-x_1)(x-x_2).\]
    这就是二次三项式的因式分解中的求根法. 上述结论可以推广 (证明方法有变化), 例如, 若关于 $x$ 的三次方程 \[
        ax^3+bx^2+cx+d= 0\quad (a\neq 0)\]
    有三个根 $x_1,x_2,x_3$, 则 \[\begin{aligned}
        &ax^3+bx^2+cx+d\\
        ={}& a(x-x_1)(x-x_2)(x-x_3).\end{aligned}\]</p>
</myremark>