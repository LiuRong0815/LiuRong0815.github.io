---
# bookCollapseSection: true
title: 均值不等式
weight: 3
bookHidden: true
prevPage: ../fraction-high-order-inequality
prevPageTitle: 分式不等式与高次不等式
nextPage: /
nextPageTitle: 高中数学资料
---

# 均值不等式


<p>对于任意 $x$, $y\in\realnum$, 恒有 $(x-y)^2\geqslant 0$, 展开后移项得
\[x^2+y^2\geqslant 2xy\quad\text{即}\quad \frac{x^2+y^2}2\geqslant xy.\]
不等式中等号成立的条件是 $x=y$, 也记为:“$=$”成立当且仅当 $x=y$. 把上面两个式子中的 $x$ 和 $y$ 分别换成 $\sqrt{x}$ 和 $\sqrt{y}$ (此时必须限制 $x$, $y\geqslant 0$), 可知
\[x+y\geqslant 2\sqrt{xy}\quad\text{即}\quad \frac{x+y}2\geqslant \sqrt{xy}.\]
因为 $\dfrac{x+y}2$ 与 $\sqrt{xy}$ 分别叫做非负实数 $x$ 与 $y$ 的\myindex{算术平均值}{算术平均值}与\myindex{几何平均值}{几何平均值}, 所以上面最后一个不等式也称为\myindex{均值不等式}{均值不等式}, 即
\[\text{均值不等式:}\ \frac{x+y}2\geqslant \sqrt{xy},\quad x,y\geqslant 0.\]
以上不等式均为常用不等式, 且都可以互相推出.
</p>
<p>利用均值不等式 (或其等价形式) 可以很方便地求特殊形式的式子的最大 (小) 值. 例如, 若 $x>0$, 则 
\[x+\dfrac1x\geqslant 2\sqrt{x\cdot\dfrac1x}=2,\]
“$=$”成立当且仅当 $x=\dfrac1x$ 即 $x=1$. 一般的, 可得如下结论 (均设 $x$, $y\geqslant 0$):
</p>
<p>(1) 若 $xy=L$ 为定值, 则 
\[x+y\geqslant 2\sqrt{xy}=2\sqrt{L},\] 所以 $x+y$ 的最小值为 $2\sqrt{L}$,“$=$”成立当且仅当 $x=y=\sqrt{L}$;
</p>
<p>(2) 若 $x+y=M$ 为定值, 则 
\[\sqrt{xy}\leqslant \frac{x+y}2=\frac{M}2\quad\text{即}\quad
  xy\leqslant \biggl(\frac{M}2\biggr)^2= \frac{M^2}4,\]
所以 $xy$ 的最大值为 $\dfrac{M^2}4$,“$=$”成立当且仅当 $x=y=\dfrac{M}2$.
</p>
<p><myexample>
<p>解答下列问题: 
  \begin{subproblem}
    \item 若 $x>0$, 求 $x+\dfrac4x$ 的取值范围;
    \item 若 $x$, $y\geqslant 0$, $xy=1$, 求 $x+2y$ 的取值范围;
    \item 若 $x$, $y\geqslant 0$, $2x+y=1$, 求 $xy$ 的取值范围.
  \end{subproblem}
</p>
</myexample>
<mysolution>
    <p>(1) 由均值不等式, 
  \[x+\dfrac4x\geqslant 2\sqrt{x\cdot\dfrac4x}=4,\]“$=$”成立当且仅当 $x=\dfrac4{x}$ 即 $x=2$, 所以 $x+\dfrac4x\in[4,+\infty)$.
</p>
<p>(2) 由均值不等式, 
  \[\frac{2x+y}2\geqslant \sqrt{2x\cdot y}\quad\text{即}\quad
    2x+y\geqslant 2\sqrt2,\]
 “$=$”成立当且仅当 $2x=y$, 结合 $xy=1$ 知 $x=\dfrac{\sqrt2}2$, $y=\sqrt2$. 所以 $xy\in[2\sqrt2,+\infty)$.
</p>
<p>(3) 由均值不等式, 
  \[\sqrt{2x\cdot y}\leqslant \frac{2x+y}2\quad\text{即}\quad
    xy\leqslant \frac18,\]
 “$=$”成立当且仅当 $2x=y$, 结合 $2x+y=1$ 知 $x=\dfrac14$, $y=\dfrac12$. 又因为 $x$, $y\geqslant 0$, 所以 $xy\geqslant 0$, 即 $xy\in\biggl[0,\dfrac14\biggr]$.
</p>
</mysolution>
</p>
<p>利用均值不等式求取值范围时, 一般把要求值的式子写在不等号前面, 等于固定值的式子写在不等号后面, 且有时需要适当的变形.
</p>
<p>在应用均值不等式时, 必须限制所考虑的式子 (均值不等式中的 $x$ 与 $y$) 为非负实数, 例如, 对任意的 $x\in\realnum$, 不能断言 $x+\dfrac1x\geqslant 2$ (当 $x\leqslant 0$ 时, 不等号显然不成立); 且应考虑等号成立的条件, 例如, 对任意的 $x\geqslant 2$, 不能由 $x+\dfrac1x\geqslant 2$ 断言 $x+\dfrac1x\in[2,+\infty)$, 因为此时“$=$”成立的条件“$x=1$”与已知条件 $x\geqslant 2$ 冲突 (实际上, 此时  $x+\dfrac1x\in \biggl[\dfrac52,+\infty\biggr)$, 具体解法以后会学到).
</p>
<p>有时, 要求取值范围的式子不能直接用均值不等式, 但可以通过变形化为能用均值不等式的形式. 
</p>
<p>\begin{example}\label{exa:201016-1940}
  解答下列问题: 
  \begin{subproblem}
    \item 若 $x>-1$, 求 $x+\dfrac1{x+1}$ 的取值范围;
    \item 若 $0< x< 4$, 求 $x(8-2x)$ 的取值范围;
    \item 若 $x< 0$, 求 $x+\dfrac1{x}$ 的取值范围.
  \end{subproblem}
</p>
</myexample>
<mysolution>
    <p>(1) 由均值不等式, 
  \[x+\dfrac1{x+1}= (x+1)+\dfrac1{x+1}-1
    \geqslant 2\sqrt{x\cdot\dfrac1{x+1}}-1=1,\]
 “$=$”成立当且仅当 $x+1=\dfrac1{x+1}$ 即 $x=0$, 所以 $x+\dfrac1{x+1}\in[1,+\infty)$.
</p>
<p>(2) 由均值不等式, 
  \[\sqrt{x(8-2x)}= \sqrt2\sqrt{x(4-x)}
    \leqslant \sqrt2\cdot\frac{x+(4-x)}2= 2\sqrt2,\]
  即 $x(8-2x)\leqslant 8$,“$=$”成立当且仅当 $x=4-x$ 即 $x=2$. 又由 $0< x< 4$ 和二次函数的性质可知, $x(8-2x)$ 的最小值在定义域端点处取到, 所以 $x(8-2x)\in(0,8]$. (此题也可以直接用二次函数的性质来解, 即考虑图象的开口方向、对称轴、定义域.)
</p>
<p>(3) 因为 $x< 0$, 所以先考虑 $(-x)+\biggl(-\dfrac1{x}\biggr)$. 由均值不等式, 
  \[(-x)+\biggl(-\dfrac1{x}\biggr)
    \geqslant 2\sqrt{(-x)\cdot\biggl(-\dfrac1{x}\biggr)}=2,\]
  即 $x+\dfrac1x\leqslant -2$,“$=$”成立当且仅当 $-x= -\dfrac1{x}$ 即 $x=-1$ (注意, 此时 $x< 0$), 所以 $x+\dfrac1{x}\in (-\infty,-2]$.
</p>
</mysolution>
</p>
<p>从解题过程可以看出, 此时解题的思路是通过适当改变常数项 (如例 \ref{exa:201016-1940} (1)) 或系数 (如例 \ref{exa:201016-1940} (2)(3)), 想办法{\bfseries 凑}出两个式子, 使它们的积 (如例 \ref{exa:201016-1940} (1)(3)) 或和 (如例 \ref{exa:201016-1940} (2)) 为定值.

<p>本次答疑主要讲解均值不等式及其应用, 2020 年 9 月 29 日答疑记录中已有该不等式的详细推导过程, 这里仅罗列相关结论:
\[\begin{aligned}
    \text{均值不等式:}\ &\frac{x+y}2\geqslant \sqrt{xy},\quad x,y\geqslant 0,\\
    \text{其等价形式:}\ &x+y\geqslant 2\sqrt{xy},\quad x,y\geqslant 0,\\
        &\frac{x^2+y^2}2\geqslant xy,\quad x,y\in\realnum.\\
        &x^2+y^2\geqslant 2xy,\quad x,y\in\realnum.
\end{aligned}\]
式中“$=$”成立当且仅当 $x=y$. 此外, 如下结论 (均设 $x$, $y\geqslant 0$):
</p>
<p>(1) 若 $xy=L$ 为定值, 则 $x+y$ 的最小值为 $2\sqrt{L}$,“$=$”成立当且仅当 $x=y=\sqrt{L}$;
</p>
<p>(2) 若 $x+y=M$ 为定值, 则 $xy$ 的最大值为 $\dfrac{M^2}4$,“$=$”成立当且仅当 $x=y=\dfrac{M}2$.
</p>
<p>用均值不等式解题时, 应想办法凑出两个式子, 使它们的积或和为定值, 如对 $x>-1$, 
\[x+\dfrac1{1+x}=(1+x)+\dfrac1{1+x}-1\geqslant 2\sqrt1-1=1.\]
除了应注意式中字母的范围 (是非负还是任意实数), 还应检验等号成立的条件, 如对 $x>2$, 虽然由均值不等式知 $x+\dfrac1x\geqslant 2$, 但等号成立当且仅当 $x=\dfrac1x$ 即 $x=1$, 与 $x>2$ 不符, 所以只能写 $x+\dfrac1x>2$.
</p>
<p><myexample>
<p>若 $a$, $b\in\realnum$ 且 $ab>0$, 则下列不等式恒成立的是 (\qquad).
    \begin{twocolpro}
    A. $a^2+b^2>2ab$ & B. $a+b\geqslant 2\sqrt{ab}$\\
    C. $\dfrac1a+\dfrac1b> \dfrac2{\sqrt{ab}}$
    & D. $\dfrac{b}a+\dfrac{a}b\geqslant 2$
    \end{twocolpro}
</p>
</myexample>
<mysolution>
    <p>若只对这四个选项简单地套用均值不等式, 可能会错误地认为全都正确. 但如果仔细检查不等式成立的前提, 可发现其中有三个选项是错的.
</p>
<p>对 A, 当 $a=b$ 时, $a^2+b^2=2ab$, 所以 A 不正确.
</p>
<p>对 B, 只有 $a$, $b\geqslant 0$ 时, 原不等式才正确, 而题中的 $ab>0$ 可能有 $a$, $b< 0$, 无法用均值不等式.
</p>
<p>对 C, 当 $a=b>0$ 时, $\dfrac1a+\dfrac1b= \dfrac2{\sqrt{ab}}$, 所以 C 不正确. 此外, 题中的 $ab>0$ 可能有 $a$, $b< 0$, 无法用均值不等式.
</p>
<p>对 D, 由 $ab>0$ 知 $\dfrac{b}a$, $\dfrac{a}b>0$, 所以可用均值不等式得出结论.
</p>
</mysolution>
</p>
<p><myexample>
<p>条件“$x>0$”是“$x^2+\dfrac1{x^2}\geqslant 2$”的什么条件?
</p>
</myexample>
<mysolution>
    <p>因为 $x^2$ 恒非负, 所以只要 $x^2\neq0$, 就有 $x^2>0$, 此时 $x^2+\dfrac1{x^2}\geqslant 2$. 这表明 $x^2+\dfrac1{x^2}\geqslant 2$ 的充要条件是 $x\neq 0$. 再与 $x>0$ 对比可知,“$x>0$”是“$x^2+\dfrac1{x^2}\geqslant 2$”的充分不必要条件.
</p>
</mysolution>
</p>
<p><myexample>
<p>若函数 $f(x)= x+\dfrac1{x-2}$ ($x>2$) 在 $x=a$ 处取最小值, 求 $a$ 的值.
</p>
</myexample>
<mysolution>
    <p>由 $x>2$ 知 $x-2>0$, 所以
    \[x+\dfrac1{x-2}= (x-2)+\dfrac1{x-2}+2\geqslant 2\sqrt1+2=4,\]
    等号成立当且仅当 $x-2=\dfrac1{x-2}$ 即 $x=3$ (注意 $x>2$). 故所求的 $a=3$.
</p>
</mysolution>
</p>
<p><myexample>
<p>若 $x$, $y\in\realnum^+$ 且 $\dfrac{x}3+\dfrac{y}4=1$, 求 $xy$ 的最大值.
</p>
</myexample>
<mysolution>
    <p>由均值不等式, 
    \[\frac{x}3+\frac{y}4\geqslant 2\sqrt{\frac{xy}{12}},
    \quad\text{即}\quad 1\geqslant 2\sqrt{\frac{xy}{12}},\]
    解得 $xy\leqslant 3$, 所以 $xy$ 的最大值为 $3$.
</p>
</mysolution>

<p>\begin{example}\label{exa:201115-1040}
    求函数 $f(t)= \dfrac{t^2-4t+1}t$ ($t>0$) 的最小值和对应的 $t$ 的值.
</p>
</myexample>
<mysolution>
    <p>因为 $t>0$, 所以由均值不等式, 
    \[f(t)= \frac{t^2-4t+1}t= t+\frac1t-4
        \geqslant 2\sqrt{t\cdot\frac1t}-4= -2,\]
   “$=$”成立当且仅当 $t=\dfrac1t$ 即 $t=1$. 以上表明 $f_{\min}=-2$, 且对应的 $t=1$.
</p>
</mysolution>
<myremark>
    <p>(1) 求值域的一般方法是讨论单调性, 但对特殊的分式函数, 则一般先考虑用均值不等式. 例 \ref{exa:201115-1040} 中还可以推导如下:
    \[f(t)= \frac{t^2-4t+1}t= \frac{t^2+1-4t}t
        \geqslant \frac{2\sqrt{t^2\cdot1}-4t}t= -2.\]
</p>
<p>(2) 用均值不等式时, 必须考虑等号成立的条件. 如果例 \ref{exa:201115-1040} 中 $t\geqslant 3$, 那么等号就不能成立, 只能写 $f(t)>-2$, 即不能得到 $f_{\min}=-2$ 的结论. 此时的解法参可借用例 \ref{exa:201115-1045} 中的单调性结论.
</p>
</myremark>
