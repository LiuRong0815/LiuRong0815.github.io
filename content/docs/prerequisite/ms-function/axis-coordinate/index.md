---
# bookCollapseSection: true
title: 数轴与平面直角坐标系
weight: 1
prevPage: ../
prevPageTitle: 初中函数提要
nextPage: ../linear-inverse
nextPageTitle: 一次函数与反比例函数
---

# 数轴与平面直角坐标系

数轴与平面直角坐标系用坐标分别刻画了直线 (一维空间) 上和平面 (二维空间) 内各点的位置. 用坐标表示点的位置后, 可方便地计算线段的长度、确定线段中点的位置, 或者计算平面图形 (如三角形, 四边形) 的面积等.

## 数轴

数轴是规定了原点 (记为 $O$) 和正方向 (通常由左至右) 的直线, 其上的点与实数一一对应. 数轴上的点与实数对应时,

- 点在原点的左右对应实数的正负
- 点到原点的距离对应实数的绝对值

例如, 若点 $A$ 在原点左侧, 且到原点的距离为 $2$, 则点 $A$ 表示实数 $-2$; 实数 $\sqrt3$ 对应的点在原点右侧, 且到原点的距离为 $\sqrt2$.

若点 $A$ 与实数 $x_1$ 对应, 则称 $x_1$ 为点 $A$ 的坐标, 可记为 $A(x_1)$ (或将点 $A$ 称为点 $x_1$). 对于点 $A(x_1)$ 和 $B(x_2)$, 若 $x_1> x_2$, 则可验证 $AB= x_1-x_2$; 而若 $x_1< x_2$, 则 $AB= x_2-x_1$ (即总是“大数减小数”), 因此可得 $A(x_1)$, $B(x_2)$ **两点间距离公式**: \\[AB= |x_1-x_2|.\\]

上式可帮助理解绝对值的几何意义: $|x|$ 表示点 $x$ 到原点的距离, 而 $|x-1|$ 表示点 $x$ 到点 $1$ 的距离, $|x+2|= |x-(-2)|$ 表示点 $x$ 到点 $-2$ 的距离, \\[
    |2x+1|= 2\biggl|x- \biggl(-\dfrac12\biggr)\biggr|\\]
表示点 $x$ 到点 $-\dfrac12$ 的距离的 $2$ 倍.

设点 $A(x_1)$ 和 $B(x_2)$ 的中点为 $M(x_0)$. 若 $x_1< x_2$, 由点 $M$ 在 $A$, $B$ 中间可知, $x_1< x_0< x_2$, 再由 $AM=MB$ 得 \\[
    x_0- x_1= x_2- x_0,\quad\text{即}\quad
    x_0= \frac{x_1+x_2}2.\\]
若 $x_1> x_2$, 同样可推出上式, 此即线段 $AB$ 的**中点坐标公式**.

## 平面直角坐标系

在平面上作两条互相垂直且原点重合的数轴, 就得到平面直角坐标系, 原点仍记为 $O$, 两条数轴分别称为 $x$ 轴 (横轴), $y$ 轴 (纵轴), 统称为坐标轴. 任取平面上一点 $P$, 并过该点分别 $x$ 轴和 $y$ 轴作垂线段, 垂足记为 $P_x$, $P_y$, 则该点可以由一组有序实数 $(x_0, y_0)$ 表示, 其中

- $x_0$ 为点 $P_x$ 在 $x$ 轴上的坐标, 并称为横坐标
- $y_0$ 为点 $P_y$ 在 $y$ 轴上的坐标, 并称为纵坐标

特别地, 点 $P_x$ 的坐标为 $(x_0,0)$, 点 $P_y$ 的坐标为 $(y_0,0)$, 即: 横轴上点地纵坐标为 $0$, 纵轴上点的横坐标为 $0$. 由定义, 纵坐标相等的点在一条水平直线上, 而横坐标相等的点在一条竖直直线上.

平面直角坐标系的坐标轴将整个平面分割为四个象限 (不计坐标轴自身), 右上角为第一象限, 沿逆时针方向分别可以得到第二至四象限.

取两点 $A(x_1,y_1)$, $B(x_2,y_2)$, 连接 $AB$, 并过这两点分别作 $x$ 轴和 $y$ 轴的垂线, 可得一个矩形. 由数轴上两点间距离公式可得两邻边长分别为 $|x_1-x_2|$, $|y_1-y_2|$, 再由勾股定理可知 $A(x_1,y_1)$, $B(x_2,y_2)$ **两点间的距离公式**: \\[
    AB= \sqrt{(x_1-x_2)^2+ (y_1-y_2)^2}.\\]

<p>设点 $A(x_1,y_1)$, $B(x_2,y_2)$ 的中点为 $M(x_0,y_0)$, 过这三点分别作 $x$ 轴和 $y$ 轴的垂线, 可得两个直角梯形. 由梯形中位线的性质可得线段 $AB$ 的 <strong>中点坐标公式</strong>: \[
    \left\{\!\!\begin{array}{l}
        x_0= \dfrac{x_1+x_2}2,\\[6pt]
        y_0= \dfrac{y_1+y_2}2,
    \end{array}\right.\quad\text{即}\quad
    M\biggl(\frac{x_1+x_2}2, \frac{y_1+y_2}2\biggr).\]</p>

## 点的变换

点的变换一般指点的平移、轴对称、中心对称、旋转, 下面简要介绍相关结论. 以下结论均建议结合图形来理解并记忆大致推导过程.

### 点的平移

点在坐标平面内的平移可以分解为沿 $x$ 轴和 $y$ 轴方向的平移. 设 $a>0$, 点 $P$ 的坐标为 $(x,y)$, 则将点 $P(x,y)$

- 向左平移 $a$ 个单位长度, 得到点 $P_1(x-a,y)$
- 向右平移 $a$ 个单位长度, 得到点 $P_2(x+a,y)$
- 向上平移 $a$ 个单位长度, 得到点 $P_3(x,y+a)$
- 向下平移 $a$ 个单位长度, 得到点 $P_4(x,y-a)$

### 点的轴对称

设点 $P$ 关于直线 $l$ 的对称点为 $P'$, 则 $l$ 是线段 $PP'$ 的中垂线. 为方便用坐标表示, 也可以转化为 $PP'\perp l$ 且 $PP'$ 的中点在 $l$ 上. 此处只介绍当 $l$ 平行于坐标轴时的结论, 而 $l$ 为一般直线的情形需要用到高中数学解析几何知识. 设 $b$ 为任意实数, 则

(1) 当 $l$ 为 $x$ 轴时, 对称点 $P'$ 的坐标为 $(x,-y)$;

(2) 当 $l$ 为 $y$ 轴时, 对称点 $P'$ 的坐标为 $(-x,y)$;

(3) 当 $l$ 平行于 $x$ 轴且其上点的纵坐标均为 $b$ 时, 对称点 $P'$ 的横坐标与点 $P$ 的横坐标相同, 而 $PP'$ 的中点在 $l$ 上表明中点的纵坐标为 $b$, 所以由中点坐标公式, 对称点 $P'$ 的坐标为 $(x,2b-y)$;

(4) 当 $l$ 平行于 $y$ 轴且其上点的横坐标均为 $b$ 时, 同理可得对称点 $P'$ 的坐标为 $(2b-x,y)$.

### 点的中心对称

<p>设点 $P(x_1,y_1)$ 关于点 $M(x_0,y_0)$ 的对称点为 $P'(x_2,y_2) $, 则 $M$ 是线段 $PP'$ 的中点, 所以 \[\left\{\!\!\begin{array}{l}
    x_0= \dfrac12(x_1+x_2),\\[6pt]
    y_0= \dfrac12(y_1+y_2),
    \end{array}\right.\quad\text{解得}\quad
    \left\{\!\!\begin{array}{l}
    x_2= 2x_0-x_1,\\
    y_2= 2y_0-y_1,
    \end{array}\right.\] 表明点 $P'$ 的坐标为 $(2x_0-x_1,2y_0-y_1)$.</p>

### 点的旋转

设点 $P$ 绕点 $M$ 逆时针旋转角度 $\theta$ 后得到点 $P'$. 此处只介绍当点 $M$ 为原点 $O$ 和角度 $\theta$ 分别为 $90^\circ$, $180^\circ$, $270^\circ$ 时的结论, 其余一般情形需要用到高中数学三角函数、向量知识.

先考虑具体的点 $P_1(1,2)$, 其关于原点 $O$ 逆时针旋转 $90^\circ$ 后得到点 $P_2(-2,1)$, 再次逆时针旋转 $90^\circ$ 后得到点 $P_3(-1,-2)$, 继续逆时针旋转 $90^\circ$ 后得到点 $P_4(2,-1)$. 以点 $P_1$, $P_2$, $P_3$, $P_4$ 中的任意一点为点 $P$, 可得结论: 

点 $P(x,y)$ 绕原点 $O$ 逆时针旋转 $90^\circ$ 后得到点 $P'(-y,x)$.

上述结论表明绕原点 $O$ 逆时针旋转 $90^\circ$ 后, 将旧点坐标横纵对调, 且横坐标变相反数可得到新点坐标. 一个简单的推论是: 点 $P(x,y)$ 绕原点 $O$ 逆时针旋转 $180^\circ$ 后得到点 $P''(-x,-y)$ (实为关于原点的中心对称), 逆时针旋转 $270^\circ$ 后得到点 $P'''(y,-x)$.

<!-- ### 点的缩放

点 $P$ 关于点 $M$ 缩放后得到点 $P'$ 是指, $P$ 和 $P'$ 均在射线 $MP$ 上, 并用 $\dfrac{MP'}{MP}$ 的值 (设为 $k$) 表示“缩”(对应 $0<k<1$), “放”(对应 $k>1$). 此处 -->