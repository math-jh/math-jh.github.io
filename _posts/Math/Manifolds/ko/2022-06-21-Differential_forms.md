---

title: "미분형식"
excerpt: "Differential form"

categories: [Math / Manifold]
permalink: /ko/math/manifold/differential_forms
header:
    overlay_image: /assets/images/Manifold/Differential_forms.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-21
last_modified_at: 2022-06-21
weight: 13

---

## 벡터다발들

우리는 앞선 글에서 exterior algebra를 정의했는데, 이를 바탕으로 미분형식을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Manifold $M$에 대하여, 

$$T^{r,s}(M)=\bigsqcup_{p\in M} T^{r,s}(T_pM),\quad \bigwedge\nolimits^\ast(M)=\bigsqcup_{p\in M}\bigwedge(T_p^\ast M),\quad \bigwedge\nolimits^k(M)=\bigsqcup_{p\in M}\bigwedge\nolimits^k(T_p^\ast M)$$

를 각각 $M$ 위에서의 *$(r,s)$-tensor bundle*, *exterior algebra bundle*, *exterior $k$-bundle*이라 부른다.

</div>

위의 세 집합들이 실제로 vector bundle이 된다는 것은 어렵지 않다. $M$의 coordinate chart $(U,\varphi)$, $\varphi=(x^i)_{i=1}^m$이 주어진다면, 가령 $T^{r,s}(M)$의 경우는 다음의 원소들

$$\frac{\partial}{\partial x^{i_1}}\otimes\cdots\otimes\frac{\partial}{\partial x^{i_r}}\otimes dx^{j_1}\otimes\cdots\otimes dx^{j_s}$$

이 $p\in U$에서 $T^{r,s}(T_pM)$의 basis가 될 것이며, 따라서 $\tilde{\varphi}:\pi^{-1}(U)\rightarrow\mathbb{R}^m\otimes\mathbb{R}^{m^{r+s}}$를 앞의 $m$개의 성분에는 $\varphi$를 따라 기준점 $p$의 좌표를 넣고, 나중의 $m^{r+s}$개의 성분에는 $\alpha\in T^{r,s}(T_pM)$을 위의 basis들로 표현했을 때 계수로 등장하는 $m^{r+s}$개의 성분을 넣어주면 된다. 

비슷하게, $\bigwedge\nolimits^{k}(M)$의 경우, $\bigwedge\nolimits^k(T^\ast_pM)$의 basis는 

$$dx^{i_1}\wedge\cdots dx^{i_k}\qquad(i_1 < i_2 < \cdots < i_k)$$

들이고, $\bigwedge\nolimits^\ast(M)$의 경우는 모든 $k$에 대하여 위의 형태의 원소들을 모아둔 집합이 각 점에서의 basis가 될 것이다.

나머지 증명은 tangent bundle이 vector bundle이 된다는 증명과 동일하다. ([§벡터다발, 예시 2](/ko/math/manifold/vector_bundles#ex2))

위에서 정의한 세 vector bundle의 $C^\infty$ section들을 각각 *tensor field*, *differential form*, *differential $k$-form*이라 부른다. <#ref#>에 의하여, 어떤 section $\sigma$가 $C^\infty$라는 것은 $\sigma$를 위에서 정의한 basis를 이용해 표현했을 때, 그 계수가 모두 $C^\infty$ 함수라는 것이다.

## 미분형식

$M$에서 정의된 모든 differential $k$-form들의 집합을 $\Omega^k(M)$으로 적고, $M$에서 정의된 모든 differential form들의 집합을 $\Omega^\ast(M)$으로 적는다. 

임의의 두 $k$-form $\omega$, $\eta$가 주어졌다 하면, $\omega+\eta$를 다음의 식

$$(\omega+\eta)_p=\omega_p+\eta_p$$

로 정의할 수 있다. 이와 비슷하게 임의의 $k$-form에 상수배를 곱할 수도 있으므로, $\Omega^k(M)$은 $\mathbb{R}$-벡터공간을 이룬다.

한편 $\Omega^\ast(M)$의 임의의 두 원소 사이에는 잘 정의된 곱셈 $\wedge$가 존재한다. 예컨대 임의의 $\omega\in\Omega^k(M)$, $\eta\in\Omega^l(M)$이 주어졌다면

$$(\omega\wedge\eta)_p=\omega_p\wedge\eta_p\tag{1}$$

으로 정의하면 된다. 그럼 정의에 의해 $\bigwedge\nolimits^0(T_p^\ast M)=\mathbb{R}$이므로, differential $0$-form은 별다른 것이 아니라 단순히 $C^\infty(M)$가 된다. 즉, 임의의 $\Omega^k(M)$의 원소에 $f\in C^\infty(M)$을 곱하여도 그 결과는 $\Omega^k(M)$에 속하며, 따라서 각각의 $\Omega^k(M)$은 $C^\infty(M)$-module로 취급할 수도 있다. 

이제 $\Omega^\ast(M)$은 $\Omega^k(M)$들의 direct sum이므로 $\mathbb{R}$-벡터공간이자 $C^\infty(M)$-module이 되며, 뿐만 아니라 위의 식 (1)을 통해 $\mathbb{N}$으로 gradation이 주어진 $\mathbb{R}$-algebra이자 $C^\infty(M)$-algebra로 생각할 수 있다.

임의의 $\omega\in\Omega^k(M)$이 주어졌다 하자. 그럼 각 점 $p\in M$에서, $\omega_p$는 isomorphism $\bigwedge\nolimits^k(T^\ast_pM)\cong A^k(T_pM)$을 통하여 $T_pM$ 위에서 정의된 alternating multilinear map $(T_pM)^k\rightarrow\mathbb{R}$로 취급할 수 있다. 따라서 $k$개의 vector field $X_1,\ldots, X_k$가 주어졌을 때, 함수 $\omega(X_1,\ldots, X_k):M\rightarrow\mathbb{R}$을 다음의 식

$$\omega(X_1,\ldots, X_k)(p)=\omega_p\bigl((X_1)_p,\ldots, (X_k)_p\bigr)$$

으로 정의해주면 된다. 따라서, $\omega$는 $C^\infty(M)$-module $\mathfrak{X}(M)$ 위에서 정의된 alternating $C^\infty(M)$-multilinear map $(\mathfrak{X}(M))^k\rightarrow C^\infty(M)$으로 생각할 수 있다. 거꾸로 임의로 주어진 alternating $C^\infty(M)$-multilinear map $\mathfrak{X}(M)^k\rightarrow C^\infty(M)$도 $k$-form을 정의한다. **[War]**에서는 이를 한 페이지를 할애하여 설명하고 있는데, 우리는 사실로 받아들이고 넘어간다.

이와 비슷하게, 임의의 vector field $X$에 대하여 $X\mathbin{\lrcorner}\omega$ 또한 다음의 식

$$(X\mathbin{\lrcorner}\omega)_p=X_p\mathbin{\lrcorner}\omega_p$$

으로 정의할 수 있으며, 이 때 $X\mathbin{\lrcorner}-$가 degree $-1$의 anti-derivation이 된다는 것이 [§외대수, 명제 8](/ko/math/manifold/exterior_algebra#pp8)로부터 명백하다.

## 외미분

우리는 [§미분사상의 예시들, 정의 6](/ko/math/manifold/examples_of_differentials#df6)에서 cotangent space를 소개하며, 그 motivation을 임의의 $f\in C^\infty(M)$마다 정의되는 differential $df_p:T_pM\rightarrow T_{f(p)}\mathbb{R}$에서 찾았다. 이제 $df$를 각 점 $p\in M$에 $df_p\in T_p^\ast M$을 대응시키는 함수로 생각하면, $df$는 각 점 $p$마다 $\bigwedge\nolimits^1(M)=T_p^\ast M$의 원소를 대응시키는 함수, 곧 $1$-form $M\rightarrow\bigwedge\nolimits^1(M)$으로 생각할 수 있다. 

우리는 $1$-form $df$를 $0$-form $f$의 *exterior derivative<sub>외미분</sub>*이라 부르고, $d:\Omega^0(M)\rightarrow\Omega^1(M)$을 *exterior differentiation operator*라 부른다. 다음과 같이 $d$가 $\Omega^\ast(M)\rightarrow\Omega^\ast(M)$으로 확장된다는 사실이 잘 알려져 있다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Manifold $M$에 대하여, 유일한 anti-derivation $d:\Omega^\ast(M)\rightarrow\Omega^\ast(M)$이 존재하여, $d$는 degree $1$이고 다음의 두 조건

1. $d^2=0$,
2. 임의의 $f\in\Omega^0(M)$에 대하여, $df$는 위와 같이 $f$의 differential과 동일하다.

을 만족한다.

</div>

$C^\infty$ 함수 $F:M\rightarrow N$이 주어졌다 하자. 그럼 linear map $dF_p:T_pM\rightarrow T_{F(p)}N$가 잘 정의된다. 앞서 [§외대수, Duality](/ko/math/manifold/exterior_algebra#duality)의 말미에서 한 것과 마찬가지로, linear map $dF_p$를 이용하여 $\bigwedge(T_{F(p)}^\ast N)$에서 $\bigwedge(T_pM)$으로의 linear map $F^\ast_p$을 얻는다. 이제 $F^\ast:\Omega^\ast(N)\rightarrow\Omega^\ast(M)$을 각 점 $p$마다 이 linear map을 대응시켜 얻은 함수로 정의하자. 즉 임의의 $\omega\in\Omega^\ast(N)$에 대하여

$$(F^\ast\omega)_p=F^\ast_p\omega_{F(p)}$$

이다. 한편, $F^\ast\omega$는 $k$-form으로서 각 vector field $X_1,\ldots, X_k\in\mathfrak{X}(M)$이 주어졌을 때의 값

$$(F^\ast\omega)(X_1,\ldots, X_k)\in C^\infty(M)$$

으로 결정되는데, 이는 위의 정의를 직접 대입하면 임의의 점 $p\in M$에 대하여,

$$(F^\ast\omega)(X_1,\ldots, X_k)(p)=(F^\ast_p\omega_{F(p)})\bigl((X_1)_p,\ldots, (X_k)_p\bigr)=\omega_{F(p)}\bigl(dF_p((X_1)_p), \ldots, dF_p((X_k)_p)\bigr)$$

임을 알 수 있다. 뿐만 아니라, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 위에서 정의한 $F^\ast:\Omega^\ast(N)\rightarrow\Omega^\ast(M)$은 $\wedge$를 보존하고, 따라서 algebra homomorphism이 된다. 뿐만 아니라, $F^\ast$는 exterior differential operator $d$와 commute한다. 즉 임의의 form $\omega\in\Omega^\ast(N)$에 대하여 다음의 식

$$d(F^\ast\omega)=F^\ast(\omega)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## Lie derivative, revisited

우리는 앞서 vector field를 정의한 후, Lie derivative를 통해 vector field의 미분에 해당하는 연산 $\mathscr{L}_XY$을 정의했다. 이는 주어진 vector field $X$에 대하여, diffeomorphism $X_t$를 통해 vector field $Y$의 각 점들에서의 값을 <em_ko>옮길</em_ko> 수 있다는 것을 이용했다. 

이와 비슷하게 우리는 differential form $\omega$ 또한 vector field $X$에 대해 미분할 수 있다. 단지 그 당시에는 tangent vector들을 옮겨야 하므로 $dX_t$를 사용했지만, 이제는 form을 옮기기 위해 위에서 정의한 $X_t^\ast$를 사용한다는 점만 다르다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 임의의 $X\in\mathfrak{X}(M)$과 $\omega\in\Omega^\ast(M)$에 대하여, $\mathscr{L}_X\omega$는 각 점 $p$마다 다음의 식

$$(\mathscr{L}_X\omega)_p=\frac{d}{dt}\bigg|_{t=0}X_t^\ast\omega_{X_t(p)}=\lim_{t\rightarrow 0}\frac{X_t^\ast\omega_{X_t(p)}-\omega_p}{t}$$

으로 정의된 form이다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 임의의 $X\in\mathfrak{X}(M)$에 대해 다음이 성립한다.

1. 임의의 $f\in C^\infty(M)$에 대하여 $\mathscr{L}_Xf=X(f)$.
2. 임의의 $Y\in \mathfrak{X}(M)$에 대하여 $\mathscr{L}_XY=[X,Y]$.
3. $\mathscr{L}_X$는 $\Omega^\ast(M)$에서 $\Omega^\ast(M)$으로의 derivation이며, $d$와 commute한다.
4. $\mathscr{L}_X=\iota_X\circ d+d\circ\iota_X$.
5. 임의의 $\omega\in\Omega^k(M)$과 $X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$에 대하여
    
    $$\mathscr{L}_{X_0}(\omega(X_1,\ldots, X_k))=(\mathscr{L}_{X_0}\omega)(X_1,\ldots, X_k)+\sum_{i=1}^k\omega(X_1,\ldots, X_{i-1}, \mathscr{L}_{X_0}X_i,X_{i+1},\ldots, X_k)$$

6. 임의의 $\omega\in\Omega^k(M)$과 $X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$에 대하여

    $$\begin{aligned}d\omega(X_0,\ldots, X_k)&=\sum_{i=0}^k(-1)^iX_i\omega(X_0,\ldots, \hat{X}_i,\ldots, X_k)\\&\phantom{==}+\sum_{i<j}(-1)^{i+j}\omega([X_i, X_j], X_0,\ldots, \hat{X}_i,\ldots, \hat{X}_j,\ldots, X_k)\end{aligned}$$

5번과 6번에서, hat은 주어진 성분이 생략되었음을 의미한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---