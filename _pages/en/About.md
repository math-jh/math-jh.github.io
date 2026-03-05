---
title: "About"
layout: single
breadcrumbs: false
permalink: /en/about
author_profile: true
header:
  image: /assets/images/Pages/Home/Main.gif
  caption: "Mirror symmetry and Schrödinger's cat. <br/>From [*Horizon* $(2018,\text{ vol.}1)$](https://horizon.kias.re.kr/6469/)<br/>Photo by [**mareykrap**](https://notefolio.net/mareykrap/104880)"
sidebar:
    nav: "category-en"
---

## About this site

I am a graduate student majoring in mathematics, and this blog is a site where I organize what I have studied. At least at the time of writing this post, since I am not yet a senior scholar, the content is mostly written in Korean by referencing well-known references in each field, with some modifications. In particular, the fields I have written about while studying (rather than after completing my studies) are even more so.

This blog's prototype was a 600-page $\TeX$ document I wrote using Overleaf in my barracks while serving in the military. I'm writing posts by translating it into Korean and making appropriate modifications.

![](/assets/images/Pages/About/notice.png){:width="250px" .align-center}

This blog's title comes from something one of my seniors once told me. Roughly, it was about not trying to study everything when doing research, but rather deciding what to accept as facts and putting the proofs and such into my own black box.

While this is entirely the right direction when doing research, I think anyone who studies mathematics also has the desire to check whether the ground they're standing on is really solid. This blog is part of a hobby activity to satisfy that desire. Therefore, the update speed is very slow.

## Blog Direction

The name "direction" is a bit grandiose; it's just an explanation of the blog content.

### Mathematics Categories

Originally, I intended to divide the mathematics posts in this blog into roughly three parts:

- Mathematics for non-majors (calculus/linear algebra)
- Mathematics for undergraduate math majors (roughly the scope of teacher certification mathematics)
- Mathematics for majors (content from advanced undergraduate to graduate level)

Currently, this direction is not being maintained very well, because the purpose of this blog has changed from explaining to potential readers to finding explanations that satisfy myself.

In particular, I have almost given up on mathematics for non-majors, which I wrote about above. For example, linear algebra was the first content I wrote for this blog, but currently writing posts in the calculus category has been pushed to the bottom of my to-do list. Also, when dealing with any topic, I decided not to distinguish between undergraduate and graduate-level content, and just write until I'm satisfied.

Also, for analysis, I have the idea of organizing content at least up to what is commonly learned upon entering graduate school (e.g., a brief introduction to $L^p$ spaces) if time permits in the future, but since my major is somewhat distant from analysis, I'm not sure when that will be.

Mathematics has aspects where each subfield influences each other, making it very difficult to determine the order in which to read posts. However, assuming we look at the overall flow, the posts on this blog are currently organized in the following order:

- The [Set Theory](/en/set_theory) category literally contains set theory content and requires no knowledge from any other category.
- The [Category Theory](/en/category_theory) category is needed for reading posts from all other categories, especially those on the algebra side. As a result, I tried to minimize mentioning posts from other categories in this category, which made it quite dry. The exception is the [Monoidal Categories](/en/category_theory/monoidal_categories) and [Monoid Objects](/en/category_theory/monoid_objects) posts, where I assumed knowledge of basic definitions of monoids and groups.
- The [Algebraic Structures](/en/algebraic_structures) category roughly corresponds to undergraduate abstract algebra and is divided into four parts: groups, rings, modules, and algebras. The difference from undergraduate content is that it borrows heavily from the language of [Category Theory](/en/category_theory).
- The [Multilinear Algebra](/en/multilinear_algebra) category needs some explanation. Originally, I intended to cover the content corresponding to Chapter 3 of **[Bou2]**, the main reference for the [Algebraic Structures](/en/algebraic_structures) category, but when the algebra content went into the [Algebraic Structures](/en/algebraic_structures) category, there wasn't much left except for introducing tensor algebra and related content. So this category's posts have two goals: raising the posts in the [Linear Algebra](/en/linear_algebra) category to general $A$-modules and introducing tensor algebra content. As a result, the name has become somewhat inappropriate, but I can't think of a better name.
- The [Homological Algebra](/en/homological_algebra) category is where we study homological algebra.
![homology](/assets/images/Pages/About/homology.jpg){:style="width:400px" .align-center}
<cap> Twitter</cap>
- The [Commutative Algebra](/en/commutative_algebra) category does commutative algebra. That is, we examine commutative rings and the module structures defined through them. However, to distinguish fields as clearly as possible, I've put any geometric meanings into the [Algebraic Geometry](/en/algebraic_geometry) category. This part is especially something I have no confidence in writing better than the main reference **[Eis]**, so it's almost in the form of removing geometric intuition from that book.
- The [Topology](/en/topology) category deals with topology, but since the reference is **[Bou3]**, there are also some somewhat unusual contents for undergraduate level. Anyway, since this has happened, I've also included sheaf-related content that is commonly learned in [Algebraic Geometry](/en/algebraic_geometry) here.
- The [Algebraic Topology](/en/algebraic_topology) category hasn't started yet, but since I've already created all the necessary content in the [Homological Algebra](/en/homological_algebra) category, I just need to add geometric flavor to it. Of course, homotopy is also an important topic, so I should also cover that.
- The [Manifolds](/en/manifold) category is literally about manifolds. The main reference for the posts in this category is **[War]**, but the first book I studied this field from was **[Lee2]**, and some parts of that book's explanations are much friendlier, so it seems to be about a 50/50 ratio. I referred to **[Lee2]** to write about Riemannian metric content in the next category, differential geometry.
- The [Differential Geometry](/en/differential_geometry) category, following [Manifolds](/en/manifold), was intended to do Riemannian geometry following **[Lee3]**. However, since my major has become somewhat distant from this field, I'm not sure when it will be updated.
- The [Algebraic Geometry](/en/algebraic_geometry) category uses the tools created in the [Commutative Algebra](/en/commutative_algebra) category to do geometry. This category is placed at the back to build geometric intuition from other categories like [Manifolds](/en/manifold). However, I still haven't decided whether to prioritize geometric intuition or algebraic formalism when writing posts in this category, so the posts in this category are still quite messy.

Analysis-related content will probably be most naturally placed right after [Topology](/en/topology/)-[Algebraic Topology]() is finished, but I'm not sure when that will be.

As mentioned at the beginning, the posts in these categories all heavily reference existing references, which I've also listed at the end of each post, but it seems good to organize them by field as well, so I've summarized them here.

#### Linear Algebra

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.
**[Lee1]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

#### Set Theory

**[Bou1]** N. Bourbaki. *Elements of the History of Mathematics*. Springer, 2013
**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.

#### Category Theory

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

#### Algebraic Structures

**[Bou2]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

#### Multilinear Algebra

**[Bou2]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

#### Homological Algebra

**[Hu]** S.T. Hu, *Introduction to homological algebra*. University Microfilms, 1979.
**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.

#### Commutative Algebra

**[AM]** M.F. Atiyah and I.G. Macdonald, *Introduction to commutative algebra*, Basic Books, 1969.
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

#### Topology

**[Bou3]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

#### Manifolds

**[Lee2]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013

#### Differential Geometry

**[Lee3]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019

#### Algebraic Geometry

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.
**[Vak]** R. Vakil, *The Rising Sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

### Blog Development Log

Categories other than mathematics currently only have a blog development log. In fact, I'm not sure what else to write here. I'm not going to write a diary, after all...

I know nothing about coding, so I had to keep struggling while creating this site. In case someone else encounters similar struggles, I've left it as a record.

## Technical Content

### Operating an English Site

In [Blog Development §Multilingual Support](/en/misc/blog_development/multilingual) we've already prepared to operate this site in both Korean and English. However, the happy imagination that I could just copy-paste the existing $\TeX$ documents into markdown syntax has been shattered, so the English site will probably be dealt with after writing all the basic content that I think "if you're going to study mathematics, you should know this much" in Korean. However, I'm not sure whether that will be faster or my graduate school graduation will be faster.

### Korean-English Terminology

To use Korean terminology as much as possible, I've been diligently translating by looking up the Korean Mathematical Society's [Mathematical Terminology](https://www.kms.or.kr/mathdict/list.html) page, but personally I often feel that Korean terminology doesn't yet capture all the intuition contained in the original text, so I've left these terms untranslated. Especially terminology introduced beyond undergraduate content is almost all like this.

Anyway, I've organized the terminology used in the blog on the [Index](/en/misc/index) page. I also have the idea of slightly revising this in the distant future and organizing it by grouping similar terms together, like this:

| English Term | Korean Term | Definition | Reference |
| --- | --- | --- | --- |
| <unselected id="binary_relation">binary relation</unselected> | <selected> 이항관계 &#9745;</selected> | [Set Theory §Binary Relations](/en/math/set_theory/binary_relation) | |
| <selected class="indented" id="antisymmetric">antisymmetric &#9745;</selected> | <unselected>antisymmetric</unselected> | [Set Theory §Definition of Order Relations](/en/math/set_theory/order_relations) | [Relation](#relation), [Order relation](#order_relation) |
| <selected class="indented" id="asymmetric">asymmetric &#9745;</selected> | <unselected>asymmetric</unselected> | [Set Theory §Definition of Order Relations](/en/math/set_theory/order_relations) | [Order relation](#order_relation) |

But I'm not sure when that will be.

### Miscellaneous

The $\TeX$ version of the files are almost direct copies of the sources, so the notation is all over the place. I've tried to unify them as much as possible, but there are still many incomplete parts.
