---
title: "함수의 극한"
description: "미적분학의 출발점인 함수의 극한을 ε-δ 언어로 정의하고, 극한의 사칙연산 법칙과 거듭제곱·근의 극한, 조임정리, 한쪽 극한과 무한대에서의 극한을 예시와 함께 다룬다."
excerpt: "함수의 극한을 ε-δ로 정의하고 극한법칙·조임정리를 증명한다"

categories: [Math / Calculus]
permalink: /ko/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-ko"

date: 2026-06-15
weight: 1

---

## 극한의 정의

함수의 미분과 적분을 정의하기 위해서는 고등학교 때 배우는 것과 마찬가지로 극한의 개념이 필요하다. 그 때와 비교하여 지금 우리가 다루는 극한이 더 발전한 것은 이제 우리는 극한을 <em-ko>정의</em-ko>한다는 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 실수 $$a$$를 포함하는 어떤 개구간 $$(c,d)$$ ($$c<a<d$$)를 점 $$a$$의 *근방<sub>neighborhood</sub>*이라 부른다.

</div>

점 $$a$$의 근방은 현재는 이 정도의 정의로 충분하다. 특별히 점 $$a$$의 근방 중 $$a$$ 자기 자신이 빠진 집합을 편의상 *삭제된 근방<sub>deleted neighborhood</sub>*라 부른다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 점 $$a$$의 어떤 삭제된 근방에서 정의된 함수 $$f$$를 생각하자. 그럼 실수 $$L$$이 $$x \to a$$일 때 $$f$$의 *극한<sub>limit</sub>*이라는 것은, 임의의 $$\epsilon > 0$$에 대하여 어떤 $$\delta > 0$$이 존재하여

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon$$

이 성립하는 것이다. 이 때 

$$\lim_{x \to a} f(x) = L$$

로 적는다.

</div>

이에 대한 직관적인 설명은 다음과 같다. 우리가 고등학교 때 극한의 개념을 $$f(x)$$가 $$L$$에 <em-ko>무한히 가까워진다</em-ko>고 이야기하는 것이 엄밀한 수학적 정의가 될 수 없는 이유는 <em-ko>가깝다</em-ko>는 개념이 수학적이지 않기 때문이다. 가령 $$L$$과 가까운 숫자들의 모임이, 수학적으로는 집합을 정의하지 않는 것과 같은 이치이다. 

직관적으로 위의 $$\epsilon-\delta$$ 정의는 이를 해결하기 위해, 모든 사람을 대상으로 합의를 만들어내는 과정으로 생각하면 이해가 편하다. 즉, $$f(x)$$가 $$L$$에 <em-ko>얼마나</em-ko> 가까울 것을 요구하든 (즉, 어떤 $$\epsilon>0$$이 주어지든), $$x$$가 $$a$$에 충분히 가깝도록 하기만 하면 ($$0 < \lvert x - a\rvert < \delta$$) 그 요구 $$\lvert f(x) - L\rvert < \epsilon$$을 맞춰줄 수 있다는 것이다. 이를 다음 예시에서 살펴보자.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 정의를 직접 적용해 극한을 증명할 때, 일차함수처럼 $$\lvert f(x) - L\rvert$$이 $$\lvert x - a\rvert$$의 상수배이면 $$\delta$$를 곧바로 읽어낼 수 있지만, 변화율이 일정하지 않은 함수에서는 한 가지 손질이 필요하다. $$g(x) = x^2$$을 생각하고 $$x \to 2$$일 때 극한값이 $$4$$임을 보이자. 우선

$$\lvert g(x)-4\rvert=\lvert x^2-4\rvert=\lvert x-2\rvert\,\lvert x+2\rvert$$

를 계산한다. 핵심은 $$\lvert x-2\rvert$$는 $$2$$ 근방에서 작지만 그 앞에 붙는 $$\lvert x+2\rvert$$는 통제되지 않으면 곱을 키울 수 있다는 점이다. 그래서 먼저 $$\delta\leq 1$$로 제한해 $$\lvert x+2\rvert<5$$를 확보하고 ($$\delta>1$$인 곳은 애초에 관심대상이 아니다), 그 위에서 $$\delta=\min(1,\epsilon/5)$$로 두면

$$0 < \lvert x-2\rvert < \delta \implies \lvert x^2 - 4\rvert < 5\delta \leq \epsilon$$

이 성립한다.

</div>

위와 같이, 본질적으로 우리가 $$\delta$$를 $$\epsilon$$에 의해 결정되는 것으로 둘 수 있다는 것이 이 정의의 핵심으로, 위에서의 직관을 이어가자면 어떠한 $$\epsilon>0$$을 가져오더라도 이 조건을 만족할 수 있는 $$\delta>0$$를 찾는 <em-ko>규칙</em-ko>이 바로 우리가 함수의 극한을 증명할 때 하는 일이다. 

## 극한의 성질들

이제 이를 바탕으로 극한의 성질들을 살펴보자. 우선 첫 번째 성질은 극한이 만일 존재한다면 유일하다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (극한의 유일성)**</ins> $$\lim_{x\to a} f(x) = L$$이고 $$\lim_{x\to a} f(x) = L'$$이면 $$L = L'$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $$L \neq L'$$이라 가정하자. 그럼 $$\epsilon = \frac{1}{2}\lvert L - L'\rvert > 0$$이다. 이제 [정의 2](#def2)에 의해 각각에 대응하는 $$\delta_1, \delta_2 > 0$$이 존재하여 다음 두 조건

$$0 < \lvert x-a\rvert < \delta_1\implies \lvert f(x) - L\rvert < \epsilon,\qquad 0 < \lvert x-a\rvert < \delta_2\implies\lvert f(x) - L'\rvert < \epsilon$$

을 만족하도록 할 수 있다. 이제 $$\delta = \min(\delta_1, \delta_2)$$로 두면 $$0 < \lvert x-a\rvert < \delta$$인 $$x$$에 대해 삼각부등식으로

$$\lvert L - L'\rvert \leq \lvert L - f(x)\rvert + \lvert f(x) - L'\rvert < \epsilon + \epsilon = \lvert L - L'\rvert$$

이 되어 모순이다. 따라서 $$L = L'$$이다.

</details>

한편, [정의 2](#def2)는 원칙적으로 함수의 극한값의 후보 $$L$$이 주어졌을 때 그 극한값이 실제로 $$L$$이 맞다는 것을 보일 때만 사용할 수 있다. 즉, 이는 함수의 극한값이 <em-ko>무엇인지</em-ko> 알려주는 도구는 아니다. 이를 위해서는 다음 명제가 유용하다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (극한법칙)**</ins> $$\lim_{x\to a} f(x) = L$$, $$\lim_{x\to a} g(x) = M$$이라 하자. 그러면

1. $$\lim_{x\to a} \bigl(f(x) + g(x)\bigr) = L + M$$,
2. 임의의 상수 $$c$$에 대해 $$\lim_{x\to a} cf(x) = cL$$,
3. $$\lim_{x\to a} f(x)g(x) = LM$$,
4. $$M \neq 0$$이면 $$\lim_{x\to a} f(x)/g(x) = L/M$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. 양수 $$\epsilon > 0$$이 주어졌을 때, $$\epsilon/2$$에 대응하는 $$\delta_1, \delta_2 > 0$$을 각각 $$f, g$$의 극한 정의에서 얻을 수 있다. 그럼 $$\delta = \min(\delta_1,\delta_2)$$로 두면, $$0 < \lvert x-a\rvert < \delta$$일 때
    
    $$\lvert (f(x)+g(x)) - (L+M)\rvert \leq \lvert f(x)-L\rvert + \lvert g(x)-M\rvert < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
    
    이다. 
2. 만일 $$c=0$$이면 아무런 $$\delta$$를 잡아도 상관없으므로 자명하다. $$c \neq 0$$이면 $$\epsilon/\lvert c\rvert$$에 대응하는 $$\delta$$를 잡으면 된다.

3. 다음의 부등식
    
    $$\lvert f(x)g(x) - LM\rvert = \lvert f(x)(g(x)-M) + M(f(x)-L)\rvert \leq \lvert f(x)\rvert\,\lvert g(x)-M\rvert + \lvert M\rvert\,\lvert f(x)-L\rvert$$
    
    을 사용한다. 그럼 직관적으로 $$x$$가 $$a$$로 갈 때 $$\lvert g(x)-M\rvert$$와 $$\lvert f(x)-L\rvert$$는 모두 $$0$$으로 가므로, 만일 그 앞에 붙는 $$\lvert f(x)\rvert, \lvert g(x)\rvert$$들이 유한하다는 것만 보장된다면 위의 1번과 비슷한 계산을 통해 이를 $$\epsilon$$보다 작게 만들 수 있다. 
    
    트릭은 $$\epsilon=1$$로 두고 [정의 2](#def2)를 $$f$$와 $$g$$ 각각에 적용하는 것이다. 그럼 적당한 $$\delta_1, \delta_2$$가 존재하여
        
    $$0<\lvert x-a\rvert<\delta_1\implies 0<\lvert f(x)-L\rvert<1\implies \lvert f(x)\rvert< \lvert L\rvert+1$$

    이도록 할 수 있고, 비슷하게 $$\lvert g(x)\rvert <\lvert M\rvert+1$$이도록 하는 $$\delta$$도 잡을 수 있다. 이제 $$\delta$$를 이들 두 조건과, 다음 두 조건
    
    $$\lvert g(x)-M\rvert < \frac{\epsilon}{2(\lvert L\rvert+1)},\qquad \lvert f(x)-L\rvert < \frac{\epsilon}{2(\lvert M\rvert+1)}$$
    
    이 모두 성립하도록 잡으면 된다. 

4. $$1/g(x) \to 1/M$$을 보인 뒤 3을 적용하면 된다. $$M \neq 0$$이므로 $$a$$ 근방에서 $$\lvert g(x)\rvert > \lvert M\rvert/2$$이고,

$$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert\,\lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert$$

이므로 $$\lvert g(x)-M\rvert$$을 충분히 작게 만들면 된다.

</details>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6 (거듭제곱과 거듭제곱근의 극한)**</ins> $$\lim_{x\to a} f(x) = L$$이면

1. 임의의 양의 정수 $$k$$에 대해 $$\lim_{x\to a} \bigl(f(x)\bigr)^k = L^k$$,
2. $$L > 0$$이면 임의의 양의 정수 $$k$$에 대해 $$\lim_{x\to a} \sqrt[k]{f(x)} = \sqrt[k]{L}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. [명제 5](#prop5)의 3을 적용하여 $$k$$에 대한 귀납법을 돌리면 된다.
2. 먼저 $$L > 0$$이므로, $$\epsilon_1 = L/2$$에 대응하는 $$\delta_1 > 0$$을 잡으면 
    
    $$0 < \lvert x-a\rvert < \delta_1\implies\lvert f(x)-L\rvert < L/2$$
    
    이므로 $$f(x) > L/2 > 0$$이다. 한편, 임의의 양의 실수 $$u,v$$에 대해 다음 전개
    
    $$u - v = \bigl(u^{1/k}-v^{1/k}\bigr)\bigl(u^{(k-1)/k}+u^{(k-2)/k}v^{1/k}+\cdots+v^{(k-1)/k}\bigr)$$
    
    를 생각하면 우변 둘째 인자의 각 항은 $$\min(u,v)^{(k-1)/k}$$보다 크므로
    
    $$\bigl\lvert u^{1/k}-v^{1/k}\bigr\rvert \leq \frac{\lvert u-v\rvert}{k\,\min(u,v)^{(k-1)/k}}$$
    
    가 성립한다. 따라서 $$0 < \lvert x-a\rvert < \delta_1$$이면 $$0<L/2 < \min(f(x), L)$$이므로, $$f(x)=u$$, $$L=v$$를 대입하여
    
    $$\bigl\lvert \sqrt[k]{f(x)}-\sqrt[k]{L}\bigr\rvert \leq \frac{\lvert f(x)-L\rvert}{k\,(L/2)^{(k-1)/k}}$$
    
    를 얻는다. 이제 임의의 $$\epsilon > 0$$에 대해 $$k\,(L/2)^{(k-1)/k}\,\epsilon$$에 대응하는 $$\delta_2 > 0$$을 택하고 $$\delta = \min(\delta_1,\delta_2)$$로 두면, $$0 < \lvert x-a\rvert < \delta$$일 때 우변이 $$\epsilon$$보다 작아진다.

</details>

이 법칙들을 조합하면 다항함수의 극한은 각 항의 극한으로 분리하여 계산할 수 있다. 핵심은 다음 예시이다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 임의의 실수 $$a$$에 대하여, 

$$\lim_{x\rightarrow a}x=a$$

이다. 이는 $$\delta=\epsilon$$으로 잡으면 된다. 또, 임의의 실수 $$c$$에 대하여, 

$$\lim_{x\rightarrow a}c=c$$

이다. 이는 아무런 $$\delta$$나 잡아도 상관없다. 

</div>

그럼 임의의 다항함수 

$$f(x)=c_nx^n+\cdots +c_1x+c_0$$

에 대하여, [명제 5](#prop5)의 합·상수배 법칙으로 극한을 각 항으로 분리하고 거듭제곱에 [따름정리 6](#cor6)을 적용하면

$$\lim_{x\rightarrow a}f(x)=c_n\Bigl(\lim_{x\rightarrow a}x\Bigr)^n+\cdots +c_1\lim_{x\rightarrow a}x+\lim_{x\rightarrow a}c_0$$

이 되어, 마지막으로 [예시 7](#ex7)을 대입하면 $$\lim_{x\to a}f(x)=f(a)$$를 얻는다. 비슷한 방식으로, 다항함수의 비로 이루어진 유리함수의 극한도 분모의 극한이 $$0$$이 아니라면 분자와 분모의 극한의 비로 얻어진다.

## 조임정리와 극한의 대소관계

극한법칙만으로 계산되지 않는 극한은 종종 부등식으로 가두어 처리한다. 이 방법의 핵심 도구가 조임정리이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (조임정리)**</ins> 실수 $$a$$의 삭제된 근방에서 $$g(x) \leq f(x) \leq h(x)$$이고 $$\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$$이면 $$\lim_{x\to a} f(x) = L$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\epsilon > 0$$에 대해, $$g$$와 $$h$$의 극한 정의에서 얻은 $$\delta_1, \delta_2$$와 $$g \leq f \leq h$$가 성립하는 근방의 반지름 $$\delta_3$$을 모아 $$\delta = \min(\delta_1,\delta_2,\delta_3)$$으로 두자. $$0 < \lvert x-a\rvert < \delta$$이면 $$L - \epsilon < g(x) \leq f(x) \leq h(x) < L + \epsilon$$이므로 $$\lvert f(x) - L\rvert < \epsilon$$이다.

</details>

부등식과 극한이 어울리는 또 다른 기본 사실은 극한이 대소관계를 보존한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (극한의 대소 보존)**</ins> $$a$$의 근방에서 ($$a$$ 제외) $$f(x) \leq g(x)$$이고 두 극한 $$L = \lim_{x\to a}f(x)$$, $$M = \lim_{x\to a}g(x)$$이 존재하면 $$L \leq M$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L > M$$이라 가정하고 $$\epsilon = \frac{1}{2}(L - M) > 0$$으로 두자. 충분히 작은 근방에서 $$f(x) > L - \epsilon = \frac{L+M}{2}$$이고 $$g(x) < M + \epsilon = \frac{L+M}{2}$$이므로 $$f(x) > g(x)$$가 되어 가정에 모순이다. 따라서 $$L \leq M$$이다.

</details>

여기서 강한 부등식 $$f < g$$는 강한 부등식 $$L < M$$을 주지 않음에 유의한다. 예컨대 $$f(x) = 0 < x^2 = g(x)$$ ($$x \neq 0$$) 이지만 두 극한은 $$x \to 0$$에서 모두 $$0$$으로 같다. 즉 부등식은 극한에서 약해질 수 있다.

압착정리의 가장 유명한 응용은 다음의 삼각함수 극한으로, 미분에서 삼각함수를 다룰 때 결정적으로 쓰인다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$\lim_{x\to 0}(\sin x)/x = 1$$이다. $$0 < x < \pi/2$$에서 단위원의 넓이를 비교하면 부등식

$$\frac{1}{2}\sin x \leq \frac{1}{2}x \leq \frac{1}{2}\tan x$$

를 얻는다. 즉 $$\sin x \leq x \leq \tan x$$이다.

![삼각형-부채꼴-직각삼각형 넓이 비교](/assets/images/Math/Calculus/functions_and_limits-1.svg){:style="width:33.66em" class="invert" .align-center}

이제 위 부등식의 양변을 $$\sin x > 0$$으로 나누고 역수를 취하면

$$\cos x \leq \frac{\sin x}{x} \leq 1$$

임을 안다. 우리의 주장은 $$\cos x \to 1$$이라는 것이다. 이를 위해 삼각함수의 반각공식과 위에서 얻은 $$\sin(x/2) \leq x/2$$를 쓰면

$$0 \leq \lvert 1 - \cos x\rvert = \left\lvert2\sin^2\frac{x}{2}\right\rvert \leq 2\left(\frac{x}{2}\right)^2 = \frac{x^2}{2}$$

이므로 

$$-\frac{x^2}{2}\leq 1 - \cos x \leq \frac{x^2}{2}$$

이며, [명제 8](#prop8)를 적용하면 $$\cos x \to 1$$임을 안다. 이제 이를 이용하여 앞선 부등식에 다시 [명제 8](#prop8)를 적용하면 $$(\sin x)/x$$의 극한값이 $$1$$임을 안다. 

</div>

다음 예시 또한 고전적이다. 

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\lim_{x\to 0} x\sin(1/x) = 0$$이다. 이는 $$\bigl\lvert x\sin(1/x)\bigr\rvert \leq \lvert x\rvert$$이므로 

$$-\lvert x\rvert \leq x\sin\frac1x \leq \lvert x\rvert$$

이고, 양 끝이 $$0$$으로 가기 때문이다. 반면 $$\sin(1/x)$$ 자체는 $$x \to 0$$에서 극한을 갖지 않는데, $$x$$가 $$0$$에 다가가는 동안 $$-1$$과 $$1$$ 사이를 무한히 진동하기 때문이다. 인자 $$x$$가 이 진동을 $$0$$으로 눌러 주는 것이 조임정리의 기여이다.

</div>

## 한쪽 극한과 무한대에서의 극한

지금까지의 극한은 $$x$$가 $$a$$로 양쪽에서 다가가는 경우였다. 다가가는 방향을 한쪽으로 제한하거나, $$x$$ 또는 $$f(x)$$가 무한히 커지는 경우로 정의를 확장하면 함수의 모양을 더 세밀하게 기술할 수 있다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 실수 $$a$$와 함수 $$f$$에 대해, 적당한 $$c > 0$$에 대하여 $$f$$가 $$(a, a+c)$$에서 정의되어 있다고 하자. 실수 $$L$$이 $$x \to a^+$$일 때 $$f$$의 *오른쪽 극한<sub>right limit</sub>*이라는 것은, 임의의 $$\epsilon > 0$$에 대해 어떤 $$\delta > 0$$이 존재하여

$$a < x < a+\delta \implies \lvert f(x) - L\rvert < \epsilon$$

이 성립하는 것이다. 이 때 $$\lim_{x\to a^+} f(x) = L$$로 적는다. 비슷하게 $$f$$가 $$(a-c, a)$$에서 정의되어 있을 때, $$x \to a^-$$일 때의 *왼쪽 극한<sub>left limit</sub>*은

$$a-\delta < x < a \implies \lvert f(x) - L\rvert < \epsilon$$

으로 정의하고 $$\lim_{x\to a^-} f(x) = L$$로 적는다.

</div>

극한 $$\lim_{x\to a} f(x)$$가 존재하는 것은 두 한쪽 극한이 모두 존재하고 서로 같은 것과 동치이다. 가령 $$f(x) = \lvert x\rvert/x$$는 $$x \to 0^+$$에서 $$1$$, $$x \to 0^-$$에서 $$-1$$로 두 한쪽 극한이 다르므로 $$x \to 0$$에서의 극한은 존재하지 않는다. 이렇게 두 한쪽 극한이 유한하지만 서로 다른 점을 함수의 *도약<sub>jump</sub>* 불연속점이라 부른다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 실수 $$a$$의 삭제된 근방에서 정의된 함수 $$f$$에 대해, $$\lim_{x\to a} f(x) = \infty$$란 임의의 $$M > 0$$에 대해 어떤 $$\delta > 0$$이 존재하여 $$0 < \lvert x-a\rvert < \delta$$이면 $$f(x) > M$$인 것이다. 비슷하게 $$\lim_{x\to a} f(x) = -\infty$$란 임의의 $$M > 0$$에 대해 어떤 $$\delta > 0$$이 존재하여 $$0 < \lvert x-a\rvert < \delta$$이면 $$f(x) < -M$$인 것이다.

</div>

예컨대 $$\lim_{x\to 0}1/x^2 = \infty$$이며, 이 경우 직선 $$x = 0$$을 그래프의 *수직점근선<sub>vertical asymptote</sub>*이라 한다.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> 어떤 실수 $$N_0$$보다 큰 $$x$$에서 정의된 함수 $$f$$에 대해, $$\lim_{x\to\infty} f(x) = L$$이란 임의의 $$\epsilon > 0$$에 대해 어떤 $$N > N_0$$이 존재하여 

$$x > N\implies\lvert f(x) - L\rvert < \epsilon$$

인 것이다. 비슷하게 어떤 $$N_0$$보다 작은 $$x$$에서 정의된 함수에 대해 $$\lim_{x\to-\infty} f(x) = L$$은 

$$x < N\implies\lvert f(x) - L\rvert < \epsilon$$

이도록 하는 $$N$$이 존재하는 것이다.

</div>

가령 $$\lim_{x\to\infty}1/x = 0$$이고, 유리함수에서는 최고차항이 그 행동을 지배하여 $$\lim_{x\to\infty}(2x^2 + 1)/(3x^2 - x) = 2/3$$이다. 이러한 유한 극한 $$L$$이 존재하면 직선 $$y = L$$이 그래프의 *수평점근선<sub>horizontal asymptote</sub>*이 된다.

직접 대입이 $$0/0$$ 꼴의 부정형을 줄 때는 인수분해나 분자의 유리화 같은 대수적 변형으로 분모의 영점을 약분하여 극한법칙이 적용되는 형태로 바꾸면 된다. [예시 10](#ex10)의 $$\lim(\sin x)/x = 1$$ 또한 이러한 대수적 정리와 결합하여 $$\sin$$이 섞인 부정형을 처리하는 데 쓰인다.
