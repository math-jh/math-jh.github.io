---

title: "에탈대수"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/etale_algebras
header:
    overlay_image: /assets/images/Math/Field_Theory/Etale_algebras.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-11
last_modified_at: 2025-05-11
weight: 5

---

$\mathbb{K}$-algebra $A$와 field extension $\mathbb{L}/\mathbb{K}$가 주어졌다 가정하자. 그럼 $\mathbb{K}$-벡터공간들 사이의 $\mathbb{K}$-linear map들의 모임 $\Hom_\mathbb{K}(A, \mathbb{L})$은 $\mathbb{K}$-벡터공간이며, 다음의 isomorphism

$$\Hom_\mathbb{K}(A,\mathbb{L})\cong\Hom_\mathbb{K}(A, \mathbb{K}\otimes_\mathbb{K}\mathbb{L})\cong\Hom_\mathbb{K}(A, \mathbb{K})\otimes_\mathbb{K}\mathbb{L}=A^\ast\otimes_\mathbb{K}\mathbb{L}$$

을 통해 $\mathbb{L}$-벡터공간으로 생각할 수도 있다. ([\[다중선형대수학\] §Hom과 텐서곱, ⁋명제 3](/ko/math/multilinear_algebra/hom_and_tensor#prop3)) 

위의 과정의 순서를 살짝 바꾸어 $A_{(\mathbb{L})}=\mathbb{L}\otimes_\mathbb{K}A$의 ($\mathbb{L}$-벡터공간으로서의) dual $(A_{(\mathbb{L})})^\ast$를 생각하자. 그럼 Hom-tensor adjoint

$$(A_{(\mathbb{L})})^\ast=\Hom_\mathbb{L}(\mathbb{L}\otimes_\mathbb{K}A, \mathbb{L})\cong\Hom_\mathbb{K}(A, \Hom_\mathbb{L}(\mathbb{L}, \mathbb{L}))\cong\Hom_\mathbb{K}(A, \mathbb{L})$$

이 존재하므로, 이로부터 $\mathbb{L}$-벡터공간들 사이의 isomorphism

$$(A_{(\mathbb{L})})^\ast=\Hom_\mathbb{L}(A_{(\mathbb{L})}, \mathbb{L})\cong\Hom_\mathbb{K}(A,\mathbb{L})\cong A^\ast\otimes_\mathbb{K}\mathbb{L}$$

을 얻는다. 특히, 만일 $A$가 $\mathbb{K}$-벡터공간으로서 유한차원이라면 $A^\ast$는 같은 차원의 $\mathbb{K}$-벡터공간이고, 따라서 $A_{(\mathbb{L})}$과 $A_{(\mathbb{L})}^\ast$ 또한 같은 차원의 $\mathbb{L}$-벡터공간이다. 특히 다음의 식

$$[A_{(\mathbb{L})}:\mathbb{L}]=\dim_\mathbb{L}A_{(\mathbb{L})}=\dim_\mathbb{L} (A_{(\mathbb{L})})^\ast=\dim_\mathbb{K}A=[A:\mathbb{K}]$$

을 얻는다. 이로부터 다음과 같이 이번 글의 핵심 아이디어들을 얻는다. 

1. Extension degree $[A:\mathbb{K}]$는 base field를 바꾸는 것에 대하여 잘 행동한다. 
2. Extension degree $[A:\mathbb{K}]$를 구하기 위해서는 아무 extension $\mathbb{L}/\mathbb{K}$을 취한 후 $\Hom_\mathbb{K}(A,\mathbb{L})$의 차원을 계산하는 것으로 충분하다. 

그럼 다음 정리는 둘째 아이디어에 관련된 것으로, 우리의 관심의 대상인 $\Hom_\mathbb{K}(A,\mathbb{L})$의 차원을 계산하는 데에 도움을 준다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Extension $\mathbb{L}/\mathbb{K}$이 주어졌다 하고 $\mathbb{K}$-algebra $A$를 고정하자. 그럼 $\Hom_{\Alg{\mathbb{K}}}(A,\mathbb{L})$는 $\mathbb{L}$-벡터공간 $\Hom_\mathbb{K}(A, \mathbb{L})$의 free subset이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉, $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$의 임의의 유한한 부분집합 $\\{u_1,\ldots, u_n\\}$이 반드시 linearly independent임을 보이면 충분하다. $n$에 대한 귀납법을 사용한다. $n=0$인 경우는 자명하므로, $n \geq 1$이라고 하자.

$\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$의 원소들 $u_1,\ldots, u_n$에 대하여, $\mathbb{L}$의 원소들 $\alpha_1,\ldots,\alpha_n$이 다음의 식

$$\sum_{i=1}^{n} \alpha_i u_i = 0$$

을 만족한다 하자. 그럼 $x,y\in A$에 대해 다음의 계산

$$\sum_{i=1}^{n-1} \alpha_i([u_i(x) - u_n(x)) u_i(y) = \sum_{i=1}^{n} \alpha_i u_i(xy) - u_n(x) \sum_{i=1}^{n} \alpha_i u_i(y) = 0$$

으로부터 

$$\sum_{i=1}^{n-1} \alpha_i(u_i(x) - u_n(x)) u_i = 0$$

임을 안다. 이제 귀납적 가정으로부터, 위의 식의 계수부분에 해당하는 $\alpha_i(u_i(x)-u_n(x))$들이 모두 $0$이어야 함을 안다. 그런데 $u_1,\ldots, u_n$은 모두 서로 다른 원소들이고, 따라서 이것이 $x$의 값에 무관하게 항등적으로 $0$이기 위해서는 $\alpha_i=0$이 모든 $i=1,\ldots, n-1$에 대해 성립해야 한다. 이를 다시 가정의 식에 대입하면 $\alpha_n$ 또한 $0$이어야 함을 안다. 

</details>

이 정리 자체는 그렇게까지 놀랄만한 것은 아닌데, 가령 $\Hom_\mathbb{K}(\mathbb{K},\mathbb{K})$와 부분집합 $\Hom_{\Alg{\mathbb{K}}}(\mathbb{K},\mathbb{K})$이 주어졌다 하면, 임의의 $\lambda\in \mathbb{K}$에 대하여 다음의 함수

$$x\mapsto \lambda x$$

는 항상 $\mathbb{K}$-vector space이지만, 이것이 $\mathbb{K}$-algebra homomorphism이기 위해서는 식 $\lambda(xy)=\lambda(x)\lambda(y)$가 성립해야 하므로 $\lambda^2=\lambda$여야 하고, 따라서 $\Hom_{\Alg{\mathbb{K}}}(\mathbb{K},\mathbb{K})$는 오직 하나의 원소 $\id$로만 이루어지기 때문이다. 

어쨌든 위의 정리로부터 우리는 다음의 부등식

$$\lvert\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})\rvert\leq \dim_\mathbb{L}\Hom_\mathbb{K}(A,L)=[A:\mathbb{K}]$$

을 얻는다. 특히 다음의 두 따름정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins>  Monoid $\Gamma$, field $\mathbb{L}$을 고정하고, $X$를 $\Gamma$에서 $\mathbb{L}^\times$로의 homomorphism들의 집합이라 하자. 그럼 $X$는 $\Gamma$에서 $\mathbb{L}$로 가는 함수들의 $\mathbb{L}$-벡터공간 $L^\Gamma$에서의 free subset이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>  

Monoid algebra $A=L\Gamma$를 생각하고, canonical basis $(e\_\gamma)\_{\gamma\in\Gamma}$를 생각하자. 

그럼 [\[대수적 구조\] §대수, ⁋명제 6](/ko/math/algebraic_structures/algebras)의 일반화를 통해 $X$와 $\Hom_\mathbb{L}(A,\mathbb{L})$ 사이의 bijection이 존재하므로 주장은 [정리 1](#thm1)로부터 바로 따라나온다. 

</details>

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3 (Dedekind)**</ins> 두 extension $\mathbb{L}/\mathbb{K}$, $\mathbb{M}/\mathbb{K}$에 대하여, $\mathbb{M}$에서 $\mathbb{L}$로의 morphism들의 집합은 $\mathbb{L}$-벡터공간으로서 free이다. 특히 만일 $\mathbb{M}/\mathbb{K}$가 finite degree extension이라면 이 집합의 원소의 개수는 많아야 $[\mathbb{M}:\mathbb{K}]$개다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A=\mathbb{M}$으로 두고 [정리 1](#thm1)을 사용하면 된다. 둘째 주장은 $\Hom_\mathbb{K}(\mathbb{M},\mathbb{L})$이 $\mathbb{L}$-벡터공간으로서 $[\mathbb{M}:\mathbb{K}]$차원이기 때문에 당연하다. 

</details>

더 나아가, 만일 $\mathbb{K}$가 무한집합이라면 이들은 *algebraically independent*이기도 하다. 

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 무한한 field $\mathbb{K}$와 extension $\mathbb{L}/\mathbb{K}$가 주어졌다 하고, $\mathbb{K}$-algebra $A$를 고정하자. 만일 $A$-algebra homomorphism들 $u_1,\ldots, u_n:A \rightarrow \mathbb{L}$에 대하여, 다항식 $f\in \mathbb{L}[\x_1,\ldots, \x_n]$이 항등적으로 $f(u_1,\ldots, u_n)=0$을 만족한다면 $f=0$이어야 한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(u_1(x), \dots, u_n(x))$의 꼴을 가지는 $\mathbb{L}^n$의 부분집합을 $B$라 하자. 그럼 [정리 1](#thm1)로부터 우리는 

$$\sum_{i=1}^n\alpha_i u_i(x)=0$$

을 모든 $x\in A$에 대해 만족하는 $\alpha_1,\ldots, \alpha_n$은 존재하지 않음을 안다. 바꿔 말하면, bilinear pairing $B\times \mathbb{L}^n \rightarrow \mathbb{L}$을 

$$\bigl((u_1(x),\cdots, u_n(x)), (\alpha_1,\ldots, \alpha_n)\bigr) \mapsto \sum_{i=1}^n \alpha_iu_i(x)$$

으로 정의한다면 이것이 유도하는 $\mathbb{L}^n\rightarrow B^\ast$가 injective이고, 이로부터 $B$가 $\mathbb{L}$을 생성해야 하는 것을 안다. 따라서, $n\times n$ 행렬 $(u_i(a_j))$이 invertible이도록 하는 $a_j\in A$들이 존재한다. 

이제 다항식 $g \in \mathbb{L}[\y_1,\ldots, \y_n}$을 다음의 식

$$g(\y_1, \ldots, \_n) = f\left( \sum_{j=1}^n u_1(a_j)y_j, \ldots, \sum_{j=1}^n u_n(a_j)\y'_j \right)$$

으로 정의하자. 여기에 임의의 원소들 $y_i\in \mathbb{K}$들을 대입하고, $x=\sum_{i=1}^n a_iy_i$라 하면 

$$g(y_1, \dots, y_n) = f(u_1(x), \dots, u_n(x)) = 0$$

이고, $f$의 가정으로부터 우리는 $g(y_1,\ldots, y_n)=0$이어야 함을 안다. 이제 $\mathbb{K}$는 무한집합이므로 $g$는 항등적으로 $0$이어야만 하고, $(u_i(a_j))$의 역행렬을 $(v_{ij})$라 하면

$$f(\x_1,\ldots, \x_n)=g\left(\sum_{j=1}^n b_{1j}\x_j, \dots, \sum_{j=1}^n b_{nj}\x_j \right)$$

이므로 $f$도 항등적으로 $0$이다.

</details>

## 에탈대수

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $\mathbb{K}$-algebra $A$가 *diagonalizable*이라는 것은 적절한 $n\geq 0$이 존재하여, $\mathbb{K}$-algebra isomorphism $A\cong \mathbb{K}^n$이 존재하는 것이다. 만일 적당한 $n\geq 0$에 대하여 $\mathbb{L}$-algebra isomorphism $A_{(\mathbb{L})}\cong \mathbb{L}^n$가 존재하도록 하는 extension $\mathbb{L}/\mathbb{K}$가 존재한다면, 이 extension이 $A$를 *diagonalize*한다고 말한다. 만일 $A$를 diagonalize하는 적절한 extension $\mathbb{L}/\mathbb{K}$가 존재한다면 $A$를 *étale algebra*라 부른다. 

</div>

Diagonalizable algebra는 그 extension degree $[A:\mathbb{K}]$가 잘 정의된다는 점에서 유용하다. 이 글의 서두에서 밝힌 첫 번째 핵심 아이디어를 사용하면 étale algebra는 이와 동일한 정도로 유용하다고 할 수 있다. 

우선 diagonalizable algebra에 대한 다음의 characterization부터 시작한다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Finite degree $n$을 갖는 $\mathbb{K}$-algebra $A$에 대하여, 다음이 모두 동치이다. 

1. $A$가 diagonalizable이다. 
2. $A$의 적당한 basis $(e_1,\ldots, e_n)$이 존재하여 $e_i^2=e_i$이고 $e_ie_j=0$이도록 할 수 있다. 
3. $A$에서 $\mathbb{K}$로의 $\mathbb{K}$-algebra homomorphism들이 $A^\ast$를 생성한다. 
4. 임의의 $A$-module은 $\mathbb{K}$에 대해 1차원인 submodule들의 direct sum으로 쪼개진다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 조건이 동치인 것은 $\mathbb{K}^n$ 위에 정의된 곱셈구조에서 바로 따라나온다. 한편 $\mathbb{K}^n$에서 $\mathbb{K}$로의 $n$개의 projection들이 $\mathbb{K}$-algebra homomorphism이므로 이들 조건은 셋째 조건을 함의한다.

거꾸로 셋째 조건이 성립한다 하고, $A^\ast$의 basis $u_1,\ldots, u_n$을 택하자. 그럼 $x\mapsto (u_i(x))$가 $A$에서 $\mathbb{K}^n$으로의 $\mathbb{K}$-algebra isomorphism인 것을 보일 수 있으므로 앞선 세 개의 조건이 모두 동치이다.

이제 넷째 조건의 동치를 보여야 한다. 이를 위해 둘째 조건이 성립한다 가정하고, 임의의 $A$-module $M$을 하나 택하자. 그럼 $x\mapsto e_ix$로 정의된 $M$의 $A$-endomorphism을 생각하면, $M$은 $e_iM$들의 direct sum이고 이로부터 넷째 조건이 나온다. 거꾸로 넷째 조건이 성립한다 가정하면 특별히 $A$ 자기자신을 1차원 $\mathbb{K}$-벡터공간들의 internal direct sum으로 쓸 수 있고, 이 때의 basis가 둘째 동치의 조건을 만족하는 것을 확인할 수 있다. 

</details>

특히 넷째 조건은 $A$를 *diagonalizable*이라 부르는 것에 대해 어느정도의 정당성을 부여한다. 다음 따름정리는 [정리 1](#thm1)의 집합 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$가 언제 *basis*가 되는지를 알려준다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> Field extension $\mathbb{L}/\mathbb{K}$와, $\mathbb{K}$-algebra homomorphism들 $A \rightarrow \mathbb{L}$들의 모임 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$를 생각하자. 그럼 부등식 

$$\lvert \Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})\rvert \leq [A:\mathbb{K}]$$

에서 등호가 성립하는 것은 $A$가 $\mathbb{L}$에 의해 diagonalize되는 것과 동치이며, 이 때 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$는 $\Hom_\mathbb{K}(A,\mathbb{L})$의 basis를 이룬다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>  

우리는 이미 $\dim_\mathbb{L}\Hom_\mathbb{K}(A,\mathbb{L})=\dim_\mathbb{K}A$임을 알고 있으며, [정리 1](#thm1)에 의해 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$는 $\Hom_\mathbb{K}(A,\mathbb{L})$의 free subset임을 안다. 따라서, 주장의 부등식이 성립하는 것이 자명하며, 등호는 오직 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$가 $\Hom_\mathbb{K}(A,\mathbb{L})$의 basis일 때 성립한다. 

한편 $\mathbb{L}$-vector space isomorphism $\Hom_\mathbb{K}(A,\mathbb{L}) \rightarrow (A_{(\mathbb{L})})^\ast$는 부분집합 $\Hom_\Alg{\mathbb{K}}(A, \mathbb{L})$을 algebra homomorphism $A_{(\mathbb{L})} \rightarrow \mathbb{L}$들의 집합 $\Hom_\Alg{\mathbb{K}}(A_{(\mathbb{L})}, \mathbb{L})$으로 보낸다. 이제 [명제 6](#prop6)의 셋째 동치조건에 의하여 이 집합 $\Hom_\Alg{\mathbb{K}}(A_{(\mathbb{L})}, \mathbb{L})이 $(A\_{(\mathbb{L})})^\ast$를 생성하는 것이 $A$가 $\mathbb{L}$에 의해 diagonalize되는 것과 동치이므로 원하는 결과를 얻는다.

</details>

즉, 만일 $A$가 étale algebra라면 $A$의 $\mathbb{K}$에 대한 extension degree는 $\Hom_{\Alg{\mathbb{K}}} (A, \mathbb{L})$의 갯수와 같으며, 이 증명을 찬찬히 뜯어보면 이를 통해 우리가 계산하는 것은 사실상 $A$를 diagonalize하는 $\mathbb{L}/\mathbb{K}$에 대하여 $[A_{(\mathbb{L})}:\mathbb{L}]$를 계산하는 것임을 알 수 있다. 이러한 관점에서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $\mathbb{K}$-algebra $A$에 대하여, 다음이 모두 동치이다. 

1. $A$는 étale이다.  
2. $A$를 diagonalize하는 fintite degree extension이 존재한다.  
3. $\overline{\mathbb{K}}/\mathbb{K}$가 $A$를 diagonalize한다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>  

우선 첫째 조건을 가정하고, $n=[A:\mathbb{K}]$라 하고 $\mathbb{L}/\mathbb{K}$가 $A$를 diagonalize한다 가정하자. 그럼 [따름정리 7](#cor7)에 의해 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$의 크기가 $n$이다. 한편 임의의 $u\in \Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$에 대하여 $[u(A):\mathbb{K}]\leq n$임이 자명하고, 따라서 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$의 원소들의 image들로 생성된 $\mathbb{L}$의 subextension $\mathbb{L}'$이 $\mathbb{K}$에 대해 finite degree이다. 이제 $A$에서 $\mathbb{L}'$로의 서로 다른 homomorphism들은 $n$개 존재하므로, 다시 [따름정리 7](#cor7)에 의해 $\mathbb{L}'$이 $A$를 diagonalize한다. 

이제 둘째 조건이 셋째 조건을 함의하는 것은 임의의 finite degree extension $\mathbb{L}/\mathbb{K}$는 $\overline{\mathbb{K}}$의 subextension으로 볼 수 있다는 것으로부터 바로 나오고, 셋째 조건이 첫째 조건을 함의하는 것은 그냥 정의이다. 

</details>

다음 명제의 유한성은 étale이라는 이름을 정당화한다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Étale $\mathbb{K}$-algebra $A$에 대하여, $A$는 유한히 많은 subalgebra와 ideal만을 가진다. 뿐만 아니라, $A$를 diagonalize하는 임의의 extension은 $A$의 subalgebra와 quotient algebra 또한 diagonalize하며, 따라서 $A$의 임의의 subalgebra와 quotient algebra는 étale이다. 
</div>

<details class="proof" markdown="1">
<summary>증명</summary>  

$\mathbb{K}^n$이 오직 유한개의 subalgebra와 ideal만을 가지며, 이들의 subalgebra와 quotient algebra가 diagonalizable인 것만 보이면 충분하다. 

$\mathbb{K}^n$의 canonical basis를 $(e_1, \dots, e_n)$이라 하고, $\mathbb{K}^n$의 subalgebra $A$에 대하여 projection map들 $\mathbb{K}^n \rightarrow \mathbb{K}$를 $A$로 restrict한 것들을 $v_1,\ldots, v_n$이라 하자. 그럼 이들의 kernel의 교집합은 $0$이므로, $v_i$들은 ($\mathbb{K}$-벡터공간으로서) $A^\ast$를 생성하며 따라서 $A$는 diagonalizable이다. 

따라서 $A$의 임의의 subalgebra 또한 diagonalizable이므로, 우리는 $A$의 임의의 subalgebra가 주어질 때마다 [명제 6](#prop6)의 둘째 조건을 만족하는 basis를 찾을 수 있어야만 한다. 그런데 $\mathbb{K}^n$의 idempotent들은 정확히 $\\{1,\ldots, n\\}$의 부분집합 $I$에 대하여 $e_I=\sum_{i\in I} e_i$의 꼴로 나타나는 것들 뿐이고, 이들은 $e_Ie_J=e_{I\cap J}$를 만족한다. 즉, 둘째 조건을 만족하는 idempotent들의 쌍은 많아봐야 $\\{1,\ldots, n\\}$의 partition의 개수만큼이고 따라서 $A$의 임의의 subalgebra는 유한히 많다. 

비슷하게, $\mathfrak{a}_I$를 $(e_i)\_{i\in I}$들을 basis로 갖는 $\mathbb{K}$의 부분공간이라 하면 ideal의 유한성을 보일 수 있으며 $\mathbb{K}^n/\mathfrak{a}_I$의 diagonalizability 또한 [명제 6](#prop6)으로 보일 수 있다.

</details>

## 분해가능차수

이제 étale algebra에 대한 성질을 더 살펴보기 전에 유용한 개념을 하나 만들자. 지금까지의 논의들에서 [정리 1](#thm1)에서 처음 등장한 집합 $\Hom_{\Alg{\mathbb{K}}}(A, \mathbb{L})$가 중요한 역할을 해 왔다. 이제 finite degree의 commutative $\mathbb{K}$-algebra $A$를 고정하고, 임의의 extension $\mathbb{L}/\mathbb{K}$이 주어질 때마다 자연수 $h(\mathbb{L})=\lvert \Hom_{\Alg{\mathbb{K}}}(A,\mathbb{L})\rvert$으로 정의하자. 그럼 우리는 부등식

$$h(\mathbb{L})\leq [A:\mathbb{K}]=n$$

이 항상 성립하는 것을 안다. 뿐만 아니라, [명제 8](#prop8)의 셋째 조건을 생각하면, 만일 위의 부등식을 등식으로 만드는 $\mathbb{L}$이 존재한다면 $h(\overline{\mathbb{K}})$ 또한 이를 등식으로 만들어야 함을 안다. 이에 힘입어 우리는 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 자연수 $h(\overline{\mathbb{K}})$를 $A$의 *separable degree<sub>분해가능차수</sub>*로 정의하고 $[A:\mathbb{K}]_s$로 적는다. 

</div>

물론 이것이 잘 정의되기 위해서는 이 값이 $\overline{\mathbb{K}}$의 선택에 의존하지 않아야 한다. 이는 다음 보조정리의 결과이다. 

<div class="proposition" markdown="1">

<ins id="lem11">**보조정리 11**</ins> $\mathbb{K}$의 어떠한 algebraic closure $\Omega$를 고정하자. 그럼 임의의 extension $\mathbb{L}/\mathbb{K}$에 대하여, $h(\mathbb{L})\leq h(\Omega)$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{L}'$을 $\mathbb{L}$ 속에서의 $\mathbb{K}$의 algebraic closure라 하자. 그럼 임의의 homomorphism $u:A \rightarrow \mathbb{L}$에 대하여 

$$[u(A):\mathbb{K}]\leq n$$

이 성립한다. 즉, $u(A)$는 algebraic extension이며 따라서 $\mathbb{L}'$에 포함된다. 이로부터 $h(\mathbb{L}')=h(\mathbb{L})$이 성립해야 함을 안다. 

한편 [§대수적 폐포, ⁋명제 11](/ko/math/field_theory/algebraically_closed_extensions#prop11)에 의하여 $\mathbb{L}'$는 $\Omega$의 적당한 subextension과 isomorpihc하므로

$$h(\mathbb{L})=h(\mathbb{L}')\leq h(\Omega)$$

가 성립한다. 

</details>

이로부터 만일 $\mathbb{L}$이 algebraically closed라면 $\mathbb{L}$과 $\Omega$의 위치를 바꿀 수 있으므로 등식이 성립해야 한다는 것을 알고, 따라서 [정의 10](#def10)이 잘 정의된다. 그럼 다음은 이에 대한 기초적인 성질들이다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 다음이 성립한다. 

1. 임의의 finite degree $\mathbb{K}$-algebra $A,B$에 대하여, $[A\otimes_\mathbb{K}B:\mathbb{K}]_s=[A:\mathbb{K}]_s[B:\mathbb{K}]_s$가 성립한다. 
2. 임의의 extension $\mathbb{K}'/\mathbb{K}$과 $\mathbb{K}$-algebra $A$에 대하여, $[A_{(\mathbb{K}')}:\mathbb{K}']_s=[A:\mathbb{K}]_s$이다. 
3. 임의의 finite degree extension $\mathbb{K}'/\mathbb{K}$와 $\mathbb{K}'$-algebra $A'$에 대하여, $[A':\mathbb{K}]_s=[A':\mathbb{K}']_s[\mathbb{K}':\mathbb{K}]_s$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\mathbb{K}$의 algebraic closure $\mathbb{L}$을 고정하고 이를 사용해 세 집합
    
    $$\Hom_\Alg{\mathbb{K}}(A, \mathbb{L}),\qquad \Hom_\Alg{\mathbb{K}}(B, \mathbb{L}),\qquad \Hom_\Alg{\mathbb{K}}(A\otimes_\mathbb{K}B, \mathbb{L})$$

    을 생각하자. 그럼 주어진 주장은 다음의 함수

    $$\Hom_\Alg{\mathbb{K}}(A,\mathbb{L})\times \Hom_\Alg{\mathbb{K}}(B, \mathbb{L}) \rightarrow \Hom_\Alg{\mathbb{K}}(A\otimes_\mathbb{K}B,\mathbb{L}); (u,v)\mapsto u\otimes v$$

    이 bijection인 것으로부터 자명하다. 
2. $\mathbb{L}$을 $\mathbb{K}'$의 algebraic closure라고 하자. 그러면 다음의 morphism
    
    $$\bar{u}(x) = u(1 \otimes x) \quad (x \in A)$$
    
    은 $\mathbb{K}'$-algebra homomorphism $u$의 집합과 $\mathbb{K}$-algebra homomorphism $\bar{u}$의 집합 사이의 bijection을 정의한다. 그러므로 등식이 성립한다.
3. 마찬가지로 $\mathbb{L}$을 $\mathbb{K}'$의 algebraic closure라고 하자. 두 집합 $\Hom_{\Alg{\mathbb{K}}}(\mathbb{K}', \mathbb{L})$, $\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})$을 생각하자. 이제 각각의 $u\in\Hom_{\Alg{\mathbb{K}}}(\mathbb{K}', \mathbb{L})$마다 다음의 집합
    
    $$\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})_u=\left\{v\in \Hom_{\Alg{\mathbb{K}}}(A', \mathbb{L})\mid\text{$v(x.1)=u(x)$ for all $x\in \mathbb{K}'$}\right\}$$

    을 생각하면 이들은 다음의 partition 

    $$\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})=\bigsqcup_{u\in \Hom_\Alg{\mathbb{K}}(\mathbb{K}', \mathbb{L})} \Hom_\Alg{\mathbb{K}}(A', \mathbb{L})_u$$

    을 유도한다. 한편 각각의 고정된 $u$에 대하여, 위의 집합 $\Hom_\Alg{\mathbb{K}}(A', \mathbb{L})_u$는, $\mathbb{L}$이 $\mathbb{K}'$의 algebraic closure이므로, 그 정의에 의하여 $[A':\mathbb{K}']$와 같은 크기를 갖는다. 이로부터 원하는 등식을 얻는다. 

</details>

이 언어를 사용하면 [따름정리 7](#cor7)은 다음과 같이 번역된다. 

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Finite degree commutative $\mathbb{K}$-algebra $A$에 대하여, $[A:\mathbb{K}]_s\leq [A:\mathbb{K}]$가 성립하며, 등식은 $A$가 étale algebra일 경우 성립한다. 

</div>

특히 이를 [명제 12](#prop12)와 조합하면 다음의 따름정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor14">**따름정리 14**</ins> 다음이 성립한다. 

1. 임의의 두 commutative $\mathbb{K}$-algebra $A,B$에 대하여, $A\otimes_\mathbb{K}B$가 étale인 것과 이들 각각이 étale인 것이 동치이다. 
2. 임의의 extension $\mathbb{K}'/\mathbb{K}$에 대하여, $\mathbb{K}$-algebra $A$가 étale인 것과 $A_{(\mathbb{K}')}$가 étale인 것이 동치이다. 
3. 임의의 extension $\mathbb{K}'/\mathbb{K}$, $\mathbb{K}'$-algebra $A'$에 대하여, $A'$가 $\mathbb{K}$에 대해 étale인 것은 $A'$가 $\mathbb{K}'$에 대해 étale이고 $\mathbb{K}'$가 $\mathbb{K}$에 대해 étale인 것과 동치이다. 

</div>

