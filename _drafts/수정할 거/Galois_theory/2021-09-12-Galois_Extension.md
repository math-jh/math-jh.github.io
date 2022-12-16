---

title: "Galois Extension"
excerpt: "Galois Extension of fields"

categories: [Math / Galois Theory]
permalink: /ko/math/galois_theory/galois_extension
header:
    overlay_image: /assets/images/Galois_theory/Galois_extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2021-09-12
last_modified_at:
weight: 7

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


이제 드디어 갈루아라는 이름이 나오기 시작한다. 참고로 부르바키가 quasi-Galois extension이라 부르는 건 최근의 책들에서는 normal extension이라 부르는 것이다. 이 글에서, $K$는 field, $\Omega$는 $K$의 algebraic closure라 하자.

## Conjugate elements

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> $E$가 $\Omega$의 sub-$K$-extension이라 하고, $u:E\rightarrow\Omega$가 $K$-homomorphism이라 하자. 그럼 

1. 만일 $u$가 $E$에서 $E$로의 homomorphism이라면, $u$는 $E$ 위에 $K$-automorphism을 정의한다.
2. $u$를 extend하는 $\Omega$ 위의 $K$-automorphism이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫번째를 보여야 한다. $u$가 $E$에서 $E$로의 homomorphism이라는 이야기는 $u(E)\subset E$라는 것이다. 우리는 이걸 가정한 후, 사실은 정확히 등호가 성립해서 $u(E)=E$라는 것을 보여야 한다. 따라서, 임의의 $x\in E$를 택하자. $E$는 $K$의 algebraic extension이므로 $x$의 minimal polynomial $f$가 존재한다. 이제, $f$의 $E$에서의 근들의 집합을 $\Phi$라 하자. 그럼 $\Phi$의 원소의 개수는 많아야 $\deg f$개이므로, $\Phi$는 유한집합이다. 한편, $\alpha\in\Phi$라 하자. 그럼 $f(\alpha)=0$에서

$$a_n\alpha^n+\cdots+a_1\alpha+a_0=0$$

인데, 위 식의 양 변에 $u$를 취하면, $u$는 $K$-homomorphism이므로 $u(a_i)=a_i$이고, 따라서

$$a_n(u(\alpha))^n+\cdots+a_1(u(\alpha))+a_0=0\tag{1}$$

이 성립한다. 즉, $u(\Phi)\subset\Phi$이다. 그런데, $u$는 domain이 field이므로 injective일 수밖에 없고, 따라서 $u(\Phi)=\Phi$여야 한다. 그럼 $x\in u(\Phi)\subset u(E)$이고, 따라서 $E=u(E)$가 성립한다. 

한편, $\Omega$는 $E$와 $u(E)$의 algebraic closure이므로, [§Algebraic Extensions, 정의 7](/ko/math/galois_theory/algebraic_extensions#df7) 직후의 remark에 의해 $u$에서 $u(E)$로의 isomorphism이 또 다른 isomorphism $v:\Omega\rightarrow\Omega$으로 확장된다는 것을 알 수 있다.

</details>

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $E$, $F$가 $\Omega$의 sub-$K$-extension들이라 하자. 그럼 $E$와 $F$가 *conjugate*이라는 것은 $\Omega$의 어떠한 $K$-automorphism $u$가 존재하여 $u(E)=F$인 것이다. 비슷하게, $\Omega$의 두 원소 $x$, $y$가 *conjugate*이라는 것은 어떤 $K$-automorphism $u$가 존재하여 $u(x)=y$인 것이다.

</div>

관계 $R$을

> $x\equiv y\mod R$ if and only if $x$ and $y$ are conjugate over $K$

으로 정의하면, $R$은 $\Omega$ 위에 equivalence relation을 정의한다. $R$에 의해 생기는 equivalence class를 각각 *conjugacy class*라 부른다. 만일 우리가 $\Omega$ 위의 $K$-automorphism들의 group $\operatorname{Aut}_K\Omega$를 생각한다면, 이들은 $\operatorname{Aut}_K\Omega$가 $\Omega$ 위에 act할 때의 orbit이 된다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $\alpha$, $\beta$가 $\Omega$의 원소들이라 하자. 다음이 모두 동치이다.

1. $\alpha$와 $\beta$가 conjugate이다.
2. $\alpha$, $\beta$의 minimal polynomial이 동일하다.
3. 적당한 $K$-isomorphism $v:K(\alpha)\rightarrow K(\beta)$가 존재하여 $v(\alpha)=\beta$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\alpha$와 $\beta$가 conjugate이라 하자. 그럼 $u\in\operatorname{Aut}_K\Omega$가 존재하여 $u(\alpha)=\beta$이다. $\alpha$의 minimal polynomial을 $f$라 하자. 그럼 (1)의 계산과 마찬가지로, 

$$f(\beta)=f(u(\alpha))=u(f(\alpha))=0$$

이 성립한다. 또, $f$는 $K[x]$에서 monic, irreducible polynomial이었으므로, $f$는 $\beta$의 minimal polynomial이다. 따라서 2번이 성립한다.

이제 $\Omega$의 두 원소 $\alpha$, $\beta$가 같은 minimal polynomial을 갖는다 하자. 그럼 minimal polynomial의 성질에 의해 ([§Algebraic Extensions, 명제 2](/ko/math/galois_theory/algebraic_extensions#pp2)), $K[x]/(f)\cong K(\alpha)$가 성립하고, 비슷하게 $K[x]/(f)\cong K(\beta)$이기도 하다. 이 isomorphism들은 $x+(f)\mapsto \alpha$, $x+(f)\mapsto\beta$로 주어지므로, 이들 isomorphism의 합성이 $v(\alpha)=\beta$를 만족하는 $K$-isomorphism이 된다.

마지막으로, $v(\alpha)=\beta$를 만족하는 $K$-isomorphism $v:K(\alpha)\rightarrow K(\beta)$가 존재한다고 가정하자. 그럼 $v$를 $\Omega$ 전체로 extend할 수 있다. ([명제 1](#pp1)) 따라서 정의에 의해 $\alpha$와 $\beta$가 conjugate이다. 

</details>

임의의 $\alpha\in\Omega$를 생각하자. $\alpha$의 minimal polynomial $f$의 degree를 $n$이라 하면, $\alpha$와 conjugate한 원소들은 모두 $f$의 근들이므로, $\alpha$와 같은 conjugacy class에 들어있는 원소는 많아야 $n$개이다. 만일 $\alpha$가 여기에 더해 *separable*한 원소라면, $f$가 $\Omega$에서 simple root들만 가져야 하므로, $\alpha$와 같은 conjugacy class에 들어있는 원소는 *정확히* $n$개이며 그 역도 성립한다. 

## Quasi-Galois extensions

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> $K$의 extension $E$가 ($K$에 대하여) *quasi-Galois*라는 것은, $E$가 algebraic extension이고, $E$에서 근을 갖는 임의의 irreducible $f\in K[x]$가 $E$에서 linear factor들로 완전히 인수분해되는 것이다.

</div>

예를 들어, $K$의 algebraic closure는 quasi-Galois다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $E$가 $\Omega$의 sub-$K$-extension이라 하자. 다음이 모두 동치이다.

1. $E$가 $K$의 quasi-Galois extension이다.
2. $E$는 non-constant polynomial $f\in K[x]$들의 splitting extension이다.
3. $\Omega$의 임의의 $K$-automorphism이 $E$를 $E$로 보낸다.
4. $E$에서 $\Omega$로의 임의의 $K$-homomorphism은 $E$를 자기 자신으로 보낸다.
5. 임의의 $x\in E$에 대하여, $x$의 conjugate들도 모두 $E$에 속한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 3과 4가 동치인 것은 말할 것도 없다. 따라서 네 가지 명제들 사이의 동치관계만 보이면 된다.

Quasi-Galois extension의 정의에 의하여, $E$가 $K$의 quasi-Galois extension이라면 임의의 $\alpha\in E$에 대하여, $\alpha$의 minimal polynomial $f$는 $E$에서 완전히 인수분해되어야 한다. 따라서 2번이 성립한다.

이제 2번을 가정하고, $\Omega$의 임의의 $K$-automorphism $u$가 주어졌다 하자. 각각의 non-constant polynomial $f$에 대하여, $u$는 $f$의 근들의 집합 $R_f$의 bijection을 유도한다. ([명제 1](#pp1)의 증명) 그런데 $E=K(\bigcup R_f)$이므로, $u(E)=E$이다. 

한편, conjugate element의 정의에 의해 3번 (4번) 조건이 성립하면 5번 조건이 성립하는 것도 자명하다.

마지막으로 5번 조건이 성립한다 하고, $f$를 근 $\alpha\in E$를 갖는 $K[x]$의 monic irreducible polynomial이라 하자. 우리는 $f$가 사실 $E$ 상에서 완전히 인수분해된다는 것을 보여야 한다. $\Omega$는 우선 algebraically closed이므로, $a_k\in \Omega$들이 존재하여 $f(x)=\prod(x-a_k)$로 인수분해할 수 있다. 그런데, $a_k$들은 $\alpha$와 conjugate한 원소들이며, 가정에 의해 $E$에 속해야 한다. 따라서 1번이 성립한다.

</details>

Quasi-Galois extension $E$를 생각하자. 만일 $E$가 또 다른 $\Omega$의 sub-$K$-extension과 conjugate이라면, 즉 어떤 $u\in\operatorname{Aut}_K\Omega$가 존재하여 $u(E)=F$라면, 위의 명제의 세 번째 동치조건에 의해 $F\subset E$여야하므로, $u$는 사실 $E$에서 $E$로의 homomorphism이고 따라서 $u(E)=E$가 되어 ([명제 1](#pp1)) $F=u(E)=E$가 성립한다. 즉, quasi-Galois extension $E$의 conjugate은 자신 뿐이다. 거꾸로 만일 $E$의 conjugate이 자기 자신뿐이라면, 임의의 $u\in\operatorname{Aut}_K\Omega$에 대해 항상 $u(E)=E$라는 것이므로, 앞선 명제의 동치조건에 의해 $E$는 quasi-Galois extension이다. 

<div class="proposition" markdown="1">

<ins id="crl5">**따름정리 5**</ins> $E$, $F$가 $E\subset F$를 만족하는 $\Omega$의 sub-$K$-extension이라 하자. 만일 $F$가 $K$에 대하여 quasi-Galois라면, $F$는 $E$에 대해서도 quasi-Galois이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $E$-automorphism $u\in\operatorname{Aut}_E\Omega$는 $K$-automorphism이기도 하므로, $F$가 $K$에 대해 quasi-Galois라면 $u(F)=F$이고 따라서 $F$는 $E$에 대해서도 quasi-Galois이다. 

</details>

<div class="proposition" markdown="1">

<ins id="crl6">**따름정리 6**</ins> $N$이 $K$의 quasi-Galois extension이고, $E$가 $N$의 subextension이라 하자. $u:E\rightarrow\Omega$가 $K$-homomorphism이라면 $u(E)\subset N$이고, 어떤  $K$-automorphism $v\in\operatorname{Aut}_KN$이 존재하여 $u$를 extend한다.

</div>

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $(N_i)_{i\in I}$가 $K$의 quasi-Galois extension들이라 하자. 그럼 $N=\bigcap N_i$와, $M=K(\bigcup N_i)$가 모두 quasi-Galois다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선, 임의의 $K$-automorphism $u\in\operatorname{Aut}_K\Omega$에 대하여 $u(N_i)=N_i$가 항상 성립하므로 $u(N)=N$이 되어 $N$은 quasi-Galois이다. 똑같은 이유로 $M$ 또한 quasi-Galois이다.

</details>

$\Omega$의 부분집합 $A$를 생각하자. 그럼 $A$의 각 원소와 conjugate한 원소들의 집합 $B=\bigcup_{u\in\operatorname{Aut}_K\Omega}u(A)$는 $u(B)=B$를 만족한다. 그럼, $K(B)$는 $K\cup B$에 의해 generate되는 field인데, $u(K)=K$, $u(B)=B$이므로 $u(K(B))=K(B)$이다. 즉, $K(B)$는 quasi-Galois extension이 되고, 여기에 더해 $A$를 포함하는 quasi-Galois extension 중 가장 작은 것이다. 따라서 $K(B)$를 $A$로 *generate*된 quasi-Galois extension이라 부른다.

특히, 방금의 정의는 다음과 같이 집합 $A$가 $K$의 extension일 때 자주 쓰이게 된다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 만일 $E$가 $K$의 finite degree를 갖는 extension이라 하면, $E$에 의해 generate되는 quasi-Galois extension 또한 finite degree를 갖는다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$E$가 $K$에 대해 finite degree를 가지므로, 어떤 유한집합 $A$에 대하여 $E=K(A)$라 할 수 있고, 따라서 $A$와 conjugate한 원소들을 모은 집합 $B$도 finite하고, 이들은 모두 $K$에 대해 finite degree를 가지므로 주어진 명제가 성립한다.

</details>

## Galois extensions

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $N$이 $K$의 algebraic extension이라 하자. 그럼 다음이 모두 동치이다.

1. $\operatorname{Aut}_KN$에 대해 invariant인 $N$의 원소들은 모두 $K$의 원소들이다.
2. $N$이 $K$의 separable, quasi-Galois extension이다.
3. 임의의 $x\in N$에 대하여, $x$의 minimal polynomial이 $N[x]$에서 linear factor들로 split한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 2번과 3번은 separable, quasi-Galois extension의 동치조건들에 의해 서로 동치이다. 따라서 1번과 이들이 동치임을 보이면 충분하다.

우선 1번을 가정하자. 임의의 $\alpha\in N$에 대하여, $\alpha$의 minimal polynomial을 $f$, 그리고 $N$에서의 $f$의 근들의 집합을 $A$라 하고

$$g(x)=\prod_{\alpha\in A}(x-\alpha)$$

를 생각하자. 임의의 $\sigma\in\operatorname{Aut}_KN$은 $A$의 permutation을 induce하므로, $g$의 계수를 고정한다. 즉, $g$는 사실 $K[x]$의 원소이고, $g(x)=0$이므로 $g$는 $f$의 배수이다. 그런데 $g$는 정의상 $f$의 factor가 아닌 factor를 가지지 않으므로, $g$는 $f$를 나누고 따라서 $g=f$이다. 즉, $x$의 minimal polynomial $f$는 $N[x]$에서 degree 1짜리 polynomial들로 split된다.

거꾸로 $\alpha\in N$이 $K$에 들어있지 않다고 하자. $N$을 포함하는 $K$의 algebraic closure $\Omega$에 대하여, $f$가 $\alpha$의 minimal polynomial이라 하면 $\alpha\not\in K$이므로 $\alpha$의 degree는 최소 2이다. 그러므로, $f(x)$의 근들의 집합 $A$도 최소 두 개의 원소를 갖는다. 즉, $\alpha\neq\beta$인 $\beta\in A$가 존재하므로, $u(\alpha)=\beta$인 $K$-automorphism $u\in\operatorname{Aut}_K\Omega$가 존재한다. 그런데 3번의 가정에 의하여, $N$은 quasi-Galois이고 따라서 $u(N)=N$이다. 그러므로 $u$에 의해 induce되는 $\sigma\in\operatorname{Aut}_KN$은 $\sigma(\alpha)=\beta\neq\alpha$를 만족하므로, 귀류법에 의해 3번은 1번을 impliy한다.

</details>

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> $K$의 extension field $N$이 *Galois extension*이라는 것은, $N$이 algebraic extension이고, 앞선 [명제 9](#pp9)의 동치조건을 만족하는 것이다.

</div>

만일 $A$가 $K$에 대해 separable한 원소들의 집합이라면, $A$에 의해 generate되는 quasi-Galois extension은 Galois extension이 된다. 특히, $K[x]$의 separable polynomial들의 splitting field는 Galois extension이 된다. 

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> $(N_i)_{i\in I}$가 $K$의 Galois extension들이라 하자. 그럼 $N=\bigcap N_i$와, $M=K(\bigcup N_i)$가 모두 Galois다.

</div>

갈루아 이론의 기본적인 정신은, 어느샌가 우리 옆에 들어와있는 $\operatorname{Aut}_NK$들을 통해 field extension을 살펴보는 것이다. 이 group을 지금까지는 임시로 $\operatorname{Aut}_KN$으로 적었는데, 이제 정식으로 이름을 주자.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> Field $K$의 Galois extension $N$에 대하여, $N$ 위에서 정의된 $K$-automorphism들의 group을 *Galois group*이라 부르고 $\operatorname{Gal}(N/K)$으로 적는다.

</div>

$K[x]$의 어떤 separable polynomial $f$가 주어졌다고 하자. $f$의 근들의 집합 $A$에 대하여, $K$의 extension field $K(A)$는 Galois extension이 된다. $N$ 위에 정의된 $K$-automorphism이 $A$를 fix하는 것은 자명하고, 또 $A$가 $N$을 generate하므로 $\sigma\in\operatorname{Gal}(N/K)$를 $A$ 위로 restrict하는 mapping은 $\operatorname{Gal}(N/K)$에서 $S_A$의 subgroup $\Gamma$로의 isomorphism이 된다. 따라서 다음이 모두 동치이다.

1. $x$, $y$가 conjugate이다.
2. $x$, $y$가 $\Gamma$ 상에서 같은 orbit에 속한다.
3. $x$, $y$가 $f$의 동일한 irreducible factor의 근이 된다. 

특히, $f$가 irreducible인 것은 $A$가 공집합이 아니고 $\Gamma$가 $A$ 위에 transitive하게 act하는 것과 동치이다. 한편, 다음의 restriction homomorphism에 대한 정리도 눈여겨볼 만 하다.

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> $\operatorname{Gal}(N/K)$에서 $\operatorname{Gal}(L/K)$로의 restriction homomorphism $\sigma\mapsto\sigma\|\_L$은 surjective이다.

</div>

## Topology of the Galois group



---
**Reference**

**[BCH]** N. Bourbaki, P.M. Cohn, and J. Howie. <i>Algebra II: Chapters 4 - 7</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013. 

---
