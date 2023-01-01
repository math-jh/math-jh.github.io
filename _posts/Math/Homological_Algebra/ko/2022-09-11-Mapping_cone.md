---

title: "Mapping cone"
excerpt: "기본정의"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/mapping_cone
header:
    overlay_image: /assets/images/Homological_algebra/a.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2022-09-11
last_modified_at: 2022-09-11
weight: 6

---

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 chain map $f:B\rightarrow C$에 대하여, $f$의 *mapping cone* $\cone(f)$는 다음의 chain complex

$$\cdots\longrightarrow\underbrace{B_n\oplus C_{n+1}}_{\cone(f)_{n+1}}\overset{d_{n+1}}{\longrightarrow}\underbrace{B_{n-1}\oplus C_n}_{\cone(f)_n}\overset{d_n}{\longrightarrow}\underbrace{B_{n-2}\oplus C_{n-1}}_{\cone(f)_{n-1}}\longrightarrow\cdots$$

를 의미한다. 이 때, differential은 다음의 식

$$d_n(b,c)=(-d_{n-1}(b), d_n(c)-f_{n-1}(b))\qquad (b\in B_{n-1},c\in C_n)$$

으로 주어진다. 

</div>

Differential $d$를 다음의 행렬

$$\begin{pmatrix}-d^B&0\\-f&d^C\end{pmatrix}$$

으로 생각하면 $d$의 식을 쉽게 기억할 수 있다. 이 부호들은 나중에 계산을 편하게 하도록 해 준다.

**디라이브드 하기 전에 채워넣기**