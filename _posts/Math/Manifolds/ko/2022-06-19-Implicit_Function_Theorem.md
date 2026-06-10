---
title: "음함수 정리"
description: "미분가능한 다양체로 확장한 음함수 정리를 다루며, immersed submanifold가 locally embedded임을 보이고 submersion level set theorem을 유도한다."
excerpt: "미분다양체에서의 음함수 정리와 그 결과들"

categories: [Math / Manifolds]
permalink: /ko/math/manifolds/implicit_function_theorem
sidebar: 
    nav: "manifolds-ko"

date: 2022-06-19
last_modified_at: 2022-12-10
weight: 9
published: false

---

우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Manifold $$M$$과 coordinate system $$(U,\varphi)$$가 주어졌다 하자. 이 때 $$\varphi=(x^i)_{i=1}^m$$이고, $$0\leq k\leq m$$라 하고, $$p\in \varphi(U)$$에 대해 다음의 집합

$$S=\{q\in U\mid x^i(q)=r^i(p), k+1\leq i\leq m\}$$

에 subspace topology와 coordinate system $$(S, (x^j\vert_S)_{j=1}^k)$$이 부여된 manifold를 $$(U,\varphi)$$의 *slice*라 부른다.

</div>

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 두 manifold 사이의 immersion $$F:M\rightarrow N$$이 주어졌다 하자. 그럼 임의의 $$p\in M$$이 주어질 때마다, $$F(p)$$를 포함하는 coordinate system $$(V,\varphi)$$와 $$p$$의 적당한 열린근방 $$U$$가 존재하여 $$F\vert_U$$가 injective이고, $$F(U)$$가 $$(V,\varphi)$$의 slice이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim M=k$$, $$\dim N=n$$이라 하자. $$F(p)$$를 포함하는 coordinate system $$(V_0,\psi)$$, $$\psi=(y^i)_{i=1}^n$$을 하나 택하자. $$dF_p$$가 injective이므로 [§부분다양체와 역함수 정리, ⁋따름정리 10](/ko/math/manifolds/submanifolds#cor10)에 의하여 집합 $$\{y^i\circ F\}$$의 적당한 부분집합이 점 $$p$$ 근방에서 $$M$$의 coordinate system을 이룬다. 좌표의 순서를 재배열하여, $$x^j=y^j\circ F$$ ($$j=1,\ldots,k$$)들이 $$p$$의 적당한 열린근방 $$U_1$$ 위에서 coordinate system $$(U_1,x)$$, $$x=(x^j)_{j=1}^k$$를 이룬다고 가정해도 좋다. 필요하다면 $$U_1$$을 줄여 $$F(U_1)\subseteq V_0$$이라 가정하자.

우선 $$F\vert_{U_1}$$은 injective이다. $$q,q'\in U_1$$이 $$F(q)=F(q')$$를 만족한다면 각각의 $$j\leq k$$에 대해 $$x^j(q)=y^j(F(q))=y^j(F(q'))=x^j(q')$$인데, $$x$$가 $$U_1$$ 위에서 injective이기 때문이다.

이제 $$U_1$$ 위에서 $$F$$를 좌표로 나타내자. $$j\leq k$$에 대하여 $$y^j\circ F=x^j$$이므로, $$\psi\circ F\circ x^{-1}:x(U_1) \rightarrow \mathbb{R}^n$$의 처음 $$k$$개의 성분은 identity이고, 따라서 적당한 $$C^\infty$$ 함수들 $$h^i:x(U_1) \rightarrow \mathbb{R}$$ ($$i=k+1,\ldots,n$$)이 존재하여 임의의 $$q\in U_1$$에 대해

$$\psi(F(q))=\bigl(x^1(q),\ldots,x^k(q),h^{k+1}(x(q)),\ldots,h^n(x(q))\bigr)$$

이 성립한다. 즉 $$F(U_1)$$은 $$\psi$$-좌표 상에서 함수 $$h=(h^{k+1},\ldots,h^n)$$의 그래프이다.

이제 $$V_0$$의 열린 부분집합

$$V'=\left\{q'\in V_0\mid (y^1(q'),\ldots,y^k(q'))\in x(U_1)\right\}$$

을 생각하면 $$F(p)\in V'$$이다. $$V'$$ 위에서 새로운 함수들을

$$w^j=y^j\quad (j=1,\ldots,k),\qquad w^i=y^i-h^i(y^1,\ldots,y^k)\quad (i=k+1,\ldots,n)$$

으로 정의하자. 그럼 점 $$F(p)$$에서

$$dw^j=dy^j\quad(j\leq k),\qquad dw^i=dy^i-\sum_{j=1}^k\frac{\partial h^i}{\partial y^j}\,dy^j\quad(i>k)$$

이므로, $$dw^i$$들은 basis $$dy^i$$들로부터 대각성분이 모두 $$1$$인 삼각행렬꼴의 변환으로 얻어져 일차독립이다. 따라서 [§부분다양체와 역함수 정리, ⁋따름정리 6](/ko/math/manifolds/submanifolds#cor6)에 의하여 $$F(p)$$의 적당한 열린근방 $$V\subseteq V'$$ 위에서 $$\varphi=(w^1,\ldots,w^n)$$은 coordinate system이 된다.

마지막으로 $$U=U_1\cap F^{-1}(V)$$로 두자. 임의의 $$q\in U$$와 $$i>k$$에 대하여

$$w^i(F(q))=y^i(F(q))-h^i(x(q))=h^i(x(q))-h^i(x(q))=0$$

이다. 거꾸로 $$q'\in V$$가 모든 $$i>k$$에 대해 $$w^i(q')=0$$을 만족한다 하자. $$b=(y^1(q'),\ldots,y^k(q'))$$라 하면 $$b\in x(U_1)$$이고, 점 $$F(x^{-1}(b))$$의 $$\psi$$-좌표는 $$(b,h(b))$$로 $$q'$$의 $$\psi$$-좌표와 일치하므로 $$q'=F(x^{-1}(b))$$이다. 특히 $$q'\in V$$이므로 $$x^{-1}(b)\in U_1\cap F^{-1}(V)=U$$이고, 즉 $$q'\in F(U)$$이다. 종합하면

$$F(U)=\left\{q'\in V\mid \text{$w^i(q')=w^i(F(p))=0$ for $i=k+1,\ldots,n$}\right\}$$

이므로 $$F(U)$$는 $$(V,\varphi)$$의 slice이다.

</details>

위의 보조정리에서, $$M$$의 열린집합 $$U$$에 대하여 $$F(U)$$가 $$(V,\varphi)$$의 slice가 된다는 것을 신경써서 볼 필요가 있다. 예를 들어, $$F(M)\cap V$$는 일반적으로 slice가 될 필요가 없으며, 이는 심지어 $$F$$가 submanifold일 경우에도 마찬가지이다.

![counterexample](/assets/images/Math/Manifolds/Implicit_Function_Theorem-1.png){:style="width:200px" class="invert" .align-center}

하지만 만일 $$M$$이 embedding이었다면 $$(V,\varphi)$$를 적당히 잡아 $$F(M)\cap V$$가 $$V$$의 slice가 되도록 할 수 있다. 이러한 관점에서 위 보조정리를 

> Immersed submanifold는 locally embedded이다

정도로 요약할 수 있다.

## 음함수 정리와 그 결과들

이제 우리는 음함수 정리를 미분다양체로 확장할 준비가 되었다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (음함수 정리)**</ins> $$U\subset\mathbb{R}^{m-n}\times\mathbb{R}^n$$이 열린집합이라 하고, 구별을 위해 $$\mathbb{R}^{m-n}$$의 좌표들을 $$r^1,\ldots, r^{m-n}$$, 그리고 $$\mathbb{R}^n$$의 좌표들을 $$s^1,\ldots, s^n$$이라 하자. 또, $$f:U\rightarrow\mathbb{R}^n$$이 $$C^\infty$$이고, 어떤 점 $$(x_0, y_0)\in U$$에 대하여 $$f(x_0,y_0)=0$$이라 하자. 만일 점 $$(x_0,y_0)$$에서 Jacobian matrix

$$\begin{pmatrix}\partial f^1/\partial r^1&\partial f^1/\partial r^2&\cdots&\partial f^1/\partial r^{m-n}&\partial f^1/\partial s^1&\partial f^1/\partial s^2&\cdots&\partial f^1/\partial s^n\\\partial f^2/\partial r^1&\partial f^2/\partial r^2&\cdots&\partial f^2/\partial r^{m-n}&\partial f^2/\partial s^1&\partial f^2/\partial s^2&\cdots&\partial f^2/\partial s^n\\ \vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\\partial f^n/\partial r^1&\partial f^n/\partial r^2&\cdots&\partial f^n/\partial r^{m-n}&\partial f^n/\partial s^1&\partial f^n/\partial s^2&\cdots&\partial f^n/\partial s^n\end{pmatrix}$$

의 $$n\times n$$ submatrix

$$\begin{pmatrix}\partial f^1/\partial s^1&\partial f^1/\partial s^2&\cdots&\partial f^1/\partial s^n\\\partial f^2/\partial s^1&\partial f^2/\partial s^2&\cdots&\partial f^2/\partial s^n\\\vdots&\vdots&\ddots&\vdots\\\partial f^n/\partial s^1&\partial f^n/\partial s^2&\cdots&\partial f^n/\partial s^n\end{pmatrix}$$

가 nonsingular라면, $$x_0$$의 적당한 열린근방 $$V$$, $$y_0$$의 적당한 열린근방 $$W$$, 그리고 $$C^\infty$$ 함수 $$g:V\rightarrow W$$가 존재하여 $$V\times W\subseteq U$$이고, 각각의 $$(p,q)\in V\times W$$마다 

$$f(p,q)=0\iff q=g(p)$$

를 만족한다.

</div>

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4 (Submersion level set theorem)**</ins> $$F:M\rightarrow N$$이 $$C^\infty$$라 하고, $$q\in F(M)$$를 고정하고 $$P=F^{-1}(q)$$라 하자. 만일 임의의 $$p\in P$$마다 $$dF_p:T_pM\rightarrow T_{F(p)}N$$이 surjective라면, $$P$$ 위에 정의된 유일한 manifold 구조가 존재하여 canonical injection $$\iota:P\hookrightarrow M$$이 submanifold가 된다. 

또, 이 때 $$\iota$$는 embedding이고, $$P$$의 codimension $$\dim M-\dim P$$가 $$\dim N$$과 동일해진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim M=m$$, $$\dim N=n$$이라 하자. 임의의 $$p\in P$$를 고정하고, $$q=F(p)$$를 포함하는 coordinate system $$(Y,\psi)$$, $$\psi=(y^j)_{j=1}^n$$을 $$\psi(q)=0$$이도록 택하자. $$dF_p$$가 surjective이므로 [§부분다양체와 역함수 정리, ⁋따름정리 9](/ko/math/manifolds/submanifolds#cor9)에 의하여 적당한 함수들 $$x^{n+1},\ldots,x^m$$이 존재하여

$$x^1=y^1\circ F,\quad\ldots,\quad x^n=y^n\circ F,\qquad x^{n+1},\quad\ldots,\quad x^m$$

이 $$p$$의 적당한 열린근방 $$W$$ 위에서 coordinate system을 이룬다. 필요하다면 $$W$$를 줄여 $$F(W)\subseteq Y$$라 가정하자. 그럼 $$w\in W$$에 대하여 $$F(w)=q$$인 것은 $$\psi$$가 injective이므로 $$y^j(F(w))=0$$이 모든 $$j\leq n$$에 대해 성립하는 것과 동치이고, 따라서

$$P\cap W=\left\{w\in W\mid x^1(w)=\cdots=x^n(w)=0\right\}$$

이다. 즉 $$P\cap W$$는 coordinate system $$(W,(x^i)_{i=1}^m)$$의 slice이다.

이제 $$P$$에 $$M$$의 subspace topology를 주고, 위에서 얻어지는 각각의 slice에 함수

$$\varphi_p=(x^{n+1},\ldots,x^m)\big\vert_{P\cap W}$$

를 주자. $$x=(x^i)_{i=1}^m$$이 $$W$$에서 열린집합 $$x(W)\subseteq\mathbb{R}^m$$으로의 homeomorphism이므로, $$\varphi_p$$는 $$P\cap W$$에서 열린집합 $$\{a\in\mathbb{R}^{m-n}\mid (0,a)\in x(W)\}$$으로의 homeomorphism이다. 또, 두 chart $$(P\cap W,\varphi_p)$$, $$(P\cap W',\varphi_{p'})$$의 transition은

$$\varphi_{p'}\circ\varphi_p^{-1}:a\mapsto \bigl(\text{$x'\circ x^{-1}(0,a)$의 마지막 $m-n$개의 성분}\bigr)$$

으로, $$M$$의 두 coordinate system 사이의 $$C^\infty$$ transition 함수의 합성과 제한이므로 $$C^\infty$$이다. $$P$$는 $$M$$의 subspace로서 Hausdorff이고 second countable이므로, 이들 chart는 $$P$$를 $$(m-n)$$차원 manifold로 만든다.

이 구조에 대하여 $$\iota:P\hookrightarrow M$$은 좌표로 나타내면 $$a\mapsto(0,a)$$의 꼴이므로 $$C^\infty$$이고, 모든 점에서 $$d\iota$$가 injective이다. 즉 $$\iota$$는 injective immersion이므로 submanifold이고, $$P$$에 처음부터 subspace topology를 주었으므로 embedding이다. 차원을 세어보면 $$P$$의 codimension은 $$\dim M-\dim P=m-(m-n)=n=\dim N$$이다.

마지막으로 이러한 manifold 구조의 유일성은 [§부분다양체의 유일성, ⁋명제 5](/ko/math/manifolds/uniqueness_of_submanifold#prop5)로부터 나온다. $$(P,\iota)$$가 subspace topology에 대해 $$M$$의 submanifold가 되는 미분구조를 가지므로, 이 구조는 $$(P,\iota)$$를 $$M$$의 submanifold로 만드는 유일한 manifold 구조이기 때문이다.

</details>

다음 따름정리의 가정은 앞선 따름정리의 가정보다 약하기 때문에 더 잘 사용할 수 있다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5 (Constant-rank level set theorem)**</ins> $$F:M\rightarrow N$$이 $$C^\infty$$라 하고, 각각의 $$p\in P$$마다 정의되는 $$dF_p:T_pM\rightarrow T_{F(p)}N$$이 모든 점 $$p\in P$$에서 같은 rank를 가진다고 하자. 그럼 $$F:M\rightarrow N$$은 embedded submanifold이다.

</div>

이 정리들을 통해 주어진 manifold $$M$$의 특정한 부분집합이 embedded submanifold라는 것을 보일 수 있는데, 이는 대표적으로 다음과 같은 논증을 따른다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$\mathbb{R}^{n+1}$$에서 $$\mathbb{R}$$로의 함수 

$$f(x)=\lvert x\rvert^2=\sum_{i=1}^{n+1} r^i(x)^2$$

를 생각하자. 임의의 점 $$x\in \mathbb{R}^{n+1}$$과 $$v\in T_x\mathbb{R}^{n+1}$$에 대하여,

$$df_x(v)=v(f)=\sum v^i\frac{\partial f}{\partial r^i}\bigg\vert_{x}=2\sum r^i(x) v^i$$

이 성립하며, 이로부터 $$x$$가 원점이 아니라면 $$v$$를 조절하여 $$df_x(v)$$가 임의의 실수값을 갖도록 할 수 있음을 안다. 즉, $$df_x$$가 원점을 제외하면 항상 surjective이므로, $$f^{-1}(1)$$이 $$\mathbb{R}^{n+1}$$의 submanifold이도록 하는 유일한 manifold 구조가 존재한다. 유일성에 의하여 이 구조는 $$S^n$$에 주어진 manifold 구조와 동일하며, 다시 [따름정리 5](#cor5)에 의해 이 구조는 $$\mathbb{R}^{n+1}$$의 embedded submanifold임을 알 수 있다.

</div>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---