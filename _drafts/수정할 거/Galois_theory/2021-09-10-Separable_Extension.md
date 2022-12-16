---

title: "Separable Extensions"
excerpt: "Separability"

categories: [Math / Galois Theory]
permalink: /ko/math/galois_theory/separable_extension
header:
    overlay_image: /assets/images/Galois_theory/Separable_extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-09-10
last_modified_at:
weight: 5

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


Separable extension을 정의하기 위해 지금까지 먼 길을 달려왔는데, 드디어 정의를 할 수 있다.

## Separable algebraic extensions

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $K$의 algebraic extension $E$가 *separable*인 것은, $E$의 subextension 가운데 finite degree를 갖는 extension들이 모두 etale-$K$-algebra인 것이다.

</div>

사실 separable *algebraic* extension은 그렇게 흥미로운 경우는 아니다. 임의의 finite degree를 갖는 etale $K$-algebra의 subextension은 항상 etale abgebra이기 때문에, 이 경우는 etale algebra의 특수한 경우가 된다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $E$가 $K$의 algebraic extension이라 하자. 만일 $E$가 separable이라면, $E$의 임의의 subextension $E'$도 separble이다. 거꾸로, $E$의 임의의 finite-degree subextension이 separable이라면 $E$도 separable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$E$가 separable이라면, $E$의 임의의 subextension $E'$에 대해, $E'$의 finite-degree subextension은 $E$의 finite-degree subextension이기도 하므로 $E'$가 separable이다. 반대 방향은 자명.

</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Field $K$가 perfect인 것은 $K$의 임의의 algebraic extension이 separable인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $K$가 perfect라 하자. 그럼 $K$의 임의의 extension은 (그 자체로 field이므로), [§Etale Algebra, 보조정리 14](/ko/math/galois_theory/etale_algebras#pp14)에 의하여 etale $K$-algebra이다. 따라서 $K$의 임의의 algebraic extension은 separable이다. 

반대 방향을 보이기 위해, 결론에 반하여 $K$가 characteristic $p$의 imperfect field라 하자. $K$가 imperfect이므로, 어떤 $b\in K$가 존재하여 $b\not\in K^p$이다. $a=b^{1/p}$라 하자. 그럼 $K(a)$는 $K$의 $p$-radical extension이고, $K$의 algebraic closure $\Omega$를 생각하면, $p$-radical extension의 성질에 의해 $K(\alpha)$에서 $\Omega$로의 유일한 $K$-homomorphism이 존재한다. 그런데 $[K(a):K]>1$이므로, $[K(a):K]_s\neq [K(a):K]$이고 따라서 $K(a)$는 etale이 아니게 되어 $K(a)$가 non-separable finite-degree extension field가 된다. 

</details>

다음 보조정리는 원래 [§Etale Algebras, 정리 15](/ko/math/galois_theory/etale_algebras#pp15)에 붙어있었어야 하나, separable extension이라는 것을 아직 정의하지 않아 남겨뒀던 것이다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Field $K$에 대해서, $A$가 finite degree를 갖는 $K$-algebra라 하자. 그럼 다음이 동치이다.

- $A$가 etale $K$-algebra이다.
- 적당한 separable algebraic extension $L_1,\ldots, L_n$들이 존재하여, $A$는 $L_1\times\cdots\times L_n$과 isomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $A$가 etale $K$-algebra라 가정하자. 그럼 [§Etale Algebras, 정리 15](/ko/math/galois_theory/etale_algebras#pp15)에 의해서, $A$는 reduced이다. 이제 [§Etale Algebras, 정리 13](/ko/math/galois_theory/etale_algebras#pp13)에 의해, $A\cong L_1\times\cdots\times L_n$이 성립한다. 이들은 etale algebra $A$의 quotient algebra로 볼 수 있으므로 각각 etale이고, 따라서 separable이다. 

반대방향 또한 $L_i$들이 모두 etale이어야 하므로 자명하다. 

</details>

이제 드디어 우리가 그 동안 motivation이라고 주장했지만 한 번도 등장하지는 않았던, separable polynomial이 나온다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> Field $K$에 대하여, $f\in K[X]$가 nonzero polynomial이고, $\Omega$가 $K$의 algebraically closed extension이라 하자. 그럼 다음이 모두 동치이다.

1. $f$와 $f'$가 relatively prime이다.
2. $f$의 $\Omega$에서의 모든 근들이 simple root이다.
3. $K$의 extension $L$이 존재하여, $f$는 $L[X]$에서 linear factor들로 완전히 인수분해된다.
4. $K[X]/(f)$가 etale이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[$1\implies 2$] $f$와 $f'$가 relatively prime이므로, 적당한 두 개의 polynomial $g$, $h$가 존재하여 $fg+f'h=1$을 만족한다. 이제 $a\in\Omega$가 $f$의 근이라고 하면, 

$$f'(a)h(a)=f(a)g(a)+f'(a)h(a)=1$$

이므로 $f'(a)\neq 0$이고, 따라서 $a$는 simple root이다. 

[$2\implies 3$] 만일 $f$의 $\Omega$에서의 모든 근 $a\in\Omega$가 simple이라면, $\Omega[X]$에서 $f$를 완전히 split할 수 있으므로, $L=\Omega$로 잡으면 된다.

[$3\implies 4$] 만일 $f$가 $L[X]$ 상에서 linear factor들 $f_1,\ldots, f_n$들로 인수분해된다고 하자. 그럼 우리는 $L$-algebra들의 homomorphism

$$(K[X]/(f))\otimes_KL\cong L[X]/(f)\cong\prod L[X]/(f_i)\cong L^n$$

이므로 $K[X]/(f)$는 $L$로 diagonalize되고, 따라서 etale이다. 

[$4\implies 1$] 마지막으로 $K[X]/(f)$가 etale이라 가정하자. 우선 $\Omega_K(K[X]/(f))$는 $f'(x)dx=0$을 만족하는 $dx$에 의해 generate되는 $K[X]/(f)$-module이다. 따라서 $K[X]/(f)$가 etale이 되기 위해서는, $f'(X)$가 $K[X]/(f)$에서 invertible해야하고, 따라서 $f$와 $f'$가 $K[X]$에서 relatively prime이어야 한다. 

</details>

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 위의 동치조건들을 만족하는 nonzero polynomial $f\in K[X]$를 *separable polynomial*이라 부른다.

</div>

추가적으로, separable polynomial은 다음 성질들을 갖는다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $f$가 $K[X]$의 irreducible polynomial이라 하자. 그럼 다음이 모두 동치이다.

1. $f$는 separable이다.
2. $K$의 extension $L$이 존재하여, $f$는 $L$에서 simple root를 갖는다.
3. $f'$가 0이 아니다.


</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1번이 2번을, 2번이 3번을 imply하는 것은 모두 자명하다. 따라서 3번이 1번을 imply하는 것만 보이면 충분하다. $f'\neq 0$이라 하고, $x\in\Omega$를 $f$의 어떤 근이라 하자. 그럼 $f$는 $x$의 minimal polynomial이고 $\deg f'&lt;\deg f$이므로 $f'$는 $x$를 근으로 가질 수 없다. 따라서 $x$는 $f$의 simple root다. 

</details>

이제 separable algebraic extension을 어떻게 정의해야 하는지는 분명하다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> $E$가 $K$의 extension field라 하자. 그럼 $K$에 대해 algebraic한 $x\in E$가 *separable*하기도 하다는 것은, $K(x)$가 $K$에 대한 separable extension인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $E$가 $K$의 extension field이고, $x\in E$가 $K$에 대해 algebraic한 원소이고 $f$가 $x$의 minimal polynomial이라 하자. 그럼 다음이 모두 동치이다.

1. $x$가 separable이다.
2. $f$가 separable이다.
3. $x$가 $f$의 simple root이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

자명.

</details>

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> <#content#>

</div>

## Purely inseparable extensions

여러가지 이유에서 separable extension만큼 중요하게 사용되는 것은 정반대의 개념인 *purely inseparable extension*이다. 이건 separable extension을 더 잘 이해하도록 도와주기도 하고, 또 우리가 앞으로 해나갈 이야기의 많은 부분에서 도움을 준다.

Algebraic extension $F/K$가 separable이라는 것은, 임의의 $u\in F$에 대해, $u$의 minimal polynomial $f$가 separable한 것은 $f$가 중근을 갖지 않는 것으로 정의된다. 따라서 [명제 7](#pp7)을 적용하면, 이는 다시 $f'$가 nonzero인 것과 동치이다. 즉, 만일 $\operatorname{char}K=0$이라면, nontrivial한 irreducible polynomial $f'$가 $f'=0$을 만족할 방법은 없고, 따라서 algebraic extension $F/K$가 항상 separable이다. 

Separable extension은 algebraic extension이 아닌 경우에도 정의되긴 하지만, 위와 같은 이유로 우리가 purely inseparable extension을 생각할 때는 (항상 separable한) $\operatorname{char}K=0$ 대신, $\operatorname{char}K=p$인 경우만 생각한다. 따라서, 남은 부분에서 별 말이 없으면 $K$는 characteristic $p$의 field이다.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> Field $K$와, $K$의 extension $E$에 대하여, $\alpha\in E$가 $K$에 대해 *$p$-radical*이라는 것은 어떤 integer $m\geq 0$이 존재하여 $\alpha^{p^m}\in K$인 것이다. 이러한 정수 $m$ 중 가장 작은 것을 $K$에 대한 $\alpha$의 *height*라 부른다. 

</div>

뜬금없이 이런 정의를 생각하는 것은 다음과 같은 이유가 있다. Algebraic element $\alpha$가 separable한 것은, $\alpha$의 minimal polynomial이 simple root들로 완전히 인수분해되는 것이므로, 이 개념의 반대개념, 즉 purely inseparable한 원소는 minimal polynomial이 중근을, 그것도 $(x-\beta)^m$과 같은 식으로 인수분해되는 것으로 정의된다. 그런데 freshman's dream을 생각하면, 이를 위해서는 $m=p^e$여야 한다는 것을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> Field $K$의 extension $E$와, height $e$를 가지는 $p$-radical element $\alpha$를 생각하자. 즉, 어떠한 $a\in K$에 대해 $\alpha^{p^e}=a$이다. 그럼 $\alpha$의 minimal polynomial은 $X^{p^e}-a$이며, 따라서 $[K(\alpha):K]=p^e$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$X^{p^e}-a$가 $\alpha$를 근으로 가진다는 것은 자명하므로, 이것이 irreducible임만 보이면 충분하다. 한편, 만일 $a\in K^p$였다면, $\alpha^{p^e}=b^p$가 어떤 $b\in K$에 대해 성립했을 것이므로, 이는 $e$의 minimality에 모순이다. 

$K$의 algebraic closure $\Omega$를 생각하자. 그럼 $\Omega$는 $K[X]$의 임의의 polynomial들의 근을 모두 포함하므로, 특히 $X^{p^e}-a=0$도 $\Omega$에서 근을 가진다. 이를 $b=a^{p^{-e}}$라 하자. $g$를 $b$의 ($K$에서의) minimal polynomial이라 하면, $f(X)=(X-b)^{p^e}$이고 ([§Field Extensions, 명제 5](/ko/math/galois_theory/field_extensions#pp5)) 따라서 $f$를 나누는 임의의 irreducible polynoial은 $b$를 근으로 가져야 한다. 이 말은 즉 $f$를 나누는 irreducible polynomial은 정확히 $g$ 뿐이라는 뜻이고, 따라서 $f=g^q$가 성립한다. 이제 차수를 고려하면, $q=p^f$여야 하는데, $g$의 constant term을 $c$라 하고 $g^q$와 $f$의 상수항을 비교하면 $c^q=-a$를 얻는다. 이는 $a\not\in K^p$에 모순이므로 $q=1$이고, $f=g$여야 한다. 따라서 $f$는 irreducible이다.   

</details>

$p$-radical element를 정의했으면, $p$-radical extension을 어떻게 정의할지는 뻔하다.

<div class="definition" markdown="1">

<ins id="df13">**정의 13**</ins> Field $K$의 extension $E$가 $p$-radical이라는 것은 $E$의 임의의 원소가 $p$-radical인 것이다. 만일 $E$의 각각의 원소들의 height를 모두 유한하게 bound시킬 수 있다면, 이들 원소들의 height 중 가장 큰 것을 $E$의 height로 정의한다.

</div>

앞서 언급한 것과 같이, $p$-radical extension은 흔히 *purely inseparable extension*이라 불린다. 

한편, extension $E/K$가 주어졌다 하고, 각각의 $n$에 대하여 $E\_n$이 height$\leq n$의 purely inseparable element들을 모아둔 집합이라 하자. 그럼 $E\_n$은 $E$의 homomorphic image이므로 field이고, 따라서 $E\_\infty=\bigcup E\_n$은 $E$의 subextension들의 ascending chain이 된다. 따라서 우리는 $E\_\infty$ 또한 $E$의 subextension이라는 것을 알 수 있고, 이는 $E$에 속한 $K$의 purely inseparable extension 중 가장 큰 것이 된다. 이를 종종 $K$의 ($E$에 대한) *relative purely inseparable closure*라 부른다. 

## Separable and inseparable degrees

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14**</ins> $E/K$가 extension이라 하자. 집합 $E_s$를 $K$에 대해 separable한 모든 algebraic element들의 모임이라 하면, $E_s$는 algebraic하고 separable한 $E$의 subextension 가운데 가장 큰 것이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

*증명.* [명제 10](#pp10)에 의하여 분명하다.

</details>

이 때, $E_s$를 $E$에 대한 $K$의 *reltaive separable closure*라 부르기도 한다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp15">**명제 15**</ins> $E/K$가 algebraic extension이고, $E_s$를 $K$의 relative separable closure라 하자. 그럼 다음이 성립한다.

1. $E$는 $E_s$의 purely inseparable extension이다.
2. 만일 $F$가 $E$의 subextension이고, $E$가 $F$의 purely inseparable extension이라면 $F\supset E_s$이다.
3. 따라서, $E_s$는 $K$에 대해 separable이고 $E$가 $E_s$에 대해 purely inseparable이도록 하는 유일한 subextension이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

<#content#>

</details>

사실 우리는 separable이라는 말을 처음 본 것이 아니다. ([정의 ]()) 

<div class="proposition" markdown="1">

<ins id="pp16">**명제 16**</ins> $E_s$가 $E/K$에서의 relative separable closure라 하자. 그럼 $[E:K]_s=[E_s:K]$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

<#content#>

</details>

그러므로, 

$$[E:K]=[E:E_s][E_s:K]$$

는 이제 다음의 식

$$[E:K]=[E:K]_s[E:K]_i$$

으로 바꿔 쓸 수 있다. 여기서 $[E:K]_i=[E:E_s]$를 *inseparable degree*라 부른다. 

<div class="proposition" markdown="1">

<ins id="pp17">**명제 17**</ins> <#content#>

</div>


---
**Reference**

**[BCH]** N. Bourbaki, P.M. Cohn, and J. Howie. <i>Algebra II: Chapters 4 - 7</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013. 

---
