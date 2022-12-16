---

title: "접속"
excerpt: "Vector bundle 위에서 정의된 미분"

categories: [Math / Manifold]
permalink: /ko/math/manifold/Connection
header:
    overlay_image: /assets/images/Manifold/Connection.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 13

---

Lie derivative를 이용하면 벡터장이나 differential form을 미분할 수 있지만, 이 개념을 임의의 vector bundle $\pi:E\rightarrow M$으로 확장하는 것은 불가능하다. Tangent bundle $TM$ 위에서는 integral flow $\phi$ 위의 두 점 $p,q$가 주어졌을 때, 두 tangent space $T_pM$과 $T_qM$을 잇는 자연스러운 isomorphism $d\phi^{-t}$가 존재했지만 vector bundle 위에서는 
