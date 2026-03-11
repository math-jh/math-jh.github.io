---

title: "Inverse of holomorphic functions"
excerpt: "Holomorphic functions and its inverse"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/inverse_functions
header:
    overlay_image: /assets/images/Complex_analysis/Inverses_of_holomorphic_functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-10-20
last_modified_at: 
weight: 6

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


우리는 Cauchy-Riemann equation으로부터 시작해서 residue theorem을 소개하고, 이를 winding number를 도입하여 조금 더 일반화했다. 그리고 나서 complex logarithm을 정의하고, argument principle이나 Rouché's theorem같은 정리들을 유도했다. 보편적으로 학부 때 중간고사 즈음까지 배우는 범위가 여기까지고, 우리는 이제 두 번째 파트로 넘어가려 한다. Stein과 Ullrich 모두 공통적으로 이쯤에서 Hadamard factorization을 소개하는데, 우리는 그 대신 holomorphic function들의 inverse를 먼저 살펴본다. Conformal mapping은 Riemann mapping theorem이랑 묶어야 하니 여기에 넣기는 한 챕터가 너무 길어지고, 그렇다고 앞의 내용들과 어울리는 내용은 아니라서 아무래도 좀 애매한 파트. 

아무튼 시작하자.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> $f$가 open set $V$에서 holomorphic하고, one-to-one이라 하자. 그럼 $f'$는 non-vanishing function이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여, 어떤 $z_0\in V$에 대해 $f'(z_0)=0$이라 하자. 만일 $z_0$ 근방에서 $f'$가 0이라면, $z_0$ 근방의 점 $w$에 대하여 $f(w)-f(z_0)=0$이 되므로 이는 $f$가 one-to-one이라는 가정에 모순이 될 것이다. 이제 우리는 $f'$가 $z_0$ 근처에서 identically vanish하지는 않아야 한다는 걸 안다. 더 일반적으로, $z_0$은 identity theorem에 의하여 isolated여야 한다. 따라서 $r>0$을 잡아 $D(z_0,r)\subset V$이고, $f'(z)$가 임의의 $z\in D(z_0,r)$에 대하여 non-vanish라 하자.

함수 $f-f(z_0)$을 생각하자. 이 함수는 $z_0$에서 root를 갖고, 또 $f'(z_0)=0$이므로 사실 $z_0$에서 최소 double root (즉 root of multiplicity 2)를 갖는다. 그럼 Rouché's theorem에 의하여, $f-w$는 $\lvert w-f(z_0)\rvert>0$을 충분히 작게 하는 $w$에 대해 적어도 두 개의 root를 가진다. 그런데 $f'$는 non-vanish이므로 이 함수 $f-w$는 모두 simple root여야 하고, 따라서 $f-w$는 두 개의 서로 다른 zero를 가져야 한다. 이는 $f$가 one-to-one이라는 가정에 모순이다.  

</details>

몇 가지를 짚고 넘어가자. 우선, 이건 holomorphic function이라 성립하는 명제다. 예를 들어 실함수 $f(x)=x^3$은 one-to-one이지만 $x=0$에서 vanishing derivative를 갖는다. 이 반례로부터, $f$가 one-to-one임을 보이는 과정 또한 생각보다 어렵다는 것도 어렴풋이 눈치챌 수 있다. 또 주의할 것은 이 명제의 역은 성립하지 않는다는 것이다. 예컨대 $f(z)=e^z$를 생각하자. $f'(z)=e^z$이고, 또 $f'(z)$의 modulus는 $e^{\Re z}$로 주어지므로 항상 1보다 크거나 같다. 하지만 $e^{2\pi}=e^{4\pi}$ 등등, 이 함수는 one-to-one은 아니다.

그렇기 때문에 우리는 우선 위 명제의 전제조건인 one-to-one 조건이 언제 만족하는지에 관심을 갖는다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Convex open set $V$에 대하여, $f$가 $V$에서 정의된 holomorphic function이라 하자. 만일 $K$가 closed convex subset이고, $f'(z)\in K$가 임의의 $z\in V$에 대해 성립한다면, $z\neq w$에 대해 항상

$$\frac{f(z)-f(w)}{z-w}\in K$$

가 성립한다.
</div>
