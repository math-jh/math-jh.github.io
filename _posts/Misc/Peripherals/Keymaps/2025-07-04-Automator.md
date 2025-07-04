---

title: "Apple Automator"
excerpt: ""

categories: [Misc / Peripherals]
permalink: /ko/misc/peripherals/keymaps/automator
header:
    overlay_image: 
    overlay_filter: 0.5
toc: false
date: 2025-07-04
last_modified_at: 2025-07-04
weight: 102

---

`Apple Automator`, 더 정확히는 그 안에 있는 `Applescript`는 많은 것을 할 수 있는 도구다. 나도 이에 대해서는 전문가는 아니라 간단히만 소개하도록 한다. 

`Automator`는 맥에 기본으로 설치되어 있다. 이를 실행하면 다음과 같은 창이 뜬다. 

![automator](/assets/images/Misc/Peripherals/Automator-1.png){:style="width:90%" .align-center}

그럼 빠른동작을 선택하고 코딩을 하면 된다. 이 글에서 설명할 것은 내가 사용하는 빠른동작들인 `Caffeinate`, `Jekyll`, 그리고 `New_document`이다. 마지막 빠른동작의 경우 나도 구글링해서 얻은 것을 그대로 쓰고 있어서 별도로 설명은 하지 않는다. 

## Caffeinate

기본적으로 맥은 아무 활동이 없이 일정 시간이 지나면 절전모드로 들어가게 되어있다. 터미널에서 실행하는 `caffeiate` 명령은 맥에게 계속 일을 시켜서 잠들지 못하게 하는 것이다. 터미널에서 매뉴얼을 찾아보면 다음과 같이 잘 설명이 되어있다. 

```
CAFFEINATE(8)               System Manager's Manual              CAFFEINATE(8)

NAME
     caffeinate – prevent the system from sleeping on behalf of a utility

SYNOPSIS
     caffeinate [-disu] [-t timeout] [-w pid] [utility arguments...]

DESCRIPTION
     caffeinate creates assertions to alter system sleep behavior.  If no
     assertion flags are specified, caffeinate creates an assertion to prevent
     idle sleep.  If a utility is specified, caffeinate creates the assertions
     on the utility's behalf, and those assertions will persist for the
     duration of the utility's execution. Otherwise, caffeinate creates the
     assertions directly, and those assertions will persist until caffeinate
     exits.

     Available options:

     -d      Create an assertion to prevent the display from sleeping.

     -i      Create an assertion to prevent the system from idle sleeping.

     -m      Create an assertion to prevent the disk from idle sleeping.

     -s      Create an assertion to prevent the system from sleeping. This
             assertion is valid only when system is running on AC power.

     -u      Create an assertion to declare that user is active. If the
             display is off, this option turns the display on and prevents the
             display from going into idle sleep. If a timeout is not specified
             with '-t' option, then this assertion is taken with a default of
             5 second timeout.

     -t      Specifies the timeout value in seconds for which this assertion
             has to be valid. The assertion is dropped after the specified
             timeout. Timeout value is not used when an utility is invoked
             with this command.

     -w      Waits for the process with the specified pid to exit. Once the
             the process exits, the assertion is also released.  This option
             is ignored when used with utility option.

EXAMPLE
     caffeinate -i make
        caffeinate forks a process, execs "make" in it, and holds an assertion
     that prevents idle sleep as long as that process is running.

SEE ALSO
     pmset(1)

LOCATION
     /usr/bin/caffeinate

Darwin                         November 9, 2012                         Darwin
```

우리가 원하는 빠른동작은 `Caffeinate -d`가 작동중이라면 작동을 중지시키고, 그렇지 않다면 `caffeinate -d` 명령어를 실행시키는 것이다. 또, 이렇게만 두면 지금 이 명령어가 실행중인지 아닌지를 알기 어려우므로 이 빠른동작을 실행할 때마다 알림을 띄워주도록 한다.

이를 위해 좌측에 있는 항목들 중 *셸 스크립트 실행*을 누른 후 그 안에 다음을 붙여넣는다. 

```bash
( pgrep caffeinate && pkill caffeinate && osascript -e 'display notification "Caffeinate disabled" with title "Caffeinate"' || ( caffeinate -d -i & osascript -e 'display notification "Caffeinate enabled" with title "Caffeinate"'))
```

뜯어보면, 우선 `pgrep caffeinate`를 통해 현재 실행중인 `caffeinate`프로세스가 있는지 찾아본다. 만일 이것이 성공한다면 (`&&`) 이 프로세스를 죽이고 (`pkill caffeinate`) caffeinate 프로세스가 종료되었다는 알림을 띄운다 (`osascript`) 그렇지 않다면 `caffeinate` 프로세스를 시작하고 그에 해당하는 알림을 띄운다. (`caffeinate`명령의 특성상 여기에는 `&&`이 아니라 `&`를 사용해야 하는 것이 자명하다. )

## Jekyll

말 그대로 블로그 글을 쓸 수 있게 세팅해주는 빠른동작이다. 마찬가지로 좌측에 있는 항목들 중 *셸 스크립트 실행*을 누른 후 그 안에 다음을 붙여넣는다. (물론 폴더 위치 등등은 바꿔주어야 할 것이다.)

```bash
( pgrep .site && pkill .site && osascript -e 'display notification "Livereload disconnected" with title "Jekyll"' || (source /Users/junhyeok/.zshrc; cd /Users/junhyeok/GitHub/math-jh.github.io/; open _posts/Math/; LANG="en_US.UTF-8" LC_ALL="en_US.UTF-8" bundle exec jekyll s --livereload --unpublished --destination="/Users/junhyeok/.site" & cd /Users/junhyeok/GitHub/math-jh.github.io/assets/Diagrams; open . & cd /Users/junhyeok/GitHub/math-jh.github.io/assets/images/Math; open . & open -n /Applications/Sublime\ Text.app & sleep 10s; open -na "Vivaldi" --args --new-window --profile-directory="Profile 5" --disk-cache-size=1 "http://localhost:4000/" & cd /Users/junhyeok/Documents/Files/Quiver; python3 -m http.server & open -na "Vivaldi" --args --new-window --profile-directory="Profile 5" --disk-cache-size=1 "http://localhost:8000/src"& sleep 1s; osascript -e 'display notification "Livereload connected" with title "Jekyll"' ))
```

아까와 마찬가지로 만일 `Jekyll`이 실행중이라면 (정확히는 `Jekyll`이 생성하는 `.site`의 내용이 로컬에 띄워져있을 경우) 이를 끄고, 그렇지 않다면 블로그 파일이 있는 폴더로 들어가 `Jekyll`을 실행하고, 필요한 폴더들과 `Sublime Text`를 실행한 후, 잠시 기다렸다가 블로그용 프로필로 브라우저를 실행하여 블로그 주소로 들어가는 것이다. 그 다음의 `python3 -m http.server` 부분은 오프라인에서도 [Quiver](https://q.uiver.app)를 사용할 수 있도록 로컬에서 띄워주는 것이다. 여기서 `--disk-cache-size=1`로 둔 이유는 LiveReload에서 이미지를 캐시하는 것을 방지하여, 이미지 파일이 바뀔 경우 즉각적으로 그 변화가 보이도록 하기 위한 것이다.

## New documents

이 빠른동작은 위의 두 개와 달리 내가 만든 게 아니라 딱히 설명할 것이 없다. 이번에는 좌측에 있는 항목들 중 *AppleScript 실행*을 누른 후 그 안에 다음을 붙여넣는다. 

```bash
try
  tell application "Finder" to set the this_folder ¬
   to (folder of the front window) as alias
on error -- no open folder windows
  set the this_folder to path to desktop folder as alias
end try

set thefilename to text returned of (display dialog ¬
 "Create file named:" default answer "filename.txt")
set thefullpath to POSIX path of this_folder & thefilename
do shell script "touch \"" & thefullpath & "\""
```

## 단축키 설정

위와 같이 빠른동작을 만들었다면 이 파일은 라이브러리 내의 `Services` 폴더에 저장된다. 이제 설정의 키보드로 가서, 키보드 단축키를 연 후 서비스 항목으로 가면 방금 만든 빠른동작들이 보이므로, 새로운 단축키를 지정해주면 된다. 

![shortcuts](/assets/images/Misc/Peripherals/Automator-2.png){:style="width:90%" .align-center}