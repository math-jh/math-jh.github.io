---

title: "부풀림 대수"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/blowup_algebra
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Blowup_algebra.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-20
last_modified_at: 2024-10-20
weight: 11

---


이번 글에서 우리는 ring $A$의 ideal $\mathfrak{a}$를 고정하고, 이로부터 만들어지는 두 가지 graded $A$-algebra를 정의한다.

## Associated graded module

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$의 $\mathfrak{a}$에 대한 *associated graded ring*을 

$$\gr_\mathfrak{a}A= A/\mathfrak{a}\oplus \mathfrak{a}/\mathfrak{a}^2\oplus\cdots$$

으로 정의한다.  

</div>

위의 정의에서, $\gr_\mathfrak{a}A$에서의 곱셈은 임의의 $a\in \mathfrak{a}^k/\mathfrak{a}^{k+1}$, $b\in \mathfrak{a}^l/\mathfrak{a}^{l+1}$이 주어졌을 때 이들의 곱 $ab$는 우선 $a,b$ 각각의 representative $\tilde{a}\in \mathfrak{a}^k, \tilde{b}\in \mathfrak{a}^l$들의 곱 $\tilde{a}\tilde{b}$를 계산한 후 이를 다시 $\mathfrak{a}^{k+l}/\mathfrak{a}^{k+l+1}$로 제한시켜 얻어진다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 위에서 정의한 $\gr_\mathfrak{a}A$의 곱셈은 잘 정의된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

서로 다른 representative $\tilde{a}',\tilde{b}'$를 택했다 하고, 적당한 $x\in \mathfrak{a}^{k+1}$과 $y\in \mathfrak{a}^{l+1}$에 대하여 $\tilde{a}'=\tilde{a}+x,\tilde{b}'=\tilde{b}+y$라 하자. 그럼

$$\tilde{a}'\tilde{b}'=\tilde{a}\tilde{b}+y\tilde{a}+x\tilde{b}+xy$$

이고, 여기서 $x\tilde{b},y\tilde{a}\in \mathfrak{a}^{k+l+1}$, $xy\in \mathfrak{a}^{k+l+2}\subseteq \mathfrak{a}^{k+l+1}$이므로 증명이 완료된다.

</details>

이를 $A$-module로 일반화시키기 위해 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Ring $A$와 $A$의 임의의 ideal $\mathfrak{a}$, $A$-module $M$에 대하여 다음의 filtration

$$M=M_0\supseteq M_1\supseteq\cdots$$

이 *$\mathfrak{a}$-filtration<sub>$I$-여과</sub>*라는 것은 모든 $k$에 대하여 $\mathfrak{a}M_k\subseteq M_{k+1}$이 성립하는 것이다. 추가로 만일 어떠한 $n$이 존재하여 $k>n$일 때마다 $\mathfrak{a}M\_k=M\_{k+1}$이 성립하도록 할 수 있으면 이 filtration이 *$\mathfrak{a}$-stable<sub>$I$-안정적 여과</sub>*이라 한다. 

이제 임의의 $\mathfrak{a}$-filtration 

$$\mathcal{J}:\quad M=M_0\supseteq M_1\supseteq\cdots$$

에 대하여, $M$의 $\mathcal{J}$에 대한 *associated graded module*을 

$$\gr_\mathcal{J}M=M/M_1\oplus M_1/M_2\oplus\cdots$$

으로 정의한다.

</div>

위의 정의에서 $\gr_\mathcal{J}M$은 $\gr_\mathfrak{a}A$-module 구조를 가지며, 이는 임의의 $a\in \mathfrak{a}^k/\mathfrak{a}^{k+1}$과 $x\in M_l/M_{l+1}$에 대하여 이들의 representative $\tilde{a}\in \mathfrak{a}^k$, $\tilde{x}\in M_l$을 택한 후 $\tilde{a}\tilde{x}$를 $M_{k+l}/M_{k+l+1}$로 제한시킨 것이며, [보조정리 2](#lem2)와 유사한 계산을 통해 이것이 잘 정의된다는 것을 확인할 수 있다. 특별히 $M=A$이고 $M_i$들이 $A$의 ideal들인 경우, [정의 1](#def1)과 마찬가지로 $\gr_\mathcal{J}A$ 또한 ring의 구조를 가지며, 이 또한 filtration $\mathcal{J}$에 대한 associated graded ring이라 부른다. 

이제 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Finitely generated module $M$의 $\mathfrak{a}$-stable filtration $\mathcal{J}$가 주어졌다 하고, $\mathcal{J}$의 모든 항 $M_k$가 $M$의 finitely generated submodule이라 하자. 그럼 $\gr_\mathcal{J}A$는 finitely generated $\gr_\mathfrak{a}A$-module이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{J}$가 $\mathfrak{a}$-stable filtration이므로 적당한 $n$이 존재하여 $\mathfrak{a}M_k=M_{k+1}$이 모든 $k>n$에 대하여 성립한다. 따라서, 이러한 $k$에 대하여는 $(\mathfrak{a}/\mathfrak{a}^2)(M_k/M_{k+1})=M_{k+1}/M_{k+2}$이 성립한다. 따라서 $\gr_\mathcal{J}M$의 성분들 중

$$M_0/M_1, M_1/M_2,\ldots, M_{n+1}/M_{n+2}$$

들을 생성하는 것들만 모으면 이들이 $\gr_\mathcal{J}M$을 모두 생성하게 된다. 이제 각각의 $M_i$들이 finitely generated라는 가정으로부터 원하는 주장이 성립한다. 

</details>

## 부풀림 대수

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Ring $A$와 ideal $\mathfrak{a}$에 대하여, $\mathfrak{a}$의 $A$에서의 *blowup algebra<sub>부풀림 대수</sub>*는 다음의 graded $A$-algebra

$$\Bl_\mathfrak{a}A=A\oplus \mathfrak{a}\oplus \mathfrak{a}^2\oplus\cdots\cong A[t \mathfrak{a}]\subseteq A[t]$$

를 의미한다. 

</div>

그럼 $\Bl_\mathfrak{a}A/\mathfrak{a}\Bl_\mathfrak{a}A=\gr_\mathfrak{a}A$임이 자명하다. 한편 더 일반적으로, 임의의 $A$-module $M$, $\mathfrak{a}$-filtration $\mathcal{J}: M_0\supseteq M_1\supseteq\cdots$에 대하여 다음의 식

$$\Bl_\mathcal{J}M =M\oplus M_1\oplus\cdots$$

으로 정의한 $\Bl_\mathcal{J}M$은 graded $\Bl_\mathfrak{a}A$-module이 된다는 것 또한 쉽게 확인할 수 있다. 이제 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $M$의 $\mathfrak{a}$-filtration $\mathcal{J}$가 $\mathfrak{a}$-stable인 것과, $\Bl_\mathcal{J}M$이 $\Bl_\mathfrak{a}A$-module로서 finitely generated인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 만일 $\Bl_\mathcal{J}M$이 finitely generated라면, 적당한 $n$이 존재하여 이들 generator들이 $\Bl_\mathcal{J}M$의 앞의 $n$개의 항에 포함되도록 할 수 있다. 이제 이들을 모두 homogeneous element들의 합으로 바꿔두면 이들 homogeneous element들로 $\Bl_\mathcal{J}M$이 생성된다. 이로부터 $\mathcal{J}$가 $\mathfrak{a}$-stable임을 안다. 이 논증은 반대방향으로도 작동한다.

</details>

## 아틴-리스 보조정리

이제 우리는 다음의 유용한 아틴-리스 보조정리를 증명한다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7 (Artin-Rees)**</ins> Noetherian ring $A$와 ideal $\mathfrak{a}\subseteq A$를 고정하고, finitely generated $A$-module $M$과 그 submodule $M'$을 고정하자. 만일 

$$\mathcal{J}:\quad M=M_0\supseteq M_1\supseteq\cdots$$

이 $\mathcal{a}$-stable filtration이라면 이로부터 유도되는 다음의 filtration

$$\mathcal{J}':\quad M'\supseteq M'\cap M_1\supseteq M'\cap M_2\supseteq\cdots$$

또한 $\mathfrak{a}$-stable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{J}$가 $\mathfrak{a}$-stable이므로 $\Bl_\mathcal{J}M$은 $\Bl_\mathfrak{a}A$-module로서 finitely generated이다. 한편 $\Bl_\mathfrak{a}A$는 finitely generated $A$-algebra이고 $A$가 noetherian이므로 [§기본개념들, §§Finiteness condition](/ko/math/commutative_algebra/basic_notions#finiteness-condition)에 의하여 $\Bl_\mathfrak{a}A$도 noetherian이다. 따라서, $\Bl_\mathcal{J}M$의 submodule $\Bl_{\mathcal{J}'}M'$ 또한 finitely generated이고, 다시 [명제 6](#prop6)을 적용하면 원하는 결과를 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8 (Krull intersection theorem)**</ins> Noetherian ring $A$, 그 ideal $\mathfrak{a}$와 finitely generated $A$-module $M$을 고정하자. 그럼 다음이 성립한다.

1. $(1-a)\left(\bigcap_1^\infty \mathfrak{a}^i M\right)=0$이도록 하는 $a\in \mathfrak{a}$가 존재한다.
2. 만일 $A$가 domain이거나 local ring이고 $\mathfrak{a}$가 proper ideal이라면 $\bigcap \mathfrak{a}^i=0$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$M$의 $\mathfrak{a}$-stable filtration

$$M\supseteq \mathfrak{a}M \supseteq \mathfrak{a}^2 M\supseteq\cdots$$

을 생각하자. 그럼 [보조정리 7](#lem7)에 의하여, 다음의 filtration

$$\left(\bigcap \mathfrak{a}^iM\right) \cap M\supseteq \left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}M \supseteq \left(\bigcap \mathfrak{a}^iM\right) \cap \mathfrak{a}^2 M\supseteq\cdots$$

또한 $\mathfrak{a}$-stable이다. 즉, 적당한 $n$에 대하여

$$\mathfrak{a}\left(\left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}^p M\right)=\left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}^{n+1} M$$

이도록 할 수 있다. 이제 위 식의 좌변과 우변을 각각 정리하면

$$\mathfrak{a}\left(\bigcap \mathfrak{a}^iM\right)=\left(\bigcap \mathfrak{a}^iM\right)$$

을 얻으므로, [§정수적 확장, ⁋보조정리 7](/ko/math/commutative_algebra/integral_extension#lem7)을 적용하면 첫째 결과를 얻는다. 

둘째 결과를 보이기 위해 $M=A$로 두자. 첫째 결과에서 얻어진 $a$에 대하여, $1-a$가 zerodivisor가 아님을 보이면 충분하다. 우선 $\mathfrak{a}$가 $A$의 proper ideal이므로 $1-a\neq 0$이고, 이로부터 $A$가 domain인 경우는 더 이상 증명할 것이 없다. 만일 $A$가 local ring이라면 $\mathfrak{a}$는 $A$의 (유일한) maximal ideal $\mathfrak{m}$에 속할 것이므로 $a\in \mathfrak{m}$이고, 이로부터 $1-a$가 unit이어야 한다. 

</details>

마지막으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $\mathfrak{a}$-filtration

$$\mathcal{J}:\qquad M=M_0\supseteq M_1\supseteq\cdots$$

이 주어진 $A$-module $M$과 associated graded module $\gr_\mathcal{J}M$이 주어졌다 하자. 그럼 임의의 $x\in M$에 대하여, $x$의 *initial form* $\initial(x)$를 다음의 식

$$\initial(x)=x+M_{k+1}\quad\text{in $M_k/M_{k+1}$,}\qquad\text{where $k$ is the greatest integer satisfying $x\in M_k$}$$

으로 정의한다. 

</div>

위와 같은 상황에서, 임의의 $A$-submodule $M'\subseteq M$이 주어졌다 하자. 그럼 $\gr_\mathcal{J}M$를 $\gr_\mathfrak{a}A$-module으로 보고, $\initial(M')$을 $x\in M'$들에 대해 $\initial(x)$으로 생성된 $\gr_\mathcal{J}M$의 $\gr_\mathfrak{a}A$-submodule로 정의할 수 있다. 

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $A=\mathbb{K}[\x,\y]$라 하고, $\mathfrak{a}=(\x,\y)$라 하자. 그럼 $\gr_\mathfrak{a}A$는 다항식의 차수를 통해 grading이 결정된 graded ring이다. 이제 $M=A$로 두고, $M$의 $A$-submodule (즉 $A$의 ideal) $\mathfrak{b}=(\x^2, \y^2)$를 생각하자. 그럼 $\mathfrak{b}$의 임의의 원소는

$$f(\x,\y)\x^2+g(\x,\y)\y^2$$

의 꼴이므로, $\initial(\mathfrak{b})$는 $\x^2, \y^2$으로 생성되는 $\gr_\mathcal{a}A$의 homogeneous ideal이다. 

</div>

그러나 일반적으로 $\initial(M')$은 $M'$의 generator들의 initial form들로 생성되지는 않는다. 

<div class="proposition" markdown="1">

<ins id="cor11">**따름정리 11**</ins> Noetherian local ring $A$와, $A$의 proper ideal $\mathfrak{a}$에 대하여, 만일 $\gr_\mathfrak{a}A$가 domain이라면 $A$ 또한 그러하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$에서 $ab=0$임을 가정하고, $a,b=0$임을 보이면 충분하다. 이제 $\gr_\mathfrak{a}A$에서 $\initial(a)\initial(b)=0$이 성립해야 하고, 따라서 $\initial(x)$ 혹은 $\initial(y)$가 $0$이어야 한다. 이제 위의 따름정리로부터 $\bigcap \mathfrak{a}^n=0$이므로, $a=0$이거나 $b=0$이어야 한다. 

</details>

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---