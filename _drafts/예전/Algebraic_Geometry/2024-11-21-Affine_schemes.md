---

title: "아핀스킴"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-21
last_modified_at: 2024-11-21
weight: 6

---

앞선 글에서 언급했던, scheme을 정의하기 위한 우리의 과제를 다시 돌이켜보면 우리는 $\Spec A$ 위에 *structure sheaf*라 불리는 특정한 sheaf를 정의해야 한다. 또, 이렇게 $\Spec A$에 위상구조와 structure sheaf를 정의하고 나면 *affine scheme*은 적당한 $\Spec A$와 같은 것으로 취급할 수 있는 대상이라 했었는데, 이 때 같은 것으로 취급하는 것이 어떤 것인지, 즉 isomorphism이 무엇인지 또한 정의해야 한다. 이번 글에서는 이 두 가지를 해결한다.

## 환 달린 공간

Sheaf의 기본적인 정의는 [\[위상수학\] §준층](/ko/math/topology/presheaves) 및 [\[위상수학\] §연속함수들의 층](/ko/math/topology/sheaves)에서 이미 다루었다. 이들을 숙지하고 나면 다음은 이미 알고 있는 것에 특별한 이름을 붙인 것에 불과하다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$와, 그 위에 정의된 $\cRing$-valued sheaf $\mathscr{O}\_X$의 pair $(X,\mathscr{O}\_X)$를 *ringed space<sub>환 달린 공간</sub>*라 부른다. 만일 $X$의 임의의 점 $x$에 대하여, $x$에서의 stalk $\mathscr{O}\_{X,x}$가 항상 local ring이라면 이 pair $(X, \mathscr{O}\_X)$를 *locally ringed space<sub>국소적 환 달린 공간</sub>*라 부른다. 

</div>

우리의 목표는 $\Spec A$에 적당한 structure sheaf $\mathscr{O}\_{\Spec A}$를 정의하여 이를 locally ringed space로 만드는 것이다. 그럼 *affine scheme*은 locally ringed space로서 $(\Spec A, \mathscr{O}_{\Spec A})$와 isomorphic한 것으로 정의된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 두 ringed space $(X, \mathscr{O}\_X)$, $(Y, \mathscr{O}\_Y)$에 대하여, 이들 사이의 morphism은 연속함수 $f:X \rightarrow Y$와 $\Sh(Y)$에서의 morphism $f^\sharp:\mathscr{O}\_Y \rightarrow f_\ast \mathscr{O}\_X$의 pair를 의미한다. 

두 locally ringed space $(X, \mathscr{O}\_X)$, $(Y, \mathscr{O}\_Y)$ 사이의 morphism은 ringed space로서의 morphism $(f,f^\sharp)$이, 추가적으로 각각의 $x\in X$에 대하여 local homomorphism $f_p^\sharp:\mathscr{O}\_{Y,f(x)} \rightarrow \mathscr{O}\_{X,x}$를 유도하는 것이다. 

</div>

이로부터 locally ringed space들 사이의 isomorphism의 개념이 얻어진다.

## 아핀 스킴

이제 affine scheme을 정의하기 위해서는 $\Spec A$ 위에 structure sheaf만 정의하면 충분하다. 대략적인 아이디어는 $A$ 자체를 $\Spec A$ 위에 정의된 함수로 보고, 이들로 만들어지는 유리함수들의 sheaf를 $\mathscr{O}\_{\Spec A}$로 정의하는 것이다.

이 아이디어를 조금 더 구체적으로 얻기 위해, 특별히 $A=\mathbb{k}[\x_1,\ldots, \x_n]$인 경우를 기억하자. ([§스펙트럼, ⁋예시 9](/ko/math/algebraic_geometry/spectrums#ex9)) 그럼 $A$의 원소 $f$는 다항식이고, 이 때 closed point $(\x_1-x_1,\ldots,\x_n-x_n)$에서의 $f$의 함숫값은 $f(x_1,\ldots, x_n)$, 즉 다음의 ring homomorphism

$$A=\mathbb{k}[\x_1,\ldots, \x_n]\rightarrow \frac{\mathbb{k}[\x_1,\ldots,\x_n]}{(\x_1-x_1,\ldots,\x_n-x_n)}\cong \mathbb{k}$$

에 의한 $f$의 image로 주어진다. 더 일반적으로 $\Spec A$의 임의의 점 $\mathfrak{p}$에 대해서도 $f$의 함숫값은 $f$의 $A/\mathfrak{p}$에서의 image로 생각할 수 있다. 

한편, 우리는 전통적으로 다항식 뿐만 아니라 이들을 분모에 넣어서 얻어지는 유리함수들에도 관심을 가져왔었는데, 이 또한 우리의 논의로 들여오기는 어려운 일이 아니다. 물론 다항식을 분모에 넣기 위해서는 이 다항식이 정의역의 모든 점에서 $0$이 되지 않아야 하지만, 이것이 정확히 sheaf가 하는 일이다. 즉, 분모에 넣고자 하는 함수를 $f$라 하면, Zariski topology 상에서 $Z(f)$는 closed subset이므로 그 complement $D(f)$는 open subset이고, 이 때 $\mathscr{O}\_{\Spec A}(D(f))$에서는 $f$가 분모에 있는 형태를 마음껏 다뤄도 된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 고정된 원소 $f\in A$에 대하여, 

$$S=\{g\in A: D(f)\subseteq D(g)\}$$

으로 정의하자. 그럼 $S$는 $A$의 multiplicative subset이며, 이 때 $\mathscr{O}\_{\Spec A}(D(f))$를 $S^{-1}A$로 정의한다.

</div>

그럼 restriction map은 [\[가환대수학\] §국소화, §§환의 국소화](/ko/math/commutative_algebra/localization#환의-국소화)의 universal property로부터 자명하게 얻어진다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 위에서 정의한 $D(f)$들의 모임은 $\Spec A$의 base가 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Spec A$의 임의의 열린집합 $U$가 주어졌다 하자. 즉 적당한 $\mathfrak{a}$에 대하여 $U=Z(\mathfrak{a})^c$이다. 이제 임의의 $\mathfrak{p}\in U$에 대하여, $\mathfrak{p}\not\supseteq \mathfrak{a}$이므로 적당한 $f\in \mathfrak{a}\setminus \mathfrak{p}$가 존재한다. 이제 $D(f)$가 $\mathfrak{p}$를 포함하며 $U$에 속한다.

</details>

이제 [정의 3](#def3)의 데이터가 [\[위상수학\] §연속함수들의 층, ⁋명제 6](/ko/math/topology/sheaves#prop6)의 조건을 만족한다는 것은 다음 명제로부터 얻어진다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $(\Spec A,\mathscr{O}\_{\Spec A})$에 대하여 다음이 성립한다.

1. 임의의 $\mathfrak{p}\in\Spec A$에 대하여, $\mathscr{O}\_{\Spec A, \mathfrak{p}}$는 $A\_\mathfrak{p}$와 isomorphic하다.
2. 임의의 $f\in A$에 대하여, $\mathscr{O}\_{\Spec A}(D(f))$와 $A_f$가 isomorphic하다.
3. 따라서, $f=1$로 두면 $\Gamma(\Spec A,\mathscr{O}\_{\Spec A})\cong A$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 우선 이를 증명하기 위해서는 homomorphism $\varphi:\mathscr{O}\_{\Spec A, \mathfrak{p}} \rightarrow A\_\mathfrak{p}$을 만들고 나서 이것이 isomorphism임을 보여야 한다. Stalk의 정의에 의해, 이 morphism을 정의하기 위해서는 각각의 $U\ni \mathfrak{p}$에 대하여, compatibility 조건을 만족하는 homomorphism $\mathscr{O}\_{\Spec A}(U) \rightarrow A\_\mathfrak{p}$들을 만들면 된다. 이 때 $\mathscr{O}\_{\Spec A}(U)$의 원소는 함수 $s:U \rightarrow \coprod\_{\mathfrak{p}\in U}A\_\mathfrak{p}$와 같으므로, 이들 homomorphism들은 함수 $s$를 받아 $\mathfrak{p}$에서의 함수값 $s(\mathfrak{p})$를 내놓는 evaluation homomorphism으로 정하는 것이 자연스럽다.  
    이제 이렇게 정의한 homomorphism $\varphi$가 isomorphism인 것을 증명해야 한다. 우선 $\varphi$는 전사함수인데, 이는 임의의 $A\_\mathfrak{p}$의 원소는 항상 다음의 꼴

    $$\frac{a}{f},\qquad a\in A,\quad f\in A\setminus\mathfrak{p}$$

    의 꼴로 나타날 수 있고, $a/f$를 $\mathscr{O}\_{\Spec A}(D(f))$의 원소로 보면 $[(a/f, D(f))]\in\mathscr{O}\_{\Spec A, \mathfrak{p}}$가 $\varphi$에 의해 $a/f$로 옮겨지기 때문이다.  
    뿐만 아니라 $\varphi$는 injective이다. $\mathfrak{p}$의 근방 $U$를 택한 후, 이 위에서의 두 section $s,t\in \mathscr{O}\_{\Spec A}(U)$를 고르자. 일반성을 잃지 않고 $s,t$가 모두 $U$ 위에서 $s=a/f$, $t=b/g$의 꼴로 나타난다고 가정할 수 있다. 그럼 적당한 $h\in A\setminus \mathfrak{p}$가 존재하여 $h(ga-fb)=0$이므로, $h$가 $0$이 되지 않는 충분히 작은 $\mathfrak{p}$의 근방 (즉 열린집합 $D(h)\cap U$)에서 $s=t$가 성립하고, 따라서 $s$와 $t$는 같은 stalk을 갖게 된다. 
2. Ring homomorphism $\psi:A_f \rightarrow \mathscr{O}\_{\Spec A}(D(f))$를 정의하고, 이것이 isomorphism이라는 것을 증명해야 한다. $D(f)$의 각 점 $\mathfrak{p}$에 대해 $f\not\in\mathfrak{p}$이므로, 임의의 $a/f^n\in A_f$를 $A_\mathfrak{p}$의 원소로 볼 수 있다. 정의에 의해 이 함수는 $\mathscr{O}\_{\Spec A}(D(f))$의 원소이므로 이 대응은 $A_f$에서 $\mathscr{O}\_{\Spec A}(D(f))$로의 함수를 정의하며, 어렵지 않게 이것이 ring homomorphism임을 보일 수 있다. 이제 이것이 isomorphism임을 증명하자.  
    우선 $\psi$는 injective이다. 이를 보이기 위해서는 $\psi(a/f^n)=\psi(b/f^m)$이라 가정한 후, 충분히 큰 $N$에 대하여 $f^N(af^m-bf^n)=0$임을 보여야 한다. 가정에 의해 $\psi(a/f^n)=\psi(b/f^m)$이므로 임의의 $\mathfrak{p}\in D(f)$에 대하여, $A_\mathfrak{p}$에서 $a/f^n$과 $b/f^m$은 같은 원소가 되고, 따라서 적당한 $h\in A\setminus\mathfrak{p}$가 존재하여 $h(af^m-bf^n)=0$이 성립한다. 그럼 $af^m-bf^n$의 annihilator ideal 

    $$\mathfrak{a}=\{x\in A: x(af^m-bf^n)=0\}$$

    를 생각하면, 이러한 $h$의 존재로부터 $\mathfrak{a}\not\subseteq\mathfrak{p}$, 즉 $\mathfrak{p}\not\in Z(\mathfrak{a})$임을 안다. 한편 이것이 모든 점 $\mathfrak{p}\in D(f)$에 대해 성립하므로 $Z(\mathfrak{a})\cap D(f)=\emptyset$이고, 따라서 $Z(\mathfrak{a})\subseteq Z(f)$로부터 $\sqrt{\mathfrak{a}}\supseteq \sqrt{(f)}$이 성립한다. 그럼

    $$f\in \sqrt{(f)}\subseteq \sqrt{\mathfrak{a}}$$

    에서, 충분히 큰 $N$에 대해 $f^N\in\mathfrak{a}$임을 알고, 따라서 $f^N(af^m-bf^n)=0$으로부터 원하는 결론을 얻는다.  
    이제 $\psi$가 surjective임을 보여야 한다. 임의의 section $s\in \mathscr{O}(D(f))$를 택하자. 그럼 $\mathscr{O}\_{\Spec A}$의 정의로부터

    $$D(f)=\bigcup V_i,\qquad \text{$s=a_i/g_i$ on $V_i$, with $g_i\not\in\mathfrak{p}$ for all $\mathfrak{p}\in V_i$}$$

    이도록 할 수 있다. 한편, [보조정리 4](#lem4)로부터, $V_i=\bigcup D(h_{ij})$이도록 하는 적당한 $h_{ij}$들을 찾을 수 있으므로, 일반성을 잃지 않고 처음부터 $V_i=D(h_i)$라 할 수 있다. 그럼 임의의 $\mathfrak{p}\in V_i$에 대해 $g_i\not\in\mathfrak{p}$이므로, $V_i=D(h_i)\subseteq D(g_i)$이고 이로부터 $\sqrt{(h_i)}\subseteq\sqrt{(g_i)}$임을 알 수 있다. 따라서 충분히 큰 $N$에 대하여, $h_i^N\in (g_i)$이고 이로부터 $h_i^N=cg_i$로 적을 수 있다. 즉 $a_i/g_i=ca_i/h_i^N$이다. 한편 prime ideal의 성질로부터 $D(h_i)=D(h_i^N)$이고, 이를 통해 $D(f)$를 

    $$D(f)=\bigcup D(h_i),\qquad \text{$s=a_i/h_i$ on $D(h_i)$}$$

    으로 적을 수 있다.  
    이제 대략 partition of unity와 비슷한 방식으로 $\psi(a/f^n)=s$를 만족하는 $a/f^n\in A_f$를 찾을 수 있다. 이를 위해 우선 우리는 $D(f)$를 위와 같이 $D(h_i)$들의 합집합으로 표현할 때, 오직 <em_ko>유한 개의</em_ko> $D(h_i)$들만 있으면 충분하다는 것을 보인다. 이는 

    $$D(f)\subseteq \bigcup D(h_i)\iff Z(f)\supseteq \bigcap Z(h_i)=Z(\sum (h_i))\iff \sqrt{(f)}\subseteq \sqrt{\sum (h_i)}$$

    로부터, $f^n$을 유한합 $\sum b_ih_i$로 적을 수 있고, 따라서 이 유한합에 등장하는 $h_i$들에 대해서만 합집합을 돌려도 $D(f)\subseteq D(h_i)$가 성립하기 때문에 가능하다. 따라서

    $$D(f)=D(h_1)\cup\cdots\cup D(h_r), \qquad \text{$s=a_i/h_i$ on $D(h_i)$}$$

    라 하자.  
    교집합 $D(h_i)\cap D(h_j)=D(h_ih_j)$에서, $s$는 $a_i/h_i$를 $A_{h_ih_j}$의 원소로 본 것, 그리고 $a_j/h_j$를 $A_{h_ih_j}$의 원소로 본 것 두 가지의 표현을 갖는다. 앞서 우리는 $\psi$가 injective임을 보였으므로, $f=h_ih_j$에 대해 injectivity를 적용하면 이 두 표현은 같아야 한다. 즉 충분히 큰 $n$에 대하여

    $$(h_ih_j)^n(h_ja_i-h_ia_j)=0$$

    이 성립하며, 이러한 쌍 $(i,j)$는 유한개 뿐이므로 충분히 큰 $N$에 대해 

    $$(h_ih_j)^N(h_ja_i-h_ia_j)=0\iff h_i^Nh_j^{N+1}a_i=h_i^{N+1}h_ja_j$$

    이 <em_ko>모든</em_ko> 쌍 $(i,j)$에 대해 성립하도록 할 수 있다. 이제 $D(h_i)=D(h_i^N)$이므로, $f^n=\sum c_i h_i^{N+1}$이도록 하는 자연수 $n$이 존재한다. $a=\sum a_ic_ih_i^N$이라 하면, 각각의 $j$에 대해

    $$h_j^{N+1}a=\sum_i a_ic_ih_i^Nh_j^{N+1}=\sum_i a_jc_ih_i^{N+1}h_j^N=a_jh_j^N\sum c_ih_i^{N+1}=a_jh_j^Nf^n$$

    즉, $a/f^n=a_jh_j^N/h_j^{N+1}=a_j/h_j$이 성립한다. 이로부터 $\psi(a/f^n)=s$가 성립한다.

</details>

임의의 ring $A$에 대하여, prime ideal $\mathfrak{p}$에서의 localization $A\_\mathfrak{p}$는 항상 유일한 maximal ideal $\mathfrak{p}A_\mathfrak{p}$을 가지므로 $A\_\mathfrak{p}$는 local ring이다. 따라서 [명제 5](#prop5)의 첫 번째 결과로부터 우리는 임의의 ring $A$에 대하여 $\Spec A$는 locally ringed space임을 안다. 

## 아핀스킴

이제 드디어 affine scheme을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Locally ringed space $(X,\mathscr{O}\_X)$가 어떤 ring의 spectrum과 isomorphic하다면 이를 *affine scheme<sub>아핀스킴</sub>*이라 부른다. 두 affine scheme들 사이의 morphism은 locally ringed space들 사이의 morphism으로 정의한다. 

</div>

위의 정의에 의하여 $\Spec$은 $\cRing$에서 affine scheme들의 category $\AffSch$으로의 functor이다. 다음 명제는 여기에 더하여, $\Spec$이 두 category 사이의 categorical equivalence를 정의한다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 다음이 성립한다.

1. 임의의 ring $A$에 대하여, $(\Spec A, \mathscr{O}\_{\Spec A})$는 항상 locally ringed space이다.
2. Ring homomorphism $\phi:A \rightarrow B$는 locally ringed space 사이의 morphism 
    
    $$(f,f^\sharp):(\Spec B,\mathscr{O}_{\Spec B}) \rightarrow (\Spec A,\mathscr{O}_{\Spec A})$$

    을 유도한다.
3. 반대로, 두 locally ringed space $(\Spec B,\mathscr{O}\_{\Spec B})$에서 $(\Spec A,\mathscr{O}\_{\Spec A})$로의 임의의 morphism은 항상 위와 같은 방식으로 얻어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 지먕히디.
2. 잎서 [§스펙트럼, ⁋보조정리 3](/ko/math/algebraic_geometry/spectrums#lem3)에서 위의 map을 정의하고 이것이 두 ringed space들 사이의 morphism임을 보였다. 한편 prime ideal $\mathfrak{p}\in\Spec B$에 대하여

    $$f^\sharp_p:\mathscr{O}_{\Spec A, f(\mathfrak{p})} \rightarrow \mathscr{O}_{\Spec B, \mathfrak{p}}$$

    는 $\phi_\mathfrak{p}:A_{\phi^{-1}(\mathfrak{p})}\rightarrow B_\mathfrak{p}$와 같으며, 이는 $A_{\phi^{-1}(\mathfrak{p})}$의 유일한 maximal ideal $\phi^{-1}(\mathfrak{p})A_{\phi^{-1}(\mathfrak{p})}$를 $B\_\mathfrak{p}$의 유일한 maximal ideal $\mathfrak{p}B_\mathfrak{p}$로 보낸다. 
3. 마지막으로, locally ringed space들 사이의 morphism $(f,f^\sharp):(\Spec B, \mathscr{O}\_{\Spec B}) \rightarrow (\Spec A, \mathscr{O}\_{\Spec A})$가 주어졌다 하자. 그럼 우선 $f^\sharp:\mathscr{O}\_{\Spec A} \rightarrow \mathscr{O}\_{\Spec B}$의 global section을 보면

    $$f^\sharp(\Spec A):\Gamma(\Spec A, \mathscr{O}_{\Spec A}) \rightarrow \Gamma(f^{-1}(\Spec A), \mathscr{O}_{\Spec B})=\Gamma(\Spec B, \mathscr{O}_{\Spec B})$$

    이고, [⁋명제 5](#prop5)의 마지막 결과에 의하여 $f^\sharp(\Spec A)$는 $A$에서 $B$로의 ring homomorphism이 된다. 그럼 3번 주장을 보이기 위해서는 이 $\phi=f^\sharp(\Spec A):A \rightarrow B$가 사실은 ($\Spec$에 의하여) $f$와 같은 것임을 보여야 한다. 우선 임의의 $\mathfrak{p}\in\Spec B$에 대하여,

    $$f^\sharp_\mathfrak{p}:\mathscr{O}_{\Spec A, f(\mathfrak{p})} \rightarrow \mathscr{O}_{X,\mathfrak{p}}$$

    을 생각하자. 그럼 정의와 [⁋명제 5](#prop5)의 첫째 결과에 의하여, $f^\sharp_\mathfrak{p}$는 $A_{f(\mathfrak{p})}\rightarrow B(\mathfrak{p})$으로 생각할 수 있으며, 동시에 $\phi$의 정의에 의해 다음의 commutative diagram이 존재한다.

    ![localization](/assets/images/Math/Algebraic_Geometry/Affine_schemes-1.png){:style="width:7.5em" class="invert" .align-center}

    그런데 가정에 의하여 $f^\sharp_\mathfrak{p}$는 local homomorphism이므로, $A_{f(\mathfrak{o})}$의 유일한 maximal ideal (즉 $f(\mathfrak{p})$의 $A_{f(\mathfrak{p})}$에서의 상)이 $f^\sharp_\mathfrak{p}$에 의해 $B$의 유일한 maximal ideal (즉 $\mathfrak{p}$의 $B$에서의 상)으로 옮겨진다. 바꿔말하면 $\phi^{-!}(\mathfrak{p})=f(\mathfrak{p})$이 성립한다. 처음부터 $\mathfrak{p}$는 임의의 prime ideal로 잡았으므로 $\Spec\phi=f$이고, 이제 어렵지 않게 $f^\sharp$이 $\phi$로부터 유도되는 것을 보일 수 있다.

</details>

---
**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---