---

title: "Github pages와 Jekyll"
excerpt: "Jekyll과 티스토리, 네이버 블로그"
read_time: false

categories: [Blog development]
permalink: /ko/blog_dev/introduction

sidebar: 
    nav: "dev"

date: 2022-07-07
last_modified_at: 2022-07-07
weight: 1

---

## 플랫폼 선택

세상에는 정말로 많은 블로그 플랫폼이 있다. 우리나라에서 주로 사용하는 티스토리나 네이버도 있고, 외국에서 많이 사용하는 듯한 워드프레스도 있다.  
플랫폼들은 모두 나름의 장단점이 있으니 어떤 것이 좋다고 하기는 어렵겠지만, 내 경험을 바탕으로 왜 티스토리나 네이버 대신 Github pages에 블로그를 만들게 되었는지를 이야기해보려 한다.

1. 우선, 나는 블로그에 전공내용 공부한 것을 정리해 올릴 계획이었으므로 최우선 고려사항은 수식입력의 용이성이었다. 이 부분에서 네이버가 가장 먼저 걸러졌다.  
    네이버 블로그는 자체적인 수식입력기를 지원하는데, 최근에 $\TeX$ 문법으로 바뀌기 전까지는 꽤나 오랫동안 한컴 수식입력기와 비슷한 문법을 사용했었다. 또, 곳곳에 수식을 입력해야 하는데 $\LaTeX$ 처럼 <code>$...$</code>로 둘러싼 내용을 자동으로 수식으로 바꿔주는 등의 기능이 없어 일일히 수식입력기를 클릭하고, 식을 입력하고 입력창을 닫아야만 수식이 입력되는 방식은 엄청나게 큰 단점으로 다가왔다.  
    다만 네이버 블로그가 티스토리 혹은 Github보다 다루기가 훨씬 편하고, 대다수의 편의기능들을 네이버가 기본설정으로 알아서 처리해주기 때문에 캐주얼하게 블로그를 사용하실 분들은 굳이 티스토리 혹은 Github을 고집하실 필요는 없을 것 같다.
2. 티스토리는 조금 운영을 했었다. 개인적인 느낌으로는 티스토리는 네이버와 Github 사이의 어딘가에 있는 느낌이다. 사이트 자체에서 css 혹은 html 파일을 읽어줄 수 있기 때문에 네이버보다 훨씬 자유로운 커스터마이징이 가능하고, 뿐만 아니라 다른 누군가가 이미 커스터마이징을 끝내고 공유해주신 스킨들이 많아 네이버에서 스킨 선택하듯 간편하게 블로그를 구성할 수도 있다. 커스터마이징이 단순히 스킨에만 국한되는 것은 아니고, 여러 기능들도 원한다면 추가할 수 있어서 특히 MathJax로 수식을 렌더링할 수 있었던 점이 나에게는 네이버에 대한 확실한 비교우위로 작용했다.  
    하지만 사용하다보니 약간 마음에 안 들었던 점이 있었다. 우선 HTML에디터를 지원은 하지만, 썩 신통찮았다. 예컨대 HTML에디터에서 작업을 하고, 포스팅을 마친 후 수정하기 위해 돌아오면 <code>&lt;strong&gt;</code> 태그가 <code>&lt;b&gt;</code> 태그로 바뀌어있는 등의 일이 있었다. 이 경우야 결과물에는 차이가 없다고는 하지만, 다음에 비슷한 일이 일어났을 때는 어떤 방식으로 오류가 생길지가 불안했다.  
    이러한 문제들은 어떻게 해결된다 하더라도, 어쨌든 HTML 코드로 작성한 글은 보기 좋은 모양은 아닌 것이 확실하다.

이런 이유로 Github와 같은 코딩냄새 나는 곳에 블로그를 만드는 것이 처음에 조금 고생하더라도 훨씬 편할 것이라 생각했다. 

## Github과 Github pages

Github는 보통 코딩을 하시는 분들이 많이 사용하는 온라인 버전관리 시스템이다. 나는 코딩에는 별 관심이 없어서 이걸 자세히 설명할 생각은 없는데, 대충 중요한 파일을 수정할 때 
```
 파일 1 (20220707 수정).hwp
 파일 1 (20220708 수정).hwp
```
등과 같이 중간중간 단계의 수정본[^1]을 꼼꼼히 남겨두는 것을 알아서 해 주는 시스템이라 생각하면 된다.  

Github pages는 이 Github의 특정 레포지토리에 사이트의 알맹이를 올려놓으면, 실제로 인터넷을 통해 이 사이트에 접속할 수 있도록 호스팅을 해 주는 것으로 생각하면 될 것 같다.

## Jekyll과 테마

하지만 어떤 사이트를 아무것도 없는 상태에서 처음부터 만드는 것은 고통스러운 일이다. 예컨대 똑같은 포맷으로 보여질 두 개의 텍스트 파일들이 있다 하더라도, 이를 사이트로 만들기 위해서는 서로 다른 두 개의 페이지를 직접 만들어야 한다. 

이를 해결해주기 위해 [Jekyll](https://jekyllrb-ko.github.io)이 있다. 위와 같은 상황에서, 두 개의 텍스트 파일들이 주어졌을 때 Jekyll은 이 파일들을 이용해 자동으로 사이트를 생성해준다. 따라서 사이트의 모양에는 크게 신경쓰지 않고 글만 작성하더라도 Jekyll을 거치면 그럴듯한 사이트가 나오게 된다. Jekyll이 어떤 모양의 사이트를 생성할지는 사용자가 어떤 Jekyll 테마를 사용하는지에 따라 결정된다.

Github의 특정 레포지토리에 이렇게 블로그에 내용에 해당하는 텍스트 파일들을 올려놓으면, Github pages는 이를 Jekyll을 통해 사이트의 형태로 바꾼 후 이 사이트를 호스팅해주는 역할을 한다. 따라서, 만일 블로그 관리를 Github을 통해 온라인으로만 할 생각이라면 Jekyll이 뭔지 굳이 알 필요는 없다.   다만 블로그를 개인 컴퓨터에서 로컬하게 띄워본 후 이 수정사항을 한번에 Github에 올리려 한다면, 로컬 컴퓨터에서는 Github pages가 없으므로 Jekyll을 직접 설치해서 이를 통해 사이트를 빌드해야 한다. 

## Markdown

위에서 내가 티스토리를 사용하지 않게 된 계기를 이야기하며, 티스토리의 코드는 HTML이라는 이야기를 했었다. HTML은 어떤 개발자가 와서 깔끔하게 다듬더라도 어쨌든 사람이 읽으라고 만들어놓은 포맷은 아니기 때문에 기본적으로 읽기가 힘들다. Github pages (혹은 Jekyll)은 마크다운을 지원한다. 마크다운은 글을 쓸 때 편하기 위해 제정된 언어인데, 예를 들어 이 페이지 맨 위의 개조식 항목의 경우, HTML로 작성한다면
```html
<ol>
    <li>우선, 나는 ... </li>
    <li>티스토리는 ... </li>
</ol>
```
이 될 것이나, 마크다운에서는 그냥 글을 쓰듯
```md
1. 우선, 나는 ...
2. 티스토리는 ...
```
와 같이 쓰면 된다. 이런 식으로 글을 쓰면, 어차피 호스팅을 할 때에는 Jekyll이 알아서 마크다운을 HTML 파일로 변환해줄 것이다. 필요한 곳에서는 HTML 언어 또한 사용할 수 있다.

다음 글부터는 실제로 Github에 블로그를 만드는 법을 살펴본다. 




[^1]: 다만 위에서 예로 든 .hwp 파일 등과 같은 바이너리 파일들은 Github으로 관리하는 의미가 없다. $\TeX$ 파일은 텍스트 파일이니 가능할 듯.