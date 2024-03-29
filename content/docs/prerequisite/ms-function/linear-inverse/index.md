---
# bookCollapseSection: true
title: 一次函数与反比例函数
weight: 2
prevPage: ../axis-coordinate
prevPageTitle: 数轴与平面直角坐标系
nextPage: ../quadratic-function-inequality
nextPageTitle: 二次函数与二次不等式
---

# 一次函数与反比例函数

利用函数可以动态地分析问题和解决问题. 不同类型的函数有不同的性质, 一次函数与反比例函数是两类较简单的函数.

## 一次函数

一次函数的解析式为 $y= kx+b$ ($k\neq 0$). 函数 $y=kx$ ($k\neq 0$) 是特殊的一次函数, 通过描点绘图可知, 其图象为过原点的直线, 且

- 当 $k>0$ 时, 直线过第一、三象限 (从左向右观察为上升)
- 当 $k<0$ 时, 直线过第二、四象限 (从左向右观察为下降)
- 当 $k$ 逐渐增大时, 图象绕原点逆时针旋转
- 当 $|k|$ 越大时, 直线越“陡峭”

![一次函数 (b=0) 的图象](/figs/2022/2022-08/2022-0814-1820.svg)

函数 $y=x$ 的图象除了过原点和第一、三象限, 还与 $x$ 轴、$y$ 轴夹角均为 $45^\circ$, 通常也称为第一、三象限的角平分线. 类似地, 函数 $y=-x$ 的图象称为第二、四象限的角平分线.

一般的一次函数 $y= kx+b$ ($k\neq 0$) 的图象仍为直线, 因此一次函数也称为**线性函数**. 其图象可由对应的 $y=kx$ 的图象平移得到: 对相同的 $x$, 两者的 $y$ 有固定的差值. 例如, $y=2x+1$ 的图象可由 $y=2x$ 的图象向上平移一个单位长度得到, $y= -x-2$ 的图象可由 $y= -x$ 的图象向下平移两个单位长度. 由此可得, $k$ 的正负号决定了 $y= kx+b$ 的函数值随 $x$ 变化的趋势: 

- 当 $k>0$ 时, $y$ 随 $x$ 增加而增加 (函数单调递增)
- 当 $k<0$ 时, $y$ 随 $x$ 增加而减少 (函数单调递减)

![一次函数的图象与 k 的关系](/figs/2022/2022-08/2022-0814-1830.svg)

<myremark>
    <p>对函数 $y= kx+b$ 的图象而言, 当 $k$ 固定时, 常数项 $b$ 的变化引起图象的平移; 当 $b$ 固定时, 一次项系数 $k$ 的变化引起图象的旋转.</p>
</myremark>

一次函数 $y= kx+b$ 的解析式也可视为关于 $x$ 和 $y$ 的二元一次方程, 该方程的所有解 $(x,y)$ 构成平面直角坐标系内一条直线. 更进一步, 计算两条直线的交点坐标, 对应求解由它们的解析式组成的二元一次方程组. 这也是计算两个函数图象的交点坐标的一般思路, 即求解联立方程组.

<myexample>
    <p>计算一次函数 $y=\dfrac32 x$, $y= \dfrac12 x$ 与 $y= -\dfrac12 x+4$ 的图象所围图形的面积.</p>
</myexample>

<mysolution>
    <p>一次函数的图象是直线, 所以需要确定三条直线围成的图形. 将三个解析式两两联立, 解对应的二元一次方程组, 可得三个交点. 例如, 求解 \[\left\{\!\!\begin{array}{l}
        y=\dfrac32 x,\\[6pt]
        y= -\dfrac12 x+4,
    \end{array}\right.\quad\text{可得}\quad \left\{\!\!\begin{array}{l}
        x=2,\\[6pt]
        y=3,
    \end{array}\right.\]
    即交点为 $(2,3)$, 记为点 $A$. 同理可得另外两个交点: $O(0,0)$, $B(4,2)$, 所以三条直线围成三角形. 再用割补法可以求得三角形的面积为 $4$.</p>
    <img alt="求坐标系中三角形的面积-辅助线" src="/figs/2022/2022-08/2022-0814-1900.svg"></img>
</mysolution>

<span id="反比例函数"></span>

## 反比例函数

反比例函数的解析式为 $y=\dfrac{k}x$ ($k\neq 0$), 式中 $x$ 与 $y$ 均不为 $0$. 该解析式有时也写成 $xy=k$. 通过描点绘图可知, 反比例函数 $y=\dfrac{k}x$ 的图象有两支, 均以 $x$ 轴和 $y$ 轴为渐近线 (分别称为水平渐近线和竖直渐近线). 此图象称为双曲线, 且

- 当 $k>0$ 时, 双曲线的两支分别在第一、三象限 (均为单调递减)
- 当 $k<0$ 时, 双曲线的两支分别在第二、四象限 (均为单调递增)

![反比例函数的图象与 k 的关系](/figs/2022/2022-08/2022-0815-1940.svg)

简单的分式函数 $y=\dfrac{k}x+b$ ($k\neq 0$) 的图象可以由对应的反比例函数 $y=\dfrac{k}x$ 的图象上下平移得到: 当 $b>0$ 时, 将后者向上平移; 反之向下平移. 由于对应的渐近线也发生平移, 所以在绘图时, 通常先绘出渐近线, 再参照渐近线和 $y=\dfrac{k}x$ 的图象绘出 $y=\dfrac{k}x+b$ 的图象.

![简单的分式函数的图象与 b 的关系](/figs/2022/2022-08/2022-0815-1950.svg)

<span id="利用反比例函数解不等式"></span>
利用反比例函数图象可以求解简单的分式不等式. 例如, 解不等式 $\dfrac1x< 1$ 相当于求函数 $y=\dfrac1x$ 的图象上纵坐标小于 $1$ 的所有点 $(x,y)$ (下图中函数图象在水平虚线下方的部分) 的横坐标取值范围, 由图可知, \\[
    x< 0\ \text{或}\ x>1.\\]
如果不借助函数图象, 直接在原不等式两边乘以 $x$, 很容易漏掉 $x< 0$ 这一取值范围 (不等式两边乘以负数, 会改变不等号的方向).

![用反比例函数图象解不等式](/figs/2022/2022-08/2022-0815-2020.svg)

<myexample>
    <p>解不等式: $x-2>\dfrac3x$.</p>
</myexample>

<mysolution>
    <p>绘出函数 $y= x-2$ 与 $y= \dfrac3x$ 的图象 (分别为直线和双曲线), 并联立解析式求出交点 $(-1,-3)$, $(3,1)$. 解原不等式相当于求直线在双曲线上方的部分的横坐标的取值范围. 结合图形可知, \[
        -1< x< 0\ \text{或}\ x>3.\]</p>
    <img alt="用反比例函数图象解不等式" src="/figs/2022/2022-08/2022-0815-2040.svg"></img>
</mysolution>

<myremark>
    <p>若上例中的不等式为 $x-\dfrac3x>2$, 则可以先化为 $x-2>\dfrac3x$, 再绘图求解, 即绘图之前, 要先将不等式化为容易绘图的形式.</p>
</myremark>

<myexercise>
    <p>解不等式: $x+1\leqslant\dfrac2x$.</p>
</myexercise>

<details><summary>参考答案</summary>
    <p>仿上例的方法, 可得 $x\leqslant -2$ 或 $x\geqslant 1$.</p>
</details>
