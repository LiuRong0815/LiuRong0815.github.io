\sectioncounter{37}
</p>

<p>
\section{空间向量}
</p>

<p>
\subsection{知识梳理}
</p>

<p>
空间直角坐标系在平面直角坐标系的基础上增加了 $z$ 轴, 通过 $3$ 个分量确定空间中一点的坐标. 通常将 $x$ 轴与 $y$ 轴水平放置, $z$ 轴向上而成为右手系, 所以 $z$ 轴也称为竖轴.
</p>

<p>
空间向量的运算与平面向量的运算基本相同. 与平面向量基本定理相对应的是空间向量基本定理: 取空间中不共面的 $3$ 个向量, 任意空间向量都可以分解为这 $3$ 个向量的线性组合. 用符号表述就是, 设向量 $\bm{i}, \bm{j}, \bm{k}$ 不共面, 对任意向量 $\bm{v}$, 存在与之对应的常数 $r,s,t$, 使得
\[\bm{v}= r\bm{i}+ s\bm{j}+ t\bm{k}.\]
</p>

<p>
将空间向量平移, 使其起点与原点重合, 则终点的坐标称为向量的坐标. 空间向量也有对应的坐标运算, 只需注意是 $3$ 个分量参与运算. 利用空间向量可以较方便地判断直线与平面的位置关系, 和计算线面距离.
</p>

<p>
直线的方向用其方向向量直接描述: 在直线 $l$ 上取两点 $A,B$, 则 $\overrightarrow{AB}$ 称为 $l$ 的方向向量. 平面的方向用其法向量间接描述: 在平面 $\alpha$ 内取两个不共线的向量 $\bm{a}, \bm{b}$, 则与 $\bm{a}, \bm{b}$ 垂直的空间向量 $\bm{n}$ 称为 $\alpha$ 的法向量. 从定义可以看出, 计算平面的法向量需要求解仅含两个方程的三元一次方程组, 实际计算时可以将某个分量视为常数.
</p>

<p>
设直线 $l_1, l_2$ 的方向向量分别为 $\bm{s}_1, \bm{s}_2$, 平面 $\alpha_1, \alpha_2$ 的法向量分别为 $\bm{n}_1, \bm{n}_2$, 则 (结合图形记忆)
\[\begin{gathered}
    l_1\parallel l_2 \Leftrightarrow \bm{s}_1\parallel \bm{s}_2,\quad
    l_1\perp l_2 \Leftrightarrow \bm{s}_1\perp \bm{s}_2,\\
    l_1\parallel \alpha_1 \Leftrightarrow \bm{s}_1\perp \bm{n}_1,\quad
    l_1\perp \alpha_1 \Leftrightarrow \bm{s}_1\parallel \bm{n}_1,\\
    \alpha_1\parallel \alpha_2 \Leftrightarrow \bm{n}_1\parallel \bm{n}_2,\quad
    \alpha_1\perp \alpha_2 \Leftrightarrow \bm{n}_1\perp \bm{n}_2,\\
\end{gathered}\]
此外, $l_1$ 与 $l_2$ 所成的角 (不超过 $90^\circ$) 为 $\bm{s}_1$ 与 $\bm{s}_2$ 的夹角 (或其补角), $l_1$ 与 $\alpha_1$ 所成的角 (不超过 $90^\circ$) 的余角为 $\bm{s}_1$ 与 $\bm{n}_2$ 的夹角 (或其补角), $\alpha_1$ 与 $\alpha_2$ 所成的二面角大小为 $\bm{n}_1$ 与 $\bm{n}_2$ 的夹角 (或其补角).
</p>

<p>
计算点到直线、点到平面、平行线之间、平行平面之间的距离, 都可以转化为计算向量的射影. 例如, 若计算点 $A$ 到直线 $l$ 的距离, 并设 $AD\perp l$ 于点 $D$, $l$ 的方向向量为 $\bm{v}$. 先任取 $l$ 上一点 $P$, 则 $\overrightarrow{PA}$ 在 $\bm{v}$ 上的射影大小 $|PD|= \dfrac{|\overrightarrow{PA}\cdot\bm{v}|}{|\bm{v}|}$ (为什么?), 再由勾股定理即可算出所求距离 $|AD|$. 有时计算点到平面的距离用等体积法更方便.
</p>

<p>
\lianxi
<myexercise>
    <p>    设 $\bm{a}= (2,1,3)$, $\bm{b}= (-4,2,x)$, 且 $\bm{a}\perp \bm{b}$, 求 $x$ 的值.
</p>
</myexercise>
<mysolution>
    <p>
    $\bm{a}\cdot \bm{b}= -8+2+3x=0$, $x=2$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设 $A(1,0,2)$, $B(1,-3,1)$, 点 $M$ 在 $z$ 轴上且 $|MA|= |MB|$, 求 $M$ 的坐标.
</p>
</myexercise>
<mysolution>
    <p>
    设 $M(0,0,m)$, 则
    \[1^2+0^2+(m-2)^2= 1^2+(-3)^2+(m-1)^2,\]
    解得 $m=-3$, 即 $M(0,0,-3)$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, $M, N$ 分别为棱 $B_1B$, $C_1C$ 的中点, 求 $DM$ 与 $A_1N$ 所成角的余弦值.
</p>
</myexercise>
<mysolution>
    <p>
    以 $D$ 为原点, $DA, DC, DD_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系. 设正方体棱长为 $2$, 则
    \[\begin{gathered}
        M(2,2,1),\quad N(0,2,1),\quad A(2,0,2),\\
        \overrightarrow{DM}= (2,2,1),\quad
        \overrightarrow{A_1N}= (-2,2,-1),
    \end{gathered}\]
    所求余弦值为
    \[\frac{|\overrightarrow{DM}\cdot\overrightarrow{A_1N}|}{|\overrightarrow{DM}||\overrightarrow{A_1N}|}
    = \frac{1}{3\cdot 3}= \frac19.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    在三棱锥 $O\text{--}ABC$ 中, $OA, OB, OC$ 两两垂直, $OA=OB= 2$, $OC=3$, 求点 $O$ 到平面 $ABC$ 的距离.
</p>
</myexercise>
<mysolution>
    <p>
    方法一: 设所求距离为 $h$, 则由 $V_{O\text{--}ABC}= V_{C\text{--}AOB}$ 知
    \mymarginpar{方法一为等体积法.}
    \[\frac13 S_{\triangle ABC}\cdot h
    = \frac13 OC\cdot \frac12 OA\cdot OB,\]
    解得 $h= \dfrac6{S_{\triangle ABC}}$. 由题意, $AB=2\sqrt2$, $AC=BC=\sqrt{13}$, 则 $\triangle ABC$ 中 $AB$ 边上的高为 $\sqrt{11}$, 所以
    \[\begin{gathered}
        S_{\triangle ABC}= \frac12 AB\cdot \sqrt{11}= \sqrt{22},\\
        h= \frac{6}{\sqrt{22}}= \frac{3\sqrt{22}}{11}.
    \end{gathered}\]
</p>

<p>
    方法二: 以 $O$ 为原点, $OA, OB, OC$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        A(2,0,0),\quad B(0,2,0),\quad C(0,0,3),\\
        \overrightarrow{AB}= (-2,2,0),\quad
        \overrightarrow{AC}= (-2,0,3).
    \end{gathered}\]
    设平面 $ABC$ 的法向量为 $\bm{n}= (r,s,t)$, 则 $\overrightarrow{AB}\perp \bm{n}$, $\overrightarrow{AC}\perp \bm{n}$, 即
    \[\left\{\!\!\begin{array}{l}
        -2r+2s= 0,\\
        -2r+3t=0,
    \end{array}\right.\quad
    \left\{\!\!\begin{array}{l}
        s= r,\\
        3t= 2r.
    \end{array}\right.\]
    取 $\bm{n}= (3,3,2)$, 所求距离为
    \[\frac{|\overrightarrow{OA}\cdot \bm{n}|}{\bm{n}}
    = \frac{6}{\sqrt{22}}= \frac{3\sqrt{22}}{11}.\]
</p>
</mysolution>
</p>

<p>
\subsection{要点导学\quad 各个击破}
\subsubsection{线面垂直与平行}
<span id="example-"></span>
<myexample>
    <p>
    设四面体 $P\text{--}ABC$ 的 $3$ 组对棱的中点连线段长度相等, 求证: 该四面体相对的棱互相垂直.
</p>
</myexample>
<mysolution>
    <p>
    设 $PA, PB$ 的中点分别为 $D,E$, $BC, AC$ 的中点分别为 $M,N$.
</p>

<p>
    方法一: 设 $\overrightarrow{PA}= \bm{a}$, $\overrightarrow{PB}= \bm{b}$, $\overrightarrow{PC}= \bm{c}$, 则
    \[\begin{gathered}
        \overrightarrow{DM}
        = \overrightarrow{PM}- \overrightarrow{PD}
        = \frac12(\bm{b}+ \bm{c})- \frac12\bm{a},\\
        \overrightarrow{EN}
        = \overrightarrow{PN}- \overrightarrow{PE}
        = \frac12(\bm{a}+ \bm{c})- \frac12\bm{b}.
    \end{gathered}\]
    由已知, $|\overrightarrow{DM}|= |\overrightarrow{EN}|$, 则
    \[\begin{gathered}
        |\bm{b}+ \bm{c}-\bm{a}|= |\bm{a}+ \bm{c}- \bm{b}|,\\
        |\bm{c}+ (\bm{b}-\bm{a})|= |\bm{c}- (\bm{b}-\bm{a})|,
    \end{gathered}\]
    平方后展开并整理,
    \[\bm{c}\cdot (\bm{b}-\bm{a})= 0,\quad
    \overrightarrow{PC}\cdot \overrightarrow{AB}= 0,\]
    所以 $PC\perp AB$. 同理可证另外两组对棱互相垂直.
</p>

<p>
    方法二: 由中位线定理,
    \[DE\parallel AB\parallel MN,\quad
    DE= \frac12 AB= NM,\]
    所以四边形 $DEMN$ 为平行四边形. 结合 $DM= EN$ 知, 四边形 $DEMN$ 为矩形, 则 $DE\perp EM$, 故 $PC\perp AB$. 结论同上.
</p>
</mysolution>
</p>

<p>
<span id="example-"></span>
<myexample>
    <p>
    设正方体 $ABCD\text{--}A_1B_1C_1$ 的棱 $AA_1$ 的中点为 $M$, 问对角线 $BD_1$ 上是否存在点 $N$ 使得 $MN\parallel$ 平面 $AB_1C$?
</p>
</myexample>
<mysolution>
    <p>
    以 $D$ 为原点, $DA, DC, DD_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系. 设正方体棱长为 $2a$, 则
    \[\begin{gathered}
        A(2a,0,0),\quad B(2a,2a,0),\quad C(0,2a,0),\\
        B_1(2a,2a,2a),\quad D_1(0,0,2a),\quad M(2a,0,a),\\
        \overrightarrow{AC}= (-2a,2a,0),\quad
        \overrightarrow{AB_1}= (0,2a,2a),\quad
        \overrightarrow{BD_1}= (-2a,-2a,2a),
    \end{gathered}\]
    因此 $\overrightarrow{AC}\cdot \overrightarrow{BD_1}= \overrightarrow{AB_1}\cdot \overrightarrow{BD_1}= 0$, 表明 $\overrightarrow{BD_1}$ 为平面 $AB_1C$ 的法向量. 由点 $N$ 在对角线 $BD_1$ 上可设 $\overrightarrow{BN}= \lambda \overrightarrow{BD_1}$, $\lambda\in [0,1]$, 则
    \mymarginpar{在确定点 $N$ 的坐标时, 要利用向量共线.}
    \[\begin{gathered}
        \overrightarrow{DN}- \overrightarrow{DB}
        = \lambda (-2a,-2a,2a),\\
        \overrightarrow{DN}
        = ((1-\lambda)2a,(1-\lambda)2a,2\lambda a).
    \end{gathered}\]
    若 $MN\parallel$ 平面 $AB_1C$, 则 $\overrightarrow{MN}\perp \overrightarrow{BD_1}$, $\overrightarrow{MN}\cdot \overrightarrow{BD_1}= 0$, 即
    \[\begin{gathered}
        (\overrightarrow{DN}- \overrightarrow{DM})\cdot \overrightarrow{BD_1}= 0,\\
        (-2\lambda a,(1-\lambda)2a,(2\lambda-1)a)\cdot (-2a,-2a,2a)= 0,
    \end{gathered}\]
    解得 $\lambda= \dfrac12$. 故存在所求的点 $N$, 且 $N$ 为 $BD_1$ 的中点.
</p>
</mysolution>
</p>

<p>
    % \begin{figure}[htb]
    % \small
    % \centering
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \hskip 0.5cm  
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \end{figure}
</p>

<p>
\lianxi
\begin{exercise}[s]
    在长方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, $AB=2$, $BC=CC_1= 1$, $E$ 是 $CD$ 的中点, 求证: $B_1E\perp$ 平面 $AED_1$.
</p>
</myexercise>
<mysolution>
    <p>
    以 $D$ 为原点, $DA, DC, DD_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        A(1,0,0),\quad E(0,1,0),\quad D_1(0,0,1),\quad B_1(1,2,1),\\
        \overrightarrow{EB_1}= (1,1,1),\quad
        \overrightarrow{AE}= (-1,1,0),\quad
        \overrightarrow{AD_1}= (-1,0,1),\\
        \overrightarrow{EB_1}\cdot \overrightarrow{AE}= 0
        = \overrightarrow{EB_1}\cdot \overrightarrow{AD_1},
    \end{gathered}\]
    表明 $B_1E\perp AE$ 且 $B_1E\perp AD_1$. 故 $B_1E\perp$ 平面 $AED_1$.
</p>
</mysolution>
</p>

<p>
\subsubsection{线面夹角}
<span id="example-"></span>
<myexample>
    <p>
    已知正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, 棱 $B_1C_1$ 的中点为 $M$, 点 $N$ 在棱 $AA_1$ 上且 $AN: NA_1= 1:3$, 求平面 $ABCD$ 与平面 $BMN$ 夹角的余弦值.
</p>
</myexample>
<mysolution>
    <p>
    以 $B$ 为原点, $BC, BA, BB_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系. 设正方体棱长为 $4a$, 则
    \[\overrightarrow{BM}= (2a,0,4a),\quad
    \overrightarrow{BN}= (0,4a,a).\]
    设平面 $BMN$ 的法向量 $\bm{n}_1= (r,s,t)$, 则 $\bm{n}_1\cdot \overrightarrow{BM}= \bm{n}_1\cdot \overrightarrow{BN}= 0$, 即
    \[\left\{\!\!\begin{array}{l}
        2ar+ 4at= 0,\\
        4as+ at= 0,
    \end{array}\right.\quad
    \left\{\!\!\begin{array}{l}
        r= -2t,\\
        4s= -t,
    \end{array}\right.\]
    可取 $\bm{n}_1= (8,1,-4)$. 取平面 $ABCD$ 的法向量 $\bm{n}_2= (0,0,1)$, 则所求余弦值为
    \[\frac{|\bm{n}_1\cdot \bm{n}_2|}{|\bm{n}_1| |\bm{n}_2|}
    = \frac4{9\cdot 1}= \frac49.\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    在三棱锥 $A\text{--}BCD$ 中, $AB=AC=BD=CD=3$, $AD=BC=2$, $M,N$ 分别是棱 $AD, BC$ 的中点, 求异面直线 $AN,CM$ 所成角的余弦值.
</p>
</myexercise>
<mysolution>
    <p>
    设 $\overrightarrow{AB}= \bm{b}$, $\overrightarrow{AC}= \bm{c}$, $\overrightarrow{AD}= \bm{d}$, 则
    \mymarginpar{此题不便于建立空间直角坐标系, 但可借助空间向量基本定理, 利用建系的想法, 将所有向量用基向量 $\bm{b},\bm{c},\bm{d}$ 表示.}
    \[\overrightarrow{BC}= \bm{c}-\bm{b},\quad 
    \overrightarrow{CD}= \bm{d}-\bm{c},\quad 
    \overrightarrow{DB}= \bm{b}-\bm{d}.\]
    由 $|\overrightarrow{BC}|= 2$ 知 $|\bm{c}= \bm{b}|= 2$, 平方并整理
    \[|\bm{c}|^2- 2\bm{c}\cdot\bm{d}+ |\bm{b}|^2= 4,\quad
    \bm{b}\cdot \bm{c}= 7.\]
    同理可得 $\bm{d}\cdot\bm{c}= \bm{b}\cdot\bm{d}= 2$. 因为
    \[\overrightarrow{AN}= \frac12(\bm{b}+\bm{c}),\quad
    \overrightarrow{CM}= \frac12\bm{d}- \bm{c},\]
    所以
    \[\begin{gathered}
        |\overrightarrow{AN}|^2
        = \frac14(|\bm{b}|^2+ 2\bm{b}\cdot\bm{c}+ |\bm{c}|^2)= 8,\\
        |\overrightarrow{CM}|^2
        = \frac14|\bm{d}|^2- \bm{d}\cdot\bm{c}+ |\bm{c}|^2= 8,\\
        \overrightarrow{AN}\cdot \overrightarrow{CM}
        = \frac14(\bm{b}\cdot\bm{d}+ \bm{c}\cdot\bm{d}
            - 2\bm{b}\cdot\bm{c}- 2|\bm{c}|^2)= -7.
    \end{gathered}\]
    所求的余弦值为
    \[\frac{|\overrightarrow{AN}\cdot \overrightarrow{CM}|}{
        |\overrightarrow{AN}| |\overrightarrow{CM}|}
    = \frac{7}{\sqrt8\cdot \sqrt8}= \frac78.\]
</p>
</mysolution>
</p>

<p>
    % \begin{figure}[htb]
    % \small
    % \centering
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \hskip 0.5cm  
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \end{figure}
</p>

<p>
\subsubsection{线面距离}
<span id="example-"></span>
<myexample>
    <p>
    已知正方体 $ABCD\text{--}A_1B_1C_1D_1$ 的棱长为 $2$, 棱 $CD$ 的中点为 $M$, 求点 $M$ 到平面 $AB_1C$ 的距离.
</p>
</myexample>
<mysolution>
    <p>
    以 $B$ 为原点, $BC, BA, BB_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        C(2,0,0),\quad A(0,2,0),\quad B_1(0,0,2),\\
        M(2,1,0),\quad \overrightarrow{CM}= (0,1,0).
    \end{gathered}\]
    设平面 $AB_1C$ 的法向量为 $\bm{n}= (r,s,t)$, 则
    \[\bm{n}\cdot \overrightarrow{AC}= 0
    = \bm{n}\cdot \overrightarrow{AB_1},\]
    解得 $r=s=t$, 取 $\bm{n}= (1,1,1)$. 所求距离为 $\overrightarrow{CM}$ 在 $\bm{n}$ 上射影的长度, 即
    \[\frac{|\overrightarrow{CM}\cdot \bm{n}|}{
        |\overrightarrow{CM}| |\bm{n}|}
    = \frac1{1\cdot \sqrt3}= \frac{\sqrt{3}}{3}.\]
</p>
</mysolution>
</p>

<p>
\lianxi
\begin{exercise}[s]
    已知正方体 $ABCD\text{--}A_1B_1C_1D_1$ 的棱长为 $2$, 棱 $DD_1, BB_1$ 的中点分别为 $E, F$, 求点 $E$ 到直线 $C_1F$ 的距离.
</p>
</myexercise>
<mysolution>
    <p>
    以 $B$ 为原点, $BC, BA, BB_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        E(2,2,1),\quad F(0,0,1),\quad C_1(2,0,2),\\
        \overrightarrow{FE}= (2,2,0),\quad 
        \overrightarrow{FC_1}= (2,0,1).
    \end{gathered}\]
    $\overrightarrow{FE}$ 在 $\overrightarrow{FC_1}$ 上射影的长度
    \[d= \frac{|\overrightarrow{FE}\cdot \overrightarrow{FC_1}|}{
        \overrightarrow{FC_1}}
    = \frac4{\sqrt5},\]
    则所求距离为
    \[\sqrt{|\overrightarrow{EF}|^2- d^2}= \frac{2\sqrt{30}}{5}.\]
</p>
</mysolution>
</p>

<p>
    % \begin{figure}[htb]
    % \small
    % \centering
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \hskip 0.5cm  
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \end{figure}
</p>

<p>
\subsubsection{课堂评价}
<myexercise>
    <p>    在长方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, $AB=2$, $BC=CC_1= 1$, $E,F$ 分别是 $CD, BC$ 的中点, 求证: 平面 $EAD_1\perp$ 平面 $EFD_1$.
</p>
</myexercise>
<mysolution>
    <p>
    以 $D$ 为原点, $DA, DC, DD_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        A(1,0,0),\quad E(0,1,0),\quad 
        D_1(0,0,1),\quad F\biggl(\frac12,2,0\biggr),\\
        \overrightarrow{AE}= (-1,1,0),\quad
        \overrightarrow{AD_1}= (-1,0,1),\quad
        \overrightarrow{EF}= \biggl(\frac12,1,0\biggr).
    \end{gathered}\]
    计算知, 平面 $EAD_1$ 的法向量 $\bm{n}_1$ 可取 $(1,1,1)$, 平面 $EFD_1$ 的法向量 $\bm{n}_2$ 可取 $(-2,1,1)$. 由 $\bm{n}_1\perp \bm{n}_2$ 知, 结论成立.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设正三棱柱 $ABC\text{--}A_1B_1C_1$ 的底面边长为 $a$, 侧棱长为 $\sqrt2a$, 求 $AC_1$ 与侧面 $ABB_1A_1$ 所成的角.
</p>
</myexercise>
<mysolution>
    <p>
    设 $AB, A_1B_1$ 的中点分别为 $D,D_1$, 则 $CD\perp AB$, $D_1D\perp$ 平面 $ABC$.
</p>

<p>
    方法一: 以 $D$ 为原点, $DC, DA, DD_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        A\biggl(0,\frac{a}2,0\biggr),\quad 
        C_1\biggl(\frac{\sqrt3}2 a,0, \sqrt2a\biggr),\quad
        \overrightarrow{AC_1}
        = \biggl(\frac{\sqrt3}2a,-\frac{a}2,\sqrt2 a\biggr).
    \end{gathered}\]
    可取侧面 $ABB_1A_1$ 的法向量 $\bm{n}= (1,0,0)$, 则所求角的正弦值为
    \[\frac{|\bm{n}\cdot \overrightarrow{AC_1}|}{
        |\bm{n}| |\overrightarrow{AC_1}|}
    = \frac{\sqrt3}{2}a\cdot \frac{1}{\sqrt3a}
    = \frac12,\]
    即所求角为 $30^\circ$.
</p>

<p>
    方法二: 连结 $C_1D_1, AD_1$, 则 $C_1D_1\perp$ 平面 $ABB_1A_1$, $\angle C_1AD_1$ 为所求角. 由 $A_1D_1= \dfrac{a}2$ 知,
    \[D_1C_1= \frac{\sqrt3}2 a,\quad D_1A= \frac32 a,\quad
    \tan\angle C_1AD_1= \frac{\sqrt3}{3},\]
    所以 $\angle C_1AD_1= 30^\circ$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知正方体 $ABCD\text{--}A_1B_1C_1D_1$ 的棱长为 $2$, 棱 $CD$ 的中点为 $E$, 正方形 $BCC_1B_1$ 的中心为 $O$, 求点 $O$ 到直线 $B_1E$ 的距离.
</p>
</myexercise>
<mysolution>
    <p>
    以 $B$ 为原点, $BC, BA, BB_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        B_1(0,0,2),\quad E(2,1,0),\quad O(1,0,1),\\
        \overrightarrow{B_1E}= (2,1,-2),\quad 
        \overrightarrow{B_1O}= (1,0,-1).
    \end{gathered}\]
    所以 $\overrightarrow{B_1O}$ 在 $\overrightarrow{B_1E}$ 上的射影大小
    \[l= \frac{|\overrightarrow{B_1D}\cdot \overrightarrow{B_1E}|}{|\overrightarrow{B_1E}|}
    = \frac43,\]
    由勾股定理, 所求距离为
    \[\sqrt{|\overrightarrow{B_1D}|^2- l^2}= \frac{\sqrt2}{3}.\]
</p>
</mysolution>
</p>

<p>
    % \begin{figure}[htb]
    % \small
    % \centering
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \hskip 0.5cm  
    % \begin{minipage}[b]{0.45\linewidth}
    %     \centering
</p>

<p>
    %     \caption{}\label{fig-}
    %   \end{minipage}
    % \end{figure}
</p>

<p>
\subsection{课后练习}
</p>

<p>
<myexercise>
    <p>    在直三棱柱 $ABC\text{--}A_1B_1C_1$ 中, $\angle ABC= 90^\circ$, $CB=1$, $CA=2$, $AA_1= \sqrt6$, 棱 $CC_1$ 的中点为 $M$, 求证: $AM\perp BA_1$.
</p>
</myexercise>
<mysolution>
    <p>
    以 $B$ 为原点, $BC, BA, BB_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[\begin{gathered}
        A(0,\sqrt3,0),\quad M\biggl(1,0,\frac{\sqrt6}2\biggr),\\
        \overrightarrow{AM}= \biggl(1,-\sqrt3,\frac{\sqrt6}2\biggr),\quad 
        \overrightarrow{BA_1}= (0,\sqrt3,\sqrt6).
    \end{gathered}\]
    所以 $\overrightarrow{AM}\cdot\overrightarrow{BA_1}= 0$, 即 $AM\perp BA_1$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    已知空间中三点 $A(0,2,3)$, $B(-2,1,6)$, $C(1,-1,5)$, 求以 $AB,AC$ 为邻边的平行四边形的面积.
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $\overrightarrow{AB}= (-2,-1,3)$, $\overrightarrow{AC}= (1,-3,2)$, 所以
    \mymarginpar{除了利用三角形面积定理, 也可以计算一点到对边的距离, 再利用三角形面积公式.}
    \[\cos\angle BAC= \frac{\overrightarrow{AB}\cdot \overrightarrow{AC}}{|\overrightarrow{AB}\cdot \overrightarrow{AC}|}
    = \frac{-2+3+6}{\sqrt{11}\cdot\sqrt{11}}= \frac12,\]
    则 $\sin\angle BAC= \dfrac{\sqrt3}2$, 所求面积为
    \[2S_{\triangle ABC}= 2\cdot\frac12 |\overrightarrow{AB}| |\overrightarrow{AC}| \sin\angle BAC
    = 7\sqrt3.\]
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设正三棱柱 $ABC\text{--}A_1B_1C_1$ 的侧棱长为 $2$, 底面边长为 $1$, 棱 $BC$ 的中点为 $M$. 侧棱 $CC_1$ 上是否存在一点 $N$ 使得 $MN\perp AB$?
</p>
</myexercise>
<mysolution>
    <p>
    取 $AC, A_1C_1$ 的中点, 分别记为 $D,D_1$, 则 $DD_1\perp$ 平面 $ABC$, $BD\perp AC$. 以 $D$ 为原点, $DB, DC, DD_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系, 则
    \[A\biggl(0, -\frac12, 0\biggr),\quad 
        B\biggl(\frac{\sqrt3}2, 0, 0\biggr),\quad
        M\biggl(\frac{\sqrt3}4, \frac14, 0\biggr).\]
    设 $N\biggl(0,\dfrac12,n\biggr)$, $n\in[0,2]$, 则
    \[\overrightarrow{MN}\cdot \overrightarrow{AB}
    = \biggl(-\frac{\sqrt3}4, \frac14, n\biggr)
        \cdot \biggl(\frac{\sqrt3}2, \frac12, 0\biggr)
    = -\frac14\neq 0,\]
    所以 $MN$ 与 $AB$ 不垂直, 即不存在符合题意的点 $N$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设平行六面体 $ABCD\text{--}A_1B_1C_1D_1$ 的底面 $ABCD$ 是边长为 $a$ 的正方形, 侧棱 $AA_1= b$, $\angle A_1AB= \angle A_1AD= 120^\circ$, 求 $AC_1$ 的长度.
</p>
</myexercise>
<mysolution>
    <p>
    设 $\overrightarrow{AB}= \bm{b}$, $\overrightarrow{AD}= \bm{d}$, $\overrightarrow{AA_1}= \bm{e}$, 则
    \mymarginpar{用单个字母表示向量可以简化表达式的形式. 解题时还用了 $3$ 个变量之和的完全平方公式.}
    \[\begin{aligned}
        \overrightarrow{AC_1}&= \bm{b}+\bm{d}+\bm{e},\\
        |\overrightarrow{AC_1}|^2
        &= |\bm{b}|^2+ |\bm{d}|^2+ |\bm{e}|^2+ 2\bm{b}\cdot\bm{d}
            + 2\bm{d}\cdot\bm{e}+ 2\bm{e}\cdot\bm{b},\\
        &= 2a^2+ b^2- 2ab,
    \end{aligned}\]
    所以 $|\overrightarrow{AC_1}|= \sqrt{2a^2+ b^2- 2ab}$.
</p>
</mysolution>
</p>

<p>
<myexercise>
    <p>    设两个单位向量 $\overrightarrow{OA}= (m,n,0)$, $\overrightarrow{OB}= (0,n,p)$ 与向量 $\overrightarrow{OC}= (1,1,1)$ 的夹角都为 $45^\circ$, 求 $\cos\angle AOB$ 的值. 
</p>
</myexercise>
<mysolution>
    <p>
    由已知, $\overrightarrow{OA}\cdot \overrightarrow{OC}= |\overrightarrow{OA}| |\overrightarrow{OC}|\cos 45^\circ$, 即
    \mymarginpar{此处也可写成
    \[m+n= 1\cdot \sqrt3\cdot \frac{\sqrt2}{2},\]
    仍应平方后算出 $4mn=1$.}
    \[m+n= \sqrt{m^2+n^2}\cdot \sqrt3\cdot \frac{\sqrt2}{2},\]
    平方并整理, $m^2+n^2= 4mn$. 由 $|\overrightarrow{OA}|= 1$ 知, $m^2+n^2= 1$, 则 $4mn=1$, 代入前一式知,
    \[\frac{1}{16n^2}+ n^2= 1,\quad n^2= \frac{2\pm\sqrt3}4.\]
    因此结合 $|\overrightarrow{OB}|= 1$ 知, 
    \[\cos\angle AOB
    = \frac{\overrightarrow{OA}\cdot \overrightarrow{OB}}{
        |\overrightarrow{OA}| |\overrightarrow{OB}|}
    = n^2= \frac{2\pm\sqrt3}4.\]
</p>
</mysolution>
</p>

<p>
    % \begin{figure}[htb]
    % \small
    % \centering
    % \begin{minipage}[b]{0.45\linewidth}
    %   \centering
</p>

<p>
    %   \caption{}\label{fig-}
    % \end{minipage}
    % \hskip 0.5cm
    % \begin{minipage}[b]{0.45\linewidth}
    %     \centering
</p>

<p>
    %     \caption{}\label{fig-}
    %   \end{minipage}
    % \end{figure}
</p>

<p>
<myexercise>
    <p>    在正方体 $ABCD\text{--}A_1B_1C_1D_1$ 中, $E,F$ 分别为棱 $BC, CD$ 上的动点, 且 $BE= CF$.
</p>

<p>
    (1) 求证: $B_1F\perp D_1E$;\qquad 
    (2) 当三棱锥 $C_1\text{--}CEF$ 的体积最大时, 求二面角 $C_1\text{--}EF\text{--}C$ 的平面角的余弦值.
</p>
</myexercise>
<mysolution>
    <p>
    (1) 以 $B$ 为原点, $BC, BA, BB_1$ 分别为 $x$ 轴、$y$ 轴和 $z$ 轴, 建立空间直角坐标系. 设正方体棱长为 $a$, $BE=b\in [0,a]$, 则
    \[\begin{gathered}
        E(b,0,0),\quad F(a,b,0),\quad 
        B_1(0,0,a),\quad D_1(a,a,a),\\
        \overrightarrow{B_1F}\cdot \overrightarrow{D_1E}
        = (a,b,-a)\cdot (a-b,a,a)= 0,
    \end{gathered}\]
    所以 $B_1F\perp D_1E$.
</p>

<p>
    (2) 三棱锥 $C_1\text{--}CEF$ 的体积
    \[V_{C_1\text{--}CEF}= \frac13 S_{\triangle CEF}\cdot CC_1
    = \frac16(a-b)ba.\]
    因为 $a$ 为定值, 所以当 $b= \dfrac{a}2$ 时, $(a-b)b$ 最大. 此时
    \[E\biggl(\frac{a}2,0,0\biggr),\quad
    F\biggl(a,\frac{a}2,0\biggr),\]
    而 $C_1(a,0,a)$, 则
    \[\overrightarrow{EF}= \biggl(\frac{a}2,\frac{a}2,0\biggr),\quad
    \overrightarrow{EC_1}= \biggl(\frac{a}2,0,a\biggr).\]
    设平面 $C_1EF$ 的法向量为 $\bm{n}_1= (r,s,t)$, 则
    \[\left\{\!\!\begin{array}{l}
        \overrightarrow{EF}\cdot\bm{n}_1= \frac{a}2(r+s)=0,\\[4pt]
        \overrightarrow{EC_1}\cdot\bm{n}_1= \frac{a}2(r+2t)=0,
    \end{array}\right.\quad
    \left\{\!\!\begin{array}{l}
        s= -r,\\
        2t= -r,
    \end{array}\right.\]
    故取 $\bm{n}_1= (-2,2,1)$. 因为平面 $CEF$ 的法向量 $\bm{n}_2$ 可取为 $(0,0,1)$, 且图中二面角的平面角为锐角, 所以所求余弦值为
    \[\frac{|\bm{n}_1\cdot\bm{n}_2|}{|\bm{n}_1| |\bm{n}_2|}
    = \frac{1}{3\cdot 1}= \frac13.\]
</p>
</mysolution>