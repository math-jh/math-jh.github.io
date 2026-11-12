---

title: "일괄 복원으로 사라진 개정분의 복구"
excerpt: "180편을 마지막 정상 판본으로 되돌린 복원이 어떤 판본을 집었는지 본문 해시로 되짚고, 함께 사라진 개정분을 골라 되살린 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/audit_revert_recovery

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-06

weight: 48
group: admin

---

관련 파일: [965acc26](https://github.com/math-jh/math-jh.github.io/commit/965acc26), [f29cfd09](https://github.com/math-jh/math-jh.github.io/commit/f29cfd09), [a17b4650](https://github.com/math-jh/math-jh.github.io/commit/a17b4650)
{: .notice--info}

8월 전수 감사의 지적을 반영하는 동안 200편 남짓한 수학 글이 `revising: true`를 달고 [직전 판본으로 동결된 채](/ko/llm_workshop/revising_freeze) 서빙되고 있었다. 사용자가 실제로 소화할 수 있는 속도로는 그 개정이 언제 끝날지 기약이 없었고, 결국 사용자는 그중 180편을 마지막 정상 판본으로 되돌렸다. 되돌린 결정 자체는 다시 뒤집지 않는다는 것이 이번 작업의 전제였다. 사용자가 보고 싶어 한 것은 그 복원과 함께 사라진 수정이었다.

> 근데 이제 감사 결과와 무관하게 내가 해놨던 수정들이 있을 텐데, 결과를 보고 고쳐서 괜찮아진 거. 그거는 커밋 안 했어. 근데 이제 감사 결과 revising true가 되어 있는 것들 중에서 이제 얼마나 예전 것들이 바뀌었는지 그런 거를 좀 보고 싶거든.

복원 커밋 `965acc26`의 메시지는 어느 시점으로 되돌렸는지 적지 않는다. "마지막 정상 판본"이 파일마다 다른 날짜일 수 있으니, 파일별로 그 판본을 역추적하는 것이 첫 일이었다.

## 본문 해시로 찾은 복원 원천

복원 후 각 파일의 내용이 과거 어느 커밋의 blob과 같은지 찾으면 된다. 다만 blob 그대로 비교하면 맞지 않는다. 복원이 frontmatter에서 `revising: true`(대개 `drift_needed: true`까지)를 지웠으므로, frontmatter를 떼고 본문만 비교한다.

```python
FM = re.compile(r'\A---\n.*?\n---\n', re.S)

def body(rev, f):
    return FM.sub("", sh("git", "show", f"{rev}:{f}"), count=1)

for f in files:
    nb = hashlib.sha1(body(R, f).encode()).hexdigest()
    for c in sh("git", "log", "--format=%H", f"{R}^", "--", f).split():
        if hashlib.sha1(body(c, f).encode()).hexdigest() == nb:
            src = c
            break
```
{: data-filename="복원 원천 추적 · 일회성 스크립트, 원본 미보존, 일부 발췌"}

`R`은 복원 커밋이다. 파일마다 `R`의 본문 해시를 구한 뒤, 복원 직전 커밋 `R^`부터 그 파일을 건드린 커밋을 최신순으로 내려가며 본문 해시가 같은 첫 커밋을 `src`로 잡는다. `src`가 잡히면 `src..R^` 사이에 그 파일을 건드린 커밋들이 곧 복원이 지나쳐 버린 것들이다. 그 목록에서 감사 커밋과 `[lastmod-skip]`을 빼면 남는 것이 실질 손실이다.

처음 돌린 판에서는 frontmatter를 이렇게 뗐다.

```python
p = t.split("\n---", 2)
if len(p) >= 3:
    return p[2]
```
{: data-filename="복원 원천 추적 첫 판 · 일회성 스크립트, 원본 미보존, 일부 발췌"}

파일 첫 줄의 `---` 앞에는 개행이 없으므로, `\n---`로 자르면 첫 번째 자리는 frontmatter를 닫는 줄이고 두 번째 자리는 본문에서 처음 나오는 `---`이다. 본문 중간에 수평선 `---`이 있는 글에서는 `p[2]`가 그 수평선 뒤의 토막만 남는다. 잘린 뒷토막끼리는 우연히 같기 쉬우니 매칭이 헐거워지고, 180편 중 178편이 "정확히 일치"로 나왔다. 그럴 리가 없다. 표본으로 고른 `Algebraic_Groups`를 열어보니 매칭됐다는 커밋과 실제 본문이 달랐다. 정규식으로 바꾸고 다시 돌리자 복원 원천이 8월 13일 감사 커밋 `635a8f80`으로 140편, 나머지는 6월까지 흩어졌다. 다이어그램 참조가 `frozen/<sha8>/` 사본으로 바뀐 15편은 본문까지 달라져 있어서, 이 비교로는 원천이 잡히지 않는다.

여기서 복원의 성격이 드러났다. 8월 13일 감사 1차 반영은 살아 있고, 8월 15일 2차 반영과 그 뒤 `revising` 상태에서 진행하던 개정이 버려진 구조다. 감사 결과 전체를 되돌린 것이 아니었다.

## 정리 박스가 줄어든 13편

복원이 지나친 커밋 중 감사·기계 커밋이 아닌 것은 4건뿐이었다. 그런데 사용자가 물었다.

> 혹시 비슷하게 그 판본 이후에 대규모로 내가 추가한 거 그런 거 없어? 몇 개 있을 것 같은데.

커밋 단위로 보면 안 잡히는 것이 있었다. [fenced-div 정리 박스와 전처리 플러그인](/ko/llm_workshop/fenced_theorem_blocks) 작업에서 정리 박스를 일괄 변환한 7월 3일 커밋 `b07d82dc`는 `[lastmod-skip]`이라 위 목록에서 빠진다. 그 대신 복원 diff에서 `:::` 블록이 순감소한 글을 세면 된다.

```python
d = sh("git", "show", "965acc26", "--", f)
removed = [l[1:] for l in d.split("\n") if l.startswith("-::: ")]
added   = [l[1:] for l in d.split("\n") if l.startswith("+::: ")]
```
{: data-filename="정리 박스 증감 집계 · 일회성 스크립트, 원본 미보존, 일부 발췌"}

`-::: `로 시작하는 줄은 복원으로 사라진 정리 박스의 여는 줄이고, `+::: `로 시작하는 줄은 복원으로 생긴 여는 줄이다. 닫는 줄 `:::`은 뒤에 공백이 없어서 세어지지 않는다. 사라진 쪽이 더 많은 글이 후보다.

13편이 걸렸고, 그중 9편은 `:::` 블록이 0이 되고 `<div class="definition">` 같은 HTML 박스가 생겼다. 7월 3일 변환 이전 판본으로 돌아간 것이다. 줄 수로 보면 `가환대수학/미분`이 399줄에서 157줄로, `갈루아 기본정리`가 217줄에서 50줄로, `사교다양체`가 174줄에서 24줄로 줄었다. 마지막 것은 정의 1 하나만 남은 상태였다. 갈루아 기본정리는 증명 블록이 열려 있고 안이 비어 있었다.

이 글들은 hunk 패치가 안 붙는다. 형식 자체가 다른 문서에 문단 단위 diff를 대는 일이라, `965acc26^` 판본을 통째로 가져오고 frontmatter의 플래그만 손대는 쪽으로 갔다.

```bash
git show "$BASE^:$f" | sed '/^revising: true$/d' > "$f.tmp$$"
mv "$f.tmp$$" "$f"
```
{: data-filename="run.sh 판본 복구부 · 원본 미보존, 일부 발췌"}

`$BASE`는 복원 커밋이다. 그 직전 커밋의 파일을 꺼내 `revising: true` 줄만 지우고, 임시 파일을 거쳐 제자리로 옮긴다. `drift_needed`는 남겼다. 이걸 지우면 EN 짝이 낡은 채로 굳는다. `가환대수학/미분`은 복구 직후 KO가 블록 26개인데 EN은 8개짜리 옛 판본이었고, 이 플래그가 그 글을 번역 워커의 재번역 큐로 보낸다. 재번역이 끝나면 EN도 26개가 된다.

## 명제 8이 빠지자 어긋난 인용 여덟 곳

8월 20일에 분수체 글에 universal property가 명제 8로 들어갔고, 뒤 번호가 한 칸씩 밀렸다. 같은 날 다른 커밋이 그 밀림을 따라가는 인용 갱신을 18개 파일에 걸쳐 처리했다. 복원은 분수체 글을 되돌렸지만 인용 갱신 쪽은 7편만 되돌렸다. 명제 8이 사라져 번호가 당겨졌는데 인용은 밀린 번호 그대로 남은 파일들이 생겼다.

라벨이 실제로 존재하는지 보면 잡힌다. 한쪽 언어만 보면 안 되는데, `prop10` 인용 네 곳이 전부 `/en/` 경로였기 때문이다.

```python
SRC = {"ko": ".../ko/2024-05-08-Field_of_Fractions.md",
       "en": ".../en/2026-03-11-Field_of_Fractions.md"}

lab = {k: labels_of(v) for k, v in SRC.items()}
bad = {}
for f in glob.glob("_posts/**/*.md", recursive=True):
    for m in re.finditer(r'/(ko|en)/math/algebraic_structures/field_of_fractions#(\w+)',
                         open(f, encoding="utf-8").read()):
        if m.group(2) not in lab[m.group(1)]:
            k = f"{m.group(1)}:{m.group(2)}"
            bad[k] = bad.get(k, 0) + 1
```
{: data-filename="분수체 인용 라벨 검사 · 일회성 스크립트, 원본 미보존, 일부 발췌, 경로 줄임"}

두 언어판 분수체 글에서 지금 있는 라벨을 모은 뒤, `_posts` 전체에서 분수체 글을 가리키는 링크를 찾는다. 정규식의 `(ko|en)`이 링크의 언어를, `#(\w+)`가 앵커를 잡고, 앵커는 그 언어판의 라벨 집합에서 찾는다. 없는 앵커만 `언어:라벨` 단위로 센다.

실행 전 여덟 곳이 나왔다. `en:prop10` 넷, `en:prop15`·`en:def12`·`en:def14`·`ko:def14` 하나씩. 분수체 글을 복구하고 인용 갱신 커밋을 다시 얹으면 0이 된다.

이 검사가 놓치는 것도 있다. 라벨이 존재하기만 하면 통과하므로, `prop8`이 다른 명제를 가리키게 된 상태는 안 잡힌다. 실제로 그런 파일이 있었고, 그건 diff를 직접 읽어서 확인했다.

## 한 파일로 묶은 실행과 유령 `.rej`

복구할 일을 패치 여러 개로 쪼개 두었더니, 사용자는 실행할 파일 하나로 묶어 달라고 했다.

> 실행할 파일 하나로 하면, 내가 여기서 `!` prefix로 진행 가능하지.

`run.sh` 하나가 판본 복구, 패치 적용, 잔여 보정, 검증까지 순서대로 돈다. 패치 적용부는 3-way를 먼저 시도하고 실패하면 `patch`로 재시도하게 짰다.

```bash
out=$(git apply -3 "$p" 2>&1)
if [ $? -eq 0 ]; then
  echo "  적용: $name"
else
  out2=$(patch -p1 --forward --no-backup-if-mismatch < "$p" 2>&1)
```
{: data-filename="run.sh 패치 적용부 · 원본 미보존, 일부 발췌"}

이게 틀렸다. `git apply -3`은 파일 하나에서 3-way 병합이 충돌해도 나머지 파일은 적용하고, 충돌한 자리에는 마커를 남긴 뒤 1을 반환한다. 스크립트는 그 1을 보고 전부 실패로 판단해 `patch`를 또 돌렸고, `patch`는 이미 적용된 hunk를 만나 거절했다. 실행이 끝나고 `.rej`가 여덟 개 남았는데 여덟 개 다 내용은 이미 파일에 들어가 있었다.

```text
Localization         ⁋명제 10 → prop10   반영됨
Basic_Notions        ⁋명제 9  → prop9    반영됨 (2곳)
Algebra_of_Schemes   ⁋정의 12 / ⁋명제 15 반영됨
```
{: data-filename=".rej 대조 결과 · 일부, 출력 정리"}

진짜로 남은 것은 충돌 마커 한 곳이었다. `.rej`를 세는 것으로는 그 하나를 다른 일곱 개와 구분할 수 없으니, 결국 여덟 개를 다 열어서 대조했다. 반환값 하나를 잘못 읽은 대가치고는 시간이 꽤 들었다.

충돌한 곳은 `Algebra_of_Schemes`의 정의 1이었고, 차이는 구절 하나였다.

```diff
-... $X$가 *integral*인 것은 공집합이 아닌 임의의 열린집합 $U$에 대하여 ...
+... $X$가 *integral*인 것은 $X\neq\emptyset$이고 공집합이 아닌 임의의 열린집합 $U$에 대하여 ...
```
{: data-filename="_posts/Math/Scheme_Theory/ko/2025-02-05-Algebra_of_Schemes.md · f29cfd09 수정 전후, 정의 1 일부, 병기 생략"}

같은 글의 명제 4가 `integral`과 `reduced + irreducible`의 동치를 주장한다. 위상수학 쪽 `irreducible` 정의는 공집합이 아닐 것을 요구하므로, `integral` 쪽에 그 조건이 없으면 $X=\emptyset$에서 좌변만 공허하게 참이 되어 명제 4가 깨진다. `f29cfd09`에는 조건이 있는 쪽이 들어갔다.

복구는 두 커밋으로 나뉘었다. 본문이 되살아난 17편은 무태그 `f29cfd09`로, 용어 교체와 인용 cascade 13편은 `[lastmod-skip]`을 단 `a17b4650`으로 갔다. 한 파일에 실질 변경과 기계 변경이 섞인 두 편은 무태그 쪽에 넣었다.

되돌린 것을 다시 되돌린 셈이다. 정의 1 하나만 남은 24줄짜리 사교다양체 글은 복원 커밋 안에서 다른 179편과 함께 CI를 통과했다. 빌드는 줄 수를 세지 않는다.
