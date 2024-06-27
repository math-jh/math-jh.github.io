---

title: "긴 완전열 (작성중)"
excerpt: "긴 완전열"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/long_exact_sequence
header:
    overlay_image: /assets/images/Math/Homological_Algebra/Long_exact_sequence.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2023-01-02
last_modified_at: 2023-01-02
weight: 4

---

이제 우리는 $\Ch(\mathcal{A})$에서의 short exact sequence가 *long exact sequence*를 유도한다는 것을 보인다. 그 전에, 이전 글에서 분량문제로 다루지 못한 truncation을 먼저 소개한다.

## Truncation

임의의 chain complex $C_\bullet$가 주어졌다 하자. 임의의 정수 $n$에 대하여, 다음의 식

$$(\tau_{\geq n}C)_i=\begin{cases}0&\text{if $i < n$}\\ Z_n&\text{if $i=n$}\\ C_i&\text{if $i >  n$}\end{cases}$$

그리고 $C_\bullet$와 동일한 differential로 정의된 chain complex $(\tau_{\geq n}C)_\bullet$를 *intelligent truncation*이라 부른다. 그럼 

$$H_i(\tau_{\geq n}C)=\begin{cases}0&\text{if $i < n$}\\ H_i(C)&\text{if $i\geq n$}\end{cases}$$

이 된다. 비슷하게 $(\tau_{< n}C)_\bullet$ 또한 정의할 수 있다. 한편 *Brutal truncation*은 다음의 식

$$(\sigma_{\geq n}C)_i=\begin{cases}0&\text{if $i \leq n$}\\ C_i&\text{otherwise}\end{cases}$$

으로 정의된다. 정의 자체는 $(\sigma_{\geq n}C)_\bullet$가 더 자연스러워보일 수 있지만, $n$번째 호몰로지를 살펴보면 intelligent truncation이 더 좋은 연산을 준다는 것을 확인할 수 있다.

## 긴 완전열

우리는 앞서 chain map $f_\bullet$의 image와 kernel이 각각의 $f_n$의 image와 kernel로 이루어진 chain complex가 된다는 것을 보았다. 따라서 

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

이 *short exact sequence*라는 것은 모든 $n$에 대하여

$$0\rightarrow A_n\rightarrow B_n\rightarrow C_n\rightarrow 0$$

이 short exact sequence라는 것과 동치라는 것을 확인할 수 있다. 이러한 가정 하에서 우리는 homology들의 long exact sequence를 만들 수 있다. 

다음 정리의 증명에서 snake lemma가 중요한 역할을 하며, 또 카테고리가 $\lMod{R}$인 경우에 명시적으로 얻어지는 connecting map을 이용하면 증명을 쉽게 마칠 수 있으므로 [\[범주론\] §아벨 카테고리, ⁋정리 9](/ko/math/category_theory/abelian_categories#thm9)을 적극적으로 이용하여 $\lMod{R}$ 카테고리에서 다음 정리에 대한 증명을 진행한다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (The long exact sequence)**</ins> 다음의 short exact sequence

$$0\rightarrow A_\bullet\rightarrow B_\bullet\rightarrow C_\bullet\rightarrow 0$$

가 주어졌다 하자. 그럼 호몰로지들 사이의 *long exact sequence*

$$\cdots\rightarrow H_n(A)\rightarrow H_n(B)\rightarrow H_n(C)\rightarrow H_{n-1}(A)\rightarrow \cdots$$

가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이는 다음의 diagram 

![long_exact_sequence](/assets/images/Math/Homological_Algebra/Long_exact_sequence-1.png){:width="655.2px" class="invert" .align-center}

을 생각하면 된다. 여기에서 $\partial$들은 모두 $\partial^A(a+\im d^A_{n+1})=d_n^Aa\in\ker d^A_{n-1}$과 같이 정의된 함수들이다. 그럼 위의 diagram에서 $\ker\partial^A$는 $H_{n+1}(A)=\ker d_n^A/\im(d^A_{n+1})$와 같고, $\coker\partial^A$는 $H_{n-1}(A)=\ker d^A_{n-1}/\im d^A_n$과 같다는 것을 쉽게 확인할 수 있다. 

따라서, 위와 아래의 행이 모두 exact라는 것만 보인다면, snake lemma에 의해 주어진 long exact sequence가 잘 유도된다. 이를 보이기 위해 다시 다음의 diagram

![long_exact_sequence_exactness](/assets/images/Math/Homological_Algebra/Long_exact_sequence-2.png){:width="463.95px" class="invert" .align-center}

을 생각하자. 이 diagram에 snake lemma (더 정확하게는 [§Diagram chasing, ⁋보조정리 5](/ko/math/homological_algebra/diagram_chasing#lem5)) 를 다시 한 번 적용하면, 두 exact sequence

$$0\rightarrow \ker(d_n^A)\rightarrow \ker(d_n^B)\rightarrow \ker(d_n^C)$$

그리고

$$\coker(d_n^A)\rightarrow\coker(d_n^B)\rightarrow\coker(d_n^C)\rightarrow 0$$

이 얻어진다.

</details>

## Naturality

위에서 만든 long exact sequence는 다음과 같은 센스에서 자연스럽다. 

