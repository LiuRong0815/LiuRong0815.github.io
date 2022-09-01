---
# bookCollapseSection: true
title: 解三角形
weight: 3
bookHidden: true
prevPage: /docs/trigonometry/sine-cosine-law/cosine-law
prevPageTitle: 余弦定理
nextPage: /docs/trigonometry/vector
nextPageTitle: 向量
---

# 解三角形


<myexample>
<p>在 $\triangle ABC$ 中, $a=\sqrt7$, $b=2$, $A= 60^\circ$, 求 $c$ 的值.
</p>
</myexample>
<mysolution>
    <p>题中有三边一角, 正好用余弦定理. 由
    \[a^2= b^2+c^2- 2bc\cos A\quad \text{即}\quad
        7= 4+c^2- 2c,\]
    解得 $c= 3$.
</p>
</mysolution>
</p>
<p><myexample>
<p>对于 $\triangle ABC$, 判断下列命题是否正确:
</p>
<p>(1) 若 $\cos A= \cos B$, 则 $\triangle ABC$ 是等腰三角形;
</p>
<p>(2) 若 $\triangle ABC$ 为锐角三角形, 则 $A+B> \dfrac\pi2$, 从而 $\sin A> \cos B$;
</p>
<p>(3) 符合条件 $a=8$, $c=10$, $B=60^\circ$ 的 $\triangle ABC$ 有两个;
</p>
<p>(4) 若 $\sin^2 A+ \sin^2 B< \sin^2 C$, 则 $\triangle ABC$ 是钝角三角形.
</p>
</myexample>
<mysolution>
    <p>(1) 因为余弦函数 $f(x)=\cos x$, $x\in(0,\pi)$ 为单调递减函数, 所以 $\cos A= \cos B$ 表明 $A=B$, 结论成立.
</p>
<p>(2) 锐角三角形的三个内角均为锐角, 则 
    \[A+B= \pi-C> \frac\pi2,\]
    即 $B> \dfrac\pi2- A$. 再由余弦函数 $f(x)=\cos x$, $x\in(0,\pi)$ 为单调递减函数知
    \[f(B)< f\Bigl(\dfrac\pi2- A\Bigr) \quad\text{即}\quad
        \cos B< \cos\Bigl(\dfrac\pi2- A\Bigr)= \sin A,\]
    结论成立.
</p>
<p>(3) 由 $b^2= a^2+c^2- 2ac\cos B$ 可算出 $b$ 的值. 所以 $\triangle ABC$ 的三边是确定的, 故符合条件的 $\triangle ABC$ 只有一个. 结论不成立. (本小题也可以结合全等三角形的“边角边”判定法得到唯一性.)
</p>
<p>(4) 由正弦定理, 已知不等式化为 $a^2+b^2< c^2$. 再由余弦定理,
    \[\cos C= \frac{a^2+b^2-c^2}{2ab}< 0,\]
    表明 $C\in\Bigl(\dfrac\pi2,\pi\Bigr)$, 即 $\triangle ABC$ 为钝角三角形. 结论成立.
</p>
</mysolution>
</p>
<p><myremark>
    <p>(1) 上题中前两个小问都用到了余弦函数在区间 $(0,\pi)$ 上的单调递减性质.
</p>
<p>(2) 最后一个小问同时用到了正弦定理和余弦定理, 也得到结论: $a^2+b^2< c^2$ $\Leftrightarrow$ 角 $C$ 为钝角.
</p>
</myremark>

<myexample>
<p>已知在 $\triangle ABC$ 中, $a=\sqrt6$, $b=3\sqrt2$, $A=30^\circ$, 求角 $B$ 的大小.
</p>
</myexample>
<mysolution>
    <p>由正弦定理, $\dfrac{a}{\sin A}= \dfrac{b}{\sin B}$, 即
    \[\frac{\sqrt6}{\sin30^\circ}= \frac{3\sqrt2}{\sin B},\quad
    \text{即}\quad \sin B= \frac{\sqrt3}{2},\]
    所以 $B= 60^\circ$ 或 $120^\circ$.
</p>
</mysolution>

<myexample>
<p>已知 $\triangle ABC$ 中, $a\sin A- b\sin B= 4c\sin C$, $\cos A= -\dfrac14$, 求 $\dfrac{c}{b}$ 的值.
</p>
</myexample>
<mysolution>
    <p>已知两式可分别用正弦定理和余弦定理化为
    \[a^2- b^2= 4c^2,\quad
        \frac{b^2+c^2-a^2}{2bc}= -\frac14,\]
    再将上述前一式代入后一式, 
    \[b^2+c^2- (b^2+4c^2)= -\frac14\cdot 2bc,\]
    整理得 $\dfrac{c}{b}= \dfrac16$.
</p>
</mysolution>


<myexample>
<p>在 $\triangle ABC$ 中, $\cos C= \dfrac17$, $c=8$, $a=7$, 求 $b$ 的值和角 $A$ 的大小.
</p>
</myexample>
<mysolution>
    <p>由余弦定理, $c^2= a^2+b^2- 2ab\cos C$, 即
    \[64= 49+ b^2- 14b\cdot\frac17, \quad\text{即}\quad
        (b+3)(b-5)=0,\]
    解得 $b=5$ (舍负). 又因为
    \[\cos A= \frac{b^2+c^2- a^2}{2bc}= \frac12,\]
    所以 $A= 60^\circ$.
</p>
</mysolution>
</p>
<p><myexample>
<p>在 $\triangle ABC$ 中, $\cos B= -\dfrac12$, $b-c=2$, $a=3$, 求 $b$, $c$ 和 $\sin(B+C)$ 的值.
</p>
</myexample>
<mysolution>
    <p>由余弦定理, $b^2= a^2+c^2- 2ac\cos B$, 将已知条件代入,
    \[(c+2)^2= 9+c^2- 6c\cdot\biggl(-\frac12\biggr),\]
    解得 $c=5$, 所以 $b=7$. 又因为
    \[\cos A= \frac{b^2+c^2- a^2}{2bc}= \frac{13}{14},\]
    则 $\sin A= \dfrac{3\sqrt3}{14}$, 所以
    \[\sin(B+C)= \sin(\pi- A)= \sin A= \frac{3\sqrt3}{14}.\]
</p>
</mysolution>
</p>
<p>在上题中计算 $\sin(B+C)$ 时，不应分别计算 $\cos B$, $\sin B$, $\cos C$ 和 $\sin C$ 后, 将 $\sin(B+C)$ 展开代入求值, 而应利用在 $\triangle ABC$ 中, $\sin(B+C)= \sin A$ 来简化计算.
</p>

<myexample>
<p>在 $\triangle ABC$ 中, $b\sin A= a\cos\Bigl(B- \dfrac\pi6\Bigr)$, $c= 5$, 求角 $B$ 的大小, 并从条件“$b=7$”和“$C=\dfrac\pi4$”中任选一个, 求 $a$ 的值.
</p>
</myexample>
<mysolution>
    <p>利用正弦定理, 已知等式可变形如下: \[\begin{aligned}
        \sin B\sin A &= \sin A\cos\Bigl(B- \frac\pi6\Bigr),\\
        \sin B &= \cos B\cos\frac\pi6+ \sin B\sin\frac\pi6,\\
        \frac12\sin B &= \frac{\sqrt3}2\cos B,\\
        \tan B&= \sqrt3,
    \end{aligned}\]
    所以 $B=\dfrac\pi3$. 下面来求 $a$ 的值.
</p>
<p>方法一: 若选择条件“$b=7$”, 则是“已知 $b$, $c$ 和 $B$, 求 $a$”, 应选择使用余弦定理. 此时 $\cos B= \dfrac{a^2+c^2- b^2}{2ac}$ 化为 \[
        \cos\frac\pi3= \frac{a^2+ 25- 49}{2a\cdot 5},
        \quad\text{解得}\quad a= 8.\]
</p>
<p>方法二: 若选择条件“$C=\dfrac\pi4$”, 则是“已知 $B$, $C$ 和 $c$, 求 $a$”, 应选择使用余弦定理. 先求出 \[
        A= \pi-B-C= \frac{5\pi}{12},
    \] 因此 \[\begin{aligned}
        \sin A
        &= \sin\frac{5\pi}{12}
         = \sin\Bigl(\frac\pi6+ \frac\pi4\Bigr)\\
        &= \sin\frac\pi6\cos\frac\pi4+ \cos\frac\pi6\sin\frac\pi4\\
        &= \frac{\sqrt6+ \sqrt2}{4},
    \end{aligned}\] 此时 $\dfrac{a}{\sin A}= \dfrac{c}{\sin C}$ 化为 \[
        \frac{a}{(\sqrt6+ \sqrt2)/4}= \frac{5}{\sqrt2/2},
        \quad\text{解得}\quad a= \frac{5(\sqrt3+1)}{2}.\]
</p>
</mysolution>

<myexample>
<p>在 $\triangle ABC$ 中, 角 $A$, $B$, $C$ 所对的边分别为 $a$, $b$, $c$, 已知 $\dfrac{2b+c}a= \dfrac{\cos(A+B)}{\cos A}$.
</p>
<p>(1) 求角 $A$ 的大小;\quad (2) 求 $\sin B\sin C$ 的最大值;
</p>
<p>(3) 若 $a= 6$, 求 $\triangle ABC$ 面积的最大值.
</p>
</myexample>
<mysolution>
    <p>(1) 由正弦定理, 已知等式化为 \[
        \frac{2\sin B+ \sin C}{\sin A}
        = \frac{\cos(\pi- C)}{\cos A}
        = -\frac{\cos C}{\cos A},\]
    交叉相乘并整理, \[\begin{aligned}
        (2\sin B+ \sin C)\cos A+ \sin A\cos C&= 0,\\
        2\sin B\cos A+ \sin(C+ A)&= 0,\\
        2\sin B\cos A+ \sin B&= 0.
    \end{aligned}\]
    因为 $\sin B\neq 0$, 所以 $\cos A= -\dfrac12$, 即 $A= \dfrac{2\pi}3$.
</p>
<p>(2) 由 (1) 知 $B+C= \pi-A= \dfrac{\pi}{3}$, 则 $B\in \Bigl(0,\dfrac\pi3\Bigr)$, 且 \[\begin{aligned}
        \sin B\sin C
        &= \sin B\sin\Bigl(\frac\pi3- B\Bigr)\\
        &= \sin B\Bigl(\sin\frac\pi3\cos B- \cos\frac\pi3\sin B\Bigr)\\
        &= \frac{\sqrt3}2\sin B\cos B- \frac12\sin^2 B\\
        &= \frac{\sqrt3}4\sin 2B- \frac14(1- \cos 2B)\\
        &= \frac12\biggl(\frac{\sqrt3}2\sin 2B+ \frac12\cos 2B\biggr)- \frac14\\
        &= \frac12\sin\Bigl(2B+ \frac\pi6\Bigr)- \frac14.
    \end{aligned}\]
    因为 $2B+ \dfrac\pi6\in \biggl(\dfrac\pi6,\dfrac{5\pi}6\biggr)$, 所以 \[
    \sin\Bigl(2B+ \frac\pi6\Bigr)\in \biggl(\frac12, 1\biggr),
    \] 即 $\sin B\sin C\in \biggl(0,\frac14\biggr]$.
</p>
<p>(3) 因为 $\triangle ABC$ 面积为 $\dfrac12 bc\sin A= \dfrac{\sqrt3}4 bc$, 所以其最大值对应 $bc$ 的最大值. 由余弦定理, $a^2= b^2+c^2- 2bc\cos A$, 将题中数据代入, \[
        36= b^2+c^2+ bc,\quad\text{即}\quad
        b^2+c^2= 36-bc.\]
    再由均值不等式, $b^2+c^2\geqslant 2bc$, 所以 \[
        36-bc\geqslant 2bc,\quad\text{即}\quad bc\leqslant 12.\]
    由此可知, $\triangle ABC$ 面积的最大值为 $\dfrac{\sqrt3}4\cdot 12= 3\sqrt3$.
</p>
</mysolution>

<myexample>
<p>设 $\triangle ABC$ 的内角 $A$, $B$, $C$ 的对边分别为 $a$, $b$, $c$, 面积为 $2\sqrt3$, 且 $(\sin B + \sin C)^2 = \sin^2 A + \sin B\sin C$, $b+c=6$, 求角 $A$ 的大小和 $a$ 的值.
</p>
</myexample>
<mysolution>
    <p>由正弦定理, $(b+c)^2= a^2+bc$, 则 \[\begin{gathered}
        b^2+c^2-a^2= -bc,\\
        \cos A= \frac{b^2+c^2-a^2}{2bc}= -\frac12,
    \end{gathered}\]
    因此 $A= 120^\circ$. 再由三角形面积定理, \[
        \frac12bc\sin A= 2\sqrt3 \Rightarrow bc=8,\]
    所以 \[
        a^2=(b+c)^2-bc= 28.\]
</p>
</mysolution>

