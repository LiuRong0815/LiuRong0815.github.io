---
# bookCollapseSection: true
title: 圆
weight: 4
prevPage: ../quadrilateral
prevPageTitle: 四边形
nextPage: ../area
nextPageTitle: 平面图形的面积
---

# 圆

圆具有轴对称性和中心对称性, 对称轴是任意过圆心的直线, 对称中心是圆心.

## 圆的定义

在平面上取定一点 $C$, 设动点 $P$ 满足 $CP= r$ ($r>0$), 将所有这样的点 $P$ 描绘出来, 就得到半径为 $r$ 的圆 $C$, 点 $C$ 称为圆心. 定义表明, 圆是到定点 (圆心) 的距离等于定长 (半径) 的所有点的全体. 连接圆心 $C$ 和圆上任一点得到圆的半径, 过 $C$ 的直线被圆所截得的线段为圆的直径 (如下图中的线段 $AB$), 长度通常记为 $d$, 即 $d= 2r$.

![圆的定义](/figs/2022/2022-08/2022-0812-2300.svg)

圆的周长 $C$ 与直径 $d$ 成正比, 比值为圆周率 $\pi$., 所以圆 $C$ 的周长为 $\pi d= 2\pi r$. 利用半径将圆 $C$ 切割为一些小扇形, 就可以将圆近似看成多个“三角形”之和, 从而说明圆的面积为 \\[
    \dfrac12 \cdot 2\pi r\cdot r= \pi r^2.\\]

再取平面上另一点 $Q$, 则点 $Q$ 与圆 $C$ 的位置关系有三种:

- $CQ_1< r\Leftrightarrow$ 点 $Q_1$ 在圆 $C$ 内
- $CQ_2= r\Leftrightarrow$ 点 $Q_2$ 在圆 $C$ 上
- $CQ_3> r\Leftrightarrow$ 点 $Q_3$ 在圆 $C$ 外

![点与圆的位置关系](/figs/2022/2022-08/2022-0812-2310.svg)

## 圆的性质

同弧所对的圆心角是圆周角的两倍, 也即同弧所对的圆周角是圆心角的一半, 所以同弧所对的圆周角为定值. 下图中, $\angle 1= \angle 2= \dfrac12 \angle 3$. 特别地, 直径所对的圆心角为平角 ($180^\circ$), 故其所对的圆周角为直角 ($90^\circ$).

![同弧所对圆周角是圆心角的一半](/figs/2022/2022-08/2022-0812-2320.svg)

垂径定理: 设圆 $C$ 上有一弦 $AB$, 若取其中点 $M$ 并连接 $CM$, 则 $CM\perp AB$; 若作 $CM\perp AB$ 于 $M$, 则 $M$ 为 $AB$ 的中点, 即 \\[
    AM= BM\Leftrightarrow CM\perp AB.\\]

![垂径定理](/figs/2022/2022-08/2022-0812-2330.svg)

<myremark>
    <p>垂径定理本质上是等腰三角形的性质.</p>
</myremark>

<myexample>
    <p>如下图所示, 线段 $AB$ 为圆 $O$ 的弦, $C$ 为 $AB$ 的中点, $OD$ 为过点 $C$ 的半径. 若 $AB=8$, $CD=2$, 求圆 $O$ 的半径.</p>
    <img alt="垂径定理与二次方程-1" src="/figs/2022/2022-08/2022-0813-0910.svg"></img>
</myexample>

<mysolution>
    <p>连接 $OA$, 由垂径定理可知, $\triangle OCA$ 为直角三角形, 且 $OC\perp CA$. 设所求半径为 $r$, 则 \[\begin{gathered}
        OA=r,\quad AC= \frac12 AB=4,\\
        OC= OD-CD= r-2,
    \end{gathered}\]
    代入 $OA^2= OC^2+CA^2$, 可知 \[
        r^2= (r-2)^2+4^2,\quad r=5.\]</p>
    <img alt="垂径定理与二次方程-1-辅助线" src="/figs/2022/2022-08/2022-0813-0920.svg"></img>
</mysolution>

<myexercise>
    <p>如下图所示, 线段 $AB$ 为圆 $O$ 的弦, 半径 $OD=5$ 且垂直于 $AB$. 若 $AD=2\sqrt5$, 求 $CD$ 的长度.</p>
    <img alt="垂径定理与二次方程-2" src="/figs/2022/2022-08/2022-0813-1000.svg"></img>
</myexercise>

<details><summary>参考答案</summary>
    <p>提示: 仍连接 $OA$ 并用垂径定理. 在 $\mathrm{Rt}\triangle ACO$ 和 $\mathrm{Rt}\triangle ACD$ 中利用勾股定理列关于 $CD$ 和 $AC$ 的方程, 消去 $AC$ 后可以解得 $CD=2$.</p>
</details>


## 直线与圆、两圆的位置关系

直线 $l$ 与圆 $C$ 的位置关系有三种:

- 相离: 直线 $l_1$ 与圆 $C$ 没有交点
- 相切: 直线 $l_2$ 与圆 $C$ 恰有一个交点
- 相交: 直线 $l_3$ 与圆 $C$ 有两个交点

![直线与圆的位置关系](/figs/2022/2022-08/2022-0812-2340.svg)

设直线 $l$ 与圆 $C$ 相切于点 $P$, 则 $CP\perp l$, 即过切点的半径垂直于切线. 此时, 圆心 $C$ 到切线 $l$ 的距离为 $CP$, 即圆心到切线的距离等于半径. 判断圆的切线的另一个方法是: 若圆心 $C$ 到直线 $l$ 的距离为半径 $r$, 则 $l$ 与圆 $C$ 相切.

<myexample>
    <p>如下图所示, 在直角梯形 $ABCD$ 中, $AB\parallel DC$, $\angle A= 90^\circ$, $BC=AB+CD$, 圆 $E$ 以 $BC$ 为直径, 求证: 圆 $E$ 与 $AD$ 相切.</p>
    <img alt="上下底之和等于斜腰的直角梯形, 以斜腰为直径的圆与直腰相切" src="/figs/2022/2022-08/2022-0813-1050.svg"></img>
</myexample>

<myproof>
    <p>由已知, 点 $E$ 为 $BC$ 的中点. 取 $AD$ 的中点 $F$, 连接 $EF$, 则 $EF$ 为直角梯形 $ABCD$ 的中位线, 所以 \[
        EF= \frac12(AB+CD)= \frac12 BC,\quad
        EF\parallel AB.\]
    因为 $\angle A= 90^\circ$, 所以可知 $EF\perp AD$. 由此可知, 圆心 $E$ 到直线 $AD$ 的距离 $EF$ 为半径 $\dfrac12 BC$, 表明圆 $E$ 与 $AD$ 相切.</p>
    <img alt="上下底之和等于斜腰的直角梯形, 以斜腰为直径的圆与直腰相切-辅助线" src="/figs/2022/2022-08/2022-0813-1100.svg"></img>
</myproof>

<myremark>
    <p>判断圆与直线相切的两个方法: 圆与直线有唯一的交点; 圆心到直线的距离等于半径, 都应熟知. 两者在高中数学里都会用到.</p>
</myremark>

<myexercise>
    <p>如上例的图所示, 在直角梯形 $ABCD$ 中, $AB\parallel DC$, $\angle A= 90^\circ$, 圆 $E$ 以 $BC$ 为直径且与 $AD$ 相切, 求证: $BC=AB+CD$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>提示: 设圆 $E$ 与 $AD$ 相切于点 $F$, 连接 $EF$, 则 \[
        EF\perp AD\Rightarrow EF\parallel AB.\]
    利用平行线分线段成比例和梯形中位线的性质, 可推出 $EF= \dfrac12 (AB+DC)$, 再由 $BC$ 为圆 $E$ 的直径可得结论.</p>
</details>

圆 $C_1$ 与圆 $C_2$ 的位置关系有五种 (自行补图):

- 外离: 两圆没有交点, 且每个圆的圆心均在另一个圆的外部
- 外切: 两圆恰有一个交点, 且每个圆的圆心均在另一个圆的外部
- 相交: 两圆有两个交点
- 内切: 两圆恰有一个交点, 且一个圆的圆心在另一个圆的内部
- 内含: 两圆没有交点, 且一个圆的圆心在另一个圆的内部
