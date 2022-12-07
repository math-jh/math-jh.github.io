---

title: "Series"
excerpt: "Basic notions"

categories: [Math / Calculus]
permalink: /ko/math/calculus/series
header:
    overlay_image: /assets/images/Calculus/Series.png
    overlay_filter: 0.5
sidebar: 
    nav: "preliminaries"

date: 2022-03-03
last_modified_at:
weight: 1

publilshed: false

---

Stewart나 Thomas의 교재와는 다르게, 김홍종 교수님의 미적분학 교재는 첫 시작을 수열과 급수로 삼았다. 우리나라 학생들은 고등학교 때 함수의 극한이나 미분, 적분 등은 지겹도록 했을테니 그럴 법도 하다. 어쩼든 결과적으로 이 책의 도입부는 해석학 교재와 비슷한 흐름을 따라가게 되었다. 다만 그 반대급부로 함수의 극한이나 연속, 미분 등의 개념을 전혀 정의하지 않다보니 논리적으로 불만족스러운 부분이 있기도 하다. 어쨌든 우리도 엄밀한 증명은 해석학이나 미분기하에 미뤄두고 큰 이야기의 흐름만 따라가기로 한다.

## 수열의 극한

고등학교 교육과정에는 수열의 극한에 대한 엄밀한 정의가 나와있지 않은데, 이를 엄밀하게 정의하는 것이 대학수학의 시작이라 할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 수열 $(a_n)$이 극한 $L$을 가진다는 것은 임의의 $\epsilon>0$마다 적당한 자연수 $N$이 존재하여 다음의 논리식

$$n>N\implies \lvert a_n-L\rvert<\epsilon$$

이 성립하는 것이다. 이 상황을 기호로는

$$\lim_{n\rightarrow\infty} a_n=L$$

이라 적는다. 수렴하지 않는 수열을 *발산한다*고 부른다.

</div>

생소해서 그렇지, 정의 자체는 직관적으로 명확하다. 위 정의를 조금 더 일상적인 언어로 풀어쓰자면

> 수열 $(a_n)$이 주어졌을 때, $n$이 충분히 크기만 하면 ($n>N$) 수열의 일반항 $a_n$이 어떤 값 $L$에 원하는 만큼 (*임의의 $\epsilon>0$마다*) 가깝게 할 수 있다

고 할 수 있다. 

발산하는 수열 중 특히 다음과 같은 상황은 따로 취급할 필요가 있다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 수열 $(a_n)$에 대하여, 만일 임의의 $M>0$마다 적당한 자연수 $N$이 존재하여 다음의 논리식

$$n>N\implies a_n>M$$

이 성립하도록 할 수 있다면, 수열 $a_n$이 *(양의) 무한대로 발산*한다고 하고, 이를

$$\lim_{n\rightarrow\infty}a_n=\infty$$

으로 표기한다. 비슷하게 음의 무한대로 발산하는 경우도 정의한다.

</div>

물론 임의의 발산하는 수열이 항상 양의 무한대 혹은 음의 무한대로 발산하지는 않는다. 예컨대 수열 $a_n=(-1)^n$은 무한대로 발산하지 않지만 발산하는 수열이다. 

고등학교 때 배웠던 극한의 성질들은 이제 위의 정의를 이용해서 보여야 하는 명제들이 된다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 수렴하는 두 수열 $(a_n)$, $(b_n)$과 상수 $c$에 대하여, 다음의 식들이 모두 성립한다.

1. $\displaystyle\lim_{n\rightarrow\infty}(a_n+b_n)=\displaystyle\lim_{n\rightarrow\infty} a_n+\displaystyle\lim_{n\rightarrow\infty}b_n$
2. $\displaystyle\lim_{n\rightarrow\infty}(a_nb_n)=\bigl(\displaystyle\lim_{n\rightarrow\infty}a_n\bigr)\bigl(\displaystyle\lim_{n\rightarrow\infty}b_n\bigr)$
3. $\displaystyle\lim_{n\rightarrow\infty}ca_n=c\displaystyle\lim_{n\rightarrow\infty}a_n$
4. $\displaystyle\lim_{n\rightarrow\infty}\frac{a_n}{b_n}=\displaystyle\frac{\displaystyle\lim_{n\rightarrow\infty}a_n}{\displaystyle\lim_{n\rightarrow\infty}b_n}$, 단 $\displaystyle\lim_{n\rightarrow\infty}b_n\neq 0$

</div>
<details class="proof" markdown="1" open>
<summary>증명</summary>

<#ref#>

</details>

임의의 함수 $f:\mathbb{R}\rightarrow\mathbb{R}$을 생각하자. 일반적으로 수열 $(a_n)$이 극한값 $L$로 수렴한다고 해서 $f(a_n)$이 $f(L)$로 수렴하지는 않는다. 예를 들어 함수

$$f(x)=\begin{cases}1&\text{if $x>0$}\\0&\text{if $x=0$}\\-1&\text{if $x<0$}\end{cases}$$

와 수열 $a_n=1/n$을 생각하자. 그럼 임의의 $n$에 대하여 $a_n>0$이므로 $f(a_n)=1$이고, 따라서 $\lim f(a_n)=1$이지만, $f(\lim a_n)=f(0)=0$이다.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px" class="invert" .align-center}

우리가 함수 $f$의 연속성을 엄밀한 용어로 정의하지는 않았지만, 만일 $f$가 연속이라면 항상

$$\lim_{n\rightarrow\infty}f(a_n)=f\Bigl(\lim_{n\rightarrow\infty}a_n\Bigr)$$

이 성립하는 것을 확인할 수 있다.

본문에서 다루는 예시는 두 가지가 있다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 첫 번째 예시는 고등학교 때부터 익숙했던 다음의 자연상수

$$\lim_{n\rightarrow\infty}\left(1+\frac{1}{n}\right)^n$$

이다. 이 극한값은 존재하며 그 값은 무리수라는 것이 알려져 있다. (<#ref#>)  이를 $e$로 표기한다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 임의의 양수 $a>1$이 주어졌다 하자. 그럼 항상 다음의 식

$$\lim_{n\rightarrow\infty}\frac{a^n}{n}=\infty$$

가 성립한다. 이는 사실 두 그래프를 비교하면 거의 자명하다.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px" class="invert" .align-center}

물론 그래프만으로 이를 증명할 수는 없고, 예컨대 **[Kim]**의 보기 1.2.3과 같은 엄밀한 argument가 필요하다.

</div>

그래프에 조금만 더 의존하면 다음과 같은 생각을 할 수 있다. 

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px" class="invert" .align-center}

위 그래프에서, 우리는 함수가 *증가하는 속도*가 대략

$$1\ll n\ll n^2\ll \cdots\ll a^n$$

인 것을 확인할 수 있다. 또, 이들의 역함수 ($y=x$ 대칭)을 생각해보면, 가장 빨리 증가하는 함수의 역함수가 가장 느리게 증가할 것이므로 거꾸로

$$1\ll\log n\ll \cdots\ll n^{1/3}\ll n^{1/2}\ll n\ll n^2\ll \cdots\ll a^n$$

을 얻는다. 마지막으로, $a^n\ll n!\ll n^n$인 것도 자명하다. 여기서 $\ll$의 뜻을 엄밀하게 정의하지는 않았고, 사실 이 표기법은 표준적인 표기법도 아니지만 우리 문맥에서 하고자 하는 이야기는 명확하다. $\ll$의 왼쪽에 있는 수열을 분모로, 오른쪽에 있는 수열을 분자로 두고 극한을 취했을 때 그 값이 무한대가 된다는 뜻이다. 역시 마찬가지로 이 사실들 또한 그래프로 해결하지 않고 엄밀하게 증명할 수 있다.

## 무한급수

*무한급수*라는 것은 별게 아니라, 주어진 수열 $(a_n)$에 대하여

$$a_1+a_2+\cdots$$

를 뜻한다. 우리는 이를 $\sum_{n=1}^\infty a_n$이라 적는다. 사실 이는 우리가 이미 정의했던 수열의 극한의 특수한 경우일 뿐인데, 다음의 *부분합 수열*

$$s_n=a_1+a_2+\cdots+a_n$$

을 정의하면, $\sum_{n=1}^\infty a_n$의 값은 정확히

$$\sum_{n=1}^\infty a_n=\lim_{n\rightarrow\infty} s_n$$

이 되기 때문이다. 그럼 우리는 무한급수의 수렴을 수열의 극한으로 표현할 수 있게 된다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (일반항 판정법)**</ins> 만일 $\sum a_n$이 수렴한다면, $\displaystyle\lim_{n\rightarrow \infty}a_n=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$a_n=s_n-s_{n-1}$의 양 변에 극한을 취하자. 우변은 가정에 의하 수렴하는 두 수열의 차이이므로 수렴하고, 그 값은 $0$이므로 원하는 정리가 성립한다.

</details>

그러나 이 역은 성립하지 않는다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 예를 들어 다음의 조화급수

$$\frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\cdots$$

에서, $1/n\rightarrow 0$이지만 위 급수는 수렴하지 않는다.

</div>

이제 남은 글에서 우리는 (주로 각 항이 양수인) 급수의 판정법들에 대해 살펴본다. 이러한 급수들을 *양항급수*라 부르는데, 종종 각 항이 0인 경우도 허용한다. 
 
## 비교판정법
 
우리가 처음으로 소개한 일반항 판정법은 사실 판정법이라고 하기는 좀 애매한데, 어떤 급수가 언제 발산하는지는 알려주지만 언제 수렴하는지는 알려주지 않기 때문이다. 

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (비교판정법)**</ins> 각 항이 양수인 두 개의 수열 $(a_n)$, $(b_n)$이 주어졌다 하고, $0\leq a_n\leq b_n$이 모든 $n$에 대해 성립한다 하자. 그럼

1. 만일 $\sum b_n<\infty$라면 $\sum a_n<\infty$ 또한 성립한다.
2. 만일 $\sum a_n=\infty$라면 $\sum b_n=\infty$ 또한 성립한다.

</div>



---

**References**

**[Kim]** 김홍종, *미적분학1<sup>+</sup>*, 서울대학교출판문화원
