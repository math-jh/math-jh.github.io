---
title: "거리공간과 열린집합·닫힌집합"
description: "거리의 공리와 ℝⁿ, 이산거리, C[a,b]의 상한노름 같은 표준 예시를 정리하고, 열린공에서 출발하여 수렴, 열린집합과 닫힌집합, closure, 부분공간, dense subset을 정의한다. 닫힌집합의 수열 판정, 무한 교집합·합집합의 반례, 동치인 거리를 증명과 함께 다루고 Cantor 집합이 닫혀 있고 내부가 비어 있으며 비가산임을 보인다."
excerpt: "거리공리와 표준 예시, 열린집합·닫힌집합·closure와 수열 판정, 부분공간, dense subset, Cantor 집합"

categories: [Math / Analysis]
permalink: /ko/math/analysis/metric_spaces
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 8

published: false

---

[§수열의 수렴, ⁋정의 1](/ko/math/analysis/convergence_of_sequences#def1)에서 $a_n \to L$을 정의할 때 쓴 것은 실수의 사칙연산이 아니라 두 점 사이의 거리 $\lvert a_n - L\rvert$뿐이었다. 따라서 거리가 몇 가지 성질을 만족하는 집합이라면 어디서든 같은 정의가 의미를 가지고, 수렴을 다루는 논증도 거의 그대로 옮겨 간다. 이 글에서는 그 성질을 공리로 적은 거리공간을 정의하고, 거리에서 열린집합과 닫힌집합, closure가 어떻게 나오는지를 정리한다. 이후 연속성과 compactness는 모두 이 언어로 서술된다.

## 거리공간

::: 정의 1
집합 $X$와 함수 $d : X \times X \to \mathbb{R}$가 모든 $x, y, z \in X$에 대하여 다음을 만족하면 $(X, d)$를 *거리공간<sub>metric space</sub>*, $d$를 $X$ 위의 *거리<sub>metric</sub>*라 한다.

1. $d(x, y) \geq 0$이고, $d(x, y) = 0$인 것은 $x = y$인 것과 동치이다.
2. $d(x, y) = d(y, x)$.
3. $d(x, z) \leq d(x, y) + d(y, z)$.
:::

세 번째 조건이 삼각부등식이다. 거리가 $\mathbb{R}$의 표준 거리일 때는 $\lvert x - z\rvert = \lvert (x-y) + (y-z)\rvert \leq \lvert x - y\rvert + \lvert y - z\rvert$로 알려진 사실이다. 공리는 셋뿐이지만 어느 하나도 생략할 수 없다. 다음 반례들은 각각 하나의 공리만 깨뜨린다.

::: 예시 2 (공리가 하나씩 깨지는 경우)
1. $\mathbb{R}$ 위의 $d(x, y) = (x - y)^2$은 첫째와 둘째 공리를 만족하지만 삼각부등식이 깨진다. $d(0, 2) = 4$인데 $d(0, 1) + d(1, 2) = 2$이다.
2. $\mathbb{R}$ 위의 $d(x, y) = \lvert x^2 - y^2\rvert$은 대칭이고 삼각부등식도 만족하지만, $d(1, -1) = 0$이므로 $d(x,y) = 0 \implies x = y$가 깨진다.
3. $\mathbb{R}$ 위의 $d(x, y) = y - x$는 삼각부등식을 등식으로 만족하지만 $x > y$이면 음수이고 대칭도 아니다. 비음성을 $d(x, y) = \max\{y - x, 0\}$으로 고치면 삼각부등식은 유지되지만 이번에는 $d(1, 0) = 0$이어서 $d(x,y) = 0 \implies x = y$와 대칭성이 모두 깨진다.
:::

### $\mathbb{R}^n$의 세 거리

$x = (x_1, \dots, x_n)$, $y = (y_1, \dots, y_n) \in \mathbb{R}^n$에 대하여

$$d_1(x, y) = \sum_{i=1}^n \lvert x_i - y_i\rvert, \qquad d_2(x, y) = \Bigl(\sum_{i=1}^n (x_i - y_i)^2\Bigr)^{1/2}, \qquad d_\infty(x, y) = \max_{1 \leq i \leq n} \lvert x_i - y_i\rvert$$

로 둔다. $d_2$가 유클리드 거리이다. 세 함수 모두 비음성과 대칭성은 정의에서 바로 나오며, $d_1(x,y) = 0$, $d_2(x,y) = 0$, $d_\infty(x,y) = 0$은 모두 모든 $i$에 대하여 $x_i = y_i$인 것과 동치이다.

::: 명제 3
$d_1, d_2, d_\infty$는 모두 $\mathbb{R}^n$ 위의 거리이고, 모든 $x, y \in \mathbb{R}^n$에 대하여

$$d_\infty(x, y) \leq d_2(x, y) \leq d_1(x, y) \leq n d_\infty(x, y)$$

가 성립한다.
:::

::: 증명
삼각부등식을 보이기 위해 $u = x - y$, $v = y - z$로 두자. 그럼 $x - z = u + v$이고, 좌표별로 $\lvert u_i + v_i\rvert \leq \lvert u_i\rvert + \lvert v_i\rvert$이다. 이 부등식을 $i$에 대해 더하면 $d_1$의 삼각부등식이 되고, $i$에 대해 최댓값을 취하면 $\max_i \lvert u_i + v_i\rvert \leq \max_i \lvert u_i\rvert + \max_i \lvert v_i\rvert$이 되어 $d_\infty$의 삼각부등식이 된다.

$d_2$의 경우 $\lVert u\rVert_2 = (\sum u_i^2)^{1/2}$으로 적자. 먼저 Cauchy–Schwarz 부등식 $\sum u_i v_i \leq \lVert u\rVert_2 \lVert v\rVert_2$를 보인다. $u = 0$이면 자명하다. $u \neq 0$이면 모든 $t \in \mathbb{R}$에 대하여

$$0 \leq \sum_{i=1}^n (u_i t + v_i)^2 = \lVert u\rVert_2^2 t^2 + 2\Bigl(\sum_{i=1}^n u_i v_i\Bigr) t + \lVert v\rVert_2^2$$

이고, $t$에 대한 이차식이 항상 $0$ 이상이므로 판별식이 $0$ 이하이다. 이는 $(\sum u_i v_i)^2 \leq \lVert u\rVert_2^2 \lVert v\rVert_2^2$이다. 이제

$$\lVert u + v\rVert_2^2 = \lVert u\rVert_2^2 + 2\sum_{i=1}^n u_i v_i + \lVert v\rVert_2^2 \leq (\lVert u\rVert_2 + \lVert v\rVert_2)^2$$

이므로 양변의 제곱근을 취하면 $d_2(x,z) \leq d_2(x,y) + d_2(y,z)$이다.

부등식 사슬에서 $d_\infty \leq d_2$는 $d_2^2$가 $\max_i (x_i - y_i)^2$을 한 항으로 포함하기 때문이다. $d_2 \leq d_1$은 음이 아닌 $a_i = \lvert x_i - y_i\rvert$에 대하여 $(\sum a_i)^2 = \sum a_i^2 + \sum_{i \neq j} a_i a_j \geq \sum a_i^2$이기 때문이다. $d_1 \leq n d_\infty$는 $n$개의 항이 각각 $d_\infty$ 이하이기 때문이다.
:::

### 이산거리와 상한노름

임의의 집합 $X$ 위에 $x \neq y$이면 $d(x, y) = 1$, $x = y$이면 $d(x, y) = 0$으로 정한 것이 *이산거리<sub>discrete metric</sub>*이다. 삼각부등식은 $d(x, z) = 1$인 경우만 보면 된다. 이때 $x \neq z$이므로 $y$는 $x$ 또는 $z$와 달라서 우변이 $1$ 이상이다. 이산거리는 점들 사이의 가까움에 대한 정보를 전혀 담지 않는 극단적인 거리이며, 아래에서 여러 번 반례로 쓰인다.

닫힌구간 $[a,b]$ 위의 연속함수 전체를 $C[a,b]$로 적고

$$d(f, g) = \max_{x \in [a,b]} \lvert f(x) - g(x)\rvert$$

로 정한다. 연속함수 $\lvert f - g\rvert$는 [\[미적분학\] §연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)에 의하여 닫힌구간에서 최댓값을 가지므로 $d(f,g)$는 유한한 실수이다. $d(f,g) = 0$이면 모든 $x$에서 $f(x) = g(x)$이고, 대칭성은 자명하다. 삼각부등식은 각 $x \in [a,b]$에서

$$\lvert f(x) - h(x)\rvert \leq \lvert f(x) - g(x)\rvert + \lvert g(x) - h(x)\rvert \leq d(f, g) + d(g, h)$$

이고 좌변의 최댓값이 $d(f,h)$이므로 얻어진다. 이 거리를 *상한노름* 거리라 한다. 점 $x$를 하나 고정하고 값만 비교하는 것이 아니라 구간 전체에서의 최대 편차를 재는 거리이다.

### 노름공간

위의 예 가운데 $d_1, d_2, d_\infty$와 $C[a,b]$의 거리는 모두 차 $x - y$의 크기로 주어진다. 이 구조를 따로 정리해 둔다.

::: 정의 4
실벡터공간 $V$ 위의 함수 $\lVert \cdot \rVert : V \to \mathbb{R}$가 모든 $x, y \in V$와 $\lambda \in \mathbb{R}$에 대하여 $\lVert x\rVert \geq 0$이고 $\lVert x\rVert = 0 \iff x = 0$, $\lVert \lambda x\rVert = \lvert \lambda\rvert \lVert x\rVert$, $\lVert x + y\rVert \leq \lVert x\rVert + \lVert y\rVert$를 만족하면 $\lVert \cdot \rVert$를 *norm<sub>노름</sub>*, $(V, \lVert \cdot \rVert)$를 *normed space<sub>노름공간</sub>*이라 한다.
:::

노름공간은 $d(x, y) = \lVert x - y\rVert$로 거리공간이 된다. $d(x,y) = 0 \iff x = y$는 첫째 조건에서, 대칭성은 $\lVert -z\rVert = \lVert z\rVert$에서, 삼각부등식은 $\lVert x - z\rVert = \lVert (x - y) + (y - z)\rVert \leq \lVert x - y\rVert + \lVert y - z\rVert$에서 나온다. $d_1, d_2, d_\infty$는 각각 $\lVert x\rVert_1 = \sum \lvert x_i\rvert$, $\lVert x\rVert_2$, $\lVert x\rVert_\infty = \max \lvert x_i\rvert$에서 얻어지고, $C[a,b]$의 거리는 상한노름 $\lVert f\rVert = \max_x \lvert f(x)\rvert$에서 얻어진다.

모든 거리가 노름에서 나오는 것은 아니다. $\mathbb{R}^n$ 위의 이산거리가 노름에서 나온다면 $d(\lambda x, 0) = \lvert \lambda\rvert d(x, 0)$이어야 하는데, $x \neq 0$이고 $\lambda = 2$이면 좌변은 $1$, 우변은 $2$이다.

## 열린공과 수렴

::: 정의 5
거리공간 $(X, d)$, 점 $x \in X$, 실수 $r > 0$에 대하여

$$B(x, r) = \{y \in X \mid d(x, y) < r\}$$

을 중심 $x$, 반지름 $r$인 *열린공<sub>open ball</sub>*이라 한다.
:::

$\mathbb{R}$의 표준 거리에서 $B(x, r) = (x - r, x + r)$이고, $(\mathbb{R}^2, d_2)$에서는 원판, $d_\infty$에서는 변의 길이가 $2r$인 정사각형의 내부, $d_1$에서는 마름모의 내부이다. 같은 집합에 거리를 바꾸면 열린공의 모양이 달라진다. 이산거리에서는 $r \leq 1$이면 $B(x, r) = \{x\}$이고 $r > 1$이면 $B(x, r) = X$이다.

::: 정의 6
거리공간 $(X, d)$의 점열 $(x_n)$이 $x \in X$로 *수렴*한다는 것은 $d(x_n, x) \to 0$인 것이다. 곧 임의의 $\varepsilon > 0$에 대하여 $N$이 존재하여 $n \geq N$이면 $x_n \in B(x, \varepsilon)$이다.
:::

정의에서 $\varepsilon$은 임의로 주어지고 $N$이 그에 맞추어 고른다는 점이 [§수열의 수렴, ⁋정의 1](/ko/math/analysis/convergence_of_sequences#def1)과 같다. 달라진 것은 $\lvert x_n - x\rvert < \varepsilon$이 $x_n \in B(x, \varepsilon)$으로 바뀐 것뿐이다.

::: 명제 7
거리공간에서 점열의 극한은 존재하면 유일하다.
:::

::: 증명
$x_n \to x$이고 $x_n \to x'$라 하자. 임의의 $\varepsilon > 0$에 대하여 $d(x_n, x) < \varepsilon/2$이고 $d(x_n, x') < \varepsilon/2$인 $n$이 있다. 삼각부등식과 대칭성에 의해 $d(x, x') \leq d(x, x_n) + d(x_n, x') < \varepsilon$이다. $\varepsilon$이 임의의 양수이므로 $d(x, x') = 0$이고, 첫째 공리에 의해 $x = x'$이다. 여기서 $\varepsilon/2$를 택한 이유는 두 항의 합이 $\varepsilon$을 넘지 않게 하기 위해서이다.
:::

몇 가지 거리에서 수렴이 어떤 모양인지 살펴본다. 이산거리에서 $\varepsilon = 1/2$로 두면 $d(x_n, x) < 1/2$은 $x_n = x$와 같으므로, 수렴하는 점열은 어떤 번호부터 상수열이 되는 점열뿐이다. $(\mathbb{R}^n, d_\infty)$에서는 $d_\infty(x^{(k)}, x) < \varepsilon$이 모든 좌표에서 $\lvert x_i^{(k)} - x_i\rvert < \varepsilon$인 것과 같고, [명제 3](#prop3)의 부등식 때문에 $d_1$, $d_2$에서의 수렴과 같은 점열이 수렴한다. 따라서 $\mathbb{R}^n$에서의 수렴은 각 좌표의 수렴과 같다. $C[a,b]$의 상한노름 거리에서 $f_n \to f$는 $\max_x \lvert f_n(x) - f(x)\rvert \to 0$, 곧 구간 전체에서 동시에 $f_n(x)$가 $f(x)$에 가까워진다는 뜻이다. 각 점에서만 $f_n(x) \to f(x)$인 것은 이보다 약한 조건이며 이 거리의 수렴이 아니다.

## 열린집합과 닫힌집합

::: 정의 8
거리공간 $X$의 subset $A$와 점 $x \in A$에 대하여, $B(x, r) \subseteq A$인 $r > 0$이 존재하면 $x$를 $A$의 *interior point<sub>내부점</sub>*이라 한다. $A$의 모든 점이 $A$의 interior point이면 $A$를 *열린집합<sub>open set</sub>*이라 한다.
:::

열린집합은 속한 어느 점에서도 사방으로 조금의 여유가 있는 집합이다. 이 여유의 크기는 점마다 다르게 잡아도 된다. 열린공이 이름대로 열린집합이라는 사실은 삼각부등식에서 나온다.

::: 명제 9
열린공 $B(x, r)$은 열린집합이다.
:::

::: 증명
$y \in B(x, r)$이면 $s = r - d(x, y) > 0$이다. $z \in B(y, s)$이면 $d(x, z) \leq d(x, y) + d(y, z) < d(x, y) + s = r$이므로 $z \in B(x, r)$이다. 따라서 $B(y, s) \subseteq B(x, r)$이다.
:::

::: 명제 10
거리공간 $X$에서 다음이 성립한다.

1. $\emptyset$과 $X$는 열린집합이다.
2. 열린집합들의 임의의 합집합은 열린집합이다.
3. 유한개의 열린집합의 교집합은 열린집합이다.
:::

::: 증명
(1) $\emptyset$에는 확인할 점이 없고, $X$에서는 임의의 $x$에 대하여 임의의 $r > 0$이 $B(x,r) \subseteq X$를 만족한다. (2) $x \in \bigcup_\alpha U_\alpha$이면 어떤 $\alpha$에 대하여 $x \in U_\alpha$이고, $U_\alpha$가 열려 있으므로 $B(x, r) \subseteq U_\alpha \subseteq \bigcup_\alpha U_\alpha$인 $r$이 있다. (3) $x \in U_1 \cap \dots \cap U_n$이면 각 $i$에 대하여 $B(x, r_i) \subseteq U_i$인 $r_i > 0$이 있다. $r = \min\{r_1, \dots, r_n\}$으로 두면 $B(x, r) \subseteq B(x, r_i) \subseteq U_i$가 모든 $i$에서 성립하므로 $B(x, r) \subseteq \bigcap_i U_i$이다. 여기서 개수가 유한해야 $r > 0$이 보장된다.
:::

(3)에서 유한이라는 조건은 빠질 수 없다. $\mathbb{R}$에서 $\bigcap_{n \geq 1} (-1/n, 1/n) = \{0\}$이고, $\{0\}$은 어떤 $B(0, r) = (-r, r)$도 담지 못하므로 열린집합이 아니다. 각 $(-1/n, 1/n)$에서 허용되는 반지름이 $1/n$으로 줄어들어 $0$으로 가기 때문이다.

집합 $A$의 interior point 전체를 $A$의 *interior* $A^\circ$로 적는다. $A^\circ$는 $A$에 포함된 열린집합 가운데 가장 큰 것이다. 우선 $x \in A^\circ$이면 $B(x, r) \subseteq A$인 $r$이 있고, [명제 9](#prop9)에 의해 $B(x,r)$의 모든 점 $y$가 $B(y, s) \subseteq B(x, r) \subseteq A$인 $s$를 가지므로 $B(x, r) \subseteq A^\circ$이다. 따라서 $A^\circ$는 열린집합이다. 또 $A$에 포함된 열린집합 $U$의 모든 점은 정의에 의해 $A$의 interior point이므로 $U \subseteq A^\circ$이다. 열린집합은 $A = A^\circ$인 집합으로 말해도 같다.

### 극한점과 닫힌집합

::: 정의 11
$A \subseteq X$이고 $x \in X$이다. 모든 $r > 0$에 대하여 $B(x, r)$이 $x$가 아닌 $A$의 점을 포함하면 $x$를 $A$의 *limit point<sub>극한점</sub>*이라 한다. 여집합 $X \setminus F$가 열린집합인 subset $F$를 *닫힌집합<sub>closed set</sub>*이라 한다.
:::

Limit point는 $A$ 바깥에 있을 수도 있고 $A$ 안에 있을 수도 있다. $A = \{1/n \mid n \geq 1\}$의 limit point는 $0$ 하나이고, $A$의 점 $1/n$은 반지름이 $\frac{1}{n} - \frac{1}{n+1}$보다 작은 열린공이 $A$의 다른 점을 담지 못하므로 limit point가 아니다. 한편 $A = [0, 1) \cup \{2\}$에서 점 $2$는 $A$에 속하지만 limit point가 아니다. 이 구분은 아래 closure에서 다시 쓰인다.

닫힌집합은 정의상 열린집합의 여집합이지만, 해석학에서 쓰는 모습은 수열의 극한에 대해 닫혀 있다는 것이다. 다음 명제가 둘을 이어 준다.

::: 명제 12
거리공간 $X$의 subset $F$에 대하여 다음은 동치이다.

1. $F$는 닫힌집합이다.
2. $F$의 모든 limit point가 $F$에 속한다.
3. $F$의 점으로 이루어진 점열이 $X$의 점 $x$로 수렴하면 $x \in F$이다.
:::

::: 증명
(1) $\Rightarrow$ (2). $x$가 $F$의 limit point인데 $x \notin F$라 하자. $X \setminus F$가 열려 있으므로 $B(x, r) \subseteq X \setminus F$인 $r$이 있다. 그러나 limit point이므로 $B(x, r)$은 $F$의 점을 포함하여 모순이다.

(2) $\Rightarrow$ (3). $x_n \in F$, $x_n \to x$라 하자. 어떤 $n$에 대하여 $x_n = x$이면 $x \in F$이다. 모든 $n$에 대하여 $x_n \neq x$이면, 임의의 $r > 0$에 대하여 큰 $n$에서 $x_n \in B(x, r)$이므로 $B(x, r)$은 $x$가 아닌 $F$의 점을 포함한다. 곧 $x$는 limit point이고 (2)에 의해 $x \in F$이다.

(3) $\Rightarrow$ (1). $X \setminus F$가 열려 있지 않다고 하고 모순을 이끈다. 그럼 어떤 $x \in X \setminus F$가 있어 모든 $r > 0$에서 $B(x, r) \not\subseteq X \setminus F$, 곧 $B(x, r) \cap F \neq \emptyset$이다. $r = 1/n$으로 두어 각 $n$마다 $x_n \in B(x, 1/n) \cap F$를 하나씩 택하면, $d(x_n, x) < 1/n$이므로 $x_n \to x$이다. (3)에 의해 $x \in F$인데 이는 $x \in X \setminus F$에 모순이다. 반지름을 $1/n$으로 고른 것은 점열이 $x$로 수렴하도록 하기 위해서이다.
:::

여집합과 드모르간 법칙 $X \setminus \bigcap_\alpha F_\alpha = \bigcup_\alpha (X \setminus F_\alpha)$, $X \setminus \bigcup_{i=1}^n F_i = \bigcap_{i=1}^n (X \setminus F_i)$를 [명제 10](#prop10)에 적용하면, $\emptyset$과 $X$는 닫혀 있고 닫힌집합의 임의의 교집합과 유한 합집합은 닫혀 있다. 열린집합과 마찬가지로 개수의 조건은 필요하다. $\bigcup_{n \geq 2} [1/n, 1] = (0, 1]$은 닫힌구간들의 합집합이지만 $\mathbb{R}$에서 닫혀 있지 않다. $1/n \in (0,1]$이 $0 \notin (0,1]$로 수렴하기 때문이다.

열린집합과 닫힌집합은 서로의 부정이 아니다. $[a, b)$는 $a$에서 왼쪽으로 새어 나가므로 열려 있지 않고, $b - 1/n$이 $b \notin [a, b)$로 수렴하므로 닫혀 있지도 않다. 반대로 $\emptyset$과 $X$는 둘 다이며, 이처럼 열리면서 닫힌 집합을 *clopen set<sub>열린닫힌집합</sub>*이라 한다. 이산거리 공간에서는 모든 subset이 clopen set이다. $r \leq 1$인 열린공이 한 점이므로 모든 singleton이 열려 있고, 임의의 집합은 singleton들의 합집합이라 열려 있으며, 여집합도 같은 이유로 열려 있기 때문이다. 또 열림과 닫힘은 집합 자체의 성질이 아니라 집합이 놓인 거리공간에 대한 성질이다. $(0, 1)$은 $\mathbb{R}$에서 열린집합이지만 닫혀 있지 않고, 거리공간 $(0, 1)$ 자신 안에서는 clopen이다. 이 내용은 아래 부분공간 절에서 정확히 다룬다.

## Closure

닫힌집합의 임의의 교집합이 닫혀 있으므로, 집합 $A$를 포함하는 모든 닫힌집합의 교집합은 $A$를 포함하는 가장 작은 닫힌집합이다.

::: 정의 13
$A \subseteq X$를 포함하는 모든 닫힌집합의 교집합을 $A$의 *closure<sub>폐포</sub>*라 하고 $\overline{A}$로 적는다.
:::

정의는 닫힌집합에 대한 것이지만 실제 계산에는 다음 특징화를 쓴다.

::: 명제 14
$A \subseteq X$에 대하여 다음 네 집합은 모두 같다.

1. $\overline{A}$.
2. $E = \{x \in X \mid \text{모든 } r > 0 \text{에 대하여 } B(x, r) \cap A \neq \emptyset\}$.
3. $A$의 점으로 이루어진 수렴하는 점열의 극한 전체.
4. $A$와 $A$의 limit point 전체의 합집합.
:::

::: 증명
(2) $=$ (4). $x \in E$이면 $x \in A$이거나 $x \notin A$이다. $x \notin A$이면 $B(x,r) \cap A$의 점은 $x$가 아니므로 $x$는 limit point이다. 거꾸로 $A$의 점은 $x \in B(x,r) \cap A$이고, limit point는 정의에서 $B(x,r) \cap A \neq \emptyset$이므로 $E$에 속한다.

(2) $=$ (3). $x \in E$이면 각 $n$마다 $x_n \in B(x, 1/n) \cap A$를 택할 수 있고 $x_n \to x$이다. 거꾸로 $A$의 점열 $x_n \to x$이면, 임의의 $r$에 대하여 큰 $n$에서 $x_n \in B(x,r) \cap A$이므로 $x \in E$이다.

(1) $=$ (2). 먼저 $E$가 닫힌집합임을 보인다. $x \notin E$이면 $B(x, r) \cap A = \emptyset$인 $r$이 있고, [명제 9](#prop9)의 증명에서처럼 $y \in B(x, r)$이면 $B(y, s) \subseteq B(x, r)$인 $s$가 있어 $B(y, s) \cap A = \emptyset$이다. 곧 $B(x, r) \subseteq X \setminus E$이므로 $X \setminus E$는 열려 있다. $A \subseteq E$는 분명하므로 $\overline{A} \subseteq E$이다. 반대로 $x \in E$이고 $A$를 포함하는 닫힌집합 $F$에 대하여 $x \notin F$라 하면, $X \setminus F$가 열려 있으므로 $B(x, r) \subseteq X \setminus F \subseteq X \setminus A$인 $r$이 있어 $B(x,r) \cap A = \emptyset$이 되고 $x \in E$에 모순이다. 따라서 $x$는 $A$를 포함하는 모든 닫힌집합에 속하고 $E \subseteq \overline{A}$이다.
:::

따라서 $A$가 닫힌집합인 것은 $\overline{A} = A$인 것과 같고, 이는 [명제 12](#prop12)의 (2)이다. Closure는 limit point만이 아니라 $A$ 자신도 포함한다. $A = [0, 1) \cup \{2\}$에서 $\overline{A} = [0, 1] \cup \{2\}$이며, $2$는 limit point가 아니지만 $A$의 점이므로 closure에 들어간다.

몇 가지를 계산해 두자. $\overline{(a, b)} = [a, b]$인 것은 $a + 1/n$, $b - 1/n$이 $(a,b)$ 안의 점열이기 때문이고, $\overline{\{1/n \mid n \geq 1\}} = \{1/n \mid n \geq 1\} \cup \{0\}$이다. $\overline{\mathbb{Q}} = \mathbb{R}$인 것은 [§실수의 완비성, ⁋정리 8](/ko/math/analysis/completeness_of_reals#thm8)에 의하여 임의의 두 실수 사이에 유리수가 있어서 모든 열린구간이 $\mathbb{Q}$의 점을 포함하기 때문이다.

열린공의 closure에 관해 흔한 오해가 하나 있다. $B(x, r)$의 closure는 *닫힌 공* $\{y \mid d(x, y) \leq r\}$과 같을 것이라 생각하기 쉽지만, 일반적으로는 전자가 후자의 subset일 뿐이다. 닫힌 공은 닫힌집합이라 $\overline{B(x,r)}$을 포함하기 때문이다. 등호가 깨지는 것은 이산거리에서 볼 수 있다.

::: 예시 15 (열린공의 closure와 닫힌 공)
이산거리를 가진 집합 $X$가 두 점 이상을 가진다고 하자. $B(x, 1) = \{x\}$이고 $\{x\}$는 닫혀 있으므로 $\overline{B(x, 1)} = \{x\}$이다. 그러나 닫힌 공 $\{y \mid d(x, y) \leq 1\}$은 $X$ 전체이다. $\mathbb{R}^n$의 표준 거리와 같은 노름공간에서는 등호가 성립하지만, 이는 노름의 동차성을 쓰는 별도의 사실이다.
:::

## 동치인 거리

수렴, 열린집합, 닫힌집합, closure는 모두 열린공에서 출발해 정의되었다. 같은 집합에 두 거리를 줄 때 이 개념들이 일치하는 상황을 정리하자.

::: 정의 16
같은 집합 $X$ 위의 두 거리 $d, d'$가 같은 열린집합들을 정하면, 곧 $U \subseteq X$가 $d$에 대하여 열려 있는 것과 $d'$에 대하여 열려 있는 것이 동치이면 $d$와 $d'$를 *동치인 거리<sub>equivalent metrics</sub>*라 한다.
:::

::: 명제 17
$d, d'$를 $X$ 위의 거리라 하자.

1. 양수 $c, C$가 있어 모든 $x, y \in X$에 대하여 $c d(x, y) \leq d'(x, y) \leq C d(x, y)$이면 $d$와 $d'$는 동치이다.
2. $d$와 $d'$가 동치이면 두 거리에서 수렴하는 점열이 같고, 닫힌집합이 같고, closure가 같다.
:::

::: 증명
(1) $B_d$, $B_{d'}$로 각 거리의 열린공을 구분하자. $d'(x, y) < c r$이면 $d(x, y) \leq d'(x,y)/c < r$이므로 $B_{d'}(x, cr) \subseteq B_d(x, r)$이고, $d(x, y) < r/C$이면 $d'(x,y) < r$이므로 $B_d(x, r/C) \subseteq B_{d'}(x, r)$이다. $U$가 $d$에 대하여 열려 있고 $x \in U$이면 $B_d(x, r) \subseteq U$인 $r$에 대하여 $B_{d'}(x, cr) \subseteq U$이므로 $U$는 $d'$에 대해서도 열려 있다. 반대 방향도 두 번째 포함으로 같다.

(2) 열린공은 열린집합이고 ([명제 9](#prop9)) 열린집합 $U \ni x$는 $x$를 중심으로 하는 열린공을 포함하므로, $x_n \to x$는 "$x$를 포함하는 모든 열린집합이 $x_n$을 결국 포함한다"와 동치이다. 이 조건은 열린집합들의 모임에만 의존한다. 닫힌집합은 열린집합의 여집합이고 closure는 닫힌집합들의 교집합이므로 역시 열린집합들의 모임에만 의존한다.
:::

[명제 3](#prop3)의 부등식 사슬에서 $c = 1/n$, $C = 1$ 등을 취하면 $d_1, d_2, d_\infty$는 서로 동치이다. 따라서 $\mathbb{R}^n$에서는 어느 거리로 수렴과 열림을 말해도 같다.

[명제 17](#prop17)의 (1)의 조건은 충분조건일 뿐이다. 거리를 상수배로 서로 누를 수 없어도 동치일 수 있다.

::: 예시 18 (동치인 거리의 두 경우)
1. $\mathbb{R}$의 표준 거리 $d$에 대하여 $d'(x, y) = \min\{d(x,y), 1\}$은 거리이다. 삼각부등식은 $d(x,y)$ 또는 $d(y,z)$ 가운데 하나라도 $1$ 이상이면 우변이 $1$ 이상이어서 자명하고, 둘 다 $1$ 미만이면 $d'$이 $d$와 같아서 $d$의 삼각부등식에서 나온다. $d$와 $d'$는 동치이다. $r \leq 1$이면 $B_{d'}(x, r) = B_d(x, r)$이고 열림은 작은 반지름만으로 확인되기 때문이다. 그러나 $d'(0, n) = 1$, $d(0, n) = n$이므로 $c d \leq d'$인 양수 $c$는 없다.
2. $\mathbb{R}$의 표준 거리와 이산거리는 동치가 아니다. 이산거리에서 $\{0\}$은 열려 있지만 표준 거리에서는 모든 $(-r, r)$이 $0$ 이외의 점을 포함하여 열려 있지 않다. 수렴에서도 $1/n$은 표준 거리에서 $0$으로 수렴하지만 이산거리에서는 수렴하지 않는다.
:::

## 부분공간

거리공간 $(X, d)$의 subset $Y$는 $d$를 $Y \times Y$로 제한하여 거리공간이 된다. 이를 $X$의 *부분공간<sub>subspace</sub>*이라 한다. $Y$에서의 열린공은 $B_Y(y, r) = B_X(y, r) \cap Y$이다. $Y$ 안에서 열린집합과 닫힌집합을 말할 때는 $X$가 아니라 $Y$의 열린공을 쓰며, 이는 $X$에서의 열림과 다를 수 있다. 가령 $Y = [0, 1]$에서 $[0, 1/2)$은 $B_Y(0, 1/2)$이므로 열린집합이지만 $\mathbb{R}$에서는 열려 있지 않다.

::: 명제 19
$Y$가 $X$의 부분공간이라 하자. $U \subseteq Y$가 $Y$에서 열린집합인 것은 $X$의 열린집합 $V$가 있어 $U = V \cap Y$인 것과 동치이다. 닫힌집합에 대해서도 마찬가지로 $F \subseteq Y$가 $Y$에서 닫혀 있는 것은 $X$의 닫힌집합 $K$가 있어 $F = K \cap Y$인 것과 동치이다.
:::

::: 증명
$U$가 $Y$에서 열려 있다고 하자. 각 $y \in U$에 대하여 $B_Y(y, r_y) \subseteq U$인 $r_y > 0$이 있다. $V = \bigcup_{y \in U} B_X(y, r_y)$로 두면 $V$는 [명제 9](#prop9)와 [명제 10](#prop10)에 의해 $X$에서 열려 있고, $V \cap Y = \bigcup_y B_Y(y, r_y) = U$이다. 거꾸로 $U = V \cap Y$, $V$가 $X$에서 열려 있다고 하자. $y \in U$이면 $B_X(y, r) \subseteq V$인 $r$이 있고, 그럼 $B_Y(y, r) = B_X(y, r) \cap Y \subseteq V \cap Y = U$이다.

닫힌집합의 경우 $F$가 $Y$에서 닫혀 있다는 것은 $Y \setminus F$가 $Y$에서 열려 있다는 것이므로, 위에 의해 $Y \setminus F = V \cap Y$인 $X$의 열린집합 $V$가 있다. $K = X \setminus V$로 두면 $K$는 닫혀 있고 $K \cap Y = Y \setminus (V \cap Y) = F$이다. 거꾸로도 같은 계산이다.
:::

[명제 19](#prop19)에서 $Y$ 자신은 항상 $Y$에서 clopen이다. $\emptyset$과 $Y$ 이외의 clopen set이 있는 경우는 $X$의 열린집합과 닫힌집합이 $Y$ 위에서 만나는 방식에서 나온다.

::: 예시 20 (유리수의 clopen subset)
$Y = \mathbb{Q}$에서 $A = \{q \in \mathbb{Q} \mid q^2 < 2\}$를 보자. [§실수의 완비성, ⁋예시 5](/ko/math/analysis/completeness_of_reals#ex5)에 의하여 $\sqrt{2}$가 무리수이므로 $A = \mathbb{Q} \cap (-\sqrt{2}, \sqrt{2}) = \mathbb{Q} \cap [-\sqrt{2}, \sqrt{2}]$이다. 첫째 표현은 $\mathbb{R}$의 열린집합과의 교집합이고 둘째는 닫힌집합과의 교집합이므로, [명제 19](#prop19)에 의해 $A$는 $\mathbb{Q}$에서 열려 있으면서 닫혀 있다. $\mathbb{R}$에서는 어떤 열린구간이나 닫힌구간도 이런 일을 하지 못하지만, $\mathbb{Q}$는 구멍이 있어서 $\emptyset$, $\mathbb{Q}$ 이외의 clopen subset을 가진다.
:::

## Dense subset

::: 정의 21
$A \subseteq X$가 $\overline{A} = X$를 만족하면 $A$를 $X$의 *dense subset*이라 한다.
:::

[명제 14](#prop14)의 (2)로 읽으면 $A$가 dense라는 것은 모든 점 $x$와 모든 $r > 0$에 대하여 $B(x, r) \cap A \neq \emptyset$이라는 것이다. 열린공이 열린집합이고 비어 있지 않은 열린집합은 열린공을 포함하므로, 이는 다음과 같이 다시 쓸 수 있다.

::: 명제 22
$A \subseteq X$가 dense인 것은 $X$의 비어 있지 않은 모든 열린집합이 $A$의 점을 포함하는 것과 동치이다.
:::

::: 증명
$A$가 dense이고 $U$가 비어 있지 않은 열린집합이면 $x \in U$와 $B(x, r) \subseteq U$인 $r$이 있고, [명제 14](#prop14)의 (2)에 의해 $B(x, r) \cap A \neq \emptyset$이므로 $U \cap A \neq \emptyset$이다. 거꾸로 모든 열린공 $B(x, r)$이 열린집합이므로 $A$의 점을 포함하고, 다시 (2)에 의해 $\overline{A} = X$이다.
:::

가령 $\mathbb{Q}$는 $\mathbb{R}$에서 dense이다. [§실수의 완비성, ⁋정리 8](/ko/math/analysis/completeness_of_reals#thm8)에 의하여 임의의 두 실수 사이에 유리수가 있기 때문이다. 같은 이유로 무리수 집합도 dense이다. $\mathbb{Q}^n$은 $\mathbb{R}^n$에서 dense인데, $d_\infty$에서 $B(x, r)$은 $\prod_i (x_i - r, x_i + r)$이고 이는 각 좌표를 유리수로 고른 점을 포함하며, $d_\infty$로 dense인 것은 [명제 17](#prop17)에 의해 $d_2$로도 dense이기 때문이다. 이산거리 공간에서는 모든 집합이 닫혀 있으므로 dense subset은 $X$ 자신뿐이다.

Dense라는 것은 내부가 크다는 뜻이 아니다. $\mathbb{Q}$는 $\mathbb{R}$에서 dense이지만 어떤 열린구간도 $\mathbb{Q}$에 포함되지 않으므로 $\mathbb{Q}^\circ = \emptyset$이다. 반대로 closure의 내부가 비어 있는 집합, 곧 $(\overline{A})^\circ = \emptyset$인 집합은 어디서도 dense하지 않은 집합이며 *nowhere dense*라 한다. $\mathbb{Z} \subseteq \mathbb{R}$이 그런 예이다. 다음 절의 Cantor 집합은 닫혀 있고 내부가 비었으면서 훨씬 큰 집합이다.

## Cantor 집합

$C_0 = [0, 1]$에서 시작하여, $C_k$가 길이 $3^{-k}$인 $2^k$개의 서로소인 닫힌구간의 합집합일 때 각 구간 $[s, s + 3^{-k}]$에서 열린 가운데 삼분의 일 $(s + 3^{-k-1}, s + 2\cdot 3^{-k-1})$을 제거하여 $C_{k+1}$을 얻는다. 각 구간이 $[s, s + 3^{-k-1}]$과 $[s + 2\cdot 3^{-k-1}, s + 3^{-k}]$로 나뉘므로 $C_{k+1}$은 길이 $3^{-k-1}$인 $2^{k+1}$개의 서로소인 닫힌구간의 합집합이다. $C_0 \supseteq C_1 \supseteq C_2 \supseteq \cdots$이고, *Cantor 집합*은 $C = \bigcap_{k \geq 0} C_k$이다.

::: 명제 23
$\mathbb{R}$의 Cantor 집합 $C$는 닫힌집합이고, 내부가 비어 있으며, 비가산집합이다.
:::

::: 증명
닫힘. 각 $C_k$는 유한개의 닫힌구간의 합집합이므로 닫혀 있고, 닫힌집합의 교집합 $C$도 닫혀 있다.

내부가 빔. 구간 $(a, b)$, $a < b$가 $C$에 포함된다고 하고 모순을 이끈다. $3^{-k} < b - a$인 $k$를 택하면 $(a, b) \subseteq C_k$이다. $(a, b)$가 $C_k$의 서로 다른 두 구간 $I < I'$의 점 $p \in I$, $q \in I'$를 모두 포함하면, $I$의 오른쪽 끝점과 $I'$의 왼쪽 끝점 사이에는 $C_k$에 속하지 않는 점이 있고 그 점은 $p$와 $q$ 사이에 있으므로 $(a, b)$에 속하여 $(a,b) \subseteq C_k$에 모순이다. 따라서 $(a, b)$는 $C_k$의 한 구간 안에 있고, 그 구간의 길이 $3^{-k}$가 $b - a$보다 작다는 사실에 모순이다. $C$에 포함되는 열린구간이 없으므로 $C^\circ = \emptyset$이다.

비가산. $a = (a_1, a_2, \dots)$, $a_i \in \{0, 2\}$인 수열에 대하여 $s_k(a) = \sum_{i=1}^k a_i 3^{-i}$로 두자. 귀납적으로 $C_k$의 $2^k$개의 구간이 정확히 $I_k(a) = [s_k(a), s_k(a) + 3^{-k}]$, $a_1, \dots, a_k \in \{0, 2\}$ 꼴임을 보인다. $k = 1$에서는 $[0, 1/3]$, $[2/3, 1]$이다. $I_k(a)$를 만드는 단계에서 구간 $[s, s + 3^{-k}]$ ($s = s_k(a)$)의 두 자식은 $[s, s + 3^{-k-1}]$과 $[s + 2\cdot 3^{-k-1}, s + 3^{-k}]$이고, 이는 새로 붙는 숫자 $a_{k+1} = 0$ 또는 $2$에 대하여 $[s + a_{k+1} 3^{-k-1}, s + a_{k+1} 3^{-k-1} + 3^{-k-1}]$ 꼴이므로 주장이 따른다.

이제 $\varphi(a) = \sum_{i \geq 1} a_i 3^{-i}$로 정의한다. 꼬리의 합이 $0 \leq \sum_{i > k} a_i 3^{-i} \leq 2 \sum_{i > k} 3^{-i} = 3^{-k}$이므로 $\varphi(a) \in I_k(a) \subseteq C_k$가 모든 $k$에서 성립하고 $\varphi(a) \in C$이다. $\varphi$는 단사이다. $a \neq b$이고 처음 다른 번호를 $j$라 하면, $I_j(a)$와 $I_j(b)$는 $C_j$의 서로 다른 구간이므로 서로소이고 $\varphi(a) \in I_j(a)$, $\varphi(b) \in I_j(b)$이므로 $\varphi(a) \neq \varphi(b)$이다.

따라서 $C$가 가산이라면 $\varphi$의 정의역 $\{0, 2\}^{\mathbb{N}}$도 가산이어야 한다. $\{0,2\}^{\mathbb{N}}$의 원소를 $a^{(1)}, a^{(2)}, \dots$로 나열했다고 하면, $b_m = 2 - a^{(m)}_m$으로 정한 수열 $b$는 $\{0, 2\}$의 값을 가지면서 모든 $m$에 대하여 $a^{(m)}$과 $m$번째 항이 다르다. 곧 $b$는 목록에 없으므로 $\{0,2\}^{\mathbb{N}}$은 비가산이고, $C$도 비가산이다.
:::

Cantor 집합은 $\mathbb{R}$의 닫힌집합이면서 어느 구간도 담지 않지만 $\mathbb{R}$만큼 많은 점을 가진다. 가산집합이면 작다는 직관이나 내부가 비어 있으면 점이 많지 않다는 직관은 모두 이 집합에서 깨진다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
