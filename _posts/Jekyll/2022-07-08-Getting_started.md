---

title: "Github pages에서 블로그 만들기"
excerpt: "Github 블로그 저장소 만들기"

lang: ko

categories: [Blog development]
permalink: /blog_dev/getting_started

sidebar: 
    nav: "dev"

date: 2022-07-08
last_modified_at: 2022-07-08
weight: 2

---

앞선 글에서 Github 블로그를 만드는 데 필요한 배경지식을 모두 갖췄으니, 이제 실제로 블로그를 만들어보자!

## Github 회원가입

Github pages를 사용하기 위해서는 당연히 Github에 회원가입을 해야 한다. [Github 홈페이지](https://github.com)에 들어가서 미리 회원가입을 해 두자.

## Jekyll 테마 고르기 및 적용

우선 블로그에서 사용할 테마를 고르자. Jekyll은 많은 사람들이 사용하다보니 구글링을 해 보면 수많은 테마들이 쏟아져나온다. [Jekyll Themes](http://jekyllthemes.org)와 같이 테마를 정리해둔 사이트도 있다. Jekyll themes에 접속해서 맘에 드는 테마를 선택하면 데모 사이트로 이동을 할 수도 있으니 직접 본 후 비교하기도 좋다. 나는 Minimal-mistakes 테마를 선택했다.

![Minimal-mistakes](/assets/images/Blog_development/Getting_started-1.png){:width="600px" .align-center}

테마를 고른 후에는 해당 테마의 Github 저장소로 이동한다. Jekyll themes 사이트에서 테마를 골랐다면 위의 사진과 같이 Homepage 버튼이 있는데, 이를 통해 이동할 수 있다. 

이후, 이 테마를 적용해야 하는데 여기에는 두 가지 방법이 있다.

1. 저장소 오른쪽 위에 있는 Fork 버튼을 눌러 저장소를 내 Github 계정으로 Fork해온다. 이렇게 하면 해당 저장소를 그대로 내 저장소로 복사해오게 된다. 이 때 github pages를 이용해 사이트를 호스팅하기 위해서는 저장소 이름이 `(본인 Username).github.io`여야 하므로, Repository name을 이에 맞게 수정해준다. 

    ![Forking_repository](/assets/images/Blog_development/Getting_started-2.png){:width="600px" .align-center}
        
    내 경우에는 이미 내 계정에 `math-jh.github.io` 이름을 가진 저장소가 있어서 오류가 뜨지만, 처음 하시는 분들은 아무 문제 없이 진행될 것이다.

2. 혹은 테마 저장소에서 `Code > Download ZIP`을 눌러 저장소의 파일을 다운받은 후, 이를 내 github 저장소에 직접 올릴 수도 있다. 이렇게 하면 해당 저장소의 파일만 내 저장소로 복사해오게 되므로 원작자가 테마를 작성할 때 생긴 커밋 히스토리등은 가져오지 않게 된다.
    이렇게 하기 위해서는 내 저장소를 우선 만들어야 하는데, 앞서 Github에 회원가입을 한 후 아무것도 하지 않았다면 텅 빈 홈 화면에 `Create a new repository` 버튼이 있을 것이다. 

    ![Create_repository](/assets/images/Blog_development/Getting_started-3.png){:width="600px" .align-center}

    이 버튼을 클릭해서 새 저장소를 만들자. 위에서 Fork를 했던 것과 마찬가지로 저장소의 이름은 `(본인 Username).github.io`로 지정해야 하며, 그 외의 설정은 어떻게 해도 무방하다. Public/Private 설정도 이 저장소가 public일지 private일지를 결정하는 것이고, github pages로 호스팅된 사이트는 둘 중 어떤 것을 택하더라도 접근이 가능하므로 뭘 선택해도 상관이 없다.  
    이렇게 저장소를 만들고 나면 아래와 같은 창이 뜨는데, 우리는 앞서 테마의 저장소를 다운받아뒀으므로 `uploading an existing file`을 택하여 다운받은 저장소를 통째로 올린다. 

    ![New_repository](/assets/images/Blog_development/Getting_started-4.png){:width="600px" .align-center}

    그럼 1번과 동일한 결과물이 나오지만, 커밋 히스토리는 정리된 상태가 된다. 이렇게 올릴 수 있는 파일의 개수는 100개로 제한되어 있으므로, 파일의 개수가 100개를 넘어가면 다른 방법을 사용해야 한다. `Set up in Desktop` 버튼을 눌러 Github Desktop 앱을 설치한 후 로그인을 하자. 아래와 같은 화면이 뜨는데, 오른쪽에 방금 만든 repository `(본인 username).github.io`를 선택하여 clone을 진행하면 된다. 

    ![Github_desktop](/assets/images/Blog_development/Getting_started-5.png){:width="600px" .align-center}

    Clone을 진행할 때, Local path는 이 github 저장소가 내 컴퓨터에서는 어디에 저장될지를 의미한다. Clone을 완료한 후, 이 path에 아까 받아둔 테마 파일을 통째로 복사한 후 첫 번째 commit을 진행하면 된다. Commit을 하려면 commit summary를 필수로 적어주어야 하는데, 파일이 하나만 수정되었다면 `Update/Create/Delete (파일이름)`과 같이 Github desktop에서 자동으로 summary를 채워줘서 신경쓰지 않아도 되지만, 지금처럼 여러 파일이 동시에 수정되었을 때는 직접 입력해줘야 한다.

    ![First_commit](/assets/images/Blog_development/Getting_started-6.png){:width="600px" .align-center}

    아직 브랜치가 없는 상태이기 때문에, 이렇게 commit을 한 후 publish branch를 누르면 Github 저장소에 테마 파일들이 모두 저장된다.

    ![Publish_branch](/assets/images/Blog_development/Getting_started-7.png){:width="600px" .align-center}

물론 Github desktop 대신 CLI를 쓰시는 분은 늘상 하시던대로 하면 된다. (사실 CLI를 쓰시는 분은 굳이 이 부분을 읽지도 않으실 듯...)

1번 혹은 2번을 택해서 진행했다면, 1\~2분정도 기다린 후 인터넷 주소창에 `(본인 Username).github.io`를 입력하여 접속하면 기본화면이 뜬다. 

![Initial_homepage](/assets/images/Blog_development/Getting_started-8.png){:width="600px" .align-center}

물론 아직은 아무것도 없으니 열심히 블로그를 다듬어야 한다. 
