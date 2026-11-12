---

title: "크론 워커의 글 단위 파일 락"
excerpt: "서로가 돌고 있으면 틱을 통째로 건너뛰던 크론 워커들을, 같은 글을 만질 때만 비켜 가게 한 글 단위 flock"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/blog_file_lock

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-10
weight: 55
group: agents

---

관련 파일: [`scripts/lib/blog_file_lock.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/lib/blog_file_lock.py), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/translation/section_anchor_gate.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/section_anchor_gate.py), [`scripts/term-extraction/term_extract_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/term_extract_worker.py), [`scripts/dependency-classifier/dependency_classifier.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/dependency_classifier.py)
{: .notice--info}

이 Pi에서 글 본문을 고치는 크론 워커는 여럿이다. 번역 워커가 EN을 쓰고, 한글 수정 후속 워커가 요청받은 KO·EN 짝을 고치고, 용어 추출 워커가 KO에 한영 병기를 넣고, 링크 관계 분류기가 링크 IAL에 `data-relation`을 단다. 두 워커가 같은 파일을 동시에 쓰면 뒤에 쓴 쪽이 앞의 결과를 덮는다.

원래는 이것을 워커 단위로 피했다. 분류기는 시작하자마자 번역 워커와 용어 워커의 전역 락을 확인하고, 둘 중 하나라도 돌고 있으면 그 틱을 버렸다. 번역 워커가 Classifying Spaces 한 편을 폴리싱하는 20분 동안, Group Actions의 링크를 분류할 수 있는데도 쉬는 식이다. 백로그 수백 편을 소화하던 시기라 헛돈 틱이 곧 밀린 일정이었다.

## 경로마다 하나씩 잡는 flock

`scripts/lib/blog_file_lock.py`는 잠그는 단위를 파일로 내렸다 ([1eb104d7](https://github.com/math-jh/math-jh.github.io/commit/1eb104d7)). 락 파일은 `/tmp/blog-file-locks/` 아래 **절대경로의 SHA-256** 이름으로 만들고, 여러 파일은 한 번에 잡는다.

```python
def _canonical(paths):
    # All callers acquire in the same order, so a future blocking caller cannot
    # introduce an AB/BA deadlock.  resolve(strict=False) also gives prospective
    # translation output paths a stable identity before the EN file exists.
    return tuple(sorted({Path(p).resolve(strict=False) for p in paths}, key=str))

def try_acquire_file_locks(paths, *, lock_dir=LOCK_DIR):
    """..."""
    canonical = _canonical(paths)
    lock_dir.mkdir(parents=True, exist_ok=True)
    fds = []
    try:
        for path in canonical:
            name = hashlib.sha256(str(path).encode("utf-8")).hexdigest() + ".lock"
            fd = os.open(lock_dir / name, os.O_CREAT | os.O_RDWR, 0o664)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                os.close(fd)
                raise
            fds.append(fd)
        return FileLockSet(fds=fds, paths=canonical)
    except OSError:
        while fds:
            os.close(fds.pop())
        return None
```
{: data-filename="scripts/lib/blog_file_lock.py · 일부 생략, 타입 표기 생략"}

호출자는 잠글 경로들을 한 번에 넘긴다. `_canonical`이 경로를 절대경로로 정규화하고 중복을 없앤 뒤 문자열 순으로 정렬하면, 함수는 그 순서대로 경로마다 락 파일을 열어 `LOCK_EX | LOCK_NB`로 배타 flock을 시도한다. `LOCK_NB`라서 다른 프로세스가 쥐고 있으면 기다리지 않고 곧바로 `OSError`가 난다. 안쪽 `except`가 방금 연 디스크립터를 닫고 예외를 다시 던지면, 바깥 `except`가 그때까지 잡은 디스크립터를 전부 닫고 `None`을 돌려준다. 끝까지 다 잡으면 디스크립터 목록을 `FileLockSet`으로 감싸 돌려주고, 호출자가 `release()`를 부르거나 `with` 블록을 벗어날 때 닫힌다. 이름이 경로의 해시라서 `/`가 든 절대경로도 한 디렉토리 안의 파일 이름 하나가 된다.

설계의 요점은 세 가지다.

- **전부 아니면 전무.** 번역 워커는 KO와 EN을 짝으로 잠근다. 하나만 잡고 나머지를 기다리면, 다른 워커가 반대 순서로 같은 짝을 잡을 때 서로를 기다리게 된다. 위 코드가 하나라도 실패하면 앞서 잡은 것까지 놓는 이유다.
- **정렬된 획득 순서.** 모든 호출자가 절대경로 정렬 순으로 잡으므로 기다리는 호출자가 끼어도 AB/BA 교착이 생기지 않는다. 기다리는 쪽은 `acquire_file_locks(paths, wait_sec=...)`를 쓰는데, 이것도 부분 집합을 쥔 채 기다리지 않고 0.25초 간격으로 전체 시도를 되풀이할 뿐이다.
- **아직 없는 파일도 이름이 있다.** EN 번역은 처음 쓸 때 파일이 없다. `resolve(strict=False)`로 정규화하면 존재하지 않는 경로도 같은 락 이름을 받으므로, "EN을 새로 쓰려는 번역 워커"와 "그 EN을 막 만들어진 참에 읽으려는 분류기"가 같은 락에서 만난다.

락 파일은 지우지 않는다. 빈 파일은 만남의 장소일 뿐이고, 디스크립터를 닫으면 flock이 풀린다. 지우는 순간 이미 그 inode를 쥔 프로세스와 새로 만든 파일을 잡은 프로세스가 서로를 못 보게 된다.

## 잠긴 글을 건너뛰는 워커들

락을 못 잡은 워커는 기다리지 않는다. 번역 워커와 용어 추출 워커는 그 글을 빼고 다음 후보를 고른다. 번역 워커의 대상 선택이 전형이다.

```python
excluded: set[Path] = set()
target = find_next_target(state, excluded)
while target is not None:
    ko_path, en_path, _reason = target
    file_lease = try_acquire_file_locks([ko_path, en_path])
    if file_lease is not None:
        break
    log(f"content lock busy, skip target: {ko_path.relative_to(BLOG_ROOT)}")
    excluded.add(ko_path)
    target = find_next_target(state, excluded)
```
{: data-filename="scripts/translation/translate_worker.py · 일부 발췌"}

`find_next_target`은 `excluded`에 든 KO를 건너뛰고 다음 우선순위의 글을 돌려준다. 그래서 루프는 잠긴 글을 하나씩 빼 가며 잡을 수 있는 첫 글에서 멈추고, 후보가 다 잠겨 있으면 `target`이 `None`이 되어 그 틱에는 할 일이 없다고 기록한다. 락 때문에 쉬는 것은 모든 후보가 잠겨 있을 때뿐이다.

용어 추출 워커가 잡는 것은 KO 한 편이다. 한글 수정 후속 워커는 요청마다 KO·EN 짝을 잡고, 못 잡으면 그 요청을 다음 틱으로 넘긴다. 분류기도 잠긴 짝은 건너뛰고 다음 짝을 본다. 락을 잡은 뒤에는 사용자가 편집 중인(dirty) 짝과 백오프 중인 짝을 같은 방식으로 건너뛴다.

기다리는 쪽도 있다. 섹션 앵커 게이트는 번역이나 폴리싱이 끝난 뒤 그 글을 인용하는 다른 EN 글의 섹션 앵커와 `§제목`을 고친다. 남의 글이라 최대 900초를 기다리고, 그래도 못 잡으면 그 글을 미룬 목록에 남긴다. 락을 잡은 뒤에는 파일을 다시 읽고 나서야 고칠 내용을 계산한다. 락 없이 먼저 훑는 읽기는 후보를 거르는 데만 쓴다.

## 글 락 바깥의 git·state·원장 락

이 락이 지키는 것은 글 파일뿐이다. git 커밋은 autopush 락(`/tmp/blog-autopush.lock`)이, 워커의 state 파일은 각자의 짧은 락이 지킨다. 번역 워커와 용어 워커는 틱 중복을 막는 자기 전역 락도 그대로 둔다. 긴 모델 호출 동안 git 락을 쥐고 있으면 서로 다른 글을 다루는 워커끼리도 줄을 서야 하므로, 글 락과 git 락을 섞지 않는 것이 이 구조의 전제다. 서비스 맵의 `blog-content-file-lock` 계약에 이 구분이 적혀 있다. flock은 권고 락이라 사용자의 편집기는 이것을 모른다. 그래서 워커들의 dirty 사전 검사와 모델 호출 뒤 원문 재검사는 락과 별개로 남아 있다.

이 모듈을 들인 커밋에서 분류기는 번역 워커·용어 워커의 락을 확인하던 코드와 자기 전역 락을 걷고, 슬롯 락 네 개 중 빈 것을 잡아 같은 크론 시각에 최대 네 프로세스로 뜬다. 두 프로세스가 같은 짝을 고르면 뒤에 온 쪽이 글 락에서 비켜 가므로, 여럿이 동시에 돌아도 같은 글을 쓰지 않는다. 9월 25일에 링크 관계가 글 IAL에서 원장 파일 하나(`_data/link_relations.yml`)로 옮겨 가면 그 슬롯은 걷히고, 분류기는 다시 한 번에 하나만 돈다. 판정마다 같은 원장을 고쳐 커밋하게 되므로, 그 뒤의 틱은 원장 락이나 자기 틱 락을 쥐고 돌며 잡혀 있으면 그 틱을 쉰다. 글 락은 분류기와 다른 워커 사이의 경계로 남는다.

워커들은 이제 서로가 돌고 있다는 이유로 쉬지 않고, 같은 글을 만질 때만 비켜 간다. 줄 서는 법을 배운 크론 워커들이 사람보다 예의 바르다는 생각이 잠깐 들었지만, 그들은 한 번 락을 못 잡으면 미련 없이 다음 글로 넘어갈 뿐이다.
