\sectioncounter{8}
  \section{对数的定义与运算}
</p>

<p>
  \subsection{知识梳理}
    若 $a^x=b$, 则定义 $x=\log_a b$, 念作“$x$ 是以 $a$ 为底, $b$ 的\myindex{对数} (logarithm)”, 
    并称 $a$ 为底数, $b$ 为真数.“$\log_a$”是函数名, 代表了取对数运算, 
    类似于“$\sqrt{\phantom{2}}$”代表了开算术平方根运算. 当底数 $a$ 为 $10$ 时, 
    $\log_{10}$ 简记为  $\lg$, 运算结果称为<strong>常用对数</strong> (common logarithm),     而当 $a$ 为 $\mathrm{e}= 2.718\cdots$ (特殊常数) 时, 
    $\log_{\mathrm{e}}$ 简记为  $\ln$, 运算结果称为<strong>自然对数</strong> (natural logarithm). </p>

<p>
    定义表明, 对数运算实际上是“取指数”运算, 例如
    \[\log_2 8= \log_2 2^3= 3,\quad \log_2 32= \log_2 2^5= 5,\quad
      \log_2 \frac12= -1.\]
    特别地, $\log_a a=1$, $\log_a 1=0$. 在对数定义中, 还要求 $a>0$ 且 $a\neq 1$, $b>0$ (为什么?). 由定义容易知道, 
    \[a^{\log_a b}=b,\quad \log_a a^x=x,\]
    表明指数运算和对数运算恰为互逆的运算. 
</p>

<p>
    用指数的运算律可以验证对数有如下运算律:
    \mymarginpar{对数运算律中没有两个对数的乘除法, 如若遇到, 一般需用下面介绍的换底公式化为常用对数或自然对数.}
    \[\log_a b+ \log_a c= \log_a (bc),\quad 
      \log_a b- \log_a c= \log_a \frac{b}c,\quad
      c\log_a b= \log_a b^c.\]
    例如对第一式, 根据对数定义可设 $b= a^x$, $c= a^y$, 则左右两边都为 $x+y$. 
    同理可验证后两式. 第三式中, 取 $c$ 为正整数时, 此式也可看作第一式的推论.
    还可以验证
     \[{\log_c a}\cdot\log_a b= \log_c b,\quad 
       \text{即\ }\log_a b= \frac{\log_c b}{\log_c a},\]
    上面后一式叫做换底公式. 使用换底公式时, 
    \mymarginpar{对数运算律和换底公式都可以逆用, 例如 
      \[\begin{aligned}
        \lg 12&= 2\lg2+\lg3,\\
        \ln 1.2&= \ln2+\ln3-\ln5.\end{aligned}\]}
    通常换成自然对数或常用对数. 这组公式可类比分式运算来记忆, 也就是
    \[\frac{a}c\cdot \frac{b}a= \frac{b}c,\quad
      \text{即\ }\frac{b}a= \frac{b/c}{a/c}.\]
</p>

<p>
  \lianxi
  <myexercise>
    <p>    计算: $\log_2 \sqrt2$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $\log_2 \sqrt2 = \log_2 2^{\frac12}= \frac12$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    计算: $2\lg\sqrt2 +\lg5$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $= \lg2+\lg5 =\lg10=1$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    计算: $\log_2 9\cdot \log_3 4$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $=\frac{\ln9}{\ln2}\cdot \frac{\ln4}{\ln3}
      =\frac{2\ln3}{\ln2}\cdot \frac{2\ln2}{\ln3}= 4$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    解关于 $x$ 的方程 $\lg x+\lg(x+3)=1$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $\lg x(x+3)=\lg 10$, 则 $x(x+3)=10$, 
    \mymarginpar{对数式中真数为正, 故对数方程需要检验.}
    解得 $x=2$ 或 $-5$. 但 $x>0$, 故 $x=2$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知 $\lg2=a$, $\lg3=b$, 用 $a$, $b$ 表示 $\lg\frac{18}{25}$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $\lg\frac{18}{25}= \lg2+2\lg3-2\lg5$, 
    \mymarginpar{一般化, $\log_{ab}a+ \log_{ab}b=1$.}
    而 $\lg2+\lg5=1$ 即 $\lg5=1-a$, 所以 $\lg\frac{18}{25}=3a+2b-2$.
  </p>
</mysolution>
</p>

<p>
  \subsection{要点导学\quad 各个击破}
  \subsubsection{对数式的计算}
  <span id="example-"></span>
<myexample>
    <p>
    计算: (1)  $2\lg2-\lg\frac1{25}$;
</p>

<p>
    (2) $(\log_3 2+\log_9 2)(\log_4 3+\log_8 3)$.
  </p>
</myexample>
</p>

<p>
  <mysolution>
    <p>
    (1) 原式 $=2\lg2+2\lg5=2$; (2) 用换底公式可算得 $\frac54$.
  </p>
</mysolution>
</p>

<p>
  \lianxi
  \begin{exercise}[s]
    计算: (1) $27^{\frac23}- 2^{\log_2 3}\cdot \log_2{\frac18}+ 2\lg\sqrt{10}$;
</p>

<p>
    (2) $\log_3 27+ \lg40+ \lg 25- \ln\mathrm{e}^2$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    (1) 原式 $=9-3\cdot(-3)+\lg10=19$;
</p>

<p>
    (2) 原式 $=3+2\lg2+1+2\lg5-2= 4$.
  </p>
</mysolution>
</p>

<p>
  \subsubsection{指数式与对数式的相互转化}
  <span id="example-"></span>
<myexample>
    <p>
    已知 $3^a =5^b =c$, 且 $\frac1a + \frac1b =2$, 求 $c$ 的值.
  </p>
</myexample>
</p>

<p>
  <mysolution>
    <p>
    由前一式, $a=\log_3 c=\frac{\ln c}{\ln3}$, $b= \frac{\ln c}{\ln5}$, 带入后一式知 $c=\sqrt{15}$.
  </p>
</mysolution>
</p>

<p>
  \lianxi
  \begin{exercise}[s]
    已知 $a$, $b$, $c$ 均为正数, 且 $3^a =4^b =6^c$, 求证:
    $\frac2a+ \frac1b= \frac2c$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    设 $3^a =4^b =6^c=k$, 则 $k>0$ 且
    \mymarginpar{连等式一般设公共值为 $k$.}
    \[a=\frac{\ln k}{\ln 3},\quad b=\frac{\ln k}{\ln 4},\quad 
      c=\frac{\ln k}{\ln6},\]
    即可验证后一式.
  </p>
</mysolution>
</p>

<p>
  \subsubsection{课堂评价}
  <myexercise>
    <p>    计算: $\frac{\lg\sqrt{27}+\lg8-3\lg\sqrt{10}}{\lg1.2}$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $=\frac12\cdot\frac{3\lg3+6\lg2-3}{\lg3+2\lg2-1}=\frac32$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    计算: $(\lg2)^2 +\lg2\cdot \lg50+\lg25$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $=(\lg2)^2 +\lg2\cdot (2-\lg2)+(2-2\lg2)=2$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    计算: $\lg\frac12 -\lg\frac58 +\lg12.5-\log_8 9\cdot\log_3 4$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $=\lg\Big(\frac12\cdot\frac85\cdot\frac{25}2\Big)- \frac{2\ln3}{3\ln2}\cdot\frac{2\ln2}{\ln3}= -\frac13$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    设 $M=3^{361}$, 利用 $\lg3\approx0.48$ 可估计 $M\approx 10^k$, $k\in\mathbb{N}$, 求 $k$ 的值.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $\lg M= 361\lg3\approx 173.28$, 四舍五入得 $M\approx 10^{173}$, 即 $k=173$.
  </p>
</mysolution>
</p>

<p>
  \subsection{课后练习}
  <myexercise>
    <p>    若 $\lg x^2-\lg(2x-10))=1$, 则 $x=$\,?
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $x^2=10(2x-10)$, $x=10$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    计算: $\log_3 81+ \lg20+ \lg 50- \ln\mathrm{e}^3$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $= 4+(\lg2+1)+(1+\lg5)-3=4$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    计算: $\frac{\lg8+\lg125-\lg2-\lg5}{\lg\sqrt{10}\cdot\lg0.1}$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    原式 $=\frac{3\lg2+3\lg5-1}{0.5\cdot(-1)}=-4$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    若 $a=\log_4 3$, 计算: $2^a+2^{-a}$.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    由已知, $4^a=3$, 则 $2^a=\sqrt3$, $2^a+2^{-a}=\frac{4\sqrt3}3$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    若函数 $f(x)=\begin{cases}
      2^x, & x\geqslant2,\\
      f(x+2), & x< 2,
      \end{cases}$ 求 $f\Big(\log_2\frac18\Big)$ 的值.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $f\Big(\log_2\frac18\Big)= f(-3)= f(3)=8$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知 $2\lg\frac{x-y}2 =\lg x+\lg y$, 求 $\frac{x}{y}$ 的值.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    $\Big(\frac{x-y}2\Big)^2=xy$, $\Big(\frac{x}y\Big)-6\frac{x}y+1=0$, 解得 $\frac{x}y=3\pm2\sqrt2$. 而 $x-y>0$ 即 $\frac{y}x>1$, 所以 $\frac{x}y=3+2\sqrt2$.
  </p>
</mysolution>
</p>

<p>
  <myexercise>
    <p>    已知 $a>b>1$, $\log_a b+\log_b a=\frac52$ 且 $a^b=b^a$, 求 $a$, $b$ 的值.
  </p>
</myexercise>
</p>

<p>
  <mysolution>
    <p>
    前一等式化为 $\frac{\ln a}{\ln b}+\frac{\ln b}{\ln a}=\frac52$, 解得 $\frac{\ln a}{\ln b}=\frac12$ 或 $2$. 由 $a>b>1$ 知 $\frac{\ln a}{\ln b}=2$, 即 $a=b^2$. 后一等式化为 $\frac{\ln a}{\ln b}=\frac{a}b$, 所以 $a=2b$, 解得 $a=4$, $b=2$.
</p>

<p>
    \varexercise 题中若只限制 $a$, $b>0$ 且 $a$, $b\neq 1$, 则如何求 $a$, $b$ 的值\,?
</p>

<p>
    仍有 $\frac{\ln a}{\ln b}=\frac{a}b=\frac12$ 或 $2$. 
    \mymarginpar{结果表明原题中若限制 $a>b>0$, 答案不变.}
    若 $a>b$, 则 $a=2b$ 且 $a=b^2$, 解得 $a=4$, $b=2$. 若 $a< b$, 则 $2a=b$ 且 $a^2=b$, 解得 $a=2$, $b=4$. 
  </p>
</mysolution>