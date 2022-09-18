---
# bookCollapseSection: true
title: 函数的奇偶性
weight: 3
# bookHidden: true
prevPage: /docs/algebra/function/function-monotone
prevPageTitle: 函数的单调性
# nextPage: /docs/algebra/function/function-graph
# nextPageTitle: 函数的图象
---

# 函数的奇偶性

<p>函数的奇偶性 (odevity) 描述的是其图象的对称性. 若图象关于原点对称, 则称其为<strong>奇函数</strong> (odd function);
</p>

<img alt="奇函数示意图" src="/figs/2022/2022-09/2022-0917-0900.svg"></img>

<p>若图象关于 $y$ 轴对称, 则称其为<strong>偶函数</strong> (even function).
</p>

<img alt="偶函数示意图" src="/figs/2022/2022-09/2022-0917-0910.svg"></img>

<p>上面的描述性定义都隐含了“函数的定义域关于原点对称”, 也就是 $a$ 与 $-a$ 应同时在定义域中. 例如, $\mathbf{R}$, $[-3,3]$, $(-\infty,-1)\cup (1,+\infty)$ 均关于原点对称, 但是 $(-3,3]$, $(-\infty,-1)\cup [1,+\infty)$ 均不关于原点对称.
</p>
<p>利用<a href="/docs/prerequisite/ms-function/axis-coordinate/#点的变换-2022-0917-0916">点的变换</a>可以得到函数奇偶性的代数表示. 设函数 $f(x)$ 的定义域 $D$ 关于原点对称, 则 \[\begin{aligned}
    &f(x)\text{\,为偶函数}\Leftrightarrow f(-x)=f(x)\Leftrightarrow f(-x)-f(x)=0,\\
    &f(x)\text{\,为奇函数}\Leftrightarrow f(-x)=-f(x)\Leftrightarrow f(-x)+f(x)=0.
\end{aligned}\]
定义中的 $x$ 应整体对待, 例如, 对奇函数 $f(x)$, \[
    f(-x+1)= f(-(x-1))= -f(x-1),\]
而不能简单地认为 $f(-x+1)= -f(x+1)$. 有些函数, 如 $f(x)= x+1$ 没有奇偶性, 称为非奇非偶函数. 由上述定义可以得到关于函数奇偶性的几个简单性质.
</p>

<p>(1) 常值函数 $f(x)= k$ 必为偶函数.
</p>
<p>(2) 若函数 $f(x)$ 既是奇函数又是偶函数, 则 \[
    f(-x)= -f(x)= f(x)\Rightarrow f(x)= 0,\]
即在不考虑定义域时, 仅有零函数 (取值恒为 $0$) 既是奇函数又是偶函数.
</p>
<p>(3) 若奇函数 $f(x)$ 的定义域为 $D$, 且 $0\in D$, 则 \[
    f(-0)= -f(0)= f(0)\Rightarrow f(0)= 0,\]
即此时函数图象必过原点.
</p>
<p>(4) $f(x)$ 为偶函数的定义等价于“$f(x)$, $f(|x|)$, $f(-x)$ 中有两者相等”. 利用绝对值的性质 $|x|= |-x|$ 可以证明此结论.
</p>

<myremark>
    <p>(1) 对函数 $f(x)= x^n$, 当指数 $n$ 为奇 (偶) 数时, $f(x)$ 为奇 (偶) 函数. 这大概是“奇偶性”的来历.
    </p>
    <p>(2) 奇函数 $f(x)$ 的代数特征 $f(-x)= -f(x)$, 可以形象地理解为“负号可以自由进出 $f$”; 偶函数 $f(x)$ 的代数特征 $f(-x)= -f(x)$, 可以形象地理解为“负号会被 $f$ 吸收”; 
    </p>
    <p>(3) 函数的奇偶性的进一步推广是函数图象的中心对称性与轴对称性. 一般地, 设函数 $f(x)$ 的定义域关于点 $a$ 对称, 则 \[\begin{aligned}
        f(x)\ \text{的图象关于点 $(a,b)$ 对称}
            &\Leftrightarrow f(a+x)+f(a-x)=2b,\\
        f(x)\ \text{的图象关于直线 $x=a$ 对称}
            &\Leftrightarrow f(a+x)=f(a-x).
        \end{aligned}\]
    上述定义均可以利用点的变换 (结合数轴上 $a+x$ 与 $a-x$ 关于 $a$ 对称) 来理解.
    </p>
</myremark>

<myexample>
    <p>设 $f(x)= ax^2 + bx+ c$, 求 $f(x)$ 分别是奇函数和偶函数的充要条件.
    </p>
</myexample>

<mysolution>
    <p>$f(x)$ 是奇函数等价于 $f(-x)= -f(x)$, 整理得 $ax^2+ c= 0$, 由 $x$ 的任意性知 $a=c=0$. 同理可得 $f(x)$ 是偶函数的充要条件是 $b=0$.
    </p>
</mysolution>

<myremark>
    <p>上例可以一般化: 若 $f(x)= ag(x)+bh(x)$, 且 $g(x)$ 为奇函数, $h(x)$ 为偶函数, 则 \[\begin{aligned}
        &f(x)\ \text{为奇函数}\Leftrightarrow b=0,\\
        &f(x)\ \text{为偶函数}\Leftrightarrow a=0.
    \end{aligned}\]
    </p>
</myremark>

<myexercise>
    <p>(1) 若函数 $f(x)=(x+a)(x-4)$ 为偶函数, 求 $a$ 的值;
    </p>
    <p>(2) 若函数 $f(x)= kx^2+(k-1)x+2$ 是偶函数, 求 $f(x)$ 的单调递减区间.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $f(-x)=f(x)$, 化简得 $a=4$.
    </p>
    <p>(2) 由题 $k=1$, $f(x)=x^2+2$, 则 $f(x)$ 的单调递减区间是 $(-\infty,0]$.
    </p>
</details>

## 奇偶性的判断方法

<p>判断函数 $f(x)$ 的奇偶性之前, 应确保其定义域 $D$ 关于原点对称; 然后检验 $f(-x)= -f(x)$ 和 $f(-x)= f(x)$ 之一是否恒成立. 检验后两个式子, 常用的方法是: 直接变形; 作差法, 如 $f(-x)= -f(x)$ 等价于 $f(-x)+f(x)= 0$; 作商法, 如 $f(-x)= -f(x)$ ($f(x)\neq 0$) 等价于 $\dfrac{f(-x)}{f(x)}= -1$.
</p>

<p>由奇偶性的定义可以进一步得到结论: 设函数 $f(x)$, $g(x)$ 均定义在数集 $D$ 上, 且 $D$ 关于原点对称, 实数 $k$ 为常数, 则
</p>
<p>(1) 当 $k\neq 0$ 时, $f(x)$ 与 $kf(x)$ 的奇偶性相同;
</p>
<p>(2) 若 $f(x)$, $g(x)$ 均为奇 (偶) 函数, 则 $f(x)+g(x)$ 也为奇 (偶) 函数;
</p>
<p>(3) 若 $f(x)$, $g(x)$ 奇偶性相同, 则 $f(x)g(x)$, $\dfrac{f(x)}{g(x)}$ ($g(x)\neq 0$) 均为偶函数; 若 $f(x)$, $g(x)$ 一奇一偶, 则 $f(x)g(x)$, $\dfrac{f(x)}{g(x)}$ ($g(x)\neq 0$) 均为奇函数.
</p>
<p>下面用定义证明 (3) 的部分结论: 设 $f(x)$, $g(x)$ 均为奇函数, 则 \[
    f(-x)= -f(x),\quad g(-x)= -g(x)\]
所以 \[
    f(-x)g(-x)= (-f(x))\cdot (-g(x))= f(x)g(x),\]
即 $f(x)g(x)$ 是偶函数. 同理可证其他情形.
</p>

<p>用上述结论来判断函数的奇偶性是比较方便的. 例如, 设函数 $f(x)= x^3 -x$, 因为 $y= x^3$ 与 $y= -x$ 均为奇函数, 所以 $f(x)$ 也为奇函数.</p>

## 求带奇偶性的函数解析式

若函数 $f(x)$ 为奇函数或偶函数, 且已知其在区间 $(a,b)$ 上的解析式, 则利用奇偶性可以求出 $f(x)$ 在区间 $(-b,-a)$ 上的解析式. 

<myexample>
    <p>设 $f(x)$ 是 $\mathbf{R}$ 上的奇函数, 当 $x\leqslant 0$ 时, $f(x)= 2x^2-x$, 求 $f(1)$ 和 $f(x)$ 的解析式.
    </p>
</myexample>

<mysolution>
    <p>因为 $f(x)$ 是奇函数, 所以 \[
        f(-1)= -f(1)\Rightarrow f(1)= -f(-1)= -3.\]
    </p>
    <p>下面确定当 $x> 0$ 时, $f(x)$ 的解析式. 此时 $-x< 0$, 代入已知解析式, \[
        f(-x)= 2(-x)^2-(-x)\Rightarrow 
        -f(x)= 2x^2+x,\]
    所以 $f(x)= -2x^2-x$. 故所求的解析式为 \[f(x)= \begin{cases}
        2x^2-x, & x\leqslant 0,\\
        -2x^2-x, & x>0.
    \end{cases}\]
    </p>
</mysolution>

<myexercise>
    <p>已知函数 $f(x)$ ($x\neq 0$) 为偶函数, 且当 $x< 0$ 时, $f(x)=x^2 -\dfrac1x$,
    求 $f(1)$ 和 $f(x)$ 的解析式.
  </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>$f(1)=f(-1)=2$, 所求的解析式为 \[f(x)= \begin{cases}
        x^2 -\dfrac1x, & x< 0,\\[6pt]
        x^2 +\dfrac1x, & x> 0.
    \end{cases}\]
    </p>
</details>

## 奇偶性的简单应用

<myexample>
    <p>已知 $f(x)$, $g(x)$ 分别是定义在 $\mathbf{R}$ 上的偶函数和奇函数, 且 \[
        f(x)-g(x)= x^3 +x^2 +1.\]
    </p>
    <p>(1) 求 $f(1)+g(1)$, $f(1)$;
    </p>
    <p>(2) 求 $f(1)+g(2)$.
    </p>
</myexample>

<mysolution>
    <p>(1) 由已知, \[\begin{gathered}
        f(-x)-g(-x)= -x^3+x^2+1,\\
        f(x)+g(x)= -x^3+x^2+1,
    \end{gathered}\]
    所以 $f(1)+g(1)= 1$. 再由 $f(1)-g(1)=3$ 解得 $f(1)=2$.
    <p>(2) 解方程组 \[\left\{\!\!\begin{array}{l}
        f(x)-g(x)= x^3 +x^2 +1,\\
        f(x)+g(x)=-x^3+x^2+1
    \end{array}\right. \Rightarrow
    \left\{\!\!\begin{array}{l}
        f(x)= x^2+1,\\
        g(x)= -x^3,
    \end{array}\right.\]
    所以 $f(1)+g(2)=2-8=-6$.
    </p>
</mysolution>

<myremark>
    <p>类似于上例的推导, 可以进一步得到: 若函数 $f(x)$ 的定义域 $D$ 关于原点对称, 则 $f(x)$ 可以写成奇函数 $\dfrac{f(x)-f(-x)}2$ 与偶函数 $\dfrac{f(x)+f(-x)}2$ 之和.
    </p>
</myremark>

<myexercise>
    <p>(1) 已知 $f(x)$ 是奇函数, $g(x)$ 是偶函数, 且 \[
        f(-1)+g(1)=2,\quad f(1)+g(-1)=4,\]
    求 $g(1)$.
    </p>
    <p>(2) 已知 $f(x)$ 为奇函数, $g(x)=f(x)+9$, $g(-2)=3$, 求 $f(2)$.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) $-f(1)+g(1)=2$ 且 $f(1)+g(1)=4$, 则 $g(1)=3$.
    </p>
    <p>(2) $g(-2)=f(-2)+9$ 即 $3=-f(2)+9$, 则 $f(2)=6$.
    </p>
</details>

<myexample>
    <p>已知 $f(x)= ax^5+bx^3+2$, 且 $f(-5)= 8$, 求 $f(5)$ 的值.
    </p>
</myexample>

<mysolution>
    <p>方法一: 直接代入, \[\begin{aligned}
        f(-5)&= a\cdot (-5)^5+ b\cdot (-5)^3+2,\\
        f(5)&=  a\cdot 5^5+b\cdot 5^3+2,
    \end{aligned}\]
    相加并化简, $f(-5)+f(5)= 4$, 即 $8+f(5)=4$, 所以 $f(5)= -4$.
    </p>
    <p>方法二: 分离出 $f(x)$ 中含参数 $a$, $b$ 的部分, 设 \[
        g(x)= f(x)- 2= ax^5+bx^3,\]
    则 $g(x)$ 是奇函数, 满足 $g(-x)+g(x)=0$. 取 $x=5$, 得到 \[
        [f(-5)-2]+ [f(5)-2]= 0\Rightarrow
        f(-5)+ f(5)= 4.\]
    同样可得 $f(5)= -4$.
    </p>
</mysolution>

奇偶性可以与单调性结合, 来解抽象不等式.

<myexample>
    <p>设函数 $f(x)$ 在区间 $[0,+\infty)$ 上单调递增, 分别在下列条件下解不等式 $f(2x-1)< f(1)$:
    </p>
    <p>(1) $f(x)$ 为偶函数;
    </p>
    <p>(2) $f(x)$ 为奇函数.
    </p>
</myexample>

<mysolution>
    <p>(1) 当 $f(x)$ 为偶函数时, 其图象关于 $y$ 轴对称, 根据 $f(x)$ 在区间 $[0,+\infty)$ 上单调递增作出其图象的草图如下:
    </p>
    <img alt="偶函数在 y 轴右侧单增" src="/figs/2022/2022-09/2022-0917-1700.svg"></img>
    <p>将 $2x-1$ 视为整体, 由图可知, $f(2x-1)< f(1)$ 等价于 $-1< 2x-1< 1$, 解得  $x\in (0,1)$.
    </p>
    <p>(2) 当 $f(x)$ 为奇函数时, 其图象关于原点对称, 且由 $f(x)$ 在点 $x=0$ 处有定义知 $f(0)=0$. 根据 $f(x)$ 在区间 $[0,+\infty)$ 上单调递增作出其图象的草图如下:
    </p>
    <img alt="奇函数在 y 轴右侧单增且过原点" src="/figs/2022/2022-09/2022-0917-1710.svg"></img>
    <p>由图可知, $f(2x-1)< f(1)$ 等价于 $2x-1< 1$, 解得 $x\in (-\infty,1)$.
    </p>
</mysolution>

<myremark>
    <p>由单调性的定义可以验证, 在区间 $(-\infty,0]$ 与 $[0,+\infty)$ 上, 偶函数的单调性“相反”, 奇函数的单调性“相同”.
    </p>
</myremark>

<myexample>
    <p>设定义在 $(-1,1)$ 上的奇函数 $f(x)$ 是增函数, 且 $f(a)+f(2a-1)< 0$, 求 $a$ 的取值范围.
    </p>
</myexample>

<mysolution>
    <p>因为 $f(x)$ 是奇函数, 所以不等式化为 \[
        f(a)< -f(2a-1)=f(1-2a).\]
    结合 $f(x)$ 是定义在 $(-1,1)$ 上的增函数知 \[\left\{\!\!\begin{array}{l}
        -1< a< 1,\\
        -1< 1-2a< 1,\\
        a< 1-2a
    \end{array}\right.\Rightarrow
      0< a< \frac13,\]
    即 $a\in\biggl(0,\dfrac13\biggr)$.
    </p>
</mysolution>

<myremark>
    <p>将不等式 $f(a)+f(2a-1)< 0$ 利用奇偶性化为 $f(a)< f(1-2a)$, 从而可以进一步利用单调性去掉“$f$”. 此时也需要注意对应法则 $f$ 的作用范围 (即题中 $f(x)$ 的定义域).
    </p>
</myremark>

<myexercise>
    <p>(1) 设奇函数函数 $f(x)$ 在 $(-\infty,+\infty)$ 上单调递减, 且 $f(1)=-1$, 解不等式 \[
        -1\leqslant f(x-1)\leqslant 1;\]
    </p>
    <p>(2) 若函数 $f(x)$ 在 $\mathbf{R}$ 上为偶函数, 且当 $x>0$ 时, $f(x)=-x+1$, 求 $f(x)< -1$ 的解集.
    </p>
</myexercise>

<details><summary>参考答案</summary>
    <p>(1) 因为 $f(x)$ 为奇函数, 所以由 $f(1)=-1$ 可知 $f(-1)=1$, 不等式化为 \[
        f(1)\leqslant f(x-1)\leqslant f(-1).\]
    又因为 $f(x)$ 在 $(-\infty,+\infty)$ 上单调递减, 所以 \[
        1\geqslant x-1\geqslant -1\Rightarrow
        0\leqslant x\leqslant 2,\]
    即所求解集为 $[0,2]$.
    </p>
    <p>(2) 函数 $f(x)$ 在 $\mathbf{R}$ 上为偶函数, 表明其图象关于 $y$ 轴对称. 直接根据对称性画图可知, $x\in(-\infty,-2)\cup(2,+\infty)$.
    </p>
</details>

## “对勾”函数

<p>考虑函数 $f(x)= x+\dfrac1x$ ($x\neq 0$), 因为 \[
    f(-x)= (-x)+\frac1{-x}= -\biggl(x+\frac1x\biggr)= -f(x),\]
所以 $f(x)$ 是奇函数. 若 $x>0$, 则 $f(x)>0$, 且当 $x$ 是充分小的正数时, $f(x)\approx \dfrac1x$; 当 $x$ 是充分大的正数时, $f(x)\approx x$. 再结合 \[\begin{gathered}
    f\biggl(\frac14\biggr)= f(4)= \frac{17}4,\quad
        f\biggl(\frac13\biggr)= f(3)= \frac{10}3,\\
    f\biggl(\frac12\biggr)= f(2)= \frac{5}2,\quad 
        f(1)= 2,
\end{gathered}\]
可以描点作图如下 (第三象限的图象与第一象限的图象关于原点对称):
</p>

<img alt="对勾函数 f(x)= x+\dfrac1x 的图象" src="/figs/2020/2020-11/2020-1115-1100.svg"></img>

<p>由图可以看出 $f(x)= x+\dfrac1x$ 的单调递增区间为 $(-\infty,-1]$ 和 $[1,+\infty)$, 单调递减区间为 $(-1,0)$ 和 $(0,1)$. 利用单调性的定义可以验证这一点. 例如, 任取 $x_1$, $x_2\in [1,+\infty)$ 满足 $x_1< x_2$, 则 \[\begin{aligned}
    f(x_1)- f(x_2)
    &= \Bigl(x_1+\dfrac1x_1\Bigr)- \Bigl(x_2+\dfrac1x_2\Bigr)\\
    &= (x_1-x_2)- \frac{x_1-x_2}{x_1x_2}\\
    &= (x_1-x_2)\Bigl(1- \frac1{x_1x_2}\Bigr).
\end{aligned}\]
此时 $x_1-x_2< 0$, $x_1x_2>1$ 即 $1- \dfrac1{x_1x_2}> 0$, 所以 \[
    (x_1-x_2)\Bigl(1- \frac1{x_1x_2}\Bigr)< 0
    \Rightarrow f(x_1)- f(x_2)< 0,\]
即 $f(x_1)< f(x_2)$, 表明 $f(x)$ 在 $[1,+\infty)$ 上单调递增.
</p>
<p>根据其图象的特征, 函数 $f(x)= x+\dfrac1x$ ($x\neq 0$) 一般形象地称为“对勾”函数. 第一象限图的最低点 $(1,2)$ 可由<a href="/docs/prerequisite/inequality/mean-value-inequality/#均值不等式-2022-0917-1521">均值不等式</a>得到: 当 $x>0$ 时, \[
    x+\dfrac1x\geqslant 2\sqrt{x\cdot\dfrac1x}= 2,\]
等号成立当且仅当 $x= \dfrac1x$ 即 $x=1$. $f(x)$ 的图象是双曲线, 有两条渐近线: $y=x$ 和 $x=0$ (即 $y$ 轴). 观察 $f(x)$ 的图象可知, 若 $x\geqslant 3$, 则 $f(x)\geqslant f(3)$, 即此时 $f_{\min}=f(3)$. 类似地, 若 $x\geqslant \dfrac12$, 则 $f_{\min}=f(1)$. 
</p>
<p>一般地, $f(x)= x+\dfrac{k}x$ ($k>0$, $x\neq 0$) 均可称为“对勾”函数. 由与前面类似的分析可得, $f(x)$ 是奇函数, 有两条渐近线 $y=x$ 和 $x=0$, 第一象限图象的最低点为 $(\sqrt{k},2\sqrt{k})$, 单调递增区间为 $(-\infty,-\sqrt{k}]$ 和 $[\sqrt{k},+\infty)$, 单调递减区间为 $(-\sqrt{k},0)$ 和 $(0,\sqrt{k})$.
</p>

<myexample>
    <p>已知函数 $f(x)= \dfrac{2x+m}{x^2+1}$ 在定义域 $\mathbf{R}$ 上是奇函数.
    </p>
    <p>(1) 求实数 $m$ 的值;
    </p>
    <p>(2) 求 $f(x)$ 在 $[2,3]$ 上的最大值和最小值.
    </p>
</myexample>

<mysolution>
    <p>(1) 因为 $f(x)$ 是奇函数, 所以 $f(-x)= -f(x)$, 即 \[
        \dfrac{2\cdot(-x)+ m}{(-x)^2+1}= -\dfrac{2x+m}{x^2+1},\]
    整理可得, $m=0$.
    </p>
    <p>(2) 由 (1) 和 $x\in[2,3]$ 可知, \[
        f(x)= \frac{2x}{x^2+1}= \frac{2}{x+\dfrac1x}.\]
    因为函数$g(x)= x+\dfrac1x$ 在 $[2,3]$ 上单调递增, 所以 \[
        g(x)\in [g(2),g(3)]= \biggl[\dfrac52,\dfrac{10}3\biggr],\]
    从而 \[
        f(x)= \frac{2}{g(x)}\in \biggl[\dfrac35,\dfrac45\biggr].\]
    </p>
</mysolution>

<myexample>
    <p>已知函数 $f(x)=\dfrac{ax^2+b}x$, 且 $f(1)=2$, $f(2)=\dfrac52$.
    </p>
    <p>(1) 确定函数 $f(x)$ 的解析式, 并判断其奇偶性;
    </p>
    <p>(2) 用定义证明函数 $f(x)$ 在区间 $(1,+\infty)$ 上单调递增;
    </p>
    <p>(3) 解关于 $t$ 的不等式 $f(1+2t^2)- f(3+t^2)< 0$.
    </p>
</myexample>

<mysolution>
    <p>(1) 由题意, \[\left\{\!\!\begin{array}{l}
        a+b=2,\\
        \dfrac{4a+b}2= \dfrac52
    \end{array}\right.\Rightarrow
    \left\{\!\!\begin{array}{l}
        a=1,\\
        b=1,
    \end{array}\right.\]
    所以 $f(x)=\dfrac{x^2+1}x$. 因为 \[
        f(-x)= \frac{(-x)^2+1}{-x}
        = -\frac{x^2+1}x= -f(x),\]
    且 $f(x)$ 的定义域为 $(-\infty,0)\cup (0,+\infty)$, 关于原点对称, 所以 $f(x)$ 为奇函数.
    </p>
    <p>(2) 任取 $1< x_1< x_2$, 则 \[\begin{aligned}
        f(x_1)-f(x_2)
        &= \frac{x_1^2+1}{x_1}- \frac{x_2^2+1}{x_2}\\
        &= \frac{x_2(x_1^2+1)- x_1(x_2^2+1)}{x_1x_2}\\
        &= \frac{x_1^2 x_2- x_1 x_2^2+x_2- x_1}{x_1x_2}\\
        &= \frac{x_1 x_2(x_1- x_2)- (x_1- x_2)}{x_1x_2}\\
        &= (x_1- x_2)\frac{x_1 x_2- 1}{x_1x_2}.
    \end{aligned}\]
    由 $1< x_1< x_2$ 知, $x_1- x_2< 0$, $x_1 x_2> 1$ 即 $x_1 x_2- 1>0$,
    所以 $f(x_1)-f(x_2)< 0$, 说明函数 $f(x)$ 在区间 $(1,+\infty)$ 上单调递增.
    </p>
    <p>(3) 不等式化为 $f(1+2t^2)< f(3+t^2)$. 因为 $1+2t^2>1$, $3+t^2>1$, 由 (2) 知, 前述不等式等价于 \[
        1+2t^2< 3+t^2\Rightarrow
        t\in(-\infty,-\sqrt2)\cup(\sqrt2,+\infty).\]    
    </p>
</mysolution>
