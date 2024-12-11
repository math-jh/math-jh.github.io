---

title: "선다발"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/line_bundles
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Line_bundles.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-12-04
last_modified_at: 2024-12-04
weight: 101

---

## 피카르드 군

앞선 글에서 우리는 vector bundle의 일반화로서 scheme $X$ 위에 정의된 (quasi-)coherent sheaf에 대해 다루었다. 이번 글에서는 특히 rank $1$의 locally free sheaf들, 즉 line bundle에 대해 대해 살펴본다. 

앞서 [§준연접가군층, ⁋정의 1](/ko/math/algebraic_geometry/quasicoherent_sheaves#def1)에서 살펴본 내용에 따르면, 임의의 rank $1$ locally free sheaf $\mathscr{L}$에 대하여 

$$\mathscr{L}^\vee=\mathscr{H}om(\mathscr{L},\mathscr{O}_X)$$

는 locally free sheaf of rank $1$이 되며, 뿐만 아니라 trace map $\mathscr{L}\otimes \mathscr{L}^\vee\cong \mathscr{O}_X$가 존재하므로, $\mathscr{L}^{-1}=\mathscr{L}^\vee$로 정의하면 locally free sheaf of rank $1$들이 group을 이루는 것을 알 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$ 위에 정의된 locally free sheaf of rank $1$들을 *invertible sheaf*라 부른다. 이들이 위의 연산 $\otimes$와 역원 $\vee$를 통해 이루는 group을 *Picard group*이라 부르고 $\Pic(X)$로 적는다. 

</div>

그럼 고정된 invertible sheaf $\mathscr{L}$과 임의의 $n$에 대하여

$$\mathscr{L}^{\otimes n}=\mathscr{L}\otimes\cdots\otimes \mathscr{L}$$

그리고

$$\mathscr{L}^{-\otimes n}:=(\mathscr{L}^\vee)^{\otimes n}$$

으로 정의하면 group homomorphism $\mathbb{Z}\rightarrow\Pic(X)$를 얻는다. 

이제 예시로 이 과정을 살펴보자.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 가장 간단한 예시로, $\mathbb{P}^1\_\mathbb{k}=\Proj \mathbb{k}[\x\_0,\x\_1]$ 위에 정의된 invertible sheaf들을 살펴보자. 이들을 정의하기 위해서는 $\mathbb{P}^1\_\mathbb{k}$의 두 open set

$$U_0=\Spec \mathbb{k}[\x_{1/0}],\quad U_1=\Spec \mathbb{k}[\x_{0/1}]$$

위에서의 section $\mathscr{L}(U\_0), \mathscr{L}(U\_1)$과, $U_0\cap U_1$에서 이들 section들이 어떻게 연결되는지를 살펴보면 된다. $U_0,U_1$ 위에 정의된 trivial bundle (즉 $U_0,U_1$의 structure sheaf들)들을 생각하자. 각각의 affine open set에서의 이들 trivial bundle의 global section들은 각각 $\mathbb{k}[\x_{1/0}]$과 $\mathbb{k}[\x_{0/1}]$의 원소들이다. 

[§스킴, ⁋예시 4](/ko/math/algebraic_geometry/schemes#ex4)에서 우리는 $U_0\cap U_1$에서 $\x_{0/1}=\x_{1/0}^{-1}$을 통해 두 trivial bundle들을 붙여줄 경우, 그렇게 얻어지는 locally free sheaf $\mathscr{O}\_{\mathbb{P}^1}$의 global section은 $\mathbb{k}$가 된다는 것을 살펴보았다. 이 때 transition function은 $\mathbb{k}[\x_{0/1}]$과 $\mathbb{k}[\x_{1/0}]$의 basis $\x_{0/1}$, $\x_{1/0}$만 서로 바꿔주고, 다른 것은 아무것도 하지 않는 것이다. 이제 $\mathbb{P}^1$ 위에 정의된 locally free sheaf $\mathscr{O}(1)=\mathscr{O}\_{\mathbb{P}^1\_\mathbb{k}}(1)$을 새로운 transition function을 사용하여 정의하자. 이 transition function은 $\mathbb{k}[\x_{1/0}]$에서 $\mathbb{k}[\x_{0/1}]$로 넘어갈 때는 $\x_{0/1}=\x_{1/0}^{-1}$을 곱해주고, 반대로 $\mathbb{k}[\x_{0/1}]$에서 $\mathbb{k}[\x_{1/0}]$으로 넘어갈 때는 $\x_{1/0}=\x_{0/1}^{-1}$을 곱해주는 것이다. 

그럼 이렇게 정의된 $\mathscr{O}(1)$의 global section은 $\mathbb{k}[\x_{1/0}]$에서는 다항식 $f(\x_{1/0})$, $\mathbb{k}[\x_{0/1}]$에서는 다항식 $g(\x_{0/1})$로 주어지며, transition function의 정의에 의하여 이들은 다음 조건

$$f(\x_{1/0})\x_{0/1}=f(1/\x_{0/1})\x_{0/1}=g(\x_{0/1}),\quad g(\x_{0/1})\x_{1/0}=g(1/\x_{1/0})\x_{1/0}=f(\x_{1/0})$$

을 만족해야 한다. 그럼 $f(1/\x_{0/1})\x_{0/1}$이 $\x_{0/1}$에 대한 다항식이 되기 위해서는 $f$는 일차식이어야 하고, 비슷한 이유로 $g$ 또한 일차식이어야 한다. 뿐만 아니라, $f(\x_{1/0})=a\x_{1/0}+b$라 하면

$$g(\x_{0/1})=\x_{0/1}(a/\x_{0/1}+b)=a+b\x_{0/1}$$

임을 안다. 즉 $\Gamma(\mathbb{P}^1\_\mathbb{k}, \mathscr{O}(1))\cong \mathbb{k}^2$이다. 더 일반적으로 $\mathscr{O}(n)=\mathscr{O}(1)^{\otimes n}$으로 정의하면 이 때의 transition function은 $\mathbb{k}[\x\_{1/0}]$에서 $\mathbb{k}[\x\_{0/1}]$로 넘어갈 때는 $\x\_{0/1}^n=\x\_{1/0}^{-n}$을 곱해주고, 반대로 $\mathbb{k}[\x_{0/1}]$에서 $\mathbb{k}[\x_{1/0}]$으로 넘어갈 때는 $\x_{1/0}^n=\x_{0/1}^{-n}$을 곱해주는 것이다. 그럼 $\Gamma(\mathbb{P}^1_\mathbb{k},\mathscr{O}(n))\cong \mathbb{k}^{n+1}$임을 알 수 있는데, 이는 global section들이 각각의 $U_i$ 위에서 다음 식

$$a_n\x_{0/1}^n+a_{n-1}\x_{0/1}^{n-1}+\cdots a_1\x_{0/1}+a_0,\qquad a_0\x_{1/0}^n+a_{1}\x_{1/0}^{n-1}+\cdots a_{n-1}\x_{1/0}+a_n$$

으로 표현되는 것들이기 때문이다. 

</div>

한편, 위와 같이 유용한 표기법 $\x_{i/j}$를 이용하면 위의 예시의 $\mathscr{O}(n)$의 global section은 다음의 다항식

$$a_n\x_0^n+a_{n-1}\x_0^{n-1}\x_1+\cdots+a_1\x_0\x_1^{n-1}+a_0\x_1^n\in \mathbb{k}[\x_0,\x_1]$$

을 각각의 open set $U_0,U_1$에서 본 것으로 이해할 수도 있다. 그럼 위의 예시를 어렵지 않게 $\mathbb{P}^m_\mathbb{k}$로 일반화할 수 있으며, 특히 $\mathscr{O}\_{\mathbb{P}^m\_\mathbb{k}}(n)$의 global section은 $\mathbb{k}[\x\_0,\ldots, \x\_m]$의 degree $n$ polynomial이고, 따라서 $\Gamma(\mathbb{P}^m_\mathbb{k},\mathscr{O}(n))$의 차원은 $m$개의 변수 중 중복을 허용하여 $n$개를 뽑는 경우의 수, 곧 $\binom{m+n}{n}$이 된다. 

## 인자와 선다발

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme $X$가 *regular in codimension $1$*이라는 것은 dimension 1짜리 local ring $\mathscr{O}_{X,x}$가 항상 regular인 것이다. 

</div>

우리는 이제 Weil divisor를 정의할 것인데, Weil divisor는 앞으로 설명할 조건 ($\ast$)를 만족하는 scheme에서만 잘 정의된다. 따라서, 이번 절에서 다루는 모든 scheme은 다음의 조건을 만족한다고 가정한다. 

> ($\ast$) $X$는 noetherian integral separated scheme이며, regular in codimension $1$이다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Scheme $X$의 closed irreducible subset을 $X$의 *prime divisor<sub>소인자</sub>*라 부른다. 그럼 $X$의 *Weil divisor<sub>베유 인자</sub>*는 prime ideal의 일차결합

$$D=\sum n_iY_i$$

을 의미하며, 따라서 정의에 의해 이 때 $n_i$들은 유한개를 제외하고는 모두 $0$이다. 특별히 $n_i\geq 0$이 모든 $i$에 대해 성립할 경우 $D$를 *effective*라 부른다. $X$의 Weil divisor들의 모임은 $\Div(X)$로 표기한다. $D$의 *support<sub>지지집합</sub>*은 $\bigcup_{n_i\neq 0} Y_i$으로 정의한다. 

</div>

$X$의 prime divisor $Y$를 고정하자. $\eta\in Y$를 $Y$의 generic point라 하면 $\mathscr{O}_{X,\eta}$는 regular local ring of dimension $1$, 즉 discrete valuation ring이 된다. 

한편 임의의 discrete valuation ring $(A,\mathfrak{m})$에 대해 생각해보면, $A$의 임의의 원소는 다음의 꼴

$$u\pi^k\qquad\text{where $u$ is a unit, $\pi$ is a uniformizer, $k\geq 0$}$$

로 쓰일 수 있으며, 이러한 원소에 $k$를 대응시키는 것이 정확히 discrete valuation $\nu$에 해당되었다. 한편 이러한 표현 하에서 discrete valuation ring의 field of fractions를 생각하는 것은 $k$를 모든 정수값을 가질 수 있도록 하는 것과 같으며, 여기에서의 discrete valuation 또한 같은 방식으로 주어진다. 

이제 $\eta$를 포함하는 affine open subset $\Spec A$를 생각하면, 이 local ring의 quotient field $\Frac(\mathscr{O}\_{X,\eta})$는

$$\Frac(\mathscr{O}_{X,\eta})=\Frac(A_\eta)=\Frac(A)$$

이므로 $X$의 function field $K(X)$와 같다. 즉, $\mathscr{O}_{X,\eta}$ 위에 주어진 discrete valuation $\nu_Y$가 위의 방식을 따라 $K(X)$ 위에 discrete valuation을 준다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $X=\Spec \mathbb{C}[\x,\y]$라 하자. 그럼 $K(X)$는 다음의 꼴

$$f(\x,\y)=\frac{g(\x,\y)}{h(\x,\y)},\qquad g,h\in \mathbb{C}[\x,\y],\quad h(x)\not\equiv 0$$

의 원소들을 모아둔 것임을 살펴보았다. 이제 $F(\x,\y)=0$에 의해 정의되는 closed subscheme $Y$, 즉

$$\Spec \mathbb{C}[\x,\y]/F(\x,\y)$$

을 생각하자. $\Spec \mathbb{C}[\x,\y]/F(\x,\y)$의 generic point $(0)$은 $\Spec \mathbb{C}[\x,\y]$에서는 $\eta=(F(\x,\y))$이므로, 여기에서의 local ring은

$$\mathscr{O}_{X,\eta}=\mathbb{C}[\x,\y]_{(F(\x,\y))}$$

즉 다음의 꼴

$$f(\x,\y)=\frac{g(\x,\y)}{h(\x,\y)},\qquad g,h\in \mathbb{C}[\x,\y],\quad F(\x,\y)\nmid h(\x,\y)$$

을 모아둔 것이다. 여기에서의 unit은 추가로 $F(\x,\y)\nmid g(\x,\y)$를 만족하는 $g(\x,\y)/h(\x,\y)$ 꼴의 원소들이며, 따라서 이 local ring의 원소들은 모두

$$f(\x,\y)=u(\x,\y) F(\x,\y)^k,\qquad\text{where $u(\x,\y)=\frac{g(\x,\y)}{h(\x,\y)}$ with $F(\x,\y)\nmid g(\x,\y),h(\x,\y)$ and $k\geq 0$}$$

의 꼴로 쓸 수 있으며, discrete valuation $\nu_Y$는 이 표현에서 지수 $k$를 읽어오는 것이다. 

한편 $\Frac(\mathscr{O}_{X,\eta})$는 [§준연접가군층, ⁋정의 13](/ko/math/algebraic_geometry/quasicoherent_sheaves#def13)에서 살펴본 $X$의 function field $K(X)$와 동일한 것을 알 수 있으며, $\nu_Y$는 이를 통해 $K(X)$ 위에 valuation을 정의한다. 이는 $K(X)$의 원소를 다음의 꼴

$$f(\x,\y)=g(\x,\y)F(\x,\y)^k,\qquad k\in \mathbb{Z}$$

으로 나타내어 얻어진다. 

</div>

더 일반적으로 이제 invertible sheaf $\mathscr{L}$과 $\mathscr{L}$의 nonzero rational section $s$의 pair $(\mathscr{L},s)$가 주어졌다 하자. 그럼 위에서 정의한 $\nu_Y$를 이용해

$$\divisor(s)=\sum\nu_YY$$

으로 정의할 수 있으며, 이는 직관적으로는 [예시 5](#ex5)와 같이 $s$의 zero와 pole이 생기는 irreducible component를 찾아낸 다음, 그 zero와 pole의 multiplicity를 앞에 붙여 만든 linear combination이다. 그럼 $\divisor$는 $(\mathscr{L},s)$들의 모임의 isomorphism class들마다 Weil divisor를 대응시키는 homomorphism이 된다. 즉, 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Noetherian normal scheme $X$에 대하여, $\divisor$는 injective이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\divisor(\mathscr{L},s)=0$이라 하자. 즉 $s$는 pole이 없는 rational section이며, 따라서 $\mathscr{O}_X$에서 $\mathscr{L}$로의 morphism $\times s: \mathscr{O}_X \rightarrow \mathscr{L}$이 정의된다. 이제 이것이 isomorphism인 것을 보이기 위해서는 $\mathscr{L}$의 trivializing open subset $U$에서 살펴보면 충분하다. 그런데 $U$ 위에서의 isomorphism $\mathscr{L}\vert_U \rightarrow \mathscr{O}_U$를 생각하고 이를 $\times s$와 합성하면, 이로부터 얻어지는 rational function이 zero도, pole도 갖지 않는 것을 확인할 수 있다.

</details>

이제 표기의 편의를 위하여 $X$가 irreducible이라 하자. [명제 6](#prop6)의 조건들이 성립한다면 $\divisor$가 injective이므로, $\Div(X)$에서의 $\divisor$의 image를 생각하는 것이 자연스럽다. 이를 위해 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Weil divisor $D\in\Div(X)$에 대하여, $\mathscr{O}_X(D)$를 다음 식

$$\Gamma(U, \mathscr{O}_X(D))=\{t\in K(X)^\times : (\divisor\vert_U)(t)+D\vert_U\geq 0\}\cup\{0\}$$

으로 정의한다.

</div>

이제 transition function은 $K(X)^\times$로부터 오며, 이를 통해 이들을 모두 붙이면 quasi-coherent sheaf $\mathscr{O}_X(D)$를 얻는다. 여기서 $(\divisor\vert_U)(t)$는 $t$를 $U$ 위에서 정의된 rational section으로 본 후 divisor를 생각한 것이다. 따라서 위의 조건은 $D$가 영점을 갖는 divisor에서는 그 차수만큼의 pole이 허용되는 것으로 보면 된다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 가령 앞선 예시와 같이 $X=\Spec \mathbb{C}[\x,\y]$라 하자. 만일 $X$의 divisor $D$가 다음의 식

$$D=2(\x-1)-4(\y)$$

으로 주어졌다면, $\mathscr{O}_X(D)$의 global section은 반드시 

$$\frac{\y^4}{(\x-1)^2}$$

의 $\mathbb{k}[\x,\y]$-multiple이어야 한다. 이를 활용하면 $\mathscr{O}_X(D)$가 trivial line bundle $\mathscr{O}_X$와 isomorphic하다는 것을 알 수 있다. 

</div>

더 일반적으로, invertible sheaf $\mathscr{L}$과 $\mathscr{L}$의 nonzero rational section $s$가 주어졌다 하면 $\mathscr{O}(\divisor s)\cong \mathscr{L}$이 성립한다.[^1] 특히 위의 예시의 경우 $\mathscr{L}=\mathscr{O}_X$이고 $s$가 $\y^4/(\x-1)^2$으로 주어진 상황이다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Divisor $D$에 대하여, 만일 임의의 $x\in X$마다 $D\vert_U$가 principal이도록 하는 열린집합 $U$가 존재한다면 $D$를 *locally principal*이라 부른다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Locally principal divisor $D$에 대하여, $\mathscr{O}(D)$는 invertible sheaf이다. 

</div>

만일 $X$가 factorial이라면 모든 divisor는 locally principal임이 알려져 있다. 따라서 위의 조건이 항상 성립하게 된다. 



[^1]: 이는 $X$가 normal이기 때문에 가능하다.