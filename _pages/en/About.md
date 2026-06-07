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

I am a graduate student in mathematics, and this blog is where I organize what I have studied. I am not a senior scholar --- at least not as I write this --- so the content is mostly well-known references in each field, retold in Korean in my own words with minor modifications. This is all the more true for the subjects I wrote up *while* studying them rather than after.

The blog's title comes from something a senior once told me: when you do research, do not try to study everything --- decide what to accept as fact, and put the proofs and the like into your own black box. That is exactly the right attitude for research, but I think anyone who does mathematics also wants, now and then, to check that the ground they stand on is really solid. This blog is a hobby in service of that wish, which is also why it is updated very seldom.

## Reading order

Mathematics is interwoven across its subfields, so deciding on a reading order is genuinely hard; on top of that, the logical order and the order that is easiest to learn in do not always agree. In the end I arranged the posts by *logical* order rather than learning order. [Category theory](/en/category_theory/), for instance, sits very early --- nothing else is a prerequisite for it --- even though its real value only shows once you have studied the subjects that use it. This ordering is largely for my own convenience as a writer: once the category theory posts explain what a free functor is, free groups, free algebras, free modules and many other definitions can each be dispatched with a single reference.

So reading the left sidebar straight from top to bottom is logically fine, but I do not recommend it. I would instead suggest opening a page on whatever you are curious about, reading on, and backtracking selectively when you hit something you do not know.

I also write each post by first laying out its overall narrative and then filling in the details from the literature. Roughly since May 2026, however, I have increasingly used LLMs in this part of the process as well; they can hallucinate, but on material I am merely revisiting such slips are easy to catch. A side effect is that posts written after then may carry fragments an LLM picked up during training, so their references can be incomplete. Even so, for someone studying a topic for the first time I believe the references below help far more than an LLM does, so I collect the ones I used here.

<details class="details" markdown="1">
<summary>References by field</summary>

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

#### Riemannian Geometry

**[Lee3]** John M. Lee. *Introduction to Riemannian Manifolds*, Graduate texts in mathematics, Springer, 2019

#### Algebraic Geometry

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

</details>

## Operating an English site

This is, by default, a Korean-language site. Like most people here I learned my mathematics in English, so why write in Korean? Fundamentally, for my own study. Reading English and writing English are easy: it is rare that a single sentence of a proof is, on its own, incomprehensible. But to me, understanding a proof is not understanding it one sentence at a time --- it is following the idea behind it, how and why it starts the way it does. Reading a proof in English and writing it up in Korean is, at the very least, an effort to read the whole proof at once and decide, in my own terms, which parts to emphasize and which I can afford to skim.

Because of that, although the site was set up for bilingual operation long ago, for a long time I did not write a single post in English. Studying has to come before translating; and since the blog only really *means* "study" to me once it reaches the neighborhood of my own research, I barely had the time to run there in a straight line, taking only what I strictly needed along the way.

Fortunately, in the meantime LLMs have developed into a remarkable tool. I cannot leave mathematical content to an LLM without checking it, but I can at least hand a post I have already written to [the LLM that does the chores around here](/en/about-Marvin) and have it translated into English. The current translation pipeline works roughly as follows:

1. If a Korean post exists but has no translation yet, translate it (`Kimi K2.6`).
2. A Python script then compares the number of `$$...$$` math blocks in the original and the translation.
3. If the counts differ, the document is split into parts and the differing parts are compared and reported by `Claude Haiku`.
4. If that report flags anything that needs fixing, the user (me) verifies it directly.
5. When no posts are left to translate, the finished translations are polished, and the error-detection loop above repeats.

A consequence of this is that I do not read every translated post in full. If, for example, the LLM makes two mistakes in step 2 that happen to cancel each other out, the error can slip past me unnoticed. **So please treat the English posts as best-effort, machine-assisted translations that may be incomplete or, occasionally, misleading; wherever an English post and its Korean original disagree, the Korean one is authoritative.** If you do find an error, I would be grateful if you let me know.
