---

title: "Github pages와 Jekyll"
excerpt: "Jekyll과 티스토리, 네이버 블로그"
read_time: false

categories: [Blog Development]
permalink: /ko/blog_dev/introduction

sidebar: 
    nav: "blog_development-ko"

date: 2022-07-07
last_modified_at: 2022-07-07
weight: 1

---

## Github pages와 Jekyll

Github는 보통 코딩하는 사람들이 많이 사용하는 온라인 버전관리 시스템이다. 대충 중요한 파일을 수정할 때 
```
 파일 1 (20220707 수정).tex
 파일 1 (20220708 수정).tex
```
등과 같이 중간중간 단계의 수정본을 꼼꼼히 남겨두는 것을 알아서 해 주는 시스템이라 생각하면 된다. Github는 여기에 사이트를 꾸려 올려두면 호스팅을 해 주는 서비스를 제공하는데, 이게 Github pages다.

코딩의 코 자도 모르면서 티스토리, 네이버, 워드프레스 등등의 블로그 플랫폼을 제외하고 Github pages를 택한 이유는 크게 두 가지다.

1. 수식입력이 용이해야 한다. 가령 네이버 블로그는 수식입력이 불편하여 일찌감치 포기했다.
2. 티스토리가 네이버의 유력한 대체제였는데, 생각보다 커스터마이징이 불가능했다.

사이트를 처음부터 끝까지 HTML로 짜는 것은 코딩을 할 줄 모르는 나같은 사람에겐 끔찍한 일이다. 다행히도 Github pages는 [Jekyll](https://jekyllrb-ko.github.io)을 통해 사이트를 생성한다. 즉, 글만 작성하더라도 Jekyll을 거치면 그럴듯한 사이트가 나오게 된다. Jekyll이 어떤 모양의 사이트를 생성할지는 사용자가 어떤 Jekyll 테마를 사용하는지에 따라 결정된다.

Github pages는 Jekyll을 통해 사이트를 생성하지만, 개인 컴퓨터에서 로컬하게 빌드하여 확인을 먼저 해 보고 싶다면 Jekyll을 직접 설치해야 한다.

## Markdown

블로그에 올릴 포스팅은 마크다운 형태로 작성해야 한다. HTML로 작성해도 상관은 없지만, 가령 HTML 코드 상에서는 

```html
<ol>
    <li>첫 번째 항목 </li>
    <li>두 번째 항목 </li>
</ol>
```

과 같이 쓸 것을 마크다운에서는

```md
1. 첫 번째 항목
2. 두 번째 항목
```

과 같이 쓰면 되기 때문에 빌드되기 전 파일을 보더라도 한 눈에 들어오게 된다.