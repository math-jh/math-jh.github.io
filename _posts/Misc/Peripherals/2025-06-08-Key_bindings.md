---

title: "키 설정"
excerpt: ""

categories: [Misc / Peripherals]
permalink: /ko/misc/peripherals/keyboards/key_bindings
header:
    overlay_image: /assets/images/Misc/peripherals/Easylink.png
    overlay_filter: 0.5

toc: false
date: 2025-06-08
last_modified_at: 2025-06-08
weight: 9

---

[Easylink 및 VIAL](/ko/misc/peripherals/keyboards/easylink) 글을 쓸 때 까지만해도 내 키보드 설정은 저것이 마지막일 것이라 생각했다. 하지만 역시 최종이라는 것은 존재하지 않는 법. 이 세팅에서 마음에 들지 않는 부분들이 점점 쌓였고 나는 새로운 해결책을 찾게 되었다. 

원래는 실사용을 조금 더 해보고 글을 남기려 했는데, 마침 코로나에 걸리는 바람에 공부하기에는 집중력이 따라주지를 않고, 한글타자를 세벌식으로 바꾼 김에 타자연습도 필요하고... 등등의 이유로 미리 쓰게 되었다. 

## 기존 세팅의 문제점

가장 마음에 안 들었던 부분은 Easylink 커넥터가 기기를 꽤나 가린다는 것이었다. 특정 키보드들에서 잘 작동하지 않다보니 Easylink 모듈에 매크로 등등을 저장해두는 의미가 많이 퇴색되었다. 또, 간혹가다 연결이 간헐적으로 끊기는 문제도 있었다. 그 외에 마음에 들지 않았던 것은 매크로가 고작 16개 뿐이라는 것. 어떻게든 16개의 매크로만 남겨두긴 했으나 솔직히 16개는 결코 많은 숫자는 아니다. 

또, 문제점이라기보단 약간 내 사고방식이 변화된 부분으로, 원래는 컴퓨터에 단축키를 저장해두고 이 단축키를 더 간단한 키로 바꾸어 키보드에 저장하는 것, 가령 `Ctrl+Cmd+Shift+C`에 `Caffeinate` 빠른동작을 할당하고 키보드의 `Fn+C`에 `Ctrl+Cmd+Shift+C`를 할당하는 것을 최대한 피하려 했었다. 이는 입력기기의 역할과 컴퓨터의 역할을 명확히 하려는 나름대로의 시도였는데, 키보드를 쓰다보니 어차피 나만 쓰는 키보드인데 단축키 좀 넣어서 편하게 쓰는 것이 뭐 그리 대수인가 하는 생각이 들었다.

마지막으로, 가장 결정적인 발견(?)은 VIA에서도 `Any` 키를 통해 Mod-Tap 키나 Layer-Tap 키를 넣어줄 수 있다는 것이었다. VIA에서 아쉬운대로 `Space Fn`이라도 써볼까 하고 넣어뵜는데, `LT(2, KC_SPC)`처럼 나오길래 혹시나 싶어서 시도해봤는데 `LT(x, kc)`도, `MT(mod, kc)`도 잘 작동하더라. 

## 과도기적 해결방안

내 기존 세팅은 다음과 같이 진행된다. 

1. 키보드에서 `\+e`를 누른다. 
2. VIA (QMK)는 이를 매크로 키(가령 `M1`키)로 인식하여, 이 매크로에 저장되어 있는대로 `ex`를 눌러준 후, `Tab` 키를 눌러준다. 
3. `Sublime Text`에서 위의 과정이 진행된다면, `ex`가 입력되고 Tab Completion을 통해 `example.sublime-snippet`이 실행된다. 

가장 생각없이 할 수 있는 방법은 위에서 언급한 `Caffeinate` 빠른동작처럼 macOS에서 지원하는 빠른동작을 이용하는 것이다. 이를 위해 `\`에 `MT(MOD_LCTL|MOD_LSFT|MOD_LGUI, KC_BSLS)`를 둔 후 Automator에서 다음의 AppleScipt를 실행하도록 한다. 

```
on run {input, parameters}
	
	tell application "System Events"
		keystroke "ex"
		key code 48
	end tell
	
	return input
end run
```
이를 저장해준 후, macOS 설정의 키보드 단축키에서 이 빠른동작에 대한 단축키를 `Ctrl+Cmd+Shift+E`로 지정하면 된다. 

원래는 Mod-Tap 키의 mod를 `MOD_HYPR`로 하려했는데 `HYPR+,`를 macOS가 이미 시스템 진단 단축키로 쓰고 있었다. 그래서 이를 피하고자 

- `Ctrl+Cmd+Opt+(C,J,N)`은 각각 `Caffeinate`, `Jekyll`, `new_document` 빠른동작,
- `Ctrl+Cmd+Shift+...`이 위와 같은 형태의 빠른동작,
- `Ctrl+Cmd+Shift+Opt+...`또한 위와 같은 형태의 빠른동작

으로 지정해두고, VIAL에서 Tap Dance로 쓰던 기능들(가령 `\+4`를 짧게 누르면 inline math, 길게 누르면 display style의 math)을 `Ctrl+Cmd+Shift+...`와 `Ctrl+Cmd+Shift+Opt+...`로 나누어두었다. 또, `]` 키도 `MT(MOD_LALT, KC_RBRC)`으로 바꾸어주었다. 물론 빠른동작 단축키를 `Ctrl+Cmd+Shift+]+...`로 지정할 수도 있었겠지만 이게 좀 더 체계적(?)인 것 같아서 이렇게 지정했다. 

## Sublime Text의 Key binding 활용

이렇게 쓰다보니 타자가 빨라지면 AppleScript가 실행되는 도중에 그 다음 키가 들어가는 현상이 발생했다. 고민을 하다보니 어차피 Sublime Text에서만 사용할 단축키를 굳이 AppleScript로 global하게 정의할 필요가 없더라. 그래서 Sublime Text의 Key binding을 이용했다. 

```
{
	"keys": ["ctrl+super+shift+e"],
	"command": "insert_snippet",
	"args": {
		"name": "Packages/User/LaTeX/Large_environments/example.sublime-snippet"
	}
} 
```

Key binding은 이런 식으로 해 주면 된다.

한편, LaTeX 문서를 작성할 때는 이 단축키가 

```
\begin{example}

\end{example}
```

을 삽입해줘야 하지만, 마크다운으로 블로그 글을 쓸 때에는

```
<div class="example" markdown="1">

<ins id="ex">**예시 **</ins> 

</div>
```

를 넣어주어야 한다. 이를 위해서는 `context`를 활용하여

```
{
	"keys": ["ctrl+super+shift+e"],
	"command": "insert_snippet",
	"args": {
		"name": "Packages/User/LaTeX/Large_environments/example.sublime-snippet"
	}, 
	"context": [
		{
			"key": "selector", 
			"operator": "equal", 
			"operand": "text.tex.latex"
		}
	]
} 
```

로 LaTeX에서만 `LaTeX/Large_environments/example.sublime-snippet`이 실행되도록 하고, 

```
{
	"keys": ["ctrl+super+shift+e"],
	"command": "insert_snippet",
	"args": {
		"name": "Packages/User/Jekyll/example_ko.sublime-snippet"
	}, 
	"context": [
		{
			"key": "selector", 
			"operator": "equal", 
			"operand": "text.html.markdown"
		}
	]
} 
```

을 통해 마크다운 문서에서는 `Jekyll/example_ko.sublime-snippet`이 실행되도록 하면 된다. 