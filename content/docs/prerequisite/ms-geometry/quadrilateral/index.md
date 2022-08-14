---
# bookCollapseSection: true
title: 四边形
weight: 3
prevPage: ../triangle
prevPageTitle: 三角形
nextPage: ../circle
nextPageTitle: 圆
---

# 四边形

四边形内角和为 $360^\circ$, 与外角和相等. 由两点之间线段最短可知, 四边形的三边之和大于第四边. 下面回顾平行四边形 (也包括矩形、菱形和正方形) 和梯形的性质.

## 平行四边形

平行四边形 $ABCD$ 是指其两组对边分别平行. 由平行线的性质可知, 平行四边形 $ABCD$ 的对角相等. 连接对角线 $AC$ 和 $BD$, 并设两者交于点 $O$, 利用全等可证

- $AB= CD$, $AD= BC$, 即两组对边分别相等
- $AO=OC$, $BO=OD$, 即对角线互相平分

![平行四边形的性质](/figs/2022/2022-08/2022-0811-2310.svg)

平行四边形是**中心对称**图形, 其对称中心为对角线的交点. 判定平行四边形的常用方法为

- 两组对边分别平行 (定义)
- 一组对边平行且相对
- 两组对边分别相等
- 对角线互相平分

<myexample>
    <p>对任意四边形 $ABCD$, 顺次连接四边中点 $E$, $F$, $G$, $H$, 求证: 四边形 $EFGH$ 为平行四边形.</p>
    <img alt="任意四边形内的平行四边形" src="/figs/2022/2022-08/2022-0812-0000.svg"></img>
</myexample>

<myproof>
    <p>连接 $AC$, 考虑 $\triangle ABC$ 和 $\triangle ADC$ 的中位线知, \[
        EF=\frac12 AC= HG,\quad EF\parallel AC\parallel HG,\]
    所以四边形 $EFGH$ 为平行四边形.</p>
    <img alt="任意四边形内的平行四边形-辅助线" src="/figs/2022/2022-08/2022-0812-0005.svg"></img>
</myproof>

<myremark>
    <p>(1) 遇到中点一般可考虑构造中位线, 此题也可通过连接 $BD$ 来证明.</p>
    <p>(2) 上图中连接 $EG$ 和 $FH$ 后可知, 两者为平行四边形 $EFGH$ 的角平分线, 所以互相平分. 这个结论可以推广, 例如, 分别取四边形 $ABCD$ 四边上的三等分点, 连接对边对应的分点后, 所得线段也被三等分 (仍可以用纯几何法证明), 如下图所示, $E$, $F$, $G$, $H$ 均为对应线段的三等分点. 这里的“三等分点”也可以改成“$n$ 等分点”, 相应的结论是“所得线段被 $n$ 等分” (用高中讲到的向量法或坐标法证明更方便).</p>
    <img alt="四边形的对边三等分点连线的三等分性" src="/figs/2022/2022-08/2022-0812-1940.svg"></img>
</myremark>

<myexercise>
    <p>上例中要使得四边形 $EFGH$ 为矩形, 则四边形 $ABCD$ 应满足什么条件? 四边形 $EFGH$ 为菱形时对应的条件是什么?</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>矩形 $EFGH$ 对应 $AC=BD$; 菱形 $EFGH$ 对应 $AC\parallel BD$, 见下方的判定条件.</p>
</details>

## 矩形、菱形和正方形

矩形 $ABCD$ 是有一个内角为 $90^\circ$ 的平行四边形, 也称其为长方形. 由平行线的性质可知, 矩形 $ABCD$ 的四个内角均为 $90^\circ$. 又由勾股定理可知, 对角线 $AC=BD$. 矩形是特殊的平行四边形, 故也为中心对称图形. 矩形还是轴对称图形, 对称轴为两组对边中点连线所在的直线. 

![矩形的性质](/figs/2022/2022-08/2022-0811-2320.svg)

要证明一个四边形为矩形, 一般先证明其为平行四边形, 然后证明如下两个结论之一:

- 一个内角为 $90^\circ$ (定义)
- 对角线相等

菱形 $ABCD$ 是有两条邻边相等的平行四边形, 因此其四边相等. 再由等腰三角形的性质可知, 对角线 $AC$ 和 $BD$ 互相垂直平分. 菱形也是中心对称图形和轴对称图形, 对称轴为两条对角线所在的直线. 

![菱形的性质](/figs/2022/2022-08/2022-0811-2340.svg)

要证明一个四边形为菱形, 一般先证明其为平行四边形, 然后证明如下两个结论之一:

- 有两条邻边相等 (定义)
- 对角线互相垂直

正方形 $ABCD$ 是有一个内角为 $90^\circ$ 且两条邻边相等 (因而既是矩形, 又是菱形) 的平行四边形. 由前述结论可知, 正方形 $ABCD$ 的两条对角线相等且互相垂直.

![正方形的性质](/figs/2022/2022-08/2022-0811-2330.svg)


<myexample>
    <p>如下图所示, 以 $\triangle ABC$ 的两边 $AB$, $AC$ 为边长, 向外作分别作正方形 $ABDE$ 和正方形 $ACFG$. 再过点 $A$ 作直线, 交 $BC$ 于点 $H$, 交 $EG$ 于点 $I$.</p>
    <p>(1) 若 $H$ 为 $BC$ 的中点, 求证: $AI\perp EG$;</p>
    <p>(2) 若 $AI\perp EG$, 求证: $H$ 为 $BC$ 的中点.</p>
    <img alt="三角形向外作两个正方形" src="/figs/2022/2022-08/2022-0812-0010.svg"></img>
</myexample>

<myproof>
    <p>(1) 倍长 $AH$ 至点 $J$, 连接 $BJ$, $CJ$. 因为 $BC$ 与 $AJ$ 互相平分, 所以四边形 $ABJC$ 为平行四边形. 结合已知的正方形可知, \[\begin{gathered}
        AB= AE,\quad BJ= AC= AG,\\
        \angle ABJ+\angle BAC= \angle EAG+\angle BAC= 180^\circ,
    \end{gathered}\]
    则 $\angle ABJ= \angle EAG$, 从而 $\triangle ABJ\cong \triangle EAG$. 因此 $\angle 1= \angle 2$, \[
        \angle 2+ \angle 3= \angle 1+ \angle 3= 90^\circ,\]
    表明 $AI\perp EG$.</p>
    <img alt="三角形向外作两个正方形-中点推垂直" src="/figs/2022/2022-08/2022-0812-1950.svg"></img>
    <p>(2) 过点 $B$ 作 $BK\perp AH$ 于 $K$, 过点 $C$ 作 $CL\perp AH$ 于 $L$. 由已知的正方形和 $AI\perp EG$ 可证 \[
        \triangle AEI\cong \triangle ABK,\quad
        \triangle AGI\cong \triangle ACL,\]
    所以 $BK=AI=CL$, 从而可证 \[
        \triangle BHK\cong \triangle CHL\Rightarrow BH=HC,\]
    即 $H$ 为 $BC$ 的中点.</p>
    <img alt="三角形向外作两个正方形-垂直推中点" src="/figs/2022/2022-08/2022-0812-2000.svg"></img>
</myproof>

<myremark>
    <p>上例和下面的练习, 用坐标法证明更方便.</p>
</myremark>

<myexercise id="三角形向外作两个正方形-中点连线为垂线">
    <p>如下图所示, 以 $\triangle ABC$ 的两边 $AB$, $AC$ 为边长, 向外作分别作正方形 $ABDE$ 和正方形 $ACFG$. 点 $H$ 为 $BC$ 中点, 点 $I$ 为 $DF$ 中点. 求证: \[
        HI\perp BC,\quad HI= \frac12 BC.\]</p>
    <img alt="三角形向外作两个正方形-中点连线为垂线" src="/figs/2022/2022-08/2022-0812-2030.svg"></img>
</myexercise>

<details><summary>参考答案</summary>
    <p>提示: 过点 $A$ 作 $AL\perp BC$ 于点 $L$, 过点 $D$ 作 $DM\perp BC$ 于点 $M$, 过点 $F$ 作 $FN\perp BC$ 于点 $N$, 可证 \[
        \triangle ABL\cong \triangle DBM,\quad
        \triangle ACL\cong \triangle FCN,\]
    则 $H$ 为 $MN$ 中点. 在梯形 $DMNF$ 中, $HI$ 为中位线, 从而可推出要证明的结论.</p>
</details>

## 梯形

梯形 $ABCD$ 是只有一组对边平行的四边形, 以下设 $AB\parallel DC$, 但 $AD$ 不与 $BC$ 平行. 此时 $AB\neq DC$ (否则 $ABCD$ 为平行四边形), 不妨设 $DC< AB$, 则称 $DC$ 为上底, $AB$ 为下底, 两者之间的距离称为梯形的高. 不平行的两边 $AD$ 与 $BC$ 均称为腰, 两腰中点的连线段 $EF$ 称为梯形 $ABCD$ 的中位线. 由三角形的全等或中位线性质可证明, \\[
    AD\parallel EF\parallel BC,\quad EF= \frac{AD+BC}2.\\]

![梯形的性质](/figs/2022/2022-08/2022-0811-2345.svg)

通过平移一腰, 可将梯形 $ABCD$ 分为三角形和平行四边形 (见下面的例题).

直角梯形 $ABCD$ 是含一个直角的梯形, 不妨设 $\angle A= 90^\circ$, 则 $\angle D= 90^\circ$. 过上底 $DC$ 的端点作高, 可将直角梯形分为矩形和直角三角形.

![直角梯形的辅助线](/figs/2022/2022-08/2022-0811-2350.svg)

等腰梯形 $ABCD$ 是不平行的两边相等的梯形, 即 $AD= BC$. 等腰梯形为轴对称图形, 对称轴为两底的中垂线 (两者重合). 过上底 $DC$ 的两个端点作双高, 可将等腰梯形分为矩形和两个全等的直角三角形.

![等腰梯形的辅助线](/figs/2022/2022-08/2022-0811-2355.svg)

<myexample>
    <p>如下图所示, 在梯形 $ABCD$ 中, $AB= 6$, $BC=5$, $CD=3$, $DA=4$, 求梯形 $ABCD$ 的面积.</p>
    <img alt="已知梯形的四边长, 求面积" src="/figs/2022/2022-08/2022-0812-2040.svg"></img>
</myexample>

<mysolution>
    <p>作 $CE\parallel DA$ 交 $AB$ 于点 $E$ (即平移一腰), 则四边形 $AECD$ 为平行四边形, 所以 \[
        AE=DC=3,\quad CE=DA=4.\]
    在 $\triangle BCE$ 中, $BE=AB-AE=3$, 所以 \[
        CE^2+EB^2= CB^2\Rightarrow \angle CE\perp EB,\]
    因此 $CE$ 为梯形 $ABCD$ 的高, 所求面积为 \[
        \frac12 (DC+AB) CE= \frac12 (3+6)\cdot 4= 18.\]</p>
    <img alt="已知梯形的四边长, 求面积-辅助线" src="/figs/2022/2022-08/2022-0812-2050.svg"></img>
</mysolution>

<myremark>
    <p>这里平移一腰后, 分出的三角形恰为直角三角形. 如果得到一般的三角形, 还需先确定梯形的高.</p>
</myremark>

<myexercise>
    <p>如下图所示, 在直角梯形 $ABCD$ 中, $AB= 6$, $BC=5$, $CD=3$, $\angle A= 90^\circ$, 求直角梯形 $ABCD$ 的面积.</p>
    <img alt="已知直角梯形的三边长, 求面积" src="/figs/2022/2022-08/2022-0812-2100.svg"></img>
</myexercise>

<details><summary>参考答案</summary>
    <p>提示: 过点 $C$ 作 $CE\perp AB$ 交 $AB$ 于点 $E$, 则得到一个直角三角形和一个矩形. 可以算出所求的面积为 $18$.</p>
</details>
