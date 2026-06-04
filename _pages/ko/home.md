---
layout: splash
permalink: /ko/
hidden: true
header:
  overlay_image: /assets/images/Pages/Home/Stationary_main.png
  overlay_filter: 0.9
  caption: "Mirror symmetry and Schrödinger's cat. <br/>From [*Horizon* $(2018,\\text{ vol.}1)$](https://horizon.kias.re.kr/6469/)<br/>Photo by [**mareykrap**](https://notefolio.net/mareykrap/104880)"
  actions:
    - label: "<span class='material-icons md-18' style='vertical-align:-.1em'>&#xE873;</span>  About"
      url: "/ko/about"
excerpt:

# Subject tiles, grouped by big category (mirrors category-ko in navigation.yml).
# Each group is rendered as its own feature_row below; the include's bordered
# wrapper separates the sections — no blank spacer tiles needed.
row_general:
  - image_path: /assets/images/Pages/Thumbnails/Files/Linear_Algebra.jpeg
    alt: "linear_algebra"
    title: "선형대수학"
    url: "/ko/linear_algebra"
    btn_class: "btn--primary"
    btn_label: "Read more"

row_foundations:
  - image_path: /assets/images/Pages/Thumbnails/Files/Set_Theory.jpeg
    alt: "set_theory"
    title: "집합론"
    url: "/ko/set_theory"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Category_Theory.jpeg
    alt: "category_theory"
    title: "범주론"
    url: "/ko/category_theory"
    btn_class: "btn--primary"
    btn_label: "Read more"

row_algebra:
  - image_path: /assets/images/Pages/Thumbnails/Files/Algebraic_Structures.jpeg
    alt: "algebraic_structures"
    title: "대수적 구조들"
    url: "/ko/algebraic_structures"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Group_Theory.jpeg
    alt: "group_theory"
    title: "군론"
    url: "/ko/group_theory"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Ring_Theory.jpeg
    alt: "ring_theory"
    title: "환론"
    url: "/ko/ring_theory"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Multilinear_Algebra.jpeg
    alt: "multilinear_algebra"
    title: "다중선형대수학"
    url: "/ko/multilinear_algebra"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Field_Theory.jpeg
    alt: "field_theory"
    title: "체론"
    url: "/ko/field_theory"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Homological_Algebra.jpeg
    alt: "homological_algebra"
    title: "호몰로지 대수학"
    url: "/ko/homological_algebra"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Commutative_Algebra.jpeg
    alt: "commutative_algebra"
    title: "가환대수학"
    url: "/ko/commutative_algebra"
    btn_class: "btn--primary"
    btn_label: "Read more"

row_geometry:
  - image_path: /assets/images/Pages/Thumbnails/Files/Topology.jpeg
    alt: "topology"
    title: "위상수학"
    url: "/ko/topology"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Algebraic_Topology.jpeg
    alt: "algebraic_topology"
    title: "대수적 위상수학"
    url: "/ko/algebraic_topology"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Manifolds.jpeg
    alt: "manifolds"
    title: "미분다양체"
    url: "/ko/manifolds"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Riemannian_Geometry.jpeg
    alt: "riemannian_geometry"
    title: "리만기하학"
    url: "/ko/riemannian_geometry"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Algebraic_Geometry.jpeg
    alt: "algebraic_geometry"
    title: "대수다양체"
    url: "/ko/algebraic_varieties"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Symplectic_Geometry.jpeg
    alt: "symplectic_geometry"
    title: "사교기하학"
    url: "/ko/symplectic_geometry"
    btn_class: "btn--primary"
    btn_label: "Read more"

row_misc:
  - image_path: /assets/images/Pages/Thumbnails/Files/Blog_Development.jpeg
    alt: "blog_development"
    title: "블로그 개발일지"
    url: "/ko/blog_development"
    btn_class: "btn--primary"
    btn_label: "Read more"
  - image_path: /assets/images/Pages/Thumbnails/Files/Peripherals.jpeg
    alt: "peripherals"
    title: "주변기기"
    url: "/ko/peripherals"
    btn_class: "btn--primary"
    btn_label: "Read more"
---

## 교양수학
{% include feature_row id="row_general" %}

## 수학기초론
{% include feature_row id="row_foundations" %}

## 대수학
{% include feature_row id="row_algebra" %}

## 기하학 및 위상수학
{% include feature_row id="row_geometry" %}

## 기타
{% include feature_row id="row_misc" %}
