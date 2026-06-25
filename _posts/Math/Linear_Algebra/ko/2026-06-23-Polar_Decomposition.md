---
title: "극분해"
description: "양의 준정부호 작용소가 유일한 양의 제곱근을 가짐을 스펙트럼 정리로부터 보이고, 이를 이용해 임의의 작용소를 유니터리 작용소와 양의 작용소의 곱으로 분해하는 극분해를 구성한다."
excerpt: "작용소의 유니터리--양정부호 분해"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/polar_decomposition
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-23

weight: 124

published: false

---

복소수 $$z$$를 $$z=e^{i\theta}\lvert z\rvert$$의 꼴, 즉 크기 $$\lvert z\rvert\geq 0$$과 단위복소수 $$e^{i\theta}$$의 곱으로 적을 수 있듯, 임의의 linear operator도 "크기"에 해당하는 양의 작용소와 "방향"에 해당하는 유니터리 작용소의 곱으로 분해된다. 이것이 *극분해*이며, 그 출발점은 양의 작용소의 제곱근이다. 우리는 [§복소내적공간](/ko/math/linear_algebra/complex_inner_product_spaces) 위에서 이론을 전개하되, 모든 논의는 [§내적공간](/ko/math/linear_algebra/inner_product_spaces)의 실내적공간 위에서도 unitary를 orthogonal로, 켤레전치를 transpose로 바꾸면 그대로 성립한다.

## 양의 작용소의 제곱근

자기수반작용소가 양의 준정부호라는 것은 [§스펙트럼 정리, ⁋정의 8](/ko/math/linear_algebra/spectral_theorem#def8)에서 정의한 대로 모든 $$v$$에 대해 $$\langle Lv,v\rangle\geq 0$$인 것이며, 이는 [§복소 스펙트럼 정리, ⁋명제 8](/ko/math/linear_algebra/complex_spectral_theorem#prop8)에 의해 자기수반작용소의 고윳값이 실수임을 함께 생각하면 모든 고윳값이 $$0$$ 이상인 것과 동치이다. 양의 작용소는 음이 아닌 실수처럼 제곱근을 가지며, 그 제곱근은 유일하다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 복소내적공간 $$V$$ 위의 양의 준정부호 자기수반작용소 $$P$$에 대하여, $$S^2=P$$를 만족하는 양의 준정부호 자기수반작용소 $$S$$가 유일하게 존재한다. 이를 $$P$$의 *제곱근<sub>square root</sub>* $$\sqrt P$$라 적는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$P$$가 자기수반이므로 [§복소 스펙트럼 정리, ⁋정리 6](/ko/math/linear_algebra/complex_spectral_theorem#thm6)에 의하여 $$P$$의 고유벡터들로 이루어진 정규직교기저 $$\{e_1,\ldots,e_n\}$$이 존재하고, $$Pe_i=\lambda_ie_i$$의 각 $$\lambda_i$$는 $$0$$ 이상의 실수이다. 이제 $$Se_i=\sqrt{\lambda_i}e_i$$로 정의하면 $$S$$는 같은 정규직교기저를 고유벡터로 가지므로 자기수반이고, 고윳값 $$\sqrt{\lambda_i}\geq 0$$이 모두 음이 아니므로 양의 준정부호이며, $$S^2e_i=\lambda_ie_i=Pe_i$$이므로 $$S^2=P$$이다.

유일성을 보이자. $$T$$가 또 다른 양의 준정부호 제곱근, 즉 $$T^2=P$$라 하자. 그럼 $$TP=T\cdot T^2=T^2\cdot T=PT$$이므로 $$T$$는 $$P$$와 가환이고, 따라서 $$P$$의 각 고유공간 $$E_{\lambda_i}(P)$$를 불변으로 남긴다. $$T$$를 $$E_{\lambda_i}(P)$$로 제한하면 그 위에서 $$T^2=P=\lambda_iI$$이므로 $$T\vert_{E_{\lambda_i}(P)}$$는 제곱이 $$\lambda_i I$$인 양의 준정부호 작용소인데, 그러한 작용소의 고윳값은 제곱이 $$\lambda_i$$이면서 음이 아니므로 $$\sqrt{\lambda_i}$$ 하나뿐이고, $$T\vert_{E_{\lambda_i}(P)}$$ 또한 자기수반이라 대각화되므로 $$T\vert_{E_{\lambda_i}(P)}=\sqrt{\lambda_i}\,I$$이다. 즉 $$T$$는 각 고유공간에서 $$\sqrt{\lambda_i}$$배로 작용하므로 $$T=S$$이다.

</details>

특히 임의의 작용소 $$A$$에 대하여 $$A^\ast A$$는 양의 준정부호 자기수반작용소이다. $$A^\ast A$$가 자기수반인 것은 $$(A^\ast A)^\ast=A^\ast A$$로부터, 양의 준정부호인 것은

$$\langle A^\ast Av,v\rangle=\langle Av,Av\rangle=\lVert Av\rVert^2\geq 0$$

으로부터 따라온다. 따라서 $$\sqrt{A^\ast A}$$가 항상 정의되며, 이것이 극분해에서 "크기"의 역할을 한다.

## 극분해

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (극분해)**</ins> 복소내적공간 $$V$$ 위의 임의의 linear operator $$A:V\rightarrow V$$에 대하여, 양의 준정부호 자기수반작용소 $$P$$와 유니터리 작용소 $$U$$가 존재하여

$$A=UP$$

이다. 이 때 $$P=\sqrt{A^\ast A}$$로 유일하게 결정되며, $$A$$가 가역이면 $$U$$ 또한 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$P=\sqrt{A^\ast A}$$로 두자. 핵심은 임의의 $$v$$에 대하여 $$\lVert Pv\rVert=\lVert Av\rVert$$이라는 것이다. 실제로 $$P$$가 자기수반이고 $$P^2=A^\ast A$$이므로

$$\lVert Pv\rVert^2=\langle Pv,Pv\rangle=\langle v,P^2v\rangle=\langle v,A^\ast Av\rangle=\langle Av,Av\rangle=\lVert Av\rVert^2$$

이다. 이로부터 대응 $$Pv\mapsto Av$$가 잘 정의된 사상 $$U_0:\im P\rightarrow\im A$$를 준다. $$Pv=Pv'$$이면 $$\lVert A(v-v')\rVert=\lVert P(v-v')\rVert=0$$이라 $$Av=Av'$$이기 때문이다. 같은 등식으로 $$U_0$$은 내적을 보존하는 단사사상이므로 $$\dim\im P=\dim\im A$$이고, 따라서 $$\dim(\im P)^\perp=\dim(\im A)^\perp$$이다. 두 직교여공간 사이의 임의의 내적보존 동형사상을 골라 $$U_0$$을 확장하면, $$V$$ 전체에서 내적을 보존하는 유니터리 작용소 $$U$$를 얻고 $$\im P$$ 위에서 $$U(Pv)=Av$$이므로 $$UP=A$$이다.

$$P=\sqrt{A^\ast A}$$인 것은 $$A=UP$$로부터 $$A^\ast A=PU^\ast UP=P^2$$이고 [명제 1](#prop1)의 제곱근의 유일성에서 따라오므로, $$P$$는 유일하다. $$A$$가 가역이면 $$P$$ 또한 가역이므로 $$U=AP^{-1}$$로 유일하게 결정된다.

</details>

극분해는 [§특이값 분해](/ko/math/linear_algebra/singular_value_decomposition)와 동전의 양면이다. $$P=\sqrt{A^\ast A}$$의 고윳값은 정확히 $$A$$의 singular value들이며, $$P$$를 [§복소 스펙트럼 정리, ⁋따름정리 7](/ko/math/linear_algebra/complex_spectral_theorem#cor7)로 $$P=W\Sigma W^\ast$$로 유니터리 대각화하면 $$A=UP=(UW)\Sigma W^\ast$$이 되어 특이값 분해를 준다. 거꾸로 특이값 분해 $$A=U_1\Sigma U_2^\ast$$로부터 $$A=(U_1U_2^\ast)(U_2\Sigma U_2^\ast)$$로 두면 극분해를 얻는다. 두 분해는 같은 정보를 "크기와 방향"으로 보느냐 "두 정규직교기저 사이의 대각화"로 보느냐의 차이일 뿐이다.

---

**참고문헌**

**[Axl]** S. Axler, *Linear algebra done right*, 3rd ed., Undergraduate Texts in Mathematics, Springer, 2015.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
