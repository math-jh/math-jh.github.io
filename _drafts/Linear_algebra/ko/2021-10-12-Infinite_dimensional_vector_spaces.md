---

title: "무한차원 벡터공간<sup>†</sup>"
excerpt: "무한차원 벡터공간의 기저와 차원"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/infinite-dimensional-vector-space
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Infinite_dimensional_vector_spaces.png
    overlay_filter: 0.5

date: 2021-10-12
last_modified_at: 2022-08-01

weight: 6

---

우리는 다음 이야기를 하기에 앞서서, 모든 (유한차원일 필요는 없는) 벡터공간이 basis를 가지며, 이 때 차원이 잘 정의된다는 것을 보인다. 

## Basis의 존재성

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합들의 family $\mathscr{B}$에 대하여, $A\in\mathscr{B}$가 *maximal*이라는 것은, 만약 임의의 $B\in\mathscr{B}$에 대하여 $A\subset B$라면 반드시 $A=B$인 것이다. (cf. [집합론, §순서집합의 원소들, 정의 1](/ko/math/set_theory/elements_in_ordered_set#df1)) 

</div>

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 $F$-벡터공간 $V$에 대하여, $V$의 모든 일차독립인 부분집합들의 모임을 $\mathscr{B}$라 하자. 만약 $\mathscr{B}$의 maximal element $\mathcal{B}$가 존재한다면, $\mathcal{B}$는 $V$의 basis가 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $\mathcal{B}$가 $V$의 basis가 아니라 가정하자. $\mathcal{B}\in\mathscr{B}$이므로 $\mathcal{B}$는 일차독립이고, 따라서 $\mathcal{B}$가 $V$의 basis가 아니기 위해서는 $\mathcal{B}$가 $V$를 span하지 않아야 한다. 이제 $\operatorname{span}\mathcal{B}$ 바깥에 있는 $V$의 원소를 하나 뽑아 이를 $v$라 하고, $\mathcal{B}'=\mathcal{B}\cup\\{v\\}$이라 하자. 만일

$$\sum_{x\in\mathcal{B}'}\alpha_xx=0,\qquad\text{$(\alpha_x)_{x\in\mathcal{B}'}$ finitely supported}$$

이라 하면, 두 가지 가능성이 있다.

1. 만일 $v\in\operatorname{supp}(\alpha_x)\_{x\in\mathcal{B}'}$인 경우, 

    $$0=\sum_{x\in\mathcal{B}'}\alpha_xx=\alpha_vv+\sum_{x\in\mathcal{B}}\alpha_xx$$
    
    이므로 
    
    $$v=\sum_{x\in\mathcal{B}}-\alpha_v^{-1}\alpha_xx$$
    
    가 되어, $v\not\in\operatorname{span}\mathcal{B}$의 원소라는 가정에 모순이다.
    
2. 따라서 $v\in\operatorname{supp}(\alpha_x)\_{x\in\mathcal{B}'}$여야 하는데, 이 경우

    $$0=\sum_{x\in\mathcal{B}'}\alpha_xx=\sum_{x\in\mathcal{B}}\alpha_xx$$
    
    이므로, $\mathcal{B}$의 일차독립성에 의해 모든 $x\in\mathcal{B}$에 대해 $\alpha_x=0$이다.

즉, $\alpha_x=0$이 모든 $x\in\mathcal{B}'$에 대해 성립하고 따라서 $\mathcal{B}'$는 일차독립인 부분집합이 된다. 그런데, $\mathcal{B}'\supsetneq\mathcal{B}$이므로 이는 $\mathcal{B}$의 maximality에 모순이다.
 
</details>

따라서, 임의의 $F$-벡터공간의 basis가 존재한다는 것을 보이기 위해서는 집합 $\mathscr{B}$의 maximal element가 존재함을 보이면 된다. 당연히 이는 Zorn's lemma를 사용한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (Zorn)**</ins> 집합들의 모임 $\mathscr{B}$의 임의의 chain이 항상 upper bound를 갖는다고 가정하자. 즉, $\mathcal{C}\subseteq\mathscr{B}$이고, $\mathcal{C}$가 추가적인 다음의 조건

> 임의의 $C_1,C_2\in\mathcal{C}$에 대하여, 항상 $C_1\subseteq C_2$이거나 $C_2\subseteq C_1$

을 만족한다면, 항상 적당한 $\mathcal{B}\in\mathscr{B}$가 존재하여, 임의의 $C\in\mathcal{C}$에 대해 $C\subseteq\mathcal{B}$이도록 할 수 있다고 가정하자. 그럼 $\mathscr{B}$는 maximal element를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[집합론, §선택공리, 정리 4](/ko/math/set_theory/axiom_of_choice#thm4).

</details>

사실, 다음 정리는 Zorn's lemma의 아주 standard한 활용이기도 하다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 임의의 $F$-벡터공간 $V$는 basis를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$V$의 모든 일차독립인 부분집합들을 모아둔 집합을 $\mathscr{B}$라 하자. $\mathscr{B}$가 [보조정리 3](#lem3)의 조건을 만족한다는 것을 보이면 된다.

이를 위해, $\mathscr{B}$의 임의의 chain $\mathcal{C}$가 주어졌다 하자. 우리는 임의의 $C\in\mathcal{C}$에 대해 $C\subseteq\mathcal{B}$가 성립하도록 하는 $\mathcal{B}\in\mathscr{B}$를 찾아야 한다. 당연히 자연스러운 선택은 $\mathcal{B}=\bigcup_{C\in\mathcal{C}}C$이다. 증명을 마무리하기 위해서는 이 집합이 $\mathscr{B}$의 원소라는 것을 보여야 한다. 즉, $\mathcal{B}$가 일차독립이어야 한다.

임의의 finitely supported family $(\alpha_x)_{x\in\mathcal{B}}$에 대하여, 

$$\sum_{x\in\mathcal{B}}\alpha_xx=0$$

이라 가정하자. $x\in\mathcal{B}$들은 모두 어떠한 $C\in\mathcal{B}$의 원소인데, 어차피 $\operatorname{supp}(\alpha_x)$는 유한집합이므로 $\operatorname{supp}(\alpha_x)$의 모든 원소들을 포함하는 $C\in\mathcal{B}$가 존재한다.[^1] $C$는 일차독립이므로, 위의 식의 모든 $\alpha_x$는 0이 되어야 하고, 따라서 $\mathcal{B}$는 일차독립.

</details>

다음 두 따름정리는 모두 유한차원일 경우에는 증명을 했었지만 ([§벡터공간의 차원, 명제 5](/ko/math/linear_algebra/dimension#pp5), [명제 6](/ko/math/linear_algebra/dimension#pp6)) 앞선 논증과 비슷하게, 무한차원 벡터공간에 대해서도 성립한다. 

<div class="proposition" markdown="1">

<ins id="crl5">**따름정리 5**</ins> $F$-벡터공간 $V$와 $V$의 임의의 일차독립인 부분집합 $S$에 대하여, $S$를 포함하는 $V$의 basis $\mathcal{B}$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 명제의 증명에서, $\mathscr{B}$는 $S$를 포함하고, 따라서 Zorn's lemma에 의하여 $S$를 포함하는 maximal한 일차독립 부분집합이 존재한다. 

</details>
<div class="proposition" markdown="1">

<ins id="crl6">**따름정리 6**</ins> $F$-벡터공간 $V$와, $V$를 span하는 부분집합 $S$에 대하여, $S$의 어떤 부분집합은 $V$의 basis가 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이번에는 $\mathscr{C}$를 

> $S$에 포함된 모든 일차독립인 부분집합들의 집합

으로 정의하자. 어렵지 않게 $\mathscr{C}$가 Zorn's lemma의 조건을 만족한다는 것을 확인할 수 있고, 따라서 maximal element $\mathcal{B}$가 존재한다. 이제 $\mathcal{B}$는 [명제 4](#pp4)에서 도입한 집합 $\mathscr{B}$ ($V$의 모든 일차독립인 부분집합들의 집합)에서도 maximal인 것을, 즉 $V$의 basis가 된다는 것을 증명하면 된다. 

결론에 반하여 $\mathcal{B}$가 $V$의 basis가 아니라 가정하자. 그럼 어떤 $v\in V$가 존재하여 $v\not\in\operatorname{span}\mathcal{B}$이다. 한편, $S$는 $V$를 span하므로, 적당한 finitely supported family $(\alpha_x)_{x\in S}$가 존재하여 

$$v=\sum_{x\in S}\alpha_xx$$

이다. (물론, $S$는 일차독립인 부분집합이 아니므로 이 표현은 유일하지 않을 수 있다.) 만일 $\operatorname{supp}(\alpha_x)_{x\in S}$의 원소들이 모두 $\mathcal{B}$의 원소였다면 $v\in\operatorname{span}\mathcal{B}$였을 것이므로, $x\not\in\mathcal{B}$를 만족하는 원소들 $x\in S$가 존재한다. 또, 만일 이러한 원소 $x$들이 모두 $\mathcal{B}$의 다른 원소들의 일차결합으로 표현 가능하다면, $\alpha_xx$들을 모두 이 일차결합으로 바꾸면 $v\in\operatorname{span}\mathcal{B}$이므로, 이러한 $x$들 가운데에는 $\mathcal{B}$의 원소들의 일차결합으로 나타나지 않는 어떤 원소 $y$가 존재한다. 

이제 $\mathcal{B}'=\mathcal{B}\cup\\{y\\}$라 하자. 그럼 $y$는 $\mathcal{B}$의 원소들의 일차결합으로 나타나지 않으므로, $\mathcal{B}'$는 일차독립인 부분집합이고, $y\in S$이므로 $\mathcal{B}'\in\mathscr{C}$이다. 이는 $\mathcal{B}$가 $\mathscr{C}$에서 maximal이라는 가정에 모순이므로, $\mathcal{B}$는 $V$의 basis여야 한다.   

</details>



## Well-definedness of dimension

이렇게 basis의 존재성을 보이고 나면, 차원이 잘 정의된다는 것을 보여야 한다. 즉, 임의의 $F$-벡터공간 $V$에 대하여, $\mathcal{B}_1$, $\mathcal{B}_2$가 두 basis라면 $\lvert\mathcal{B}\_1\rvert=\lvert\mathcal{B}\_2\rvert$임을 보여야 한다. 

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 어떤 $F$-벡터공간 $V$가 무한한 basis $\mathcal{B}\_1$을 갖는다면, $V$의 또 다른 basis $\mathcal{B}\_2$ 또한 무한하며 그 cardinality는 $\lvert\mathcal{B}\_1\rvert$와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 결론에 반하여 $V$의 유한한 basis $\mathcal{B}'$가 존재한다 하자. $\operatorname{span}\mathcal{B}'=V$이므로, $\mathcal{B}$의 모든 원소들은 $\mathcal{B}'$의 원소들의 일차결합으로 표현 가능하다. 그런데, 다시 $\mathcal{B}'$의 (유한히 많은) 원소들은 $V$의 원소이므로, 이들 각각은 basis $\mathcal{B}$의 일차결합으로 나타나야 한다. 따라서 $\mathcal{B}'$의 모든 원소들을 일차결합으로 표현하기 위해서는 유한히 많은 $\mathcal{B}$의 원소들만이 필요하다. 이들을 $\\{x_1,\ldots, x_m\\}$이라 하자. $V$의 임의의 원소는 항상 $\mathcal{B}'$들의 일차결합으로, 그리고 다시 $\\{x_1,\ldots,x_m\\}$의 원소들로 표현할 수 있으므로, $\mathcal{B}\setminus\\{x_1,\ldots, x_m\\}$의 원소도 이들의 일차결합으로 표기 가능하며, 이는 일차독립성에 모순이다.

따라서, $V$의 다른 basis 또한 항상 무한해야 한다. 이제 다른 basis $\mathcal{B}\_2$의 cardinality가 $\mathcal{B}\_1$의 cardinality와 동일하다는 것을 보여야 한다. $\mathscr{B}$를 다음의 집합

> $\mathcal{B}$의 유한한 부분집합들의 모임

으로 정의하자. 각각의 $x\in\mathcal{B}\_1$들은 $\mathcal{B}\_2$의 원소들의 일차결합 $x=\sum_{y\in\mathcal{B}\_2}x_yy$으로 유일하게 표현 가능하므로, 함수 $f:\mathcal{B}\_1\rightarrow\mathscr{B}$를 $x\mapsto\operatorname{supp}(x_y)\_{y\in\mathcal{B}\_2}$으로 정의하자. 즉, $f$는 임의의 $x\in\mathcal{B}\_1$이 

$$x=\alpha_1y_1+\cdots+\alpha_ny_n$$

으로 표현될 때, $x\mapsto\\{y_1,\ldots,y_n\\}$이라 할 수 있다. 만일 $\operatorname{im}f$가 유한집합이라면, 앞선 논증과 마찬가지로 $\bigcup_{S\in\operatorname{im}f}S$가 $V$를 span하는 유한집합이 되므로 모순이다. 따라서 $\operatorname{im}f$는 무한집합이다. 

안타깝게도, $f$는 injective하지 않기 때문에 우리가 원하는 cardinality의 비교에는 별 도움을 주지 못한다. 따라서 추가적인 construction이 필요하다. 우선 우리는 임의의 $T\in\operatorname{im}f$에 대해 $f^{-1}(T)$가 유한집합이라는 것을 보인다. $x\in f^{-1}(T)$라 하자. 즉, $x$는 $\mathcal{B}\_1$의 원소들 가운데 $T$의 원소들의 일차결합으로 나타나는 원소이다. 그럼, 자명하게 $x\in\operatorname{span}T$이므로, $f^{-1}(T)\subset\operatorname{span}T$이다. 한편, $T$는 유한집합이며, $T$의 각각의 원소들은 유한히 많은 $X$의 원소들의 일차결합으로 나타나므로, 다시 $T$를 span하는 유한히 많은 $\mathcal{B}$의 원소들의 모임 $S$를 택할 수 있다. 이제, $\operatorname{span}T\subset\operatorname{span}S$이고, 따라서 $f^{-1}(T)\subset S$이므로 $f^{-1}(T)$는 유한집합이다.

이제 각각의 $T$에 대하여, $f^{-1}(T)=\\{x_1,\ldots, x_m\\}$이라 하고, $g_T:f^{-1}(T)\rightarrow(\operatorname{im}f)\times\mathbb{N}$을 $x_k\mapsto (T,k)$으로 정의하자. 이 함수는 드디어 injection이 되고, 또 $f^{-1}(T)$들은 자명하게 $\mathcal{B}\_1$의 partition을 이루므로 이들을 합쳐 $\mathcal{B}\_1$에서 $\operatorname{im}f\times\mathbb{N}$으로의 injection을 만들 수 있다. 이제 

$$\lvert\mathcal{B}_1\rvert\leq\lvert\operatorname{im}f\times\mathbb{N}\rvert=\lvert\operatorname{im}f\rvert\aleph_0=\lvert\operatorname{im}f\rvert\leq\lvert\mathscr{B}\rvert=\lvert\mathcal{B}_2\rvert$$ 

이고, $\mathcal{B}\_1$과 $\mathcal{B}\_2$의 역할을 뒤바꾸면 원하는대로 $\lvert\mathcal{B}\_1\rvert=\lvert\mathcal{B}\_2\rvert$를 얻는다.

</details>


---

**참고문헌**

**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
[^1]: $\operatorname{supp}(\alpha_x)=\\{x_1,\ldots, x_n\\}$이라 한다면, $x_1$을 포함하는 $\mathcal{C}$의 원소를 하나 골라 이를 $C_1$이라 하고, $C_1$보다 큰 $\mathcal{C}$의 원소 중 $x_2$를 포함하는 것을 하나 골라 (이러한 것이 없다면, $x_2\not\in\mathcal{B}$일 것이므로) 이를 $C_2$라 하고, ... 
