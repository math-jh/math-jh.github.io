---

title: "군의 작용"
excerpt: "Groups acting on a set"

categories: [Math / Groups]
permalink: /ko/math/groups/group_action
header:
    overlay_image: /assets/images/Groups/Group_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures"

date: 2022-02-23
last_modified_at: 2022-02-27
weight: 6

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


이제 우리는 학부 group theory의 꽃이라 할 수 있는 Sylow's theorem을 증명한다. 하지만 그 전에 group action을 먼저 정의해야 한다.

## Monoid acting on a set

집합 $E$가 주어졌다 하고, 집합 $\Fun(E,E)$를 생각하자. $\Fun(E,E)$는 자연스러운 monoid structure를 갖는다. ([§Introduction, 정의 16](/ko/math/groups/introduction#df16) 직후의 remark) 

$\Fun(E,E)$의 임의의 원소 $f$를 택하자. 그럼 $f$는 집합 $E$ 위의 함수이다. 즉, 임의의 $x\in E$에 대하여

$$x\mapsto f(x)$$

라는 대응이 잘 정의된다. 뿐만 아니라 이 대응은 monoid structure를 잘 보존해준다. 즉, 임의의 $f,g\in \Fun(E,E)$에 대하여, $\Fun(E,E)$의 원소 $f\circ g$도 마찬가지로 함수가 될텐데, 이는

$$x\mapsto (f\circ g)(x)$$

이고, 정의에 의해 $(f\circ g)(x)$라는 원소는 $x$에 $g$를 먼저 계산한 후, $f$를 계산하여 얻어지는 원소이다. 이를 motivation 삼아 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Monoid $M$가 주어졌다 하자. $M$이 집합 $E$ 위에 *left monoid action*을 정의한다는 것은 각각의 $\alpha\in M$마다 $\Fun(E,E)$의 원소 $f_\alpha$가 하나씩 대응되어, 다음의 두 조건

1. $f_e=\id_E$,
2. 모든 $\alpha,\beta\in M$에 대해 $f_{\alpha\beta}=f_\alpha\circ f_\beta$ 

을 만족하는 것이다. 이 때 $E$를 *left $M$-set*이라 부른다. 만일 2번 조건을 

> 모든 $\alpha,\beta\in M$에 대해 $f_{\alpha\beta}=f_\beta\circ f_\alpha$

으로 바꾼다면 이를 *right monoid action*이라 부르고, $E$는 *right $M$-set*이라 부른다. 

특별히 $M$이 group인 경우, 이들을 *left (resp. right) group action*이라 부른다. 

</div>

즉 $M$이 집합 $E$ 위에 left action을 정의한다는 것은 monoid homomorphism $\phi:M\rightarrow\Fun(E,E)$가 주어졌다는 것과 같다. 1번 조건은 정확히 $\phi(e)$가 $\Fun(E,E)$의 항등원이 되어야 한다는 조건이고, 2번 조건은 $\phi$가 monoid $M$의 연산을 잘 보존해야 한다는 뜻이기 때문이다. 

한편, group $G$가 집합 $E$ 위에 act할 경우, 임의의 $\alpha\in G$에 대하여 $\alpha\alpha^{-1}=\alpha^{-1}\alpha=e$인 원소 $\alpha^{-1}$이 존재하므로, 위의 조건들에 의하여 반드시

$$f_\alpha\circ f_{\alpha^{-1}}=f_{\alpha\alpha^{-1}}=f_e=\id_E$$

그리고 유사하게 

$$f_{\alpha^{-1}}\circ f_\alpha=f_{\alpha^{-1}\alpha}=f_e=\id_E$$

이 성립해야 한다. 그러므로 group action에서는 임의의 $\alpha$에 대응된 $f_\alpha$가 invertible하며, 그 inverse는 $f_{\alpha^{-1}}$과 같게 된다. 즉, 정의에서는 $f_\alpha$가 $\Fun(E,E)$의 원소라고 하였지만, group action의 경우는 $f_\alpha$가 $\Fun(E,E)$ 대신 그 부분집합인 *bijective*한 함수들의 모임에 속한다고 해도 된다. 이 모임은 자연스러운 *group structure* 구조를 가지며, 우리는 이를 $E$ 위에서 정의된 *symmetric group*이라 부르고 $S_E$로 적기로 했었다. ([§Examples, Symmetric group](/ko/math/groups/examples#symmetric-groups)) 

한편, 두 개의 $M$-set $E,F$가 주어졌다면, 이들 사이의 *$M$-set homomorphism*또한 쉽게 정의할 수 있다. 이는 정확히 다음의 식

$$\varphi(m\cdot x)=m\cdot\varphi(x)$$

이 모든 $x\in E$, $m\in M$에 대해 성립한다는 것이다. 당연하게 임의의 $M$-set $E$에 대하여, $E$에서 $E$로의 $M$-set homomorphism들의 모임은 monoid structure를 가지고, $E$에서 $E$로의 bijective $M$-set homomorphism들은 group structure 구조를 갖게 된다. 


우선 다양한 예시들을 살펴보자.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Dihedral group $D_{2n}$과, $n$개 꼭짓점들의 집합 $V=\\{0,1,\ldots, n-1\\}$을 생각하자. 그럼 $D_{2n}$은 자연스럽게 $V$ 위에 act한다. $D_{2n}$의 두 generator $r$, $s$에 대하여

$$r(0)=1, \qquad r(1)=2,\qquad \ldots,\qquad  r(n-2)=n-1,\qquad  r(n-1)=0$$

그리고

$$s(k)=\begin{cases}0&\text{if $k=0$,}\\ n-k&\text{otherwise} \end{cases}$$

으로 정의한 후, 다른 원소들은 두 번째 조건을 만족하도록 정의하면 된다. 

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 이번엔 고정된 field $F$에 대하여, $\Mat_n(F)$가 $F^n$ 위에 act하는 상황을 생각할 수 있다. 즉 임의의 $n\times n$ matrix

$$\begin{pmatrix}a_{11}&a_{12}&\ldots&a_{1n}\\a_{21}&a_{22}&\ldots&a_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ a_{n1}&a_{n2}&\ldots&a_{nn}\end{pmatrix}$$

는 $F^n$에서 $F^n$으로의 함수를 다음의 식

$$\begin{pmatrix}x_1\\ x_2\\ \vdots\\ x_n\end{pmatrix}\mapsto \begin{pmatrix}a_{11}&a_{12}&\ldots&a_{1n}\\a_{21}&a_{22}&\ldots&a_{2n}\\ \vdots&\vdots&\ddots&\vdots\\ a_{n1}&a_{n2}&\ldots&a_{nn}\end{pmatrix}\begin{pmatrix}x_1\\ x_2\\ \vdots\\ x_n\end{pmatrix}$$

을 통해서 정의하며, 이 함수는 monoid action이 된다. 

</div>

위의 예시들은 $D_{2n}$이나 $\Mat_n(F)$ 등이 자연스럽게 group action을 정의한다는 것을 보여준다. 사실 이들은 처음 정의할 때부터 집합 ($V$ 또는 $F^n$) 위의 함수들로 정의되었으니 당연한 결과이기도 하다. 

앞으로 어떤 monoid $M$이 집합 $E$ 위에 act할 때에는, $\alpha\in M$과 $x\in E$에 대해 정의된 값 $f_\alpha(x)$를 간단하게 $\alpha\cdot x$로 적거나, 더 간단하게는 $\alpha x$로도 적는다. 물론 right action의 경우에는 다른 notation $x\cdot\alpha$ 혹은 $x\alpha$이 필요하겠지만, 다음 정의에 의해 right action은 모두 left action으로 환원시켜 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> Monoid $(M,\star, e)$가 주어졌다 하자. 그럼 이 monoid $M$의 *opposite monoid* $M^\op$는 다음과 같이 정의된 연산

$$x\star^\op y=y\star x$$

을 통해 정의되는 monoid $(M, \star^\op, e)$를 뜻한다.

</div>

어떤 monoid $M$이 집합 $E$ 위에 right action을 정의할 경우, 우리는 이를 $M^\op$가 집합 $E$ 위에 left action을 정의한다고 생각할 수 있으므로 action에 대해 살펴보기 위해서는 left action에 대한 이론만 만들면 충분하다. 따라서 앞으로 monoid (resp. group) action이라 부르는 것들은 모두 *left* monoid (resp. group) action만을 의미한다. 

Action에 대해 몇 가지 추가적인 정의를 하자. 

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Monoid $M$과 $M$-set $E$를 생각하고, 이 action이 $\phi:M\rightarrow\Fun(E,E)$로 주어졌다 하자.

1. 이 action이 *faithful*하다는 것은 $\ker\phi=\\{e\\}$가 성립하는 것이다.
2. 이 action이 *transitive*하다는 것은 임의의 $x,y\in E$에 대해 $\alpha x=y$를 만족하는 $\alpha$가 항상 존재하는 것이다.

</div>

대부분의 경우에 transitive action은 group action에서만 정의되는데, 그 이유는 조만간 orbit을 정의하며 알게 된다. 

## Stabilizer 

Monoid $M$과 $M$-set $E$에 대하여, 우리는 $\alpha\in M$이 $x\in E$에 act할 때 이 값을 $\alpha x$로 적기로 하였다. 더 일반적으로, $E$의 부분집합 $A$에 대하여 $\alpha A$를 다음의 집합

$$\alpha A=\{\alpha x: x\in A\}$$

으로 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> Monoid $M$과 $M$-set $E$를 생각하자. $E$의 부분집합 $A, B$에 대하여 $\alpha A\subset B$이도록 하는 $\alpha$들의 모임을 $A$에서 $B$로의 *transporter*라고 부르고, 만일 $\alpha A=B$가 성립한다면 이들 모임을 *strict transporter*라 부른다. $A=B$일 경우, transporter와 strict transporter를 각각 $A$의 *stabilizer*와 *strict stabilizer*라 부른다. 또, 임의의 $x\in A$에 대하여 $\alpha x=x$가 성립하도록 하는 $\alpha$들의 모임을 $A$의 *fixer*라고 부른다.

</div>

일반적으로, 집합 $A$의 fixer는 항상 strict stabilizer의 부분집합이고, strict stabilizer는 항상 stabilizer의 부분집합이지만 그 역은 성립하지 않는다. 하지만 만일 $A=\\{x\\}$라면 $A$의 stabilizer와 strict stabilizer, fixer는 모두 $\alpha x=x$를 만족하는 $\alpha\in M$들의 모임이므로 동일한 모임을 지정한다. 이를 간단히 $x$의 stabilizer라 적는다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Monoid $M$과 $M$-set $E$, 그리고 $E$의 부분집합 $A$가 주어졌다 하자.

1. $A$의 stabilizer와 strict stabilizer, fixer는 $M$의 submonoid가 된다.
2. 만일 $\alpha\in M$이 invertible이고 $A$의 strict stabilizer (resp. fixer)의 원소라면, $\alpha^{-1}$ 또한 strict stabilizer (resp. fixer)의 원소가 된다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 항등원 $e$는 임의의 $x\in E$에 대하여 $e\cdot x=\id_E(x)=x$를 만족하므로 $A$의 fixer에 속한다. 또, 임의의 $\alpha,\beta\in M$과 임의의 $x\in E$에 대하여 다음의 식

$$(\alpha\beta)x=\alpha(\beta x)$$

이 성립하고, 따라서 만일 $\alpha,\beta$가 모두 $A$의 fixer라면 $(\alpha\beta)x=x$이므로 $\alpha\beta$ 또한 $A$의 fixer가 된다. 이와 비슷하게, 만일 $\alpha,\beta$가 모두 $A$의 strict stabilizer라면 

$$(\alpha\beta)A=\alpha(\beta A)=\alpha A=A$$

가 되어 $\alpha\beta$ 또한 strict stabilizer가 되고, stabilizer는 위의 식에서 등호만 적절하게 $\subset$으로 바꾸면 얻어진다.

이제 2번을 보여야 하는데, strict stabilizer의 경우는 다음의 식

$$A=(\alpha^{-1}\alpha)A=\alpha^{-1}(\alpha A)=\alpha^{-1}A$$

에서 자명하다. 또, fixer의 경우는 위 식의 집합 $A$를 원소 $x\in A$로 바꾸면 된다. 

</details>

1번의 결과에 의하여, $A$의 stabilizer는 그 자체로 monoid structure를 가진다. 또, 이 monoid는 집합 $A$ 위에 act할 경우 그 결과물로 항상 $A$의 원소가 나오므로, 자연스럽게 $A$ 위의 action을 정의한다. 또, 2번의 결과에 의해, 특히 $M$이 group이라면 $A$의 strict stabilizer와 fixer는 $M$의 subgroup이 된다.

<div class="proposition" markdown="1">

<ins id="crl8">**따름정리 8**</ins> Group $G$와 $G$-set $E$, 그리고 $E$의 부분집합 $A$에 대하여, $A$의 stabilizer $S$와 fixer $F$는 각각 $G$의 subgroup이 되고, $F\trianglelefteq S$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$F$가 $G$의 normal subgroup인 것만 보이면 충분하다. 그런데 앞서 말한 1번의 결과에 의하여, $S$는 집합 $A$ 위에 act한다. 즉, group homomorphism $\phi:S\rightarrow S_A$가 잘 정의된다. 그럼 $F\subset S$는 정확히 $\phi$에 의해 $\id_A$로 옮겨지는 원소들의 모임, 즉 $\ker\phi$이므로 $S$의 normal subgroup이 된다. 

</details>

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Group $G$와, $G$-set $E$가 주어졌다 하자. $x\in E$의 stabilizer를 $G_x$라 적으면, 다음의 식

$$G_{\alpha x}=\alpha G_x\alpha^{-1}$$

이 모든 $\alpha\in G$에 대해 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $\beta\in G_x$에 대하여, $\alpha\beta\alpha^{-1}\in G_{\alpha x}$가 성립한다는 사실은 다음의 식

$$(\alpha\beta\alpha^{-1})(\alpha x)=\alpha(\beta x)=\alpha x$$

에서 분명하다. 반대로, $x=\alpha^{-1}(\alpha x)$이므로, 임의의 $\beta\in G_{\alpha x}$에 대하여

$$(\alpha^{-1}\beta\alpha)x=(\alpha^{-1}\beta\alpha)(\alpha^{-1}\alpha x)=\alpha^{-1}(\beta(\alpha x))=\alpha^{-1}(\alpha x)=x$$

이 성립하므로 $\alpha^{-1} G_{\alpha x}\alpha\subset G_x$이고 따라서 $G_{\alpha x}\subset\alpha G_x\alpha^{-1}$이 성립한다.

</details>

## Inner automorphism

우리는 앞서 group action의 예시를 몇 가지 살펴보았다. 학부 수준의 group theory에서 다루는 group action들 중 재미있는 것은 대부분 $G$가 자기 자신 위에 act하는 경우, 그 중에서도 conjugation으로 act하는 경우 생긴다. ([§Examples, 예시 24](/ko/math/groups/examples#ex24) 이후의 remark)

Monoid $\Fun(G,G)$를 생각하자. 이제는 $G$가 단순히 집합이 아니라 연산이 주어진 group이므로, 우리가 관심있는 대상들 또한 $G$에서 $G$로의 함수들이 아니라 $G$에서 $G$로의 *homomorphism*들로 바뀌게 된다. $G$에서 $G$로의 homomorphism들을 우리는 *endomorphism*이라 부르고, 이들의 모임을 $\End(G)$로 적는다. 이 모임이 함수의 합성에 대해 monoid structure를 이룬다는 것은 자명하다.

Monoid $\End(G)$는 일반적으로 group이 되지 않는다. 그리고 그 이유는 정확히 역원을 갖지 않는다는 것 하나 때문이므로, $G$에서 $G$로의 *bijective* homomorphism들을 모아두면 이는 group structure를 갖게 된다. 이렇게 $G$ 위에서 정의된 bijective endomorphism들을 우리는 *automorphism*이라 부르고, 이들이 이루는 group을 $\Aut(G)$로 적기로 한다.

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> Group $G$의 임의의 원소 $x$에 대하여, 다음의 식

$$y\mapsto xyx^{-1}$$

으로 정의되는 $G$에서 $G$로의 함수를 $\Inn(x)$로 적자. 그럼 $\Inn(x)$는 $G$의 automorphism이 된다. 또, $G$에서 $\Aut(G)$로의 mapping $\Inn:G\rightarrow\Aut(G)$을 다음의 식

$$x\mapsto\Inn(x)$$

으로 정의하면 이는 group homomorphism이 되며, $\Inn$의 kernel은 $G$의 center, 그리고 image는 $\Aut(G)$의 normal subgroup이 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\Inn(x)$가 $G$의 automorphism인 것을 보여야 한다. 임의의 $y,z\in G$에 대하여, 

$$\Inn(x)(yz)=x(yz)x^{-1}=(xyx^{-1})(xzx^{-1})=\Inn(x)(y)\Inn(x)(z)$$

이 성립하므로 $\Inn(x)$는 $G$ 위의 endomorphism을 정의한다. 한편, 우리는 임의의 $x,y\in G$와 임의의 $z\in G$에 대하여

$$\Inn(xy)(z)=(xy)z(xy)^{-1}=x(yzy^{-1})x^{-1}=\bigl(\Inn(x)\circ\Inn(y)\bigr)(z)$$

이 성립하는 것을 쉽게 확인할 수 있고, 또 $\Inn(e)=\id_G$이므로 $x\mapsto\Inn(x)$는 $G$에서 $\End(G)$로의 monoid homomorphism을 정의한다. 그런데 $G$의 임의의 원소는 invertible하므로, 다음의 식

$$\Inn(x)\circ\Inn(x^{-1})=\Inn(e)=\Inn(x^{-1})\circ\Inn(x)$$

으로부터 $\Inn(x)$ 또한 invertible하다는 것을 알 수 있다. 즉, $\Inn(x)$들은 모두 실은 $\Aut(G)$의 원소들이고, 따라서 $\Inn:G\rightarrow\Aut(G)$는 group homomorphism이 된다. 

이제 $\Inn$의 kernel과 image를 찾아보자. 우선 $x\in \ker\Inn$이기 위해서는 $\Inn(x)=\id_G$여야 하고, 이는 곧 임의의 $y\in G$에 대하여 다음의 식

$$y=\id_G=\Inn(x)(y)=xyx^{-1}$$

이 성립하는 것과 동치이다. 그런데 위 식은 $yx=xy$와 동치이므로, $x\in\ker\Inn$인 것은 $x$가 임의의 $y$와 commute한다, 곧 $x$가 $G$의 center에 포함된다는 것과 동치이다.

마지막으로 $\Inn$의 image가 $\Aut(G)$의 normal subgroup이 된다는 것을 보여야 한다. 임의의 $\alpha\in\Aut(G)$가 주어졌다 하자. 그럼 임의의 $\Inn(x)\in \im(\Inn)$과 임의의 $y\in G$에 대하여,

$$(\alpha\circ\Inn(x)\circ\alpha^{-1})(y)=\alpha(x\alpha^{-1}(y)x^{-1})=\alpha(x) y\alpha(x)^{-1}=\Inn(\alpha(x))\in\im(\Inn)$$

이 되므로 $\Inn$의 image는 $\Aut(G)$의 normal subgroup이 된다.  
 
</details>

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> Group $G$에 대하여, $y\mapsto xyx^{-1}$ 꼴로 정의되는 $G$의 automorphism을 $G$의 *inner automorphism*이라 부른다. Inner automorphism들의 모임을 $\Inn(G)$로 표기한다. 

</div>

정의에 의하여, $G$의 subgroup $N$이 normal인 것은 임의의 $x$에 대해 $xNx^{-1}=N$인 것과 동치이다. 즉, $N$이 normal인 것은 $N$이 임의의 inner automorphism에 대해 stable하다는 것과 동치이다. 그렇다면 이 characterization을 inner automorphism이 아닌, 임의의 automorphism으로 확장할 수 있다.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> Group $G$의 subgroup $H$가 *characteristic subgroup*이라는 것은 임의의 $\alpha\in\Aut(G)$에 대해 $\alpha(H)=H$가 성립하는 것이다.

</div>

예를 들어 $G$의 center $C(G)$는 characteristic subgroup이 된다. 임의의 automorphism $\alpha\in\Aut(G)$와 $\alpha (x)\in \alpha(C(G))$, 그리고 임의의 $y\in G$에 대하여  

$$\alpha(x)y=\alpha(x)\alpha(\alpha^{-1}(y))=\alpha(x\alpha^{-1}(y))=\alpha(\alpha^{-1}(y)x)=\cdots=y\alpha(x)$$

가 성립하기 때문이다. 

일반적으로 $\trianglelefteq$는 transitive하지 않다. 즉, $N\trianglelefteq G$이고 $H\trianglelefteq N$이라 하여 $H\trianglelefteq G$인 것은 아니다. 하지만 characteristic subgroup은 transitive하게 작동한다. 

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> Group $G$와, $G$의 characteristic subgroup $H$가 주어졌다 하자. 만일 $K$가 $H$의 characteristic subgroup이라면, $K$는 $G$의 characteristic subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Aut(G)$의 임의의 원소 $\alpha$가 주어졌다 하자. $H$는 characteristic subgroup이므로, $\alpha\|\_H$는 $\Aut(H)$의 원소이고, $K$는 $H$의 characteristic subgroup이므로 $\alpha(K)=\alpha\|\_H(K)=K$가 성립한다.

</details>

만일 $H$가 $G$의 normal subgroup이었다면, $\Inn(G)$의 임의의 원소가 $H$로 잘 restrict되므로 위와 동일한 증명에 의하여 

> $H$가 $G$의 normal subgroup이고, $K$가 $H$의 characteristic subgroup이라면 $K$는 $G$의 normal subgroup이다.

가 성립한다.

## Orbit

<div class="definition" markdown="1">

<ins id="df14">**정의 14**</ins> Group $G$와 $G$-set $E$를 생각하자. 주어진 원소 $x,y\in E$에 대하여, 만일 어떠한 $\alpha\in G$가 존재하여 $y=\alpha x$이도록 할 수 있다면 이 action에 의해 $y$가 $x$에 *conjugate*하다고 한다. 또, $x$와 conjugate한 모든 원소들의 집합을 $x$의 *orbit*이라 부른다.

</div>

위에서 정의한 conjugate은 $E$ 위에서의 equivalence relation $\sim$을 정의한다. 이는 다음의 세 조건

1. $x=ex$,
2. $y=\alpha x\implies x=\alpha^{-1}y$,
3. $z=\beta y,y=\alpha x\implies z=(\beta\alpha)x$

으로부터 명확하다. 그럼 $x$의 orbit은 다름아닌 이 equivalence relation의 equivalence class가 되고, $G$의 action이 transitive하다는 것은 ([정의 5](#df5)) 이 equivalence relation에 의한 quotient set $E/\sim$이 하나의 원소로 이루어져 있다는 뜻이다. 만일 $G$가 단순한 monoid였다면 $\sim$은 equivalence relation이 되지 않았을 것이고, orbit 또한 큰 의미를 갖지 않았을 것이다.

임의의 group $G$와 subgroup $H$에 대하여, left coset들의 모임 $G/H$를 생각하자. 임의의 $xH\in g/H$에 대하여, $G$의 action을 다음의 식

$$g\cdot(xH)=(gx)H$$

으로 정의할 수 있다. 한편, $H$의 normalizer $N=N_G(H)$에 대하여, $N$은 $H$ 위에 다음의 식

$$(xH)\cdot n=xHn=(xn)H$$

으로 act하며, 이는 $N$의 right action을 정의한다. 또, 만일 $n\in H$라면 $Hn=nH=H$이므로 이 action의 kernel은 $H$이고, 따라서 $N/H$가 $G/H$ 위에 right action을 정의한다. 우리가 맨 처음에 지적했듯, 이러한 상황에서는 opposite group $(N/H)^{\op}$이 $G/H$ 위에 (left) act하는 것으로 취급할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp15">**명제 15**</ins> 위와 같은 상황에서, $(N/H)^{\op}$의 action은 transitive하다. 또, 만일 이 action을 $\phi:(N/H)^{\op}\rightarrow S_{G/H}$으로 적으면, $\phi$는 $(N/H)^\op$와, $G$-set $G/H$의 bijective $G$-set homomorphism들의 group 사이의 isomorphism이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G/H$에서, $eH$의 orbit은 $G/H$ 전체가 되므로 action이 transitive함은 자명하다. 따라서 둘째 주장만 보이면 충분하다. 편의상 

> $G$-set $G/H$의 bijective $G$-set homomorphism들의 group

을 $\Phi$로 적자. 주어진 명제는 group homomorphism $\phi:(N/H)^{\op}\rightarrow S_{G/H}$가 injective이고, 사실 $\im\phi$는 정확히 $\Phi$가 된다는 뜻이다. 

 먼저 $\ker\phi\leq H$이므로, $\phi$에 의해 identity map에 대응되는 모든 $N$의 원소들은 $N/H$에서 $eH$에 포함되고 따라서 $\phi$는 injective이다. 

또, 위의 식에서 알 수 있듯, $(N/H)^\op$의 left action과 $G$의 left action은 서로 commute하므로, $(N/H)^\op$의 원소들 각각은 $G/H$에서 $G/H$로의 $G$-set homomorphism을 정의하고, 이들 원소는 모두 invertible하므로 사실 이들에 대응되는 $G/H$ 위에서의 $G$-set endomorphism은 사실 $G$-set automorphism이 되어야 한다. 즉 $\im\phi\leq\Phi$가 성립한다.

이제 반대방향 포함관계를 보여야 하므로, $f\in\Phi$라 하자. 우선 $f(eH)$의 stabilizer $G_{f(eH)}를 생각하면, 이는 $g\cdot f(eH)=f(eH)$를 만족하는 모든 $g\in G$들의 모임이다. 그런데 $f$는 $G$-set automorphism이므로, 위의 식은

$$f\bigl(g\cdot (eH)\bigr)=f(eH)$$

와 동치이고, $f$는 bijective이므로 $g\cdot (eH)=eH$와 동치가 된다. 따라서 $f(eH)$의 stabilizer는 정확히 $eH$의 stabilizer, 곧 $H$와 같다. 한편, $f(eH)=\alpha(eH)$를 만족하는 $\alpha\in G$를 택하자. [명제 9](#pp9)에 의해 $f(eH)$의 stabilizer는

$$H=G_{f(eH)}=G_{\alpha(eH)}=\alpha G_{eH}\alpha^{-1}=\alpha H\alpha^{-1}$$

을 만족하고, 따라서 $\alpha$는 $H$의 normalizer, 즉 $N$의 원소이다. 이제 임의의 $xH\in G/H$에 대하여

$$f(xH)=f\bigl(x(eH)\bigr)=xf(eH)=x(\alpha H)=x(H\alpha)=xH\alpha$$

이므로, $f$는 $\alpha$ (혹은 $\alpha H$)에 의해 정의되는 mapping과 동일하고 따라서 $\phi$는 surjective하다. 

</details>


한편, 우리는 $x$의 *stabilizer*를 다음의 식

$$G_x=\{g\in G: gx=x\}$$

으로 정의했었는데, 



---
**Reference**

**[Bou]** Bourbaki, N., *Algebra I*, Elements of Mathematics, Springer, 1989.  
**[Hun]** Thomas W. Hungerford, *Algebra*, Graduate texts in mathematics, Springer, 2003.

---
