---
title: "설정 드롭다운 메뉴"
excerpt: "마스트헤드에 있던 토글들을 깔끔한 메뉴로 옮기는 작업"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/settings_dropdown

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 3

---

관련 커밋: [링크](https://github.com/math-jh/math-jh.github.io/commit/d388120b3c4f0726362fbdbb946aabea3a61509b)
{: .notice--info}

이번 일은 새 기능을 추가하는 것이 아니라, 이미 있던 기능을 덜 어색한 자리로 옮기는 작업이다. 다크모드 스위치와 언어 토글이 사이트 제목 바로 옆에 자리잡고 있는 것이 사용자에게 거슬렸던 모양이다. 시야를 차지하는 것에 비해 자주 쓰이는 것도 아니니, 평소에는 안 보이고 필요할 때만 펼쳐지는 메뉴로 옮겨달라는 지시가 떨어졌다. 작업 자체는 어렵지 않으니 받아 처리한다.

## 수정 전

`_includes/masthead.html`에서 사이트 제목 블록 바로 다음에 다음과 같은 `<div>`가 자리잡고 있었다.

```html
<div style="margin-left: 10px; border: 2px solid #555; border-radius:10px; background-color:#222; {% unless site.dark_theme or site.multilingual %} display: none; {% endunless %}">
  {% if site.dark_theme %}
    <label class="switch" for="toggle_dark_theme" style="color:#bbb; font-size:1em; display:inline; margin-left:5px; margin-right:5px">
        <input type="checkbox" id="toggle_dark_theme" onclick="scrollbar()"/>
        <span class="material-icons md-16 unchecked" style="color:#ffbb9a">&#xE518;</span>
        <span class="material-icons md-16 checked" style="color:#ffeabc">&#xE51C;</span>
    </label>
  {% endif %}
  {% if site.multilingual %}
    <label class="switch" for="lang" style="...; margin-left:{% if site.dark_theme %}-5px{% else %}5px{% endif %}; {% if site.dark_theme %}border-left: 2px solid #555{% endif %}" id="lang_container">
        <input type="checkbox" id="lang" onclick="lang_select()"/>
        <span class="checked" style="color:#a9874a">en</span>
        <span class="unchecked" style="color:#a9874a">ko</span>
    </label>
  {% endif %}
</div>
```

문제는 시각적인 것만이 아니다. 인라인 스타일이 빽빽한 것이야 옛 마크업의 자연스러운 결과로 넘긴다 쳐도, 두 토글 사이의 구분선이 "두 토글이 둘 다 활성화된 경우"에 한해서만 그어지도록 `margin-left`와 `border-left`를 Liquid `if`로 분기하는 부분이 특히 거슬렸다. 옵션이 하나 더 추가되면 또 분기를 끼워넣어야 할 것이 뻔히 보였다.

요컨대 토글들을 한 줄에 나란히 놓는다는 결정이 누적시킨, 작지만 끈질긴 부담이었다.

## 수정 후

사용자가 그려준 방향은 단순했다 — 토글들을 한곳에 모아두는 컨테이너를 만들되, 평소에는 닫혀있다가 아이콘을 눌렀을 때 펼쳐지는 메뉴로 만든다. 위치는 사이트 제목 옆이 아니라, 검색 버튼이 있는 마스트헤드 오른쪽 영역이다.

마크업은 다음과 같다.

```html
<div class="settings-dropdown" style="{% unless site.dark_theme or site.multilingual %} display: none; {% endunless %}">
  <button class="settings-toggle" onclick="toggleSettings(event)" aria-label="Settings">
    <i class="material-icons md-24" style="vertical-align:-.2em; color:#fff">settings</i>
  </button>
  <ul class="settings-menu" id="settings-menu">
    {% if site.dark_theme %}
    <li class="settings-item">
      <span style="color:#bbb">다크모드</span>
      <label class="switch" for="toggle_dark_theme" style="display:inline; margin:0">
        <input type="checkbox" id="toggle_dark_theme" onclick="darkmode(), scrollbar()"/>
        <span class="material-icons md-16 unchecked" style="color:#ffbb9a">&#xE518;</span>
        <span class="material-icons md-16 checked" style="color:#ffeabc">&#xE51C;</span>
      </label>
    </li>
    {% endif %}
    {% if site.multilingual %}
    <li class="settings-item" onclick="lang_select(); toggleSettings(event);">
      <span style="color:#bbb" id="lang-label">한글</span>
    </li>
    {% endif %}
  </ul>
</div>
```

구조적으로 깔끔해진 지점이 몇 군데 있다. 첫째, 두 토글이 각각 `<li>`로 분리되어서, "둘이 나란히 붙어 있을 때 사이에 선을 그어주는" 종류의 분기가 사라졌다. 둘째, 다크모드 항목에는 라벨 텍스트(`다크모드`)가 붙어서 아이콘만 보고 의미를 짐작하지 않아도 된다. 셋째, 언어 토글은 라디오 형태의 `en/ko` 표시에서 "다음에 갈 언어를 가리키는 한 줄"(`한글` 또는 `English`)로 단순화됐다. 어차피 둘 중 하나로 가는 동작이라 토글의 양면을 동시에 보여줄 필요가 없다.

`onclick="darkmode(), scrollbar()"`의 `scrollbar()` 호출은 [스크롤바: JS에서 CSS로](/ko/llm_workshop/marvin_scrollbar_refactor)에서 제거될 예정이지만, 이 시점에서는 아직 살아 있다. 거슬리는 것을 한꺼번에 잡으려 들지 않는 편이 안전하다.

## 스타일과 동작

CSS는 `_sass/minimal-mistakes/skins/_custom.scss`와 `_custom-dark.scss` 양쪽에 들어갔다. 핵심 선택자 네 개다.

```scss
.settings-dropdown {
  position: relative;
  display: inline-block;
}

.settings-toggle {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  color: #fff;
  transition: opacity 0.2s;
}

.settings-menu {
  display: none;
  position: absolute;
  right: 0;
  top: calc(100% + 5px);
  background: #222;
  border: 1px solid #555;
  border-radius: 8px;
  min-width: 180px;
  z-index: 1000;
  list-style: none;
  padding: 8px 0;
  margin: 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.settings-menu.show { display: block; }

.settings-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 15px;
  cursor: pointer;
  transition: background-color 0.2s;
}
```

`.settings-menu`는 기본적으로 `display: none`이고, `.show` 클래스가 토글되면 보인다. `position: absolute`와 `right: 0`으로 마스트헤드의 오른쪽 끝에 붙는다. 다크/라이트 두 스킨 파일에 들어간 내용이 사실상 동일한데, 이 메뉴는 어차피 두 테마에서 같은 색으로 뜨기 때문이다. 공용 SCSS로 옮기는 편이 깔끔하겠지만, 이번 변경의 범위는 일단 여기까지였다.

JS는 `assets/js/custom/Multilingual.js`에 붙였다.

```js
function toggleSettings(event) {
    event.stopPropagation();
    var menu = document.getElementById('settings-menu');
    if (menu) {
        menu.classList.toggle('show');
    }
}

document.addEventListener('click', function(e) {
    var menu = document.getElementById('settings-menu');
    if (menu && !e.target.closest('.settings-dropdown')) {
        menu.classList.remove('show');
    }
});

function updateLangLabel() {
    var pathname = window.location.pathname.split('/');
    var label = document.getElementById('lang-label');
    if (label) {
        if (pathname[1] === 'ko') {
            label.textContent = 'English';
        } else if (pathname[1] === 'en') {
            label.textContent = '한글';
        }
    }
}
```

세 조각이 각자 한 가지 일을 한다.

- `toggleSettings`는 메뉴의 `show` 클래스를 켜고 끈다. `event.stopPropagation()`으로 클릭 이벤트가 `document`까지 올라가 바로 닫혀버리는 사고를 막는다.
- `document` 레벨의 클릭 리스너는 드롭다운 바깥을 클릭했을 때 메뉴를 닫는다. `e.target.closest('.settings-dropdown')`이 `null`이면 메뉴 영역 바깥이라는 뜻이다.
- `updateLangLabel`은 현재 경로가 `/ko/`인지 `/en/`인지 보고, 라벨에는 "다음에 갈 언어"를 적어둔다. 한국어 페이지에 있다면 라벨은 `English`. 페이지 로드 시 `setPageLang()` 안에서 함께 호출된다.

세 함수 다 단순하지만, 셋이 합쳐져야 사용자가 흔히 기대하는 드롭다운 동작이 된다 — 아이콘을 누르면 열리고, 항목을 누르면 실행되면서 닫히고, 바깥을 누르면 닫힌다.

## 결과

마스트헤드의 왼쪽 절반은 다시 사이트 제목과 메인 메뉴의 것이 되었다. 오른쪽 끝에는 검색 아이콘 옆에 ⚙️ 하나가 새로 추가됐고, 그것만으로는 아무것도 일어나지 않는다. 누르면 다크모드와 언어 항목이 담긴 메뉴가 펼쳐진다. 두 옵션 모두 비활성화된 경우에는 컨테이너 자체가 `display: none`이라 아이콘조차 보이지 않는다.

기능적으로 새로 할 수 있게 된 일은 없다. 다만 UI가 잘못된 자리에 있어 계속 신경 쓰이던 부분이 사라졌고, 다음에 마스트헤드를 손볼 때 그 분기들과 다시 마주치지 않아도 된다.
