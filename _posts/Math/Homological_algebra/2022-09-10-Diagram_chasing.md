---

title: "Diagram chasing"
excerpt: "기본정의"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/diagram_chasing
header:
    overlay_image: /assets/images/Homological_algebra/a.png
    overlay_filter: 0.5
sidebar: 
    nav: "homological_algebra-ko"

date: 2022-09-10
last_modified_at: 2022-09-10
weight: 2

---

호몰로지 대수학에서는 diagram chasing이라 부르는 증명방법이 많이 사용된다. 이번 글에서는 이를 사용한 몇 가지 결과를 정리한다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1 (The four lemma)**</ins> $R$-module들의 commutative diagram

![Four_lemma](/assets/images/Homological_algebra/Diagram_chasing-1.png){:width="300.15px" class="invert" .align-center}

이 주어졌다 하자. 이 때 위와 아래의 행은 모두 exact이다. $\alpha$가 전사이고, $\delta$가 단사라 가정하자. 그럼

1. 만일 $\gamma$가 전사라면 $\beta$ 또한 전사이다.
2. 만일 $\beta$가 단사라면 $\gamma$ 또한 단사이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 임의의 $b'\in B'$를 택하자. 우리는 적당한 $b\in B$가 존재하여 $\beta(b)=b'$임을 보여야 한다. 가정에 의해 $\gamma$는 전사이므로, 적당한 $c\in C$가 존재하여 $\gamma(c)=g'(b')\in C'$가 성립한다. 이제
  
    $$\delta(h(c))=h'(\gamma(c))=h'(g'(b'))=0$$

    이므로 $h(c)\in\ker\delta$이고, $\delta$는 단사이므로 $h(c)=0$이다. 즉, $c\in\ker(h)=\operatorname{im}(g)$이므로 적당한 $b_0\in B$가 존재하여 $g(b_0)=c$이다. 이제 이러한 $b_0$에 대하여, $b'-\beta(b_0)\in B'$를 생각하자. 그럼

    $$g'(b'-\beta(b_0))=g'(b')-g'(\beta(b_0))=\gamma(c)-\gamma(g(b_0))=\gamma(c)-\gamma(c)=0$$

    이므로, $b'-\beta(b_0)\in\ker(g')=\operatorname{im}(f')$가 성립한다. 따라서 적당한 $a'\in A'$가 존재하여 $f'(a')=b'-\beta(b_0)$이다. $\alpha$는 전사이므로, $\alpha(a)=a'$를 만족하는 $a\in A$가 존재한다. 그럼

    $$\beta(f(a))=f'(\alpha(a))=f'(a')=b'-\beta(b_0)$$

    이고, 따라서 $b=b_0+f(a)$라 하면 $\beta(b)=b'$임을 확인할 수 있다.
2. 어떤 $c\in C$가 $\gamma(c)=0$을 만족한다 하자. 우리는 $c=0$임을 보여야 한다. 우선

    $$0=h'(0)=h'(\gamma(c))=\delta(h(c))$$

    이고, $\delta$는 단사이므로 $h(c)=0$임을 안다. 즉 $c\in\ker(h)=\operatorname{im}(g)$이므로, 적당한 $b_0\in B$가 존재하여 $g(b_0)=c$이다. 이제 $B'$의 원소 $\beta(b_0)$를 생각하면,

    $$g'(\beta(b_0))=\gamma(g(b_0))=\gamma(c)=0$$

    이므로, $\beta(b_0)\in\ker(g')=\operatorname{im}(f')$이 성립한다. 따라서 적당한 $a'\in A'$가 존재하여 $f'(a')=\beta(b_0)$이고, $\alpha$는 전사이므로 $\alpha(a)=a'$를 만족하는 $a\in A$도 존재한다. 이제 $b=b_0-f(a)$라 하자. 그럼

    $$g(b)=g(b_0-f(a))=g(b_0)-g(f(a))=g(b_0)=c$$

    이다. 한편, 

    $$\beta(b)=\beta(b_0-f(a))=\beta(b_0)-\beta(f(a))=\beta(b_0)-f'(\alpha(a))=\beta(b_0)-f'(a')=\beta(b_0)-\beta(b_0)=0$$

    이므로 $b\in\ker(\beta)$이고, $\beta$는 단사이므로 $b=0$가 된다. 따라서 $c=g(b)=0$이고, $\gamma$는 단사이다.

</details>

위의 명제는 다음의 자명한 두 따름정리를 갖는다.

<div class="proposition" markdown="1">

<ins id="crl2">**따름정리 2 (The five lemma)**</ins> $R$-module들의 commutative diagram

![five_lemma](/assets/images/Homological_algebra/Diagram_chasing-2.png){:width="410.25px" class="invert" .align-center}

이 주어졌다 하자. 이 때 위와 아래의 행은 모두 exact이다. 만일 $\alpha,\beta,\delta,\epsilon$이 모두 전단사라면, $\gamma$ 또한 전단사이다.

</div>

<div class="proposition" markdown="1">

<ins id="crl3">**따름정리 3 (The short five lemma)**</ins> $R$-module들의 commutative diagram

![short_five_lemma](/assets/images/Homological_algebra/Diagram_chasing-3.png){:width="384.45px" class="invert" .align-center}

이 주어졌다 하자. 이 때 위와 아래의 행은 모두 exact이다. 이제 $\alpha,\gamma$가 모두 단사라면 $\beta$도 단사이고, $\alpha,\gamma$가 모두 전사라면 $\beta$도 전사이다.

</div>

우리의 주된 목표는 snake lemma를 증명하는 것인데, 이 보조정리는 보여야 할 것이 많아서 **[Hu]**의 연습문제를 순서대로 따라가는 것이 더 좋아보인다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $R$-module들의 commutative square

![induced_morphism](/assets/images/Homological_algebra/Diagram_chasing-4.png){:width="135.9px" class="invert" .align-center}

가 주어졌다 하자. 그럼 $\xi$는 $\ker(h)$를 $\ker(h')$로, $\eta$는 $\operatorname{im}(h)$를 $\operatorname{im}(h')$로 보내며, 특히 다음의 함수들

$$\xi^\sharp:\ker(h)\rightarrow\ker(h'),\quad \eta^\sharp:\operatorname{im}(h)\rightarrow\operatorname{im}(h'),\quad\xi^\ast:X/\ker(h)\rightarrow X'/\ker(h'),\quad \eta^\ast:\operatorname{coker}(h)\rightarrow\operatorname{coker}(h')$$

이 잘 정의된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$i:\ker(h)\rightarrow X$와 $\xi$의 합성 $\xi\circ i:\ker h\rightarrow X'$를 생각하자. 그럼 

$$h'\circ(\xi\circ i)=(\eta\circ h)\circ i=\eta\circ 0=0$$

이므로, [§완전열, 명제 4](/ko/math/homological_algebra/exact_sequences#pp4)로부터 유일한 $\xi^\sharp:\ker(h)\rightarrow\ker(h')$가 존재한다는 것을 안다. 

![induced_morphism_kernel](/assets/images/Homological_algebra/Diagram_chasing-5.png){:width="274.2px" class="invert" .align-center}

비슷하게 $p'\circ\eta:Y\rightarrow \operatorname{coker} (h')$로부터,

$$(p'\circ\eta)\circ h=p'\circ(h'\circ\xi)=(p'\circ h')\circ\xi=0\circ\xi=0$$

이고, $\operatorname{coker}(h)$의 universal property로부터 $\eta^\ast$를 정의할 수 있다.

![induced_morphism_cokernel](/assets/images/Homological_algebra/Diagram_chasing-6.png){:width="294.3px" class="invert" .align-center}

정의에 의해 $\operatorname{coker}(h)=Y/\operatorname{im}(h), \operatorname{coker}(h')=Y'/\operatorname{im}(h')$이므로, $\eta^\ast$가 $0$을 $0$으로 보내는 것으로부터 $\eta^\sharp$ 또한 잘 정의된다. 마지막으로 $\xi^\ast$의 경우, $p:X'\rightarrow X'/\ker(h')$를 생각하면 

$$\ker(h)\subseteq\ker(p\circ\xi)$$

이고, 따라서 $p\circ\xi$가 $\xi^\ast:X/\ker(h)\rightarrow X'/\ker(h')$를 유도한다. (<#ref#>)

</details>

이를 이용하면 다음 보조정리를 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $R$-module들의 commutative diagram

img

이 주어졌다 하자. 그럼 $f,g$와 $f',g'$는 각각 다음의 두 열

$$\ker(\alpha)\rightarrow\ker(\beta)\rightarrow\ker(\gamma),\qquad \operatorname{coker}(\alpha)\rightarrow\operatorname{coker}(\beta)\rightarrow\operatorname{coker}(\gamma)$$

를 유도한다. 뿐만 아니라, $f':A'\rightarrow B'$가 단사라면 첫째 열이 exact가 되고, $g:B\rightarrow C$가 전사라면 둘째 열이 exact가 된다.

</div>

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (The snake lemma)**</ins> 

</div>
