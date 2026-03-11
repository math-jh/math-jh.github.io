---

title: "사교벡터공간"
excerpt: "Symplectic form의 정의"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/linear_symplectic_geometry
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/Linear_symplectic_geometry.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-04-28
last_modified_at: 2023-04-28
weight: 2

---

물리에서 momentum은 covector로 취급되기 때문에, 수학적으로 phase space를 기술할 때에는 manifold $M$의 cotangent bundle $T^\ast M$을 생각하는 것이 자연스럽다. 

물리적인 이유가 아니더라도 symplectic manifold를 기술할 때에는 tangent bundle $TM$보다 $T^\ast M$이 훨씬 자연스러운데, 이는 $T^\ast M$은 자연스러운 symplectic form을 갖기 때문이다. Symplectic form이 무엇인지를 살펴보기 전에 우리는 먼저 선형대수 세팅에서 사교기하를 먼저 살펴본다.

## Symplectic form

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 벡터공간 $(V,\omega)$가 *symplectic vector space*라는 것은 $\omega:V\times V\rightarrow \mathbb{R}$이 다음 두 조건을 만족하는 것이다.

- (Skew-symmetry) 임의의 $v,w\in V$에 대하여, $\omega(v,w)=-\omega(w,v)$이다.
- (Nondegeneracy) $\omega(v,w)=0$이 모든 $w\in V$에 대해 성립하도록 하는 $v$는 오직 $v=0$ 뿐이다.

이 때, $\omega$를 *symplectic form*이라 부른다.

</div>

어렵지 않게 모든 symplectic vector space는 반드시 짝수차원이어야 한다는 사실을 알 수 있다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 임의의 skew-symmetric bilinear map $\omega:V\times V\rightarrow \mathbb{R}$가 주어졌다 하자. 그럼 $V$의 basis $u_1,\ldots, u_k, e_1, \ldots,e_n,f_1,\ldots, f_n$이 존재하여 다음 조건이 모두 만족되도록 할 수 있다.

- 모든 $v\in V$에 대하여, $\omega(u_i,v)=0$이 성립한다.
- 모든 $i,j$에 대하여, $\omega(e_i,e_j)=\omega(f_i,f_j)=0$이 성립한다.
- 모든 $i,j$에 대하여, $\omega(e_i,f_j)=\delta_{ij}$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 다음 집합

$$\{u\in V: \omega(u,v)=0\text{ for all $v\in V$}\}$$

이 $V$의 부분공간이 된다는 것을 쉽게 확인할 수 있다. 따라서 이 부분공간의 basis를 택하면 $u_1,\ldots, u_k$를 얻는다. 이제 $V=U\oplus W$라 하자. 그럼 $W$의 basis $e_1,\ldots, e_n,f_1,\ldots, f_n$을 다음과 같이 찾을 수 있다. 

임의의 벡터 $e_1\in W$를 하나 택하자. 그럼 $\omega$는 $W$ 위에서 non-degenerate이므로, $\omega(e_1,f_1)\neq 0$을 만족하는 $f_1\in W$이 존재하며, 필요한만큼 상수배를 하여 $\omega(e_1,f_1)=1$이라 가정할 수 있다. $\omega$가 skew-symmetric이므로 $\omega(e_1,e_1)=\omega(f_1,f_1)=0$임은 자명하다.

이와 같은 과정을 반복하여, 다음 두 조건

- 모든 $i,j$에 대하여, $\omega(e_i,e_j)=\omega(f_i,f_j)=0$이 성립한다.
- 모든 $i,j$에 대하여, $\omega(e_i,f_j)=\delta_{ij}$이 성립한다.

을 만족하는 벡터 $e_1,\ldots, e_k, f_1,\ldots, f_k\in W$가 주어졌다 하고, $\span\\{e_1,\ldots, e_k,f_1,\ldots, f_k\\}\leq W$에 속하지 않는 임의의 벡터 $e_{k+1}$를 하나 택하자. 만일 임의의 $i=1,\ldots, k$에 대하여

$$\omega(e_{k+1}, e_i)=\lambda_i,\qquad\omega(e_{k+1},f_i)=\eta_i$$

라면, $e_{k+1}$ 대신 다음 벡터

$$e_{k+1}-\sum_{i=1}^k(\lambda_i f_i+\eta_i e_i)$$

을 생각하여 $e_{k+1}$가 다음 조건들

$$\omega(e_{k+1},e_i)=\omega(e_{k+1},f_i)=0\qquad\text{for all $i=1,\ldots, k$}$$

을 만족하는 벡터였다고 가정할 수 있다. 한편 $W$에서 $\omega$는 non-degenerate이므로 $\omega(e_{k+1},f_{k+1})\neq 0$을 만족하는 벡터 $f_{k+1}\in W$가 존재한다. 마찬가지로 $f_{k+1}$가 

$$\omega(f_{k+1}, e_i)=\lambda_i',\qquad\omega(f_{k+1},f_i)=\eta_i'$$

을 만족한다면, $f_{k+1}$ 대신 다음 벡터

$$f_{k+1}-\sum_{i=1}^k(\lambda_i' f_i+\eta_i' e_i)$$

을 생각하여 $f_{k+1}$가 다음 조건들

$$\omega(f_{k+1},e_i)=\omega(f_{k+1},f_i)=0\qquad\text{for all $i=1,\ldots, k$}$$

을 만족한다고 할 수 있고, 이후 적절한 상수배를 통해 $\omega(e_{k+1},f_{k+1})=1$이라 가정할 수 있다. 

</details>

위의 보조정리에서 부분공간 $U=\span\\{u_1,\ldots, u_k\\}$은 $\omega$가 항등적으로 영인 공간이며, 따라서 이 부분공간의 complement $W$에서 $\omega$는 symplectic form이 된다. 거꾸로 임의의 벡터공간에 symplectic form이 주어졌다면, $\omega$가 non-degenerate인 것으로부터 $U=0$이어야 하므로 임의의 symplectic vector space는 반드시 짝수차원이어야 한다. 이 때, 위의 보조정리에서 얻어지는 basis

$$e_1,\ldots, e_n, f_1,\ldots, f_n$$

을 *symplectic basis*라 부른다. Symplectic form을 보존하는 linear map을 *(linear) symplectomorphism*이라 부른다면, symplectic basis의 선택에 의하여 임의의 symplectic vector space는 이전 글에서 살펴본 공간 $(\mathbb{R}^{2n},\omega_0)$과 symplectomorphic하다는 것을 확인할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $(V,\omega)$가 symplectic vector space라 하고, $W\leq V$가 임의의 부분공간이라 하자. 그럼 $W$의 *symplectic complement*는

$$W^\omega=\{v\in V:\omega(v,w)=0\text{ for all $w\in W$}\}$$

으로 정의된 공간이다. 

1. 만일 $W\subseteq W^\omega$이 성립한다면, $W$를 *isotropic subspace*라 부른다.
2. 만일 $W^\omega\subseteq W$이 성립한다면, $W$를 *coisotropic subspace*라 부른다.
3. 만일 $W\cap W^\omega=\\{0\\}$이 성립한다면, $W$를 *symplectic subspace*라 부른다.
4. 만일 $W=W^\omega$이 성립한다면, $W$를 *Lagrangian subspace*라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Symplectic vector space $(V,\omega)$와 그 부분공간 $W$에 대하여, 다음이 성립한다.

1. $\dim W+\dim W^\omega=\dim V$이고, $(W^\omega)^\omega=W$이 성립한다.
2. $W$가 symplectic subspace인 것은 $W^\omega$가 sympelctic subspace인 것과 동치이다.
3. $W$가 isotropic인 것은 $W^\omega$가 coisotropic인 것과 동치이다. 또, $W$가 coisotropic인 것은 $W^\omega$가 isotropic인 것과 동치이다.
4. $W$가 Lagrangian인 것은 $W$가 isotropic이고 $\dim W=\frac{1}{2}\dim V$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $\omega$는 non-degenerate pairing이므로, $v\mapsto \omega(v,-)$는 $V$에서 $V^\ast$로의 isomorphism을 정의한다. ([\[선형대수학\], §쌍대공간, ⁋명제 4](/ko/math/linear_algebra/dual_space#prop4)) 
    
    $W$의 annihilator를 $W^\perp\subseteq V^\ast$라 하자. ([\[선형대수학\], §쌍대공간, ⁋정의 7](/ko/math/linear_algebra/dual_space#def7)) 임의의 $u\in W^\omega$에 대하여
    
    $$\omega(u,w)=0\qquad\text{for all $w\in W$}$$
    
    가 성립하고, 따라서 $\omega(u,-)$는 항상 $W^\perp$에 속한다. 거꾸로 임의의 $\varphi\in V^\ast$가 주어질 때마다 유일한 $u\in V$가 존재하여 $\varphi=\omega(u,-)$이라 할 수 있는데, 만일 $\varphi\in W^\perp$였다면 
    
    $$0=\varphi(w)=\omega(u,w)\qquad\text{for all $w\in W$}$$
    
    이 성립하므로 $u\in W^\omega$이다. 즉, 위의 isomorphism을 통해 우리는 두 공간 $W^\perp$와 $W^\omega$가 isomorphic하다는. 것을 안다. 이제 1번의 첫 등식은

    $$\dim V=\dim W+\dim W^\perp=\dim W+\dim W^\omega$$

    으로부터 자명하고, 등식 $(W^\omega)^\omega=W$는 $W\subseteq(W^\omega)^\omega$가 성립하고, 첫 등식에 의해 $\dim (W^\omega)^\omega=\dim W$여야 하므로 얻어진다.

2. $(W^\omega)^\omega=W$이므로 $W\cap W^\omega=(W^\omega)^\omega\cap W^\omega$가 성립한다.
3. 만일 $W\subseteq W^\omega$라면 $(W^\omega)^\omega\subseteq W^\omega$이므로 $W^\omega$는 coisotropic이다.
4. $W$가 Lagrangian이라면 $W=W^\omega$이므로 $\dim W+\dim W^\omega$로부터 $\dim W=\frac{1}{2}\dim V$이고 $W$는 isotropic subspace이다. 거꾸로 만일 $\dim W=\frac{1}{2}\dim V$라면 $\dim W^\omega$ 또한 $\frac{1}{2}\dim V$이므로, 이러한 차원 조건을 만족하는 isotropic subspace는 Lagrangian이다.

</details>

## Symplectic quotient

한편, $\mathbb{R}$-벡터공간 $V$와 임의의 부분공간 $W$에 대하여, quotient space $V/W$는 항상 잘 정의된다. 그리나 $V$가 symplectic vector space였다 하더라도 일반적으로 $V/W$가 symplectic vector space의 구조를 가질 필요는 없다. 가령 $W$가 홀수차원 부분공간이었다면 $V/W$ 또한 홀수차원이 되므로, 당연히 symplectic vector space의 구조를 가질 수 없다. 

$W$가 짝수차원 부분공간이어도 이는 마찬가지인데, 우리는 quotient space $V/W$에

$$\overline{\omega}([v_1],[v_2])=\omega(v_1,v_2)$$

을 통해 symplectic form을 정의하려는 시도를 할 수 있지만, 이것이 잘 정의되려면 다음 식

$$\omega(v_1+w_1,v_2+w_2)=\omega(v_1,v_2)+\omega(v_1,w_2)+\omega(w_1,v_2)+\omega(w_1,w_2)$$

의 값이 $\omega(v_1,v_2)$와 동일해야 한다. $W$에 어떠한 조건도 걸려있지 않다면, 우변의 뒤쪽 세 항이 $0$이 될 이유는 없으므로 $V/W$에 symplectic form은 일반적으로 잘 정의되지 않는다. 뿐만 아니라, $W$가 symplectic subspace였다 해도 우변의 마지막 항인 $\omega(w_1,w_2)$만 사라지므로 여전히 조건이 부족하다.

이를 잘 작동하게 하기 위해서는 다음과 같은 방식으로 quotient space를 정의해주면 된다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $(V,\omega)$가 symplectic vector space이고, $W$가 coisotropic subspace라 하자. 그럼 $W/W^\omega$ 위에 유일한 symplectic structure $\overline{\omega}$가 존재하여, projection $W\rightarrow W/W^\omega$에 의한 $\overline{\omega}$의 pullback과, $\omega$의 $W$로의 restriction이 동일하도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $[w_1],[w_2]\in W$에 대해 $\overline{\omega}([w_1],[w_2])=\omega(w_1,w_2)$으로 정의하자. 이 식이 잘 정의된 symplectic form을 주기만 한다면 원하는 성질이 성립한다는 것은 자명하다. 우선 임의의 $u_1,u_2\in W^\omega$에 대하여,

$$\omega(w_1+u_1,w_2+u_2)=\omega(w_1,w_2)+\omega(w_1,u_2)+\omega(u_1,w_2)+\omega(u_1,u_2)$$

가 성립하며, $w_1,w_2,u_1,u_2$는 모두 $W$의 원소이고 $u_1,u_2$는 $W^\omega$의 원소이므로 우변의 뒤쪽 세 항이 모두 0이 된다. 따라서 $\overline{\omega}$는 잘 정의된다. $\overline{\omega}$가 skew-symmetric인 것은 정의에 의해 자명하므로, $\overline{\omega}$가 non-degenerate인 것만 보이면 충분하다. 만일 $[w]\in W$가 모든 $[w']\in W$에 대해 $\overline{\omega}([w],[w'])=0$을 만족한다면,

$$0=\overline{\omega}([w],[w'])=\omega(w,w')\qquad\text{for all $w'\in W$}$$

이므로 정의에 의해 $w\in W^\omega$이고 따라서 $[w]=0$이다. 즉 $\overline{\omega}$는 non-degenerate이다.

</details>

Symplectic vector space의 모든 1차원 부분공간은 isotropic subspace이므로, [보조정리 4](#lem4)에 의하여 모든 codimension 1의 부분공간 $W$는 coisotropic subspace이다. 이 공간에 [보조정리 5](#lem5)를 적용하면 우리는 원래의 벡터공간에서 2차원이 줄어든 새로운 symplectic vector space를 얻게 된다.