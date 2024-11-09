---

title: "동반소아이디얼"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/associated_primes
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Associated_primes.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-16
last_modified_at: 2024-10-16
weight: 6

---

## Prime avoidance lemma

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$와 $A$-module $M$에 대하여, $A$의 prime ideal $\mathfrak{p}$가 $M$의 *associated prime ideal<sub>동반소아이디얼</sub>*이라는 것은 어떠한 $x\in M$에 대해 $\mathfrak{p}=\ann(x)$인 것이다. Associated prime들의 모임을 $\Ass M$으로 적는다. 

</div>

정의에 의하여 $\mathfrak{p}$가 $M$의 associated prime인 것과, $A/\mathfrak{p}$가 $M$의 적당한 submodule인 것이 동치이다. 이는 $A \rightarrow M$을 $1\mapsto x$로 잡고 first isomorphism theorem을 적용하면 바로 알 수 있다. 

이번 글에서 우리는 associated prime ideal에 대한 다양한 성질들을 살펴본다. 그 과정에서 중요한 역할을 하는 것은 다음의 보조정리이다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2 (Prime avoidance lemma)**</ins> $A$의 ideal들 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n, \mathfrak{b}$가 주어졌다 하고, $\mathfrak{b}\subseteq \mathfrak{a}_1\cup\cdots\cup \mathfrak{a}_n$이라 하자. 만일 $R$이 무한한 field를 포함하거나, 많아야 두 개의 $\mathfrak{a}_i$만이 prime ideal이 아니라면 $\mathfrak{b}$는 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$ 중 하나에 속한다. 

추가로, 만일 $A$가 graded이고 $\mathfrak{b}$가 homogeneous ideal이며 모든 $\mathfrak{a}_i$가 prime ideal이라면, $\mathfrak{b}$의 homogeneous element들이 $\mathfrak{a}_1\cup\cdots\cup \mathfrak{a}_n$에 속하는 것으로 가정해도 결론이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $R$이 무한한 field $\mathbb{k}$를 포함한다면, ideal들 각각을 $\mathbb{k}$-벡터공간으로 본다면 

$$\mathfrak{b}=\bigcup_{i=1}^n (\mathfrak{b}\cap \mathfrak{a}_i)$$

이고 임의의 $\mathbb{k}$-벡터공간은 자기 자신의 proper subspace들의 유한한 union으로 표현할 수 없으므로 자명하다. 

나머지 경우는 $n$에 대한 귀납법으로 증명한다. $n=1$일 경우는 증명할 것이 없다. 

큰 $n$에 대해서는, 만일 $\mathfrak{a}\_1,\ldots, \mathfrak{a}\_n$ 가운데 하나를 빼도 조건의 포함관계가 성립한다면 이는 귀납적 가정으로 해결 가능하므로 그렇지 않은 경우만 고려하면 충분하다. 즉, $x\_i\not\in \bigcup\_{j\neq i}\mathfrak{a}\_j$를 만족하는 $x\_i\in \mathfrak{b}$가 항상 존재한다고 가정해도 충분하며, $x\_i$의 조건에 의하여 반드시 $x\_i\in \mathfrak{a}\_i$이다. 

이제 $n=2$인 경우, $\mathfrak{b}$의 원소 $x_1+x_2$를 생각하자. 만일 $x_1+x_2\in \mathfrak{a}_1$이라면, $x_2=(x_1+x_2)-x_1\in \mathfrak{a}_1$이므로 모순이고, 비슷하게 $x_1+x_2$는 $\mathfrak{a}_2$의 원소일 수도 없다. 이는 $\mathfrak{b}\subseteq \mathfrak{a}_1\cup \mathfrak{a}_2$라는 가정에 모순이다. 

$n>3$인 경우도 비슷한 아이디어를 사용한다. 주어진 조건으로부터 $\mathfrak{a}\_1,\ldots \mathfrak{a}\_n$ 중 적어도 하나는 prime ideal이므로, 일반성을 잃지 않고 $\mathfrak{a}\_1$이 prime ideal이라 가정할 수 있다. 그럼 원소 $x_1+x_2x_3\cdots x_n$을 생각하고, $\mathfrak{a}_1$이 prime ideal이라는 가정을 잘 사용하면 모순을 얻는다. 

Graded ring의 경우는 $x_i$를 $x_2x_3\cdots$과 같은 degree를 갖도록 여러번 곱해서 차수만 맞춰주면 된다. 

</details>

특히 위의 보조정리는 앞의 전제조건보다는 나중 전제조건을 만족하고 많이 사용하게 된다. 

## Associated prime ideals

이제 우리는 $\Ass M$에 대해 조금 더 자세히 살펴본다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $A$-module $M$을 하나 고정하고, $\mathfrak{a}$가 $\ann(x)$ 꼴의 아이디얼들 중 maximal이라 가정하자. 그럼 $\mathfrak{a}$는 prime ideal이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$ab\in \mathfrak{a}$라 하고 $b\not\in \mathfrak{a}$라 한 후, $a\in \mathfrak{a}$임을 보여야 한다. $\mathfrak{a}=\ann(x)$라 하자. 그럼 가정에 의해 $abx=0$이고 $bx\neq 0$이다. 이제 $\mathfrak{a}\subseteq\ann(bx)$이므로 $\mathfrak{a}$의 maximality에 의하여 $\mathfrak{a}=\ann(bx)$이다. 이로부터 

$$(a)+\mathfrak{a}\subseteq \ann(bx)=\mathfrak{a}$$

이므로 $a\in \mathfrak{a}$임을 안다. 

</details>

위의 명제로부터 얻어지는 $\mathfrak{a}$는 prime ideal인 동시에 적당한 원소의 annihilator이므로 정의에 의해 $\Ass M$에 속한다. 

한편 [§국소화의 성질들, ⁋보조정리 3](/ko/math/commutative_algebra/properties_of_localization#lem3)에 의하여, 임의의 $A$-module $M$에 대하여, $x\in M$이 $0$인 것은 localization $\epsilon_\mathfrak{m}: M \rightarrow M_\mathfrak{m}$에서의 image가 모두 $0$인 것과 동치이며, 따라서 $x=0$인 것을 보이기 위해서는 모든 prime ideal $\mathfrak{p}$에 대하여 $\epsilon_\mathfrak{p}(x)=0$임을 보이면 충분하다. 다음 따름정리도 같은 맥락에서 이해할 수 있다. 

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> Noetherian ring $A$ 위에서 정의된 module $M$을 생각하자. 그럼 다음이 성립한다. 

1. $M$의 원소 $x$에 대하여, $x=0$인 것은 $M$의 maximal associated prime $\mathfrak{p}$가 주어질 때마다 $\epsilon_\mathfrak{p}(x)=0$인 것과 동치이다.
2. $M$의 submodule $L$에 대하여, $L=0$인 것과 모든 $\mathfrak{p}\in\Ass M$에 대하여 $L_\mathfrak{p}$인 것이 동치이다.
3. $A$-linear map $u:M \rightarrow N$이 injective인 것은 임의의 $\mathfrak{p}\in \Ass M$에 대하여 $u_\mathfrak{p}$가 injective인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 1번 결과의 경우, $A$가 noetherian이라는 가정으로부터 임의의 $x\in M$이 주어질 때마다 $\ann(x)$를 포함하는 annihilator ideal들 가운데 maximal인 ideal $\mathfrak{p}$를 하나 택할 수 있으며, [명제 3](#prop3)에 의해 $\mathfrak{p}\in \Ass M$이다. 따라서 $M_\mathfrak{p}$에서 $x/1$은 $0$이 되지 않는다. 2번 결과는 1번 결과에 의해 자명하며, 3번 결과는 2번 결과에서 $L=\ker u$로 두면 된다.

</details>

이번 글의 목표는 [정리 7](#thm7)을 증명하는 것이다. 이를 위해 다음의 두 보조정리가 필요하다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $A$-module들의 short exact sequence

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

가 주어졌다 하자. 그럼

$$\Ass M'\subset \Ass M\subset (\Ass M')\cup (\Ass M'')$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 포함관계는 자명하다. 두 번째 포함관계의 경우, $\mathfrak{p}\in\Ass M$이 $\Ass M'$에 속하지 않는다 가정하고 이것이 $\Ass M''$에 속함을 보이자. 만일 $x\in M$에 대하여 $\mathfrak{p}=\ann(x)$라면 $Ax\cong A/\mathfrak{p}$이다. 그런데 $\mathfrak{p}$가 prime ideal이므로, $0$이 아닌 임의의 $ax\in Ax$에 대하여 

$$a'\in\ann(ax)\iff a'ax=0\iff a'a\in \mathfrak{p}\iff a'\in \mathfrak{p}$$

가 되어 $\ann(ax)=\mathfrak{p}$이다. 여기서 마지막 동치는 $ax\neq 0$이라는 사실과 $Ax\cong A/\mathfrak{p}$인 것으로부터 $a\not\in \mathfrak{p}$를 사용하여 얻어졌다. 이제 이 등식은 특시 $Ax$의 임의의 $0$이 아닌 submodule은 annihilator로서 $\mathfrak{p}$를 가져야 한다는 것을 보여주는데, $\mathfrak{p}\not\in \Ass M'$인 사실과 종합하면 $Ax\cap M'=0$이어야 함을 안다. 따라서 $Ax$의 $M''$에서의 image는 $Ax$와 isomorphic하고, 이로부터 $\mathfrak{p}\in \Ass M''$임을 안다. 

</details>

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Noetherian ring $A$ 위에 정의된 finitely generated module $M$에 대하여, 다음 조건을 만족하는 filtration

$$0=M_0\subseteq M_1\subseteq\cdots\subseteq M_n=M,\qquad \text{$M_{k+1}/M_k\cong A/\mathfrak{p}_k$ for some prime $\mathfrak{p}_k$, for all $k$}$$

을 찾을 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 [명제 3](#prop3)을 이용해 $M$의 associated prime $\mathfrak{p}_1\in\Ass M$을 찾을 수 있고, 따라서 $M_1\cong A/\mathfrak{p}_1$을 만족하는 submodule $M_1$이 존재한다. 똑같은 논리를 $M/M_1$에 적용하여 $M_2$를 얻을 수 있으며, 이러한 과정을 반복하다보면 $M$이 noetherian인 것으로부터 원하는 결론을 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> Noetherian ring $A$ 위에 정의된 finitely generated module $M$에 대하여 다음이 성립한다.

1. $\Ass M$은 공집합이 아닌 유한집합이며, 이들 각각의 원소는 $\ann M$을 포함한다. 뿐만 아니라, $\ann M$을 포함하는 prime ideal들의 집합에서 minimal한 prime ideal들은 모두 $\Ass M$에 포함된다.
2. Associated prime들의 합집합은 $0$과, $M$의 모든 zero-divisor들의 모임으로 이루어진다.
3. 다음의 식
    
    $$\Ass_{S^{-1}A}S^{-1}M=\{\mathfrak{p}S^{-1}A: \mathfrak{p}\in\Ass M, \mathfrak{p}\cap S=\emptyset\}$$

    이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 결과의 경우, $\Ass M$이 공집합이 아닌 것은 [명제 3](#prop3)에 의한 것이며, $\Ass M$이 $\ann M$을 포함한다는 것은 자명하다. 한편, [보조정리 5](#lem5)에 의하여 다음 short exact sequence

$$0 \rightarrow M_{n-1} \rightarrow M_n \rightarrow M_n/M_{n-1} \rightarrow 0$$

를 생각하면 $\Ass M_n \subseteq \Ass M_{n-1}\cup \Ass M_n/M_{n-1}=\Ass M_{n-1}\cup \Ass A/\mathfrak{p}_n$이다. 

한편, 임의의 prime ideal $\mathfrak{p}$에 대하여 $\Ass(A/\mathfrak{p})=\\{\mathfrak{p}\\}$임을 다음과 같이 보일 수 있다. $\mathfrak{q}\in \Ass(A/\mathfrak{p})$라 하고, $\mathfrak{q}=\ann(x+\mathfrak{p})$로 적자. 그럼 우선 $\mathfrak{p}\subseteq \mathfrak{q}$임이 자명하다. 이는 임의의 $p\in \mathfrak{p}$에 대하여, 

$$p(x+\mathfrak{p})=px+\mathfrak{p}=0+\mathfrak{p}$$

이 성립하기 때문이다. 만일 $\mathfrak{q}\not\subseteq \mathfrak{p}$라면, $q\in \mathfrak{q}\setminus \mathfrak{p}$가 존재한다. 그럼

$$0=q(x+\mathfrak{p})=qx+\mathfrak{p}$$

인 것으로부터 $qx\in \mathfrak{p}$인 것을 알고, 그럼 $q\not\in \mathfrak{p}$인 것으로부터 $x+\mathfrak{p}$가 $0$이었어야 함을 안다. 그런데 이는 $\mathfrak{q}=A$라는 뜻이므로 모순이다. 

따라서, 위와 같은 방식으로

$$\Ass M \Ass M_{n-1}\cup \{ \mathfrak{p}_{n-1}\}\subseteq \Ass M_{n-2}\cup \{\mathfrak{p}_{n-1},\mathfrak{p}_{n-2}\}\cdots$$

를 반복하면 첫 번째 결과의 유한성을 얻는다. 

첫 번째 결과의 나머지 부분은 세 번째 결과를 증명하여 얻어진다. 그 전에 두 번째 결과의 경우, 만일 $a\in A$가 어떤 $x\in M$의 annihilator ideal에 속한다면, 이 annihilator ideal를 포함하는 maximal한 annihilator ideal을 생각할 수 있고 이것이 $\Ass M$에 속하므로 자명하다. 세 번째 결과의 경우는 표기법에 유의하며 [§국소화의 성질들, ⁋명제 5](/ko/math/commutative_algebra/properties_of_localization#prop5)를 사용하면 된다. 

세 번째 결과를 가정하면 남은 부분도 자명하다. 만일 $\mathfrak{p}$가 $\ann M$을 포함하는 prime ideal들 중 minimal한 것이라면, 세 번째 결과를 이용하면 localization $A_\mathfrak{p}$에서의 maximal ideal $\mathfrak{p}$를 생각할 수 있는데, $\ann M$을 포함하는 유일한 prime ideal이 $\mathfrak{p}$ 뿐이므로 반드시 $\mathfrak{p}\in \Ass M$이어야 한다.  

</details>




