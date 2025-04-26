---

title: "체의 확장"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/field_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Field_extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-04-26
last_modified_at: 2025-04-26
weight: 2

---

우리는 [§체, ⁋명제 2](/ko/math/field_theory/fields#prop2)에 의하여 field들 사이의 morphism은 injective이거나 zero map 뿐이라는 것을 살펴보았다. 이번 글에서 우리는 전자의 경우에 대하여 살펴본다. 

우리는 field morphism 중 injective인 것을 *field extension*이라 부른다. 그럼 고정된 field $\mathbb{K}\in\Field$에 대하여, $\mathbb{K}$의 under category는 $\mathbb{K}$ extension들의 category가 된다. 

[\[범주론\] §범주, ⁋예시 13](/ko/math/category_theory/categories)의 표기법과는 다소 차이가 있으나, 우리는 field extension $\mathbb{K}\rightarrow \mathbb{L}$을 종종 $\mathbb{L}/\mathbb{K}$와 같이 표기한다. 그럼 field extension $\mathbb{L}/\mathbb{K}$가 주어질 때마다 우리는 injective map $\mathbb{K}\hookrightarrow\mathbb{L}$을 통해 $\mathbb{K}$를 $\mathbb{L}$의 subfield와 identify할 수 있다. 그러나, 만일 $\mathbb{L}=\mathbb{K}$이고 $\mathbb{K}\hookrightarrow\mathbb{L}=\mathbb{K}$이 endomorphism인 경우, 이러한 identification은 혼동의 여지가 있으므로 이 경우에는 $\mathbb{K}$와 $\mathbb{L}$의 subfield를 identify하지 않는다.  

정의에 의하여, 두 extension $\mathbb{K} \rightarrow \mathbb{L}_1$과 $\mathbb{K} \rightarrow \mathbb{L}_2$가 주어졌다 하면, 다음 commutative diagram

img

이 이들 사이의 morphism이 된다. 이 때, $\mathbb{L}_1$과 $\mathbb{L}_2$는 모두 field이므로, morphism $\mathbb{L}_1 \rightarrow \mathbb{L}_2$는 반드시 injective여야 한다. 위의 주의사항을 지키는 선에서, 이 경우 우리는 $\mathbb{L}_1$이 $\mathbb{L}_2$의 *subextension*이라 부른다. 

임의의 $\mathbb{K}$-algebra는 특히 $\mathbb{K}$-module, 즉 $\mathbb{K}$-벡터공간이므로 그 차원이 잘 정의된다. 특히 field extension $\mathbb{K} \rightarrow \mathbb{L}$을 통해 $\mathbb{L}$을 $\mathbb{K}$-algebra로 볼 경우, $\mathbb{L}$의 $\mathbb{K}$-벡터공간으로서의 차원이 잘 정의된다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $\dim_{\mathbb{K}}\mathbb{L}$을 extension $\mathbb{L}/\mathbb{K}$의 *degree*라 부르고 $[\mathbb{L}:\mathbb{K}]$로 표기한다. 

</div>