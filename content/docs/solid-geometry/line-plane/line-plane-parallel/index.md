---
# bookCollapseSection: true
title: 线面平行
weight: 2
bookHidden: true
prevPage: /docs/solid-geometry/line-plane/line-plane-position
prevPageTitle: 直线与平面的位置关系
nextPage: /docs/solid-geometry/line-plane/line-plane-perp
nextPageTitle: 线面垂直
---

# 线面平行

<p>线面平行判定定理: 平面外一条直线与此平面内某条直线平行, 则该直线与此平面平行.
</p>
<p>对应的符号语言 (如图 \ref{fig-190630-1800}): $a\not\subset\alpha$, $b\subset\alpha$ 且 $a\parallel b$ $\Rightarrow$ $a\parallel\alpha$.
</p>
<p>面面平行判定定理: 一个平面内的两条相交直线与另一个平面平行, 则这两个平面平行.
</p>
<p>对应的符号语言 (如图 \ref{fig-190630-1810}): $a\subset\beta$,  $b\subset\beta$, $a\cap b= P$, $a\parallel\alpha$, $b\parallel\alpha$ $\Rightarrow$ $\beta\parallel\alpha$.
</p>
<p>\begin{figure}[htb]
    \small
    \centering
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[scale=0.8]
        \draw (0,0,0) coordinate (A);
        \draw (3,0,0) coordinate (B);
        \draw (0,0,-3) coordinate (D);
        \draw (B)++(D) coordinate (C);
        \draw (0.5,0) +(0,-0.05)node[above] {$\alpha$};
</p>
<p>\def\ay{2} \def\bz{-0.9}
        \draw (A)--(B)--(C)--(D)--(A) (0.5,0,\bz)--(2.5,0,\bz) (0.9,\ay)--(3,\ay);
        \draw (1.8,\ay) node[above] {$a$};
        \draw (1.5,0,\bz) node[above] {$b$};
      \end{tikzpicture}
      \caption{}\label{fig-190630-1800}
    \end{minipage}
    \hskip 0.5cm  
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[scale=0.8]
        \draw (0,0,0) coordinate (A);
        \draw (3,0,0) coordinate (B);
        \draw (0,0,-3) coordinate (D);
        \draw (B)++(D) coordinate (C);
        \draw (0.5,0) +(0,-0.05)node[above] {$\alpha$};
        \draw (0,2,0) coordinate (A1);
        \draw (A1)++(B) coordinate (B1);
        \draw (A1)++(D) coordinate (D1);
        \draw (A1)++(C) coordinate (C1);
        \draw (A1)++(0.5,0) +(0,-0.05)node[above] {$\beta$};
</p>
<p>\draw (A)--(B)--(C)--(D)--(A) (A1)--(B1)--(C1)--(D1)--(A1);
        \draw[name path= linea] (0.7,2,-0.8)--(2.4,2,-2.1); % line a
        \draw[name path= lineb] (0.7,2,-2.1)--(2.4,2,-0.8); %\line b
        \draw (1.3,2,-0.7) node {$a$};
        \draw (0.5,2,-2.2) node {$b$}; 
        \draw[fill=black,name intersections={of=linea and lineb}] (intersection-1) circle (1pt) node[above] {$P$};
      \end{tikzpicture}
      \caption{}\label{fig-190630-1810}
    \end{minipage}
    \end{figure}
</p>
<p><myexample>
<p>如图所示, 直线 $a\parallel \text{平面\ }\alpha$, 点 $A$ 与直线 $a$ 在平面 $\alpha$ 的两侧, 点 $B$, $C$, $D\in a$, 线段 $AB$, $AC$, $AD$ 分别交平面 $\alpha$ 于点 $E$, $F$, $G$. 若 $BD= 4$, $CF=4$, $AF=5$, 求 $EG$ 的大小.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0525-2300-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>由 $a\parallel \alpha$ 和线面平行性质定理知 $EG\parallel BD$. 考虑 $\triangle ABD$ 可得, 
    \[\triangle AFG\sim \triangle ACD,\quad
    \triangle AEG\sim \triangle ABD,\]
    所以 
    \[\frac{EG}{BD}= \frac{AG}{AD}=\frac{AF}{AC}\quad\text{即}\quad
    \frac{EG}{4}= = \frac59,\]
    解得 $EG=\dfrac{20}9$.
</p>
</mysolution>
</p>
<p><myexample>
<p>如图所示, 在四棱锥 $S\text{--}ABCD$ 中, 底面 $ABCD$ 为平行四边形, 点 $E$ 是 $SA$ 上一点. 若 $SC\parallel\text{平面\ }EBD$, 求 $\dfrac{SE}{SA}$ 的值.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0525-2310-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>连接 $AC$, 设其与 $BD$ 的交点为 $F$, 则点 $F$ 为 $AC$ 中点. 再连接 $EF$, 因为 $SC\parallel\text{平面\ }EBD$, 所以 $EF\parallel SC$, 表明点 $E$ 为 $AS$ 中点, 故 $\dfrac{SE}{SA}= \dfrac12$.
</p>
</mysolution>
</p>
<p><myexample>
<p>在正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 点 $E$, $F$, $E_1$, $F_1$ 分别是棱 $AB$, $AD$, $B_1C_1$, $C_1D_1$ 的中点, 求证: $EF\parallel E_1F_1$ 且 $EF= E_1F_1$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0525-2320-crop}
    </center>
</p>
</myexample>
<myproof>
    <p>连接 $BD$ 和 $B_1D_1$. 显然, $EF$ 和 $E_1F_1$ 分别为 $\triangle ABD$ 和 $\triangle C_1B_1D_1$ 的中位线, 所以
    \[EF\parallel BD,\ EF=\frac12BD,\quad 
    E_1F_1\parallel B_1D_1,\ E_1F_1=\frac12B_1D_1.\]
    因为在正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, $BB_1\parallel DD_1$ 且 $BB_1= DD_1$, 所以四边形 $BB_1D_1D$ 为平行四边形, 而 $BD\parallel B_1D_1$ 且 $BD= B_1D_1$. 由此可知, $EF\parallel E_1F_1$ 且 $EF= E_1F_1$.
</p>
</myproof>

<p>线面平行性质定理: 一条直线与一个平面平行, 则过这条直线的任一平面与此平面的交线平行于该直线.
</p>
<p>对应的符号语言 (如图 \ref{fig-190630-1900}): $a\parallel\alpha$,  $a\subset\beta$, $\alpha\cap\beta= b$ $\Rightarrow$ $a\parallel b$.
</p>
<p>面面平行性质定理: 如果两个平行平面同时和第三个平面相交, 那么它们的交线平行.
</p>
<p>对应的符号语言 (如图 \ref{fig-190630-1910}): $\alpha\parallel\beta$, $\alpha\cap\gamma= a$, $\beta\cap\gamma= b$ $\Rightarrow$ $a\parallel b$.
</p>
<p>\begin{figure}[htb]
    \small
    \centering
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[line cap=round,line join=round,scale=0.6]
        \draw (-2.796,-1.386)-- (-1.095,-1.421);
        \draw (-2.796,-1.386)-- (-4.674,1.732);
        \draw (-2.796,-1.386)-- (-0.280,0.598);
        \draw (-4.674,1.732)-- (-2.158,3.716);
        \draw (-2.158,3.716)-- (-0.280,0.598);
        \draw [densely dashed] (-2.973,1.697)-- (-4.674,1.732);
        \draw [densely dashed] (-2.973,1.697)-- (-1.657,-0.488);
        \draw (-1.657,-0.488)-- (-1.095,-1.421);
        \draw (-1.220,0.617)-- (-2.499,2.741);
</p>
<p>\draw (-1.5,-1.2) node {$\alpha$};
        \draw (-4.107,-0.163) node {$b$};
        \draw (-0.8,0.581) node {$\beta$};
        \draw (-2.158,1.289) node {$a$};
      \end{tikzpicture}
      \caption{}\label{fig-190630-1900}
    \end{minipage}
    \hskip 0.5cm  
    \begin{minipage}[b]{0.45\linewidth}
      \centering
      \begin{tikzpicture}[line cap=round,line join=round,scale=0.6]
        \draw (-4.071,-1.421)-- (0.605,-1.385);
        \draw (-4.071,-1.421)-- (-2.689,0.031);
        \draw (-2.122,-2.625)-- (-1.449,2.724);
        \draw (-1.449,2.724)-- (0.144,4.176);
        \draw (-3.717,0.881)-- (0.959,0.9175);
        \draw (0.959,0.9175)-- (2.341,2.369);
        \draw (-2.335,2.334)-- (-3.717,0.881);
        \draw (1.987,0.066)-- (0.605,-1.385);
        \draw (-1.679,0.897)-- (-0.084,2.351);
        \draw (-1.969,-1.405)-- (-0.374,0.048);
        \draw[densely dashed] (-1.497,2.340)-- (-0.084,2.351);
        \draw[densely dashed] (-0.084,2.351)-- (-0.266,0.907);
        \draw[densely dashed] (-0.374,0.048)-- (-0.528,-1.173);
        \draw[densely dashed] (-0.528,-1.173)-- (-0.772,-1.396);
        \draw (0.144,4.176)-- (-0.084,2.351);
        \draw (-0.266,0.907)-- (-0.374,0.048);
        \draw[densely dashed] (-0.374,0.048)-- (-1.787,0.038);
        \draw (-1.497,2.340)-- (-2.335,2.3344);
        \draw (-0.084,2.3515)-- (2.341,2.369);
        \draw (1.987,0.0666)-- (-0.374,0.048);
        \draw (-1.787,0.038)-- (-2.6896,0.031);
        \draw (-0.772,-1.396)-- (-2.122,-2.625);
</p>
<p></p>
<p>\draw (-3.2,-1.1) node {$\alpha$};
        \draw (-2.8,1.3) node {$\beta$};
        \draw (-0.3,3.2) node {$\gamma$};
        \draw (-0.457,1.5) node {$b$};
        \draw (-0.81,-0.8) node {$a$};
      \end{tikzpicture}
      \caption{}\label{fig-190630-1910}
    \end{minipage}
    \end{figure}
</p>
<p></p>
<p><myexample>
<p>一个几何体的平面展开图如图所示 (顶点 $P$ 在展开图中分别为点 $P_1$, $P_2$, $P_3$, $P_4$), 其中四边形 $ABCD$ 为正方形, 点 $E$, $F$ 分别为 $P_4B$, $P_1C$ 的中点. 关于此几何体, 判断下列结论正确与否:
</p>
<p>(1) 直线 $AE$ 与直线 $BF$ 异面;
</p>
<p>(2) 直线 $AE$ 与直线 $DF$ 异面;
</p>
<p>(3) 直线 $EF\parallel\text{平面\ }PAD$;
</p>
<p>(4) 直线 $EF\parallel\text{平面\ }ABCD$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0602-2300-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0602-2310-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>该几何体为四棱锥 $P\text{--}ABCD$. 作图可以看出, $AE$ 与 $BF$ 不相交且不平行 (均可用反证法说明), 所以必然异面. 结论 (1) 正确.
</p>
<p>因为点 $E$, $F$ 分别为 $PB$, $PC$ 的中点, 所以 $EF$ 为 $\triangle PBC$ 的中位线, $EF\parallel BC$. 从而直线 $EF\parallel\text{平面\ }ABCD$, 结论 (4) 正确.
</p>
<p>又因为 $BC\parallel AD$, 所以 $EF\parallel AD$, 故直线 $EF\parallel\text{平面\ }PAD$, 结论 (3) 正确.
</p>
<p>由 $EF\parallel AD$ 知 $AE$ 与 $DF$ 共面. 结论 (2) 错误.
</p>
</mysolution>
</p>
<p><myexample>
<p>如图, 正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 点 $M$, $N$ 分别是 $AB$, $A_1D_1$ 的中点. 判断 $MN$ 与平面 $BB_1D_1D$ 的位置关系, 并说明理由.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0602-2320-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0602-2325-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>$MN\parallel$ 平面 $BB_1D_1D$. 理由如下:
</p>
<p>连接 $A_1C_1$ 与 $B_1D_1$ 交于点 $O_1$, 则点 $O_1$ 为 $B_1D_1$ 中点, 再连接 $BO_1$, $NO_1$. 因为 $N$ 为 $A_1D_1$ 中点, 所以
    \[NO_1\parallel A_1B_1\parallel MB,\quad
    NO_1= \frac12 A_1B_1= MB,\]
    则四边形 $MBO_1N$ 为平行四边形. 由此可知 $MN\parallel BO_1$, 而 $MN\parallel$ 平面 $BB_1D_1D$.
</p>
</mysolution>
</p>
<p><myexample>
<p>如图, 在棱长为 $2$ 的正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 点 $E$, $F$ 分别是棱 $DD_1$, $C_1D_1$ 的中点, 证明: $B_1F\parallel$ 平面 $A_1BE$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0602-2330-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0602-2335-crop}
    </center>
</p>
</myexample>
<myproof>
    <p>连接 $AB_1$ 交 $A_1B$ 于点 $O$, 则 $O$ 为 $AB_1$ 的中点, 再连接 $OE$, $EF$, $C_1D$. 因为点 $E$, $F$ 分别是棱 $DD_1$, $C_1D_1$ 的中点, 所以
    \[EF=\frac12 C_1D,\quad EF\parallel C_1D.\]
    因为 $AD=B_1C_1$, $AD\parallel B_1C_1$, 所以四边形 $ADC_1B_1$ 为平行四边形, 而 $AB_1=DC_1$, $AB_1\parallel DC_1$. 结合点 $O$ 为 $AB_1$ 的中点知, 
    \[\begin{gathered}
        EF= \frac12 C_1D= \frac12 B_1A= B_1O,\\
        EF\parallel C_1D\parallel B_1O,
    \end{gathered}\]
    所以四边形 $B_1OEF$ 为平行四边形, 且 $B_1F\parallel OE$, 因此 $B_1F\parallel$ 平面 $A_1BE$.
</p>
</myproof>
</p>
<p><myexample>
<p>如图所示, 在三棱柱 $ABC\text{--}A_1B_1C_1$ 中, 点 $D$, $E$ 分别是棱$CC_1$, $AB$ 的中点, 证明: $DE\parallel\text{平面 }AB_1C_1$.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0602-2340-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0602-2345-crop}
    </center>
</p>
</myexample>
<myproof>
    <p>取 $AB_1$ 的中点 $O$, 连接 $OC_1$, $OE$. 可以证明 (自行补全过程)
    \[\begin{gathered}
        OE= \frac12 BB_1= \frac12 CC_1= C_1D,\\
        OE\parallel BB_1\parallel C_1D,
    \end{gathered}\]
    所以四边形 $OEDC_1$ 为平行四边形, 且 $C_1O\parallel DE$, 因此 $DE\parallel\text{平面 }AB_1C_1$.
</p>
</myproof>

<myexample>
<p>正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中的边长为 $2$, 点 $E$ 为 $AD$ 的中点, 点 $F$ 在 $CC_1$ 上. 若 $EF\parallel \text{平面 }AB_1C$, 求 $EF$ 的大小.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0603-0010-crop}\qquad\qquad
        \includegraphics[scale=1.5]{2021-0603-0015-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>由图可知, 平面 $AEF$ 必与平面 $AB_1C$ 相交, 设交线为 $AG$ 且点 $G$ 在 $B_1C$ 上, 再连接 $GF$. 因为 $EF\parallel \text{平面 }AB_1C$, 所以 $EF\parallel AG$. 又因为平面 $ADD_1A_1\parallel$ 平面 $BCC_1B_1$, 所以 $AE\parallel GF$, 则四边形 $AEFG$ 为平行四边形, 且 
    \[FG=AE=\dfrac12 AD=1.\]
    由 $AE\parallel B_1C_1$ 知 $B_1C_1\parallel GF$, 所以点 $F$ 为 $CC_1$ 的中点. 连接 $EC$, 考虑 $\mathrm{Rt}\triangle ECF$ 可知 (自行补全过程),
    \[EF= \sqrt{EC^2+CF^2}= \sqrt{6}.\]
</p>
</mysolution>

<myexample>
<p>如左图所示, 在四棱锥 $P\text{--}ABCD$ 中, 底面 $ABCD$ 是边长为 $2$ 的正方形, $\angle PAD= \angle PAB = 90^\circ$, $PA= 2\sqrt{2}$, 点 $E$ 和 $F$ 分别是 $CD$ 和 $PB$ 的中点, 
</p>
<p>(1) 求证: 直线 $EF\parallel$ 平面 $PAD$;
</p>
<p>(2) 求直线 $PC$ 与平面 $ABCD$ 所成角的大小.
</p>
<p><center>
        \includegraphics[scale=1.5]{2021-0701-2100-1-crop}\qquad
        \includegraphics[scale=1.5]{2021-0701-2100-2-crop}
    </center>
</p>
</myexample>
<mysolution>
    <p>(1) 如右图所示, 取 $PA$ 中点 $G$, 连接 $GD$, $GF$. 因为点 $F$ 是 $PB$ 的中点, 所以 $GF\parallel AB$ 且 $GF=\dfrac12 AB$. 又因为点 $E$ 是正方形 $ABCD$ 中 $CD$ 的中点, 所以 $DE\parallel AB$ 且 $DE=\dfrac12 AB$. 从而 $DE\parallel GF$ 且 $DE= GF$, 四边形 $DEFG$ 是平行四边形. 由此可得 $EF\parallel DA$, 故直线 $EF\parallel$ 平面 $PAD$.
</p>
<p>(2) 因为 $\angle PAD= \angle PAB = 90^\circ$, 所以 $PA\perp AD$, $PA\perp AB$, 则 $PA\perp$ 平面 $ABCD$, $PA\perp AC$ 且 $\angle PCA$ 为直线 $PC$ 与平面 $ABCD$ 所成角. 因为正方形 $ABCD$ 的边长为 $2$, 所以 $AC=2\sqrt2$. 结合 $PA= 2\sqrt{2}$ 可知, $\angle PCA= 45^\circ$.
</p>
</mysolution>

