---

title: "Class group"
excerpt: "Fractional ideals and the Class group"

categories: [Math / Algebraic Number Theory]
permalink: /ko/math/algebraic_number_theory/class_group
header:
    overlay_image: /assets/images/Algebraic_number_theory/class_group.png
    overlay_filter: 0.5
sidebar: 
    nav: "further_topics"

date: 2021-10-03
last_modified_at: 
weight: 3

published: false

---

<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


이 글에서, $R$은 항상 Dedekind domain을, $K$는 $R$의 quotient field를 나타낸다.

## Fractional ideals

사실, 우리가 앞서 Dedekind domain의 unique factorization property를 보인 방법은 약간 복잡한 감도 없잖아 있다. 다른 방법은 *fractional ideal*의 개념을 도입하는 것이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $R$의 *fractional ideal*은 $R$-module $K$의 finitely generated $R$-submodule을 뜻한다. 만일 $\mathfrak{M}$이 $R$의 fractional ideal이라면, $\mathfrak{M}^{-1}$을 다음의 집합

$$\mathfrak{M}^{-1}=\{x\in K:x\mathfrak{M}\subset R\}$$

으로 정의한다.

</div>

우선 fractional ideal에 대한 간단한 다음의 명제부터 보이자. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 다음이 모두 동치이다.

1. $\mathfrak{M}$은 fractional ideal이다.
2. 적당한 nonzero $d\in R$이 존재하여 $d\mathfrak{M}\subset R$이다.
3. 어떤 nonzero $x\in K$와 nonzero ideal $\mathfrak{a}\subset R$에 대하여 $\mathfrak{M}=x\mathfrak{a}$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 적당한 $x_i\in K$들에 대해 $\mathfrak{M}=\sum x_iR$이라 하자. 그럼 $x_i$들은 어차피 유한히 많으므로, 적당한 $d$를 곱해 이들을 모두 $R$의 원소들로 만들어 줄 수 있다. 그리고 이러한 $d$가 2번 조건을 만족한다. 이제 2번 조건이 성립한다 가정하자. 그럼 $d\mathfrak{M}$는 $R$-module이고 $R$에 속하므로 $R$의 ideal이 된다. 따라서 $x=1/d$로 잡고, $\mathfrak{a}=d\mathfrak{M}$로 잡으면 3번이 성립한다. 마지막으로 3번을 가정하고 1번을 보여야 한다. $R$은 Dedekind domain이고 따라서 Noetherian이므로, $R$의 임의의 ideal은 finitely generated이다. 이제 $\mathfrak{M}=x\mathfrak{a}$ 또한 finitely generated여야 한다. 

</details>

그럼 임의의 fractional ideal $\mathfrak{M}$에 대하여 $\mathfrak{M}$의 inverse $\mathfrak{M}^{-1}$ 또한 fractional ideal임을 보일 수 있다. 임의의 $y\in \mathfrak{M}$을 택하자. 그럼 $\mathfrak{M}^{-1}$의 정의에 의해 $y\mathfrak{M}^{-1}\subset R$이 성립한다. 

하지만 왜 $\mathfrak{M}^{-1}$을 $\mathfrak{M}$을 inverse라 부르는지는 아직 설명되지 않았다. 우선 fractional ideal들의 곱을 우리가 늘상 하던 것과 같이 정의하자. 즉, $\mathfrak{M},\mathfrak{N}$이 각각 fractional ideal들이라면, $\mathfrak{MN}$은 임의의 $m_i\in \mathfrak{M}$, $n_j\in\mathfrak{N}$에 대해 $\sum m_in_j$들을 모아둔 집합이다. 어렵지 않게 $\mathfrak{MN}$도 마찬가지로 fractional ideal임을 보일 수 있다. 

이 상황에서 $R$은[^1] 임의의 fractional ideal $\mathfrak{M}$에 대해 $R\mathfrak{M}=\mathfrak{M}$을 만족한다. 즉, $R$이 일종의 항등원의 역할을 한다. 그렇다면 $\mathfrak{M}^{-1}$을 $\mathfrak{M}$의 inverse라 부르는 이유는 다음의 정의로 설명될 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Fractional ideal $\mathfrak{M}$이 *invertible*하다는 것은 $\mathfrak{M}\mathfrak{M}^{-1}=R$이 성립하는 것이다. 

</div>

그런데, Dedekind ring에 대해서는 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 임의의 ideal은 invertible하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$R$의 임의의 ideal $\mathfrak{A}$를 생각하자. 그럼 $\mathfrak{A}\mathfrak{A}^{-1}=\mathfrak{B}$는 fractional ideal이다. 뿐만 아니라, $\mathfrak{A}\mathfrak{A}^{-1}$의 임의의 원소는 항상 $R$의 원소이므로, $\mathfrak{B}$는 사실 $R$의 ideal이 된다. 이제 $R$의 각각의 maximal ideal $\mathfrak{p}$에 대하여, localization에서 다음의 식

$$\mathfrak{B}_\mathfrak{p}=(\mathfrak{A}\mathfrak{A}^{-1})_\mathfrak{p}=\mathfrak{A}_\mathfrak{p}\mathfrak{A}_\mathfrak{p}^{-1}=R_\mathfrak{p}$$

을 관찰하면, lying-over theorem에 의해 $\mathfrak{B}=R$이 성립한다.

</details>

따라서, Dedekind domain $R$의 임의의 fractional ideal들을 모아둔 집합은 사실 group structure를 이룬다. 

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $R$의 fractional ideal들을 모두 모아둔 집합 $\mathbf{I}(R)$을 $R$의 *ideal group*이라 부른다. 또, principal fractional ideal들을 모아둔 집합 $\mathbf{P}(R)$을 정의하자. $\mathbf{P}(R)$도 마찬가지로 group structure를 이룬다는 것을 확인할 수 있고, $\mathbf{I}(R)$는 abelian group이므로 quotient $\mathbf{C}(R)=\mathbf{I}(R)/\mathbf{P}(R)$이 잘 정의된다. 이를 $R$의 *class group*이라 부른다.

</div>

만일 $R$이 PID였다면, $\mathbf{I}(R)=\mathbf{P}(R)$은 trivial group이 됐을 것이다. 이런 측면에서, $\mathbf{C}(R)$은 <span style="border-highlight">$R$이 얼마나 PID로부터 멀리 떨어져있는지</span>를 측정하는 도구라 생각할 수 있다. 


---

**References**

[Jan] Gerald J. Janusz. *Algebraic Number Fields*, American  Mathematical Soc., 1995 

---

[^1]: $R$은 fractional ideal이 됨은 말할 것도 없이 분명하다.
