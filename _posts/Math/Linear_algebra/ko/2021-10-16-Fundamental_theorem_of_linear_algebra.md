---

title: "선형대수학의 기본정리"
excerpt: "선형대수학의 기본정리"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/ftla
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Linear_algebra/Basis_and_dimension.png
    overlay_filter: 0.5

date: 2021-10-16
last_modified_at: 2022-08-07

weight: 11

---

지난 글에서 각각 $n$차원, $m$차원인 두 $F$-벡터공간 $V,W$에 대하여 $\operatorname{Hom}(V,W)$는 $mn$차원 $F$-벡터공간이 된다는 것을 살펴보았다. 또 $m\times n$ 행렬들의 공간 $\operatorname{Mat}_{m\times n}(F)$ 또한 $mn$차원의 $F$-벡터공간이다. 

## 기본정리: 유클리드 공간의 경우

우선 유클리드 $n$-공간의 경우부터 시작한다. 이 글에서, 유클리드 공간 $F^n$, $F^m$는 단순한 $F$-벡터공간일 뿐만 아니라, 표준기저 $\mathcal{E}_n=\\{e_1,\ldots, e_n\\},\mathcal{E}_m=\\{e_1,\ldots,e_m\\}$까지 고정된 공간으로 취급한다.[^1] 

앞선 review는 당연히 $V=F^n$, $W=F^m$일 때에도 성립하며, 이 경우 특히 식 (1)은 선형사상의 행렬표현 정도가 아니라, 정확히 선형사상

$$\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix}\in F^n\quad\mapsto\quad\begin{pmatrix}w_1\\w_2\\\vdots\\w_m\end{pmatrix}\in F^m$$

그 자체가 된다. 뿐만 아니라, $m\times n$ 행렬은 똑같은 방식으로 선형사상을 지정해준다는 것을 확인할 수 있다.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 유클리드 $n$-공간 $F^n$과, 행렬 $A\in\operatorname{Mat}\_{m\times n}(F)$를 생각하자. 임의의 $x\in F^n$에 대하여, $L_A(x)$를 다음의 식

$$L_A(x)=Ax$$

으로 정의하면, $L_A$는 $F^n$에서 $F^m$으로의 선형사상이 된다. 

</div>

$F^n$에서 $F^m$으로의 임의의 선형사상 $L$이 주어졌다 하고, 식 (1)을 통해 얻어지는 행렬을 $[L]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$라 하자. 그럼 우리는 어렵지 않게 $L=L\_{[L]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}}$임을 확인할 수 있다. 그러니, 적어도 유클리드 $n$-공간에서는 다음 두 집합들 사이의 bijection

<center style="margin-bottom: 10pt">{$F^n$에서 $F^m$로의 선형사상들의 집합} $\longleftrightarrow$ $\operatorname{Mat}_{m\times n}(F)$</center>
  
이 존재한다. 더 정확하게는, 각각 $L\mapsto [L]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$, 그리고 $A\mapsto L_A$ ([예시 1](#ex1)의 정의)이 서로의 역함수가 되는 bijection이 된다. 

따라서 유클리드 공간 $F^n$들을 모두 모아두면, 이들 사이의 선형사상 $F^n\rightarrow F^m$은 사실 정확하게 $m\times n$ 행렬들과 동일하므로, 이들 모임은 *대상들*인 유클리드 $n$-공간들 $F^n$,그리고 이 대상들 사이의 (구조를 보존하는) *함수* $F^n\rightarrow F^m$, 즉 $\operatorname{Mat}_{m\times n}(F)$의 원소들(행렬들)로 이루어지게 된다. 

물론 아직까지는 우리가 답하지 못하는 질문들이 많다. 예를 들어, 

1. 우리는 위의 bijection을 통해 선형사상 $F^n\rightarrow F^m$을 행렬로 보고 있는데, 그럼 두 선형사상 $L_1:F^n\rightarrow F^m$, $L_2:F^m\rightarrow F^k$의 합성 $L_2\circ L_1:F^n\rightarrow F^k$는 행렬로 따지면 어떻게 될 것인지? 
2. 혹은, $\operatorname{Mat}\_{m\times n}(F)$는 $F$-벡터공간인데, 그럼 위 bijection의 왼쪽에 있는 선형사상들의 집합 또한 $F$-벡터공간인지? 

등등.

둘째 질문은 사실 질문이라기엔 좀 부족하다. 왜냐하면, 어떤 두 집합 $A,B$ 사이에 bijection이 존재하고, 집합 $B$ 위에 어떤 수학적인 구조가 주어져 있다면, 이 bijection을 통해 항상 집합 $A$에 이 구조를 물려줄 수 있기 때문이다. 예를 들어, 집합 $\mathbb{N}$과 $\mathbb{Z}$ 사이에는 bijection이 존재한다. 함수 $f:\mathbb{N}\rightarrow\mathbb{Z}$를 다음의 식

$$f(n)=(-1)^n\left\lfloor \frac{n+1}{2}\right\rfloor$$

으로 정의하면 $f$는 $\mathbb{N}$에서 $\mathbb{Z}$로의 bijection이다.[^2] 한편, $\mathbb{Z}$는 가환군 구조를 갖고 $\mathbb{N}$은 그렇지 않다. ([§Basic definition, 정의 1](#df1)) 하지만, $\mathbb{N}$ 위의 더하기를 $f$를 통해 아예 새롭게 더해버리면, 즉 $1+1$을 $2$로 정의하는 대신, $\mathbb{Z}$에서 $f(1)+f(1)=-1-1=-2$를 계산한 후, $f^{-1}$을 통해 $f^{-1}(-2)=4$이므로 아예 $1+1=4$로 정의해버리면 $\mathbb{N}$은 가환군 구조를 갖게 된다.  
우리는 간결함을 위해 이 *대수적 구조*를 우리가 아는 구조 중 가장 단순한 가환군 구조로 두었지만, 당연히 $F$-벡터공간의 경우에도 똑같은 논리가 성립한다. (굳이 concrete한 예시가 필요하다면 **[Lee], 보기 3.6.7**이 그러하다.) 

아무튼 이러한 문제 때문에, 둘째 질문은 사실 bijection의 왼쪽 집합, $F^n$에서 $F^m$으로의 선형사상들의 집합이 $F$-벡터공간 구조를 *스스로* 가지고 있을 때만 말이 될 것이고, 이 경우 정확한 질문은 단순히 $F^n$에서 $F^m$으로의 선형사상들의 집합이 $F$-벡터공간이냐는 것이 아니라, 이 bijection이 과연 양쪽의 $F$-벡터공간 구조를 유지하는지, 곧 이 bijection이 실은 동형사상인지가 될 것이다.

사실은, 더 일반적으로 임의의 $F$-벡터공간들에 대해 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 두 $F$-벡터공간 $V$, $W$를 생각하자. $L,L_1,L_2$이 $V$에서 $W$로의 선형사상들이고,  $\alpha\in F$라면

$$L_1+L_2:v\mapsto L_1(v)+L_2(v),\qquad \alpha L:v\mapsto \alpha L(v)$$

들도 선형사상이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$v, v_1,v_2\in V$이고, $\alpha\in F$라 하자. 그럼

$$\begin{aligned}
        (L_1+L_2)(v_1+v_2)&=L_1(v_1+v_2)+L_2(v_1+v_2)\\
        &=L_1(v_1)+L_1(v_2)+L_2(v_1)+L_2(v_2)\\
        &=L_1(v_1)+L_2(v_1)+L_1(v_2)+L_2(v_2)\\
        &=(L_1+L_2)(v_1)+(L_1+L_2)(v_2)
    \end{aligned}$$

이고,

$$\begin{aligned}
        (L_1+L_2)(\alpha v)&=L_1(\alpha v)+L_2(\alpha v)=\alpha L_1(v)+\alpha L_2(v)\\
        &=\alpha(L_1(v)+L_2(v))\\
        &=\alpha (L_1+L_2)(v).
    \end{aligned}$$
    
이므로 $L_1+L_2$은 선형사상이 된다. 두 번째 주장도 비슷하게 보일 수 있다.

</details>

따라서, 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 두 $F$-벡터공간 $V,W$에 대하여, $V$에서 $W$로의 모든 선형사상들의 집합에 [명제 2](#pp2)의 연산을 준 $F$-벡터공간을 $\operatorname{Hom}(V,W)$로 적는다. 특별히 $W=F$일 경우, $\operatorname{Hom}(V,F)$를 $V$의 *쌍대공간*이라 부르고 $V^\*$으로 적는다.

</div>

**[Goc]**이나 **[Lee]**나 공통적으로 이 집합은 $\mathcal{L}(V,W)$ 혹은 $\mathfrak{L}(V,W)$으로 쓰는데, 아마도 학부생이 겁먹지 말라는 친절한 배려일 것 같다. $\operatorname{Hom}(V,W)$는 $V$에서 $W$로의 $F$-벡터공간 *homomorphism*들의 집합이라는 뜻인데, 여기서 *homomorphism*(준동형사상)이라는 것은 주어진 대수적 구조[^3]를 보존하는 함수, 우리의 경우에는 선형사상을 의미한다.

그럼 이제, 우리가 찾은 bijection은 $\operatorname{Hom}(F^n, F^m)$과 $\operatorname{Mat}_{m\times n}(F)$ 사이의 bijection이라고 쓸 수 있다. 미뤄뒀던 둘째 질문은 그럼, 이 bijection이 $F$-벡터공간들 사이의 동형사상이냐는 것이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> $\operatorname{Hom}(F^n,F^m)\cong\operatorname{Mat}_{m\times n}(F)$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

말만 거창하지, 사실 증명은 계산 빼면 할 게 없다. 우리는 임의의 $L\in \operatorname{Hom}(F^n,F^m)$에 대하여, $[L]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$를 위와 같이 정의하자. 우리는 이 map $L\mapsto[L]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$가 선형사상임을 보여야 한다.

예를 들어, $L_1,L_2$가 모두 $\operatorname{Hom}(F^n,F^m)$의 원소라 하자. 그럼 각각의 $e_i\in\mathcal{E}_n$에 대하여, 

$$\begin{aligned}L_1(e_1)&=\alpha_{1,1}e_1+\alpha_{2,1}e_2+\cdots+\alpha_{m,1}e_m\\L_1(e_2)&=\alpha_{1,2}e_1+\alpha_{2,2}e_2+\cdots+\alpha_{m,2}e_m\\&\vdots\\L_1(e_n)&=\alpha_{1,n}e_1+\alpha_{2,n}e_2+\cdots+\alpha_{m,n}e_m\end{aligned}$$

그리고

$$\begin{aligned}L_2(e_1)&=\beta_{1,1}e_1+\beta_{2,1}e_2+\cdots+\beta_{m,1}e_m\\L_2(e_2)&=\beta_{1,2}e_1+\beta_{2,2}e_2+\cdots+\beta_{m,2}e_m\\&\vdots\\L_2(e_n)&=\beta_{1,n}e_1+\beta_{2,n}e_2+\cdots+\beta_{m,n}e_m\end{aligned}$$

이도록 하는 스칼라들의 family $(\alpha_{i,j})$, $(\beta_{i,j})$들이 존재한다. 이제, 

$$\begin{aligned}(L_1+L_2)(e_1)&=(\alpha_{1,1}+\beta_{1,1})e_1+(\alpha_{2,1}+\beta_{2,1})e_2+\cdots+(\alpha_{m,1}+\beta_{m,1})e_m\\(L_1+L_2)(e_2)&=(\alpha_{1,2}+\beta_{1,2})e_1+(\alpha_{2,2}+\beta_{2,2})e_2+\cdots+(\alpha_{m,2}+\beta_{m,2})e_m\\&\vdots\\(L_1+L_2)(e_n)&=(\alpha_{1,n}+\beta_{1,n})e_1+(\alpha_{2,n}+\beta_{2,n})e_2+\cdots+(\alpha_{m,n}+\beta_{m,n})e_m\end{aligned}$$

일 것이고, 따라서 $L_1+L_2$의 행렬표현 $[L\_1+L\_2]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$은 정확히 $[L\_1]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}+[L\_2]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$이 된다. 이와 유사하게 스칼라곱에 대한 것도 성립한다.

</details>

물론 전혀 다르게 생긴 두 공간 $\operatorname{Hom}(F^n,F^m)$와 $\operatorname{Mat}_{m\times n}(F)$가 동형이라는 것은 신기한 일이지만, 고작 이 정도로 기본정리이라고 부르기에는 조금 부족하다. 보통은 위의 정리와 아래의 정리 (첫 번째 질문에 대한 답) 을 합쳐 선형대수학의 기본정리라 부른다. 

> 우선 작은 관찰 하나: 식 (1)의 $(v_1\;v_2\;\cdots\;v_n)^t$ 자리에 표준기저 $e_1,\ldots, e_n$을 넣으면, 그 결과는 각각 
> 
> $$\begin{pmatrix}\alpha_{1,1}\\\alpha_{2,1}\\\vdots\\\alpha_{m,1}\end{pmatrix},\quad \begin{pmatrix}\alpha_{1,2}\\\alpha_{2,2}\\\vdots\\\alpha_{m,2}\end{pmatrix},\quad \begin{pmatrix}\alpha_{1,n}\\\alpha_{2,n}\\\vdots\\\alpha_{m,n}\end{pmatrix}$$
> 
> 이 나온다. 즉, 주어진 행렬 $A$에 대하여 $L_A$는 $F^n$의 기저 $e_i$를 $A_i$ ($A_i$는 $A$의 $i$번째 column)으로 보내는 선형사상이며, 거꾸로 만일 선형사상 $L$이 $e_i$들을 각각 $A_i=(\alpha\_{1,i}\;\alpha\_{2,i}\;\cdots\;\alpha\_{m,i})^t$로 보낸다면, $[L]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$은 다음의 행렬
> 
> $$A=(A_1|A_2|\cdots|A_n)$$
> 
> 으로 주어진다.


<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 세 개의 유클리드 공간들 $F^n,F^m,F^k$가 주어졌다 하자. 그럼 임의의 $L\_1:F^n\rightarrow F^m$, $L\_2:F^m\rightarrow F^k$에 대하여 항상

$$[L_2\circ L_1]^{\mathcal{E}_n}_{\mathcal{E}_k}=[L_2]^{\mathcal{E}_m}_{\mathcal{E}_k}[L_1]^{\mathcal{E}_n}_{\mathcal{E}_m}$$

이 성립한다. 즉, 선형사상의 합성은 행렬의 곱과 같다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 관찰에 의하여, 좌변의 $[L_2\circ L_1]^{\mathcal{E}\_n}\_{\mathcal{E}\_k}$을 결정하기 위해서는 $L_2\circ L_1$에 의해 $\mathcal{E}\_n$의 원소 $e_i$들이 어디로 옮겨지는지만 확인하면 된다. $L_1$, $L_2$가 다음의 식

$$[L_1]^{\mathcal{E}_n}_{\mathcal{E}_m}=\begin{pmatrix}\alpha_{1,1}&\alpha_{1,2}&\cdots&\alpha_{1,n}\\\alpha_{2,1}&\alpha_{2,2}&\cdots&\alpha_{2,n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m,1}&\alpha_{m,2}&\cdots&\alpha_{m,n}\end{pmatrix},\quad[L_2]^{\mathcal{E}_m}_{\mathcal{E}_k}=\begin{pmatrix}\beta_{1,1}&\beta_{1,2}&\cdots&\beta_{1,m}\\\beta_{2,1}&\beta_{2,2}&\cdots&\beta_{2,m}\\\vdots&\vdots&\ddots&\vdots\\\beta_{k,1}&\beta_{k,2}&\cdots&\beta_{k,m}\end{pmatrix}$$

으로 주어졌다 하자. 약간의 계산을 하면,

$$\begin{aligned}(L_2\circ L_1)(e_i)&=L_2(\alpha_{1,i}e_1+\cdots+\alpha_{m,i}e_m)\\&=\alpha_{1,i}L_2(e_1)+\alpha_{2,i}L_2(e_2)+\cdots+\alpha_{m,i}L(e_m)\\&=\alpha_{1,i}(\beta_{1,1}e_1+\beta_{2,1}e_2+\cdots+\beta_{k,1}e_k)\\&\phantom{==}+\alpha_{2,i}(\beta_{1,2}e_1+\beta_{2,2}e_2+\cdots+\beta_{k,2}e_k)\\&\phantom{===}+\cdots\\&\phantom{====}+\alpha_{m,i}(\beta_{1,m}e_1+\beta_{2,m}e_2+\cdots+\beta_{k,m}e_k)\end{aligned}$$

이제, 위 식을 기저 $e_1,\ldots, e_k$들끼리 묶으면, 

$$(L_2\circ L_1)(e_i)=\left(\sum_{l=1}^m\alpha_{l,i}\beta_{1,l}\right)e_1+\cdots+\left(\sum_{l=1}^m\alpha_{l,i}\beta_{k,l}\right)e_k.$$

앞서 우리는 $[L\_2\circ L\_1]^{\mathcal{E}\_n}\_{\mathcal{E}\_k}$의 $i$번째 열은 정확히 $e_i$가 $L_2\circ L_1$에 의해 옮겨지는 벡터라는 것을 확인했으므로, 행렬 $[L\_2\circ L\_1]^{\mathcal{E}\_n}\_{\mathcal{E}\_k}$의 $i$열, $j$행은 이 벡터의 $j$번째 성분 $\sum\_{l=1}^m\alpha_{l,i}\beta_{j,l}$이 된다. 그런데, 행렬의 곱을 정의할 때 썼던 식 ([§선형사상과 행렬표현, 정의 6](/ko/math/linear_algebra/matrix#df6))

> $BA=(BA_1\|BA_2\|\cdots\|BA_n)$, 이 때 $BA_i$의 $j$번째 성분은
> 
> $$\sum_{l=1}^m A_{l,i}B_{j,l}.\tag{2}$$
>

을 떠올리면 이 값은 정확히 행렬곱 $[L\_2]^{\mathcal{E}\_m}\_{\mathcal{E}\_k}[L\_1]^{\mathcal{E}\_n}\_{\mathcal{E}\_m}$의 $i$열, $j$행 성분이고, 따라서 증명 끝.

</details>

## 기본정리: 일반적인 경우

앞서 우리가 증명한 기본정리는 유클리드 공간에 대해서만 적용되지만, 아주 작은 수정만 있으면 일반적인 유한차원 $F$-벡터공간에 대해서도 성립한다. 사실 이 작은 수정사항은 우리가 이미 다뤘지만 유클리드 공간의 경우에 집중하느라 일부러 무시한 것에 가깝다.

우리가 무시했던 것은 바로, 임의의 $n$차원 $F$-벡터공간 $V$는 $F^n$과 자연스럽게 동형이라는 것이다. 이를 위해서는 기저 $\mathcal{B}$의 선택이 필요한데, 기저 $\mathcal{B}=\\{x_1,\ldots, x_n\\}$이 주어진다면 선형사상 $v\mapsto [v]\_\mathcal{B}$가 $V$에서 $F^n$으로의 동형사상을 정의한다. 뿐만 아니라, 위의 [Review](#review)에서의 행렬표현 또한 일반적인 $F$-벡터공간 $V$와 $W$에 대해[^4] 서술되어 있었다. $\operatorname{Hom}$을 일반적인 $F$-벡터공간 $V$와 $W$에 대해 정의했음은 물론이다. 

그러므로 일반적인 경우를 다루는 우리의 두 가지 도구는 임의의 $F$-벡터공간 $V$와 그 기저 $\mathcal{B}=\\{x_1,\ldots, x_n\\}$에 대해 정의된 *좌표표현*

$$v=\sum_{i=1}^n v_ix_i\mapsto [v]_\mathcal{B}=\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix}\in F^n$$

그리고, 또 다른 $F$-벡터공간 $W$, 기저 $\mathcal{C}=\\{y_1,\ldots, y_m\\}$, 그리고 다음의 식들

$$\begin{aligned}L(x_1)&=\alpha_{1,1}y_1+\alpha_{2,1}y_2+\cdots+\alpha_{m,1}y_m\\L(x_2)&=\alpha_{1,2}y_1+\alpha_{2,2}y_2+\cdots+\alpha_{m,2}y_m\\&\vdots\\L(x_n)&=\alpha_{1,n}y_1+\alpha_{2,n}y_2+\cdots+\alpha_{m,n}y_m\end{aligned}$$

에 의해 유일하게 결정되는 선형사상 $L$에 대해 정의된 $L$의 $\mathcal{B},\mathcal{C}$에 대해 정의된 *행렬표현*

$$[L]^\mathcal{B}_\mathcal{C}=\begin{pmatrix}\alpha_{1,1}&\alpha_{1,2}&\cdots&\alpha_{1,n}\\\alpha_{2,1}&\alpha_{2,2}&\cdots&\alpha_{2,n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m,1}&\alpha_{m,2}&\cdots&\alpha_{m,n}\end{pmatrix}$$

이다. 행렬표현 $[L]^\mathcal{B}_\mathcal{C}$는 단순히 $L$을 행렬로 표현한 것 뿐만 아니라, 식 (1)을 생각하면 이 표현은 실제로 $L$의 값을 계산하는 데에 도움을 준다. 즉, 만일 $v\in V$라면, $L(v)$의 기저 $\mathcal{C}$ 상에서의 행렬표현은 다음의 식

$$[L(v)]_\mathcal{C}=[L]^\mathcal{B}_\mathcal{C}[v]_\mathcal{B}\tag{3}$$

으로 주어진다.

그럼 [정리 4](#thm4)에 대한 일반적인 버전은 다음의 정리로 주어진다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> $\operatorname{Hom}(V,W)\cong \operatorname{Mat}_{m\times n}(F)$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$V$, $W$의 기저 $\mathcal{B}$, $\mathcal{C}$를 각각 고정하자. 임의의 $L\in \operatorname{Hom}(V,W)$에 대하여, map $L\mapsto[L]^\mathcal{B}\_\mathcal{C}$가 선형사상임을 보여야 한다.

예를 들어, $L_1,L_2$가 모두 $\operatorname{Hom}(V,W)$의 원소라 하자. 그럼 각각의 $x_i\in\mathcal{B}$에 대하여, 

$$\begin{aligned}L_1(x_1)&=\alpha_{1,1}y_1+\alpha_{2,1}y_2+\cdots+\alpha_{m,1}y_m\\L_1(x_2)&=\alpha_{1,2}y_1+\alpha_{2,2}y_2+\cdots+\alpha_{m,2}y_m\\&\vdots\\L_1(x_n)&=\alpha_{1,n}y_1+\alpha_{2,n}y_2+\cdots+\alpha_{m,n}y_m\end{aligned}$$

그리고

$$\begin{aligned}L_2(x_1)&=\beta_{1,1}y_1+\beta_{2,1}y_2+\cdots+\beta_{m,1}y_m\\L_2(x_2)&=\beta_{1,2}y_1+\beta_{2,2}y_2+\cdots+\beta_{m,2}y_m\\&\vdots\\L_2(x_n)&=\beta_{1,n}y_1+\beta_{2,n}y_2+\cdots+\beta_{m,n}y_m\end{aligned}$$

이도록 하는 스칼라들의 family $(\alpha_{i,j})$, $(\beta_{i,j})$들이 존재한다. 이제, 

$$\begin{aligned}(L_1+L_2)(x_1)&=(\alpha_{1,1}+\beta_{1,1})y_1+(\alpha_{2,1}+\beta_{2,1})y_2+\cdots+(\alpha_{m,1}+\beta_{m,1})y_m\\(L_1+L_2)(x_2)&=(\alpha_{1,2}+\beta_{1,2})y_1+(\alpha_{2,2}+\beta_{2,2})y_2+\cdots+(\alpha_{m,2}+\beta_{m,2})y_m\\&\vdots\\(L_1+L_2)(x_n)&=(\alpha_{1,n}+\beta_{1,n})y_1+(\alpha_{2,n}+\beta_{2,n})y_2+\cdots+(\alpha_{m,n}+\beta_{m,n})y_m\end{aligned}$$

일 것이고, 따라서 $L_1+L_2$의 행렬표현 $[L\_1+L\_2]^\mathcal{B}\_\mathcal{C}$은 정확히 $[L\_1]^\mathcal{B}\_\mathcal{C}+[L\_2]^\mathcal{B}\_\mathcal{C}$이 된다. 이와 유사하게 스칼라곱에 대한 것도 성립한다.

</details>

[정리 5](#thm5)의 analogue를 증명하기 전에 우리는 *작은 관찰*을 하나 했었는데, 이 관찰의 일반적인 버전은 다음과 같다. 

> 식 (3)에서, $v$가 $x_i$일 경우 $[v]_\mathcal{B}=e_i$이므로, 
> 
> $$[L(x_i)]_\mathcal{C}=[L]^\mathcal{B}_\mathcal{C}[v]_\mathcal{B}=[L]^\mathcal{B}_\mathcal{C}e_i$$
> 
> 이고, 우변의 식은 정확히 행렬 $[L]^\mathcal{B}_\mathcal{C}$의 $i$번째 열이다. 따라서, 만일 기저 $\mathcal{B}\_1=\\{x_1,\ldots, x_n\\}$들이 선형사상 $L$을 통해 (basis $\mathcal{B}\_2=\\{y_1,\ldots, y_m\\}$이 고정된 상태에서) 다음 $n$개의 벡터들
> 
> $$A_1=\begin{pmatrix}\alpha_{1,1}\\ \alpha_{2,1}\\ \vdots\\ \alpha_{m,1}\end{pmatrix},\quad A_2=\begin{pmatrix}\alpha_{1,2}\\ \alpha_{2,2}\\ \vdots\\ \alpha_{m,2}\end{pmatrix},\quad\cdots,\quad A_n=\begin{pmatrix}\alpha_{1,n}\\ \alpha_{2,n}\\ \vdots\\ \alpha_{m,n}\end{pmatrix},$$
> 
> 로 옮겨진다면, 이 선형사상 $L$의 행렬표현 $[L]^{\mathcal{B}\_1}\_{\mathcal{B}\_2}$은 다음의 식
> 
> $$(A_1|A_2|\cdots|A_n)$$
> 
> 으로 주어진다. 

이제 다음을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 세 개의 $F$-벡터공간 $V\_1,V\_2,V\_3$와 이들 각각의 basis $\mathcal{B}\_1=\\{x_1,\ldots,x_n\\}$, $\mathcal{B}\_2=\\{y_1,\ldots, y_m\\}$, $\mathcal{B}\_3=\\{z_1,\ldots, z_k\\}$가 주어졌다 하자. 그럼 임의의 $L\_1:V\_1\rightarrow V\_2$, $L\_2:V\_2\rightarrow V\_3$에 대하여 항상

$$[L_2\circ L_1]^{\mathcal{B}_1}_{\mathcal{B}_3}=[L_2]^{\mathcal{B}_2}_{\mathcal{B}_3}[L_1]^{\mathcal{B}_1}_{\mathcal{B}_2}$$

이 성립한다. 즉, 선형사상의 합성은 행렬의 곱과 같다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 관찰에 의하여, 좌변의 $[L_2\circ L_1]^{\mathcal{B}\_1}\_{\mathcal{B}\_3}$을 결정하기 위해서는 $L_2\circ L_1$에 의해 $\mathcal{B}\_1$의 원소들이 어디로 옮겨지는지만 확인하면 된다. $L_1$, $L_2$가 다음의 식

$$[L_1]^{\mathcal{B}_1}_{\mathcal{B}_2}=\begin{pmatrix}\alpha_{1,1}&\alpha_{1,2}&\cdots&\alpha_{1,n}\\\alpha_{2,1}&\alpha_{2,2}&\cdots&\alpha_{2,n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m,1}&\alpha_{m,2}&\cdots&\alpha_{m,n}\end{pmatrix},\quad[L_2]^{\mathcal{B}_2}_{\mathcal{B}_3}=\begin{pmatrix}\beta_{1,1}&\beta_{1,2}&\cdots&\beta_{1,m}\\\beta_{2,1}&\beta_{2,2}&\cdots&\beta_{2,m}\\\vdots&\vdots&\ddots&\vdots\\\beta_{k,1}&\beta_{k,2}&\cdots&\beta_{k,m}\end{pmatrix}$$

으로 주어졌다 하자. 약간의 계산을 하면,

$$\begin{aligned}(L_2\circ L_1)(x_i)&=L_2(\alpha_{1,i}y_1+\cdots+\alpha_{m,i}y_m)\\&=\alpha_{1,i}L_2(y_1)+\alpha_{2,i}L_2(y_2)+\cdots+\alpha_{m,i}L(y_m)\\&=\alpha_{1,i}(\beta_{1,1}z_1+\beta_{2,1}z_2+\cdots+\beta_{k,1}z_k)\\&\phantom{==}+\alpha_{2,i}(\beta_{1,2}z_1+\beta_{2,2}z_2+\cdots+\beta_{k,2}z_k)\\&\phantom{===}+\cdots\\&\phantom{====}+\alpha_{m,i}(\beta_{1,m}z_1+\beta_{2,m}z_2+\cdots+\beta_{k,m}z_k)\end{aligned}$$

이제, 위 식을 $z$들끼리 묶으면, 

$$(L_2\circ L_1)(x_i)=\left(\sum_{l=1}^m\alpha_{l,i}\beta_{1,l}\right)z_1+\cdots+\left(\sum_{l=1}^m\alpha_{l,i}\beta_{k,l}\right)z_k$$

앞서 우리는 $[L\_2\circ L\_1]^{\mathcal{B}\_1}\_{\mathcal{B}\_3}$의 $i$번째 열은 정확히 $x_i$가 $L_2\circ L_1$이 옮겨지는 벡터의 $\mathcal{B}\_3$에서의 좌표표현이라는 것을 확인했으므로, 행렬 $[L\_2\circ L\_1]^{\mathcal{B}\_1}\_{\mathcal{B}\_3}$의 $i$열, $j$행은 이 벡터의 $j$번째 성분 $\sum\_{l=1}^m\alpha_{l,i}\beta_{j,l}$이 된다. 그런데, 행렬의 곱을 정의할 때 썼던 식 (2)를 떠올리면 이 값은 정확히 행렬곱 $[L\_2]^{\mathcal{B}\_2}\_{\mathcal{B}\_3}[L\_1]^{\mathcal{B}\_1}\_{\mathcal{B}\_2}$의 $i$열, $j$행 성분이고, 따라서 증명 끝.

</details>

우리가 명심해야 할 것은, 행렬표현은 기저의 선택에 아주 강하게 의존한다는 것이다. 기저가 바뀌면, 하다못해 기저의 원소들이 배열된 순서가 바뀌더라도 행렬표현은 달라질 수 있다. 

어쨌든, 위 정리의 쓸만한 따름정리는 다음과 같다.

<div class="proposition" markdown="1">

<ins id="crl8">**따름정리 8**</ins> 두 $n$차원 $F$-벡터공간 $V,W$가 주어졌다 하고, 이들의 기저 $\mathcal{B},\mathcal{C}$를 고정하자. 그럼 임의의 $L\in\operatorname{Hom}(V,W)$에 대하여, $L^{-1}\in\operatorname{Hom}(W,V)$의 기저 $\mathcal{C},\mathcal{B}$에 대한 행렬표현 $[L^{-1}]^{\mathcal{C}}\_{\mathcal{B}}$은 행렬 $[L]^{\mathcal{B}}\_\mathcal{C}$의 역행렬과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

역행렬과 역함수의 유일성에 의하여 자명.

</details>

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 잠시 앞선 두 개의 section을 비교해보면, 일반적인 경우를 증명할 때 우리가 먼저 증명한 유클리드 공간의 경우는 전혀 사용되지 않았다는 것을 확인할 수 있다. 즉 만일 유클리드 공간에 대한 이야기없이 일반적인 경우부터 시작하더라도 (motivation은 부족하겠지만) 별다른 문제 없이 진행할 수 있었을 것이란 뜻이다. 이 경우, 유클리드 공간의 경우는 일반적인 경우의 특수한 경우가 된다.[^5] 그렇다면 왜 굳이 이 두 경우를 나눈 것일까?

Category theory를 동원하면, 일반적인 경우가 유클리드 공간에서의 기본정리의 아주 자연스러운 일반화라는 것을 보일 수 있다. 이 사실을 **[Lee]**에서는 **우리의 철학**이라는 이름으로 설명하고 있는데, 아무래도 이를 직접적으로 언급하지 않으려고 하다보니 내용이 조금 두루뭉술한 느낌을 지울 수 없다. 그래서 아예 본문에 이 내용을 추가하는 것은 포기하고, 대신 [새로운 글](/ko/math/linear_algebra/ftla_categorical_viewpoint)을 적었다.

</div>

## 기저변환행렬

우리는 앞서 행렬과 선형사상이 같은 것이라는 사실을 살펴봤다. 하지만 이 명제에는 약간 주의할 것이 있는데, 이는 이 둘 사이를 자유롭게 돌아다니기 위해서는 기저의 선택이 필연적이라는 사실이다. 일반적으로, 선형사상은 벡터공간 간의 함수이기 때문에 이를 정의할 때 기저에 대한 이야기를 전혀 하지 않아도 좋지만, 이를 행렬로 나타내는 순간 기저를 하나 고정해주어야 한다. 

예를 들어 어떤 선형사상 $L:V\rightarrow W$가 주어졌다 하자. 추가적으로 만족해야 할 성질들이 있긴 하지만, 본질적으로 $L$은 집합 $V$에서 집합 $W$로의 함수이고, 함수로써 각각의 원소 $v\in V$마다 함숫값 $L(v)$를 대응시켜 준다. 이렇게 정의된 선형사상 $L$에게 $V$의 기저는 전혀 중요한 정보가 아니다. $V$에 기저의 선택이 주어져있지 않더라도 $L$은 $v$를 $L(v)$로 보낼 것이고, $V$의 기저로 $\mathcal{B}$를 택하더라도, 혹은 $\mathcal{C}$를 택하더라도 $L$은 여전히 $v$를 $L(v)$로 보낼 것이다. 그러나 $L$의 행렬표현의 경우, $V$에 기저의 선택이 주어져있지 않으면 애초부터 행렬표현이 불가능하고, 기저를 어떻게 택하느냐에 따라 그 표현 또한 달라진다. 

비슷하게 $L$이 동형사상이라는 성질 또한 기저의 선택과는 전혀 무관한 성질이라는 것을 확인할 수 있다. 선형사상 $L$이 동형사상이 되기 위한 필요충분조건은 집합간의 함수로써 $L$이 bijection이 된다는 것임을 이미 증명했기 때문이다. ([§선형사상, 보조정리 17](/ko/math/linear_algebra/linear_map#lem17), 물론, 이것이 가능하기 위해서는 $\dim V=\dim W$가 성립해야 한다.) 그런데 [따름정리 8](/ko/math/linear_algebra/ftla#crl8)에 따르면, 선형사상 $L$이 역함수를 갖는다면 행렬 $[L]^\mathcal{B}\_\mathcal{C}$ 또한 역행렬을 갖는다. 이 말은 즉 선형사상 $L$이 역함수를 갖기만 한다면 *기저를 어떻게 택하더라도* 그 행렬표현 또한 역행렬을 갖는다는 이야기가 된다. 따라서, 같은 선형사상의 다른 기저선택으로 얻어진 두 행렬  $[L]^\mathcal{B}\_\mathcal{C}$과 $[L]^{\mathcal{B}'}\_{\mathcal{C}'}$은 전혀 달라보이지만 $L$로부터 얻어지는 공통적인 어떤 성질은 유지하고 있어야 한다.

이러한 상황은 change of basis, 즉 기저변환을 나타내는 행렬을 생각하면 쉽게 해결할 수 있다. 잠시 벡터공간이라는 대상을 우리가 알고 있는 벡터공간 $V$와, 여기에 더해 $V$의 기저 $\mathcal{B}$까지 주어진 대상이라 생각하자. 즉 이 절의 논의에서 벡터공간이라는 것은 $(V,\mathcal{B})$를 뜻하며, 만일 $V$에 대한 기저 $\mathcal{C}$를 택했다면 그렇게 얻어지는 공간 $(V,\mathcal{C})$는 $(V,\mathcal{B})$와는 다른 공간이다.

 <div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 벡터공간 $V$와, $V$의 두 기저 $\mathcal{B}_1$, $\mathcal{B}_2$가 주어졌다 하자. $V$에서 $V$로의 항등함수 $\operatorname{id}_V$에 대하여, 행렬 $[\operatorname{id}\_V]^{\mathcal{B}\_1}\_{\mathcal{B}\_2}$를 기저 $\mathcal{B}_1$에서 기저 $\mathcal{B}_2$로의 *기저변환행렬*이라 부른다.

</div>

$\mathcal{B}\_1$과 $\mathcal{B}\_2$는 반드시 같은 수의 원소를 가져야 하므로, 기저변환행렬은 반드시 정사각행렬이다. 또, 만일 두 기저 $\mathcal{B}_1$과 $\mathcal{B}_2$가 동일하다면 기저변환행렬은 정확히 항등행렬 $I$가 되어야 한다는 것을 쉽게 확인할 수 있다.

임의의 선형사상 $L:V\rightarrow W$이 주어졌다 하자. $V$에 두 개의 기저 $\mathcal{B}\_1$, $\mathcal{B}\_2$, 그리고 $W$에 두 개의 기저 $\mathcal{C}\_1$, $\mathcal{C}\_2$가 주어졌다 하고, 두 개의 행렬표현 $[L]^{\mathcal{B}\_1}\_{\mathcal{C}\_1}$와 $[L]^{\mathcal{B}\_2}\_{\mathcal{C}\_2}$를 생각할 수 있다. 그럼 다음의 식

$$[L]_{\mathcal{C}_2}^{\mathcal{B}_2}=[\operatorname{id}_W]_{\mathcal{C}_2}^{\mathcal{C}_1}[L]_{\mathcal{C}_1}^{\mathcal{B}_1}[\operatorname{id}_V]_{\mathcal{B}_1}^{\mathcal{B}_2}$$

이 성립한다는 것이 선형대수학의 기본정리로부터 자명하다. 따라서 만일 임의의 기저변환행렬이 역행렬을 갖는다는 사실을 알게 된다면, 위에서 이야기한 명제

> 하나의 행렬표현 $[L]\_{\mathcal{C}\_1}^{\mathcal{B}\_1}$가 역행렬을 가지면, 다른 임의의 행렬표현 $[L]\_{\mathcal{C}\_2}^{\mathcal{B}\_2}$또한 역행렬을 갖는다.

를 증명할 수 있다. $[L]\_{\mathcal{C}\_2}^{\mathcal{B}\_2}$은 역행렬을 갖는 세 개의 행렬 $[\operatorname{id}\_W]\_{\mathcal{C}\_2}^{\mathcal{C}\_1}$, $[L]\_{\mathcal{C}\_1}^{\mathcal{B}\_1}$, $[\operatorname{id}\_V]\_{\mathcal{B}\_1}^{\mathcal{B}\_2}$의 곱이기 때문이다. 그런데 임의의 벡터공간 $V$와 두 기저 $\mathcal{B}_1$, $\mathcal{B}_2$에 대해 기저변환행렬이 반드시 역행렬을 갖는다는 것은 다음의 식

$$I=[\operatorname{id}_V]_{\mathcal{B}_1}^{\mathcal{B}_2}[\operatorname{id}_V]_{\mathcal{B}_2}^{\mathcal{B}_1}=[\operatorname{id}_V]_{\mathcal{B}_2}^{\mathcal{B}_1}[\operatorname{id}_V]_{\mathcal{B}_1}^{\mathcal{B}_2}$$

으로부터 자명하므로, 임의의 선형사상에 대한 행렬표현의 가역성(invertiblity)은 기저의 선택에 무관하다는 것을 다시 한 번 확인할 수 있다. 


---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---

[^1]: 물론 $\mathcal{E}_n$의 $e_1$과, $\mathcal{E}_m$의 $e_1$은 서로 다른 벡터이지만, 혼동될 일은 별로 없을 것이다.
[^2]: 이 함수는 $0,1,2,3,4,\ldots$를 $0,-1,1,-2,2,\ldots$으로 보내주는 함수이다.
[^3]: 첫 글에서 잠깐 언급한 군이나 체, 우리가 다루고 있는 벡터공간 등.
[^4]: 물론, 기저 $\mathcal{B}$와 $\mathcal{C}$의 선택이 전제된.
[^5]: 이 글을 처음 쓰기 시작할 때만 하더라도 유클리드 공간의 경우는 따로 서술되어 있지 않았고, 사실 지금도 유클리드 공간은 일반적인 경우에 썼던 것을 거의 복붙해놓은 수준이다.
