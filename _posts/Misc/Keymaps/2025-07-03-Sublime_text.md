---

title: "서브라임 텍스트"
excerpt: ""

categories: [Misc / Keymaps]
permalink: /ko/misc/keymaps/sublime_text
header:
    overlay_image: 
    overlay_filter: 0.5
toc: false
date: 2025-07-03
last_modified_at: 2025-07-03
weight: 1

---

나는 이렇게 블로그에 글을 올리거나, 논문 등 $\LaTeX$ 작업을 할 때 주로 `Sublime Text`를 이용한다. 원래는 내가 개발자도 아니고, 굳이 이렇게 각각의 프로그램들이 주가 되는 카테고리를 만들 생각은 없었으나 키보드 관련 글들을 쓰다가 `VIA` 등과 관련된 이야기가 나오면 아무래도 Keybinding 관련된 이야기를 할 수밖에 없고, 따지고 들어가면 결국 키보드 키 세팅을 왜 이렇게 할 수밖에 없었는지는 내가 `Sublime Text`에서 어떻게 key binding을 설정했는지를 먼저 설명해야 하는 것이었다. 

이 카테고리의 글들은 모두 마찬가지로 결과적으로는 왜 내 키맵이 이렇게 해괴망측한지를 설명하기 위한 것이다. 아마 각각의 글들은 모두 제목으로 프로그램 이름을 달아둘 것이지만, 이와 같은 이유로 그 내용은 오직 이 프로그램의 다양한 단축키(...)에 대한 것이 주를 이룰 것이다. 이렇듯 키보드에 관한 내용이 주임에도 불구하고 첫 글이 `Sublime Text`인 이유는 결과적으로 여기에서 다양한 key binding을 우선 설명하는 것이 필요하기 때문이다. 

내가 단축키를 지정할 때 세운 몇 가지 원칙들이 있다. 

1. `VIA` 내에서 해결할 수 있는 단축키일 것.  
    - 내가 주로 사용하는 키보드는 어차피 `QMK`나 `ZMK`로 소스부터 컴파일하긴 하지만 우선 내가 갖고 있는 키보드의 절대다수는 `VIA` 지원이다. 이론적으로는 모든 `VIA` 지원 키보드는 `QMK` 지원 키보드이므로 이는 다소 웃긴 말일 수는 있으나, 사실 대부분 `VIA` 지원 키보드라 이름붙이고 나오는 키보드들이 `json` 파일만 제공하고 기본적인 설정 파일들은 별도로 제공하지 않는 경우가 대부분이다. 때문에 `VIA` 안에서 지원하는 기능들만을 활용하는 것을 가장 큰 목표로 삼았다. 
2. 키보드가 하는 역할은 최대한 줄이고 컴퓨터의 역할을 늘릴 것.  
    - 이건 사람에 따라 취향이 갈릴 수도 있는 영역이고 나 또한 종종 마음이 바뀐다.  
    가령 $\LaTeX$에서 `\begin{definition}...\end{definition}`를 넣는 상황을 생각해보면, 매크로 기능을 사용하여 키보드에 이 문구를 저장해두고 특정 키를 누를 때마다 이 문구가 나가도록 할 수 있다. 이러한 방식의 장점은 어느 컴퓨터에서도 해당 키를 누르면 같은 결과가 나온다는 것이고 단점은 MCU의 한계로 인해 저장할 수 있는 매크로에 한계가 있고 세밀한 지정이 불가능하다는 것이다. 반대로 키보드에는 어떠한 것도 저장하지 않고 컴퓨터에 이 매크로를 저장하여, 특정 키 조합 (가령 `Ctrl+Shift+Super+D`)을 누르면 이 매크로가 나가도록 할 수 있다. 이 방식은 앞선 방식과 정반대의 장단점을 가진다. 즉 메모리 걱정없이, 프로그램이 지원하는 다양한 기능을 십분 활용하여 다채로운 사용이 가능하다는 것은 장점이지만 내가 설정해두지 않은 컴퓨터에서는 이러한 사용이 불가능하다는 것이 단점이다.  
    나는 둘째 방법을 택했다.
3. $\LaTeX$ 관련 단축키에서는 `\`를 사용하지 않을 것.  
    - 내 주력 키보드인 Sofle과 Charybdis는 thumb cluster 중 하나에 따로 $\LaTeX$ snippet 입력용 키를 할당해줄 수 있어서 해당사항이 없지만, 일반적인 HHKB배열이나 TKL, 풀배열 등의 경우는 마땅히 단축키를 지정할만한 키가 없다. 물론 아무 키에나 할당해도 상관은 없지만 가급적이면 직관적인 ($\LaTeX$에서 모든 명령어는 `\`로 시작한다.) 키를 택하는 것이 좋을 것이다. 
4. 가급적이면 윈도우에서도 쓸 수 있게 만들 것.

## Snippet

`Sublime Text`는 다양한 단축키를 기본으로 제공하지만, 나는 개발자가 아니니 별 쓸모가 없다. 내가 필요로 하는 것은 위에서 언급한 것과 같이 `\begin{definition}...\end{definition}` 등을 넣거나 하는 정도의 것들이다. 이를 위해서는 다음과 같이 snippet을 만들어주면 된다.

```xml
<snippet>
    <content><![CDATA[
\begin{definition}
    ${0}
\end{definition}
]]></content>
    <tabTrigger>def</tabTrigger>
    <scope>text.tex.latex</scope>
</snippet>
```

보다시피 `<content><![CDATA[ ... ]]></content>` 안에 들어가는 내용은 이 snippet을 실행했을 때 나와야하는 결과물이며, 이 사이에 있는 `${0}`은 이 snippet이 끝났을 때 커서가 있어야하는 위치이다. 이는 `${1}`이 등장하는 다음 코드를 보면 좀 더 이해가 잘 될 것이므로 일단은 넘어가자. `tabTrigger`는 내가 지정한 단축어(여기서는 `def`)를 타이핑하고 `Tab` 키를 누르면 이 snippet이 실행되도록 하는 것인데, 우리는 어차피 이 snippet을 실행시키는 keybinding을 새로 만들 것이므로 안 써줘도 상관은 없다. `scope`는 tab trigger로 이 snippet을 실행할 때 어떤 형식의 파일에서만 실행될지를 지정해주는 항목이다. 

한편 블로그에 글을 쓸 때, 즉 `markdown` 파일을 수정할 때 정의를 넣기 위해서는 `\begin{definition}...\end{definition}`이 아니라 다음의 `HTML` 코드

```html
<div class="definition" markdown="1">

<ins id="defX">**정의 X**</ins> 

</div>
```

를 넣어야 한다. 여기서 `X`는 숫자이다. 그럼 이를 넣기 위한 snippet은 다음과 같다. 

```xml
<snippet>
    <content><![CDATA[
<div class="definition" markdown="1">

<ins id="def${1}">**정의 ${1}**</ins> ${0}

</div>
]]></content>
    <tabTrigger>def</tabTrigger>
    <scope>text.html.markdown</scope>
</snippet>
```

아까와 다른 점으로 `${1}`이 생겼는데, 이제 snippet을 실행하면 커서가 `${1}`에서 시작하며, 위의 snippet에는 `${1}`이 두 개 있으므로 커서가 이 두 곳에서 동시에 활성화되어 숫자 `X`를 입력하면 위의 `HTML` 코드와 같은 형태가 나온다. 이후 `Tab`을 누르면 `${2}`, `${3}` 등등을 거쳐 `${0}`에서 끝이 나게 된다. 위의 snippet과 비교해보면 `tabTrigger`가 둘 다 `def`으로 겹치지만. 서로 다른 `scope` 덕분에 $\LaTeX$ 파일에서 tab completion을 통해 snippet을 불러오면 첫 번째 snippet이, 마크다운 파일에서는 두 번째 snippet이 나온다. 

## Key bindings

이제 이들을 단축키에 지정하자. 지금까지 한 것 만으로도 `D`,`E`,`F` 키를 순서대로 타이핑한 후 `Tab`을 누르는 매크로를 사용하여 이 snippet이 작동되도록 할 수 있으나, 이는 설계원칙 2에 어긋난다. 그 대신, 특정 키가 modifier key `Ctrl+Shift+Super`로 작동하게 해 두고, `Ctrl+Shift+Super+D`에 이 snippet이, `Ctrl+Shift+Super+T`에 Theorem을 넣어주는 snippet이 나오도록 한다면 매크로 소모 없이 원하는만큼 snippet을 불러올 수 있다. 

이를 위해 다음과 같은 key binding을 추가한다. 

```json
[
    {"keys": ["ctrl+super+shift+]", "d"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/definition.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.tex.latex"}]},
    {"keys": ["ctrl+super+shift+]", "d"], "command": "insert_snippet", "args": {"name": "Packages/User/Jekyll/definition_ko.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.html.markdown"}]}, 
]
```

이제 `keys`에 해당하는 키 `Ctrl+Shift+Super+]`, `D`를 순차적으로 누르면 `command`에 해당하는 `insert_snippet`이 발동되며, 이 때 발동되는 snippet이 무엇인지는 `args`에서 정해주었다. 똑같은 `keys`를 갖는 위의 두 개의 key binding 중 어떤 것이 발동될지는 지금 작업중인 파일 형식과 `context`에서 지정한 파일형식을 비교하여 결정된다. 

Key binding을 보면 위에서부터 계속 예시로 들었던 것과는 달리 `Ctrl+Shift+Super+D` 대신 두 글자로 이루어진 열 `Ctrl+Shift+Super+]`, `D`를 사용한 것을 알 수 있는데, 이는 일부분이 겹치는 key binding을 처리하기 위해서이다. 가령 명제(Proposition)와 증명(Proof)을 생각하자. 이들은 모두 문서 전체에서 굉장히 빈번하게 쓰일 snippet들이며, 어떤 방식으로든 명제는 문자 `P`에, 증명은 문자 `P`, `F`에 대응시키고 싶다. 문제는, 만일 

```json
[
    {"keys": ["ctrl+super+shift+p"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/proposition.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.tex.latex"}]},
    {"keys": ["ctrl+super+shift+p", "ctrl+super+shift+f"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/proof.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.html.markdown"}]}, 
]
```

와 같이 key binding을 짠다면, `Ctrl+Shift+Super+P`를 입력한 순간에 `Sublime Text` 입장에서는 사용자가 첫 번째와 두 번째 key binding 중 어떠한 것을 입력하려 했는지 알 수 없기 때문에 명제 key binding을 넣을 때마다 불쾌한 딜레이가 생기게 된다. 그 대신, 선행하는 `Ctrl+Shift+Super+]`의 개수를 통해 이 key binding이 몇 글자인지를 알려준다면 이러한 일은 일어나지 않는다. 즉 다음과 같이 하면 된다. 

```json
[
    {"keys": ["ctrl+super+shift+]", "d"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/proposition.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.tex.latex"}]},
    {"keys": ["ctrl+super+shift+]", "ctrl+super+shift+]", "p", "f"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/proof.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.html.markdown"}]}, 
]
```

한편 각각의 key binding마다 약간의 변형이 가해진 버전이 있을 수 있는데, 가령 번호 없는 definition `\begin{definition*}...\end{definition*}`을 생각할 수 있을 것이다. 이 때는 여기에 해당하는 snippet을 새로 만들고, key binding에는 `Alt` 키를 추가하여 

```json
[
    {"keys": ["ctrl+super+shift+]", "d"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/definition.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.tex.latex"}]},
    {"keys": ["ctrl+super+shift+alt+]", "d"], "command": "insert_snippet", "args": {"name": "Packages/User/LaTeX/Large_environments/definition_ast.sublime-snippet"}, "context": [{"key": "selector", "operator": "equal", "operand": "text.tex.latex"}]}, 
]
```

와 같은 식으로 설정하면 된다.