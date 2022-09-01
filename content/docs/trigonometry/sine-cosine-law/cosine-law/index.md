---
# bookCollapseSection: true
title: 余弦定理
weight: 2
bookHidden: true
prevPage: /docs/trigonometry/sine-cosine-law/sine-law
prevPageTitle: 正弦定理
nextPage: /docs/trigonometry/sine-cosine-law/solving-triangles
nextPageTitle: 解三角形
---

# 余弦定理

<p>对 $\triangle ABC$, 由直角坐标系中的距离公式或向量的内积运算可得余弦定理: 
\[a^2= b^2+ c^2- 2bc\cos A,\quad\cos A=\frac{b^2+c^2-a^2}{2bc}.\]
还可以写出
\[b^2= a^2+ c^2- 2ac\cos B,\quad\cos C=\frac{a^2+b^2-c^2}{2ab},\]
即余弦定理共三组公式. 在解三角形时, 一般题中已知等式里角多则先考虑用正弦定理, 边多则先考虑用余弦定理.
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $a=\sqrt7$, $b=2$, $A=60^\circ$, 求 $c$ 的值.
</p>
</myexample>
<mysolution>
    <p>将已知条件代入 $a^2= b^2+c^2-2bc\cos A$, 得
    \[7= 4+c^2-2c, \quad\text{即}\quad c=3\ (\text{舍负}).\]
</p>
</mysolution>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $\sin A: \sin B= 3: 5$, $c=2b-a$, 求 $\cos B$ 的值. 
</p>
</myexample>
<mysolution>
    <p>$\sin A: \sin B= 3: 5$ 等价于 $a:b= 3:5$, 故设 $a=3k$, $b=5k$ ($k>0$). 再由 $c=2b-a$ 知 $c= 7k$, 所以
    \[\cos B= \frac{a^2+c^2- b^2}{2ac}= \frac{11}{14}.\]
</p>
</mysolution>
</p>
<p>上题用到两个常见解题思路: 
</p>
<p>(1) 将正弦值的比例与边长的比例互化; 
</p>
<p>(2) 由比例式设辅助参数 $k$.
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $(2a-c)(a^2+c^2-b^2)= 2abc\cos C$, 求角 $B$ 的大小.
</p>
</myexample>
<mysolution>
    <p>将 $a^2+c^2-b^2= 2ac\cos B$ 代入已知式子,
    \[\begin{gathered}
        (2a-c)\cdot 2ac\cos B= 2abc\cos C,\\
        (2a-c)\cos B= b\cos C.
    \end{gathered}\]
    再由正弦定理,
    \[\begin{gathered}
        (2\sin A-\sin C)\cos B= \sin B\cos C,\\
        2\sin A\cos B= \sin (B+C)= \sin A,
    \end{gathered}\]
    所以 $\cos B= \dfrac12$, 即 $B= 60^\circ$.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 遇到形如“$a^2+c^2-b^2$”的式子, 应直接考虑余弦定理.
</p>
<p>(2) 式子 $(2a-c)\cos B= b\cos C$ 也可以利用余弦定理化简.
</p>
<p>(3) $\sin (B+C)= \sin A$ 可参考例 \ref{exa:2021-0427-2310} 后的说明.
</p>
</myremark>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $2c\cos B= 2a+b$, 求角 $C$ 的大小, 并求当 $a=2b$ 时, $\tan A$ 的值.
</p>
</myexample>
<mysolution>
    <p>将 $\cos B= \dfrac{a^2+c^2-b^2}{2ac}$ 代入已知式子, 整理得
    \[c^2= a^2+b^2+ab.\]
    所以
    \[\cos C= \dfrac{a^2+b^2-c^2}{2ab}= -\dfrac12,\]
    即 $C= \dfrac{2\pi}3$.
</p>
<p>当 $a=2b$ 时, 由 $c^2= a^2+b^2+ab$ 知
    \[c^2= (2b)^2+b^2+2b\cdot b= 7b^2,\quad\text{即}\quad
        c= \sqrt7 b.\]
    所以 
    \[\cos A= \frac{b^2+c^2-a^2}{2bc}= \frac2{\sqrt7},\]
    则 $\tan A= \dfrac{2\sqrt3}{3}$.
</p>
</mysolution>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $(a-c\cos B)\sin B= (b-c\cos A)\sin A$, 判断该三角形的形状.
</p>
</myexample>
<mysolution>
    <p>由正弦定理, 已知式化为
    \[\begin{gathered}
        (\sin A-\sin C\cos B)\sin B= (\sin B-\sin C\cos A)\sin A,\\
        \cos B\sin B= \cos A\sin A.
    \end{gathered}\]
    再由二倍角公式, $\sin 2B= \sin 2A$, 所以
    \[\begin{gathered}
        2B= 2A\quad\text{或}\quad 2B+2A= 180^\circ,\\
        B= A\quad\text{或}\quad B+A= 90^\circ,
    \end{gathered}\]
    表明 $\triangle ABC$ 为等腰三角形或直角三角形.
</p>
</mysolution>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $2\cos B\sin A= \sin C$, 判断该三角形的形状.
</p>
</myexample>
<mysolution>
    <p>方法一: 将已知式化为 $2\cos B\cdot a= c$, 再将 $\cos B= \dfrac{a^2+c^2-b^2}{2ac}$ 代入并整理, 可得 $a=b$, 即 $\triangle ABC$ 为等腰三角形.
</p>
<p>方法二: 将 $\sin C= \sin(A+B)$ 代入已知式并展开后整理, 可得 $\sin(A-B)= 0$, 所以 $A=B$, 仍有 $\triangle ABC$ 为等腰三角形.
</p>
</mysolution>
</p>
<p>表示三角形的边角关系的式子, 通常既可以利用正弦定理化简, 也可以利用余弦定理化简. 解题的关键是结合已知式子的特点, 选择合适的公式以简化计算. 可通过练习积累解题经验, 做到更快地选择合适的解题方法.

