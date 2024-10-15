---

title: "가우스 소거법"
excerpt: "가우스 소거법과 역행렬"

categories: [Math / Basic Linear Algebra]
permalink: /ko/math/basic_linear_algebra/Gaussian_elimination
sidebar: 
    nav: "basic_linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Basic_Linear_Algebra/Gaussian_elimination.png
    overlay_filter: 0.5

date: 2022-08-19
last_modified_at: 2022-08-19

weight: 9

---

## 가우스 소거법

다음의 일차연립방정식

$$\begin{aligned}a_{11}x_{1}+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}\tag{1}$$

이 주어졌다 하자. 이전 글에서 정의한 행렬의 곱에 의하여 위의 식은 다음의 행렬들

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\quad b=\begin{pmatrix}b_1\\b_2\\\vdots\\b_m\end{pmatrix}$$

에 대하여 $Ax=b$으로 쓸 수 있다. 만일 $m=n$이고, 행렬 $A$의 역행렬이 존재한다면 이 연립방정식의 해는 다음의 식

$$x=A^{-1}b$$

을 통해 유일하게 결정된다. 만일 $m\neq n$이거나 혹은 $A$의 역행렬이 존재하지 않으면 위의 일차연립방정식의 해는 존재하지 않을 수도 있고, 무한히 많을 수도 있다. 우리는 이 경우에도 유용하게 사용할 수 있는 *가우스 소거법*을 살펴본다.

식 (1)의 계수들 중 $a_{ji}=0$이 모든 $j$에 대해 성립하도록 하는 $1\leq i\leq n$이 존재한다 가정하자. 이 경우, 만일 

$$x_1=c_1,\quad x_2=c_2,\quad \ldots,\quad x_i=c_i,\quad\ldots,\quad x_n=c_n$$

이 식 (1)의 하나의 해라면 $x_i$의 값을 임의의 $d_i$로 바꾼 다음의 순서쌍

$$x_1=c_1,\quad x_2=c_2,\quad\ldots,\quad x_i=d_i,\quad\ldots,\quad x_n=c_n$$

또한 식 (1)의 해가 된다. 따라서 만일 $a_{ij}$들이 모두 $0$이라면, $b$가 영벡터일 경우 식 (1)은 임의의 $\mathbb{k}^n$의 순서쌍을 모두 해로 가지며, 그렇지 않을 경우 해가 존재하지 않는다. 이와 같은 자명한 경우를 피하기 위해, 적어도 하나의 $a_{ij}$는 0이 아니라 가정한다. 

이제 정수 $k$를 <phrase>$a_{jk}\neq 0$이도록 하는 $1\leq j\leq m$이 존재하는 정수들 중 가장 작은 것</phrase>으로 정의하고, 이렇게 고정된 $k$에 대하여 $a_{jk}\neq 0$를 만족하는 가장 작은 정수 $j$를 택하자. 이제 $j$번째 식

$$a_{j1}x_1+a_{j2}x_2+\cdots+a_{jk}x_k+\cdots+a_{nk}x_n=b_j$$

을 식의 가장 위쪽으로 올려

$$\begin{aligned}a_{j1}x_{1}+a_{j2}x_2+\cdots+a_{jn}x_n&=b_j\\a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\\hspace{10pt}\vdots&\\a_{mn}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\end{aligned}$$

으로 쓰면 $a_{jk}$의 정의로부터 $a_{j1},a_{j2},\ldots, a_{j,(k-1)}$과, 그 밑에 있는 계수들은 모두 $0$이 되어야 한다. 이제 식

$$a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n=b_i$$

마다, 첫째 식에 $-a_{ik}/a_{jk}$를 곱하여 더해주면

$$\left(a_{i1}-\frac{a_{ik}}{a_{jk}}a_{j1}\right)x_1+\left(a_{i2}-\frac{a_{ik}}{a_{jk}}a_{j2}\right)x_2+\cdots+\left(a_{ik}-\frac{a_{ik}}{a_{jk}}a_{jk}\right)x_k+\cdots+\left(a_{in}-\frac{a_{ik}}{a_{jk}}a_{jn}\right)x_n=b_i-\frac{a_{ik}}{a_{jk}}b_k$$

이 된다. 위의 식에서 $x_1,\ldots, x_{k-1}$의 계수는 원래부터 모두 0이었으며, 방금 전의 연산을 통해 $x_k$의 계수 또한 0이 된다. 즉, 이 과정을 거치면 $x_1,\ldots, x_{k-1}$의 계수는 모두 0이며, $x_k$의 계수들 중 0이 아닌 것은 오직 첫 번째 행에만 존재하게 된다. 

이제 두 번째 행부터 마지막 행까지의 $n-1$개 식에 대해 이 과정을 반복하고, 다시 세 번째 행부터 마지막 행까지의 $n-2$개 식에 대해 이 과정을 반복한다. 이를 계속하여 마지막 행에 도착하면 위의 식 (1)은 최종적으로 다음 두 조건 (\*)을 만족한다.

1. 만일 모든 계수가 0인 식이 있다면, 이 식은 연립방정식의 가장 밑에 위치한다.
2. 모든 계수가 0은 아닌 식에 대해, 이 식에서 처음으로 등장하는 0이 아닌 계수는 위의 식에서 이러한 성질을 만족하는 계수보다 오른쪽에 있다.

다음 연립방정식은 위의 두 조건을 만족한다.

$$\begin{aligned}x_1+2x_2+4x_3+3x_4&=2\\\phantom{x_1+}3x_2\phantom{+2x_3}+6x_4&=3\\\phantom{x_1+2x_2+}x_3+5x_4&=1\end{aligned}$$

약간의 조작을 추가로 가하면 이 식으로부터 연립방정식의 해를 바로 구해낼 수 있다. 각 식에서 0이 아닌 최초의 계수를 *선행계수<sub>leading coefficient</sub>*라 부르자. 위의 식을 예시로 들면, 첫째 식의 선행계수는 $x_1$의 계수인 1이고, 둘째 식의 선행계수는 $x_2$의 계수인 3, 그리고 마지막 식의 선행계수는 $x_3$의 선행계수인 1이다. 

이제 각 행마다 선행계수 위에 있는 계수들을 모두 없애준다. 즉, 마지막 식의 선행계수 위에 있는 항인 $4x_3$을 없애야 하고, 둘째 식의 선행계수 위에 있는 항인 $2x_2$를 없애야 한다. 이를 위해서는 마지막 식에 4를 곱하여 첫째 식에서 빼 주고, 둘째 식에 $2/3$을 곱하여 첫째 식에서 빼 주면 된다. 그 결과는 다음과 같다.

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}3x_2\phantom{+2x_3}+\phantom{1}6x_4&=3\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

이로부터 위의 연립방정식의 일반해는

$$x_1=-4+21x_4,\quad x_2=1-2x_4,\quad x_3=1-5x_4$$

임을 알 수 있다. 물론 연립방정식의 둘째 식의 선행계수를 미리 계산하여

$$\begin{aligned}x_1\phantom{+2x_2+4x_3}-21x_4&=-4\\\phantom{x_1+}1x_2\phantom{+2x_3}+\phantom{1}2x_4&=1\\\phantom{x_1+2x_2+}x_3+\phantom{1}5x_4&=1\end{aligned}$$

으로 적었다면 조금 더 계산상의 이득을 볼 수 있었을 것이다.

지금까지 설명한 과정을 통해 연립방정식을 푸는 방법을 *가우스 소거법* 혹은 *요르단-가우스 소거법*이라 부른다.

## 기본행연산과 가우스 소거법

처음에 주어진 연립방정식 (1)은 행렬을 이용해 $Ax=b$로 간단하게 표현할 수 있었다. 가우스 소거법은 이 행렬 $A$와 $b$를 적절히 바꾸어 이 식을 $A'x=b'$로 쓸 수 있으며, 이 때 행렬 $A'$는 두 조건 (\*)를 만족하도록 잡을 수 있다는 것을 보여준다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 주어진 행렬 $A$에 대하여, *기본행연산<sub>elementary row operation, ERO</sub>*은 다음 세 개의 연산을 뜻한다.

1. 두 개의 행 전체를 위아래로 교환하는 연산,
2. 한 행에 0이 아닌 상수를 곱하는 연산,
3. 한 행의 배수를 다른 행에 더하는 연산.

</div>

또, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $m\times n$ 행렬 $A$가 주어졌다 하자. 임의의 $1\leq i\leq m$에 대해 정수 $j_0(i)=\min\\{j\leq n\mid a_{ij}\neq 0\\}$이 잘 정의된다면 $a_{i,j_0(i)}$를 $i$번째 행의 *선행계수*라 부른다. 추가적으로 만일 다음의 두 조건

1. 만일 $a_{i1}, a_{i2},\ldots, a_{in}=0$이라면, $i < k$를 만족하는 모든 $k$에 대해 $a_{k1}, a_{k2},\ldots, a_{kn}=0$이다.
2. 만일 $i < i'$이며 두 정수 $j_0(i), j_0(i')$이 모두 잘 정의된다면 반드시 $j_0(i) < j_0(i')$이다.

이 만족된다면, 행렬 $A$를 *행사다리꼴행렬<sub>row échelon matrix, REF</sub>*이라 부른다. 만일 추가적으로 

1. $a_{i, j_0(i)}$가 항상 1이고, 
2. 모든 $i'\neq i$에 대해 $M_{i', j_0(i)}=0$

이라면, $A$를 *기약행사다리꼴행렬<sub>reduced row échelon matrix, RREF</sub>*이라 부른다.

</div>

따라서 앞선 절에서의 논의를 종합하면 가우스 소거법은 행렬 $A$에서 기본행연산을 통해 행사다리꼴행렬, 혹은 더 나아가 기약행사다리꼴행렬을 만드는 과정이라 할 수 있다. 일반적으로 주어진 행렬 $A$에서 만들어지는 행사다리꼴은 여러가지가 될 수 있으나, 기약행사다리꼴행렬은 반드시 유일하게 결정된다는 사실이 잘 알려져 있다. 우리는 이 유일성을 사용할 일이 없으므로 증명하지 않는다.

다시 연립방정식 (1)로 돌아오자. 각 식의 순서를 바꾸거나, 각 식의 양 변에 상수를 곱하는 것, 그리고 각 식의 배수를 다른 식에 더하는 것은 연립방정식을 처음 접했을 때부터 익숙한 풀이이므로 이상하지 않다. 그러나 같은 식을 행렬을 통해 $Ax=b$로 적는다면, $A$에 적용하는 기본행연산이 왜 $b$에도 같은 방식으로 영향을 미치는가는 명확하지 않다. 이제 임의의 $m\times n$ 행렬이 주어졌다 하고, 몇 개의 $m\times m$ 행렬을 생각하자. 

우선 $E_{i,j}$는 $m\times m$ 단위행렬 $I$에서 $i$번째와 $j$번째 행을 바꾸어 얻어지는 행렬이다. 예를 들어 $E_{1,2}$는 다음의 행렬

$$E_{1,2}=\begin{pmatrix}0&1&0&\cdots&0\\1&0&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

이 된다. 한편, $E'\_{i,r}$은 $m\times m$ 단위행렬 $I$의 $i$번째 행에 $r$을 곱하여 얻어지는 행렬이다. 예를 들어 $E'\_{1,r}$은 다음의 행렬

$$E'_{1,r}=\begin{pmatrix}r&0&0&\cdots&0\\0&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

이 된다. 마지막으로 $E''\_{i,j,r}$은 $m\times m$ 단위행렬 $I$의 $j$행 $i$열 성분을 $r$로 바꾸어 얻어진 행렬이다. 예를 들어 $E''\_{1,2,r}$은 다음의 행렬

$$E''_{1,2,r}=\begin{pmatrix}1&0&0&\cdots&0\\r&1&0&\cdots&0\\ 0&0&1&\cdots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\ 0&0&0&\cdots&1\end{pmatrix}$$

이 된다. 이들을 묶어서 *기본행렬*이라 부르기도 한다. 이제 $E_{ij}A$, $E'\_{i,r}A$, $E''\_{i,j,r}A$를 각각 계산해보면 

1. $E_{ij}A$는 $A$의 $i$번째 행과 $j$번째 행을 바꾸어 얻어진 행렬,
2. $E'\_{i,r}A$는 $A$의 $i$번째 행에 상수 $r$을 곱하여 얻어진 행렬,
3. $E''\_{i,j,r}A$는 $A$의 $j$번째 행에, ($i$행)$\times r$을 더하여 얻어진 행렬

이 된다는 것을 쉽게 확인할 수 있다. 즉, 행렬 $A$에 기본행연산을 행하는 것은 위에서 정의한 행렬 $E_{ij}$, $E_{i,r}'$, 혹은 $E_{i,j,r}''$를 곱하는 것과 같으며, 연립방정식 $Ax=b$에 위의 조작을 가하는 것은 양 변의 왼쪽에 해당하는 기본행렬 $E$를 곱하여 $(EA)x=(Eb)$를 얻어내는 것과 같다. 

기본행렬들 $E$는 모두 가역행렬이다. 이는 기본행렬에 해당하는 기본행연산이 수행된 행렬에 다시 기본행연산을 적용하여 원래의 행렬을 얻을 수 있다는 것으로부터 자명하다.

---

**참고문헌**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---