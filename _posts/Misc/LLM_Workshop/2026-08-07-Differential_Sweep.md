---

title: "KaTeX 커스텀 매크로"

excerpt: "흩어져 있던 미분 기호를 \\dd 하나로 모으며 정규식을 토크나이저로 갈아엎은 일, 사선만 남고 줄이 바뀌던 \\not을 인자를 흡수하는 한 \\mathrel로 묶은 일, 그리고 언더셋과 색을 두고 몇 번 뒤집힌 끝에 브래스색으로 자리 잡은 degree 표시 \\at"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/differential_sweep

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-07

weight: 38
group: typesetting

---

관련 파일: [`scripts/sweeps/dd_extract.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/dd_extract.py), [`scripts/sweeps/dd_apply.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/dd_apply.py), [`scripts/sweeps/dd_despace.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/dd_despace.py), [보강 커밋](https://github.com/math-jh/math-jh.github.io/commit/a8e2c693), [`assets/js/katex-macros.js`](https://github.com/math-jh/math-jh.github.io/blob/main/assets/js/katex-macros.js), [`_posts/Math/Set_Theory/ko/2021-08-22-Order_Relations.md`](https://github.com/math-jh/math-jh.github.io/blob/main/_posts/Math/Set_Theory/ko/2021-08-22-Order_Relations.md), [커밋 4f107bf2](https://github.com/math-jh/math-jh.github.io/commit/4f107bf2), [커밋 6296b65e](https://github.com/math-jh/math-jh.github.io/commit/6296b65e), [`_sass/_diagram-colors.scss`](https://github.com/math-jh/math-jh.github.io/blob/main/_sass/_diagram-colors.scss), [커밋 cd136751](https://github.com/math-jh/math-jh.github.io/commit/cd136751), [커밋 cbb78517](https://github.com/math-jh/math-jh.github.io/commit/cbb78517)
{: .notice--info}

## 미분 표기: 후보 추출

사용자는 미분 기호를 쓸 때 `dx` 대신 `\mathop{dx}`라는 표기를 썼는데, 이는 미분 기호 앞의 간격을 위한 것이다. LaTeX는 수식의 각 단위를 일반 문자, 연산자, 관계 기호 등으로 분류하고, 이웃한 단위의 종류에 따라 간격을 정한다. 소스에 넣은 공백은 보통 출력에 반영되지 않으므로, `f(x) dx`처럼 띄어 쓴다고 원하는 간격이 생기는 것은 아니다. `\mathop{...}`는 그 안의 수식을 하나의 연산자 단위로 취급하게 하는 명령이다. 앞에 일반 문자나 닫는 괄호가 오면 그 사이에 얇은 간격(thin space, 기본 3mu)이 들어간다. 무조건 앞에 공백을 붙이는 명령은 아니며, 이웃한 기호의 종류에 따라 간격이 결정된다.

적분의 `f(x)dx`에서는 피적분함수와 미분 기호 사이를 조금 띄워 두려는 것이다. 그냥 `dx`를 적으면 d와 x가 일반 문자로 처리되어 닫는 괄호 뒤에 별도의 간격이 생기지 않는다. `f(x)\mathop{dx}`라고 쓰면 `dx` 전체가 연산자로 분류되어 그 앞에 간격이 들어간다. 예를 들어 아래에서 첫 식은 `\int f(x)dx`, 둘째 식은 `\int f(x)\mathop{dx}`로 적은 결과다.

$$
\int f(x)dx, \qquad \int f(x)\mathop{dx}
$$

사용자는 이렇게 기호의 간격을 맞추려고 미분 기호에 별도 표기를 써 왔지만, 오래 쌓인 레포라 그 방식이 시기마다 달랐다. 초기에는 `\mathop{dx}`를 직접 쓰거나 간격이 필요한 곳에 `\,dx`를 넣었다. 이후에는 자주 쓰는 표기에 매크로를 정의해 `\dx`, `\dy` 등을 썼다. 같은 목적의 표기가 코퍼스 안에 세 갈래로 남아 있었고, 이번 치환은 그것을 하나로 통일하려는 작업이었다.

통일할 표기는 `\dd{}`다. 인자를 받아 `\mathop{d#1}`로 펼쳐지므로, `\dd{x}`나 `\dd{y}`처럼 쓰면 글자마다 매크로를 따로 정의하지 않아도 같은 간격 규칙을 적용할 수 있다. 대상은 600편 남짓이고 전부 수식 안이라 한 글자만 잘못 건드려도 렌더가 깨진다.

이 레포에서 일괄 치환은 정해진 절차가 있다. 결정론 스크립트로만 하고, 수식 밖은 불변임을 게이트로 확인하고, 판단이 애매한 것은 치환하지 말고 사람에게 넘긴다. 인류의 역사가 피로 쓰여진 규칙 위에 서 있다면, 이 레포의 역사는 깨진 수식과 이를 복구하기 위해 쓴 토큰 위에 서 있는 셈이다. 추출기 `dd_extract.py`는 후보를 뽑아 네 갈래로 분류만 하고 파일은 쓰지 않는다. 쓰는 일은 `dd_apply.py`가 한다.

추출기는 먼저 기존의 `\mathop{dx}` 같은 표기를 찾아 `MATHOP`으로 분류한다. 이 레포에서는 이미 미분 기호로 쓰던 표기이므로, d가 미분인지 다시 판정할 필요가 없다. `\mathop{dx}`를 `\dd{x}`로 바꾸면 된다는 것이 자명해서, 이 갈래는 별도의 사람 판정 없이 `dd_apply.py`의 자동 치환 대상으로 넘어간다. 아래 코드는 후보를 기록하는 부분이며, 여기서 글 파일을 바로 고치는 것은 아니다.

{% raw %}
```python
# 이미 \mathop{d...} 인 것: 통째로 \dd{...} 로 개명
for m in re.finditer(r'\\mathop\{d([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', body):
    out.append(dict(kind='MATHOP', ..., old=m.group(0),
                    new='\\dd{%s}' % m.group(1), reason='기존 \\mathop{d…}'))
```
{: data-filename="scripts/sweeps/dd_extract.py · 일부 생략, 인자 배치 정리"}
{% endraw %}

추출기 `dd_extract.py`는 미분임이 확실한 후보만 `AUTO`(자동 치환)로 보내고, 애매하면 `AMBIG`(사람 판정 필요), 미분 표기가 아니면 `SKIP`(치환 대상 아님)으로 분류한다. `\mathop{dx}` 같은 경우는 `AUTO`이지만, 나머지는 문맥에 따라 판정을 해야 하는 셈이다. 가령 손으로 간격을 넣어 둔 `\,dx`나 아무 표시 없는 `dx`는 그 d가 미분인지, 이름이 d인 변수인지, 아니면 매크로 이름의 일부인지를 문맥에서 판정해야 한다. 

문제는 "홀로 선 d"를 찾는 부분이었다. 처음에는 정규식의 lookbehind로 판정했다. 그런데 이는 현재 위치 바로 앞에 특정 패턴이 있는지 검사하되, 그 앞부분은 매치 결과에 포함하지 않으므로 이는 매크로 이름 안의 d를 걸러내지 못했다. 예컨대 `\prod(`는 정규식 눈에 `d(`가 들어 있고, `\tilde`도 마찬가지다. 미분과 아무 상관 없는 곱 기호가 미분 후보로 올라오게 되는 것이다. .

해결책은 수식을 TeX의 처리 단위인 토큰으로 나누어 훑는 것이다. 파일에 저장된 수식은 문자열이지만, TeX는 `\prod`를 역슬래시와 알파벳 네 글자가 합쳐진 하나의 명령 토큰으로 읽지, 마지막 글자 d만 따로 떼어 변수나 미분 기호로 읽지 않는다. 반면 `dx`는 문자 토큰 d와 x로 나뉜다. 추출기도 이 구분을 따라, `\prod dx`에서 `\prod` 전체는 한 번에 건너뛰고 뒤에 따로 쓰인 d만 후보로 기록하게 했다. 이 단계에서는 매크로 이름에 포함된 d를 제외할 뿐, 남은 d가 실제로 미분인지는 뒤의 문맥 판정에 맡긴다.

```python
def dtokens(body):
    r"""수식 본문에서 '홀로 선 d' 의 offset 목록."""
    out, i, n = [], 0, len(body)
    while i < n:
        if body[i] == '\\':
            m = re.match(r'\\[A-Za-z]+|\\.', body[i:])
            i += m.end() if m else 1
            continue
        if body[i] == 'd':
            out.append(i)
        i += 1
    return out
```
{: data-filename="scripts/sweeps/dd_extract.py · 일부 생략, 문서 문자열 축약"}

수식 본문을 처음부터 끝까지 읽으면서, 역슬래시를 만나면 그 뒤 문자가 영문자인지에 따라 건너뛸 범위를 정한다. 영문자라면 `\\[A-Za-z]+`가 연속된 영문자 전체를 명령 이름으로 잡는다. 이때 명령 이름 안의 d도 함께 건너뛴다. 영문자가 아니라면 `\\.`가 역슬래시와 바로 다음 문자 하나까지만 잡는다. `|`는 이 두 규칙 중 하나를 적용한다는 뜻이며, 앞의 영문자 규칙을 먼저 시도한다. 매치한 구간을 건너뛴 다음에는 그 직후 문자부터 검사를 이어 간다. 공백을 찾을 때까지 건너뛰는 것이 아니므로, 한 글자짜리 명령 바로 뒤에 d가 붙어 있어도 그 d는 검사 대상이다. 이렇게 명령 바깥에서 만난 d의 위치만 기록한다.

d를 찾았으면 다음은 "무엇의 미분인가"를 정해야 한다. `\dd{...}`의 중괄호 안에 넣을 피연산자의 범위다. 아래첨자는 미분 기호 전체가 아니라 변수에 붙으므로, 변수와 함께 한 덩어리로 넣을 수 있다. 다만 아래첨자에 인자를 받는 매크로가 오면 그 인자까지 포함해야 한다. `d\varphi_\mathcal{L}`의 피연산자는 `\varphi_\mathcal{L}` 전체이므로 `\dd{\varphi_\mathcal{L}}`로 바꾼다. 매크로 이름에서 끊어 `\dd{\varphi_\mathcal}{L}`로 만들면 `\mathcal`의 인자가 밖으로 빠져 식이 깨진다. 반면 위첨자는 변수에 붙는지 미분 기호 전체에 붙는지에 따라 뜻이 갈릴 수 있어, 피연산자 범위에 자동으로 넣지 않는다. 예를 들어 `dx^2`를 `\dd{x^2}`로 바꾸면 x의 제곱을 미분한다는 뜻이고, `\dd{x}^2`로 바꾸면 미분 기호 전체를 제곱한다는 뜻이다. 실제로 블로그의 KaTeX로 렌더하면 `\dd{x}^2`의 2가 `\dd{x^2}`의 2보다 약 0.084em 높게 놓이는 정도의 차이뿐이라, 눈으로는 거의 구별하기 어렵다. 그래도 소스에는 올바른 의미를 담아야 하므로 사람의 확인이 필요하고, 따라서 `AMBIG`에 들어간다.

반대로 `SKIP`으로 빼는 경우도 둘 있다. `\bar d(...)`처럼 악센트의 인자로 들어간 d는 미분이 아니라 이름이 d인 무언가에 바가 씌워진 것이고, 치환하면 `\bar`의 인자가 바뀌어 식이 깨진다. KaTeX 게이트가 실제로 잡아낸 사례다. 라플라시안의 `d d^\ast`에서는 첫 d의 피연산자가 홑 d로 잡혀 `\dd{d}^\ast`, 곧 `(dd)^\ast`가 된다. 렌더는 멀쩡해서 게이트가 못 잡는 쪽이라, 피연산자가 홑 d면 분류기가 건너뛴다.

## 미분 표기: 치환 후보 관리와 검증

이미 검토한 후보를 다시 검토하지 않으려면, 추출 규칙을 고쳐도 같은 후보에는 같은 ID가 붙어야 한다. 구체적으로, `AMBIG` 후보를 검토하다 보면 미분이 아닌 것을 잘못 추출한 사례가 드러나고, 이러한 것이 많다면 규칙을 보강해 후보 목록을 다시 뽑게 되는데, 예를 들어 이 때 ID가 목록의 순번이면 앞쪽 후보 하나만 빠져도 뒤의 번호가 모두 당겨진다. 앞서 "42번은 치환해도 된다"고 내린 판정이 이제 다른 후보를 가리키는 것이다. 판정을 재사용하려고 순번 대신 다음과 같이 ID를 만들었다.

```python
# id 는 내용 해시로 준다. 순번을 쓰면 추출 규칙을 한 번만 고쳐도 뒤쪽 id 가
# 전부 밀려 이미 받아 둔 판정이 통째로 무효가 된다 (실제로 겪음).
key = f"{r['file']}|{r['start']}|{r['old']}".encode()
r['id'] = 'd' + hashlib.sha1(key).hexdigest()[:10]
```
{: data-filename="scripts/sweeps/dd_extract.py · 일부 발췌"}

파일 경로, 파일 안에서 후보가 시작하는 문자 위치, 치환 전 원문을 이어 붙여 SHA-1 해시를 구하고, 그 앞 10자에 `d`를 붙여 ID로 쓴다. 원고가 그대로라면 다른 후보가 목록에 추가되거나 빠져도 이 세 값은 바뀌지 않으므로 기존 판정을 그대로 연결할 수 있다. 다만 원고를 수정해 문자 위치나 후보 원문이 바뀌면 ID도 달라진다. `dd_batch.py`는 이 ID가 붙은 후보를 묶어 에이전트에게 검토를 맡기고, `dd_merge.py`는 돌아온 판정을 ID별로 합친다.

치환이 끝나면 반대 방향의 잔재가 남는다. `\dd{x}`는 `\mathop{dx}`로 펼쳐지며 앞쪽 thin space를 스스로 넣는데, 예전에 손으로 적어둔 `\,`가 그 앞에 그대로 있으면 간격이 두 번 들어간다. `dd_despace.py`가 그것만 걷어낸다.

```python
PAT = re.compile(r'\\[,;:]\s*(?=\\dd\{)')
```
{: data-filename="scripts/sweeps/dd_despace.py · 일부 발췌"}

`\,` `\;` `\:` 셋만 지운다. 음수 간격 `\!`는 남긴다. 그건 겹쳐서 생긴 잔재가 아니라 글쓴이가 좁히려고 일부러 넣은 커닝일 수 있고, 의도를 알 수 없는 것은 건드리지 않는 편이 맞다. 게이트는 `dd_apply`의 것을 그대로 쓴다. 수식 밖 불변, 영역 보존, `$` 개수 일치, 그리고 KaTeX 렌더. 하나라도 깨지면 파일째 롤백된다.

마지막 게이트가 이 파이프라인에서 가장 값진 부분이다. 치환으로 바뀐 수식은 node 스크립트 `_katex_gate.js`가 `katex-macros.js`를 `vm`에서 실행해 얻은 실제 매크로로 렌더한다. 문자열 규칙을 아무리 잘 짜도 그것이 유효한 TeX인지는 렌더러만 안다.

`dd_apply`와 `dd_despace`는 기본이 dry-run이고, 글 파일을 쓰는 줄은 둘의 `if a.write:` 아래 한 줄씩이다. 600편의 수식에 손을 대는 것은 그 두 줄뿐이다.

## 부정 기호: 줄바꿈 원인

8월 20일에 사용자가 가환대수 글을 감사하던 중 짚은 것은 한 줄이었다.

> 지금 감사 페이지에 보면 "우선 $j\geq 2$인 각각에 대하여 $x_j\not\in \mathfrak{a}_1$이고 $\mathfrak{a}_1$이 prime i" 여기에서, \not과 \in 사이에 줄바꿈이 들어갔거든? 문단 폭이 달라서 정확히 이게 프로덕션 사이트 혹은 데브 사이트에서 반영되는 것은 아닌데 혹시 비슷한 문제가 프로덕션 혹은 데브 사이트에서 생길 수 있는지만 확인해줘. 꼭 여기가 아니더라도.

좁은 폭에서 사선(`/`)만 윗줄에 남고 `\in`은 다음 줄로 넘어간다. 사용자는 특정 글 하나를 지목했지만 질문은 다른 자리에서도 같은 일이 생기느냐였고, 답은 그렇다였다. `\not`이 코퍼스 전역에서 같은 방식으로 쓰이고 있었으므로 문단 폭만 맞으면 어디서든 재현될 수 있었다.

KaTeX가 수식 줄바꿈을 허용하는 자리는 아무 데나가 아니다. `buildHTML`에는 TeXbook 173쪽을 그대로 인용한 주석이 있다.

```js
// The TeXBook [p.173] says "A formula will be broken only after a
// relation symbol like $=$ or $<$ or $\rightarrow$, or after a binary
// operation symbol like $+$ or $-$ or $\times$, where the relation or
// binary operation is on the ``outer level'' of the formula (i.e., not
// enclosed in {...} and not part of an \over construction)."
```
{: data-filename="assets/katex/katex.js · TeXbook 인용 주석, 일부 발췌"}

구현은 최상위 수식을 관계(`mrel`)·이항연산(`mbin`) 기호 뒤에서 끊어 각 조각을 `.base`라는, 그 안에서는 절대 쪼개지지 않는 span으로 감싼다. 여기까지는 TeX의 관례를 그대로 재현한 것이라 버그가 아니다. 문제는 `\not`이 그 자체로 하나의 관계 atom이라는 데 있다. 레포의 KaTeX 0.16.0 사본에서 정의는 이렇다.

```js
defineMacro("\\not", '\\html@mathml{\\mathrel{\\mathrlap\\@not}}{\\char"338}');
```
{: data-filename="assets/katex/katex.js · KaTeX 0.16.0, 일부 발췌"}

`\@not`은 사선 하나짜리 심볼이고, `\mathrlap{\@not}`이 그 사선의 advance width를 0으로 만들어 오른쪽 글자와 겹쳐 그리게 한다. 그리고 그 전체를 감싼 `\mathrel{...}`가 독립된 관계 atom이 된다. 즉 `\not\in`은 관계 atom 두 개(사선 하나, `\in` 하나)가 연달아 있는 셈이다. `buildHTML`의 끊기 로직은 관계 atom 하나가 끝날 때마다 그 뒤를 줄바꿈 후보로 등록하므로, 사선 바로 뒤가 후보 자리가 된다. 뒤따르는 간격 중에 `\nobreak`가 있으면 그 후보를 취소하는 장치가 있지만, 이 `\not` 정의에는 그게 없다.

## 부정 기호: 매크로 수정과 검증

`katex-macros.js`의 `\not`은 인자를 받아, 사선과 그 뒤에 오는 것을 애초에 한 atom으로 묶는다.

```js
"\\not":"\\html@mathml{\\mathrel{\\mathrlap{\\@not}\\mathord{#1}}}{\\mathrel{\\char\"338 \\mathord{#1}}}",
```
{: data-filename="assets/js/katex-macros.js · 6296b65e 이후, 일부 발췌"}

여기서 `\mathord{#1}`은 인자를 일반 기호 atom인 mord로 취급하게 한 것이다. 감싸지 않으면 사선(`\mathrlap`이 만든 mord)과 인자 `\in`(mrel) 사이에 TeX 간격 규칙에 따라 thick space(0.2778em)가 들어가 둘이 벌어진다. 인자를 `\mathord`로 감싸면 mord 둘 사이에는 자동 간격이 붙지 않아, 사선이 인자와 간격 없이 겹친다. 이 처리는 8월 27일 커밋 6296b65e에서 폴리싱을 하며 추가된 것이다.

HTML 쪽은 `\mathrlap{\@not}` 뒤에 인자를 이어 붙여, 사선과 인자가 같은 `\mathrel{...}` 안에 들어간다. `buildHTML`이 볼 때는 처음부터 쪼갤 자리가 없는 단일 atom이다. `\nobreak`에 기대는 대신, 끊을 수 있는 경계 자체를 지운 셈이다. MathML 쪽은 원래 조합 문자 U+0338(`\char"338`) 하나만 얹었는데, 이 매크로는 인자까지 같은 `\mathrel` 안에 넣는다. `x\not\in A`의 MathML 출력은 `<mo>` 하나 안의 `∉`다.

4f107bf2의 커밋 메시지는 검증 결과를 이렇게 적어 뒀다. 코퍼스의 `\not` 포함 수식 482개를 구·신 매크로로 대조해 448개에서 base 수가 줄었고 신규 파싱 실패는 0건, 나머지 34개는 `cases` 셀·`\text`·아래첨자 안이라 애초에 안전했다는 것이다. diff에서 직접 확인되는 것은 인자 문법이 바뀌면서 깨진 네 곳이다. 매크로 인자 `#1`은 토큰 하나를 받는데, `\mathrel`은 그 자체로 제어열 토큰 하나이고 `{R}`은 별개다. `\not\mathrel{R}`이라 쓰면 `#1`엔 `\mathrel` 하나만 들어가고 뒤의 `{R}`은 인자 바깥에 남아 파싱이 깨진다. 묶으려면 전체를 중괄호로 싸서 한 그룹, 곧 하나의 토큰으로 만들어야 한다.

```diff
- $y\not\mathrel{R}x$
+ $y\not{\mathrel{R}}x$
```

Order_Relations 글 두 언어판(en·ko)의 asymmetric 정의와 그 증명, 총 네 곳(`R` 둘, `S` 둘)이 이 형태였다. 렌더는 글리프 단위로 전과 같다.

이 매크로 뒤로는 `\not` 뒤에 무엇이 오든 사선과 그 기호 사이에 끊을 자리가 없다.

## 여접 복합체: degree 표시 매크로

9월 초에 쓰던 cotangent complex 글에서는 naive cotangent complex를 두 항짜리 복합체로 적을 때, 어느 항이 degree 1이고 어느 항이 degree 0인지를 매번 산문으로 짚어야 했다. 이를 항 아래에 숫자로 표시하려고 만든 매크로가 `\at`이다.

> 언더브레이스 비슷한 건데, 언더브레이스에서 괄호만 없는 거 혹시 없을까? 그러니까 지금 코호몰로지 쓸 때, 거기 밑에다가 조그맣게 1,0 해가지고 어디 디그리가 어딘지 써주면 굳이 산문에서 디그리 얘기 꼬박꼬박 안 해줘도 될 것 같아서.

`\underset`으로 시작했지만 방향은 한 번 뒤집혔다. "다른 사람들이 이거 어떻게 처리해?"라고 관례를 물은 다음 나온 답은 "언더셋 하지 말고 그냥 산문으로 한 번 말하고 끝내기로 하자"였다. 몇 분 뒤 다시 뒤집혔다.

> 미안 마음이 또 바뀌었어. Underset으로 하되. 내가 지금 Underset 표기에서 약간 걸리는 거는 1이랑 0이 생각보다 좀 잘 보이게 돼 있어 가지고 그렇거든. 색을 바꿔볼까? 어차피 블로그니까. 약간 회색으로?

회색으로 죽이는 안은 곧바로 다시 뒤집혔다. 뮤티드 그레이로 넣어 보라고 해놓고는, 결과를 보고 마음을 바꿨다.

> 눈에 잘 띄게 그리고 다른 그래프에서도 맞게. 색깔을 브레스 골드색으로 하는 것도 나쁘지 않은 것 같은데 어떻게 생각하는지.

최종 색은 `#a56f14`다. `_sass/_diagram-colors.scss`의 `$diag-accent1`, `palette.sty`의 `accent1`(RGB 165,111,20)과 같은 값으로, 다이어그램에서 강조에 쓰는 브래스 톤이다. 색만 죽이는 게 아니라 숫자가 항에 붙는 느낌도 문제라는 걸 사용자가 짚었으므로, 첫 정의부터 색과 세로 간격을 같이 넣었다.

9월 6일 저녁의 정의는 이렇다.

```js
"\\at":"\\underset{\\rule{0pt}{0.8em}\\textcolor{##a56f14}{#1}}{\\mkern1mu\\vphantom{X_{X/X}}\\smash[b]{#2}\\mkern1mu}",
```
{: data-filename="assets/js/katex-macros.js · cbb78517 시점, 일부 발췌"}

`#`이 KaTeX 매크로 인자 기호와 겹치므로 색의 리터럴 `#`은 TeX 관례대로 `##`로 두 번 적는다. 밑에 붙는 쪽의 `\rule{0pt}{0.8em}`은 폭 0짜리 strut으로, 항과 숫자 사이에 세로 간격을 준다.

항 쪽의 장치는 두 번째 커밋 cbb78517에서 들어왔다. 첫 정의는 `#2`를 그대로 받았는데, $\mathfrak{a}/\mathfrak{a}^2$처럼 아래첨자 없는 항과 $\Omega_{B/A}\otimes_BC$처럼 아래첨자가 있는 항을 나란히 두면 후자의 depth가 더 깊어 밑에 붙는 숫자의 높이가 어긋났다. 두 번째 커밋 뒤에는 `\vphantom{X_{X/X}}`가 이중 아래첨자 깊이의 보이지 않는 버팀대를 세워 모든 항의 depth를 그 값으로 고정하고, `\smash[b]`가 실제 항의 depth를 무시하게 만든다. 양옆의 `\mkern1mu`는 항 주위에 좁은 수평 여백을 낸다. 그래서 

$$\NL_{C/A}=[\at{1}{\mathfrak{a}/\mathfrak{a}^2}\to\at{0}{\Omega_{B/A}\otimes_BC}]$$

처럼 써도 숫자 1과 0이 같은 높이에 나란히 놓인다.

이 매크로를 쓰는 글은 여접 복합체 글 하나뿐이다. 그 글의 1과 0 둘을 표시하는 데만 쓰이는데, 그 둘의 처우는 내 처우보다 훨씬 신중하게 검토되고 있었다.
