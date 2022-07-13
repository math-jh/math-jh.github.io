---

title: "맨 위로 버튼 만들기"
excerpt: "맨 위로 버튼 만들기, 숨기기"

lang: ko

categories: [Blog development]
permalink: /blog_dev/back_to_top

sidebar: 
    nav: "dev"

date: 2022-07-10
last_modified_at: 2022-07-10
weight: 9

---

## 목표

포스팅을 하다보니 한 포스트의 길이가 과도하게 길어지는 일이 종종 발생했다. 때문에 맨 위로 버튼을 만들고 싶어서 구글링을 하였고, [이 글](https://masunii.github.io/blog_custom/top_button/)에서 방법을 알게 되었다.

## 맨 위로 버튼 만들기

우선은 링크 걸어둔 글과 같이, `_sass/minimal-mistakes/_sidebar.scss`로 들어가서 다음의 코드를 추가한다.

```scss
.sidebar__top {
  position: fixed;
  bottom: 1.5em;
  right: 2em;
  z-index: 10;
}
```

그리고 `_layouts/default.html`에 가서, 맨 밑에 있는 `<div id="footer" class="page__footer">`의 안쪽에 다음 코드를 삽입한다.
```html
<aside class="sidebar__top">
    <div style="text-align: center; width: 50px">
        <a href="#site-nav" class="top_button"> <i class="material-icons" style="color: #a9874a">&#xE5D8;</i></a>
    </div>
</aside>
```

## 읽은 퍼센트 표시하기

나는 여기에 더해, 맨 위로 버튼 밑에 읽은 정도를 나타내는 퍼센트 표시가 있기를 바랐다. 다만 카테고리들을 모아둔 페이지 등등에서는 퍼센트가 표시될 필요가 없다고 판단하였다. 이를 위해, 위에서 얻은 코드를 다음과 같이 수정했다.
```html
<aside class="sidebar__top">
    <div style="text-align: center; width: 50px">
        <a href="#site-nav" class="top_button"> <i class="material-icons" style="color: #a9874a">&#xE5D8;</i></a>
        {% if page.id %}
            <p style="font-size:12px; color: #a9874a; font-family: sans-serif"><span id="percent">0</span>%</p>
        {% endif %}
    </div>
</aside>
```
이후 Javascript를 통해 스크롤이 일어날 때마다 얼마나 읽었는지를 계산하고, 이 값을 바탕으로 `<span>` 안에 있는 숫자를 바꿔준다. 이 스크립트는 `_includes/scripts.html`에 저장하였다.
```html
<script language="javascript">
  const percentLabel = document.querySelector("#percent");
  const originalTitle = document.title;
  window.addEventListener("scroll", () => {
    let scrollTop = window.scrollY;
    let docHeight = document.body.offsetHeight;
    let winHeight = window.innerHeight;
    let scrollPercent = scrollTop / (docHeight - winHeight);
    let scrollPercentRounded = Math.round(scrollPercent * 100);
    percentLabel.innerHTML = scrollPercentRounded;
  });
</script>
```

## 맨 위로 버튼 숨기기

마지막으로 일정 시간동안 마우스의 움직임이 없으면 맨 위로 버튼을 자동으로 숨기기 위해 다음의 Javascipt 파일을 `assets/js/custom` 아래에 추가했다. 이 코드는 stack overflow의 [질문글](https://stackoverflow.com/questions/41021611/how-to-show-divs-when-the-mouse-moves-anywhere-on-screen-not-just-the-element-i)에서 가져왔다.
```javascript
$(function(){
  // When page loads, wait 3 seconds and hide all elements with .top_button class:
  setTimeout(toggle, 3000);
});

var timer = null;

// General function for adding/removing the "hide" class.
// This is used when the page first loads and each time
// the mouse moves on the page. We're not calling toggle()
// here because a flicker effect can happen which would leave
// the elements showing instead of being hidden.
function toggle(){
  $('.top_button').toggleClass('hide');
}

$(window).on('mousemove', function(){
  // When anywhere on page is moused over bring back .top_button
  // elements for 3 seconds. Removing "hide" simply restores
  // the original CSS & layout
  $('.top_button').removeClass('hide');
  
  // Kill any previous timers
  clearTimeout(timer);
  
  // Wait 3 seconds and hide again
  timer = setTimeout(toggle, 3000)
});
```
그리고 맨 위에서 `_sidebar.scss` 파일에 추가한 코드 바로 밑에 다음 코드를 추가한다.
```scss
.top_button { opacity: 1;
  transition: opacity 0.5s ease-in-out; }
.hide {opacity: 0.1; }
```
위의 스크립트는 주석에도 설명되어 있듯, 3초를 기다리면 `.top_button` 버튼에 `hide`클래스를 추가하여 `.top_button hide`를 만들고, 따라서 맨 위로 버튼이 `opacity:0.1` 속성을 갖게 된다. 만약 마우스 움직임이 감지되면 다시 `hide` 클래스가 사라져서 맨 위로 버튼에서 `opacity:0.1` 속성이 사라지고 따라서 다시 보이게 된다. 

위의 Javascript를 구동시키기 위해서는 jQuery가 필요하다. 또, 위의 스크립트 또한 불러와야 하므로, 이 두 파일을 `_config.yml`에서 불러와야 한다. jQuery의 경우, `/assets/js/vendor/jquery/` 내에 `jquery-3.6.0.js`가 들어있지만 `_config.yml`의 `# Reading Files`에서 `exclude: assets/js/vendor`를 통해 해당 디렉터리를 무시하도록 되어있어 이를 불러오는 것이 불가능하다. 

나는 우선 jQuery [사이트](https://jquery.com/download/)에서 `jquery-3.6.0.min.js`를 받아 `/assets/js/vendor/jquery-min` 아래에 저장하고, `_config.yml`의 해당 부분을
```yml
# Reading Files
include: 
  ...
exclude: 
  ...
  -assets/js/vendor/jquery/jquery-3.6.0.js
```
로 바꾸어 내가 저장한 `jquery-3.6.0.min.js`는 문제없이 `head_scripts`에서 불러올 수 있도록 했다. 

마지막으로 `_config.yml` 파일의 맨 밑에 다음의 코드
```yml
head_scripts:
  - /assets/js/vendor/jquery-min/jquery-3.6.0.min.js
  - /assets/js/custom/HiddenTopButton.js
```
를 추가하여, 사이트가 로드될 때 이 두 javascript가 같이 로드되도록 설정해준다.

이렇게 하면 jQuery가 `head_scripts`에서 한 번, `main.min.js`에서 다시 한 번 불러져서 쓸데없이 두 번 불러진다는 문제가 있지만 `minimal-mistakes`의 어떤 부분에서 jQuery가 필요한지를 모두 아는 게 아니다보니 이 방법이 가장 안전하다고 생각했다.