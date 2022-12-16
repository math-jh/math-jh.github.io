---

title: "호몰로지와 코호몰로지"
excerpt: "기본정의"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/homology_and_cohomology
header:
    overlay_image: /assets/images/Algebraic_topology/a.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-06-27
last_modified_at: 2022-06-27
weight: 101

---

위상수학에서 살짝 맛본 기본군은 직관적으로 그 의미가 명확한 불변량이다. 기본군은 고리를 통해 공간에 뚫려있는 구멍을 잡아낸다. 예를 들어 $X=\mathbb{R}^2\setminus\\{0\\}$을 생각하면, 이 공간에서 원점을 감싸는 고리는 연속적인 방법으로는 한 점으로 변형하는 것이 불가능하기 때문에 $\pi\_1(X)$가 0이 아니고, 따라서 우리는 $X$에 구멍이 뚫려 있다는 사실을 안다. 

하지만 이 개념의 한계 또한 명확하다. 예컨대 $Y=\mathbb{R}^3\setminus\\{0\\}$을 생각하면 이 공간 상의 어떠한 고리를 주어도 한 점으로 수축시킬 수 있다. 이는 <em_ko>고리</em_ko> $S^1$이 공간 상의 구멍을 탐지하는 데에 한계가 있다는 것을 보여준다. 이를 해결하기 위한 방법은 당연히 $S^1$ 대신 더 높은 차원의 <em_ko>고리</em_ko>, 예컨대 $S^2$를 사용하는 것이다. 방금의 상황에서 $S^1$ 대신 $S^2$를 사용한다면, 원점을 감싸고 있는 $S^2$는 한 점으로 수축할 수 없고, 그렇지 않은 $S^2$는 한 점으로 수축할 수 있음이 직관적으로 명확하다.

우리는 이렇게 기본군 $\pi\_1(X)$를 일반화하여 $\pi\_2(X)$, 더 나아가 $\pi\_n(X)$를 정의할 수 있다. 그러나 일반적으로 이 군들을 직접 계산하는 것은 굉장히 어렵다. 다행히도 우리가 궁금해하는 많은 성질들은 homotopy group $\pi\_n(X)$ 대신, 더 계산하기 쉬운 *homology group*들만 살펴보아도 충분하다는 것이 밝혀져 있다.

## 호몰로지 군과 코호몰로지 군

[호몰로지 대수학](/ko/homological_algebra/)에서 다루는 호몰로지는 대수적으로 명확한 의미를 갖는다. 간단히 정의를 기억해보자면, $R$-module들의 열 $(C\_n)\_{n\in\mathbb{Z}}$가 *chain complex*라는 것은 이들 사이에 *boundary map* $d\_n:C\_n\rightarrow C\_{n-1}$들이 정의되어 다음의 열

$$C_\bullet:\qquad\cdots C_{n+1}\overset{d_{n+1}}{\longrightarrow}C_n\overset{d_n}{\longrightarrow} C_{n-1}\longrightarrow\cdots$$

에서 항상 $d_{n-1}d_n=0$, 혹은 더 간단히 $d^2=0$이 성립하는 것이다. 이는 곧 $\operatorname{im}(d_n)\subseteq\ker d_{n-1}$이 항상 성립한다는 것과 동치이며, 특별히 모든 $n$에 대해 $\operatorname{im}(d_n)=\ker(d_{n-1})$이 성립하면 우리는 $C_\bullet$이 *exact sequence*라 부른다. 이 때, $C_\bullet$의 $n$번째 *homology group<sub>호몰로지 군</sub>*[^1]은 다음의 식

$$H_n(C_\bullet)=\ker(d_{n-1})/\operatorname{im}(d_n)$$

으로 정의된다. 따라서 모든 $n$에 대해 $C_\bullet$의 homology group이 모두 $0$이라면 $C_\bullet$은 exact sequence가 된다. 

비슷하게, 다음의 열 $(C^n)\_{n\in\mathbb{Z}}$가 *cochain complex*라는 것은 이들 사이의 *boundary map* $d^n:C^n\rightarrow C^{n+1}$이 $d^{n+1}d^n=0$을 항상 만족하는 것이다. 이 때, 다음의 열

$$C^\bullet:\qquad\cdots C^{n-1}\overset{d^{n-1}}{\longrightarrow}C^n\overset{d^n}{\longrightarrow} C^{n+1}\longrightarrow\cdots$$

에서 다음의 식

$$H^n(C^\bullet)=\ker(d^n)/\operatorname{im}(d^{n-1})$$

으로 정의된 $R$-module을 $C^\bullet$의 $n$번째 *cohomology group<sub>코호몰로지 군</sub>*이라 부른다. 

따라서 대수적으로 homology group과 cohomology group은 차이가 없다. 그러나 기하적으로는 호몰로지 군과 코호몰로지 군을 구분하는 것이 도움이 된다. 

## Homology theory

위의 정의에 기하적인 의미를 부여하는 것은 공간 $X$마다 다음의 chain complex

$$C(X)_\bullet:\qquad \cdots\longrightarrow C_{n+1}(X)\overset{d_{n+1}}{\longrightarrow}C_n(X)\overset{d_n}{\longrightarrow} C_{n-1}(X)\longrightarrow\cdots$$

혹은 cochain complex

$$C(X)^\bullet:\qquad\cdots C^{n-1}(X)\overset{d^{n-1}}{\longrightarrow}C^n(X)\overset{d^n}{\longrightarrow} C^{n+1}(X)\longrightarrow\cdots$$

를 대응시키는 것으로부터 시작된다.  **[Hat]**에서는 쉽게 내용을 전달하기 위해 위의 chain complex의 성분들이 모두 $\mathbf{Ab}$에 속하는 경우를 먼저 다뤘으나, 우리는 약간 더 일반화하여 이들이 $\mathbf{Mod}\_R$에 속하는 것으로 생각한다.[^2]

그럼 $C(X)\_\bullet$들은 모두 category $\mathbf{Ch}(\mathbf{Mod}\_R)$의 object들이며, $n$번째 homology group $H_n$은 $\mathbf{Ch}(\mathbf{Mod}\_R)$에서 $\mathbf{Mod}\_R$로의 functor가 된다. 우리의 관심의 대상이 되는 공간들의 category를 $\mathcal{T}$라 하자. 그럼 위의 과정은 $\mathcal{T}$에서 $\mathbf{Ch}(\mathbf{Mod}\_R)$로의 functor를 만드는 것으로 이해할 수 있으며, 이를 다시 functor $H_n$과 합성하면 $\mathcal{T}\rightarrow\mathbf{Mod}\_R$을 얻는다. 이를 간단하게 *homology theory*라 부른다.

이러한 functor $\mathcal{T}\rightarrow\mathbf{Ch}(\mathbf{Mod}\_R)$은 유일하지 않으며, 따라서 homology theory도 여럿 있다. 그러나 Eilenberg와 Steenrod에 의해 이들이 만족해야 할 성질들이 공리적으로 정의되었고, 우리가 다룰 명제들은 이 공리들을 통해 얻어낼 수 있으므로 적어도 우리의 지금 관심사에서는 모든 homology theory들이 (같은 대상에 동시에 적용된다면) 동등한 것으로 보아도 좋다. 

---
**참고문헌**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.  
**[Hat]** A. Hatcher. *Algebraic Topology*. Cambridge University Press, 2002.

---

[^1]: 정확하게는 homology module.
[^2]: 물론 이들이 $\mathbf{Mod}\_R$ 대신 임의의 abelian category $\mathcal{A}$에 속하여도 성립한다. 