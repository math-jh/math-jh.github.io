---
title: "Serre 관계식"
description: "Cartan matrix로부터 generator e_i, f_i, h_i와 Serre 관계식으로 정의되는 Lie algebra g(A)를 free Lie algebra의 몫으로 구성하고, finite type Cartan matrix에 대해 g(A)가 유한차원 semisimple Lie algebra임을 주장하는 Serre 정리를 서술한다. 이로써 Cartan matrix와 유한차원 semisimple Lie algebra 사이의 분류가 완성됨을 보이고 Chevalley basis를 언급한다."
excerpt: "Chevalley–Serre presentation, Serre 관계식, g(A), Serre 정리, Cartan matrix ↔ semisimple Lie algebra 분류"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/serre_relations
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 7.5

published: false
---

유한차원 semisimple Lie algebra $$\mathfrak{g}$$는 Cartan subalgebra $$\mathfrak{h}$$를 고정할 때 root system $$\Phi$$를 낳고, simple root들을 택하면 $$\Phi$$의 모든 정보가 Cartan matrix $$A=(a_{ij})$$ 하나로 압축된다 ([§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)). 자연스러운 물음은 그 역방향이다. 즉 Cartan matrix $$A$$만이 주어졌을 때, 그것을 root system으로 갖는 Lie algebra를 $$A$$로부터 직접 재구성할 수 있는가. 각 simple root $$\alpha_i$$가 $$\mathfrak{g}$$ 안에 $$\sl_2$$와 동형인 부분대수 $$\langle e_i,f_i,h_i\rangle$$를 만들어내고, 서로 다른 두 simple root에 딸린 이 $$\sl_2$$들이 Cartan matrix가 지정하는 방식으로 얽힌다는 사실을 떠올리면, 이 얽힘을 generator와 relation으로 옮겨 적는 것이 답이 된다. 이 글에서 우리는 Cartan matrix $$A$$로부터 generator $$e_i,f_i,h_i$$와 *Serre 관계식*으로 표시되는 Lie algebra $$\mathfrak{g}(A)$$를 정의하고, $$A$$가 finite type일 때 $$\mathfrak{g}(A)$$가 정확히 그 Cartan matrix를 갖는 유한차원 semisimple Lie algebra임을, 그리고 모든 유한차원 semisimple Lie algebra가 이렇게 표시됨을 주장하는 Serre 정리를 서술한다. 이로써 Cartan matrix와 유한차원 semisimple Lie algebra 사이의 분류가 완결된다.

이 글 전체에서 $$k$$는 대수적으로 닫힌 표수 $$0$$의 체이고, Lie algebra는 별다른 언급이 없는 한 $$k$$ 위에서 생각한다. Cartan matrix·root system·simple root·Killing form 등은 앞선 글들에서 정의한 그대로 사용하며 ([§근계, ⁋정의 9](/ko/math/lie_theory/root_systems#def9), [§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)), 보편 포락 대수와 그 안에서의 $$\ad$$ 작용에 대한 표기는 ([§보편 포락 대수, ⁋정의 2](/ko/math/lie_theory/universal_enveloping_algebra#def2))를 따른다.

## Cartan matrix와 그 type

먼저 출발점이 되는 행렬의 부류를 정리한다. Root system에서 얻은 Cartan matrix는 정수성과 대각성분 조건을 만족하였는데 ([§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16) 이후의 논의), 추상적으로는 다음 조건을 만족하는 행렬을 generalized Cartan matrix라 부른다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 정수 성분 정방행렬 $$A=(a_{ij})_{1\leq i,j\leq\ell}$$가 *generalized Cartan matrix<sub>일반화 카르탕 행렬</sub>*라는 것은 다음 세 조건을 만족하는 것이다.

1. 모든 $$i$$에 대하여 $$a_{ii}=2$$이다.
2. $$i\neq j$$이면 $$a_{ij}\leq 0$$이다.
3. $$a_{ij}=0$$인 것과 $$a_{ji}=0$$인 것이 동치이다.

나아가 $$A$$가 *finite type<sub>유한형</sub>*이라는 것은, 양의 대각행렬 $$D=\operatorname{diag}(d_1,\ldots,d_\ell)$$가 존재하여 $$DA$$가 symmetric이고 positive definite가 되도록 할 수 있는 것이다.

</div>

세 조건은 root system의 Cartan matrix가 만족하던 성질을 그대로 옮긴 것이다. 실제로 $$a_{ij}=\langle\alpha_i,\alpha_j\rangle=2(\alpha_i,\alpha_j)/(\alpha_j,\alpha_j)$$이므로 $$a_{ii}=2$$이고, 서로 다른 simple root는 둔각을 이루어 $$(\alpha_i,\alpha_j)\leq 0$$이므로 $$a_{ij}\leq 0$$이며, $$a_{ij}=0$$은 $$(\alpha_i,\alpha_j)=0$$과 동치이므로 $$a_{ji}=0$$과 동치이다. Finite type 조건의 $$D$$는 $$d_i=(\alpha_i,\alpha_i)/2$$로 택하면 $$(DA)_{ij}=(\alpha_i,\alpha_j)$$가 되어 inner product의 Gram 행렬, 곧 symmetric positive definite가 된다. 따라서 유한차원 semisimple Lie algebra에서 얻은 Cartan matrix는 항상 finite type이다. 이 글에서 우리가 관심을 두는 것은 정확히 이 finite type의 경우이며, generalized Cartan matrix를 도입한 것은 $$\mathfrak{g}(A)$$의 정의가 finite type 여부와 무관하게 똑같이 작동함을 분명히 하기 위함이다.

<div class="remark" markdown="1">

<ins id="rmk2">**참고 2**</ins> Finite type이 아닌 generalized Cartan matrix에 대해서도 아래 [정의 3](#def3)의 표시는 그대로 의미를 가지며, 이때 얻어지는 $$\mathfrak{g}(A)$$는 일반적으로 무한차원인 Kac–Moody algebra이다. 우리는 finite type만을 다루므로 그 경우의 $$\mathfrak{g}(A)$$가 유한차원 semisimple임을 [정리 7](#thm7)에서 서술하는 데 집중한다.

</div>

## Lie algebra $$\mathfrak{g}(A)$$의 정의

이제 generator와 relation으로 Lie algebra를 구성한다. 자유 대상의 몫이라는 점에서 보편 포락 대수의 구성 ([§보편 포락 대수, ⁋정의 2](/ko/math/lie_theory/universal_enveloping_algebra#def2))과 형식이 같으나, 여기에서는 결합대수가 아니라 Lie algebra 단계에서 몫을 취한다. 집합 $$X=\{e_i,f_i,h_i\mid 1\leq i\leq\ell\}$$ 위의 *free Lie algebra<sub>자유 리 대수</sub>* $$\mathfrak{F}(X)$$를, $$X$$로부터 임의의 Lie algebra로 가는 모든 집합 사상이 유일한 Lie algebra 준동형으로 확장되는 보편 대상으로 둔다. 구체적으로는 $$X$$ 위의 free vector space의 텐서대수 $$\T(X)$$ 안에서 $$X$$로 생성되는 가장 작은 Lie 부분대수가 $$\mathfrak{F}(X)$$이며, 그 보편 성질은 텐서대수의 보편 성질 ([§보편 포락 대수, ⁋명제 4](/ko/math/lie_theory/universal_enveloping_algebra#prop4))을 commutator Lie 구조로 제한한 것으로 얻어진다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Generalized Cartan matrix $$A=(a_{ij})_{1\leq i,j\leq\ell}$$에 대하여, 기호들 $$e_i,f_i,h_i$$ ($$1\leq i\leq\ell$$) 위의 free Lie algebra $$\mathfrak{F}$$를 생각하고, 다음 관계식들로 생성되는 ideal $$\mathfrak{R}\subseteq\mathfrak{F}$$를 둔다.

$$[h_i,h_j]=0,\qquad [h_i,e_j]=a_{ji}e_j,\qquad [h_i,f_j]=-a_{ji}f_j,\qquad [e_i,f_j]=\delta_{ij}h_i,$$

$$(\ad e_i)^{\,1-a_{ji}}e_j=0\quad(i\neq j),\qquad (\ad f_i)^{\,1-a_{ji}}f_j=0\quad(i\neq j).$$

몫 Lie algebra

$$\mathfrak{g}(A)=\mathfrak{F}/\mathfrak{R}$$

를 Cartan matrix $$A$$에 딸린 *Chevalley–Serre presentation*으로 표시되는 Lie algebra라 부르고, 위 관계식들을 *Serre 관계식<sub>Serre relations</sub>*이라 부른다. 마지막 두 줄의 관계식, 곧 $$i\neq j$$에 대한 $$(\ad e_i)^{1-a_{ji}}e_j=0$$과 $$(\ad f_i)^{1-a_{ji}}f_j=0$$을 특별히 *Serre relation*이라 한정해 부르기도 한다.

</div>

여기에서 $$\delta_{ij}$$는 Kronecker delta이고, $$(\ad x)^m y$$는 $$\ad x$$를 $$y$$에 $$m$$번 반복 적용한 것 $$[x,[x,\cdots[x,y]\cdots]]$$를 뜻한다. 관계식의 의미를 하나씩 풀어 보면, $$[h_i,h_j]=0$$은 $$h_i$$들이 abelian 부분, 곧 Cartan subalgebra의 역할을 할 부분을 생성함을 강제하고, $$[h_i,e_j]=a_{ji}e_j$$와 $$[h_i,f_j]=-a_{ji}f_j$$는 $$e_j,f_j$$가 각각 weight $$\alpha_j$$, $$-\alpha_j$$의 root vector처럼 행동하게 하며, $$[e_i,f_j]=\delta_{ij}h_i$$는 같은 첨자의 $$e_i,f_i,h_i$$가 $$\sl_2$$의 표준 관계식 $$[e,f]=h$$를 만족하고 첨자가 다르면 $$e_i,f_j$$가 commute함을 말한다. 처음 세 줄까지만 부과한 Lie algebra는 일반적으로 무한차원이며, 이를 유한하게 잘라내는 것이 마지막 두 줄의 Serre relation이다.

이 표시가 우리가 아는 예와 맞물리는지를 가장 작은 경우에서 확인한다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\ell=1$$이고 $$A=(2)$$인 경우를 보자. Generator는 $$e_1,f_1,h_1$$ 셋뿐이고, $$i\neq j$$인 첨자쌍이 없으므로 Serre relation은 없으며, 남는 관계식은

$$[h_1,e_1]=2e_1,\qquad [h_1,f_1]=-2f_1,\qquad [e_1,f_1]=h_1$$

뿐이다. 이는 정확히 $$\sl_2$$의 commutation relation이므로 ([§근계, ⁋정의 8](/ko/math/lie_theory/root_systems#def8) 이전의 $$\sl(2;\mathbb{C})$$ 분석) $$\mathfrak{g}(A)\cong\sl_2$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\ell=2$$이고 $$A=\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)$$인 경우, 이는 root system $$A_2$$의 Cartan matrix이다. 여기에서 $$1-a_{12}=1-a_{21}=2$$이므로 Serre relation은

$$(\ad e_1)^2 e_2=[e_1,[e_1,e_2]]=0,\qquad (\ad e_2)^2 e_1=[e_2,[e_2,e_1]]=0$$

과 $$f$$에 대한 같은 꼴의 두 관계식이다. 이 표시로 얻어지는 $$\mathfrak{g}(A)$$는 $$\sl_3$$이며, $$e_1,e_2$$는 두 simple root에 딸린 root vector, $$[e_1,e_2]$$는 highest root에 딸린 root vector에 해당한다. Serre relation $$[e_1,[e_1,e_2]]=0$$은 root $$2\alpha_1+\alpha_2$$가 $$A_2$$의 root가 아니라는 사실, 곧 그 자리의 root space가 $$0$$임을 대수적으로 표현한 것이다.

</div>

두 예시는 Serre relation의 지수 $$1-a_{ji}$$가 어떻게 결정되는지를 보여준다. $$\sl_2$$ 표현론에서 $$e_j$$를 weight $$\alpha_j$$의 highest weight처럼 보고 $$\sl_{2,\alpha_i}=\langle e_i,f_i,h_i\rangle$$의 작용을 생각하면, $$\ad e_i$$를 거듭 적용해 얻는 weight 사슬 $$\alpha_j,\alpha_j+\alpha_i,\alpha_j+2\alpha_i,\ldots$$이 더는 root가 되지 않고 끊기는 지점이 바로 $$\alpha_j-a_{ji}\alpha_i$$ 다음, 곧 $$(\ad e_i)^{1-a_{ji}}e_j$$ 자리이다. $$h_i$$가 $$e_j$$에 weight $$\beta(h_i)=a_{ji}$$로 작용하므로 $$\alpha_i$$-string의 길이가 $$1-a_{ji}$$로 정해지는 것인데, 이는 [§근계, ⁋명제 7](/ko/math/lie_theory/root_systems#prop7)의 $$\sl_2$$ string 계산이 그대로 옮겨 온 것이다.

## 삼각 분해와 Cartan 부분의 통제

$$\mathfrak{g}(A)$$가 의도한 구조를 갖는지를 보려면 먼저 generator $$h_i,e_i,f_i$$들이 몫에서 무너지지 않고 독립적으로 살아남는지, 그리고 $$\mathfrak{g}(A)$$가 $$\sl_2$$ 표현론을 적용할 수 있는 형태로 분해되는지를 확인해야 한다. 핵심은 처음 세 줄의 관계식만으로 이미 weight 구조가 강제된다는 점이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$A=(a_{ij})$$가 $$\det A\neq 0$$인 generalized Cartan matrix라 하자. $$\mathfrak{g}(A)$$ 안에서 $$h_1,\ldots,h_\ell$$의 상은 일차독립이고, 이들이 생성하는 abelian 부분대수 $$\mathfrak{h}=\span_k\{h_1,\ldots,h_\ell\}$$의 $$\ad$$ 작용에 대하여

$$\mathfrak{g}(A)=\mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+$$

인 weight 공간 분해가 성립한다. 여기에서 $$\mathfrak{n}^+$$는 $$e_i$$들로 생성되는 부분대수, $$\mathfrak{n}^-$$는 $$f_i$$들로 생성되는 부분대수이며, $$\mathfrak{n}^{\pm}$$의 각 weight은 simple root $$\alpha_1,\ldots,\alpha_\ell$$의 음이 아닌(각각 양이 아닌) 정수계수 합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$h_i$$들의 일차독립을 본다. $$\mathfrak{h}^{\ast}$$의 원소 $$\alpha_j$$를 $$\alpha_j(h_i)=a_{ji}$$로 정하면, $$\det A\neq 0$$이므로 $$\{\alpha_j\}$$는 $$\{h_i\}$$의 dual에 해당하는 일차독립 family를 이루고, 따라서 $$h_i$$들도 일차독립이다. 이를 엄밀히 하려면 $$h_i$$들이 몫에서 $$0$$이 아님을 보이는 표현을 하나 제시하면 충분한데, 아래에서 구성하는 weight 공간 분해 자체가 그 표현을 제공한다.

$$\mathfrak{g}(A)$$를 $$\mathfrak{h}$$의 $$\ad$$ 작용에 대한 weight 공간으로 분해한다. 관계식 $$[h_i,e_j]=a_{ji}e_j=\alpha_j(h_i)e_j$$와 $$[h_i,f_j]=-\alpha_j(h_i)f_j$$로부터 각 generator는 $$\mathfrak{h}$$에 대한 weight vector이다. $$e_j$$의 weight은 $$\alpha_j$$, $$f_j$$의 weight은 $$-\alpha_j$$, $$h_i$$의 weight은 $$0$$이다. Weight은 bracket에 대해 더해지므로 ([§근계, ⁋명제 6](/ko/math/lie_theory/root_systems#prop6)), generator들의 반복 bracket으로 생성되는 $$\mathfrak{g}(A)$$ 전체는 $$\mathfrak{h}^{\ast}$$의 원소들에 대한 weight 공간들의 직합이다. $$e_i$$들만의 bracket으로 만들어지는 원소는 $$\alpha_i$$들의 음이 아닌 정수계수 합을 weight으로 가지므로 $$\mathfrak{n}^+=\bigoplus_{\beta>0}\mathfrak{g}_\beta$$ 꼴이고, 마찬가지로 $$f_i$$들로 만들어지는 $$\mathfrak{n}^-=\bigoplus_{\beta<0}\mathfrak{g}_\beta$$이다. weight $$0$$ 부분은 정확히 $$\mathfrak{h}$$이다. 실제로 $$[e_i,f_j]=\delta_{ij}h_i$$가 weight $$0$$ 성분을 $$h_i$$들로 닫아 주고, 더 긴 bracket이 weight $$0$$을 주려면 $$e$$와 $$f$$의 개수가 균형을 이루어야 하는데 이때마다 $$[e_i,f_j]=\delta_{ij}h_i$$로 환원되어 $$\mathfrak{h}$$를 벗어나지 않기 때문이다. 따라서

$$\mathfrak{g}(A)=\mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+$$

를 얻고, weight $$0$$ 공간이 $$\mathfrak{h}$$로서 $$\ell$$차원이므로 $$h_i$$들은 일차독립이다.

</details>

이 분해를 *triangular decomposition<sub>삼각 분해</sub>*이라 부른다. $$\mathfrak{h}$$를 $$\mathfrak{g}(A)$$의 Cartan 부분, $$\mathfrak{n}^+,\mathfrak{n}^-$$를 각각 위·아래 nilpotent 부분으로 보는 관점이며, finite type일 때 이는 semisimple Lie algebra의 root 분해 $$\mathfrak{g}=\mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+$$와 정확히 대응한다 ([§근계, ⁋정의 5](/ko/math/lie_theory/root_systems#def5) 이후의 root decomposition). 처음 세 줄의 관계식만으로는 $$\mathfrak{n}^{\pm}$$가 무한차원일 수 있으나, Serre relation이 각 $$\alpha_i$$-string을 $$1-a_{ij}$$ 길이에서 끊어 weight 공간들을 유한하게 잘라낸다. finite type에서 이 절단이 정확히 root system $$\Phi$$의 root들만 살아남게 만든다는 것이 다음 정리의 핵심이다.

## Serre의 정리

이제 finite type Cartan matrix에 대한 주 정리를 서술한다. 이 정리는 두 방향, 곧 표시로부터 semisimple Lie algebra를 얻는 방향과 임의의 semisimple Lie algebra가 이런 표시를 가진다는 방향을 함께 담는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Serre)**</ins> $$A=(a_{ij})_{1\leq i,j\leq\ell}$$가 finite type generalized Cartan matrix라 하자. 그럼 [정의 3](#def3)의 $$\mathfrak{g}(A)$$는 유한차원 semisimple Lie algebra이고, $$\mathfrak{h}=\span_k\{h_1,\ldots,h_\ell\}$$은 그 Cartan subalgebra이며, 그에 딸린 root system의 Cartan matrix는 다시 $$A$$이다. 역으로 임의의 유한차원 semisimple Lie algebra $$\mathfrak{g}$$에 대하여, Cartan subalgebra와 simple root를 택해 얻은 Cartan matrix를 $$A$$라 하면, generator $$e_i,f_i,h_i$$를 각 simple root에 딸린 표준 원소로 보내는 사상은 동형

$$\mathfrak{g}(A)\;\xrightarrow{\ \sim\ }\;\mathfrak{g}$$

를 정의한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명을 두 방향으로 나눈다.

(역방향) $$\mathfrak{g}$$가 유한차원 semisimple이라 하자. Cartan subalgebra $$\mathfrak{h}$$와 root decomposition $$\mathfrak{g}=\mathfrak{h}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$를 택하고 ([§근계, ⁋정의 5](/ko/math/lie_theory/root_systems#def5)), positive root와 simple root $$\Delta=\{\alpha_1,\ldots,\alpha_\ell\}$$를 고정한다 ([§근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15)). 각 simple root $$\alpha_i$$에 대하여, [§근계, ⁋보조정리 11](/ko/math/lie_theory/root_systems#lem11) 이후의 구성으로

$$[e_i,f_i]=h_i,\qquad [h_i,e_i]=2e_i,\qquad [h_i,f_i]=-2f_i$$

를 만족하는 표준 원소 $$e_i\in\mathfrak{g}_{\alpha_i}$$, $$f_i\in\mathfrak{g}_{-\alpha_i}$$, $$h_i=h_{\alpha_i}\in\mathfrak{h}$$를 택한다. 이때 $$h_i$$의 작용은 $$[h_i,e_j]=\alpha_j(h_i)e_j=a_{ji}e_j$$이고 $$[h_i,f_j]=-a_{ji}f_j$$이며, $$i\neq j$$에 대하여 $$\alpha_i-\alpha_j$$가 root가 아니므로 ([§근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15) 이후의 simple root 성질) $$[e_i,f_j]=0=\delta_{ij}h_i$$이다. 또 $$h_i$$들이 commute하므로 처음 네 줄의 관계식이 모두 성립한다.

Serre relation은 $$\alpha_i$$-string의 길이로부터 따라온다. $$\sl_{2,\alpha_i}=\langle e_i,f_i,h_i\rangle$$의 작용에서 $$e_j$$는 weight $$\alpha_j(h_i)=a_{ji}$$의 highest weight vector처럼 행동하고 ([§근계, ⁋명제 7](/ko/math/lie_theory/root_systems#prop7)), root $$\alpha_j$$를 지나는 $$\alpha_i$$-string은 $$\alpha_j,\alpha_j+\alpha_i,\ldots,\alpha_j-a_{ji}\alpha_i$$로 끝난다. 따라서 $$\alpha_j+(1-a_{ji})\alpha_i$$는 root가 아니어서 그 root space가 $$0$$이고, $$(\ad e_i)^{1-a_{ji}}e_j\in\mathfrak{g}_{\alpha_j+(1-a_{ji})\alpha_i}=0$$이다. $$f$$에 대한 관계식도 같다. 그러므로 generator $$e_i,f_i,h_i$$들이 [정의 3](#def3)의 모든 Serre 관계식을 만족하고, free Lie algebra의 보편 성질로 Lie algebra 준동형 $$\pi:\mathfrak{g}(A)\rightarrow\mathfrak{g}$$가 유일하게 정해진다. $$\mathfrak{g}$$가 semisimple이므로 각 root space는 $$e_i$$들의 반복 bracket으로 생성되고 ([§근계, ⁋보조정리 10](/ko/math/lie_theory/root_systems#lem10)), $$\mathfrak{g}$$가 root vector와 $$\mathfrak{h}$$로 생성되므로 $$\pi$$는 전사이다. 단사성은 [명제 6](#prop6)의 삼각 분해를 $$\mathfrak{g}(A)$$와 $$\mathfrak{g}$$ 양쪽에서 비교하여 얻는다. $$\pi$$는 weight 공간을 weight 공간으로 보내고, finite type일 때 아래 정방향에서 보듯 $$\mathfrak{g}(A)$$의 nonzero weight 공간이 정확히 $$\Phi$$의 root들에서만 나타나며 각 root space가 $$1$$차원이므로, 전사인 $$\pi$$는 각 weight 공간에서 차원을 보존해 동형이다.

(정방향) $$A$$가 finite type이면, $$A$$를 Cartan matrix로 갖는 유한차원 semisimple Lie algebra $$\mathfrak{g}$$가 존재한다. 이는 Cartan matrix가 root system을 통해 유한차원 semisimple Lie algebra를 유일하게 결정한다는 분류 정리로부터 나오며, $$A_\ell,B_\ell,C_\ell,D_\ell$$의 고전형에 대해서는 $$\sl_{\ell+1},\mathfrak{so}_{2\ell+1},\mathfrak{sp}_{2\ell},\mathfrak{so}_{2\ell}$$이 그러한 $$\mathfrak{g}$$를 직접 제공하고, 예외형 $$G_2,F_4,E_6,E_7,E_8$$도 각각 구체적인 실현을 가진다. 그러한 $$\mathfrak{g}$$에 역방향을 적용하면 전사 준동형 $$\pi:\mathfrak{g}(A)\rightarrow\mathfrak{g}$$를 얻고, $$\pi$$가 동형임을 보이는 것은 $$\dim\mathfrak{g}(A)\leq\dim\mathfrak{g}$$, 곧 $$\mathfrak{g}(A)$$가 유한차원이며 그 차원이 $$\mathfrak{g}$$를 넘지 않음을 보이는 것으로 충분하다.

$$\mathfrak{n}^+$$가 유한차원임을 보인다. $$\mathfrak{n}^+$$는 $$e_1,\ldots,e_\ell$$로 생성되는 free Lie algebra의 몫이되, Serre relation $$(\ad e_i)^{1-a_{ji}}e_j=0$$들로 추가로 몫한 것이다. $$A$$가 finite type이라는 조건은 대칭화 $$DA$$가 positive definite라는 것이므로, $$\mathfrak{n}^+$$의 weight으로 나타날 수 있는 $$\sum_i c_i\alpha_i$$ ($$c_i\geq 0$$ 정수) 가운데 실제로 nonzero weight 공간을 갖는 것은 root system $$\Phi$$의 positive root 유한개로 한정된다. 핵심 보조 사실은 다음이다. Serre relation을 부과한 $$\mathfrak{n}^+$$에서 $$\ad$$ 작용에 의한 각 $$\alpha_i$$-string의 길이가 $$1-a_{ji}$$로 잘리므로, weight $$\beta=\sum c_i\alpha_i$$의 공간이 $$0$$이 아니려면 $$\beta$$가 simple reflection들의 작용 아래 닫힌 유한 집합, 곧 $$\Phi^+$$ 안에 들어야 한다. positive definite 조건은 그러한 $$\beta$$가 유한개임과 각 weight 공간이 유한차원임을 보장한다. 따라서 $$\mathfrak{n}^+$$는 유한차원이고, 대칭적으로 $$\mathfrak{n}^-$$도 유한차원이며, $$\mathfrak{h}$$가 $$\ell$$차원이므로 [명제 6](#prop6)의 삼각 분해에 의해 $$\mathfrak{g}(A)$$는 유한차원이다.

이제 $$\pi:\mathfrak{g}(A)\rightarrow\mathfrak{g}$$가 weight 공간마다 차원을 비교하면 동형임이 따른다. $$\mathfrak{g}$$의 nonzero root space는 정확히 $$\Phi$$의 root에서 $$1$$차원으로 나타나고, $$\pi$$가 전사이므로 $$\mathfrak{g}(A)$$의 대응 weight 공간은 차원이 $$1$$ 이상이다. 그런데 위에서 본 string 절단으로 $$\mathfrak{g}(A)$$의 weight 공간 또한 $$\Phi$$의 root에서만 나타나며 그 차원이 $$1$$을 넘지 않으므로, 모든 weight 공간에서 차원이 정확히 일치하여 $$\pi$$는 동형이다. 따라서 $$\mathfrak{g}(A)\cong\mathfrak{g}$$는 유한차원 semisimple이고, $$\mathfrak{h}$$가 그 Cartan subalgebra이며 그 Cartan matrix가 $$A$$임이 따라온다.

</details>

증명의 두 방향은 같은 다리의 양 끝이다. 역방향은 임의의 semisimple Lie algebra가 그 Cartan matrix로부터 generator와 relation으로 복원됨을 말하고, 정방향은 finite type Cartan matrix가 항상 그러한 semisimple Lie algebra에서 비롯됨을 말한다. 둘을 합치면 finite type Cartan matrix와 유한차원 semisimple Lie algebra가 서로를 유일하게 결정한다. 한 가지 주의할 부호 관례는 $$[h_i,e_j]=a_{ij}e_j$$에서 $$a_{ij}=\langle\alpha_i,\alpha_j\rangle=2(\alpha_i,\alpha_j)/(\alpha_j,\alpha_j)$$의 첨자 순서이다. $$h_i$$는 $$\alpha_i$$에 딸린 coroot이고 $$e_j$$는 weight $$\alpha_j$$이므로 그 weight은 $$\alpha_j(h_i)=\langle\alpha_j,\alpha_i^{\vee}\rangle=a_{ij}$$인데, [§근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)의 $$a_{ij}=\langle\alpha_i,\alpha_j\rangle$$ 관례와 맞추어 본문은 $$[h_i,e_j]=a_{ij}e_j$$로 적었다. 따라서 Serre relation의 지수 $$1-a_{ij}$$ 역시 이 관례 아래에서 $$\alpha_j$$를 지나는 $$\alpha_i$$-string의 길이로 읽힌다.

## 분류와 Chevalley basis

Serre 정리는 root system 이론과 결합하여 분류를 완성한다. [§근계, ⁋명제 12](/ko/math/lie_theory/root_systems#prop12)에서 보았듯 유한차원 semisimple Lie algebra는 Cartan subalgebra를 거쳐 root system을 낳고, simple root를 택하면 Cartan matrix가, 따라서 Dynkin diagram이 결정된다 ([§Borel subgroup, ⁋정의 1](/ko/math/lie_theory/borel_subgroup#def1)). 거꾸로 Serre 정리는 finite type Cartan matrix로부터 그것을 실현하는 유한차원 semisimple Lie algebra를 직접 구성해 준다. 이 두 방향이 서로 역임을 합치면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> 유한차원 semisimple Lie algebra의 동형류와 finite type Cartan matrix의 동치류, 곧 Dynkin diagram 사이에 자연스러운 일대일 대응이 있다. simple Lie algebra는 연결된 Dynkin diagram, 곧 $$A_\ell\,(\ell\geq 1),B_\ell\,(\ell\geq 2),C_\ell\,(\ell\geq 3),D_\ell\,(\ell\geq 4)$$의 네 무한족과 다섯 예외형 $$E_6,E_7,E_8,F_4,G_2$$에 대응한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 7](#thm7)의 역방향은 각 유한차원 semisimple $$\mathfrak{g}$$에 finite type Cartan matrix $$A$$를 대응시키고, 정방향은 각 $$A$$에 $$\mathfrak{g}(A)$$를 대응시킨다. 두 대응이 서로 역임은 정리의 동형 $$\mathfrak{g}(A)\cong\mathfrak{g}$$가 정확히 말하는 바이다. Cartan matrix는 simple root의 번호 매김에 따라 동시치환만큼의 모호함을 가지므로, 그 동치류는 Dynkin diagram과 일대일 대응한다 ([§Borel subgroup, ⁋정의 1](/ko/math/lie_theory/borel_subgroup#def1) 이후의 논의). 마지막으로 $$\mathfrak{g}$$가 simple인 것은 그 Dynkin diagram이 연결인 것과 동치인데, 이는 Cartan matrix가 직합으로 쪼개지지 않는 것이 semisimple 분해 $$\mathfrak{g}=\bigoplus_i\mathfrak{g}_i$$ ([§Killing 형식과 Cartan 판정법, ⁋정리 10](/ko/math/lie_theory/killing_form_and_cartan_criterion#thm10))의 simple 성분이 하나뿐인 것과 같기 때문이다. 연결된 finite type Dynkin diagram의 목록이 네 무한족과 다섯 예외형뿐이라는 것은 generalized Cartan matrix의 positive definite 조건을 그래프 조합론으로 분류하여 얻어지며 ([§Borel subgroup, ⁋정리 6](/ko/math/lie_theory/borel_subgroup#thm6)), 이로써 대응이 완성된다.

</details>

이 분류에서 한 가지 정밀화는 $$\mathfrak{g}(A)$$를 정수계수로 적을 수 있다는 점이다. Serre 정리가 주는 generator $$e_i,f_i,h_i$$로부터 모든 root vector를 정수계수 bracket으로 만들어 내면, $$\mathfrak{g}$$의 기저를 적절히 고를 수 있다.

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9 (Chevalley basis)**</ins> 유한차원 semisimple Lie algebra $$\mathfrak{g}$$는 다음 성질을 갖는 기저 $$\{h_i\mid 1\leq i\leq\ell\}\cup\{e_\alpha\mid\alpha\in\Phi\}$$를 갖는다. 모든 구조 상수가 정수이며, 특히 $$[h_i,e_\alpha]=\langle\alpha,\alpha_i^{\vee}\rangle e_\alpha$$, $$[e_\alpha,e_{-\alpha}]=h_\alpha$$ ($$h_\alpha$$는 coroot $$\alpha^{\vee}$$에 대응하는 $$h_i$$들의 정수계수 합), 그리고 $$\alpha+\beta\in\Phi$$일 때 $$[e_\alpha,e_\beta]=\pm(p+1)e_{\alpha+\beta}$$이다. 여기에서 $$p$$는 $$\beta$$를 지나는 $$\alpha$$-string $$\beta-p\alpha,\ldots,\beta+q\alpha$$의 왼쪽 길이이다.

</div>

이러한 기저를 *Chevalley basis<sub>슈발레 기저</sub>*라 부른다. 그 존재는 Serre 정리가 주는 generator로부터 출발해 각 root vector $$e_\alpha$$를 부호까지 일관되게 정규화함으로써 증명되며, 구조 상수가 모두 정수이므로 $$\mathfrak{g}$$의 정수형 $$\mathbb{Z}$$-부분대수를 정의할 수 있다. 이 정수형은 임의의 체 $$\mathbb{F}$$로 base change하여 그 체 위의 semisimple Lie algebra와 Chevalley group을 정의하는 출발점이 된다. 이로써 Cartan matrix라는 유한한 정수 자료가 표수에 무관하게 Lie 이론 전체를 떠받친다는 사실이 확인된다.

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Ser]** J.-P. Serre, *Complex semisimple Lie algebras*, Springer, 1987.  
**[Kac]** V. G. Kac, *Infinite-dimensional Lie algebras*, 3rd ed., Cambridge University Press, 1990.  
**[Bou]** N. Bourbaki, *Lie groups and Lie algebras, Chapters 4–6*, Springer, 2002.  
