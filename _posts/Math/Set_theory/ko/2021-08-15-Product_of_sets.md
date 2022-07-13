---

title: "집합의 곱"
excerpt: "집합들 사이의 곱"

lang: ko

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/product_of_sets
header:
    overlay_image: /assets/images/Set_theory/Product_of_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-15
last_modified_at: 2022-05-17
weight: 8

---

## 집합의 곱

Family를 처음 소개하며 언급했듯, 순서쌍을 가장 자연스럽게 일반화하는 것은 함수이다. 더 정확히 이야기하자면, $n$-tuple은 $I=\\{1,2,\cdots, n\\}$을 정의역으로 갖는, $i$를 넣으면 $i$번째 성분을 돌려주는 함수로 생각할 수 있었으며, 우리는 이에 착안하여 index set $I$를 일반적인 집합으로 확장하였다.  
한편 우리는 두 집합의 cartesian product도 이미 정의했었다. 우리는 집합 $X_1$, $X_2$에 대하여 $x_1\in X_1$, $x_2\in X_2$인 $(x_1,x_2)$들을 모두 모아둔 집합을 $X_1\times X_2$이라 약속했다. 이를 앞서 말한 함수 형태로 보자면, $X_1\times X_2$는 정의역 $\\{1,2\\}$를 갖는 함수 $f$들의 모임으로, 이 함수 $f$들은 $f(1)=x_1\in X_1$, $f(2)=x_2\in X_2$를 만족한다. 

따라서 일반적인 family의 곱은 다음과 같이 정의하는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $(X_i)\_{i\in I}$가 집합들의 family라 하자. 그럼 정의역 $I$를 갖는 모든 functional graph들 중, $F(i)\in X_i$를 만족하는 것들의 모임을 이 family의 *product<sub>곱</sub>*라 부르고, 이를 $\prod\_{i\in I} X_i$로 적는다. 이들의 원소를 $(x_i)\_{i\in I}$로 적으며, 각각의 $X_i$를 $i$번째 성분이라 부르고, $F\in\prod\_{i\in I} X_i$를 $F(i)$로 대응시키는 함수를 $i$번째 coordinate function이라 부르고 $\operatorname{pr}\_i$로 적는다.

</div>

따라서 일반적으로, 집합들의 곱을 다루기 위해서는 <em_ko>함수들의 집합</em_ko>을 생각할 필요가 있다.

우선 집합 $E$, $F$가 주어졌다고 하자. 그럼 $E$에서 $F$로의 functional graph는 집합 $E\times F$의 부분집합이므로 $\mathcal{P}(E\times F)$의 원소이다. 따라서 $E$에서 $F$로의 functional graph들의 모임은 $E\times F$들의 부분집합의 모임이므로, 이 모임은 $\mathcal{P}(E\times F)$의 부분집합이 된다. 이를 우리는 $F^E$로 적는다.  
이제 $G\in F^E$는 $E\rightarrow F$인 어떤 함수의 functional graph이므로, 정의에 의하여 $g=(G,E,F)$는 $E$에서 $F$로의 함수이다. 따라서 이러한 triple들을 모으면 $E$에서 $F$로의 함수들의 집합이 생길 것이다. 이 집합을 $\operatorname{Fun}(E, F)$로 적자. 우리는 $g\leftrightarrow G$에 의하여 $\operatorname{Fun}(E,F)$의 각각의 원소와 $F^E$의 각각의 원소를 동일시할 수 있고, 따라서 $\operatorname{Fun}(E, F)$ 자체도 $F^E$와 자명하게 동일시할 수 있다. 

어떠한 map $u:E'\rightarrow E$와 $v:F\rightarrow F'$가 주어졌다고 하고, 다음의 diagram을 생각하자.

![induced_mapping](/assets/images/Set_theory/Product_of_sets-1.png){:width="110px"  class="invert" .align-center}

이 diagram에서, 어떤 함수 $f:E\rightarrow F$가 주어질 때마다 우리는 이에 해당하는 $E'$에서 $F'$로의 함수 $\tilde{f}$를 생각할 수 있다. 이 함수는 $\tilde{f}=v\circ f\circ u$로 정의되는 함수이다. 그렇다면 $f\mapsto \tilde{f}$는 $\operatorname{Fun}(E, F)$에서 $\operatorname{Fun}(E', F')$로의 함수이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위의 diagram에서, $u$가 surjection이고 $v$가 injection이라면 $f\mapsto \tilde{f}$는 injection이다. 만일 $u$가 injection이고 $v$가 surjection이라면, $f\mapsto \tilde{f}$는 surjection이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
우선 $u$, $v$가 각각 surjection과 injection이라 하자. 위의 함수 $f\mapsto \tilde{f}$가 주어졌다고 할 때, 이 함수가 injection임을 보이기 위해서는 $\tilde{f}=\tilde{g}$라면 $f=g$임을 보여야 한다. $s$와 $r$을 각각에 해당하는 section과 retraction이라 하자. 즉 $u\circ s=\operatorname{id}_E$이고 $r\circ v=\operatorname{id}_F$이다. 만일 $\tilde{f}=\tilde{g}$라면, 

$$\begin{aligned}
  f&=\operatorname{id}_F\circ f\circ\operatorname{id}_E=(r\circ v)\circ f\circ(u\circ s)=r\circ(v\circ f\circ u)\circ s\\
  &=r\circ\tilde{f}\circ s=r\circ\tilde{g}\circ s\\
  &=r\circ(v\circ g\circ u)\circ s=(r\circ v)\circ g\circ (u\circ s)=\operatorname{id}_F\circ g\circ\operatorname{id}_E=g
\end{aligned}$$

이므로 $f=g$이다. 따라서 주어진 함수는 injective이다. 

이제 $u$와 $v$가 각각 injection과 surjective라 하자. 이제 임의의 $f'\in\operatorname{Fun}(E',F')$에 대하여 $\tilde{f}=f'$인 $f\in\operatorname{Fun}(E, F)$가 존재함을 보여야 한다. $r'$, $s'$가 각각 $u$와 $v$의 retraction과 section이라 하자. 즉 $r'\circ u=\operatorname{id}\_{E'}$이고 $v\circ s'=\operatorname{id}\_{F'}$이다. 그럼

$$f'=\operatorname{id}_{F'}\circ f'\circ\operatorname{id}_{E'}=(v\circ s')\circ f'\circ(r'\circ u)=v\circ(s'\circ f'\circ r')\circ u$$

이므로, $f=s'\circ f'\circ r'$로 잡으면 된다.
</details>

따라서 만일 $u$와 $v$가 모두 bijection이라면 $f\mapsto \tilde{f}$ 또한 bijection이 된다. 

앞서 집합들 사이의 sum이 universal property를 만족했었는데, 마찬가지로 product도 비슷한 universal property를 만족한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 집합들의 family $(X_i)$들의 product $X$와, projection map들 $\operatorname{pr}\_i:X\rightarrow X_i$가 주어졌다 하자. 다른 집합 $Y$와, map들 $f_i:Y\rightarrow X_i$가 주어졌다고 하면, 식 $f_i=\operatorname{pr}\_i\circ f$를 만족하도록 하는 유일한 함수 $f:Y\rightarrow X$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 주어진 조건 $f\_i=\operatorname{pr}\_i\circ f$를 만족하는 함수 $f,f'$가 주어졌다 하자. 우리는 임의의 $y\in Y$에 대해 $f(y)=f'(y)$임을 보여야 한다. 그런데 $f(y)$와 $f'(y)$는 어차피 $X$의 원소이므로 함수(순서쌍)이고, 따라서 $i$가 대응되는 값($i$번째 좌표)들에 의해 결정된다. 따라서 임의의 $y\in Y$와 $i\in I$가 주어졌다고 할 때, $\operatorname{pr}\_i(f(y))=\operatorname{pr}\_i(f'(y))$라는 것을 보이면 충분하다. 그런데

$$\operatorname{pr}_i(f(y))=f_i(y)=\operatorname{pr}_i(f'(y))$$  

이므로, 그러한 함수 $f$는 유일해야 한다.

존재성의 경우, 마찬가지로 위의 유일성 증명에 힌트를 얻어 $f(y)$의 값을

> $(f(y))(i)=f_i(y)$를 만족하는 함수 (혹은 $i$번째 좌표가 $f_i(y)$인 순서쌍)

으로 정의한 후 이 대응 $y\mapsto f(y)$가 실제로 함수임을 보이면 된다. 

</details>

따라서 [정리 3](#thm3)의 조건을 만족하는 $(X, \operatorname{pr}\_i)$가 적어도 하나는 존재하므로, 이를 product의 정의로 삼아도 된다. [§집합의 합, 따름정리 9](/ko/math/set_theory/sum_of_sets#crl9)과 정확하게 같은 논리를 펼치면 이 universal property를 만족하는 대상 및 $\operatorname{pr}_i$들 또한 unique up to bijection임을 확인할 수 있다.


<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 집합 $A$, $B$, $C$에 대해 $f:B\times C\rightarrow A$라 하자. 만일 $\tilde{f}$가 $C$에서 $\operatorname{Fun}(B,A)$로의 함수 $y\mapsto f(-,y)$라면, $f\mapsto\tilde{f}$는 bijection이다. 즉, $\operatorname{Fun}(B\times C,A)$와 $\operatorname{Fun}(C, \operatorname{Fun}(B, A))$ 사이의 bijection이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>
우선 $\tilde{f}$는 $C$에서 $\operatorname{Fun}(B,A)$로의 함수이므로, $\tilde{f}\in\operatorname{Fun}(C,\operatorname{Fun}(B,A))$이다. 따라서 주어진 함수는 $\operatorname{Fun}(B\times C, A)$에서 $\operatorname{Fun}(C, \operatorname{Fun}(B,A))$로의 함수이다. 우리는 이 함수가 bijection임을 보이기 위해 역함수를 만들 것이다.

$g\in\operatorname{Fun}(C, \operatorname{Fun}(B,A))$가 주어졌다고 하자. 그럼 임의의 $y\in C$에 대하여, $g(y)$는 $\operatorname{Fun}(B, A)$의 원소이다. 이제 $\bar{g}:B\times C\rightarrow A$를 $(x, y)$를 $g(y)(x)$로 보내는 함수로 정의하자. 그럼 임의의 $g\in \operatorname{Fun}(C,\operatorname{Fun}(B,A))$에 대하여, $g$를 $\bar{g}$로 보내는 함수

$$\begin{aligned}
-:\operatorname{Fun}(C, \operatorname{Fun}(B,A))&\rightarrow\operatorname{Fun}(B\times C,A)\\
g\phantom{function}&\mapsto\phantom{function}\bar{g}
\end{aligned}$$

를 생각할 수 있다. 앞서 말한대로, 우리는 이 함수 $-$가 원래의 함수

$$\begin{aligned}
\sim\;:\operatorname{Fun}(B\times C,A)&\rightarrow\operatorname{Fun}(C, \operatorname{Fun}(B,A))\\
f\phantom{function}&\mapsto\phantom{function}\tilde{f}
\end{aligned}$$

의 역함수임을 보여야 한다.

임의의 $f:B\times C\rightarrow A$에 대하여, $\tilde{f}\in \operatorname{Fun}(C, \operatorname{Fun}(B, A))$이다. 이제 이 함수를 거꾸로 $-$를 타고 $\operatorname{Fun}(B\times C,A)$로 보내자. 그럼 이 결과 $\bar{\tilde{f}}$는 $(x, y)$를 $\tilde{f}(y)(x)$로 보내는 함수이다. 그런데 $\tilde{f}(y)$는 함수 $f(-, y)$이므로 $\bar{\tilde{f}}=f$이다.  
한편 임의의 $g\in\operatorname{Fun}(C, \operatorname{Fun}(B, A))$에 대하여, $\bar{g}$를 먼저 적용한 후 $\tilde{\bar{g}}$를 조사해보면, $\tilde{\bar{g}}$는 $y\mapsto \bar{g}(-,y)$로 정해지는 함수이다. 그런데 $\bar{g}$의 정의에 의하여 이는 다시 $y$를 $g(y)(-)$로 보내는 함수이다. 즉 $\tilde{\bar{g}}$는 다시 $g$가 된다. 이로부터 $\bar{\tilde{f}}=f$이고 $\tilde{\bar{g}}=g$이므로 이들은 서로 역함수 관계이다. 즉, 우리는 다음을 보인 것이다.

$$\begin{aligned}
  f\overset{\sim}{\longrightarrow}&\tilde{f}\overset{-}{\longrightarrow}\bar{\tilde{f}}=f,\\
  g\overset{-}{\longrightarrow}&\bar{g}\overset{\sim}{\longrightarrow}\tilde{\bar{g}}=g
\end{aligned}$$

그러므로 $\sim\;:f\mapsto\tilde{f}$는 bijection이다. 
</details>

우리는 합집합을 정의한 직후에, index set을 surjection을 통해 바꾸어도 아무런 일도 일어나지 않음을 보았는데, 집합들의 곱에서는 bijection을 통해 바꾸어도 아무런 일도 일어나지 않는다. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $(X_i)\_{i\in I}$가 집합들의 family이고 $u:K\rightarrow I$가 bijection이라 하자. 만일 $U$가 $u$의 그래프라면 $F\mapsto F\circ U$는 bijection이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>
다음의 diagram을 생각하자.

![induced_bijection](/assets/images/Set_theory/Product_of_sets-2.png){:width="160px"  class="invert" .align-center}

여기서 $v$는 $(x_i)\_{i\in I}$를 $(x\_{u(k)})\_{k\in K}$로 대응시키는 bijection이다. 그럼 위의 [명제 2](#pp2)에 의하여 $F\mapsto F\circ U$는 bijection이다.
</details>

합집합, 교집합과 마찬가지로, product의 결합법칙 또한 성립한다. 하지만 결합법칙이라는 이야기를 하기 위해서는 우선 다음의 정의를 해야 한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> Family $(X_i)\_{i\in I}$와 그 product $\prod\_{i\in I} X_i$가 주어졌다고 하자. 그럼 부분집합 $J\subset I$에 대하여, $\prod\_{i\in J} X_i$를 *partial product<sub>부분곱</sub>*이라 부른다. 이 때, $f\in\prod\_{i\in I} X_i$의 *restriction*은 $F\circ\Delta_J$로 주어지며, $F\mapsto F\circ\Delta_J$를 subindex $J$로의 projection이라 부르고 $\operatorname{pr}\_J$로 적는다.

</div>

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Family $(X_i)\_{i\in I}$에 대하여, $X_i$들이 모두 공집합이 아니라 하자. 만일 $g:J\rightarrow\bigcup\_{i\in I} X_i$가 $g(i)\in X_i$를 만족한다면, $I$를 정의역으로 갖는 $g$의 extension $f$가 존재하여 $f(i)\in X_i$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $i\in I\setminus J$에 대하여, $X_i$가 공집합이 아니므로 $x_i\in X_i$를 하나씩 뽑을 수 있다. 따라서 $g$의 그래프 $G$를 $G\cup\left(\bigcup\_{i\in I\setminus J}\left\\{(i, x_i)\right\\}\right)$로 확장하면 된다.
</details>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $(X_i)$가 $I\neq\emptyset$을 만족하는 family라 하자. 만일 $(J_k)\_{k\in K}$이 $I$의 partition이라면, $\prod\_{i\in I}X_i$에서 $\prod\_{k\in K}\left(\prod\_{i\in J_k}X_i\right)$로의 함수 $f\mapsto (\operatorname{pr}\_{J_k})\_{k\in K}$ 또한 bijection이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$(J_k)\_{k\in K}$이 partition이므로, $f_k:J_k\rightarrow \bigcup\_{i\in I} X_i$는 mutually disjoint한 정의역을 갖는 함수들의 family이고, 따라서 [§집합의 합, 명제 2](/ko/math/set_theory/sum_of_sets#pp2)를 적용하면 bijection을 얻는다.
</details>

이쯤에서 universal property가 얼마나 강력한지를 다시 언급하지 않을 수가 없다. 직전의 명제를 증명할 때, 적당한 함수 (두 projection들의 합성)들을 이용해서 universal property의 유일성 증명과 비슷하게 진행했다면 위의 명제는 universal property로부터 바로 따라나왔을 것이다.  


우리는 이변수함수를 정의한 이후 $u\times v$를 정의했는데, 다음은 그에 대한 일반화이다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> $(X_i)\_{i\in I}$, $(Y_i)\_{i\in I}$가 같은 index를 갖는 family이고 $(g_i)\_{i\in I}$를 

> $g_i$가 $X_i$에서 $Y_i$로의 함수인 family

라 하자. 각각의 $f\in \prod_{i\in I}X_i$에 대하여, $u_f$가 함수 $i=g_i(f(i))$의 그래프라 하자. 그럼 함수 $f\mapsto u_f$를 *canonical extension*이라 부른다.

</div>


<ins id="pp10">**명제 10**</ins> $(X_i)\_{i\in I}$, $(Y_i)\_{i\in I}$, $(Z_i)\_{i\in I}$가 세 family라 하고, $(g_i)\_{i\in I}$, $(g_i')\_{i\in I}$가 각각 $X_i$에서 $Y_i$, $Y_i$에서 $Z_i$로의 함수들의 family라 하자. 만일 $g$와 $g'$가 각각 $\prod_{i\in I} X_i$에서 $\prod\_{i\in I} Y_i$, $\prod\_{i\in I}Y_i$에서 $\prod_{i\in I}Z_i$로 가는 $(g_i)\_{i\in I}$와 $(g_i')\_{i\in I}$의 product이라 한다면, $(g_i'\circ g_i)$와 $g'\circ g$이 같다.
{: .proposition}

## 분배법칙

한편, 두 개 이상의 연산이 정의되어 있다면 분배법칙이 성립하는지가 중요한 관심사다.

<div class="proposition" markdown="1">
<ins id="pp11">**명제 11**</ins> $((X\_{k,i})\_{i\in J\_k})\_{k\in K}$가 family들의 family라 하자. 추가로 $K\neq\emptyset$이고 $J_k\neq\emptyset$가 모든 $k\in K$에 대해 성립한다고 하자. 그럼 $I=\prod\_{k\in K} J_k\neq\emptyset$에 대하여,

$$\bigcup_{k\in K}\left(\bigcap_{i\in J_k}X_{k,i}\right)=\bigcap_{f\in I}\left(\bigcup_{k\in K}X_{k,f(k)}\right),\quad\bigcap_{k\in K}\left(\bigcup_{i\in J}X_{k,i}\right)=\bigcup_{f\in I}\left(\bigcap_{k\in K}X_{k,f(k)}\right)$$

이 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>
우선 $x\in \bigcup\_{k\in K}\left(\bigcap\_{i\in J_k}X\_{k,i}\right)$라 하자. 우리는 $x\in \bigcap\_{f\in I}\left(\bigcup\_{k\in K}X\_{k,f(k)}\right)$, 즉 모든 $f\in I$에 대하여 $x\in \bigcup\_{k\in K}X\_{k,f(k)}$임을 보여야 한다. 어떤 $k\in K$에 대하여 $x\in \bigcap\_{i\in J_k}X\_{k,i}$이므로, $x\in X\_{k,f(k)}$이다. 따라서 $x\in \bigcup\_{k\in K}X\_{k,f(k)}$가 모든 $f$에 대하여 성립하고, 따라서 포함관계가 성립한다.  

반대쪽 포함관계를 보이기 위해 대우명제를 사용하자. 즉 $x\not\in \bigcup\_{k\in K}\left(\bigcap\_{i\in J_k}X\_{k,i}\right)$라 하자. 그럼 모든 $k\in K$에 대하여, $x\not\in \bigcap\_{i\in J_k}X\_{k,i}$이다. 따라서 어떤 $i$가 존재하여, 모든 $k$에 대해 $x\not\in  X\_{k,i}$이다. 이제 $f(k)$가 그러한 $i$가 되도록 하는 $f\in I$를 잡으면, $x\not\in\bigcup\_{k\in K}X\_{k,f(k)}$이고 , 따라서 우변에 속하지 않는다. 두 번째 식도 이와 비슷하게 보이면 된다.
</details>

Product와 union, 그리고 product와 intersection 사이에도 다음과 같이 분배법칙이 성립하며, 이에 대한 증명은 위와 거의 같으므로 생략한다.

<div class="proposition" markdown="1">
<ins id="pp12">**명제 12**</ins> $((X\_{k,i})\_{i\in J\_k})\_{k\in K}$가 family들의 family이고, $I$를 위의 명제와 동일하게 정의하자. 그럼 

$$\prod_{k\in K}\left(\bigcup_{i\in J_k}X_{k,i}\right)=\bigcup_{f\in I}\left(\prod_{k\in K}X_{k,f(k)}\right),\quad\prod_{k\in K}\left(\bigcap_{i\in J}X_{k,i}\right)=\bigcap_{f\in I}\left(\prod_{k\in K}X_{k,f(k)}\right)$$

가 성립한다.
</div>

---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

