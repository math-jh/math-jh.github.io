---

title: "블로그 커스터마이징"
excerpt: "본문 너비 늘리기, 파비콘 적용, 머티리얼 아이콘 적용"

read_time: false

categories: [Blog development]
permalink: /ko/blog_dev/personalization

sidebar: 
    nav: "dev"
    
date: 2022-07-09
last_modified_at: 2022-07-09
weight: 8

---

관련 커밋: [링크 1](https://github.com/math-jh/math-jh.github.io/commit/52533f6a305698a54de1f74971d733e5e7d59b72), [링크 2](https://github.com/math-jh/math-jh.github.io/commit/78122756009023af2a8016215e1926b198801f08)
{: .notice--info}

Minimal-mistakes 테마의 가장 큰 장점 중 하나는 기본 테마가 깔끔해서 이리저리 수정하기 좋은 것이라 생각한다. 이 글에서는 내 블로그에서 적용된 여러 변경점들을 정리해두었다. 

Minimal-mistakes 테마의 스타일 파일은 `_sass/minimal-mistakes/` 디렉터리에 들어있고, 하위 디렉터리 `_sass/minimal-mistakes/skins`에 스킨이 들어있다. 대충 눈치껏 살펴보면 페이지를 구성할 때 

1. `assets/css/main.scss` 파일이 로드되고, 이 파일이 스킨과 `_sass/minimal-mistakes.scss` 파일을 순차적으로 로드한다.
2. `_sass/minimal-mistakes.scss` 파일에 적혀있는 순서대로 `_sass/minimal-mistakes/`의 `.scss`파일들이 로드된다.

이런 식으로 진행되는 것 같다.

## 하이퍼링크에서 밑줄 없애기

우선 모든 하이퍼링크마다 밑줄이 쳐져 있는 것이 눈에 거슬렸다. 이를 없애기 위해서는 아무 `.scss` 파일에다 `a` 태그에 대한 속성을 추가해주면 되겠지만, 그래도 어느정도 맥락을 맞추기 위해서 `.scss`파일들을 열어본다. `_base.scss`파일에 다음과 같은 코드가 있다.

```scss
/* links */

a {
  &:focus {
    @extend %tab-focus;
  }

  &:visited {
    color: $link-color-visited;
  }

  &:hover {
    color: $link-color-hover;
    outline: 0;
  }
}
```
이 코드에 `text-decoration: none;`을 추가하여 링크마다 밑줄을 치지 않도록 해 준다. 
```scss
/* links */

a {
  text-decoration: none;

  &:focus {
    @extend %tab-focus;
  }

  &:visited {
    color: $link-color-visited;
  }

  &:hover {
    color: $link-color-hover;
    outline: 0;
  }
}
```
원래는 아래 그림과 같이 각 링크마다 밑줄이 적혀있었는데,

![Before_hyperlink](/assets/images/Blog_development/Personalization-1.png){:width="500px" .align-center}

이렇게 코드를 수정하고 나면 다음과 같이 밑줄이 없어진 것을 확인할 수 있다.

![After_hyperlink](/assets/images/Blog_development/Personalization-2.png){:width="500px" .align-center}

## 본문 너비 늘리기

Minimal-mistakes 테마를 처음 보고 가장 마음에 들지 않았던 것은 광활한 화면에 비해 본문영역이 차지하는 너비가 너무 좁다는 것이었다. 이는 `_sass/minimal-mistakes/_variables.scss` 파일의 가장 밑에 있는 

```scss
/*
   Grid
   ========================================================================== */

$right-sidebar-width-narrow: 200px !default;
$right-sidebar-width: 300px !default;
$right-sidebar-width-wide: 400px !default;
```

부분을

```scss
/*
   Grid
   ========================================================================== */

$right-sidebar-width-narrow: 150px !default;
$right-sidebar-width: 200px !default;
$right-sidebar-width-wide: 250px !default;
```

으로 수정해주면 된다. 그럼 위의 그림과 같던 본문의 너비가 

![After_text_width](/assets/images/Blog_development/Personalization-3.png){:width="500px" .align-center}

이와 같이 넓어진 것을 확인할 수 있다.

## 파비콘 추가

파비콘은 웹사이트 옆에 붙는 아이콘이다. 이를 수정하면 github 블로그도 자기만의 아이콘을 갖도록 할 수 있다. [이 글](https://ansohxxn.github.io/blog/favicon/)을 참고했으며, 간단해서 별달리 첨언할 것이 없다. 다만 나는 `assets/favicons/` 밑에 파비콘 파일을 두었기 때문에, `custom.html`에 붙여넣는 링크가 조금 달라졌다.

## 머티리얼 디자인 아이콘 적용

Minimal-mistakes 테마는 사이트의 각 아이콘을 [Font Awesome](https://fontawesome.com)을 통해 웹으로 제공받는다. 이는 역시 외부 사이트에 대한 의존성을 최대한 줄이려는 내 의도와 맞지 않기 때문에 이들 아이콘을 사이트 내에서 구현할 수 있는 방법을 찾기 시작했다. 또, 개인적으로는 동글동글한 아이콘들이 마음에 들지 않기도 했다. 

이렇게 찾다보니 찾은 것이 머터리얼 디자인이다. 머티리얼 디자인은 구글에서 밀고 있는 디자인 지침 정도로 생각하면 될 것 같다. 나는 특히 이 디자인에서 제공하는 아이콘 (sharp를 사용했다)에 관심이 있었고, 또 색상표 또한 참고하여 수학 관련 글에 들어갈 notice들 색상을 정해주었다. 

이 커밋에서 수정한 것은 굉장히 많아서 일일히 적는 것이 힘들고 별 의미도 없을 것 같다. 크게 수정한 흐름만 정리하자면, 

1. Google의 머터리얼 디자인 아이콘 [repository](https://github.com/marella/material-icons)에서 `material-icons-sharp.woff`와 `woff2` 파일을 다운받아, [폰트 추가]()에서 했던 것처럼 폰트를 추가해준다.
2. Google에서 일러준 바와 같이 ([공식문서](https://developers.google.com/fonts/docs/material_icons)), 다음 코드를 적당한 곳에 붙여넣는다. 나는 `_base.scss`에 붙여넣었다.
    ````scss
    /* Material icons */
    .material-icons {
      font-family: 'Material Icons';
      font-weight: normal;
      font-style: normal;
      font-size: 24px;  /* Preferred icon size */
      display: inline-block;
      line-height: 1;
      text-transform: none;
      letter-spacing: normal;
      word-wrap: normal;
      white-space: nowrap;
      direction: ltr;

      /* Support for all WebKit browsers. */
      -webkit-font-smoothing: antialiased;
    
      /* Support for Safari and Chrome. */
      text-rendering: optimizeLegibility;

      /* Support for Firefox. */
      -moz-osx-font-smoothing: grayscale;

      /* Support for IE. */
      font-feature-settings: 'liga';
    }

    /* Rules for sizing the icon. */
    .material-icons.md-10 { font-size: 10px; }
    .material-icons.md-14 { font-size: 14px; }
    .material-icons.md-16 { font-size: 16px; }
    .material-icons.md-18 { font-size: 18px; }
    .material-icons.md-24 { font-size: 24px; }
    .material-icons.md-36 { font-size: 36px; }
    .material-icons.md-48 { font-size: 48px; }

    /* Rules for using icons as black on a light background. */
    .material-icons.md-dark { color: rgba(0, 0, 0, 0.54); }
    .material-icons.md-dark.md-inactive { color: rgba(0, 0, 0, 0.26); }

    /* Rules for using icons as white on a dark background. */
    .material-icons.md-light { color: rgba(255, 255, 255, 1); }
    .material-icons.md-light.md-inactive { color: rgba(255, 255, 255, 0.3); }
    ````
3. 이후 사이트에서 font awesome 폰트를 사용하는 곳을 모두 찾아 적절한 아이콘으로 바꿔준다. 


