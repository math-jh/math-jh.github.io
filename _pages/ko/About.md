---

title: ""
layout: single
breadcrumbs: false
permalink: /ko/about
author_profile: true
header:
  image: /assets/images/Pages/Home/Main.gif
  caption: "Mirror symmetry and Schrödinger's cat. <br/>From [*Horizon* $(2018,\\text{ vol.}1)$](https://horizon.kias.re.kr/6469/)<br/>Photo by [**mareykrap**](https://notefolio.net/mareykrap/104880)"
sidebar: 
    nav: "category-ko"

---

## 사이트 소개

이 블로그는 개인적으로 공부한 것들을 정리해 둔 사이트입니다.

이 블로그의 프로토타입은 군대에 있을 때 싸지방에서 overleaf를 이용해서 작성한 600페이지 가량의 $\TeX$ 문서인데, 이를 한글로 옮기고 적당히 수정하여 글을 쓰고 있습니다. 

![](/assets/images/Pages/About/notice.png){:width="250px" class="invert" .align-center}

다만 이 문서는 학부 때 배운 내용들만 정리해 둔 것이라, 학부에서 제가 배우지 않은 카테고리들은 처음부터 새로 써야 해서 업데이트 주기가 뜸합니다. 또, 저 문서를 작성한 후 새로 배운 것들을 잘 섞어서 글에 넣느라 하나를 작성하는 데에 시간이 좀 걸려서 학부 때 배운 내용들도 업데이트 주기가 뜸합니다.  
(그냥 모든 문서의 업데이트 주기가 뜸합니다.)

## 영어 사이트 운영

[\[블로그 개발\] §다국어 지원](/ko/blog_development/multilingual)에서 이미 이 사이트를 한글/영어를 병행하여 운영할 준비는 갖추어 두었습니다. 그러나 위에서 이야기한 것과 같이 새로 추가한 내용들이 원래의 문서 분량보다도 많아지는 현상이 일어나서, 기존의 $\TeX$ 문서를 마크다운 문법에 맞추어 복사-붙여넣기만 하면 될 것이라 생각했던 행복한 상상이 깨져버렸습니다. 

따라서 영어 사이트는 아마도 "수학 공부할거면 이 정도는 알아야지" 싶은 기초적인 내용들을 전부 한글로 쓴 후에야 손을 댈 것 같습니다. 다만 그게 빠를지 제 대학원 졸업이 빠를지는 잘 모르겠습니다.

## 한-영 용어

가급적이면 한글용어를 사용하기 위해 대한수학회의 [수학용어](https://www.kms.or.kr/mathdict/list.html) 페이지를 찾아가며 열심히 번역했지만, 개인적으로 느끼기에 한글용어가 아직 원문에 담겨있는 직관을 다 담지 못한다고 느끼는 경우가 많아 이러한 용어들은 번역하지 않고 그대로 두었습니다. 특히 학부 내용 너머에서 도입되는 용어들은 거의 대부분이 그러합니다. 

어쨌든 [찾아보기](/ko/misc/index) 페이지에 블로그에서 사용한 용어들을 정리해 두었습니다. 이 또한 먼 미래에는 약간 손을 봐서

| 영문 용어 | 한글 용어 | 정의 | 참고 |
| --- | --- | --- | --- |
| <unselected id="binary_relation">binary relation</unselected> | <selected> 이항관계 &#9745;</selected> | [\[집합론\] §이항관계](/ko/math/set_theory/binary_relation) |  |
| <selected class="indented" id="antisymmetric">antisymmetric &#9745;</selected> | <unselected>반대칭적</unselected> | [\[집합론\] §순서관계의 정의](/ko/math/set_theory/order_relations) | [Relation](#relation), [Order relation](#order_relation) |
| <selected class="indented" id="asymmetric">asymmetric &#9745;</selected> | <unselected>비대칭적</unselected> | [\[집합론\] §순서관계의 정의](/ko/math/set_theory/order_relations) | [Order relation](#order_relation) |

처럼 비슷한 용어들 위주로 뭉쳐놓을 생각이지만 언제가 될지는 잘 모르겠습니다.

## 카테고리별 분류

카테고리는 크게 수학과 그 외 잡다한 것으로 분류했습니다.

### 수학

수학 카테고리의 경우, 

- 비전공자들이 배우는 선형대수학/미적분학 내용
- 현대수학의 주춧돌에 해당하는 집합론과 범주론 내용
- 세부적인 전공 내용인 대수학, 해석학, 기하 및 위상수학

으로 크게 나누었습니다. 이산수학이나 통계학 쪽은 제가 관심도 없고 잘 모르는 분야라, 작성할 예정이 없습니다. 또 선형대수학의 경우 수학을 전공한다면 가장 많이 쓰이게 되는 도구 중 하나라 비전공자에겐 약간 과하다 싶은 내용도 모두 포함되어 있습니다.

### 그 외 카테고리

그 외 카테고리에는 우선 블로그 개발일지만 있습니다. 저는 코딩을 전혀 할 줄 몰라 이 사이트를 만들며 삽질을 계속해야 했었는데, 혹시라도 비슷한 삽질을 할 사람이 있을까 하여 기록으로 남겨두었습니다.

## 기타

블로그 내의 자체적인 검색엔진으로 [algolia](https://www.algolia.com/)를 사용하고 있는데, 제가 Travis CI를 사용하지 않는 관계로 색인 생성이 수동입니다. 따라서 최신 글은 잘 검색이 되지 않을 수 있습니다.

또, $\TeX$ 버전의 파일은 거의 소스들을 그대로 베껴쓴 것이라 노테이션이 제각각인데, 이를 최대한 통일하려 노력하긴 했지만 아직 미흡한 부분이 많이 있습니다.