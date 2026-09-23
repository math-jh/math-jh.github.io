---

title: "워커끼리 글 단위로 비켜 가기"
excerpt: "서로가 돌고 있으면 틱을 통째로 건너뛰던 크론 워커들을, 같은 글을 만질 때만 비켜 가는 글 단위 flock으로 바꾸고 의존성 분류기를 네 슬롯으로 병렬화한 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/blog_file_lock

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-10
last_modified_at: 2026-09-23
weight: 55

---

관련 파일: [`scripts/lib/blog_file_lock.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/lib/blog_file_lock.py), [`scripts/dependency-classifier/dependency_classifier.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/dependency_classifier.py), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/term-extraction/term_extract_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/term_extract_worker.py)
{: .notice--info}

이 Pi에서 글 본문을 고치는 크론 워커는 셋이다. 번역 워커가 EN을 쓰고, 용어 추출 워커가 KO에 한영 병기를 넣고, 의존성 분류기가 링크 IAL에 `data-relation`을 단다. 세 워커가 같은 파일을 동시에 쓰면 뒤에 쓴 쪽이 앞의 결과를 덮는다. 그래서 원래는 서로를 피했는데, 피하는 단위가 **워커 전체**였다.

## 틱을 통째로 버리던 상호 배제

`1eb104d7` 이전의 분류기는 시작하자마자 번역 워커와 용어 워커의 PID 락을 확인했다.

```python
if not acquire_pid_lock(TRANSLATE_LOCK):
    log("translation/follow-up worker is running; skip")
    return 0
term_fh = open(TERM_LOCK, "w")
...
    fcntl.flock(term_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py (1eb104d7^)"}

번역 워커가 Classifying Spaces 한 편을 폴리싱하는 20분 동안, 분류기는 Group Actions의 링크를 분류할 수 있는데도 틱을 버렸다. 번역 워커는 4시간마다 20분 안팎을 돌고 용어 워커도 30분마다 돈다. 분류기가 30분 간격으로 깨어날 때마다 둘 중 하나와 겹치면 그 틱은 헛돈다. 백로그 수백 편을 소화하던 시기에는 이 헛돈 틱이 곧 밀린 일정이었다.

## 경로마다 하나씩 잡는 flock

`scripts/lib/blog_file_lock.py`는 잠그는 단위를 파일로 내렸다. 락 파일은 `/tmp/blog-file-locks/` 아래 **절대경로의 SHA-256** 이름으로 만들고, 여러 파일은 한 번에 잡는다.

```python
def _canonical(paths):
    # All callers acquire in the same order, so a future blocking caller cannot
    # introduce an AB/BA deadlock.  resolve(strict=False) also gives prospective
    # translation output paths a stable identity before the EN file exists.
    return tuple(sorted({Path(p).resolve(strict=False) for p in paths}, key=str))

def try_acquire_file_locks(paths, *, lock_dir=LOCK_DIR):
    canonical = _canonical(paths)
    fds = []
    try:
        for path in canonical:
            name = hashlib.sha256(str(path).encode("utf-8")).hexdigest() + ".lock"
            fd = os.open(lock_dir / name, os.O_CREAT | os.O_RDWR, 0o664)
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            fds.append(fd)
        return FileLockSet(fds=fds, paths=canonical)
    except OSError:
        while fds:
            os.close(fds.pop())
        return None
```
{: data-filename="scripts/lib/blog_file_lock.py"}

설계의 요점은 세 가지다.

- **전부 아니면 전무.** 번역 워커는 KO와 EN을 짝으로 잠근다. 하나만 잡고 나머지를 기다리면, 다른 워커가 반대 순서로 같은 짝을 잡을 때 서로를 기다리게 된다. 여기서는 하나라도 실패하면 앞서 잡은 것까지 즉시 풀고 `None`을 돌려준다. 호출자는 그 글을 건너뛰고 다음 글로 간다.
- **정렬된 획득 순서.** 지금 호출자는 전부 non-blocking이지만, 나중에 기다리는 호출자가 생겨도 AB/BA 교착이 생기지 않게 모든 호출자가 절대경로 정렬 순으로 잡는다. 기다리는 쪽이 필요한 곳(섹션 앵커 게이트의 사후 수리)은 `acquire_file_locks(paths, wait_sec=900)`로 부분 집합을 쥔 채 기다리지 않고 전체 시도를 반복한다.
- **아직 없는 파일도 이름이 있다.** EN 번역은 처음 쓸 때 파일이 없다. `resolve(strict=False)`로 정규화하면 존재하지 않는 경로도 같은 락 이름을 받으므로, "EN을 새로 쓰려는 번역 워커"와 "그 EN을 막 만들어진 참에 읽으려는 분류기"가 같은 락에서 만난다.

락 파일은 지우지 않는다. 빈 파일은 만남의 장소일 뿐이고, 디스크립터를 닫으면 flock이 풀린다. 지우는 순간 이미 그 inode를 쥔 프로세스와 새로 만든 파일을 잡은 프로세스가 서로를 못 보게 된다.

이 락이 지키는 것은 글 파일뿐이다. git 커밋은 여전히 autopush 락이, 워커의 자체 state 파일은 각자의 짧은 락이 지킨다. 긴 모델 호출 동안 git 락을 쥐고 있으면 서로 다른 글을 다루는 워커끼리도 줄을 서야 하므로, 글 락과 git 락을 섞지 않는 것이 이 구조의 전제다. 서비스 맵의 `blog-content-file-lock` 계약에 이 구분이 적혀 있다.

## 네 슬롯으로 도는 분류기

글 단위로 비켜 갈 수 있게 되자 분류기는 같은 크론 시각에 여러 프로세스로 뜰 수 있게 됐다. 전역 PID 락을 걷고, 비싼 모델 호출을 네 개로 제한하는 슬롯 락을 두었다.

```python
SLOT_PATHS = tuple(Path(f"/tmp/dependency-classifier-slot-{i}.lock") for i in range(4))

def acquire_slot():
    """Cap expensive classifier model calls at four concurrent processes."""
    for path in SLOT_PATHS:
        lock_fh = open(path, "w")
        try:
            fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return lock_fh
        except OSError:
            lock_fh.close()
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py (1eb104d7)"}

슬롯을 얻은 프로세스는 큐에서 **잠글 수 있는** 첫 글 짝을 고른다. 다른 프로세스가 쥔 글, 사용자가 편집 중인(dirty) 글, 백오프 중인 글은 건너뛴다. 큐가 비었다는 로그 문구도 그에 맞춰 "queue empty (or every pending target is locked/dirty/backed off)"로 바뀌었다. 분류기의 state 파일은 프로세스 넷이 같이 쓰므로, 저장할 때는 짧은 state 락을 잡고 디스크의 최신본을 다시 읽어 **자기 유닛의 결과만** 병합한다(`merge_unit_states`). 통째로 덮으면 먼저 끝난 프로세스의 결과를 나중 프로세스가 지운다.

배포 순간의 겹침도 하나 챙겼다. 새 코드가 올라가는 시점에 옛 코드의 분류기가 아직 돌고 있으면, 옛 코드는 파일 락을 모른다. 그래서 새 코드는 옛 전역 락 파일(`/tmp/dependency-classifier.lock`)이 잡혀 있으면 그 틱을 쉰다. 옛 프로세스가 사라지면 이 검사는 늘 통과하므로 무해하다.

백로그를 소화하는 동안 분류기는 2분 간격으로 깨어나 최대 넷이 동시에 돌았다. 백로그가 끝난 뒤 사용자가 한 시간에 두 번(`:30`, `:45`)으로 되돌렸다. 슬롯은 그 뒤 Codex 백엔드가 붙으면서 여섯으로 늘었고, 그 안에서 제공자별 상한(Antigravity 4, Claude Opus 4, Codex 6)이 따로 걸린다. 여섯 개의 근거는 코드 주석에 남아 있다. Codex는 동시 8개 시험을 통과했고, 여섯은 사용자가 IDE에서 쓸 몫을 남긴 값이다.

## 같은 락을 쓰는 곳들

번역 워커(KO·EN 짝), 한글 수정 후속 워커(짝), 용어 추출 워커(KO 한 편), 섹션 앵커 게이트(형제 글 수리), EN 마커 회수 스윕, 그리고 대시보드 서버의 링크 판정 버튼이 전부 이 모듈을 부른다. 대시보드가 끼어 있는 이유는 판정 버튼이 서버에서 직접 글 파일의 IAL을 고치기 때문이다. 사람이 누른 버튼도 워커 하나로 친다.

모듈 하나에 89줄, 테스트 52줄이다. 워커들은 이제 서로가 돌고 있다는 이유로 쉬지 않고, 같은 글을 만질 때만 비켜 간다. 줄 서는 법을 배운 크론 워커들이 사람보다 예의 바르다는 생각이 잠깐 들었지만, 그들은 한 번 락을 못 잡으면 미련 없이 다음 글로 넘어갈 뿐이다.
