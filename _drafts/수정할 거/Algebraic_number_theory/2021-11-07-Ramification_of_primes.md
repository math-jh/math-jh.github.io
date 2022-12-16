---

title: "Ramification of primes"
excerpt: "Fractional ideals and the Class group"

categories: [Math / Algebraic Number Theory]
permalink: /ko/math/algebraic_number_theory/ramification_of_primes
header:
    overlay_image: /assets/images/Algebraic_number_theory/Ramification_of_primes.png
    overlay_filter: 0.5
sidebar: 
    nav: "further_topics"

date: 2021-11-07
last_modified_at: 
weight: 5

published: false

---

<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


## Main theorem about the extension of Dedekind domain

우리는 지금까지 대부분의 경우 Dedekind domain에 관심을 집중하고 있는데, 이건 다음의 정리 때문이다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $R$이 Dedekind domain, $K$가 $R$의 quotient field이고 $L/K$가 finite dimensional extension이라 하자. 그럼 $L$에서의 $R$의 integral closure 역시 Dedekind domain이다.

</div>

이 정리에 의하여, 예를 들어 $\mathbb{Q}(\sqrt{-5})$에서 $\mathbb{Z}[\sqrt{-5}]$의 ideal의 factorization등이 보장된다. 

<details class="proof--alone" markdown="1">
<summary>증명</summary>

$L$에서의 $K$의 relative separable closure를 $E$라 하자. 그럼 $E/K$는 separable extension이고, $L/E$는 purely inseparable extension이 된다. $R'$을 $R$의 $E$에서의 integral closure, 그리고 $R\'\'$을 $R'$의 $L$에서의 integral closure라 하면 integral closure의 transitivity에 의하여 $R\'\'$은 $R$의 $L$에서의 integral closure가 된다. 

우리는 우선 $R'$이 Dedekind domian인 것을 보인다. 이는 $R'$이 integrally closed Noetherian domain이고, 또 $R'$의 모든 prime ideal이 곧 maximal ideal이라는 것을 보이면 된다. $R'$은 $R$의 integral closure이므로 $R'$이 integrally closed가 되는 것은 자명하다. 또, $R'$은 field $L$의 subring이므로, integral domain이 되는 것 또한 자명하다. 

이제 $R'$이 Noetherian이라는 것을 보이자. $E/K$는 finite-dimensional extension이므로 basis $a_1,\ldots,a_n$을 잡을 수 있다. 한편, $E$의 임의의 원소 $x$는 $K[\mathrm{x}]$에서 minimal polynomial을 가진다. 이 minimal polynomial을 $f$라 하고, 식

$$f(\mathrm{x})=\mathrm{x}+\frac{r_{n-1}}{s_{n-1}}\mathrm{x}^{n-1}+\cdots+\frac{r_1}{s_1}\mathrm{x}+\frac{r_0}{s_0}=0$$

의 양 변에 $s_i$들의 least common multiple $s$를 곱하면 약간의 renaming을 통해

$$(s\mathrm{x})^n+r_{n-1}'(s\mathrm{x})^{n-1}+\cdots+r_1'(s\mathrm{x})+r_0'=0$$

이라 할 수 있다. $x$는 위의 식을 만족하므로, $\mathrm{t}=sx$는 다음의 식

$$\mathrm{t}^n+r_{n-1}'\mathrm{t}^{n-1}+\cdots+r_1'\mathrm{t}+r_0'=0$$

을 만족하고 따라서 $sx$는 $R$에 대해 integral이다. 따라서 $E$는 $R'$의 quotient field가 되고, 뿐만 아니라 임의의 $x\in E$에 적당한 $s\in R$을 곱하여 $sx$가 $R'$에 포함되도록 할 수 있다. 특히, $a_i$들 각각에 적당한 $R$의 원소들을 각각 곱하여 이들이 모두 $R'$에 속해있도록 할 수 있다. 따라서 일반성을 잃지 않고, 처음부터 $a_i$들이 모두 integral basis였다고 하자. 이제 $(a_i)$들의 dual basis $(b_j)$를 잡자. 그럼

> Claim. $R'\subset \sum Rb_j$.

임의의 $y\in R'$을 고르자. 그럼 $b_j$들이 $E/K$의 basis이므로, 적당한 $c_j\in K$들에 대하여 $y=c_jb_j$라 할 수 있다. 우리가 보이고 싶은 것은 $c_j$가 사실은 $R$의 원소들이라는 것이다. 이를 위해 trace form을 계산해보면

$$(y,a_i)=\left(\sum c_jb_j, a_i\right)=\sum c_j(b_j,a_i)=c_i $$

이고, $y$와 $a_i$ 각각이 $R'$의 원소이므로 $(y,a_i)=T_{E/K}(ya_i)$는 $ya_i\in R$의 minimal polynomial의 계수가 된다. 즉, $c_i\in R$이므로 claim이 완성된다.

따라서 $R'$은 finitely generated $R$-module $\sum Rb_j$의 $R$-submodule이고, 따라서 $R'$의 ideal들도 이 finitely generated $R$-module의 submodule이 된다. $R$은 Noetherian이므로 이들 ideal들은 모두 finitely generated이고 따라서 $R'$도 Noetherian이 된다.

이제 $R'$의 임의의 prime ideal이 maximal이라는 것을 보이면 $R'$이 Dedekind domain이라는 증명이 완료된다. 이를 위해 다음의 claim을 먼저 보이자.

> Claim. $A\subset B$가 integral domain이고, $A$가 integrally closed, 그리고 $B/A$가 integral이라 하자. 임의의 nonzero prime ideal $\mathfrak{P}\subset B$에 대하여, $\mathfrak{P}\cap A$도 $A$의 nonzero prime ideal이 된다. 

$\mathfrak{P}\cap A$가 nonzero임만 보이면 나머지는 분명하다. 임의의 nonzero $x\in\mathfrak{P}$에 대하여, $x$의 minimal polynomial

$$f(\mathrm{x})=\mathrm{x}^{r+1}+a_r\mathrm{x}^r+\cdots+a_1\mathrm{x}+a_0$$

이 $\operatorname{Frac}A$에 대한 minimal polynomial이라 하자. 그럼 이들 계수들은 모두 $A$에 속하고, $f(\mathrm{x})$의 irreducibility에 의해 $a_0\neq 0$이다. 따라서

$$a_0=-a_1x-a_2x^2-\cdots-x^{r+1}\in\mathfrak{P}\cap A.$$

특히, $A$를 field, $B$를 <span class="border-highlight">$B/A$가 integral인 integral domain</span>으로 잡으면 $B$는 field가 되어야 한다.

$\mathfrak{P}$를 $R'$의 nonzero prime ideal이라 하자. $R'$이 Dedekind domain임을 보이기 위해, 우리는 $\mathfrak{P}$가 maximal임을 보여야 한다. 앞선 claim에 의하여, $\mathfrak{p}=\mathfrak{P}\cap R$은 $R$의 nonzero prime ideal이 된다. 그런데 $R$은 Dedekind ring이므로 $R/\mathfrak{p}$는 field이다. 한편, $R'/\mathfrak{P}$는 integral domain이고 $R/\mathfrak{p}$를 포함한다. 이제 $\bar{x}=x+\mathfrak{P}$를 임의로 고르자. 그럼 $x\in R'$에 대해 integral이므로, monic polynomial

$$f(\mathrm{x})=\mathrm{x}^m+r_{m-1}\mathrm{x}^{m-1}+\cdots+r_1\mathrm{x}+r_0$$

이 존재하여 $f(x)=0$이다. 따라서, 양 변을 $\mathfrak{p}$로 나누면 $f$는 $R/\mathfrak{p}[\mathrm{x}]$의 polynomial이고, 이는 $\bar{x}$를 근으로 갖는다. 이제 $R'/\mathfrak{P}$는 $R/\mathfrak{p}$에 대해 integral이고, 그러므로 $R'/\mathfrak{P}$는 field가 되어 $\mathfrak{P}$는 $R'$의 maximal ideal이 된다.

이제 남은 것은 $R'$이 Dedekind domain이 된다는 것을 이용하여, purely inseparable extension $L/E$에서의 $R'$의 integral closure $R\'\'$ 또한 Dedekind domain이 된다는 것을 보이는 일이다. 이를 위해 우리는 $R\'\'$의 임의의 원소가 유한하게 많은 prime ideal에만 속해있으며, 또 $R\'\'$의 maximal ideal에서의 localization이 DVR이 됨을 보일 것이다. 

$L/E$는 finite-dimensional purely inseparable extension이므로, $\operatorname{char} L=p$이고, $q=p^r$에 대해 $x^q\in E$가 모든 $x\in L$에 대해 성립하도록 하는 $r>0$이 존재한다. 만약 $x\in R\'\'$이라면, $x\in E\cap R\'\'$이고, $R'$은 integrally closed이므로 $x^q\in R'$이다. 또, 반대로 만일 $x^q\in R'$이라면 $x$는 $R'$에 대해 integral이므로 $x\in R\'\'$이다. 

임의의 원소 $a\in R\'\'$에 대하여, $a$를 포함하는 $R\'\'$의 prime ideal은 많아야 유한 개 뿐이라는 것을 증명해야 한다. 이는 $R\'\'$의 prime ideal들과 $R\'$의 prime ideal들 사이의 일대일대응을 만들어서 해결할 것이다. $\mathfrak{P}$가 $R\'\'$의 nonzero prime ideal이라 하자. 그럼 $\mathfrak{p}=\mathfrak{P}\cap R'$은 $R'$의 nonzero prime ideal이고, 따라서 $\mathfrak{p}$는 maximal이다. 그럼 이제 임의의 $x\in\mathfrak{P}$에 대하여, $x^q\in\mathfrak{p}$이다. 반대로 만일 $x^q\in\mathfrak{p}$라면 $x$는 $R'$에 대해 integral이므로 $R\'\'$에 포함된다. 따라서 이는 prime ideal들 사이의 correspondence가 되고, $a^q$를 포함하는 $R'$의 prime ideal은 유한 개 뿐이므로, $a$를 포함하는 $R\'\'$의 prime ideal 또한 유한 개 뿐이다. 

이제 마지막으로, 임의의 maximal ideal $\mathfrak{P}\subset R\'\'$에 대해 $R_\mathfrak{P}\'\'$이 DVR이 됨을 보이자. 만일 $R'$이 DVR이었다면, $R\'\'$의 임의의   nonzero maximal ideal $\mathfrak{P}$와 $\mathfrak{p}=R'\cap\mathfrak{P}$에 대하여 $S=R'\setminus\mathfrak{p}$가 $R'$, $R\'\'$ 모두에서 multiplicative set이 될 것이다. 또 $S\subset R\'\'\setminus \mathfrak{P}$이므로 $R\'\'\_S\subset R\'\'\_\mathfrak{P}$이다. 그런데, 반대로 임의의 $x/y\in\mathfrak{R}\'\'_\mathfrak{P}$에 대하여, $y^q\in R'$이지만 $y\not\in\mathfrak{p}$이고, 따라서 $y^q\in S$이므로 $x/y=xy^{q-1}/y^q\in R\'\'_S$이기도 하다. 그러므로, 다음의 claim만 보이면 나머지는 자명하다.

> $R\'$이 quotient field $E$를 갖는 DVR이고, $R\'\'$이 finite-dimensional purely inseparable extension $L/E$에서 $R'$의 integral closure라 하자. 그럼 $R\'\'$도 DVR이다.  
</details>

## Ramification index and relative degree

$R\subset R'$이 Dedekind domain들이고, $K,L$이 이들의 quotient field라 하자. 우리는 이 상황에서, $R$의 prime ideal과 $R'$의 prime ideal이 갖는 관계를 살펴볼 것이다.

$\mathfrak{p}$가 $R$의 prime ideal이라 하자. 그럼 $\mathfrak{p}R'$은 $R'$에서의 (prime일 필요는 없는) ideal이 된다. $R'$은 Dedekind ring이므로, 이 ideal $\mathfrak{p}R'$은 다음의 식

$$\mathfrak{p}R'=\mathfrak{P}_1^{e_1}\cdots\mathfrak{P}_g^{e_g}$$

과 같이 factorization이 가능하다. 여기서 $\mathfrak{P}_i$들은 모두 $R'$의 서로 다른 prime ideal들이고, $e_i$들은 양의 정수이다. $R$의 prime ideal $\mathfrak{p}$의 $R'$에서의 image를 생각하자. 정의에 의해 $\mathfrak{p}$는 $\mathfrak{p}R'$에 속하고, 따라서 $\mathfrak{p}$는 모든 $\mathfrak{P}_i$들에도 속한다. 그럼 $\mathfrak{p}\subset\mathfrak{P}_i$의 양 변에 $R$과의 교집합을 취해주면, $\mathfrak{p}=\mathfrak{p}\cap R\subset\mathfrak{P}_i\cap R$이고, Dedekind domain에서 모든 prime ideal은 maximal이므로, $\mathfrak{p}=\mathfrak{P}_i\cap R$이 성립한다. 즉 $\mathfrak{P}_i$들은 모두 $\mathfrak{p}$ 위에 lying over하는 prime ideal들이다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $R\subset R'$이 Dedekind domain들이고, $\mathfrak{P}$가 $R'$의 nonzero prime ideal, 그리고 $\mathfrak{p}=R\cap\mathfrak{P}$라 하자. 그럼 $\mathfrak{P}$의 $R$에 대한 *ramification index*는 $\mathfrak{p}R'$의 $R'$에서의 factorization에서 나타나는 $\mathfrak{P}$의 지수다. 이를 $e(\mathfrak{P}/R)$ 혹은 $e(\mathfrak{P}/\mathfrak{p})$와 같이 쓴다.

</div>

한편, 이와 밀접한 관련을 갖는 relative degree라는 것이 있다. 이를 정의하기 위해선 우선 다음의 보조정리가 필요하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $R\subset R'$이 Dedekind domain들이고, $K\subset L$이 이들의 quotient field라 하자. $\mathfrak{A}$가 $\mathfrak{A}\cap R=\mathfrak{p}\neq 0$을 만족하는 $R'$의 ideal이라면, $R'/\mathfrak{A}$는 $R/\mathfrak{p}$-vector space이고, 그 dimension은

$$[R'/\mathfrak{A}:R/\mathfrak{p}]\leq[L:K]$$

을 만족한다. 

</div>

따라서, $L/K$가 finite extension이라면 항상 $[R'/\mathfrak{A}:R/\mathfrak{p}]$는 유한하다는 것을 알 수 있다. 그럼 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> $R\subset R'$이 Dedekind domain들이고, $\mathfrak{P}$가 $R'$의 nonzero prime ideal이며 $\mathfrak{p}=R\cap\mathfrak{P}$라 하자. 그럼 field extension의 degree $[R'/\mathfrak{P}:R/\mathfrak{p}]$는 $\mathfrak{P}$의 $\mathfrak{p}$에 대한 *relative degree*라 부르고, 이를 $f(\mathfrak{P}/\mathfrak{p})$ 혹은 $f(\mathfrak{P}/R)$로 적는다. 

</div>

이들 사이에는 다음과 같은 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> $R\subset R'$이 Dedekind domain들이고, $R'$이 $R$에 대해 integral이며, $\mathfrak{p}$가 $R$의 nonzero prime ideal이라 하자. $\mathfrak{p}R'$의 factorization

$$\mathfrak{p}R'=\mathfrak{P}_1^{e_1}\cdots\mathfrak{P}_g^{e_g}$$

가 주어졌다 하고, $f_i=f(\mathfrak{P}_i/R)$로 정의하자. 그럼

1. $\sum e_if_i$는 $R'/\mathfrak{p}R'$의 $R/\mathfrak{p}$에 대한 dimension과 같다.
2. 따라서, 만일 $K$, $L$이 $R$, $R'$의 quotient field들이고 $[L:K]$가 유한하다면 $\sum e_if_i\leq[L:K]$가 성립한다.
3. 특히, 만약 $S=R\setminus\mathfrak{p}$이고, $R_S'$가 $R_S$-module로서 finitely generated라면 등호가 성립한다.

</div>

세 번째 조건은 특히 $R$이 Dedekind ring이고, $K=\operatorname{Frac}R$, $L/K$가 finite-dimensional separable extension, 그리고 $R'$이 $R$의 $L$에서의 integral closure일 때 성립한다. 이는 우리가 항상 다뤄왔던 경우와 동일하다.

그런데 만일 여기에 더해 $L/K$가 normal extension이기도 하다면, 즉 $L/K$가 Galois라면 다음과 같이 더 강력한 결과가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> $R$이 Dedekind domain, $K=\operatorname{Frac}R$이고 $L/K$가 finite-dimensional Galois extension, 그리고 $R'$이 $R$의 $L$에서의 integral closure라 하자. 그럼 임의의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{p}R'$은 다음과 같은 factorization

$$\mathfrak{p}R'=(\mathfrak{P}_1\cdots\mathfrak{P}_g)^e$$

를 갖는다. 따라서 $\mathfrak{P}_i$들의 ramification index는 모두 $e$로 동일하다. 추가적으로, 각각의 relative degree들 $f(\mathfrak{P}_i/\mathfrak{p})$도 모두 서로 같으며, 이 값을 $f$라 하면 따라서 다음의 식 $efg=[L:K]$이 성립한다.

</div>

## Ramification

여기에서 $R$은 Dedekind domain, $K=\operatorname{Frac}R$, $L/K$는 finite-dimensional separable extension이고 $R'$은 $L$에서의 $R$의 integral closure이다. 

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> $\mathfrak{P}$가 $R'$의 nonzero prime ideal이고, $\mathfrak{p}=R\cap\mathfrak{P}$라 하자. $\mathfrak{P}$가 $R$에 대해 *ramified*되어있다는 것은 $e(\mathfrak{P}/R)>1$이거나 $R'/\mathfrak{P}$가 $R/\mathfrak{p}$에 대해 separable하지 않은 것이다. 만약 $\mathfrak{p}R'$이 어떤 ramified prime ideal $\mathfrak{P}$로 나뉜다면, $\mathfrak{p}$를 $R'$에서 *ramified*되어있다고 말한다.   

</div>

또, $x_1,\ldots, x_n$이 $L/K$의 basis라 하자. 그럼 

$$\Delta(x_1,\ldots, x_n)=\det[T(x_ix_j)]$$

를 이 basis의 *discriminant*라 부른다. 만일 이들 원소들이 모두 $R'$의 원소라면, 즉 이 basis가 integral basis라면 $\Delta$는 $R$에 속하게 된다. 이러한 *모든* integral basis $(x_i)$에 대해 $\Delta(x_1,\ldots, x_n)$듫을 모아둔 집합을 생각할 수 있는데, 이 집합은 $R$의 ideal이 되며, 우리는 이를 $R'$의 *discriminant ideal*이라 부르고 $\Delta(R'/R)$로 적는다. 

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> $S$가 $R$의 multiplicative subset이라면, $\Delta(R_S'/R_S)=\Delta(R'/R)_S$가 성립한다.

</div>

대부분의 경우 $R'$은 free $R$-module로 생각할 수 있는데, 이 경우에는 다음의 보조정리가 매우 유용하다.

<div class="proposition" markdown="1">

<ins id="lem9">**보조정리 9**</ins> 만일 $R'$이 free $R$-module이고, 이들의 free generator들이 $x_1,\ldots, x_n$이라면 다음의 식

$$\Delta(R'/R)=\Delta(x_1,\ldots, x_n)R$$

이 성립한다.

</div>

Discriminant ideal이 중요한 이유는 다음 정리 때문이다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> $R'$에서 ramify되는 $R$의 prime ideal들은 $\Delta(R'/R)$을 포함하는 것들이다.

</div>

## Kummer's theorem

하지만 $\mathfrak{p}R'$의 factorization을 찾는 것이 항상 쉬운 것은 아니다. Kummer's theorem은 이런 경우를 종종 해결해준다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11 (Kummer)**</ins> $\mathfrak{p}$가 nonzero prime ideal이라 하자. 만일 어떤 $\theta\in L$이 존재하여 $R_\mathfrak{p}$의 $L$에서의 integral closure가 $R_\mathfrak{p}[\theta]$이도록 할 수 있다면, $\theta$의 minimal polynomial이 존재한다. 이를 $f(\mathrm{x})\in K[\mathrm{x}]$라 하고, $\bar{f}(\mathrm{x})$를 $f(\mathrm{x})$의 계수들을 $\mathfrak{p}$로 reduce하여 얻어진 $R/\mathfrak{p}[\mathrm{x}]$의 다항식이라 하자. $\bar{f}$가 다음의 식

$$\bar{f}(\mathrm{x})=g_1(\mathrm{x})^{a_1}\cdots g_t(\mathrm{x})^{a_t}$$

으로 인수분해된다면, 적당한 $R'$의 prime ideal들이 존재하여

$$\mathfrak{p}R'=\mathfrak{P}_1^{a_1}\cdots\mathfrak{P}_t^{a_t}$$

가 성립하며, 이 때 $\mathfrak{P}_i$들의 relative degree $f(\mathfrak{P}_i/R)$은 정확히 $g_i$들의 degree와 같다. 

</div>

이 정리는 앞서 말한대로 꽤 유용하지만, 전제조건을 맞추는 것이 그렇게 쉽지는 않다. $L$은 $K$에 대한 separable extension이니 primitive element theorem을 쓸 수 있지만, 일반적으로 $R'$은 field는 아니므로 이런 도구가 없기 때문이다. 따라서 다음과 같이 이럴 때 사용한 도구를 미리 만들어둬야 한다.

<div class="proposition" markdown="1">

<ins id="lem12">**보조정리 12**</ins> $[L:K]=n$이라 하자. $\theta$를 $K(\theta)=L$을 만족하는 $R'$의 원소라 하고, $\Delta(\theta)=\Delta(1,\theta,\ldots,\theta^{n-1})$이라 하면 

1. $\Delta(\theta)R'\subset R[\theta]\subset R'$이고
2. 만일 $\mathfrak{p}$가 $\Delta(\theta)$룰 포함하지 않는 prime ideal이라면, $S=R\setminus\mathfrak{p}$에 대해 $R'\_S=R\_\mathfrak{p}[\theta]$가 성립한다.

</div>

이 보조정리를 잘 사용하려면 다음과 같이 power basis의 discriminant를 계산하는 또 다른 보조정리가 있으면 편하다.

<div class="proposition" markdown="1">

<ins id="lem13">**보조정리 13**</ins> $L=K(\theta)$가 dimension $n$의 separable extension이라 하고, $f(\mathrm{x})$가 $\theta$의 minimum polynomial이라 하자. 그럼 다음의 식

$$\Delta(\theta)=(-1)^{n(n-1)/2}N_{L/K}(f'(\theta))$$

이 성립한다.

</div>
---

**References**

[Jan] Gerald J. Janusz. *Algebraic Number Fields*, American  Mathematical Soc., 1995

---
