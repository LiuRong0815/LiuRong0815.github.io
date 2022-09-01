---
# bookCollapseSection: true
title: 排列
weight: 1
bookHidden: true
prevPage: /docs/probability-statistics/permutation-combination
prevPageTitle: 排列与组合
nextPage: /docs/probability-statistics/permutation-combination/combination
nextPageTitle: 组合
---

# 排列


<p>在计数时, 有两个常用的计数原理 (均可以结合树状图来理解). 加法原理用于分类计数 (即分类讨论, 类似于电路图中的并联), 乘法原理用于分步计数 (类似于电路图中的串联). 实际计数时, 需要结合题意确定计数顺序, 有时还会利用集合中的补集运算, 详见下面的例子.
</p>
<p><myexample>
<p>$3$ 个学生从 $4$ 本不同的参考书中各挑选 $1$ 本, 求不同的选法数.
</p>
</myexample>
<mysolution>
    <p>由乘法原理, 选法数为 $4\times 3\times 2= 24$.
</p>
</mysolution>
</p>
<p><myexample>
<p>由数字 $1$, $2$, $3$ 组成的无重复数字的整数, 求其中偶数的个数.
</p>
</myexample>
<mysolution>
    <p>偶数的特点是末位为偶数, 故先考虑末位. 由于题中没有指定整数的位数, 所以需分位数讨论 (加法原理):
</p>
<p>(1) 若组成一位数, 则只有 $2$;
</p>
<p>(2) 若组成两位数, 则有 $12$, $32$;
</p>
<p>(3) 若组成三位数, 则有 $132$, $123$,
</p>
<p>综上所述, 偶数共 $5$ 个.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 若上题中的数字改为 $1$, $2$, $\cdots$, $6$, 则需按位数分 $6$ 种情况计算. 每种情况都是先考虑末位 (共 $3$ 种可能), 再计算其他位. 结果可用排列数表示为 \[
        3+ 3\mathrm{A}_5^1+ 3\mathrm{A}_5^2+ \cdots+ 3\mathrm{A}_5^5.\]
</p>
<p>(2) 若上题中的数字改为 $0$, $1$, $2$, $\cdots$, $6$, 则应特别注意位数大于 $1$ 时, 首位不能为 $0$. 可以先考虑 $0$ 是否为末位, 再视情况限制 $0$ 不为首位; 也可以先不管首位的限制, 再减去两位数及以上首位为 $0$ 的数的个数 (这里用到补集运算). 前一种方法的结果可用排列数表示为 \[
        4+ (\mathrm{A}_6^1+ 3\cdot 5)
        + (\mathrm{A}_6^2+ 3\cdot 5\mathrm{A}_5^1)+\cdots
        + (\mathrm{A}_6^6+ 3\cdot 5\mathrm{A}_5^5),\]
    后一种方法的结果可用排列数表示为 \[\begin{aligned}
        &4+ 4\mathrm{A}_6^1+ 4\mathrm{A}_6^2+ \cdots+ 4\mathrm{A}_6^6\\
        &- (3+ 3\mathrm{A}_5^1+ 3\mathrm{A}_5^2+ \cdots+ 3\mathrm{A}_5^5).
    \end{aligned}\]
    两种计算方法的结果数值一样 (用两种方法计数也是检验排列组合题的一种方法).
</p>
</myremark>
</p>
<p><myexample>
<p>甲、乙、丙三人踢毽子, 互相传递, 每人每次传给另外的人. 由甲开始踢, 经过 $4$ 次传递后, 毽子又被传回甲, 求不同的传递方式共有多少种.
</p>
</myexample>
<mysolution>
    <p>因为第 $4$ 次传回甲, 所以只需考虑中间 $3$ 次传递的对象. 此时, 相邻两次为不同的人, 则第 $1$ 次和第 $3$ 次均不能传给甲, 故这两次只能在乙和丙中选. 列树形图可知,
</p>
<p>(1) 若第 $1$ 次和第 $3$ 次均传给乙, 则第 $2$ 次可传给甲和丙;
</p>
<p>(2) 若第 $1$ 次和第 $3$ 次均传给丙, 则第 $2$ 次可传给甲和乙;
</p>
<p>(3) 若第 $1$ 次传给乙且第 $3$ 次传给丙, 则第 $2$ 次只能传给甲;
</p>
<p>(4) 若第 $1$ 次传给丙且第 $3$ 次传给乙, 则第 $2$ 次也只能传给甲,
</p>
<p>综上所述, 共有 $2+2+1+1= 6$ 种传递方式 (考试解题时, 分类讨论的过程可以只列树形图, 无需文字描述).
</p>
</mysolution>
</p>
<p><myexample>
<p>用数字 $1$, $2$ 组成一个四位数, 则 $1$, $2$ 都出现的四位偶数有多少个?
</p>
</myexample>
<mysolution>
    <p>偶数的末位必为偶数 (这里是 $2$), 故只需考虑前三位, 且这三位不能只有 $2$. 先不限制 $1$, $2$ 都出现, 再去掉只有 $2$ 的情况, 所以所求个数为 $2^3-1= 7$.
</p>
</mysolution>
</p>
<p>\subsection{排列数}
</p>
<p>排列数 $\mathrm{A}_9^3$ 是指从 $9$ 个不同的元素中挑选 $3$ 个, 并将这 $3$ 个元素从左到右排序的方法数. 由乘法原理, \[
    \mathrm{A}_9^3= 9\times 8\times 7.\]
同理可得, \[
    \mathrm{A}_9^9= 9\times 8\times 7\times \cdots\times 2\times 1.\]
上式右端常记为 $9!$, 叫做“$9$ 的阶乘”. 例如, \[\begin{aligned}
    5!&= 5\times 4\times\cdots\times 1= 120,\\
    7!&= 7\times 6\times\cdots\times 1= 5040.
\end{aligned}\]
借用阶乘的记号, \[
    \mathrm{A}_9^3= \frac{9\times 8\times 7\times \cdots\times 1}{7\times 6\times \cdots\times 1}
    = \frac{9!}{7!}.\]
</p>
<p>一般地, 排列数 $\mathrm{A}_n^m$ ($m\leqslant n$ 且 $m$ 为非负整数, $n$ 为正整数) 是指从 $n$ 个不同的元素中挑选 $m$ 个, 并将这 $m$ 个元素从左到右排序的方法数. 类似于前面的分析, \[\begin{aligned}
    \mathrm{A}_n^m
    &= n(n-1)(n-2) \cdots [n-(m-1)]\\
    &= n(n-1)(n-2) \cdots (n-m+1)\\
    &= \frac{n!}{(n-m)!}.
\end{aligned}\]
注意, 上式第一行的等号右边共 $n-m$ 个因子, 而第一个因子为 $n=n-0$, 所以最后的因式为 $[n-(m-1)]= (n-m+1)$. 特别地, 规定 $\mathrm{A}_n^0= 1$, $0!=1$. 在实际计算时, 可以根据需要选择合适的公式来计算排列数. 一般来说, 直接展开是为了计算最后的得数, 改写为用阶乘表示是为了化简式子.
</p>
<p>逆用上面的公式, 也可以将连乘式用阶乘表式, 进而改为排列数, 例如, \[\begin{aligned}
    &4\times 5\times 6\times \cdots\times (n-1)\times n\\
    ={}& \frac{1\times 2\times 3\times \cdots\times (n-1)\times n}{1\times 2\times 3}\\
    ={}& \frac{n!}{3!}= \mathrm{A}_n^3.
\end{aligned}\]
</p>
<p><myexample>
<p>计算 $\mathrm{A}_{12}^3- \mathrm{A}_{10}^3$.
</p>
</myexample>
<mysolution>
    <p>按定义, \[
        \mathrm{A}_{12}^3- \mathrm{A}_{10}^3
        = 12\times 11\times 10- 10\times 9\times 8
        = 600.\]
    (计算上式时, 建议先提公因数 $12\times 10$.)
</p>
</mysolution>
</p>
<p><myexample>
<p>对正整数 $n$, 解排列数方程 $\mathrm{A}_{n+1}^2- \mathrm{A}_{n}^2= 10$.
</p>
</myexample>
<mysolution>
    <p>按定义变形, \[
        (n+1)n- n(n-1)=10\Rightarrow n=5.\]
    (计算上式时, 建议先提公因式 $n$.)
</p>
</mysolution>
</p>
<p><myexample>
<p>若整数 $a< 27$, 将 $(27-a)(28-a)\cdots(34-a)$ 改写成排列数.
</p>
</myexample>
<mysolution>
    <p>原式为连续 $8$ 个正整数相乘, 且最大的正整数为 $34-a$, 所以可以改写为 $\mathrm{A}_{34-a}^8$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>计算连乘整数的个数时, 可以按等差数列考虑, 也可以在式子前面补充从 $1$ 开始的式子, 从而得到未补充前式子的个数. 如上题中, 用后一方法可以补充 $1-a$, $2-a$, $\cdots$, $26-a$ 共 $26$ 个因式, 连同已知的式子共 $34$ 个因式, 所以原式为 $34-26= 8$ 个因式相乘.
</p>
</myremark>
</p>
<p><myexample>
<p>判断下列各式与排列数 $\mathrm{A}_{n}^m$ 是否相等:
</p>
<p>(1) $\dfrac{n!}{(n-m)!}$;\quad
    (2) $n(n-1)(n-2)\cdots (n-m)$;
</p>
<p>(3) $\dfrac{n\mathrm{A}_{n-1}^m}{n-m+1}$;\quad
    (4) $\mathrm{A}_{n}^1 \mathrm{A}_{n-1}^{m-1}$.
</p>
</myexample>
<mysolution>
    <p>(1) 相等, 这是排列数的计算方法之一.
</p>
<p>(2) 不相等, 这里共 $m+1$ 个因式, 而 $\mathrm{A}_{n}^m$ 展开时共 $m$ 个因式.
</p>
<p>(3) 不相等, 因为 \[\begin{aligned}
        \frac{n\mathrm{A}_{n-1}^m}{n-m+1}
        &= \frac{n}{n-m+1}\cdot \frac{(n-1)!}{(n-1-m)!}\\
        &= \frac{n-m}{n-m+1}\cdot \frac{n!}{(n-m)!}\\
        &= \frac{n-m}{n-m+1}\cdot \mathrm{A}_{n}^m.
    \end{aligned}\]
</p>
<p>(4) 相等, 直接按组合数的计算公式展开, \[\begin{aligned}
        \mathrm{A}_{n}^1 \mathrm{A}_{n-1}^{m-1}
        &= n\cdot \frac{(n-1)!}{[(n-1)-(m-1)!]}\\
        &= \frac{n!}{(n-m)!}
         = \mathrm{A}_{n}^m.
    \end{aligned}\]
</p>
</mysolution>

<myexample>
<p>有 $5$ 名同学被安排在周一至周五值日, 每人负责一天. 已知甲同学只能在周一值日, 那么他们值日顺序的编排方案共有多少种?
</p>
</myexample>
<mysolution>
    <p>题意相当于剩下的 $4$ 名同学分担周二至周五, 故排列数为 $\mathrm{A}_4^4= 24$.
</p>
</mysolution>
</p>
<p><myexample>
<p>某班级从 A,B,C,D,E,F 共 $6$ 名学生中选四人参加 $4\times 100\,\mathrm{m}$ 接力比赛, 其中第一棒只能在 A,B 中选一人, 第四棒只能在 A,C 中选一人, 则不同的选派方法共有多少种?
</p>
</myexample>
<mysolution>
    <p>重点关注题中对第一棒和第四棒的限制.
</p>
<p>(1) 若第一棒选 A, 则第四棒只能选 C, 剩下两棒任意选取, 排列数为 $\mathrm{A}_4^2$.
</p>
<p>(2) 若第一棒选 B, 则第四棒可能选 A,C. 无论选哪一名, 剩下两棒可以任意选取, 排列数均为 $\mathrm{A}_4^2$.
</p>
<p>综上所述, 所求排列数为 $3\mathrm{A}_4^2= 36$.
</p>
</mysolution>
</p>
<p><myexample>
<p>从 $1,3,5,7,9$ 这五个数中, 每次取出两个不同的数, 并分别记为 $a,b$, 则 $\lg a- \lg b$ 的不同取值有多少个?
</p>
</myexample>
<mysolution>
    <p>若不考虑是否重复, 则 $\lg a- \lg b$ 的取值有 $\mathrm{A}_5^2$ 个. 因为 $\lg a- \lg b= \lg \dfrac{a}b$, 所以重复的是能约分的 $\dfrac{a}b$. 观察可知, \[
        \frac13= \frac39,\quad \frac31= \frac93\]
    是仅有的两组能约分的 $\dfrac{a}b$. 因此所求 $\lg a- \lg b$ 的不同取值有 $\mathrm{A}_5^2- 2= 18$ 个.
</p>
</mysolution>
</p>
<p><myremark>
    <p>若将题干改为“从 $1,2,4,5$ 这四个数中取数”, 其余不变, 则答案为 $\mathrm{A}_4^2-2= 10$ 个.
</p>
</myremark>
</p>
<p><myexample>
<p>A, B, C, D 四名同学排成一排照相, 要求自左向右, A 不排第一, B 不排第四, 共有多少种不同的排列方法?
</p>
</myexample>
<mysolution>
    <p>方法一: 参照下图, 先不考虑限制, 可得全集 $U$, 排列数为 $\mathrm{A}_4^4$. 再分别排除“A 排第一”和“B 排第四”的情形, 对应集合 $M$ 和 $N$, 排列数均为 $\mathrm{A}_3^3$. 但是因为集合 $S= M\cap N$ 对应的“A 排第一且B 排第四”均包含在 $M$ 和 $N$ 内, 所以只能排除一次, 其排列数为 $\mathrm{A}_2^2$. 综上所述, 所求排列数为 \[
        \mathrm{A}_4^4- 2\mathrm{A}_3^3+ \mathrm{A}_2^2= 14.\]
    <center>
        \includegraphics[scale=1.5]{2022-0410-1145-crop}
    </center>
</p>
<p>方法二: 由题意, 只能 B,C,D 中某一位排第一. 
</p>
<p>(1) 若 B 排第一, 则后三位可以任意排, 排列数为 $\mathrm{A}_3^3$.
</p>
<p>(2) 若 C 排第一, 则还需注意 B 不能排第四, 即只能排第二或第三. 无论哪种情形, 剩下两位都可以任意排. 所以按乘法原理, 排列数为 $2\mathrm{A}_2^2$.
</p>
<p>(3) 若 D 排第一, 结论同 (2).
</p>
<p>综上所述, 所求排列数为 \[
        \mathrm{A}_3^3+ 2\mathrm{A}_2^2= 14.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>解排列数不等式 $\mathrm{A}_{n-1}^2- n< 7$.
</p>
</myexample>
<mysolution>
    <p>由排列数的定义, 不等式化为 \[\left\{\!\!\begin{array}{l}
        \dfrac{n(n-1)}2- n< 7,\\
        n-1\geqslant 2,
    \end{array}\right.\Rightarrow 
    3\leqslant n< 5.\]
    后一不等式是为了确保排列数有意义. 因为 $n$ 为正整数, 所以 $n=3,4$.
</p>
</mysolution>

