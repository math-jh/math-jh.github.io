---

title: "Residue theorem"
excerpt: "Residue theorem"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/residue_theorem
header:
    overlay_image: /assets/images/Complex_analysis/Residue_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-10-19
last_modified_at:
weight: 3

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## Singularities of holomorphic functions

우리는 Cauchy's theorem을 일반적인 경우로 확장하려 한다. 우리는 Cauchy's theorem이 성립하지 않는 예시를 알고 있으므로, 이 경우에 우선 관심을 기울일 필요가 있다.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins>

</div>

이 예시에서 $1/z$가 Cauchy's theorem을 만족하지 않는 이유는 이 함수가 $z=0$에서는 정의조차 되지 않기 때문이다. 이렇게 $f$가 $z_0$의 neighborhood에서는 정의되지만 $z_0$에서는 정의되지 않을 때, 우리는 $f$가 $z_0$에서 *isolated singularity*를 갖는다고 말한다. 

우리는 다음과 같이 holomorphic function들의 singularity들을 다음과 같이 분류한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $f$가 isolated singularity $z$를 갖는다고 하자. 

1. 만일 $f(z)$의 값을 적절히 정의하여 $f$가 $z$ 근방에서 holomorphic이도록 할 수 있으면, $z$는 *removable singularity*라 부른다.
2. 함수 $1/f$가 $z$에서 removable singularity를 갖지만 $f$는 removable singularity를 갖지 않는다면, $z$는 $f$의 *pole*이라 부른다.
3. 위의 두 가지 경우에 모두 해당하지 않는 경우를 *essential singularity*라 부른다.

</div>

어렵지 않게, $z$가 $f$의 pole이라면 $1/f$를 holomorphic function으로 만들기 위해서는 반드시 $1/f(z)=0$으로 정의해야 한다는 것을 알 수 있다. Nonzero $a\in \mathbb{C}$에 대하여 $1/f(z)=a$로 정의한 것이 holomorphic이라면, $f(z)=1/a$로 정의하여 $f$를 $z$ 근방에서 holomorphic이도록 만들 수 있으므로 $z$가 removable이기 때문이다. 따라서, 만일 $f$가 $z$에서 pole을 갖는다면, $1/f$의 zero $z$의 order를 생각할 수 있고, 이를 pole의 order로 정의한다.

앞으로 논의의 편의를 위해 *punctured disc*를 

$$D'(z,r)=D(z,r)\setminus\{z\}$$

으로 정의하자. 그럼 $f$가 $z$에서 isolated singularity를 갖는다는 것은 충분히 작은 $r$이 존재하여 $f$가 $D'(z,r)$에서는 holomorphic이지만 $z$에서는 $f$가 정의되지 않는 것이다.

우리는 이제 세 singularity의 특징을 보여주는 명제를 각각 살펴볼 것이다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3 (Riemann)**</ins> Holomorphic function $f$가 isolated singularity $z$ 근방에서 bounded라면 $z$는 removable singularity이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $g:D(z,r)\rightarrow\mathbb{C}$를 다음의 식

$$g(w)=\begin{cases}(w-z)^2f(w)&w\neq z,\\ 0&w=z.\end{cases}$$

으로 정의하자. 그럼 $g$는 $z$에서 연속이고, 뿐만 아니라 $z$에서 differentiable하며 $g'(z)=0$이라는 것도 알 수 있다. 따라서 $g$는 order $\geq 2$의 근 $z$을 갖는 holomorphic function이므로, 적당한 holomorphic function $h$가 존재하여

$$g(w)=(w-z)^2h(w)$$

라 할 수 있다. 이제 $h$는 $w\neq z$에서는 $f$와 같은 함수이므로, 정의에 의해 $f$는 $z$에서 removable singularity를 갖는다.

</details>

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Holomorphic function $f$가 $z$에서 pole을 갖는 것은 적당한 positive integer $N$과, complex number들의 sequence $(a\_n)\_{n\geq -N}$가 존재하여 $a_{-N}\neq 0$이고

$$f(w)=\sum_{n=-N}^\infty a_n(w-z)^n$$

인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞서 말한 것에 의해 $f$가 order $N$의 pole을 갖는다면

$$\frac{1}{f(w)}=(w-z)^N h(w)$$

이다. 이제 holomorphic function $h$는 $z$ 근방에서 non-vanishing이므로 $1/h$도 $z$ 근방에서 holomorphic이고, 따라서 $f(w)$를

$$f(w)=(w-z)^{-N} \tilde{h}(w)$$

로 적을 수 있다. 이제 $\tilde{h}$의 power series expansion을 생각하면 원하는 결과를 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5 (Casorati-Weierstrass)**</ins> $f$가 $z$에서 essential singularity를 갖는다면, punctured disc $D'(z,r)$의 $f$에 의한 image는 $\mathbb{C}$에서 dense하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여, 어떤 $\delta>0$이 존재하여 어떤 $a\in\mathbb{C}$에 대해

$$\lvert f(w)-a\rvert>\delta$$

가 임의의 $w\in D'(z,r)$에 대해 성립하도록 할 수 있다고 하자. 그럼 $D'(r,z)$에 새로운 함수

$$g(w)=\frac{1}{f(w)-a}$$

를 정의할 수 있으며, $g$는 $1/\delta$에 의해 bounded되어있으므로 $g$는 $z$에서 removable singularity를 갖는다. 그럼 $g(z)$는 0이거나 0이 아닌데, 0이라면 $f(w)-a$가 $w=z$에서 pole을 가지므로 모순이고, 0이 아니라면 $f(w)-a$가 $w=z$에서 removable singularity를 가지므로 모순이다.

</details>

일반적으로 removable singularity를 갖는 함수는 holomorphic function과 다르게 취급할 이유가 전혀 없다. 그리고, essential singularity는 앞선 명제에서 보듯이 singularity 근방에서 굉장히 나쁘게 행동하므로 removable singularity와는 정반대 이유에서 우리의 관심사가 아니다. 때문에 우리는 pole에 많은 관심을 가질 것이다. 우선, [명제 4](#pp4)로부터 우리는 $f$가 $z$에서 order $N$의 pole을 갖는다면, 다음의 식

$$f(w)=\frac{a_{-N}}{(w-z)^n}+\cdots+\frac{a_{-1}}{w-z}+G(z)\tag{1}$$

을 얻는다. 여기서 $G(z)$는 holomorphic function이다. 그럼 계수 $a_{-1}$을 $f$의 *residue*라 부르며, 이를 $\operatorname{res}_{z} f$로 적는다. 

곧 살펴보겠지만, residue는 많은 적분을 간편하게 계산하게 해 준다. 따라서 이 residue의 값을 계산하는 방법이 궁금하다. $f$가 simple root를 가질 때는 $N=1$이므로, 그냥 간단히 $(w-z)f(w)$의 상수항을 찾으면 된다. 즉, 이 때 $\operatorname{res}\_zf=\lim\_{w\rightarrow z}(w-z)f(w)$가 성립한다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $f$가 $z$에서 order $N$의 pole을 갖는다면, 다음의 식

$$\operatorname{res}_zf=\lim_{w\rightarrow z}\frac{1}{(n-1)!}\left(\frac{d}{dw}\right)^{n-1}(w-z)^nf(w)$$

이 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

단순 계산.

</details>

## Residue theorem

우리는 앞서 residue가 여러 적분을 계산하는 데에 큰 도움을 준다고 했는데, 이는 다음 정리에 따른 것이다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (The residue theorem)**</ins> Open disc $D$와 $D$의 어떤 점 $z$에 대하여, $f$가 $D\setminus z$에서 holomorphic하고 $z$에서 pole을 갖는다 하자. 그럼 다음의 식

$$\int_{\partial D} f(z)\mathop{dz}=2\pi i\operatorname{res}_zf$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

식 (1)에서, 항 $a_{-1}/(w-z)$를 제외한 모든 항들은 primitive를 갖는다. 따라서 Cauchy's integral formula에 의해 나머지는 자명하다. 

</details>

더 일반적으로, $n$개의 pole을 갖는다면 여러 개의 keyhole을 만들면 되므로 적분은 *적분 경로 안에 있는 pole들의 residue의 합*으로 나타나게 된다.

우리가 지금까지는 최대한 계산을 피해 왔지만, residue theorem을 사용하는 것은 중요하므로 몇 가지의 예시를 살펴보지 않을 수 없다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> <#content#>

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> <#content#>

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> <#content#>

</div>

이렇게 residue theorem은 적분을 계산하는 데에 아주 큰 도움이 된다. 그런데 residue theorem의 증명을 찬찬히 뜯어보면 어딘가 기이한 부분이 있다. 식 (1)의 $G(z)$는 holomorphic이고, 우리는 holomorphic function들이 primitive를 갖는다는 것을 보였으므로 이건 괜찮은데, 음수 차수의 항들이 조금 걸린다. 예를 들어, $a_{-N}/(w-z)^n$은 왜 primitive를 갖는데, $a_{-1}/(w-z)$는 primitive를 갖지 않는가? 우리는 지금까지 함수 $f(z)=1/z$가 primitive를 갖지 않는다고 주장해왔는데[^1], 과연 이게 사실이긴 한가? $f(z)$도 primitive $\log z$를 갖지 않는가?

결과적으로 이야기하면 $f(z)$는 primitive를 갖지 않으며, 이는 $\log z$가 잘 정의되지 않기 때문이다. 더 정확히 이야기해서, $e^z$는 실함수에서는 일대일 함수이고, 따라서 역함수를 갖지만, 복소수에서는 일대일이 아니기 때문에 역함수를 갖지 않게 된다. 물론 이 이야기를 계속 해 나갈 수 있지만, 잠시 멈춰서 우리가 미뤄뒀던 이야기를 해 보자.

## Cauchy's theorem on simply connected domains 

우리는 대수위상에서 homotopy의 개념을 정의했었는데, 잠깐 remind를 해 보면

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> 같은 끝점을 갖는 두 curve $\gamma\_0, $\gamma\_1:[a,b]\rightarrow\Omega$이 *homotopic*하다는 것은 적당한 curve들의 family $(\gamma\_s)\_{0\leq s\leq 1}$이 존재하여, 모든 $s$에 대해

$$\gamma_s(a)=\gamma_0(a)=\gamma_1(a),\qquad \gamma_s(b)=\gamma_0(b)=\gamma_1(b)$$ 

가 성립하고, $(s,t)\mapsto \gamma\_s(t)$가 continuous한 것이다. 
</div>

직관적으로 두 curve가 homotopic하다는 것은 하나의 curve를 연속적으로 잘 변형하여 다른 하나의 curve로 변형할 수 있다는 것이다. 일단 우리는 대수위상에서 배우는 자세한 내용에는 관심이 없고, 이 정도 정의만 알면 충분하다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> 만일 $f$가 $\Omega$에서 holomorphic하고, 두 curve $\gamma_0$, $\gamma_1$이 $\Omega$에서 homotopic하다면 

$$\int_{\gamma_0}f(z)\mathop{dz}=\int_{\gamma_1}f(z)\mathop{dz}$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

<#content#>

</details>

어떤 집합 $\Omega$가 *simply connected*라는 것은, 같은 끝점을 공유하는 임의의 두 curve가 homotopic한 것이다. 혹은, 이와 동등하게, 임의의 closed curve가 점과 homotopic한 것이다. 

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13**</ins> Simply connected domain 위에서 정의된 임의의 holomorphic function은 primitive를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

<#content#>

</details>

## Complex logarithm

이제 우리의 숙원사업(?)이던 Cauchy's theorem의 가장 일반화된 버전을 증명했으니, 안심하고 원래의 궤도로 돌아오자. 우리는 우선 $\log z$를 정의하는 것이 만만치 않은 이유를 살펴봤는데, 이건 근본적으로 $e^2\pi i=1$이고, 따라서 임의의 $x$에 대해 $e^{x+2\pi i k}=e^x$가 성립하기 때문에 발생하는 일이다. 하지만 우리는 이런 상황을 처음 보는 게 아니다. 예를 들어, 우리는 $\sin$이나 $\cos$ 등을 다루면서도 이런 문제에 부딪혔지만, 어쨌든 $\arcsin$이나 $\arccos$ 등을 정의하는 데 성공했다. 그리고 그 방법은 여러번 겹치는 함숫값들을 모두 고려하는 대신 $\sin$ 혹은 $\cos$의 일부분만 잘라서 살펴보는 것이었다. 따라서 complex logarithm 또한 $0<\theta<2\pi$인 경우로 한정하여 생각하는 것이 자연스러울 것이다. 이렇게 정의역을 가지치기해서 줄여주면 complex logarithm은 holomorphic function이 될 것이다.

<div class="definition" markdown="1">

<ins id="df14">**정의 14**</ins> Open set $\Omega$에 대하여, $\Omega$ 위에 정의된 *branch of logarithm*은 다음의 식

$$e^{L(z)}=z$$

를 모든 $z\in \Omega$에 대해 만족하는 holomorphic function $L$이다.

</div>

물론 임의의 $\Omega$에 대해 branch of logarithm이 정의될 필요는 없다. 그렇다면 언제 $\Omega$ 위에서 잘 정의된 branch of logarithm이 존재할까?

<div class="proposition" markdown="1">

<ins id="pp15">**명제 15**</ins> Connected open set $\Omega$와, $z_0\in \Omega$를 고정하자. 그럼 다음이 동치이다.

1. $L$이 $V$에서의 branch of logarithm이다.
2. $e^{L(z_0)}=z_0$이고, $L'(z)=1/z$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

*증명.* <#content#>

</details>

그럼, 사실 우리는 $\Omega$ 위에 정의된 branch of logarithm이 언제 존재하는지를 알고 있던 것이다. 즉, $0\not\in\Omega$이고 ($L'(z)=1/z$이므로), 또 $L$이 $L'(z)=1/z$의 primitive로서 정의되기 위해서는 $\Omega$가 simply connected여야 한다. 이 때 $\Omega$의 모양을 머리속으로 그려보면, $\Omega$는 0을 포함하지 않으므로 punctured disc처럼 생겼는데, 이것이 simply connected이기도 하려면 원점에서부터 $\Omega$를 바깥쪽으로 찢어야 한다. 따라서 우리가 앞서 말한 complex logarithm의 "가지"는, 굳이 $\theta=0$이나 $\theta=\pi$ 등일 필요가 없어진다. 

더 constructive하게, $L$은 다음과 같이 정의된다. 1~z, well defined by simply connectedness



[^1]: 사실, 증명도 하긴 했었다.
