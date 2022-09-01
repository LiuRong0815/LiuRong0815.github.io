---
# bookCollapseSection: true
title: 正弦定理
weight: 1
bookHidden: true
prevPage: /docs/trigonometry/sine-cosine-law
prevPageTitle: 正弦定理与余弦定理
nextPage: /docs/trigonometry/sine-cosine-law/cosine-law
nextPageTitle: 余弦定理
---

# 正弦定理

<p>设 $\triangle ABC$ 中, 角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 则由三角形面积公式和任意角正弦的定义可得三角形面积定理 (高中常用):
\[S= \frac{1}{2}ab\sin C=\frac{1}{2}bc\sin A=\frac{1}{2}ca\sin B.\]
推导见“2021 年 2 月 28 日答疑记录”的第一个例子. 
</p>
<p>将三角形面积定理换一种写法就得到正弦定理: 
\[\frac{a}{\sin A}= \frac{b}{\sin B}= \frac{c}{\sin C},\]
有时也写成
\[\frac{BC}{\sin A}= \frac{AC}{\sin B}= \frac{AB}{\sin C}.\]
作 $\triangle ABC$ 外接圆, 用纯几何法可证明 $\dfrac{a}{\sin A}= 2R$, 其中常数 $R$ 表示外接圆半径. 应用时也常写 $a= 2R\sin A$, 以及
\[\frac{\sin A}a= \frac{\sin B}b= \frac{\sin C}c.\]
有些关于 $a$, $b$ 或 $\sin A$, $\sin B$ 的式子可以利用正弦定理互相转化, 如
\[\sin^2 A= \sin^2 B\Leftrightarrow a\sin A= b\sin B
    \Leftrightarrow a^2=b^2.\]
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $A= 60^\circ$, $B= 45^\circ$, $BC= 3\sqrt2$, 求 $AC$ 的值.
</p>
</myexample>
<mysolution>
    <p>由正弦定理, $\dfrac{BC}{\sin A}= \dfrac{AC}{\sin B}$, 代入已知条件, 解得 $AC= 2\sqrt3$.
</p>
</mysolution>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $a= \sqrt2$, $b=\sqrt3$, $B= 60^\circ$,  求角 $A$ 的大小.
</p>
</myexample>
<mysolution>
    <p>由 $\dfrac{a}{\sin A}= \dfrac{b}{\sin B}$ 可以解得 $\sin A= \dfrac{\sqrt2}2$, 再画正弦线知 $A= 45^\circ$ 或 $135^\circ$. 因为 $B= 60^\circ$ 且三角形内角和不超过 $180^\circ$, 所以只能 $A= 45^\circ$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 三角形内角的大小可以利用其正、余弦值或正切值反推得到. 需要注意的是, 通常由正弦值可以推得两个角. 
</p>
<p>(2) 上题中, 也可以利用“大边对大角”知 $A< B$, 仍得到 $A= 45^\circ$.
</p>
</myremark>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $\sqrt3 a\cos B+ b\sin A= 0$, 求角 $B$ 的大小.
</p>
</myexample>
<mysolution>
    <p>已知式化为
    \[\sqrt3 \sin A\cos B+ \sin B\sin A= 0,\quad\text{即}\quad
        \tan B= -\sqrt3,\]
    所以 $B= 120^\circ$.
</p>
</mysolution>
</p>
<p>\begin{example}\label{exa:2021-0427-2310}
    在 $\triangle ABC$ 中, $a=2$, $\sin(A+B)= \dfrac13$, $\sin A= \dfrac14$, 求 $c$ 的值.
</p>
</myexample>
<mysolution>
    <p>$\sin(A+B)= \dfrac13$ 可化为 $\sin C= \dfrac13$, 再由 $\dfrac{a}{\sin A}= \dfrac{c}{\sin C}$ 知 $c= \dfrac83$.
</p>
</mysolution>
</p>
<p>上题中的 $\sin (A+B)= \sin C$ 可由 $A+B= \pi- C$ 和诱导公式得到.
</p>


<myexample>
<p>(三角形面积定理) 设 $\triangle ABC$ 中, $AB=c$, $BC=a$, $AC=b$, 则
    \[S_{\triangle ABC}= \frac12 ab\sin C
        = \frac12 bc\sin A= \frac12 ca\sin B.\]
</p>
</myexample>
<mysolution>
    <p>如图所示, 作 $AB$ 边上的高, 考虑 $\mathrm{Rt}\triangle ACD$ 可知
    \[\frac{CD}{CA}= \sin A= \sin(\pi-A),\]
    所以 $CD= b\sin A$, 且
    \[S_{\triangle ABC}= \frac12 AB\cdot CD
        = \frac12 bc\sin A.\]
    同理可得另外两个公式.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0228-1240-crop}\qquad
        \includegraphics[scale=1.5]{2021-0228-1520-crop}
    </center>
</p>
</mysolution>

