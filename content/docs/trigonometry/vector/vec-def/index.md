---
# bookCollapseSection: true
title: 向量的定义
weight: 1
bookHidden: true
prevPage: /docs/trigonometry/vector
prevPageTitle: 向量
nextPage: /docs/trigonometry/vector/vec-basic-theorem
nextPageTitle: 平面向量基本定理
---

# 向量的定义


<p>由向量的加法, $\overrightarrow{AB}+ \overrightarrow{BC}= \overrightarrow{AC}$, 移项得 $\overrightarrow{BC}= \overrightarrow{AC}- \overrightarrow{AB}$, 表明一个向量可以改写为新起点的两个向量之差, 且原向量终点在前, 起点在后, 不妨简称为“终点减去起点”. 类似地,
\[\overrightarrow{MN}= \overrightarrow{ON}- \overrightarrow{OM}
    = \overrightarrow{PN}- \overrightarrow{PM},\]
即新的起点可以任意指定.
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $\overrightarrow{BD}= \dfrac13\overrightarrow{BC}$, 用 $\overrightarrow{AB}$, $\overrightarrow{AC}$ 表示 $\overrightarrow{AD}$.
</p>
</myexample>
<mysolution>
    <p>把已知等式拆解为以 $A$ 为起点的向量表示,
    \[\overrightarrow{AD}- \overrightarrow{AB}
        = \dfrac13(\overrightarrow{AC}- \overrightarrow{AB}),\]
    解得 $\overrightarrow{AD}= \dfrac23\overrightarrow{AB}+ \dfrac13\overrightarrow{AC}$.
</p>
</mysolution>
</p>
<p>上题不画图也能顺利解出, 复杂的题还是建议画图帮助思考解题思路. 用上面的方法很容易得到, 若点 $C$ 为线段 $AB$ 的中点, 则
\[\overrightarrow{OC}
    = \dfrac12\overrightarrow{OA}+ \dfrac12\overrightarrow{OB}.\]
此结论可以类比中点坐标公式来记忆, 而且解题时可以直接使用.
</p>
<p><myexample>
<p>已知 $O$ 是 $\triangle ABC$ 所在平面内一点, $D$ 为 $BC$ 边的中点,
    且 $2\overrightarrow{OA}+ \overrightarrow{OB}+ \overrightarrow{OC}=\bm{0}$, 判断 $\overrightarrow{AO}$ 与 $\overrightarrow{OD}$ 的关系.
</p>
</myexample>
<mysolution>
    <p>因为 $\overrightarrow{OB}+ \overrightarrow{OC}= 2\overrightarrow{OD}$, 所以
    \[2\overrightarrow{OA}+ 2\overrightarrow{OD}= \bm{0}
    \quad\text{即}\quad \overrightarrow{AO}= \overrightarrow{OD}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知 $\triangle ABC$ 中, $D$ 为 $BC$ 的中点, $E$ 为 $AD$ 的中点, 用 $\overrightarrow{AB}$, $\overrightarrow{AC}$ 表示 $\overrightarrow{BE}$.
</p>
</myexample>
<mysolution>
    <p>不妨将所有向量都用以 $A$ 为起点的向量表示, 最终转化为 $\overrightarrow{AB}$ 和 $\overrightarrow{AC}$. 由题意作草图知, $\overrightarrow{AD}= \dfrac12\overrightarrow{AB}+ \dfrac12\overrightarrow{AC}$,
    \[\overrightarrow{AE}= \frac12\overrightarrow{AD}
        = \frac14\overrightarrow{AB}+ \frac14\overrightarrow{AC},\]
    所以
    \[\overrightarrow{BE}
        = \overrightarrow{AE}- \overrightarrow{AB}
        = -\frac34\overrightarrow{AB}+ \frac14\overrightarrow{AC}.\]
</p>
</mysolution>
</p>
<p>上题的解题思路将 $A$ 视为原点, 简化了解题过程. 在解题时, 应牢记最终是用 $\overrightarrow{AB}$, $\overrightarrow{AC}$ 表示所有向量.
</p>
<p><myexample>
<p>若四个点 $O$, $A$, $B$, $C$ 满足 $\overrightarrow{OC}= \dfrac23\overrightarrow{OA}+ \dfrac13\overrightarrow{OB}$, 且设 $|\overrightarrow{AB}|\neq 0$, 求 $|\overrightarrow{AC}|$ 与 $|\overrightarrow{AB}|$ 的倍数关系.
</p>
</myexample>
<mysolution>
    <p>视点 $O$ 为原点, 则由已知等式, 
    \[\begin{aligned}
        \overrightarrow{AC}
        &= \overrightarrow{OC}- \overrightarrow{OA}
         = -\dfrac13\overrightarrow{OA}+ \dfrac13\overrightarrow{OB}\\
        &= \frac13(\overrightarrow{OB}- \overrightarrow{OA})
         = \frac13\overrightarrow{AB},
    \end{aligned}\]
    表明 $3|\overrightarrow{AC}|= |\overrightarrow{AB}|$.
</p>
</mysolution>
</p>
<p><myexample>
<p>如图所示, 在梯形 $ABCD$ 中, $\overrightarrow{DC}= 2\overrightarrow{AB}$, 点 $P$ 在线段 $CD$ 上, 且 $DP= \dfrac12PC$, 点 $E$ 为 $BC$ 中点, 用 $\overrightarrow{AB}$ 和 $\overrightarrow{AD}$ 表示 $\overrightarrow{EP}$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0320-2040-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>视点 $A$ 为原点, 用 $\overrightarrow{AB}$ 和 $\overrightarrow{AD}$ 表示所有以 $A$ 为起点的向量. 由题意,
    \[\begin{aligned}
        \overrightarrow{AP}
        &= \overrightarrow{AD}+ \overrightarrow{DP}
         = \overrightarrow{AD}+ \frac23\overrightarrow{AB},\\
        \overrightarrow{AC}
        &= \overrightarrow{AD}+ \overrightarrow{DC}
         = \overrightarrow{AD}+ 2\overrightarrow{AB},\\
        \overrightarrow{AE}
        &= \frac12\overrightarrow{AC}+ \frac12\overrightarrow{AB}
         = \frac12\overrightarrow{AD}+ \frac32\overrightarrow{AB},\\
    \end{aligned}\]
    所以
    \[\overrightarrow{EP}
        = \overrightarrow{AP}- \overrightarrow{AE}
        = \frac12\overrightarrow{AD}- \frac56\overrightarrow{AB}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>已知 $\overrightarrow{AC}= \dfrac25\overrightarrow{AB}+ \mu\overrightarrow{BC}$, 求 $\mu$ 的值.
</p>
</myexample>
<mysolution>
    <p>方法一: 直接画图分析可知, $\mu= -\dfrac23$.
</p>
<p>方法二: 由已知, 
    \[\overrightarrow{AC}= \dfrac25\overrightarrow{AB}
        = \dfrac25(\overrightarrow{AC}+\overrightarrow{CB}),\]
    解得 $\overrightarrow{AC}= \dfrac23\overrightarrow{CB}= -\dfrac23\overrightarrow{BC}$, 即 $\mu= -\dfrac23$.
</p>
</mysolution>
</p>
<p>\subsection{共线向量的判别方法}
</p>
<p>因为数学中的向量只考虑自由向量, 所以两个向量平行等价于两者共线, 即非零向量 $\bm{a}$ 和 $\bm{b}$ 满足 $\bm{a}\parallel\bm{b}$ 的充要条件是存在 $k$ 使得 $\bm{a}=k\bm{b}$. 若向量 $\bm{i}$, $\bm{j}$ 不共线, 
并将非零向量 $\bm{a}$ 和 $\bm{b}$ 分别表示为 $x_1\bm{i}+y_1\bm{j}$
和 $x_2\bm{i}+y_2\bm{j}$, 则 
\[\bm{a}\parallel\bm{b}\Leftrightarrow 
    x_1\bm{i}+y_1\bm{j}= k(x_2\bm{i}+y_2\bm{j}),\ \text{即}\ 
    \left\{\!\!\begin{array}{l}
        x_1= kx_2,\\
        y_1= ky_2,
    \end{array}\right.\]
由此消去 $k$ 得, $d\frac{x_1}{x_2}= \dfrac{y_1}{y_2}$. 此结论一般简记为“对应系数成比例”, 并改写为 $x_1y_2=x_2y_1$, 即
\[x_1\bm{i}+y_1\bm{j} \parallel x_2\bm{i}+y_2\bm{j}
    \Leftrightarrow x_1y_2=x_2y_1.\]
</p>
<p>三点共线问题通常化为两个有公共点的向量的共线问题. 如点 $A$, $B$, $C$ 共线等价于 $\overrightarrow{AB}\parallel \overrightarrow{AC}$. 后者也可以替换为 $\overrightarrow{AB}\parallel \overrightarrow{BC}$ 或 $\overrightarrow{AC}\parallel \overrightarrow{BC}$ (视题中条件, 选择容易表示的式子).
</p>
<p><myexample>
<p>已知向量 $\bm{e}_1$, $\bm{e}_2$ 不共线, $\overrightarrow{AB}= \bm{e}_1+ k\bm{e}_2$, $\overrightarrow{CB}= \bm{e}_1+ 3\bm{e}_2$, $\overrightarrow{CD}= 2\bm{e}_1- \bm{e}_2$, 且 $A$, $B$, $D$ 三点共线, 求 $k$ 的值.
</p>
</myexample>
<mysolution>
    <p>$A$, $B$, $D$ 三点共线等价于向量 $\overrightarrow{AB}$ 和$\overrightarrow{BD}$ 共线. 由
    \[\overrightarrow{BD}= \overrightarrow{CD}- \overrightarrow{CB}
        = \bm{e}_1- 4\bm{e}_2\]
    知 $\dfrac{1}{1}= \dfrac{k}{-4}$, 即 $k=-4$.
</p>
</mysolution>
</p>
<p><myexample>
<p>已知向量 $\bm{a}$, $\bm{b}$ 不共线, $\overrightarrow{AB}= \bm{a}+ 3\bm{b}$, $\overrightarrow{BC}= 5\bm{a}+ 3\bm{b}$, $\overrightarrow{CD}= -3\bm{a}+ 3\bm{b}$, 分别判断下列各组点是否共线:
</p>
<p>(1) $A$, $B$, $C$;\quad (2) $A$, $B$, $D$;\quad
    (3) $A$, $C$, $D$;\quad (4) $B$, $C$, $D$.
</p>
</myexample>
<mysolution>
    <p>(1) 对点 $A$, $B$, $C$, 考虑 $\overrightarrow{AB}= \bm{a}+ 3\bm{b}$, $\overrightarrow{BC}= 5\bm{a}+ 3\bm{b}$. 显然 $\dfrac15\neq \dfrac33$, 即对应系数不成比例, 故点 $A$, $B$, $C$ 不共线.
</p>
<p>(2) $A$, $B$, $D$, 考虑 $\overrightarrow{AB}= \bm{a}+ 3\bm{b}$, $\overrightarrow{BD}= 2\bm{a}+ 6\bm{b}$. 显然 $\dfrac12= \dfrac36$, 即对应系数成比例, 故点 $A$, $B$, $D$ 共线.
</p>
<p>(3) $A$, $C$, $D$, 考虑 $\overrightarrow{AC}= 6\bm{a}+ 6\bm{b}$, $\overrightarrow{BC}= 5\bm{a}+ 3\bm{b}$. 显然 $\dfrac65\neq \dfrac63$, 即对应系数不成比例, 故点 $A$, $C$, $D$ 不共线.
</p>
<p>4) $B$, $C$, $D$, 考虑 $\overrightarrow{BC}= 5\bm{a}+ 3\bm{b}$, $\overrightarrow{CD}= -3\bm{a}+ 3\bm{b}$. 显然 $\dfrac5{-3}\neq \dfrac33$, 即对应系数不成比例, 故点 $B$, $C$, $D$ 不共线.
</p>
</mysolution>

<myexample>
<p>已知 $\overrightarrow{AB}= \bm{a}$, $\overrightarrow{AC}= \bm{b}$, $\overrightarrow{CD}= \bm{c}$, 用 $\bm{a}$, $\bm{b}$, $\bm{c}$ 表示 $\overrightarrow{BD}$.
</p>
</myexample>
<mysolution>
    <p>方法一: 直接拼凑可知,
    \[\overrightarrow{BD}
        = \overrightarrow{BA}+ \overrightarrow{AC}+ \overrightarrow{CD}
        = -\bm{a}+ \bm{b}+ \bm{c}.\]
</p>
<p>方法二: 将所有向量用以点 $A$ 为起点的向量表示,
    \[\overrightarrow{CD}= \overrightarrow{AD}- \overrightarrow{AC},\quad
    \overrightarrow{BD}= \overrightarrow{AD}- \overrightarrow{AB},\]
    作差知 
    \[\overrightarrow{BD}- \overrightarrow{CD}= \overrightarrow{AC}- \overrightarrow{AB},\]
    即 $\overrightarrow{BD}= -\bm{a}+ \bm{b}+ \bm{c}$.
</p>
</mysolution>
</p>
<p><myexample>
<p>在平行四边形 $ABCD$ 中, 设 $\overrightarrow{AB}= \bm{a}$, $\overrightarrow{AD}= \bm{b}$, $\overrightarrow{AC}= \bm{c}$, $\overrightarrow{BD}= \bm{d}$, 用 $\bm{a}$, $\bm{b}$ 表示 $\bm{c}$, $\bm{d}$.
</p>
</myexample>
<mysolution>
    <p>由平行四边形法则, 
    \[\overrightarrow{AC}= \overrightarrow{AB}+ \overrightarrow{AD}
        \quad\text{即}\quad \bm{c}= \bm{a}+\bm{b}.\]
    再由向量减法法则, 
    \[\overrightarrow{BD}= \overrightarrow{AD}- \overrightarrow{AB}
        \quad\text{即}\quad \bm{d}= \bm{b}+\bm{a}.\]
</p>
</mysolution>
</p>
<p><myexample>
<p>如图所示, 在等腰梯形 $ABCD$ 中, $CD= \frac12AB$, $BC=CD+DA$, $DE\perp AC$ 于点 $E$, 用 $\overrightarrow{AB}$, $\overrightarrow{AC}$ 表示 $\overrightarrow{DE}$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0418-2310-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>取 $AB$ 中点 $F$, 连结 $CF$, $DF$. 由题意, $AF$ 与 $DC$ 平行且相等, 表明四边形 $AFCD$ 为平行四边形, 即 $AC$ 和 $DF$ 互相平分. 再由 $AD=DC$ 和 $DE\perp AC$ 知, 点 $E$ 为 $AC$ 中点, 所以点 $E$ 在 $DF$ 上, 且 $\overrightarrow{DE}= \dfrac12\overrightarrow{DF}$.
</p>
<p>因为 $FB$ 与 $DC$ 平行且相等, 所以四边形 $FBCD$ 为平行四边形,
    \[\overrightarrow{DF}= \overrightarrow{BC}
        = \overrightarrow{AC}- \overrightarrow{AB},\]
    故 $\overrightarrow{DE}= \dfrac12(\overrightarrow{AC}- \overrightarrow{AB})$.
</p>
</mysolution>

<myexample>
<p>已知非零向量 $\bm{a}$, $\bm{b}$, $\bm{c}$, 判断下列命题的正误:
</p>
<p>(1) 若 $\bm{a}\cdot\bm{c}= \bm{b}\cdot\bm{c}$, 则 $\bm{a}=\bm{b}$;
</p>
<p>(2) 若 $|\bm{a}+ \bm{b}|= |\bm{a}|+ |\bm{b}|$, 则 $\bm{a}\parallel \bm{b}$;
</p>
<p>(3) 若 $|\bm{a}+\bm{b}|= |\bm{a}-\bm{b}|$, 则 $\bm{a}\perp\bm{b}$;
</p>
<p>(4) 若  $(\bm{a}+\bm{b})\cdot(\bm{a}-\bm{b})=0$, 则 $\bm{a}=\bm{b}$ 或 $\bm{a}= -\bm{b}$.
</p>
</myexample>
<mysolution>
    <p>(1) 向量内积运算与实数乘法运算不同, 没有消去律, 仅能推出 $(\bm{a}-\bm{b})\cdot\bm{c}= 0$, 即 $\bm{a}-\bm{b}\perp\bm{c}$. 原结论错误.
</p>
<p>(2) 原式两边平方, $(\bm{a}+ \bm{b})^2= (|\bm{a}|+ |\bm{b}|)^2$, 展开整理得 $\bm{a}\cdot\bm{b}= |\bm{a}|\,|\bm{b}|$. 设 $\bm{a}$ 与 $\bm{b}$ 的夹角为 $\theta$, 则由内积的定义, 
    \[\cos\theta= \frac{\bm{a}\cdot\bm{b}}{|\bm{a}|\,|\bm{b}|}= 1,\]
    所以 $\theta= 0$, 即 $\bm{a}$ 与 $\bm{b}$ 同向平行. 原结论正确.
</p>
<p>此小题的结论也可以从几何角度考虑. 由向量加法的定义, $\bm{a}$, $\bm{b}$ 和 $\bm{a}+\bm{b}$ 可以构成封闭的图形. 如果 $\bm{a}$ 与 $\bm{b}$ 不平行, 那它们比与 $\bm{a}+\bm{b}$ 构成三角形. 由于三角形中任意两边之和大于第三边, 所以 $|\bm{a}+ \bm{b}|< |\bm{a}|+ |\bm{b}|$, 与已知不符. 这说明 $\bm{a}\parallel \bm{b}$, 且作图易知, $\bm{a}$ 与 $\bm{b}$ 同向平行.
</p>
<p>(3) 原式两边平方后整理得 $\bm{a}\cdot\bm{b}= 0$, 即 $\bm{a}\perp\bm{b}$. 原结论正确.
</p>
<p>(4) 原式展开后整理得, $\bm{a}^2= \bm{b}^2$ 即 $|\bm{a}|^2= |\bm{b}|^2$, 所以 $|\bm{a}|= |\bm{b}|$. 原结论错误.
</p>
</mysolution>
</p>
<p><myremark>
    <p>向量内积运算与实数乘法运算虽然有不少类似之处, 但也有很多不同: (1) 中提到, 向量内积运算没有消去律; (4) 中表明, 内积结果无法开方为向量, 只能转化为实数运算. 此外, $|\bm{a}|^2= \bm{a}^2= \bm{a}\cdot\bm{a}$, 即将向量的模平方后化为内积式, 是解题时常用的转化方法. 
</p>
</myremark>

