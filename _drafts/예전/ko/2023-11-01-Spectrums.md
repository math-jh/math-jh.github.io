---

title: "스펙트럼"
excerpt: "환의 스펙트럼"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/spectrums
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Spectrums.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-11-01
last_modified_at: 2023-11-01
weight: 4
toc: false

---

드디어 우리는 본격적으로 scheme을 정의하기 위한 첫 단계를 시작한다. [§대수다양체](/ko/math/algebraic_geometry/algebraic_varieties)에서 설명하였듯, scheme은 affine scheme들을 붙여서 만들어지며, 이들 affine scheme은 임의의 ring $A$로부터 만들어지는 ringed space $(\Spec A, \mathscr{O}\_{\Spec A})$이다. 

## 자리스키 위상

우선 위상공간으로서 $\Spec A$가 무엇인지를 정의해야 한다. Ring $A$의 prime ideal들의 집합을 $\Spec A$로 적고, 임의의 ideal $\mathfrak{a}\leq A$에 대하여, $V(\mathfrak{a})$를 $\mathfrak{a}$를 포함하는 prime ideal들의 모임이라 하자. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 다음이 성립한다.

1. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $V(\mathfrak{ab})=V(\mathfrak{a})\cup V(\mathfrak{b})$가 성립한다.
2. $A$의 ideal들의 모임 $\\{\mathfrak{a}\_i\\}$에 대하여, $V(\sum \mathfrak{a}\_i)=\bigcap V(\mathfrak{a}\_i)$가 성립한다.
3. $A$의 임의의 ideal $\mathfrak{a},\mathfrak{b}$에 대하여, $V(\mathfrak{a})\subseteq V(\mathfrak{b})\iff \sqrt{\mathfrak{a}}\supseteq \sqrt{\mathfrak{b}}$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\mathfrak{a}$ 혹은 $\mathfrak{b}$를 포함하는 prime ideal $\mathfrak{p}$는 그보다 작은 ideal $\mathfrak{ab}$ 또한 포함하는 것이 자명하므로, 반대방향 포함관계만 보이면 충분하다. $\mathfrak{p}\supset \mathfrak{ab}$라 가정하자. 만일 $\mathfrak{p}\not\supseteq \mathfrak{b}$라 하면, $b\not\in \mathfrak{p}$인 $\mathfrak{b}$의 원소 $b$를 찾을 수 있다. 한편, 임의의 $a\in \mathfrak{a}$에 대하여, $ab\in \mathfrak{ab}\subseteq \mathfrak{p}$이고, 앞선 가정에 의해 $b\not\in \mathfrak{p}$이므로 반드시 $a\in \mathfrak{p}$이고 따라서 $a\subseteq \mathfrak{p}$가 성립한다.
2. 이는 $\sum \mathfrak{a}_i$가 ideal들 $\mathfrak{a}_i$ 각각을 모두 포함하는 ideal 중 가장 작은 것으로 정의되므로 자명하다.
3. Ideal $\mathfrak{a}$의 radical $\sqrt{\mathfrak{a}}$는 $\mathfrak{a}$를 포함하는 prime ideal들을 모두 교집합하여 얻어지므로 자명하다.

</details>

이 보조정리에 의해, $\Spec A$ 위에 위상구조를 줄 수 있다. 이는 간단히 $\Spec A$의 닫힌집합들을 $V(\mathfrak{a})$들이라고 선언하면 되고, 실제로 $V(\mathfrak{a})$들이 닫힌집합이 만족해야 할 성질들을 만족한다는 것이 위의 보조정리이다. 이렇게 정의된 위상을 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다.

## 스펙트럼

우선 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위상공간 $X$와, 그 위에 정의된 ring-valued sheaf $\mathscr{O}_X$의 pair $(X,\mathscr{O}_X)$를 *ringed space<sub>환 달린 공간</sub>*라 부른다. Ringed space $(X,\mathscr{O}\_X)$에서 $(Y,\mathscr{O}\_Y)$로의 *morphism*은 연속함수 $f:X \rightarrow Y$와, sheaf morphism $f^\sharp:\mathscr{O}\_Y \rightarrow f\_\ast\mathscr{O}\_X$으로 주어진다.

</div>

이번 글의 목표는 ring $A$로부터 ringed space $(\Spec A, \mathscr{O}\_{\Spec A})$를 만들고, 이것이 $\cRing$에서 ringed space들의 카테고리로의 contravariant functor를 정의한다는 것을 증명하는 것이다. 이를 위해서는 우선 $\Spec A$ 위에 sheaf of rings $\mathscr{O}$를 정의해야 한다. 

임의의 열린집합 $U\subseteq \Spec A$에 대하여, $\mathscr{O}(U)$의 원소들은 각 점 $\mathfrak{p}$에서의 값이 $A_\mathfrak{p}$에 속하는 함수들 $s:U \rightarrow \coprod\_{\mathfrak{p}\in U}A\_\mathfrak{p}$ 가운데, $s$가 local하게도 $A$의 원소의 quotient로 쓰여지는 함수들의 모임으로 정의한다. 즉, 임의의 $\mathfrak{p}\in U$가 주어졌을 때마다, $\mathfrak{p}$의 적당한 근방 $V\subseteq U$가 존재하여, 모든 $\mathfrak{q}\in V$마다 $s(\mathfrak{q})=a/f$이도록 하는 $a,f\in A$가 존재해야 한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Ring $A$에 대하여, $A$의 *spectrum<sub>스펙트럼</sub>*은 위의 과정을 통해 얻어진 ringed space $(\Spec A,\mathscr{O}\_{\Spec A})$를 의미한다. $\mathscr{O}\_{\Spec A}$를 $\Spec A$의 *structure sheaf*라 부른다.

</div>

혼동의 여지가 없을 때에는 $(\Spec A, \mathscr{O}\_{\Spec A})$ 대신 간단히 $\Spec A$로만 적는다. 우리는 위에서 $\mathscr{O}\_{\Spec A}$가 어떻게 생겼는지를 정확하게 묘사하긴 하였으나, 모든 열린집합에 대해 위의 계산을 반복하는 것은 현명한 일이 아니다. 

일반적으로 어떠한 위상공간 위에서 정의된 임의의 sheaf를 묘사하기 위해서는 이 sheaf가 그 위상공간의 base 위에서 어떻게 정의되는지만 알면 충분하다. 이는 몇 가지 사실로부터 자명한데, 

1. 임의의 열린집합을 가져올 때마다 그 열린집합에 포함된 base의 원소가 있으므로, base에 속하는 열린집합들에 대해서만 limit을 취해도 stalk은 똑같이 나온다. 
2. Sheaf $\mathscr{F}$와 고정된 열린집합 $U$에 대하여, $\mathscr{F}(U)\rightarrow\prod_{x\in U} \mathscr{F}_x$는 injective이며, 그 image는 [§층, ⁋보조정리 4](/ko/math/algebraic_geometry/sheaves#lem4)를 증명할 때 쓰였던 compatibility condition을 만족하는 $(s_x)$들의 모임이다.
3. 1번에서 만들어낸 stalk들은 위의 compatibility condition을 만족하고, 따라서 2번 결과로부터 $\mathscr{F}(U)$를 복원할 수 있다. 

각 사실들에 대한 증명은 생략하였지만 이들은 전부 어렵지 않다. 어쨌든 이로부터 우리는 $\Spec A$의 괜찮은 base만 찾아오면 된다. 임의의 $f\in A$에 대하여, 열린집합 $D(f)$를 $V((f))$의 complement로 정의하자. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 위에서 정의한 $D(f)$들의 모임은 위상공간 $\Spec A$의 base가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Spec A$의 임의의 열린집합 $U$가 주어졌다 하자. 즉 적당한 $\mathfrak{a}$에 대하여 $U=V(\mathfrak{a})^c$이다. 이제 임의의 $\mathfrak{p}\in U$에 대하여, $\mathfrak{p}\not\supseteq \mathfrak{a}$이므로 적당한 $f\in \mathfrak{a}\setminus \mathfrak{p}$가 존재한다. 이제 $D(f)$가 $\mathfrak{p}$를 포함하며 $U$에 속한다.

</details>

그럼 다음 명제의 두 번째 결과로부터 $\mathscr{O}\_{\Spec A}$를 더 현명하게 표현할 수 있다. 

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
    우선 $\psi$는 injective이다. 이를 보이기 위해서는 $\psi(a/f^n)=\psi(b^m)$이라 가정한 후, 충분히 큰 $N$에 대하여 $f^N(af^m-bf^n)=0$임을 보여야 한다. 가정에 의해 $\psi(a/f^n)=\psi(b^m)$이므로 임의의 $\mathfrak{p}\in D(f)$에 대하여, $A_\mathfrak{p}$에서 $a/f^n$과 $b/f^m$은 같은 원소가 되고, 따라서 적당한 $h\in A\setminus\mathfrak{p}$가 존재하여 $h(af^m-bf^n)=0$이 성립한다. 그럼 $af^m-bf^n$의 annihilator ideal 

    $$\mathfrak{a}=\{x\in A: x(af^m-bf^n)=0\}$$

    를 생각하면, 이러한 $h$의 존재로부터 $\mathfrak{a}\not\subseteq\mathfrak{p}$, 즉 $\mathfrak{p}\not\in V(\mathfrak{a})$임을 안다. 한편 이것이 모든 점 $\mathfrak{p}\in D(f)$에 대해 성립하므로 $V(\mathfrak{a})\cap D(f)=\emptyset$이고, 따라서 $V(\mathfrak{a})\subseteq V(f)$로부터 $\sqrt{\mathfrak{a}}\supseteq \sqrt{(f)}$이 성립한다. 그럼

    $$f\in \sqrt{(f)}\subseteq \sqrt{\mathfrak{a}}$$

    에서, 충분히 큰 $N$에 대해 $f^N\in\mathfrak{a}$임을 알고, 따라서 $f^N(af^m-bf^n)=0$으로부터 원하는 결론을 얻는다.  
    이제 $\psi$가 surjective임을 보여야 한다. 임의의 section $s\in \mathscr{O}(D(f))$를 택하자. 그럼 $\mathscr{O}\_{\Spec A}$의 정의로부터

    $$D(f)=\bigcup V_i,\qquad \text{$s=a_i/g_i$ on $V_i$, with $g_i\not\in\mathfrak{p}$ for all $\mathfrak{p}\in V_i$}$$

    이도록 할 수 있다. 한편, [보조정리 4](#lem4)로부터, $V_i=\bigcup D(h_{ij})$이도록 하는 적당한 $h_{ij}$들을 찾을 수 있으므로, 일반성을 잃지 않고 처음부터 $V_i=D(h_i)$라 할 수 있다. 그럼 임의의 $\mathfrak{p}\in V_i$에 대해 $g_i\not\in\mathfrak{p}$이므로, $V_i=D(h_i)\subseteq D(g_i)$이고 이로부터 $\sqrt{(h_i)}\subseteq\sqrt{(g_i)}$임을 알 수 있다. 따라서 충분히 큰 $N$에 대하여, $h_i^N\in (g_i)$이고 이로부터 $h_i^N=cg_i$로 적을 수 있다. 즉 $a_i/g_i=ca_i/h_i^N$이다. 한편 prime ideal의 성질로부터 $D(h_i)=D(h_i^N)$이고, 이를 통해 $D(f)$를 

    $$D(f)=\bigcup D(h_i),\qquad \text{$s=a_i/h_i$ on $D(h_i)$}$$

    으로 적을 수 있다.  
    이제 대략 partition of unity와 비슷한 방식으로 $\psi(a/f^n)=s$를 만족하는 $a/f^n\in A_f$를 찾을 수 있다. 이를 위해 우선 우리는 $D(f)$를 위와 같이 $D(h_i)$들의 합집합으로 표현할 때, 오직 <em_ko>유한 개의</em_ko> $D(h_i)$들만 있으면 충분하다는 것을 보인다. 이는 

    $$D(f)\subseteq \bigcup D(h_i)\iff V(f)\supseteq \bigcap V(h_i)=V(\sum (h_i))\iff \sqrt{(f)}\subseteq \sqrt{\sum (h_i)}$$

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

## $\Spec$ 함자

마지막으로 우리는 위의 대응의 functoriality를 보인다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Ring homomorphism $\phi:A \rightarrow B$는 ringed space 사이의 morphism 
    
$$(f,f^\sharp):(\Spec B,\mathscr{O}_{\Spec B}) \rightarrow (\Spec A,\mathscr{O}_{\Spec A})$$

을 유도한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Ring homomorphism $\phi:A \rightarrow B$와, $B$의 임의의 prime ideal $\mathfrak{p}$에 대하여 $\phi^{-1}(\mathfrak{p})$는 $A$의 prime ideal이다. 이러한 방식으로 $f:\Spec B \rightarrow \Spec A$를 정의하자. 즉 함수로서 $f(\mathfrak{p})=\phi^{-1}(\mathfrak{p})$로 정의된다. 이렇게 정의한 $f$의 연속성을 보이기 위해서는 임의의 닫힌집합의 $f$에 대한 preimage가 닫힌집합임을 보이면 된다. ([\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)) 그런데 $\Spec A$의 임의의 닫힌집합은 모두 $V(\mathfrak{a})$의 꼴이므로, 이는 $f^{-1}(V(\mathfrak{a}))$가 항상 닫힌집합임을 보이는 것과 같다. 이는 다음 식
    
$$f^{-1}(V(\mathfrak{a}))=V(\phi(\mathfrak{a}))\tag{$\ast$}$$

으로부터 얻어진다. 식 ($\ast$)을 확인하기 위해 $f(\mathfrak{p})=\phi^{-1}(\mathfrak{p})\in V(\mathfrak{a})$인 $\mathfrak{p}\in\Spec B$를 택하자. 즉 $\mathfrak{a}\subseteq\phi^{-1}(\mathfrak{p})$이고 이로부터 $\phi(\mathfrak{a})\subseteq \mathfrak{p}$이므로 $\mathfrak{p}\in V(\mathfrak{a})$이다. 한편 임의의 $\mathfrak{p}\in V(\phi(\mathfrak{a}))$에 대하여,

$$\phi(\mathfrak{a})\subseteq \mathfrak{p}\implies \mathfrak{a}\subseteq \phi^{-1}(\phi(\mathfrak{a}))\subseteq \phi^{-1}(\mathfrak{p})=f(\mathfrak{p})$$

이므로 $f(\mathfrak{p})\in V(\mathfrak{a})$임을 안다.  
한편, structure sheaf 사이의 morphism $f^\sharp:\mathscr{O}\_{\Spec B}\rightarrow f_\ast\mathscr{O}\_{\Spec A}$은 임의의 열린집합 $V\subseteq \Spec A$에 대하여, 

$$f^\sharp\vert_V:\mathscr{O}_{\Spec A}(V) \rightarrow \mathscr{O}_{\Spec B}(f^{-1}(V));\quad s\mapsto s\circ f$$

으로 주어진다.

</details>

---
**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---
