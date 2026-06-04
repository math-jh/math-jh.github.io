---
title: "사영공간의 닫힌 부분스킴"
description: "사영공간의 닫힌 부분스킴은 동차 다항식들의 영점집합으로 표현할 수 있으며, 이 성질 덕분에 아핀 스킴과 거의 비슷한 방식으로 다룰 수 있다."
excerpt: "Projective space의 closed subscheme과 homogeneous ideal의 대응"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/closed_subschemes_of_projective_spaces
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
last_modified_at: 2025-03-08
weight: 14

---

이제 우리는 closed subscheme의 예시로 $$\mathbb{P}_\mathbb{K}^n$$의 closed subscheme들을 살펴본다. $$\mathbb{P}^n$$은 affine scheme보다는 약간 복잡하지만 그래도 일반적인 scheme보다는 다루기가 편한 대상인데, [§사영스킴, ⁋정의 4](/ko/math/scheme_theory/projective_schemes#def4)에 의하여 $$\mathbb{P}^n$$의 임의의 닫힌집합은 항상 $$\mathbb{K}[\x_0,\ldots, \x_n]$$의 homogeneous polynomial들의 zero set으로 쓸 수 있기 때문이다. 즉, 이들 homogeneous polynomial들은, 비록 $$\mathbb{P}^n$$에서 정의된 함수는 아니지만 적어도 닫힌집합을 표현할 때는 affine scheme과 거의 유사한 방식을 사용할 수 있다. 