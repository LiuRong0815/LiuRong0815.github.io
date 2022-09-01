---
# bookCollapseSection: true
title: 平面向量基本定理
weight: 2
bookHidden: true
prevPage: /docs/trigonometry/vector/vec-def
prevPageTitle: 向量的定义
nextPage: /docs/trigonometry/vector/dot-product
nextPageTitle: 向量的内积
---

# 平面向量基本定理


<myexample>
<p>已知 $\triangle ABC$ 中, 角 $A$, $B$, $C$ 所对的边分別为 $a$, $b$, $c$, $a=\sqrt7$, $b=2$. 向量 $\bm{m}= (a,\sqrt3b)$, $\bm{n}= (\cos A, \sin B)$, 且 $\bm{m}\parallel\bm{n}$. 求角 $A$ 的大小和 $\triangle ABC$ 的面枳.
</p>
</myexample>
<mysolution>
    <p>因为 $\bm{m}\parallel\bm{n}$, 所以 $a\sin B= \sqrt3b\cos A$. 由正弦定理,
    \[\sin A\sin B= \sqrt3\sin B\cos A\quad\text{即}\quad
        \tan A=\sqrt3,\]
    则 $A= 60^\circ$.
</p>
<p>求三角形面积优先考虑面积定理. 由余弦定理, 
    \[a^2= b^2+c^2- 2bc\cos A\quad\text{即}\quad
        7= 4+c^2- 4c\cdot\frac12,\]
    解得 $c= 3$ (舍负). 因此
    \[S_{\triangle ABC}= \frac12 bc\sin A
        = \frac12\cdot 2\cdot 3\cdot \frac{\sqrt3}{2}
        = \frac{3\sqrt3}{2}.\]
</p>
</mysolution>


<myexample>
<p>如图所示, 在 $\triangle ABC$ 中, 点 $D$, $E$ 満足 $\overrightarrow{BC}= 2\overrightarrow{BD}$, $\overrightarrow{CA}= 3\overrightarrow{CE}$. 若 $\overrightarrow{DE}= x\overrightarrow{AB}+ y\overrightarrow{AC}$, 求 $x-y$ 的值.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0714-2240-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>以 $\overrightarrow{AB}$ 和 $\overrightarrow{AC}$ 为基向量, 表示所有其他向量. 由 $\overrightarrow{BC}= 2\overrightarrow{BD}$ 知 $D$ 为 $BC$ 中点, 则 \[\overrightarrow{AD}= \frac12(\overrightarrow{AB}+ \overrightarrow{AC}).\] 
    再由 $\overrightarrow{CA}= 3\overrightarrow{CE}$ 知 $\overrightarrow{AE}= \frac23\overrightarrow{AC}$, 所以 \[\begin{aligned}
        \overrightarrow{DE}
        &= \overrightarrow{AE}- y\overrightarrow{AD}\\
        &= \frac23\overrightarrow{AC}- \frac12(\overrightarrow{AB}+ \overrightarrow{AC})\\
        &= -\frac12\overrightarrow{AB}+ \frac16\overrightarrow{AC}.
    \end{aligned}\]
    上式表明 $x= -\dfrac12$, $y=\dfrac16$, 所以 $x-y= -\dfrac23$.
</p>
</mysolution>

<myexample>
<p>在平面直角坐标系 $Oxy$ 中, 已知 $A(1,0)$, $B(0,1)$, $C$ 为第一象限内一点, $\angle AOC= \dfrac{\pi}4$ 且 $|OC|=2$. 若 $\overrightarrow{OC}= \lambda\overrightarrow{OA}+ \mu\overrightarrow{OB}$, 求 $\lambda+\mu$ 的值.
</p>
</myexample>
<mysolution>
    <p>作图可知, $C(\sqrt2,\sqrt2)$, 代入已知的向量等式得, $\lambda= \mu= \sqrt2$, 所以 $\lambda+\mu= 2\sqrt2$.
</p>
</mysolution>

