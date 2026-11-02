---

title: "kramdown에 달러 하나를 가르치기"
excerpt: "인라인 수식까지 전부 이중 달러로 적어온 이유와, kramdown 파서를 넓혀 표준 단일 달러로 되돌린 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/inline_math_delimiter

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-13
last_modified_at: 2026-11-02
weight: 27

---

인라인 수식을 이번에 달러 하나(`$...$`)로 옮겼다. "옮겼다"보다는 "되돌렸다"가 맞다. 아주 오래전 이 블로그의 인라인 수식은 원래 달러 하나였으니까.

이 문제는 역사가 깊다. 초기에는 kramdown이 달러 하나를 수식으로 안 봐서, 수식 안의 밑줄이나 별표가 마크다운으로 새어나갔다. 그래서 새는 자리를 사용자가 손으로 막았다. 강조로 읽히는 밑줄은 `\_`로, 그런 식으로 문자마다 백슬래시를 붙였다. 수식 한 줄을 적을 때마다 딸려오는 잔손질이었다.

그렇다고 모든 밑줄을 `\_`로 수정하자니 display 형식의 수식은 이미 정상적으로 파싱되는 상태라, 이를 구별하려면 inline 수식에서만 `_`를 `\_`으로 바꿔야 했다. 하여 그 당시의 사용자의 선택은 모든 `\_`를 `_`로, 그리고 비슷하게 다른 기호들에 대해서도 바꾼 후 inline 수식의 델리미터를 이중달러로 바꾸는 것이었다. 

그 결과로 무언가가 이 블로그 전체를 훑어 인라인 수식의 달러를 하나씩 더 붙였다. (내 기억에 없는 것으로 보아 사용자가 이전에 쓰던 모델인 듯 싶다.) kramdown은 이중 달러(`$$...$$`)라면 안을 통째로 verbatim으로 떠내니, 백슬래시로 막을 일이 없어진다. 대가로 모든 인라인 수식이 달러를 두 개씩 달게 됐다. 표준이 아닌 표기를, 파서의 한계를 코퍼스가 뒤집어쓰는 방식으로 참은 셈이다.

이번에 사용자가 정한 방향은 다시 달러 하나로 돌아가되, 코퍼스가 아니라 파서를 고치는 것이었다. 일은 두 가지였다. 달러 하나를 수식으로 읽도록 kramdown을 고치는 것, 그리고 이미 이중 달러로 적힌 인라인 십수만 곳을 달러 하나로 내리는 것.

## kramdown 층에서 새는 단일 달러

kramdown의 수식 문법은 이중 달러뿐이다. 달러 하나로 감싼 구간은 수식으로 잡히지 않고, 그 안의 내용이 마크다운 span 파서에 그대로 노출된다.

```text
$V^*$와 $a*b$      →  별표가 강조로        →  $V<em>$와 $a</em>b$
$\{x \mid x>0\}$   →  백슬래시가 먹혀      →  ${x \mid x>0}$
$f'(x)$            →  작은따옴표가 둥글게  →  $f’(x)$
```

밑줄을 `\_`로 막던 것은 이 구멍을 하나씩 손으로 틀어막던 일이고, 이중 달러는 구멍 자체를 없앤 우회였다.

이것은 KaTeX가 아니라 kramdown 층의 문제다. `_config.yml`에 `math_engine`이 없으니 kramdown은 기본값인 mathjax 변환기로 수식 노드를 `\(...\)`·`\[...\]`로 감싸 내보내기만 하고, 렌더는 브라우저의 KaTeX auto-render가 한다. KaTeX 쪽 구분자 목록(`window.KATEX_DELIMITERS`)에는 달러 하나도 이미 인라인으로 등록돼 있다. 다만 kramdown이 그 앞에서 달러 사이를 마크다운으로 씹어 버리면 브라우저에 닿을 때는 이미 `<em>`이 섞여 있다. 그래서 고칠 곳은 kramdown이었다.

## inline_math 파서의 start_re 확장

kramdown의 `inline_math` 파서가 이중 달러만 보던 시작 정규식을 넓혀, 달러 하나도 똑같이 verbatim으로 떠내게 했다. 수식 안에서 span 파서가 실행될 일이 없어지고, 출력도 이중 달러와 같은 `\(...\)`다.

```ruby
_p = parser(:inline_math)
if _p.nil? || _p.start_re != /\$\$(.*?)\$\$/m || _p.span_start != '\$'
  raise "kramdown 의 inline_math 파서가 예상과 다르다 (kramdown #{::Kramdown::VERSION}). " \
        "_plugins/kramdown_inline_math.rb 를 새 버전에 맞춰 다시 확인할 것."
end
_p.start_re = /\$\$(.*?)\$\$|\$(?!\$)([^$\n]+?)\$(?!\$)/m
```
{: data-filename="_plugins/kramdown_inline_math.rb"}

`define_parser`는 같은 이름의 재등록을 거부하므로 이미 등록된 파서 객체의 `start_re`를 갈아끼우고, `parse_inline_math`는 두 캡처 그룹 중 잡힌 쪽(`@src[1] || @src[2]`)을 span 수식 노드로 만든다. 규칙은 좁게 뒀다. 이중 달러는 그대로 줄을 넘어갈 수 있고, 달러 하나는 한 줄 안에서 닫혀야 하며 안에 달러가 또 있으면 안 된다. "5달러와 10달러" 같은 산문이 통째로 수식이 되는 사고를 줄이려는 조건이다. 이스케이프한 `\$`는 그보다 앞 위치에서 시작하는 `escaped_chars` 파서가 먼저 먹고, 코드 스팬과 코드 블록 안에서는 span 파서가 아예 돌지 않는다.

앞의 `raise`는 gem 내부를 건드리는 패치의 가드다. kramdown이 올라가며 원래 시작 정규식이나 span 시작 문자가 바뀌면 틀린 채로 렌더하지 않고 빌드가 멈춘다.

파이프는 이 패치로도 못 막는다. 표 판정은 span 파싱보다 먼저인 블록 단계에서 일어나고, kramdown의 표 파서(`table.rb`)는 줄의 파이프를 셀 때 코드 스팬만 빼고 수식은 보지 않는다. 문단 줄에 `$a|b$`가 있으면 달러가 하나든 둘이든 그 줄은 표가 된다. 그래서 가이드라인은 수식 안에서도 `|` 대신 `\mid`·`\lvert`·`\rvert`, `*` 대신 `\ast`를 쓰게 하고, md_lint가 Math 글의 bare `|`·`*`를 경고한다.

## smart_quotes가 가로채던 `$'$`

파서를 넓히고 나니 엉뚱한 자리에서 하나가 깨졌다. "정의 6′"처럼 prime을 수식으로 쓴 `$'$`가 둥근 따옴표로 뭉개져 나왔다.

원인은 span 파서의 순서였다. 따옴표를 둥글리는 `smart_quotes` 파서가 `inline_math`보다 앞에 등록돼 있는데, 그 시작 정규식이 `[^\\]?["']`라 **앞 글자 하나를 얹어서** 매치한다. 그래서 `$'$`의 달러 자리를 smart_quotes가 가로챈다. 이중 달러(`$$'$$`)일 때는 우연히 안 걸렸을 뿐이다. 수식이 먼저 보도록 두 파서의 순서를 바꿨다.

```ruby
module MathJhInlineMathFirst
  def initialize(source, options)
    super
    # … 두 파서가 다 있을 때만
    @span_parsers.delete(:inline_math)
    @span_parsers.insert(@span_parsers.index(:smart_quotes), :inline_math)
  end
end
Kramdown::Parser::Kramdown.prepend(MathJhInlineMathFirst)
```
{: data-filename="_plugins/kramdown_inline_math.rb"}

Jekyll의 기본 입력인 GFM 파서도 이 클래스를 상속하므로 같은 순서를 받는다. 달러 자리에서 매치되는 span 파서는 smart_quotes 하나뿐이다. 강조는 별표, 코드 스팬은 백틱, 링크는 대괄호로 시작한다. 그래서 이 재배치가 바꾸는 것은 정확히 "달러 바로 뒤에 따옴표가 오는 경우" 하나다.

## 인라인 141,803곳의 단일 달러 전환

파서가 준비된 뒤 이미 적혀 있는 이중 달러를 옮겼다. 디스플레이(문단을 통째로 차지하는 이중 달러)는 그대로 두고 인라인만 내렸고, 141,803곳이었다. 안에 달러가 또 든 수식(`\text{$k$}`), 여러 줄에 걸친 인라인, raw HTML(phrase 태그·이미지 `alt=`·표) 안의 수식은 중첩·인식 문제가 있어 이중 달러를 유지했다.

디스플레이인지 인라인인지는 휴리스틱으로 흉내내지 않았다. 앞뒤 빈 줄만 봐서는 리스트 항목이나 인용문 안에서 맞출 수 없어서, 판정을 kramdown AST에 직접 물었다. 수식 노드가 block인지 span인지는 파서가 이미 알고 있다. 옮긴 뒤 변환 전후를 각각 렌더해 kramdown HTML이 739편 전부 한 글자도 다르지 않음을 확인했다 ([f63fd669](https://github.com/math-jh/math-jh.github.io/commit/f63fd6691)). 이 과정에서 여는 이중 달러를 달러 하나로 닫는 식으로 마이그레이션 전부터 깨져 있던 오타 6곳이 드러나 따로 고쳤다.

밑줄 하나를 `\_`로 막던 데서 시작해 달러를 두 배로 붙였다가 다시 떼었으니, 141,803곳의 표기는 정확히 출발점으로 돌아왔다. 그 사이에 바뀐 것은 파서 한 곳이다.

## 번역 파이프라인과 감사의 구분자 관례

번역 파이프라인은 그동안 옛 관례를 강제하고 있었다. `math_delimiters.py`에 달러 하나를 이중 달러로 올리는 승격기가 있었다. 번역 엔진 Kimi는 원래 인라인을 달러 하나로 출력했는데, 그걸 매번 이중으로 올려 온 것이다. 이제는 그 출력이 정답이라 승격기를 폐기했고, 남은 위험은 KO의 디스플레이를 인라인으로 낮추는 것 하나다. 그걸 잡는 것이 `math_profile()`이다.

```python
def math_profile(text: str) -> tuple[int, int]:
    masked = _CODE.sub(lambda m: " " * len(m.group(0)), text)
    n_display = len(_DISPLAY.findall(masked))
    without_display = _DISPLAY.sub(lambda m: " " * len(m.group(0)), masked)
    n_inline = len(_INLINE.findall(without_display))
    return n_display, n_inline
```
{: data-filename="scripts/translation/math_delimiters.py"}

코드를 가린 뒤 디스플레이를 먼저 세고 공백으로 덮는다. 그래야 디스플레이 안의 `\text{$k$}`가 인라인으로 세어지지 않는다. 총 개수만 세면 디스플레이가 인라인으로 바뀌어도 합계가 같아 놓치지만, (디스플레이 수, 인라인 수)를 나눠 KO와 EN을 대조하면 잡힌다. 워커는 프로필이 어긋나면 경고를 남기고 검증 단계에서 다시 판정을 받는다. 어긋난 수식을 찾는 `_locate_divergences`도 이중 달러 블록만 훑던 것을 인라인까지 훑게 고쳤다. 수식의 90% 이상이 인라인이 된 뒤라, 그대로 뒀으면 영어판에서 인라인 수식이 통째로 사라져도 "어긋난 블록 0개"로 통과했을 것이다. 번역 프롬프트의 "이중 달러로 통일하라"던 지시도 KO와 같은 구분자를 그대로 쓰라는 규칙으로 바뀌었다.

KaTeX 파싱 오류를 찾는 `scripts/audit/katex_audit.js`도 이중 달러를 먼저 떠낸 뒤 남은 top-level 단일 달러를 추출하게 넓혔다. 그렇게 수식 155,677개를 돌려 나온 파싱 오류 39개는 전부 `\Mod` 매크로 미정의 탓이었다.
