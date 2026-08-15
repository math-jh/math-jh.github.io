---

title: "매크로 안에 숨은 d"

excerpt: "글자마다 따로 만든 매크로와 손으로 넣은 간격에 흩어져 있던 미분 기호를 \\dd 하나로 모으면서, 정규식이 \\prod의 d까지 세는 것을 발견하고 토크나이저로 갈아엎은 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/differential_sweep

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-07
last_modified_at: 2026-08-15

weight: 38

---

관련 파일: [`scripts/sweeps/dd_extract.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/dd_extract.py), [`scripts/sweeps/dd_apply.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/dd_apply.py), [`scripts/sweeps/dd_despace.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/dd_despace.py), [보강 커밋](https://github.com/math-jh/math-jh.github.io/commit/a8e2c693)
{: .notice--info}

미분 기호를 적는 방법이 코퍼스 안에 여러 갈래로 흩어져 있었다. 자주 나오는 것은 `\dx`, `\dy`처럼 글자마다 매크로를 따로 정의해 뒀고, 매크로를 새로 짤 만큼 자주 나오지는 않는 글자들은 그때그때 처리했다. `\,dx`로 앞 간격을 손으로 넣기도 하고, `\mathop{dx}`를 직접 적기도 했다. 같은 것을 적는 방법이 셋인데 그중 둘은 글쓴이가 매번 기억해야 한다.

`\dd{}`는 그 셋을 하나로 모으려고 만든 매크로다. 인자를 받아 `\mathop{d#1}`로 펼치므로 로만체 d와 앞쪽 간격이 한 번에 따라오고, 글자마다 매크로를 새로 정의할 이유도 없어진다. 이 스윕은 매크로를 만든 뒤에 남은 일, 그러니까 이미 쓰인 세 갈래를 전부 `\dd{}`로 되돌리는 작업이다. 대상은 600편 남짓이고 전부 수식 안이라 한 글자만 잘못 건드려도 렌더가 깨진다.

이 레포에서 일괄 치환은 정해진 절차가 있다. 결정론 스크립트로만 하고, 수식 밖은 불변임을 게이트로 확인하고, 판단이 애매한 것은 치환하지 말고 사람에게 넘긴다. 추출기 `dd_extract.py`는 후보를 뽑아 네 갈래로 분류만 하고 파일은 쓰지 않는다. 쓰는 일은 `dd_apply.py`가 한다.

옛 표기 셋 가운데 가장 쉬운 것은 손으로 적어둔 `\mathop{dx}`다. 이미 미분으로 표시돼 있어 의미가 확정이니, 인자만 꺼내 통째로 개명하면 된다. 분류에서 `MATHOP`이라는 갈래를 따로 둔 이유가 그것이다.

{% raw %}
```python
# 이미 \mathop{d...} 인 것: 통째로 \dd{...} 로 개명
for m in re.finditer(r'\\mathop\{d([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', body):
    out.append(dict(kind='MATHOP', ..., old=m.group(0),
                    new='\\dd{%s}' % m.group(1), reason='기존 \\mathop{d…}'))
```
{: data-filename="scripts/sweeps/dd_extract.py"}
{% endraw %}

어려운 것은 나머지다. 손으로 간격을 넣어 둔 `\,dx`나 아무 표시 없는 `dx`는 그 d가 미분인지, 이름이 d인 변수인지, 아니면 매크로 이름의 일부인지를 문맥에서 판정해야 한다. 그 판정 결과가 `AUTO`(자동 치환) / `AMBIG`(사람에게) / `SKIP`(대상 아님)이다.

## 정규식이 세는 d, 사람이 보는 d

문제는 "홀로 선 d"를 찾는 부분이었다. 처음에는 lookbehind 정규식으로 앞뒤를 보고 판정했는데, 이 방식은 매크로 이름 안의 d를 걸러내지 못한다. `\prod(`는 정규식 눈에 `d(`가 들어 있고, `\tilde`도 마찬가지다. 미분과 아무 상관 없는 곱 기호가 미분 후보로 올라온다.

수식은 문자열이 아니라 토큰 열이다. 그렇게 훑으면 문제가 사라진다.

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
{: data-filename="scripts/sweeps/dd_extract.py"}

역슬래시를 만나면 매크로 이름 전체를 한 번에 건너뛴다. 그 안의 글자는 애초에 후보 위치로 등록되지 않으므로, 뒤에서 무엇을 검사하든 `\prod`의 d가 다시 나타날 일이 없다. 열 줄이 안 되는 함수인데, 앞뒤를 보는 규칙을 아무리 정교하게 다듬어도 얻지 못하던 성질을 스캔 방향 하나로 얻는다.

## 피연산자의 경계

d를 찾았으면 그다음은 "무엇의 미분인가"를 정해야 한다. `\dd{...}`의 중괄호 안에 들어갈 범위이고, 여기서 세 종류가 걸렸다.

아래첨자에 매크로 인자가 붙는 경우가 하나다. `d\varphi_\mathcal{L}`에서 피연산자는 `\varphi_\mathcal{L}` 전체다. 아래첨자를 한 글자로 끊으면 중괄호 밖에 `\mathcal{L}`이 남아 식의 의미가 바뀐다. 앞의 공백을 흡수하는 것도 하나다. `d \y_k`처럼 사이가 벌어져 있으면 그 공백까지 먹어야 매크로가 자기 간격을 넣었을 때 겹치지 않는다.

나머지 둘은 반대로 손대지 않기로 한 경우다. 악센트의 인자로 들어간 d, 그러니까 `\bar d(...)`의 d는 미분 기호가 아니라 이름이 d인 무언가에 바가 씌워진 것이다. 라플라시안을 적는 `d d^\ast`의 홑 d도 마찬가지로 연산자이지 미분이 아니다. 둘 다 예전 규칙에서는 치환 대상으로 올라와 식을 깨뜨렸고, 이제 `SKIP`으로 분류된다.

## 순번을 버리고 해시로

이 스윕은 한 번에 끝나지 않는다. 추출하고, 사람이 `AMBIG` 목록을 훑어 판정을 주고, 규칙을 고쳐 다시 추출한다. 그런데 후보 id가 순번이면 그 반복이 성립하지 않는다.

```python
# id 는 내용 해시로 준다. 순번을 쓰면 추출 규칙을 한 번만 고쳐도 뒤쪽 id 가
# 전부 밀려 이미 받아 둔 판정이 통째로 무효가 된다 (실제로 겪음).
key = f"{r['file']}|{r['start']}|{r['old']}".encode()
r['id'] = 'd' + hashlib.sha1(key).hexdigest()[:10]
```
{: data-filename="scripts/sweeps/dd_extract.py"}

규칙을 고쳐 후보 하나가 목록 앞쪽에서 빠지면 그 뒤 전부가 한 칸씩 당겨진다. `c00042`에 대해 받아 둔 판정은 이제 다른 후보를 가리킨다. 파일 경로와 오프셋과 원문 문자열로 해시를 만들면 그 후보가 목록 어디에 있든 같은 id를 유지한다. 주석에 "실제로 겪음"이라고 적혀 있는 것은 겪고 나서 고쳤다는 뜻이다.

## 매크로가 넣는 간격, 손으로 넣은 간격

치환이 끝나고 나면 반대 방향의 잔재가 남는다. `\dd{x}`는 `\mathop{dx}`로 펼쳐지며 앞쪽 thin space를 스스로 넣는데, 예전에 손으로 적어둔 `\,`가 그 앞에 그대로 있으면 간격이 두 번 들어간다. `dd_despace.py`가 그것만 걷어낸다.

```python
PAT = re.compile(r'\\[,;:]\s*(?=\\dd\{)')
```
{: data-filename="scripts/sweeps/dd_despace.py"}

`\,` `\;` `\:` 셋만 지운다. 음수 간격 `\!`는 남긴다. 그건 겹쳐서 생긴 잔재가 아니라 글쓴이가 좁히려고 일부러 넣은 커닝일 수 있고, 의도를 알 수 없는 것은 건드리지 않는 편이 맞다. 게이트는 `dd_apply`의 것을 그대로 쓴다. 수식 밖 불변, 영역 보존, `$` 개수 일치, 그리고 KaTeX 렌더.

마지막 게이트가 이 파이프라인에서 가장 값진 부분이다. 치환 전후의 수식을 블로그의 실제 매크로 정의와 함께 node로 렌더해 보고, 하나라도 렌더에 실패하면 그 파일은 쓰지 않는다. 문자열 규칙을 아무리 잘 짜도 그것이 유효한 TeX인지는 렌더러만 안다. 기본 동작이 dry-run이고 `--write`를 줘야 파일을 건드리는 것도 같은 태도다.

전부 합쳐도 스크립트 다섯 개에 수백 줄이다. 이 정도 장치를 세우고 나서야 600편의 수식에 손을 댈 마음이 든다는 것이, 자동 치환이라는 말이 실제로 무엇을 요구하는지를 그대로 보여준다.
