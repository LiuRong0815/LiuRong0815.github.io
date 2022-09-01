---
# bookCollapseSection: true
title: 组合
weight: 2
bookHidden: true
prevPage: /docs/probability-statistics/permutation-combination/permutation
prevPageTitle: 排列
nextPage: /docs/probability-statistics/permutation-combination/binomial-theorem
nextPageTitle: 二项式定理
---

# 组合

<p>组合数 $\mathrm{C}_n^m$ 表示从 $n$ 个互异元素中取 $m$ 个元素的方法数, 其中正整数 $m$, $n$ 满足 $m\leqslant n$. 由定义, $\mathrm{C}_n^m= \mathrm{C}_n^{n-m}$, 即“取 $m$ 个元素”对应于“取 $n-m$ 个元素”, 这是组合数的对称性. 再由定义, $\mathrm{C}_n^n=1$, 并规定 $\mathrm{C}_0^0=\mathrm{C}_n^0= 1$, 此时 $\mathrm{C}_n^0= \mathrm{C}_n^n$, 仍有对称性.
</p>
<p>组合数的计算公式可由乘法原理得到. 从 $n$ 个互异元素中取 $m$ 个元素, 再从左至右排成一行, 对应的排列数为 $\mathrm{A}_n^m$, 而 $m$ 个元素排成一行的排列数为 $m!$, 所以 \[
    \mathrm{C}_n^m\cdot m!= \mathrm{A}_n^m\Rightarrow
    \mathrm{C}_n^m= \frac{\mathrm{A}_n^m}{m!}= \frac{n!}{m!(n-m)!}.\]
上式也可以改写为 \[
    \mathrm{C}_n^m= \frac{n(n-1)\cdots(n-m+1)}{1\cdot 2\cdot\,\cdots\,\cdot m}.\]
实际计算时, 常用后一公式, 而前一式主要用来简化中间计算过程.
</p>
<p>“2022 年 4 月 10 日答疑记录”中给出了组合数 $\mathrm{C}_n^m$ 关于 $m$ 的单调性: 对固定的 $n$, 随 $m$ 的增加, 函数 $f(m)= \mathrm{C}_n^m$ 的值先增后减, 且在中间取最大值. 例如, 对于 $\mathrm{C}_9^m$, 最大值为 $\mathrm{C}_9^4$ 和 $\mathrm{C}_9^5$ (两者相等); 对于 $\mathrm{C}_{90}^m$, 最大值为 $\mathrm{C}_{90}^{45}$.
</p>
<p>将组合数排成数阵, 可以得到“杨辉三角”: \[\begin{array}{ccccccccccccc}
        &&&&&&\mathrm{C}_0^0&&&&&&\\
        &&&&&\mathrm{C}_1^0&&\mathrm{C}_1^1&&&&&\\
        &&&&\mathrm{C}_2^0&&\mathrm{C}_2^1&&\mathrm{C}_2^2&&&&\\
        &&&\mathrm{C}_3^0&&\mathrm{C}_3^1&&\mathrm{C}_3^2&&\mathrm{C}_3^3&&&\\
        &&\mathrm{C}_4^0&&\mathrm{C}_4^1&&\mathrm{C}_4^2&&\mathrm{C}_4^3&&\mathrm{C}_4^4&&\\
        &\mathrm{C}_5^0&&\mathrm{C}_5^1&&\mathrm{C}_5^2&&\mathrm{C}_5^3&&\mathrm{C}_5^4&&\mathrm{C}_5^5&\\
        \mathrm{C}_6^0&&\mathrm{C}_6^1&&\mathrm{C}_6^2&&\mathrm{C}_6^3&&\mathrm{C}_6^4&&\mathrm{C}_6^5&&\mathrm{C}_6^6\\
        &&&&&&\cdots&&&&&&
    \end{array}\]
或 \[\begin{array}{ccccccccccccc}
        &&&&&&1&&&&&&\\
        &&&&&1&&1&&&&&\\
        &&&&1&&2&&1&&&&\\
        &&&1&&3&&3&&1&&&\\
        &&1&&4&&6&&4&&1&&\\
        &1&&5&&10&&10&&5&&1&\\
        1&&6&&15&&20&&15&&6&&1\\
        &&&&&&\cdots&&&&&&
    \end{array}\]
数阵从上到下依次为第 $0$ 行, 第 $1$ 行, 等等, 每行组合数均为对应的二项式系数. 第 $n$ 行组合数的下标为行数 $n$, 上标从 $0$ 递增到 $n$. 每个组合数与其右上角相邻的组合数, 上角相同. 此外, 每个组合数等于其上方相邻两个组合数之和, 写成公式为 \[
    \mathrm{C}_{n+1}^m= \mathrm{C}_{n}^{m-1}+ \mathrm{C}_{n}^m,\]
有时也写成\[
    \mathrm{C}_{n+1}^{m+1}= \mathrm{C}_{n}^{m}+ \mathrm{C}_{n}^{m+1}.\]
这个公式可以由组合数的计算公式来验证.
</p>

<myexample>
<p>学校要邀请 $9$ 位学生家长中的 $6$ 人参加一个座谈会, 其中甲、乙两位家长不能同时参加, 求参会的不同方法数.
</p>
</myexample>
<mysolution>
    <p>方法一: 将甲、乙分为一组，剩下 $7$ 人分为一组, 分情况考虑: 甲、乙选其一, 从第二组 $7$ 人里再选 $5$ 人; 甲、乙, 均不参会, 直接在第二组 $7$ 人里选 $6$ 人. 因此所求方法数为 \[
        \mathrm{C}_2^1\mathrm{C}_7^5+ \mathrm{C}_7^6
        = 2\mathrm{C}_7^2+ \mathrm{C}_7^1
        = 42+ 7= 49.\]
</p>
<p>方法二: 先不考虑限制, 从 $9$ 人中选 $6$ 人, 再从中减去甲、乙同时参加的方法数, 所求方法数为 \[
        \mathrm{C}_9^6- \mathrm{C}_7^4
        = \mathrm{C}_9^3- \mathrm{C}_7^3
        = 84- 35= 49.\]
</p>
</mysolution>

