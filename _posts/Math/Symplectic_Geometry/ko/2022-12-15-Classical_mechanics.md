---

title: "고전역학"
excerpt: "고전역학과 phase space"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/classical_mechanics
header:
    overlay_image: /assets/images/Classical_mechanics.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2022-12-15
last_modified_at: 2022-12-15
weight: 1

---

이번 글에서는 사교기하에서 다루는 사교다양체가 도입된 역사적인 (물리적인) 배경을 살펴본다. 수학도로서 이곳저곳에서 주워들은 내용을 정리한 것이라 물리적으로는 오류가 조금 있을 수도 있다.

## 에너지 보존법칙

물리학, 특히 역학에는 물체의 운동을 서술하는 여러가지 공식이 있다. 가령 뉴턴의 운동법칙 $F=ma$는 물리학을 배우지 않은 사람이라도 모두 알고 있는 공식일 것이다. 

19세기 들어 물리학자들에게 명확해진 사실 중 하나는, 이러한 공식들이 물체의 운동을 결정하는 것이 아니라 어떤 하나의 함수가 물체의 운동을 결정한다는 것이다. 어떻게 보면 이 사실은 <em_ko>에너지 보존법칙</em_ko>과도 어느정도 관련이 있다고 할 수 있다. 

이를 살펴보가 위해 하나의 축은 물체의 위치를, 다른 축은 물체의 운동량을 나타내는 *phase space<sub>위상공간</sub>*를 생각하자.  예를 들어, 1차원 공간에 해당하는 phase space는 위치 축과 운동량 축 하나씩으로 이루어진 2차원 공간이 될 것이고, 일반적으로 $n$차원 공간의 phase space는 $n$차원의 위치좌표와 $n$차원의 운동량좌표로 이루어진 $2n$차원 공간이 될 것이다.

img

이러한 상황에서, 운동에너지 $K=\frac{1}{2}mv^2$ 혹은 위치에너지 $P=mgh$ 등은 상수인 $m$, $g$를 제외하면 위치좌표와 속도좌표를 통해 기술할 수 있는 물리량이 된다. 즉, 이들 에너지들은 phase space에서 $\mathbb{R}$로의 함수이다. 그럼 에너지 보존법칙은 물체의 운동을 phase space에 기술하였을 때, 그 궤적은 에너지 함수의 등위면에 완전하게 포함되어야 한다는 것을 의미한다. 

가령 어떠한 힘도 작용하지 않는 1차원 상에서의 물체의 운동을 생각하자. 즉, 이 물체가 가지는 에너지는 오직 운동에너지 뿐이므로, 우리는 에너지 함수 $E:\mathbb{R}^2\rightarrow\mathbb{R}$을 $E(x,v)=v^2$이라 생각할 수 있다. 그럼 $E$의 등위면은 위치축과 평행하게 그려지는 선분들이다.

img

에너지 보존법칙에 의하면, 시작점이 phase space 상의 한 점인 물체는 시간이 얼마나 흐르든 이 등위면을 벗어날 수 없다. 이를 물리적으로 해석하자면, 외부의 힘이 작용하지 않을 때 물체의 가속도는 0인 것으로 해석할 수 있다.

고등학교 때 배우는 역학적 에너지 보존법칙은 일반적으로 운동에너지와 위치에너지의 합이 변하지 않는다는 것을 의미한다. 위와 비슷하게 그림을 그려보면 에너지 함수의 등위면은 대략적으로 다음과 같다.

img

마찬가지로 에너지 보존법칙에 의하면 물체의 운동은 항상 이 에너지의 등위면 위에 있어야 한다.

마지막으로 용수철에 달린 물체의 운동을 생각하자. Hooke's law에 따르면 용수철이 물체에 부여하는 위치에너지는 $\frac{1}{2}kx^2$으로 주어진다. 물체의 운동에너지는 $\frac{1}{2}mv^2$이므로, 에너지 함수 $E$를 $E(x,v)=\frac{1}{2}kx^2+\frac{1}{2}mv^2$으로 정의하면 된다. 이를 phase space 상에 그리면 다음과 같이 타원 형태가 나오게 된다.

img

이는 물체의 운동이 주기운동이 될 것임을 암시한다.

위의 그림은 물체가 운동하는 차원이 1차원일 경우는 말이 되지만, 물체가 운동하는 차원이 2차원만 되더라도 phase space는 4차원이 되고, 따라서 에너지 등위면은 3차원이 되므로 이 안에서 물체가 실제로 어떠한 곡선을 따라 움직이는지를 설명하기 위해서는 추가적인 도구가 필요하다. 

## 최소작용의 원리

이 과정에서 중요한 역할을 하는 것은 다음 <em_ko>최소작용의 원리</em_ko>이다.

> 물체가 $x_0$에서 $x_1$로 움직일 때, 이 물체는 다음의 *액션*을 최소로 하는 경로 $z(t)=(x(t),y(t))$ ($t_0\leq t\leq t_1$)를 따라 움직인다.
> 
> $$\mathcal{A}_H(z)=\int_{t_0}^{t_1}\langle y,\dot{x}\rangle-H(z)\mathop{dt}$$

식에서 새로 도입한 $H$는 *Hamiltonian<sub>해밀토니안</sub>*을 의미하며, 앞으로 할 이야기에서는 그냥 에너지라 생각해도 무방하다. 수학적으로 이러한 $\mathcal{A}_H(z)$를 어떻게 다루는지는 아주 잘 알려져있으며, 이를 따라 계산을 해 보면 다음 *Hamilton's equation*

$$\dot{x}=\frac{\partial H}{\partial y},\quad \dot{y}=-\frac{\partial H}{\partial x}$$

을 얻는다.

$\mathbb{R}^{2n}$에서 정의된 almost complex structure $J_0$을 생각하면, 위의 식은 간략하게

$$\dot{z}=-J_0\nabla H(z)$$

으로 적을 수 있다. 직관적으로, gradient $\nabla H$는 $H$의 변화량을 가장 크게 하는 방향, 곧 $H$의 등위면에 수직인 방향을 가리키므로 $J_0$를 통해 이를 다시 90도 돌려 $H$의 등위면과 평행한 방향으로 만든 것이 $\dot{z}$인 것으로 생각할 수 있다. 

이제 물체가 실제로 운동하는 경로, 즉 $z$를 찾는 것은 다음의 *Hamiltonian vector field*

$$X_H=-J_0\nabla H(z)$$

의 integral flow를 찾는 문제와 정확하게 같아지며, 우리는 이것이 항상 가능하다는 것을 알고 있다. ([\[미분다양체\] §벡터장, ⁋정리 6](/ko/math/manifold/vector_fields#thm6))

## Symplectic form

위의 과정을 요약하자면, 해밀토니안 $H$는 다음의 식

$$dH=\langle-J_0\nabla H(z), -\rangle$$

을 통해 물체의 운동을 기술한다. 이제 $\mathbb{R}^{2n}$ 위에 $2$-form

$$\omega_0(-,-):=\langle J_0-, -\rangle$$

을 정의하면, 위의 식은 함수 $f$의 gradient $f$가 $df=\langle \nabla f,-\rangle$을 정의하는 것과 유사하게

$$dH=\omega_0(X_H, -)$$

으로 적을 수 있다. $\omega_0$는 $\mathbb{R}^{2n}$ 위에 정의된 *canonical symplectic form*이라 부르고, 이러한 관점에서 $X_H$를 *symplectic gradient*라고 부르기도 한다.

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: 엄밀하게 말하자면 속도에 해당하는 축이 아니라 운동량(momentum)에 해당하는 축이다. 이는 속도가 tangent vector인데 반해, 운동량은 cotangent space의 원소이기 때문이다. 한편, phase space의 한글명은 topological space와 겹치지만 어차피 이 블로그에서는 phase space를 언급할 일이 별로 없다.