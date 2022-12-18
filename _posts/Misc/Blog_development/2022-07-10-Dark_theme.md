---

title: "Minimal mistakes 테마 다크모드 추가하기"
excerpt: "다크모드 추가"

read_time: false

categories: [Blog Development]
permalink: /ko/blog_dev/dark_theme

sidebar: 
    nav: "dev"
    
date: 2022-07-10
last_modified_at: 2022-07-10
weight: 10

---

관련 커밋: [링크](https://github.com/math-jh/math-jh.github.io/commit/dcf3036a834a9bb235604c7ea2ca8b8754cd06d3)
{: .notice--info}

## 다크모드 설정하기

나는 보통 밤에 블로그를 관리하므로, 블로그의 전반적인 테마가 어두웠으면 하는 바람이 있었다. 물론 단순히 어두운 테마를 사용해도 되는 일이긴 하지만, 그보다는 다크모드를 사용하고 싶었다. [이 글](https://etch-cure.github.io/blog/toggle-dark-mode/)에서 방법을 찾았다.

우선 `_config.yml` 파일에서 다음과 같이 다크모드를 사용할 것임을 알린다. 또, 어떤 스킨을 다크모드로 사용할지를 알려줘야 한다. 나는 새로 `custom-dark.scss` 파일을 추가했다.
```yml
dark_theme                : true
dark_skin                 : "custom-dark"
```
그리고 `assets/css/` 디렉터리로 들어가, 다음과 같이 `main_dark.scss`를 추가한다.
```scss
---
# Only the main Sass file needs front matter (the dashes are enough)
---

@charset "utf-8";

@import "minimal-mistakes/skins/{{ site.dark_skin | default: 'default' }}"; // skin
@import "minimal-mistakes"; // main partials

```
그 후 `_includes/head.html`로 들어가서, 위에서 지정한 `dark_theme`이 참이라면 방금 만든 `main_dark.scss`를 로드하도록 한다.
{% raw %}
```html
{% if site.dark_theme %}
  <link rel="stylesheet" href="/assets/css/main_dark.css">
{% endif %}
```
{% endraw %}

그리고 `_layouts/default.html`의 `<head>` 태그 내부에 다음의 코드를 붙여넣는다.
```html
<style>
    .switch input[type="checkbox"],
    .switch .checked {
        display: none;
    }
    .switch input[type="checkbox"]:checked ~ .checked
    {
        display: inline-block;
    }
    .switch input[type="checkbox"]:checked ~ .unchecked
    {
        display: none;
    }
    label[for="toggle_dark_theme"] {
        position: relative;
        top: .15em;
    }
    .vl {
        border-left: 2px solid white;
        height: 1em;
    }
</style>
```
마지막으로 `_includes/masthead.html`에서 `<a class="site-title">`과 `<ul class="visible-links">` 사이에 다음 코드를 넣어준다.
{% raw %}
```html
{% if site.dark_theme %}
<div style="margin-left: 5px; border: 2px solid #555; border-radius:10px; background-color:#222">
    <label class="switch" for="toggle_dark_theme" style="color:#bbb; font-size:1em; display:inline; margin-left:5px; margin-right:5px">
        <input type="checkbox" id="toggle_dark_theme" onclick="scrollbar()"/>
        <span class="material-icons md-16 unchecked" style="color:#ffbb9a">&#xE518;</span>
        <span class="material-icons md-16 checked" style="color:#ffeabc">&#xE51C;</span>
    </label>
</div>
{% endif %}
```
{% endraw %}
그럼 masthead에 버튼이 추가되었을 것이며, 이 버튼은 누를 때마다 해와 달이 번갈아 나온다. 하지만 아직 이 버튼의 행동을 지정하지 않았기 때문에 유의미한 변화는 어떤 것도 일어나지 않는다.
`assets/js/custom` 폴더에 (물론 `_config.yml`에서 제대로 불러오기만 한다면 어디에 놓든 상관은 없다) 다음의 Javascript
```javascript
    function darkmode(){

    var defaultTheme = [...document.styleSheets].find(style => /(main.css)$/.test(style.href))
    var darkTheme = [...document.styleSheets].find(style => /(main_dark.css)$/.test(style.href))

    if (darkTheme) {
        const darkModeCookie = document.cookie
            .split('; ')
            .find(co => co.startsWith('MDARK='))
        if (darkModeCookie !== undefined) {
            const dmodeValue = darkModeCookie.split('=')[1]
            darkTheme.disabled = dmodeValue !== 'Y'
            defaultTheme.disabled = dmodeValue === 'Y'
        } else {
            if (matchMedia('(prefers-color-scheme: dark)').matches) {
                darkTheme.disabled = false
                defaultTheme.disabled = true
            } else {
                darkTheme.disabled = true
                defaultTheme.disabled = false
            }
            document.cookie = `MDARK=${darkTheme.disabled ? 'N' : 'Y'}; path=/;`
        }

        let toggleThemeBtn = document.getElementById("toggle_dark_theme")
        if (toggleThemeBtn) {
            toggleThemeBtn.checked = defaultTheme.disabled
        }

        let changeTheme = () => {
            darkTheme.disabled = !darkTheme.disabled
            defaultTheme.disabled = !darkTheme.disabled
            document.cookie = `MDARK=${darkTheme.disabled ? 'N' : 'Y'}; path=/;`
        }

        toggleThemeBtn.addEventListener('click', changeTheme)
    }
    }
```
를 넣는다. 그 후 `_layouts/default.html` 파일의 `<body class="layout-- ...">` 태그에 속성 `onload="darkmode()"`를 추가해주고, `_config.yml`의 항목 `head_scripts:`에 방금 만든 `js`파일을 추가해준다.

여기까지 완료하면 다크모드와 라이트모드를 왔다갔다 할 수 있게 되었다. 또, 처음 접속했을 때의 시스템 환경설정에 맞춰 다크모드인지 아닌지가 결정된다. 

## 모양 다듬기

위 글에서 소개한 다크모드는 아주 잘 작동했지만, 몇 가지 모양을 다듬을 것이 있었다.

우선 나는 라이트 모드일 때에도 배경이 완전한 하얀색이 아니라 대다수의 그림들 (주로 diagram들)이 배경이 지워진 상태의, 검은 색이었는데 이런 그림은 다크모드로 전환하였을 때 거의 보이지 않는다는 문제가 있었다.

![octahedral axiom](/assets/images/Octahedral.png){:width="500px" .align-center}

때문에 다크모드에서는 이런 그림들에 색상을 반전시켜줄 필요가 있어서, 이들 그림에 `invert` 클래스를 추가해준 후, `_main-dark.scss` 파일의 말미에 다음의 코드
```scss
img.invert {
  filter: invert(1);
}
```
를 추가해주었다. 

![octahedral axiom](/assets/images/Octahedral.png){:width="500px" class="invert" .align-center}

잘 작동하는 것 같다. `invert` 태그를 `_inculdes/author-profiles.html`에서도 추가해주었다. 

또, 인라인 코드 블럭이 지난번부터 마음에 들지 않았는데, 다크모드에서의 인라인 코드 블럭 색상을 바꾸는 것보다 이들 태그를 `_sass/minimal-mistakes/_pages.scss`에서 수정하는 것이 좋아보였다.
```scss
  :not(pre) > code {
    padding-top: 0.1rem;
    padding-bottom: 0.1rem;
    font-size: 0.8em;
    background: $code-background-color;
    border-radius: $border-radius;

    &::before,
    &::after {
      letter-spacing: -0.2em;
      content: "\00a0"; /* non-breaking space*/
    }
  }
```
이렇게 되어 있던 코드를
```scss
  :not(pre) > code {
    padding-top: 0.1rem;
    padding-bottom: 0.1rem;
    font-size: 0.8em;
    background: mix($background-color, $text-color, 90%);
    border-radius: $border-radius;
    color: $text-color;

    &::before,
    &::after {
      letter-spacing: -0.2em;
      content: "\00a0"; /* non-breaking space*/
    }
  }
```
이렇게 수정했다. 

## 스크롤바 꾸미기

마지막으로 스크롤바를 예쁘게 꾸미고 싶었다. 또, 이 스크롤바가 사이트가 라이트 모드인지, 다크 모드인지에 따라 달라지도록 만들려고 하였다.

우선 아까 `_layouts/default.html`의 `<head>` 태그 안에 넣은 `<style>` 태그에 
```css
body::-webkit-scrollbar{width: 16px;}
body::-webkit-scrollbar-track {background-color:#071734;}
body::-webkit-scrollbar-thumb:hover {background: #a9874a; background-clip: padding-box; border: 2px solid transparent}
```
를 추가한다. 또, 좌측 사이드바와 페이지 목차 또한 간혹 스크롤바가 생길 정도로 길어질 때가 있어서, 약간의 시행착오 끝에 다음을 추가하면 된다는 것을 알아냈다.
```css
.sidebar.sticky::-webkit-scrollbar{width: 6px}
.sidebar.sticky::-webkit-scrollbar-track{display: none}
.sidebar.sticky::-webkit-scrollbar-thumb:hover {background: #071734; background-clip: padding-box; border: 1px solid transparent}

.toc__menu::-webkit-scrollbar{width: 6px}
.toc__menu::-webkit-scrollbar-track{display: none}
.toc__menu::-webkit-scrollbar-thumb:hover {background: #071734; background-clip: padding-box; border: 1px solid transparent}
```
의도적으로 `-webkit-scrollbar-thumb`을 비워뒀기 때문에 아직까지는 스크롤바 트랙 위에 스크롤바가 보이지 않는다. 이제 `<style>`태그가 끝난 직후에 `<style>` 태그를 하나 더 만들고, `id`를 `scrollbar-color`로 바꿔준다. 즉 다음 코드를 `</style>` 직후에 추가한다.
```html
<style id="scrollbar-color">

</style>
```
이 태그 안에는 아무것도 없지만, Javascript를 이용하면 사이트가 로드될 때 이 태그 안의 내용물을 color scheme에 맞도록 해줄 수 있다. 다음 js를 `assets/js/custom/` 안에 넣는다.
```javascript
function scrollbar() {
if(document.getElementById("toggle_dark_theme").checked == true)
document.head.querySelector("#scrollbar-color").innerHTML=`
   body::-webkit-scrollbar-thumb {background-color:#455a64; border-radius: 3px; background-clip: padding-box; border:2px solid transparent}
   .sidebar.sticky::-webkit-scrollbar-thumb {background-color:#282828; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
   .toc__menu::-webkit-scrollbar-thumb {background-color:#282828; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
 `
 else
 document.head.querySelector("#scrollbar-color").innerHTML=`
   body::-webkit-scrollbar-thumb {background-color:#cfd8dc; border-radius: 3px; background-clip: padding-box; border:2px solid transparent}
   .sidebar.sticky::-webkit-scrollbar-thumb {background-color:#eaeaf2; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
   .toc__menu::-webkit-scrollbar-thumb {background-color:#eaeaf2; border-radius: 3px; background-clip: padding-box; border:1px solid transparent}
 `
 }
```
이제 `_config.yml`의 headscript에서 이 javascript 또한 불러오고, `_layouts/default.html` 파일의 `<body class="layout-- ...">` 태그에서 `scrollbar()` 또한 불러오도록 하여 속성 `onload="darkmode(), scrollbar()"`으로 지정하면 된다.