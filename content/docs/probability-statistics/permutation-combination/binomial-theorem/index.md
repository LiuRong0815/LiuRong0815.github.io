---
# bookCollapseSection: true
title: 二项式定理
weight: 3
bookHidden: true
prevPage: /docs/probability-statistics/permutation-combination/combination
prevPageTitle: 组合
nextPage: /docs/probability-statistics/statistics
nextPageTitle: 统计
---

# 二项式定理


<p>$(x+y)^n$ 表示二项式 $x+y$ 的 $n$ 次方. 先观察当 $n$ 较小时, 展开式的结构特点. 当 $n=2$ 时, \[\begin{aligned}
    (x+y)^2&= (x+y)(x+y)= x(x+y)+ y(x+y)\\
    &= (x^2+xy)+ (yx+y^2)= x^2+ 2xy+y^2,
\end{aligned}\]
这就是完全平方公式. 展开时主要利用分配律将前一个括号中的 $x,y$ 分别与后一个括号中的 $x,y$ 相乘, 所得 $4$ 个因式合并同类项后共 $3$ 项.
</p>
<p>再来看当 $n=3$ 时的情形. 此时, 逐次用分配律再合并, \[\begin{aligned}
    (x+y)^3&= (x+y)(x+y)(x+y)\\
    &= x(x+y)(x+y)+ y(x+y)(x+y)\\
    &= [x^2(x+y)+ xy(x+y)]+ [yx(x+y)+ y^2(x+y)]\\
    &= \cdots\\
    &= x^3+ 3x^2y+ 3xy^2+ y^3.
\end{aligned}\]
可以看出, 展开后得到 $8$ 个因式, 合并同类项后共 $4$ 项. 仔细观察上述过程, 可以看出每个因式都是从 $(x+y)(x+y)(x+y)$ 的各括号中分别选取 $x$ 或 $y$ 再相乘得到的, 从而可得如下规律:
</p>
<p>(1) 每个因式均为 $3$ 次式, 且按 $x$ 的降幂排列为 \[
    x^3,\quad x^2y,\quad xy^2,\quad y^3,\]
共 $4$ 项;
</p>
<p>(2) 要得到 $x^3$, 相当于从每个括号中均取 $x$ 相乘, 即从 $3$ 个 $x$ 中取 $3$ 个 $x$, 共 $\mathrm{C}_3^3$ 种取法, 所以 $x^3$ 的系数为 $\mathrm{C}_3^3= 1$;
</p>
<p>(3) 要得到 $x^2y$, 相当于从两个括号中取 $x$ 且从剩下的一个括号中取 $y$ 相乘, 即从 $3$ 个 $x$ 中取 $2$ 个 $x$, 共 $\mathrm{C}_3^2$ 种取法, 所以 $x^2y$ 的系数为 $\mathrm{C}_3^2= 3$;
</p>
<p>(4) 类似地, $xy^2$ 的系数为 $\mathrm{C}_3^1= 3$, $y^3$ 的系数为 $\mathrm{C}_3^0= 1$.
</p>
<p>由以上规律, $(x+y)^3$ 的展开式又可以写成 \[
    \mathrm{C}_3^3 x^3+ \mathrm{C}_3^2 x^2y
    + \mathrm{C}_3^1 xy^2+ \mathrm{C}_3^0 y^3.\]
如果从取 $y$ 的个数来考虑, 上述展开式还可以写成 \[
    \mathrm{C}_3^0 x^3+ \mathrm{C}_3^1 x^2y+ 
    \mathrm{C}_3^2 xy^2+ \mathrm{C}_3^3 y^3.\]
同样的道理, 当 $n= 4$ 时, \[\begin{aligned}
    (x+y)^4&= \mathrm{C}_4^4 x^4+ \mathrm{C}_4^3 x^3y
    + \mathrm{C}_4^2 x^2y^2+ \mathrm{C}_4^1 xy^3
    + \mathrm{C}_4^0 y^4\\
    &= \mathrm{C}_4^0 x^4+ \mathrm{C}_4^1 x^3y
    + \mathrm{C}_4^2 x^2y^2+ \mathrm{C}_4^3 xy^3
    + \mathrm{C}_4^4 y^4\\
    &= x^4+ 4x^3y+ 6x^2y^2+ 4xy^3+ y^4.
\end{aligned}\]
</p>
<p>对一般的正整数 $n$, 将 $(x+y)^n$ 展开就得到二项式定理 \[
    (x+y)^n= \mathrm{C}_n^0 x^n+ \mathrm{C}_n^1 x^{n-1}y
    + \mathrm{C}_n^2 x^{n-2}y^2+\cdots 
    + \mathrm{C}_n^{n-1} xy^{n-1}+ \mathrm{C}_n^n y^n.\]
这里只按取 $y$ 的个数来列式 (与人教 A 版教材一致), 实际应用时, 也可以按取 $x$ 的个数来列式. 上式等号右边共 $n+1$ 项, 通常把第 $k$ 项记为 $T_k$, 则可以得到通项 (实为第 $k+1$ 项) 公式 \[
    T_{k+1}= \mathrm{C}_n^k x^{n-k}y^k,\quad k= 0,1,\cdots,n.\]
注意, 因为 $y$ 的次方从 $0$ 开始, 所以比项数少 $1$, 如 $y^2$ 对应第 $3$ 项, 而 $y^6$ 对应第 $7$ 项.
</p>
<p>从前面的推导过程, 还可以得到组合数的一个性质: 若正整数 $m,n$ 满足 $m\leqslant n$, 则 \[
    \mathrm{C}_n^m= \mathrm{C}_n^{n-m}.\]
上式表明, 从 $n$ 个互异元素中取 $m$ 个元素的取法数与取 $n-m$ 个元素的取法数相等, 即取 $m$ 个元素就对应了取 $n-m$ 个元素. 例如, \[
    \mathrm{C}_{10}^3= \mathrm{C}_{10}^7,\quad
    \mathrm{C}_{100}^{36}= \mathrm{C}_{100}^{64}.\]
</p>
<p>\subsection{二项式定理的简单应用}
</p>
<p><myexample>
<p>若二项式 $(x+a)^{10}$ 的展开式中, $x^7$ 的系数为 $15$, 求 $a$ 的值.
</p>
</myexample>
<mysolution>
    <p>先写通项公式, \[
        T_{k+1}= \mathrm{C}_{10}^k x^{10-k}a^k
        = \mathrm{C}_{10}^k a^k x^{10-k}.\]
    因为 $x^7$ 对应的 $k$ 满足 $10-k=7$, 即 $k=3$, 此时, $x^7$ 的系数为 $\mathrm{C}_{10}^3 a^3$, 于是 \[
        \mathrm{C}_{10}^3 a^3= 15,\quad a=\frac12.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>若二项式 $(1+2x)^n$ 的展开式中, $x^3$ 的系数等于 $x^2$ 的系数的 $4$ 倍, 求 $n$ 的值.
</p>
</myexample>
<mysolution>
    <p>对照二项式定理, 将此处的 $1$ 看成公式中的 $x$, $2x$ 看成公式中的 $y$, 写出通项公式并整理, \[
        T_{k+1}= \mathrm{C}_n^k 1^{n-k}(2x)^k
        = \mathrm{C}_n^k 2^k x^k,\]
    所以 $x^2$ 的系数为 $\mathrm{C}_n^2 2^2= 4\mathrm{C}_n^2$, $x^3$ 的系数为 $\mathrm{C}_n^3 2^3= 8\mathrm{C}_n^3$. 由题意, \[
        8\mathrm{C}_n^3= 4\cdot 4\mathrm{C}_n^2,\quad n=8.\]
    解上述组合数方程时, 应先按组合数公式 \[
        \mathrm{C}_n^m= \frac{n(n-1)\cdots(n-m+1)}
            {1\cdot2\cdot\,\cdots\,\cdot m}\]
    将等号两边的式子展开, 再约去非零乘积因子后求解.
</p>
</mysolution>
</p>
<p><myexample>
<p>求 $(x-\sqrt2 y)^{10}$ 的展开式中 $x^6y^4$ 的系数.
</p>
</myexample>
<mysolution>
    <p>二项式定理中式子为和式, 所以这里将 $(x-\sqrt2 y)^{10}$ 改写为 $[x+(-\sqrt2 y)]^{10}$ 再写通项公式, \[
        T_{k+1}= \mathrm{C}_{10}^k x^{10-k}(-\sqrt2 y)^k
        = \mathrm{C}_{10}^k(-\sqrt2)^k x^{10-k} y^k.\]
    因为 $x^6y^4$ 对应 $k=4$, 所以所求系数为 $\mathrm{C}_{10}^4(-\sqrt2)^4= 840$.
</p>
</mysolution>
</p>
<p><myexample>
<p>求 $\biggl(\sqrt{x}- \dfrac2x\biggr)^6$ 的展开式中的常数项.
</p>
</myexample>
<mysolution>
    <p>通项公式为 \[
        T_{k+1}= \mathrm{C}_6^k (\sqrt{x})^{6-k} \biggl(-\dfrac2x\biggr)^k
        = \mathrm{C}_6^k(-2)^k x^{\frac{6-k}2-k}.\]
    常数项对应 $x^0$, 所以按指数列方程 \[
        \frac{6-k}2-k= 0,\quad k= 2.\]
    $x^0$ 的系数 $\mathrm{C}_6^2 (-2)^2= 60$ 即为所求常数项.
</p>
</mysolution>
</p>
<p><myexample>
<p>在 $(1-x)^5- (1-x)^6$ 的展开式中, 求含 $x^3$ 的项的系数.
</p>
</myexample>
<mysolution>
    <p>$(1-x)^5$ 中含 $x^3$ 的项为 \[
        \mathrm{C}_5^3 1^{5-3}(-x)^3
        = - \mathrm{C}_5^3 x^3,\]
    $(1-x)^6$ 中含 $x^3$ 的项为 \[
        \mathrm{C}_6^3 1^{6-3}(-x)^3
        = - \mathrm{C}_6^3 x^3,\]
    所以原式展开后, 含 $x^3$ 的项的系数为 \[
        - \mathrm{C}_5^3- (-\mathrm{C}_6^3)= 10.\]
</p>
</mysolution>
</p>
<p>\subsection{系数与二项式系数}
</p>
<p>将关于 $x$ 的式子 $(x+a)^n$ 按二项式定理展开, 通项 (第 $k+1$ 项) 为 \[
    T_{k+1}= \mathrm{C}_n^k x^{n-k} a^k
    = \mathrm{C}_n^k a^k x^{n-k}.\]
式中 $\mathrm{C}_n^k$ 称为第 $k+1$ 项的二项式系数, 而 $\mathrm{C}_n^k a^k$ 称为第 $k+1$ 项的系数, 即二项式系数仅为组合数. 例如, 将 $(x+2)^7$ 展开后, 含 $x^4$ 的项为 \[
    \mathrm{C}_7^3 x^4\cdot 2^3= 8 \mathrm{C}_7^3 x^4,\]
所以这一项的二项式系数为 $\mathrm{C}_7^3$, 系数为 $8\mathrm{C}_7^3$.
</p>
<p><myexample>
<p>已知 $\biggl(\sqrt{x}- \dfrac2x\biggr)^n$ 的展开式中第 $3$ 项的系数比第 $2$ 项的系数大 $162$, 求 $n$ 的值和展开式中含 $x^3$ 的项, 并指出该项的二项式系数.
</p>
</myexample>
<mysolution>
    <p>展开式的第 $k+1$ 项为 \[
        T_{k+1}= \mathrm{C}_n^k (\sqrt{x})^{n-k} \biggl(-\frac2x\biggr)^k
        = (-2)^k \mathrm{C}_n^k x^{\frac{n-k}2-k},\]
    由题中系数关系,\[
        (-2)^2 \mathrm{C}_n^3= (-2)^1 \mathrm{C}_n^2+ 162,\]
    解得 $n= 9$. 所以 \[
        T_{k+1}= (-2)^k \mathrm{C}_9^k x^{\frac{9-k}2-k}
        = (-2)^k \mathrm{C}_9^k x^{\frac{9-3k}2},\]
    含 $x^3$ 的项对应 \[
        \frac{9-3k}2= 3,\quad k=1,\]
    即为第 $2$ 项 \[
        T_2= (-2)^1 \mathrm{C}_9^1 x^3
        = -18 x^3,\]
    该项的二项式系数为 $\mathrm{C}_9^1= 9$.
</p>
</mysolution>
</p>
<p>关于 $x$ 的式子 $(x+a)^n$ 展开为 \[
    \mathrm{C}_n^0 x^n+ \mathrm{C}_n^1 a\cdot x^{n-1}+\cdots
    +\mathrm{C}_n^{n-1} a^{n-1}\cdot x+ \mathrm{C}_n^n a^n,\]
记其二次项系数之和为 $P$, 系数之和为 $Q$, 则 \[\begin{gathered}
    P= \mathrm{C}_n^0+ \mathrm{C}_n^1+\cdots
    +\mathrm{C}_n^{n-1}+ \mathrm{C}_n^n,\\
    Q= \mathrm{C}_n^0 a^0+ \mathrm{C}_n^1 a^1+\cdots
    +\mathrm{C}_n^{n-1} a^{n-1}+ \mathrm{C}_n^n a^n.
\end{gathered}\]
对比展开式可知, 这两个式子均可以由 $(x+a)^n$ 得到: 令 $x=a=1$, 则 \[
    P= (1+1)^n= 2^n;\]
令 $x=1$, 则 \[
    Q= (1+a)^n,\]
即得到组合数的性质 \[\begin{gathered}
    \mathrm{C}_n^0+ \mathrm{C}_n^1+\cdots
    +\mathrm{C}_n^{n-1}+ \mathrm{C}_n^n= 2^n,\\
    \mathrm{C}_n^0 a^0+ \mathrm{C}_n^1 a^1+\cdots
    +\mathrm{C}_n^{n-1} a^{n-1}+ \mathrm{C}_n^n a^n= (1+a)^n.
\end{gathered}\]
例如, \[\begin{gathered}
    \mathrm{C}_8^0+ \mathrm{C}_8^1+\cdots
    +\mathrm{C}_8^7+ \mathrm{C}_8^8= 2^8,\\
    \mathrm{C}_8^0+ 3\mathrm{C}_8^1+\cdots
    +3^7\mathrm{C}_8^7+ 3^8\mathrm{C}_8^8= 4^8.
\end{gathered}\]
</p>
<p><myexample>
<p>若 $(x+3y)^n$ 的展开式中各项系数之和等于 $(7a+b)^{10}$ 的展开式中各二次项系数之和, 求 $n$ 的值.
</p>
</myexample>
<mysolution>
    <p>回想二项式定理可知, 要得到 $(x+3y)^n$ 的展开式中各项系数之和, 只需令 $x=y=1$, 即各项系数之和为 $4^n$; 要得到 $(7a+b)^{10}$ 的展开式中各二项式系数之和, 只需令 $7a=b=1$, 即各二项式系数之和为 $2^{10}$. 由题意, \[
        4^n= 2^{10},\quad n=5.\]
</p>
</mysolution>


\subsection{二项式系数的性质}
</p>
<p>将关于 $x$ 的式子 $(x+a)^n$ 按二项式定理展开, \[
    (x+a)^n= \mathrm{C}_n^0 x^n+ a\mathrm{C}_n^1 x^{n-1}
    + a^2\mathrm{C}_n^2 x^{n-2}+\cdots 
    + a^{n-1}\mathrm{C}_n^{n-1} x+ \mathrm{C}_n^n a^n.\]
在第 $k+1$ 项 $a^k \mathrm{C}_n^k x^{n-k}$ 中, 组合数 $\mathrm{C}_n^k$ 称为其二项式系数, 而 $a^k \mathrm{C}_n^k$ 称为其系数. 当 $a=1$ 时, 两者相等.
</p>
<p>令 $x=a=1$, 则可得 \[
    \mathrm{C}_n^0+ \mathrm{C}_n^1+\cdots
    +\mathrm{C}_n^{n-1}+ \mathrm{C}_n^n= 2^n.\]
现在考虑求其中奇数项的和与偶数项的和. 举一个具体的例子, 设 \[\begin{gathered}
    A= \mathrm{C}_{10}^0+ \mathrm{C}_{10}^2+\cdots
    +\mathrm{C}_{10}^{10},\\
    B= \mathrm{C}_{10}^1+ \mathrm{C}_{10}^3+\cdots
    +\mathrm{C}_{10}^9,
\end{gathered}\]
则 \[\begin{gathered}
    A+B = \mathrm{C}_{10}^0+ \mathrm{C}_{10}^1+\cdots
    +\mathrm{C}_{10}^{10}= 2^{10},\\
    A-B = \mathrm{C}_{10}^0- \mathrm{C}_{10}^1+\cdots
    -\mathrm{C}_{10}^9+ \mathrm{C}_{10}^{10}= 0,
\end{gathered}\]
后一式由前述展开式中令 $x=1$, $a=-1$ 得到. 进而可以解得 \[
    A= B= \frac{2^{10}}2= 2^9.\]
一般地, \[\begin{aligned}
    2^{n-1}&= \mathrm{C}_n^0+ \mathrm{C}_n^2+\mathrm{C}_n^4+\cdots\\
    &= \mathrm{C}_n^1+ \mathrm{C}_n^3+\mathrm{C}_n^5+\cdots.
\end{aligned}\]
前面的代入数值法也可以用于化简与二项式展开类似的式子.
</p>
<p>由组合数的定义, 若正整数 $m,n$ 满足 $m\leqslant n$, 则 \[
    \mathrm{C}_n^m= \mathrm{C}_n^{n-m},\]
即从 $n$ 个互异元素中取 $m$ 个元素对应了取 $n-m$ 个元素. 这是二项式系数的对称性. 再来看二项式系数的单调性. 先考虑一个具体的例子. 将 $\mathrm{C}_9^m$ 看成关于 $m$ 的函数 $f(m)$, 则由组合数和阶乘的计算公式, \[\begin{aligned}
    &f(m+1)- f(m)= \mathrm{C}_9^{m+1}- \mathrm{C}_9^m\\
    ={}& \frac{9!}{(m+1)![9-(m+1)]!}- \frac{9!}{m!(9-m)!}\\
    ={}& \frac{9!}{(m+1)!(9-m)!} [(9-m)- (m+1)]\\
    ={}& \frac{9!}{(m+1)!(9-m)!} (8- 2m).
\end{aligned}\]
由此可以看出, 当且仅当 $8-2m>0$ 即 $m< 4$ (或 $m\leqslant 3$) 时, $f(m+1)> f(m)$. 此时 $f(m)$ 单调递增, 也即 \[\begin{gathered}
    \mathrm{C}_9^0< \mathrm{C}_9^1< \mathrm{C}_9^2
    < \mathrm{C}_9^3< \mathrm{C}_9^4= \mathrm{C}_9^5,\\
    \mathrm{C}_9^5> \mathrm{C}_9^6> \mathrm{C}_9^7
    > \mathrm{C}_9^8> \mathrm{C}_9^9.
\end{gathered}\]
换句话说, 随 $m$ 的增加, $f(m)= \mathrm{C}_9^m$ 的值先增后减, 且在中间取最大值 (这里 $\mathrm{C}_9^4$ 和 $\mathrm{C}_9^5$ 都是最大值). 这一点从二项式系数的对称性也能部分体现. 同样地, 对组合数 $\mathrm{C}_{100}^m$, 最大的是 $\mathrm{C}_{100}^{50}$ (仅一个); 对组合数 $\mathrm{C}_{101}^m$, 最大的是 $\mathrm{C}_{101}^{50}$ 和 $\mathrm{C}_{101}^{51}$ (两者相等).
</p>
<p>\subsection{二项式系数的性质的简单应用}
</p>
<p><myexample>
<p>在 $(1+x)^n$ 的展开式中, 若只有 $x^5$ 的系数最大, 求 $n$ 的值.
</p>
</myexample>
<mysolution>
    <p>这里的系数就是二项式系数. 因为仅有 $x^5$ 的系数最大, 而它前面还有 $x^0$, $x^1$, $\cdots$, $x^4$ 共 $5$ 项 (均忽略系数), 所以后面也应该有 $5$ 项, 共 $11$ 项. 因此 $n+1 = 11$ ($n$ 次式展开共 $n+1$ 项), 即 $n=10$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>若上题改为“若 $x^5$ 的系数最大”, 则需要利用对称性分类讨论:
</p>
<p>(1) 当仅有 $x^5$ 的系数最大时, $n=10$.
</p>
<p>(2) 当 $x^4, x^5$ 的系数同时最大时, 前面有 $x^0, x^1, \cdots, x^3$ 共 $4$ 项, 所以后面也有 $4$ 项, 共 $10$ 项. 这时 $n+1 = 10$, 即 $n=9$.
</p>
<p>(3) 当 $x^5, x^6$ 的系数同时最大时, 同样的分析可以知道, $n=11$.
</p>
</myremark>
</p>
<p><myexample>
<p>若实数 $a= 2-\sqrt2$, 求值: \[
        a^{10}- 2\mathrm{C}_{10}^1 a^9
        + 2^2\mathrm{C}_{10}^2 a^8-\cdots + 2^{10}.\]
</p>
</myexample>
<mysolution>
    <p>将上式与 $(a+x)^{10}$ 的展开式对比可知, 只要令 $x=-2$, 两者就相等, 所以上式化为 \[
        (a-2)^{10}= (2-\sqrt2-2)^{10}= 2^5= 32.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知 $(1+2\sqrt{x})^n$ 的展开式中, 某一项的系数恰好是它前一项的系数的 $2$ 倍, 且是它后一项的系数的 $\dfrac56$, 求展开式中二项式系数最大的项.
</p>
</myexample>
<mysolution>
    <p>展开式的通项 (第 $k+1$ 项) 为 \[
        T_{k+1}= \mathrm{C}_n^k 1^{n-k} (2\sqrt{x})^k
        = 2^k \mathrm{C}_n^k x^{\frac{k}2}.\]
    设题中的某一项为第 $k+1$ 项, 则按题中系数的关系, \[\left\{\!\!\begin{array}{l}
        2^k \mathrm{C}_n^k= 2\cdot 2^{k-1} \mathrm{C}_n^{k-1},\\
        2^k \mathrm{C}_n^k= \frac56 2^{k+1} \mathrm{C}_n^{k+1}.
    \end{array}\right.\]
    对于前一式, 先约分得 $\mathrm{C}_n^k= \mathrm{C}_n^{k-1}$, 再利用组合数和阶乘的计算公式, \[\begin{gathered}
        \frac{n!}{k!(n-k)!}= \frac{n!}{(k-1)![n-(k-1)]!},\\
        k!(n-k)!= (k-1)!(n-k+1)!,\\
        k= n-k+1.
    \end{gathered}\]
    用同样的方法化简后一式, 可得 \[
        3(k+1)= 5(n-k),\]
    与前式联立解得, $n=7$. 因此二项式系数 $\mathrm{C}_7^3$ 和 $\mathrm{C}_7^4$ 最大, 对应的项分别为 \[
        2^3 \mathrm{C}_7^3 x^{\frac32}= 280 x^{\frac32},\quad
        2^4 \mathrm{C}_7^4 x^{\frac42}= 560 x^2.\]
</p>
</mysolution>

<myexample>
<p>若 $\biggl(ax^2 +\dfrac{b}x\biggr)^6$ 的展开式中, $x^3$ 的系数为 $20$, 求 $a^2+ b^2$ 的最小值.
</p>
</myexample>
<mysolution>
    <p>题中二项式展开后的第 $k+1$ 项为 \[
        T_{k+1}
        = \mathrm{C}_6^{6-k} (ax^2)^{6-k} \biggl(\dfrac{b}x\biggr)^k
        = \mathrm{C}_6^{6-k} a^{6-k} b^k x^{2(6-k)-k}.\]
    对 $x^3$, \[
        2(6-k)-k=3\Rightarrow k=3,\]
    所以其系数为 \[
        \mathrm{C}_6^{6-k} a^{6-k} b^k
        = \mathrm{C}_6^3 a^3 b^3= 20,\]
    解得 $ab= 1$. 再由基本不等式, \[
        a^2+ b^2\geqslant 2ab=2,\]
    等号成立当且仅当 $a=b=1$, 即 $a^2+ b^2$ 的最小值为 $2$.
</p>
</mysolution>

<myexample>
<p>设 $(2x-1)^4= a_0+a_1x+a_2x^2 +a_3x^3+a_4x^4$, 求值:
</p>
<p>(1) $a_0+a_1+a_2+a_3+ a_4$;\quad
    (2) $a_1+a_2+a_3+ a_4$;\quad
    (3) $a_0+a_2+ a_4$, $a_1+a_3$.
</p>
</myexample>
<mysolution>
    <p>观察可知, \[
        a_0+a_1+a_2+a_3+ a_4= f(1)= 1,\quad a_0= f(0)=1,\]
    所以 \[
        a_1+a_2+a_3+ a_4= f(1)-f(0)= 0.\]
    再设 $a_0+a_2+ a_4=A$, $a_1+a_3=B$, 则 \[
        A+B= f(1)=1,\quad A-B= f(-1)= 81,\]
    所以 \[
        A= \frac12[f(1)+f(-1)]= 41,\quad
        B= \frac12[f(1)-f(-1)]= -40.\]
</p>
</mysolution>

