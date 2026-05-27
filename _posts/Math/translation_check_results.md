# Translation Consistency Check Results

Date: 2026-05-27

Checking ko (original) ↔ en (translation) pairs for mathematical content consistency.

---


## Algebraic_Structures: Abelian_Groups
[STATUS: CONSISTENT]
- All 16 labeled items (Theorems 1, 12, 14, 15; Definitions 2, 3, 6, 11, 13, 16; Propositions 4, 5, 7, 8, 9; Example 10) present in both files with matching IDs.
- All LaTeX formulas are identical between KO and EN.
- All proofs (Propositions 4, 9; Theorems 12, 14) are correctly translated.
- Internal cross-references and external links use consistent language prefixes (/ko/ vs /en/).
- Section structure fully matches across both files.
- Note: Korean original has a minor typo "힌玩家朋友" (line 251) which should be "한편"; EN correctly renders this as "Thus" — not a translation issue.


## Algebraic_Structures: Direct_Products
[STATUS: CONSISTENT]
- All mathematical content matches between KO and EN files
- Lemma 1 (Grp is cartesian monoidal category): statement, proof, and all LaTeX formulas identical
- Corollary 2 (product unique up to unique isomorphism): statement and proof match
- Corollary 3 (product of homomorphisms, ker/im preserved): statement, proof, diagram reference, and all LaTeX formulas identical
- Corollary 4 (normal subgroups, quotient group): statement, proof, diagram reference, and the key isomorphism formula identical
- Corollary 5 (subgroup from subgroups): statement and proof match
- Partial Products section: definitions, formulas, and the final isomorphism formula all identical
- Cross-references (lem1, cor2, cor3, cor4, cor5) are correctly mapped
- External links correctly adapted (ko to en paths, anchor slug for limits section)
- References section identical
- No missing content in either direction


## Algebraic_Structures: Field_of_Fractions
[STATUS: CONSISTENT]
- All definitions match: Def 2 (ring of fractions), Def 3 (division ring/field), Def 5 (zero divisor/integral domain), Def 7 (field of fractions), Def 10 (localization), Def 11 (nilpotent/reduced), Def 13 (nilradical).
- All theorems/propositions match: Thm 1, Prop 4, Prop 6, Prop 8, Prop 9, Prop 12, Prop 14.
- All proofs are faithfully translated with identical mathematical reasoning.
- All LaTeX formulas are identical between KO and EN versions.
- No missing content on either side.
- Pre-existing notation issue in both versions: line 85 KO / line 82 EN uses "$x\in \alpha/\gamma$" where "$x=\alpha/\gamma$" was likely intended (Prop 12 proof step 5).


## Algebraic_Structures: Algebraic_Structures
[STATUS: CONSISTENT]
- All 10 definitions (Def 1-10) present in both files with correct translation
- Definition 1 (binary operation/magma), Definition 3 (associative), Definition 4 (commutative), Definition 6 (homomorphism/isomorphism), Definition 8 (submagma), Definition 9 (left/right compatible), Definition 10 (quotient magma): all match
- Example 2 (power set magmas, N-minus) and Example 5 (product magma): both present with identical LaTeX
- Proposition 7 (composition of homomorphisms) with proof: statement and proof match exactly
- All LaTeX formulas are identical between KO and EN (associativity, commutativity, product isomorphism, homomorphism condition, composition proof, im f closure, compatibility conditions, quotient operation)
- Cross-references to Set Theory properly translated with locale path changes (/ko/ to /en/) and Korean titles to English (e.g., §곱집합의 성질 to §Properties of Product Sets, §동치관계 to §Equivalence Relations)
- Diagram image paths identical in both files
- References section matches (Bourbaki Algebra I)
- No missing content detected in either direction


## Algebraic_Structures: Free_Products
[STATUS: CONSISTENT]
- All mathematical content matches between KO and EN versions
- Definitions (Def 2: Free group via universal mapping problem): identical mathematical content
- Corollary 3 (Any group is a homomorphic image of a free group): identical statement and proof
- Proposition 5 (Free product is the coproduct in Grp): identical statement and proof
- Examples 1 and 4: all formulas, computations, and explanations match
- LaTeX formulas are identical across both files (Hom notation, coprod, prod^\ast, aligned equations)
- Construction of free groups (reduced words, X^{-1}, e, concatenation, inverse example x_1x_2^{-1}x_3^2): fully consistent
- Free product construction (3 conditions for reduced words, reduction procedure): fully consistent
- Closing discussion (Hom(Z,G) cong U(G), F(X) as free product of Z): fully consistent
- Cross-references to category theory sections (adjoints, representable functors) properly translated with matching anchors
- Footnote [^1] and reference [Bou] Bourbaki present in both with equivalent content
- Image references (Free_Products-1.png) identical
- Notation consistent: Grp, Set, Hom, coprod, prod^ast used identically


## Algebraic_Structures: Graded_Modules
[STATUS: CONSISTENT]
- All 3 definitions (graded left A-module, graded homomorphism, graded homomorphism of degree i) correctly translated with identical LaTeX formulas.
- Both propositions (Proposition 4: equivalent conditions for graded submodule; Proposition 5: properties of graded A-homomorphism) have matching statements.
- Cross-references to Graded Rings section (Propositions 2, 6, 7) correctly updated with English permalinks.
- No missing content detected in either direction.
- Note: KO section title "등급가군" mapped to generic "Definition" rather than "Graded Modules" in EN, but this is a stylistic choice, not a mathematical inconsistency.


## Algebraic_Structures: Group_Homomorphisms
[STATUS: CONSISTENT]
- All 6 propositions (1-6) and 1 definition (4) present in both files with matching statements and proofs
- All LaTeX formulas are identical between KO and EN
- Cross-references correctly adapted (ko/ → en/ paths)
- Footnote [^1] preserved in both
- Reference [Bou] Bourbaki, Algebra I present in both
- No missing or extraneous mathematical content


## Algebraic_Structures: Change_of_Base_Ring
[STATUS: CONSISTENT]
- All 4 definitions (Definition 1: restriction of scalars, Definition 3: extension of scalars, Definition 4: coextension of scalars) present in both files with matching content.
- Example 2 (forgetful functor from unique ring homomorphism Z->B) matches.
- Lemma 5 (bilinear map Phi between tensor products) with proof: statements and proofs identical.
- Proposition 5 (phi_! dashv phi* adjunction) with full proof: all steps match, including the two diagram references (Change_of_Base_Ring-3.png, Change_of_Base_Ring-4.png).
- Proposition 6 (phi* dashv phi_* adjunction): present in both, with identical concluding remark about commuting with limits and colimits.
- All LaTeX formulas are identical between KO and EN.
- All 5 diagram/image references are consistent (same file paths).
- Footnote [^1] about (A,Z)-bimodule structure is present in both.
- Section titles use "scalar" (KO) vs "Scalars" (EN) -- purely linguistic, no mathematical difference.
- Lemma 5 and Proposition 5 share the number "5" in both versions -- a source numbering quirk, not a translation issue.


## Algebraic_Structures: Algebras
[STATUS: ISSUES FOUND]
- LaTeX discrepancy in Proposition 8 proof: KO has `f(\x_i)^\alpha_i` (incorrect superscript/subscript grouping), EN correctly has `f(\x_i)^{\alpha_i}`. The EN version fixed a LaTeX error present in the KO original.
- Proposition 12 part 4: Both versions state "ideals of A containing 𝔞" when it should be "two-sided ideals of E containing 𝔞" (correspondence theorem for quotient algebras). This is a mathematical error present identically in both KO and EN, not a translation inconsistency.
- All other definitions (1,2,5,7,9,10,11), propositions (3,4,6,8,12), proofs, examples, section structure, and LaTeX formulas are fully consistent between KO and EN.


## Algebraic_Structures: Graded_Rings
[STATUS: ISSUES FOUND]

- **Example 3 (ex3)**: Both Korean and English state "the free ring $F(G)$ generated by $A$". This appears to be an error in the Korean original that was faithfully preserved in the translation. It should likely read "generated by $G$" since $G$ is the given abelian group and $F(G)$ is the free ring on $G$.

- **Proposition 7 (prop7)**: The Korean original states "$A/\mathfrak{a}$ is a graded **ideal**" (등급 아이디얼), which is mathematically incorrect -- the quotient $A/\mathfrak{a}$ is a graded **ring**, not an ideal. The English translation correctly states "graded ring". This is a correction made during translation.

- **Structural consistency**: All definitions (1, 4), propositions (2, 6, 7), examples (3, 5), and proofs are present in both versions. All LaTeX formulas are identical. No content is missing from either side.

## Algebraic_Structures: Modules
[STATUS: CONSISTENT]
- All 6 definitions (Def 1-4, 6, 9) match between KO and EN with correct mathematical content.
- All 3 propositions/theorems (Prop 7, Prop 8, Thm 10) have matching statements and proofs.
- Example 5 (ring as module over itself, ideals as submodules) is fully translated.
- All LaTeX formulas are identical between KO and EN.
- Minor note: EN corrects a LaTeX brace placement typo in the proof of Prop 8. KO has \Hom_{\lMod{A}(u,N)} (brace closed after (u,N)) while EN has \Hom_{\lMod{A}}(u,N) (brace closed after A). EN renders the intended meaning correctly.
- Notation is consistent: \lMod{A}, \rMod{A}, \Hom_A(M,N), \ker u, \im u.
- Section structure matches: definitions, submodules/quotient modules, linear maps, isomorphism theorem.
- Reference [Bou] Bourbaki Algebra I present in both.


## Algebraic_Structures: Quotient_Groups
[STATUS: CONSISTENT]
- All sections match: Normal Subgroups, Cosets (잉여류)
- Definitions 2 (normal subgroup), 3 (right/left coset), 4 (index) all correctly translated with identical LaTeX
- Proposition 1 ([e] is subgroup) and Proposition 5 (Lagrange theorem) match with identical statements and proofs
- Remark 1 on left/right compatibility correctly translated
- All LaTeX formulas verified identical between KO and EN
- Footnote [1] on right coset notation correctly translated
- No missing or extra content in either version


## Algebraic_Structures: Operations_of_Rings
[STATUS: CONSISTENT]
- All 6 labeled items (Proposition 1, Theorem 2, Proposition 3, Proposition 4, Theorem 5, Definition 6) present in both files with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN.
- Cross-references properly adapted (KO /ko/ paths → EN /en/ paths, Korean section names → English section names).
- Proposition 4 uses f,g instead of φ,ψ in both versions (consistent, not a discrepancy).
- No missing content in either version; all three sections (Products, Coproducts, Tensor Products) fully translated.


## Algebraic_Structures: Grothendieck_Groups
[STATUS: CONSISTENT]
- All 7 definitions/propositions/lemmas (Proposition 1, Proposition 2, Lemma 3, Lemma 4, Proposition 5, Definition 6, Definition 7) present in both files with correct mathematical content.
- All proofs are faithfully translated with identical LaTeX formulas and mathematical notation.
- Image references (Grothendieck_Groups-1.png through -4.png) are identical in both versions.
- Reference to [Bou] (Bourbaki) is identical in both versions.
- The EN translation correctly fixes two apparent typos in the KO original:
  - Lemma 4 proof (KO line 166): KO has `[(b+a)]` (single-element pair) where it should be `[(b,a)]` (two-element pair representing the inverse). EN correctly has `[(b,a)]`.
  - Proposition 5 proof (KO line 192): KO has `\bar{f}([(a,b)]) = f(a)-f(a)` which equals zero and is nonsensical. EN correctly has `\bar{f}([(a,b)]) = f(a)-f(b)`.
- No content is missing from either version.

## Algebraic_Structures: Group_Actions
[STATUS: CONSISTENT]
- All 13 definitions (Def 1-6, 10, 12-13), 4 propositions (Prop 7, 9, 11, Theorem 14), 2 corollaries/lemmas (Cor 8, Lemma 15), and 1 example (Ex 3) are present in both files with correct numbering and matching content.
- All LaTeX formulas are identical between KO and EN, including: Hom-set isomorphism, left/right action equalities, opposite magma definition, power set action verification, M-set homomorphism condition, pullback action formula, stabilizer/fixer inclusions and proofs, orbit-stabilizer theorem, Burnside counting lemma (Lemma 15), and all proof chains.
- Internal cross-references (e.g., Proposition 9 referencing Definition 10, Corollary 8 proof used in inner automorphism discussion) are preserved with correct anchor links.
- External cross-references to Set Theory sections (Product of Sets Proposition 4, Examples of Equivalence Relations Proposition 7) and Algebraic Structures sections (Quotient Groups Proposition 5, Algebraic Structures Definition 6) are correctly translated with matching English URLs.
- Diagram image references (Modules-1.png, Modules-2.png) and header image are identical.
- Reference section (Bourbaki Algebra I) is identical.
- No missing content detected in either direction.


## Algebraic_Structures: Operations_of_Modules
[STATUS: CONSISTENT]
- All 9 labeled items (Theorem 1, Proposition 2, Proposition 3, Definition 4, Theorem 5, Theorem 6, Definition 7, Proposition 8, Theorem 9) present in both files with matching ids and content.
- Proof of Theorem 5 present in both files; content and LaTeX formulas match.
- All LaTeX formulas (equations (1), (2), adjunctions, balanced/bilinear definitions, bimodule condition) are identical between KO and EN.
- Section structure matches: Direct Products and Direct Sums, Free Modules, Tensor Products of Modules, Tensor Products of Modules over Commutative Rings.
- Cross-references to Category Theory sections (Limits Proposition 10, Abelian Categories Definitions 1 and 7) correctly adapted to /en/ paths.
- Link to Abelian Groups tensor product section correctly adapted with Korean anchor (#텐서곱) preserved in EN version (line 150) — minor cosmetic issue but functional since the EN post likely uses the same anchor.
- Note: both versions use $$\lMod{R}$$ (line 79 KO / line 78 EN) in the Free Modules section where $$\lMod{A}$$ is likely intended; this is a pre-existing issue in the original, not a translation error.
- No missing content detected in either direction.


## Algebraic_Structures: Restricted_Sums
[STATUS: CONSISTENT]
- All definitions match: Definition 1 (restricted sum, weak direct product), Definition 4 (internal weak direct product)
- All theorems/propositions match: Theorem 2 (universal property with full proof), Proposition 3 (normal subgroup quotient), Proposition 5 (internal weak direct product criterion with full proof)
- No missing content in either direction; all mathematical content is faithfully translated
- All LaTeX formulas are identical between KO and EN (product notations, commutativity conditions, support notation, quotient expressions)
- Mathematical notation is consistent ($\iota_i$, $\pr_i$, $\prod^w$, $\supp$, etc.)
- Minor note: both versions contain what appears to be a pre-existing typo in the surjectivity proof of Proposition 5 where $\iota_i$ is written instead of $\iota$ (line 157 KO / line 153 EN), but this is consistent across both files
- Cross-reference to "Theorem 6" in the remark after Theorem 2 is present in both versions (refers to a subsequent post)


## Algebraic_Structures: Quotient_Rings
[STATUS: CONSISTENT]
- Definition 1 (quotient ring): correctly translated, same LaTeX formulas.
- Proposition 2 (canonical projection and universal property): both parts match in statement and proof; all LaTeX identical.
- Theorem 3 (ring isomorphism theorems, parts 1–4): all four parts match in statement; proof direction matches. No content missing from either side.
- Cross-references (quotient groups, isomorphism theorems) properly localized to /ko/ and /en/ respectively.
- References (Bourbaki) identical.
- NOTE: Both KO (line 74) and EN (line 74) in Theorem 3 part 2 share the same typo — `\ker f` should be `\ker\phi` in the isomorphism `$$S/(S\cap \ker f)$$`. This is an error in the original Korean carried faithfully into the translation; not a translation inconsistency.


## Algebraic_Structures: Isomorphism_Theorems
[STATUS: CONSISTENT]
- All 8 mathematical items match between KO and EN: Lemma 1, Theorem 2, Proposition 3, Lemma 4, Theorem 5, Theorem 6, Theorem 7, Proposition 8
- All LaTeX formulas are identical between the two files
- Cross-references to Set Theory sections are properly translated (e.g., "[집합론] §동치관계의 예시들" -> "[Set Theory] §Examples of Equivalence Relations")
- Proofs for all items that have proofs (Lemma 1, Lemma 4, Theorem 5, Theorem 6, Proposition 8) are faithfully translated
- Section structure matches exactly: 5 sections with identical ordering
- References (Bourbaki) and footnotes are properly translated
- Note: Two pre-existing typos in the KO original are faithfully carried over in EN: (1) in Lemma 4 proof, the text says $$n_1in N336060 but the equation uses 336060n_2$$; (2) in the coequalizer section, $$x\in X$$ and $$x\in g$$ appear where $$x\in G$$ was likely intended. These are not translation errors.


## Algebraic_Topology: Acyclic_Models_Theorem
[STATUS: CONSISTENT]
- All definitions (Definition 1, Definition 2) match between KO and EN with correct translation and identical LaTeX
- Theorem 3 (Acyclic models theorem) statement and proof sketch are faithfully translated; all LaTeX formulas are identical
- Applications section (Kunneth theorem, Eilenberg-Zilber/Alexander-Whitney maps, flip map diagram) is fully consistent
- All 5 image references match between versions
- Notation is consistent throughout (e.g., Ch_{>=0}(A-Mod), Top, mathcal{M})
- Note: both files contain a minor typo x_m instead of x_n in the proof sketch formula (line 102), but this is a pre-existing issue in the original, not a translation error


## Algebraic_Topology: Acyclic_Models_Theorem
[STATUS: CONSISTENT]
- All definitions (Definition 1, Definition 2) match between KO and EN with correct translation and identical LaTeX
- Theorem 3 (Acyclic models theorem) statement and proof sketch are faithfully translated; all LaTeX formulas are identical
- Applications section (Kunneth theorem, Eilenberg-Zilber/Alexander-Whitney maps, flip map diagram) is fully consistent
- All 5 image references match between versions
- Notation is consistent throughout (e.g., Ch_{>=0}(A-Mod), Top, mathcal{M})
- Note: both files contain a minor typo x_m instead of x_n in the proof sketch formula (line 102), but this is a pre-existing issue in the original, not a translation error


## Algebraic_Structures: Groups
[STATUS: CONSISTENT]
- All 8 definitions (Def 1-4, 6, 8, 11, 14) present in both KO and EN with correct translation
- All propositions (5, 9, 13), theorems (7: Eckmann-Hilton), corollaries (10), and lemmas (12: Cancellation law) present in both with matching statements and proofs
- No missing content in either version
- All LaTeX formulas are identical between KO and EN
- Cross-references correctly updated from /ko/ to /en/ paths (representable_functors, monoid_objects, algebraic_structures, functors)
- Images (Groups-1.png, Groups-2.png) referenced identically
- References ([Bou] Bourbaki) and footnotes match
- Minor note: Eckmann-Hilton proof uses "1" instead of "e" for identity in both versions; consistent between KO and EN (appears to be from original source)


## Algebraic_Structures: Rings
[STATUS: CONSISTENT]
- All 5 definitions (ring, ring homomorphism, subring, ideal, maximal ideal) present and correctly translated in both versions.
- All 4 propositions/theorems (Prop 2, Prop 4, Prop 6, Thm 9/Krull) with proofs match in both versions.
- All LaTeX formulas are identical between KO and EN.
- Internal cross-references correctly adapted (ko/ paths → en/ paths).
- Minor note: KO original has a typo "히니민" on the post-Prop 6 discussion (should be "하나만"), but EN correctly translates the intended meaning as "one". This is an original-KO typo, not a translation error.
- No missing content detected in either direction.


## Algebraic_Topology: Cup_Products
[STATUS: CONSISTENT]
- All 6 labeled mathematical objects match (Definition 1, Proposition 2, Proposition 3, Proposition 4, Definition 5, Proposition 6).
- All LaTeX formulas are identical between KO and EN across every displayed equation.
- Proof of Proposition 3 and the informal proof sketches for Propositions 4 and 6 are faithfully translated.
- Section structure is identical: Exterior Product, Definition and Basic Properties, Functoriality, Cap Product, References.
- Image references (Cup_Products-1.png, Cup_Products-2.png, Cup_Products-3.png) are the same in both files.
- The Kronecker pairing formula on the adjunction step (KO line 174 / EN line 170) contains `\lvert\sigma_i\rangle` instead of `\lvert\sigma_i\rvert` in both files, but this is a shared pre-existing typo, not a translation discrepancy.
- No content is missing from either file.

## Algebraic_Varieties: Projective_Varieties
[STATUS: CONSISTENT]
- All 15 definitions (1-15) present in both KO and EN with correct translation
- All propositions/theorems (Prop 5, Thm 7, Prop 9, Prop 10, Prop 14) present with matching statements and proofs
- All examples (11, 13, 16, 17) present in both versions
- LaTeX formulas are identical across both files
- Mathematical notation is consistent throughout
- Minor note: EN file includes "Zarieties" typo in [Sha] reference (matching KO original), but this is a pre-existing issue in the source reference
- No missing content detected in either direction


## Algebraic_Topology: Characteristic_Classes
[STATUS: CONSISTENT]
- All 3 definitions (Def 1: fiber bundle, Def 2: vector bundle, Def 5: Stiefel-Whitney classes) present in both files with matching mathematical content and identical LaTeX formulas.
- All 2 propositions (Prop 4: trivial bundle iff n everywhere linearly independent sections, Prop 6: isomorphic bundles have same SW class) present with matching statements and proofs.
- All 2 examples (Example 3: tautological line bundle over RP^n, Example 7: Gr_2(R^4) cup product computation) faithfully translated with identical LaTeX formulas and geometric reasoning.
- All LaTeX formulas are identical between KO and EN, including: fiber bundle diagram, vector bundle morphism, pullback bundle definition, Whitney sum, Cech cohomology (cochains, differential, H^p), transition functions g_{ij}, SW class axioms (rank, naturality, Whitney product, normalization), Schubert symbol/cycle/class definitions, Omega_lambda sets, infinite Grassmannian direct limit, tautological bundle E(gamma^k_n), and w_i cohomology classes.
- All 5 image references match (Characteristic_Classes-1.png through -5.png).
- Cross-references correctly adapted with /ko/ to /en/ paths (Poincare_duality, cohomology sections).
- Section structure matches: introduction, Vector Bundles, Cech Cohomology, Stiefel-Whitney Classes, Grassmannians, Euler Class (partial).
- Pre-existing typo in both versions: "gemerator" (should be "generator") in the Grassmannians section (KO line 338 / EN line 329). This is a typo in the KO original faithfully carried into the translation.
- EN has expected translation metadata (translated_at, translation_source: kimi-cli).
- No missing content detected in either direction.

## Algebraic_Topology: Homology
[STATUS: CONSISTENT]
- All definitions (1, 3, 7, 13) match between KO and EN with correct translations.
- All propositions (5, 9, 10, 11, 12) have matching statements and proofs.
- All examples (2, 4, 6, 8) are fully translated with no missing content.
- All LaTeX formulas are identical between KO and EN, including formula (1), boundary maps, chain complex computations, and homology results (e.g., H_2(T^2)=Z, H_1(T^2)=Z+Z, H_0(T^2)=Z).
- Cross-references correctly adapted from /ko/ to /en/ paths.
- All image references are identical.
- Footnote [^1] on coefficient rings is present in both versions.
- Minor note: KO original has typo "모른" (should be "모든") in Proposition 11, EN correctly translates as "for all". This is a pre-existing typo in the Korean source, not a translation error.


## Algebraic_Varieties: Rational_Maps
[STATUS: CONSISTENT]
- All 5 definitions (1, 5, 6, 8, 9) match between KO and EN with correct mathematical content
- All 3 propositions (2, 3, 10) have matching statements and proofs
- All 4 examples (4, 7, 11, 12) are fully translated with identical mathematical content
- All LaTeX formulas are identical between the two files
- Mathematical notation is consistent throughout (e.g., K(X), Frac, P^n, A^2, Bl notation)
- Section structure matches: Rational Functions, Rational Maps, Birational Equivalence, Blow-up
- References section is identical
- Note: KO file has a minor typo "regular funcction" (double c) in Definition 1, not a translation issue


## Algebraic_Topology: Homotopy
[STATUS: CONSISTENT]
- All 6 labeled definitions (2, 4, 7, 9, 10, 11) present in both files with correct translation
- All 3 propositions/theorems (1, 3, 6) have matching statements and proofs
- All 3 examples (5, 8, 12) present and mathematically identical
- All LaTeX formulas identical across both files (equation tags, piecewise definitions, simplex decomposition, path product, etc.)
- All internal cross-references properly translated and linked
- External cross-references to other posts correctly localized (e.g. Homological Algebra, Category Theory, Set Theory sections)
- Both files reference the same images (Homotopy-1.png, Homotopy-2.png, Homotopy-3.png)
- No content missing from either side
- Note: Both versions write pi_1(R,x) instead of pi_1(R^n,x) in Example 12; this is a shared content issue, not a translation error


## Algebraic_Topology: Covering_Spaces
[STATUS: CONSISTENT]
- All definitions (Def 2, 3, 5, 8, 9, 10), theorems (Thm 11, 13, 15), propositions (Prop 4), corollaries (Cor 12, 14), and lemmas (Lem 1, 6, 7) are present in both files with matching mathematical statements and proofs.
- All LaTeX formulas are identical between KO and EN.
- Image references and internal cross-references (anchor links) are consistent.
- References section matches (Hat, May, Mun, Tao).
- Two typos in the KO original were correctly fixed in the EN translation: (1) KO line 84 writes $$\\Pi_1(f)$$ where EN correctly writes $$\\Pi_1(p)$$; (2) KO line 242 writes $$X=U\\cap V$$ while the text says "합집합 (union)", EN correctly writes $$X=U\\cup V$$. These are KO-original errors, not translation issues.
- Minor formatting issue in EN: line 225 has mismatched LaTeX delimiters — opens with $$ but closes with single $ in the expression $$p:(E, y)\\rightarrow (B,x)$$. Should be $$...$$.
- No missing content in either direction.


## Algebraic_Topology: Poincare_Duality
[STATUS: CONSISTENT]
- All 15 labeled items match between KO and EN: Definitions 1-4, 10, 12, 14 (x2); Propositions 6, 7; Theorems 9, 11; Lemmas 8, 13; Examples 5, 15.
- All proofs (Lemma 8, Lemma 13) are faithfully translated with identical mathematical reasoning.
- All LaTeX formulas are identical or equivalent between KO and EN.
- Cross-references correctly adapted from /ko/ to /en/ paths.
- All image references (Poincare_Duality-1 through -6.png) are identical in both versions.
- References ([Hat] Hatcher, [May] May) match.
- Minor KO-original typos corrected in EN translation:
  - Lemma 8 (line 198 KO): KO has "$$i>n$$", EN correctly has "$$i>m$$" (m is the manifold dimension defined earlier).
  - Lemma 13 proof (lines 320, 322 KO): KO has "$$H_{n-p}(M;A)$$" twice, EN correctly has "$$H_{m-p}(M;A)$$" consistent with the rest of the paper.
  These are original-KO errors, not translation issues.
- Note: Both versions share duplicate numbering — "Definition 14" labels both "local coefficient system" and "sheaf cohomology". This is a pre-existing issue in the original, not a translation error.
- No content is missing from either direction.


## Algebraic_Varieties: Quasi_Projective_Varieties
[STATUS: CONSISTENT]
- All 4 definitions (def1, def5, def7, def13), 9 propositions (prop2-prop12), and 2 examples (ex6, ex14) are present in both files with matching mathematical content.
- All proofs match in logical structure and LaTeX formulas.
- Minor notation difference: KO file uses a custom macro `\x_i` (e.g., `\x_0`, `\x_1`) in several places (lines 24, 113) while EN uses `x_i` directly. These render identically assuming the macro is defined as `x`.
- Minor punctuation difference: EN line 115 places a period inside the display math `$$...s_1}.$$` while KO does not. Cosmetic only.
- Cross-references to other sections (Affine Varieties, Projective Varieties, Sheaves) are correctly translated with matching English permalinks.
- No missing or extra mathematical content on either side.


## Algebraic_Varieties: Tangent_Spaces_and_Smoothness
[STATUS: CONSISTENT]
- All 5 definitions (Def 1: Zariski tangent space, Def 5: smooth/singular point, Def 9: generic point, Def 11: smooth variety, Def 13: tangent cone) present in both files with matching LaTeX and correct translation.
- All 5 propositions (Prop 2: affine tangent space, Prop 3: dimension via Jacobian, Prop 4: dim T_x >= dim X, Prop 8: Jacobian criterion, Prop 10: existence of smooth points) present with matching statements, proofs, and LaTeX formulas.
- All 5 examples (Ex 6: smooth points, Ex 7: singular points, Ex 12: smooth/singular varieties, Ex 14: nodal tangent cone, Ex 15: cusp tangent cone) present in both files with identical mathematical content.
- LaTeX formulas are identical between KO and EN throughout.
- Cross-references correctly adapted (ko/ vs en/ link paths, all anchor IDs preserved).
- References section identical ([Har], [Sha]).
- No missing content in either direction.


## Algebraic_Varieties: Affine_Varieties
[STATUS: CONSISTENT]
- All 10 definitions (1, 2, 5, 8, 11, 14, 15, 17) match between KO and EN
- All 8 propositions/theorems (4, 6, 7, 9, 10, 12, 16, 18) with statements and proofs match
- Both examples (3, 13) match
- All LaTeX formulas are identical across both versions
- Section structure is identical (Definition of Affine Varieties, Nullstellensatz, Coordinate Rings and Regularity, Morphisms Between Affine Varieties)
- All internal cross-references (anchor IDs) and external links to topology/commutative_algebra/set_theory/category_theory are consistent with /ko/ vs /en/ paths
- References (Har, Sha, Ful) match
- Minor stylistic note: KO uses $$\mathfrak{a}=1$$ while EN uses $$\mathfrak{a}=(1)$$ (ideal notation) — EN is slightly more precise but this is not an error



## Algebraic_Varieties: Grassmannians
[STATUS: ISSUES FOUND]
- Minor dimension-swap inconsistency in the remark after Proposition 4 proof: KO line 79 says the remaining block is $$(n-k) \times k$$, while EN line 78 correctly says $$k \times (n-k)$$. In the matrix A = (I_k | B), B is k × (n-k), so the EN version is mathematically correct and the KO original has a transposed dimension.
- All other definitions (1, 3, 6, 10, 12, 13), examples (2, 9, 11), propositions (4, 5, 7, 8, 14), proofs, LaTeX formulas, and references match exactly between KO and EN.
- Cross-reference links correctly use /ko/ and /en/ prefixes respectively.


## Algebraic_Topology: Cohomology
[STATUS: CONSISTENT]
- All 10 mathematical definitions/theorems/propositions/lemmas/corollaries (Prop 1, Def 2, Prop 3, Thm 4, Thm 5, Prop 6, Def 7, Lemma 8, Thm 9, Cor 10) are present in both versions with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN versions.
- Cross-reference label IDs (prop1, def2, prop3, thm4, thm65, prop6, def7, lem8, thm9, cor10) are consistent across both versions.
- Both versions share two pre-existing broken cross-references: [Definition 2](#thm2) should be #def2, and [Theorem 5](#thm5) should be #thm65. These are bugs in the original KO text carried into EN, not translation errors.
- Minor note: In the Mayer-Vietoris statement, the KO text says "합집합" (union) but the LaTeX formula uses U∩V (intersection) instead of U∪V. The EN version correctly has X=U∪V. This means the EN translation actually fixed a typo present in the KO original.
- The proof of Lemma 8 is complete and mathematically identical in both versions.
- The de Rham cohomology examples (integration computations) are identical in both versions.
- References and footnote are consistent.


## Algebraic_Varieties: Cohomology_of_Projective_Spaces
[STATUS: CONSISTENT]
- Both KO and EN files contain identical mathematical structure: Proposition 1 (Bott), Definition 2 (Euler characteristic), Corollary 3, Proposition 4 (Serre Vanishing), Definition 5 (m-regular), Definition 6 (globally generated), Proposition 7 (Castelnuovo-Mumford Regularity), Example 8, Proposition 9, Proposition 10.
- All LaTeX formulas are identical between KO and EN across every definition, theorem, proposition, corollary, and proof.
- All proofs are fully translated with matching mathematical content and logical steps.
- No missing content detected in either direction.
- Cross-references correctly adjusted for language (ko/ vs en/ paths).
- Minor note: in the proof of Proposition 4, the KO file uses `i_*\mathcal{G}` while EN uses `i_*\mathcal{F}` in the line `H^i(X, \mathcal{F}) = \check{H}^i(\{X \cap U_j\}, \mathcal{F}) = \check{H}^i(\{U_j\}, i_*\mathcal{G}) = H^i(\mathbb{P}^N, i_*\mathcal{G})` — this is a pre-existing issue in the KO original, not a translation error; the EN version correctly uses `\mathcal{F}`/`i_*\mathcal{F}`.

## Algebraic_Varieties: Serre_Duality
[STATUS: CONSISTENT]
- All 5 labeled items (Propositions 1, 2, 4, 5 and Example 3) present in both versions with matching mathematical statements
- All LaTeX formulas are identical between KO and EN
- Cross-references correctly adapted (ko/ to en/ paths, same anchor IDs: prop1, prop2, ex3, prop4, prop5)
- Section structure matches: intro, Serre Duality on Projective Space, Generalizations, Grothendieck Duality, References
- Cup product definition, trace map, dualizing sheaf, relative Serre duality, and Grothendieck duality adjunction all translated faithfully
- Minor translation simplification in EN: KO mentions "cocycle" explicitly in the bilinear map paragraph (line 52), EN omits it — no mathematical content lost
- References ([Har], [Ser]) identical in both


## Algebraic_Varieties: Line_Bundles
[STATUS: CONSISTENT]
- All 8 definitions (def1, def4, def9, def13, def15, def17, def23, def25) present in both files with identical mathematical content.
- All 10 propositions (prop2, prop5, prop6, prop7, prop8, prop10, prop14, prop18, prop19, prop20, prop21, prop26) have matching statements and proofs.
- All 6 examples (ex3, ex11, ex12, ex16, ex22, ex24) present with identical LaTeX formulas.
- LaTeX formulas are identical across both files; notation (Pic, CaCl, Cl, divisor macro, x_i) is consistent.
- Internal cross-references (anchors #def1, #prop2, etc.) match in both versions.
- URL cross-references correctly adapted: /ko/ paths changed to /en/ paths.
- No missing content detected; sections, paragraphs, and proofs are fully preserved.


## Algebraic_Varieties: Divisors
[STATUS: CONSISTENT]
- All 8 definitions (def1, def2, def3, def7, def9, def12, def15, def16) match between KO and EN with accurate translations.
- All 3 propositions with proofs (prop6, prop8, prop14) have matching statements and proofs.
- All 5 examples (ex4, ex5, ex10, ex11, ex13) are present and consistent in both versions.
- LaTeX formulas are identical across both files throughout.
- Internal cross-references use correct language-prefixed paths (/ko/ vs /en/) in each version.
- Minor shared issue: both files reference "[Definition 8]" (def8) when discussing the Cartier analogue of linear equivalence, but no Definition 8 exists (the actual definition of linear equivalence for Weil divisors is Definition 7). This is not a translation inconsistency since both files share the same reference.
- No content is missing from either side beyond language difference.


## Algebraic_Varieties: Linear_Systems
[STATUS: CONSISTENT]
- All definitions (1, 2, 4, 5, 9, 10) match between KO and EN with correct mathematical content
- Proposition 6 matches in both statement and proof sketch
- All examples (3, 7, 8) match with identical LaTeX formulas and mathematical reasoning
- All LaTeX formulas are identical across both versions (binomial coefficients, projectivizations, restriction maps, Veronese embedding, etc.)
- Cross-references are correctly translated (e.g., §인자→§Divisors, §선다발과 벡터다발→§Line Bundles and Vector Bundles, §사영다양체→§Projective Varieties) with matching anchor IDs
- Section structure is identical: intro, Definitions 1-2, Linear Systems on Projective Space, Example 3, quasi-projective discussion, Base Locus, Definitions 4-5, Proposition 6, Examples 7-8, Ample Line Bundles, Definitions 9-10
- Footnote 1 and references ([Har], [Sha]) match
- No missing content in either direction


## Algebraic_Varieties: Sheaf_Cohomology
[STATUS: CONSISTENT]
- All 22 numbered items (definitions, propositions, lemmas, theorem, examples, corollary) present in both files with matching mathematical content.
- All LaTeX formulas are identical between KO and EN versions.
- All proofs translated faithfully: Lemma 9 (injective implies flasque), Lemma 10 (flasque implies Cech-acyclic), Theorem 11 (Leray), Proposition 12 (affine acyclicity), Proposition 14 (Godement sheaf flasque), Proposition 16 (flasque Gamma-acyclic), Proposition 17 (acyclic resolution), Corollary 20 (five-term exact sequence), Proposition 21 (Cech-to-derived functor spectral sequence), Proposition 22 (H^1 = Pic).
- Cross-references correctly remapped from /ko/ to /en/ paths in the EN version.
- Footnote [^1] present in both files with correct content.
- References section identical (Har, Sha, God, Wei).
- EN front matter includes expected extra fields: translated_at, translation_source.
- No missing content or mathematical discrepancies found.


## Algebraic_Varieties: Dimension
[STATUS: CONSISTENT]
- All 14 labels (ex1, prop2, cor3, prop4, prop5, prop6, prop7, ex8, prop9, prop10, def11, prop12, ex13, ex14) match between KO and EN.
- All LaTeX formulas are identical between the two files (equation (*), S(X), codimension formulas, chain inequalities, dimension inequality).
- All proofs are present and correctly translated in both versions.
- Examples 1, 8, 13, 14 have matching mathematical content.
- Definition 11 (finite morphism) is accurately translated.
- Internal cross-references (Proposition 6, Proposition 7) are consistent.
- External cross-references to other posts use correct localized paths (/ko/ vs /en/) and translated section/label names.
- References section is identical in both files.
- No missing or extra content detected.


## Algebraic_Varieties: Chow_Groups
[STATUS: CONSISTENT]
- All 4 definitions (Def 1: algebraic k-cycle, Def 2: principal cycle, Def 3: rational equivalence, Def 5: Chow group) match with correct translation.
- All 7 propositions (Prop 4, 6, 7, 8, 11, 12, 13) have matching statements across KO and EN.
- All 3 examples (Ex 9, 10, 14) match with identical LaTeX formulas.
- LaTeX formulas are identical in both versions (all displayed equations match exactly).
- Mathematical notation is consistent: Cl(X), Pic(X), CH_k(X), Z_k(X), H^BM_{2k}, etc.
- Internal cross-references correctly adapted (KO links to /ko/ paths, EN links to /en/ paths; anchor IDs preserved).
- No missing content on either side; both versions cover the same sections: Chow Groups, Functoriality, Computing Chow Groups, Chow Ring.
- References section identical (Fulton, Hartshorne).


## Algebraic_Varieties: Canonical_Bundle
[STATUS: CONSISTENT]
- All 6 definitions (Def 1-6), 4 propositions (Prop 3, 7, 9, 11, 12), and 4 examples (Ex 4, 8, 10, 13) present in both KO and EN with correct translations.
- All proofs (Prop 3, 11, 12) are fully translated with matching mathematical content.
- LaTeX formulas are identical across both files (differences only in trailing punctuation on displayed equations).
- Internal cross-references correctly adapted (ko ↔ en link paths, Korean anchor names preserved as-is).
- Section structure matches exactly: intro, Vector Bundles and Quasi-Coherent Sheaves, Canonical Bundle, Canonical Bundle of P^n, Adjunction Formula, Blow-up canonical divisor, References.
- No missing or extra content detected.


## Algebraic_Topology: Topological_Manifolds
[STATUS: CONSISTENT]
- All 2 definitions (Def 1: locally Euclidean, Def 2: topological manifold) present in both files with correct translation and identical LaTeX formulas.
- All 3 examples (Ex 3: open submanifold, Ex 4: graph of continuous function, Ex 5: product manifold) present with matching mathematical content and identical LaTeX.
- Proposition 6 (quotient map: second-countable + locally Euclidean implies second countable) with full proof: statement and proof are faithfully translated; all LaTeX formulas identical.
- The half-space formula H^m = {x in R^m | x_m >= 0} is identical in both files.
- The manifold with boundary mention is correctly translated.
- Cross-references correctly adapted from /ko/ to /en/ paths (Topology §Compactness, §Hausdorff Spaces, §Filter Convergence).
- EN front matter includes expected extra fields: translated_at, translation_source, last_polished_at.
- EN corrected two minor issues present in the KO original:
  1. Example 5 (line 84 KO): KO has (x_1, x_1) while EN correctly has (x_1, x_2).
  2. Proposition 6 proof (line 98 KO): KO has (pi^{-1}(U_i)_{i in J} with missing closing parenthesis; EN correctly has (pi^{-1}(U_i))_{i in J}.
- Note: Both versions share a notational inconsistency in Example 4 where U is defined as a subset of R^n but the graph Gamma(f) is written as a subset of R^m x R^k (should be R^n x R^k, or U should be in R^m). This is a pre-existing error in the KO original, faithfully preserved in EN.
- No missing content detected in either direction.

## Algebraic_Varieties: Riemann_Roch_Surfaces
[STATUS: CONSISTENT]
- All 12 labeled items (Definitions 1, 9, 12; Propositions 2, 4, 7, 10; Lemma 3; Corollary 11; Examples 5, 6, 8) present in both KO and EN with matching statements and proofs
- All LaTeX formulas are identical between versions, including: intersection number definition, exact sequence, genus formula, Riemann-Roch formula, Kodaira vanishing, Hodge index theorem, plurigenera definition
- Cross-references use consistent anchors (def1, prop2, lem3, prop4, ex5, ex6, prop7, ex8, def9, prop10, cor11, def12) and correct language-prefixed paths (/ko/ vs /en/)
- References section matches: Hart, BHPV, Huyb
- No missing or extra content detected


## Algebraic_Varieties: Intersection_Product
[STATUS: CONSISTENT]
- All definitions (1, 3, 5, 7), propositions (4, 6, 9, 14), lemma (8), and examples (2, 10-13) present in both KO and EN with matching mathematical content.
- LaTeX formulas are identical across both versions (intersection multiplicity, Tor formula, proper intersection, intersection product, Chow ring, moving lemma formula, deformation construction, all example computations).
- Section structure matches: intro, intersection multiplicity, transverse intersection, intersection product definition, moving lemma, deformation to normal cone, examples, projection formula, references.
- Cross-references correctly adapted from /ko/ to /en/ paths in the English version.
- Proof sketch for Proposition 9 (deformation to normal cone) is fully translated with consistent mathematical content.
- Minor KO-only artifact: Proposition 6 has a dangling "를 정의할 수 있다." sentence fragment at line 100 that does not correspond to any EN text; not a mathematical discrepancy.


## Algebraic_Varieties: Kodaira_Vanishing
[STATUS: CONSISTENT]
- All 6 labeled items (Proposition 1, Proposition 2, Example 3, Definition 4, Proposition 5, Proposition 6) present in both files with matching IDs (prop1, prop2, ex3, def4, prop5, prop6).
- All LaTeX formulas are identical between KO and EN, including: Kodaira vanishing statement, Serre duality proof, projective space cohomology case formula, Riemann-Roch formula (chi, plurigenus computation), Kodaira dimension definition (min and limsup forms), separation of points/tangent vectors conditions, short exact sequences, long exact sequences, and multiplication map.
- Cross-references correctly adapted: KO uses /ko/math/... paths, EN uses /en/math/... paths. All referenced section labels (canonical_bundle#def1, serre_duality#prop2, canonical_bundle#prop7, line_bundles#ex16, cohomology_of_projective_spaces#prop1, cohomology_of_projective_spaces#prop4, riemann_roch_surfaces#prop4, riemann_roch_surfaces#def12, linear_systems#def9) are consistent.
- Minor pre-existing notational issue (not a translation error): In Example 3, both KO and EN use index p in the formula H^p but write i>0 in the surrounding text. This originates in the KO original.
- References section: all three references ([Har], [Laz], [Kod]) match exactly.
- No content missing from either side; paragraph-by-paragraph correspondence is complete.


## Algebraic_Varieties: Riemann_Roch_Theorem
[STATUS: CONSISTENT]
- All mathematical definitions (Definition 1: Riemann-Roch dimension), lemmas (Lemma 2: vanishing of H^i for i>=2), propositions (Proposition 3: Riemann-Roch for curves, Proposition 7: degree-genus formula), and examples (Examples 4, 5, 6, 8) are present in both files with matching content.
- All LaTeX formulas are identical between KO and EN (equations 1-4, Riemann-Roch formula, Euler characteristic formulas, long exact sequence, cokernel computation, degree-genus formula).
- Proofs for Lemma 2, Proposition 3, and Proposition 7 are fully translated with equivalent mathematical content.
- Cross-references correctly route to language-appropriate URLs (/ko/... vs /en/...) with matching anchor IDs (def1, lem2, prop3, ex4, ex5, ex6, prop7, ex8).
- Minor note: both files contain a reference to "Proposition 2" / "명제 2" with link #prop2 (line 155-157), but the actual element is Lemma 2 with id #lem2. This is a pre-existing error in the Korean original, consistently carried over to the English translation.
- Terminology is correctly translated: 보조정리->Lemma, 명제->Proposition, 예시->Example, 증명->Proof.
- The Korean-only annotation "초타원곡선" for hyperelliptic curve is appropriately omitted in the English version.


## Algebraic_Varieties: Bezout_Theorem
[STATUS: CONSISTENT]
- All propositions (1, 3, 4, 5, 6, 8, 9, 10) present in both files with matching statements and proofs
- All examples (2, 7) faithfully translated with identical mathematical content
- All LaTeX formulas are identical between KO and EN
- Cross-references correctly adapted (e.g. §차원 → §Dimension, §교차곱 → §Intersection Product, 내부 앵커 링크 번역 일치)
- Section structure identical: introduction, proof of P^2 case, generalization via Chow ring, applications (Cayley-Bacharach, Pascal, double points), references
- Front matter consistent; EN includes expected translation metadata (translated_at, translation_source)
- No missing or extra content detected

## Category_Theory: Representable_Functors
[STATUS: CONSISTENT]
- All definitions (1, 5, 7) match between KO and EN with correct translation
- All theorems (3 Yoneda, 4 Yoneda) have matching statements and proofs
- Proposition 8 and its proof are faithfully translated
- Examples (2, 6) have equivalent content
- All LaTeX formulas are identical between versions
- No missing content detected in either version
- Section structure matches: Yoneda lemma, Universal Property
- References section preserved


## Category_Theory: Natural_Transformations
[STATUS: CONSISTENT]
- All 4 definitions (natural transformation, equivalence of categories, skeletal category, skeleton) match exactly between KO and EN
- Theorem 5 (equivalence iff fully faithful + essentially surjective) and Corollary 6 (equivalent iff skeletons isomorphic) have matching statements in both versions
- All LaTeX formulas are identical between KO and EN
- Korean subtitle annotations and <em-ko> tags correctly removed in EN translation
- No missing mathematical content in either version
- Minor shared note: both files use \mathcal{F} in Theorem 5 statement where F was defined (cosmetic, not a translation issue)


## Category_Theory: Functors
[STATUS: CONSISTENT]
- All 10 numbered items match between KO and EN: Definition 1, Lemma 2, Example 3, Example 4, Definition 5, Definition 6, Definition 7, Example 8, Definition 9, Definition 10.
- All LaTeX formulas are identical between KO and EN, including the proof of Lemma 2.
- All image references (Functors-1.png through Functors-4.png) match with identical style attributes.
- Cross-links correctly use /ko/ and /en/ prefixes respectively.
- Footnote [^1] about C_bullet being functorial is present in both.
- Korean subscript annotations (함자, 반변함자, 공변함자, 반대 카테고리, 충실, 충만) are correctly omitted in the EN translation.
- Note: Both versions reference $$\mathcal{A}$$ with a prime in Example 8 ("$$\mathcal{A}$$에서의 morphism" / "morphism in $$\mathcal{A}$$") which appears to be a shared typo for $$\mathcal{A}^\op$$, but this is consistent across both languages and not a translation issue.


## Category_Theory: Monoidal_Categories
[STATUS: CONSISTENT]
- All mathematical definitions (Definition 5: Monoidal category, Definition 7: Cartesian category) match between KO and EN with correct translations and identical LaTeX formulas.
- Proposition 8 statement and proof sketch are consistent.
- Example 6 (Set, Grp, Top, R-modules, Vect_k/Ab) fully matches.
- All LaTeX formulas are identical between both files (associator α, unitors λ/ρ, symmetor γ, diagonal Δ, augmentation ε).
- All 9 diagram/image references are identical.
- Symmetric monoidal category and braided monoidal category definitions match.
- Coherence theorem discussion and cartesian monoidal category discussion are consistent.
- Footnote [^1] and references match.
- No missing content in either direction.


## Category_Theory: Categories
[STATUS: CONSISTENT]
- All 8 definitions (1, 4, 5, 6, 7, 9, 10, 11) translated correctly with matching LaTeX
- Proposition 8 (isomorphism implies bimorphism) and its proof translated correctly
- All 4 examples (2, 3, 12, 13) translated with correct content
- All LaTeX formulas are identical between KO and EN
- All category symbols (Set, Mon, Grp, Ab, Ring, Field, lset, rset, lMod, rMod, Vect, FVect, Top, Man, Ch, Set_*, Top_*) consistent
- All cross-references within the post preserved (links point to same anchors)
- Section structure matches: definitions/examples, isomorphisms, End/Aut, category examples
- Reference ([Rie]) preserved
- Note: Both KO and EN contain a reference to [Def 8](#def8) which should likely be [Def 6](#def6) or [Def 7](#def7) since no Definition 8 exists (only Proposition 8). This is a pre-existing issue in the KO original, faithfully reproduced in the translation.


## Category_Theory: Limits
[STATUS: ISSUES FOUND]
- Theorem 9 (정리 9): Korean original has a formula error. Korean states `$$\lim\Hom_\mathcal{A}(A, F-)\cong\lim\Hom_\mathcal{A}(A, F-)$$` (LHS ≅ LHS, trivially true). English translation correctly states `$$\lim\Hom_\mathcal{A}(A, F-)\cong\Hom_\mathcal{A}(A,\lim F)$$`. The English translation fixes the Korean typo.
- Korean line 73: typo "cocomplete categoory" (extra o); English correctly has "cocomplete category".
- Korean line 128: typo "universa; property" (semicolon instead of l); English correctly has "universal property".
- All definitions (1, 2, 3), examples (4, 5, 6, 7, 8), proposition (10), and section structure match between ko and en.
- All LaTeX formulas are identical, except the Theorem 9 statement noted above.
- Footnotes and references match.


## Algebraic_Topology: Computation_of_Homology
[STATUS: CONSISTENT]
- All 7 labeled items match: Definition 1 (relative homology), Theorem 2 (Excision), Definition 3 (good pair), Proposition 4 ($$H_k(X,A)\cong\widetilde{H}_k(X/A)$$), Theorem 5 (simplicial=singular on Δ-complexes), Definition 6 (Eilenberg-Steenrod axioms), Proposition 7 (Mayer-Vietoris)
- All 5 numbered equations (1)-(5) have identical LaTeX in both versions
- All 8 referenced images (Computation_of_Homology-1 through -8) match
- Proof of Theorem 5 (sketch): induction strategy, filtration, long exact sequences all faithfully translated
- Definition 6: all 5 Eilenberg-Steenrod axioms (Homotopy, Excision, Dimension, Additivity, Exactness) match
- Eilenberg-Steenrod uniqueness discussion and coefficient group generalization match
- Cross-references correctly adapted (/ko/ to /en/) with matching anchors (def1, thm2, def3, prop4, thm5, def6, prop7)
- Typo fix in EN: Proposition 7 statement has $$X=U\cup V$$ in EN correcting $$X=U\cap V$$ in KO (KO text says "합집합"/union but formula has \cap; EN correctly uses \cup)
- Both files share a minor LaTeX issue in proof of Thm 5: $$H_{n-1}{\partial\Delta^k,\Lambda}$$ should have parentheses (pre-existing in KO, faithfully reproduced in EN)
- Both files share a typo in the canonical homomorphism list: $$H_\bullet^\Delta(A)\rightarrow H_\bullet^\Delta(A)$$ should be $$H_\bullet^\Delta(A)\rightarrow H_\bullet(A)$$ (pre-existing in KO, faithfully reproduced in EN)
- No missing content in either direction

## Category_Theory: Abelian_Categories
[STATUS: CONSISTENT]
- All 5 definitions (Def 1: Ab-category/additive category, Def 3: abelian category, Def 4: chain complex, Def 5: exact sequence, Def 7: left/right exact functor) present in both files with identical LaTeX formulas.
- Proposition 2 (zero map is additive identity) and its proof match exactly.
- Theorem 8 (Freyd-Mitchell embedding theorem) statement matches exactly.
- Example 6 (short exact sequence) matches exactly.
- All LaTeX formulas are identical between KO and EN versions.
- Section structure matches: Additive category, Abelian category, Chain complex, Freyd-Mitchell embedding theorem.
- Footnote [^1] present in both files with consistent content.
- Minor note: Definition 1 uses $$\Hom_\mathcal{C}(A,B)$$ in both versions (likely should be $$\mathcal{A}$$ instead of $$\mathcal{C}$$), but this is an issue in the original KO, not a translation error.


## Commutative_Algebra: Properties_of_Localization
[STATUS: CONSISTENT]
- All 8 enumerated results (Lemma 1, Proposition 2, Lemma 3, Proposition 4, Proposition 5, Corollary 6, Proposition 7, Corollary 8) present in both versions with matching statements and proofs.
- All LaTeX formulas identical between KO and EN.
- Sections, cross-references, and references fully translated.
- Note: KO file has a pre-existing link bug on line 100 (`#cor3` should be `#lem3`); the EN version correctly uses `#lem3`.


## Category_Theory: Monoid_Objects
[STATUS: CONSISTENT]
- All sections present in both KO and EN: Monoid Objects, Group Objects, Hopf Monoid
- Definitions 1, 3, 5, 6, 7: data, conditions, and diagrams all match
- Examples 2, 4, 8: all examples present and correctly translated
- LaTeX formulas identical throughout (lambda_M, rho_M, mu(eta(1)@m)=m, G->{e}->G composition)
- Image references and widths identical
- Footnotes 1 and 2 both present with correct content
- References (nLab, Riehl) identical
- No missing or extra content detected


## Commutative_Algebra: Localization
[STATUS: ISSUES FOUND]
- All definitions (1, 3, 4, 7, 10), propositions (2, 5, 6, 8), and corollary (9) are present in both files with matching mathematical content.
- All proofs match in content and LaTeX formulas are identical between KO and EN.
- Cross-references are properly adapted (ko → en paths, Korean → English labels).
- **Issue 1 (KO typo):** KO Definition 3 (line 58) says "$$U$$의 원소들의 임의의 곱이 다시 $$S$$에 속하는 것이다" — uses $$U$$ instead of $$S$$. EN correctly says "the product of any elements of $$S$$".
- **Issue 2 (KO broken reference):** KO line 216 references "[명제 7](#prop7)" but should reference "[명제 8](#prop8)" (there is no prop7; the relevant result is Proposition 8). EN correctly says "[Proposition 8](#prop8)".


## Category_Theory: Adjoints
[STATUS: CONSISTENT]
- All 7 sections match between KO and EN (Definition of Adjoint Functors, Unit and Counit, Free and Forgetful Functors, Contravariant Adjoint Functors, Two-Variable Adjoint Functors, Internal Hom, Limits and Adjoints).
- All numbered items match: Definition 1, Example 2, Example 3, Definition 4, Proposition 5, Definition 6, Example 7, Definition 8, Theorem 9.
- All LaTeX formulas are identical between KO and EN.
- Cross-references correctly adapted (ko→en paths, Korean section/example names→English equivalents).
- Image references identical in both files.
- Both files contain the same bare text placeholder "Enriched category / internal hom" (line 87 KO, line 86 EN) — consistent.
- Both files reference [Example 6](#ex6) in the Internal Hom section (should be Example 7 based on the file content) — pre-existing broken link in the original, faithfully carried over; not a translation issue.
- Proposition 5 part 2 types for G(-,C) and H(-,C) appear inconsistent with Definition 6 in both versions — pre-existing issue in the original, not a translation issue.


## Commutative_Algebra: Primary_Decomposition
[STATUS: CONSISTENT]
- All 7 labeled items (Def 1, Prop 2, Thm 3, Def 4, Lemma 5, Lemma 6, Thm 7) present in both KO and EN with matching mathematical content.
- All LaTeX formulas are identical between KO and EN.
- All proofs (Prop 2, Lemma 5, Lemma 6, Thm 3) faithfully translated.
- Cross-references correctly mapped (e.g. KO "§동반소아이디얼, ⁋보조정리 5" → EN "§Associated Primes, ⁋Lemma 5"; KO "§국소화의 성질들, ⁋따름정리 8" → EN "§Properties of Localization, ⁋Corollary 8"; KO "§국소화, ⁋명제 5" → EN "§Localization, ⁋Proposition 5"; KO "[다중선형대수학] §완전열, ⁋명제 7" → EN "[Multilinear Algebra] §Exact Sequences, ⁋Proposition 7").
- Section headings correctly translated: 으뜸부분가군→Primary Submodules, 으뜸분해→Primary Decomposition, 으뜸분해와 인수분해→Primary Decomposition and Factorization.
- Minor typos in KO original ("둘때" should be "둘째" on line 54; "prim" should be "prime" on line 69) but EN translates the intended meaning correctly.
- Both versions share a duplicated anchor fragment `#prop7#prop7` in one link (pre-existing in KO, preserved in EN).
- Empty proof block in Thm 7 is present in both versions (intentionally unwritten).


## Commutative_Algebra: Lying_Over_and_Going_Up
[STATUS: CONSISTENT]
- All propositions (Proposition 1, Lemma 2, Corollary 3, Corollary 4) are present in both files with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN versions.
- Cross-references (Lemma 4, Lemma 8 in Integral Extensions) correctly adapted with /ko/ to /en/ path prefixes.
- HTML IDs (prop1, lem2, cor3, cor4) are consistent across both files.
- References section matches (Eisenbud citation identical).
- Transition paragraph between Proposition 1 and Lemma 2 correctly translated.
- Note: Korean original has a minor typo in Corollary 3 proof (떄 instead of 때) but the English translation is correct and unaffected.


## Commutative_Algebra: Basic_Notions
[STATUS: CONSISTENT]
- All 5 definitions (Def 1: annihilator, Def 2: ACC/DCC/noetherian/artinian, Def 7: finitely presented, Def 8: coherent module, Def 10: prime ideal) present in both files with identical LaTeX formulas.
- All theorems/propositions (Thm 3, Prop 4, Prop 5, Cor 6, Prop 9, Prop 11) present in both with matching statements and proofs.
- Section structure identical: Basic Definitions, Finiteness condition, Prime Ideals, References.
- All LaTeX formulas are identical between KO and EN.
- Internal cross-references correctly adapted (KO /ko/ paths to EN /en/ paths, same anchor IDs).
- Reference [Eis] (Eisenbud) present in both.
- No missing or extra content in either file.
- Minor note: In the proof of Thm 3, Korean text uses "x_0" in one place while the English proof uses "x_1" at the same position, but this is a stylistic choice that does not affect the mathematical argument.


## Commutative_Algebra: Associated_Primes
[STATUS: CONSISTENT]
- All 8 labeled items (Definition 1, Lemma 2, Proposition 3, Corollary 4, Lemma 5, Lemma 6, Theorem 7, Corollary 8) are present in both versions with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN versions.
- Proof of Lemma 2 (Prime avoidance lemma) correctly translated in full.
- Proof of Theorem 7 correctly translated in full, including the argument that Ass(A/p)={p} for any prime ideal p.
- Proof of Corollary 8 correctly translated in full.
- Conventions note (associated primes of an ideal a mean Ass A/a, not Ass a) preserved.
- Introductory/explanatory paragraphs between propositions are all present and correctly translated.
- Cross-references to other posts (Properties of Localization) use correct EN permalinks.
- Reference [Eis] Eisenbud cited in both versions.
- Note: both versions share a minor typo in the proof of Theorem 7 (line 180 KO / line 173 EN) where "\\Ass M \\Ass M_{n-1}" should be "\\Ass M \\subseteq \\Ass M_{n-1}" -- this is not a translation issue.
- Note: Lemma 2 and its proof use "$$R$$" for the ring while the rest of the post uses "$$A$$" -- this notational inconsistency is present in both versions and is not a translation issue.


## Commutative_Algebra: Jordan-Holder_Theorem
[STATUS: CONSISTENT]
- All definitions (1: simple module, 2: composition series/length), theorems (3, 4, 5), and corollaries (6, 7, 8) present in both files with matching mathematical content.
- LaTeX formulas are identical between KO and EN versions.
- Proofs match in both versions.
- Note: Both files share a pre-existing typo "finiely" in Corollary 6 (should be "finitely") and "finite lenngth" in the proof of Theorem 4 (should be "finite length") -- these are in the original Korean source as well.
- EN file at line 109 has a cross-reference anchor link that still uses Korean text: `/en/math/commutative_algebra/basic_notions#기본-정의들` instead of an English anchor. This is a minor internal link issue, not a content discrepancy.


## Commutative_Algebra: Nullstellensatz
[STATUS: ISSUES FOUND]
- **KO line 100 - LaTeX typo**: The Korean file has `\frac{q_1}{1_0}` which should be `\frac{q_1}{q_0}`. The English file correctly has `\frac{q_1}{q_0}` on line 99. This is a mathematical error in the Korean original.
- **EN line 33 - Korean anchor in English cross-reference**: The link to Nakayama's Lemma uses the Korean anchor `#나카야마-보조정리` instead of the corresponding English anchor. This likely results in a broken link on the English site.
- All other content is consistent: Definitions 1-2, Lemma 3 (Rabinowitch), Theorem 4 (Nullstellensatz), Lemma 5, Proposition 6, all proofs, and all LaTeX formulas (aside from the typo noted above) match between KO and EN. Cross-references correctly use language-appropriate base URLs. The bibliography is identical.


## Commutative_Algebra: Blowup_Algebra
[STATUS: ISSUES FOUND]
- Notation inconsistency in Lemma 7 (Artin-Rees) statement: Korean line 135 uses `$$\mathcal{a}$$` (calligraphic a) while English line 123 correctly uses `$$\mathfrak{a}$$` (fraktur a). The rest of both files consistently uses `\mathfrak{a}`, so the Korean line is a typo.
- Both files share two mathematical errors (not translation issues): (1) Proposition 4 statement says `\gr_\mathcal{J}A` but should say `\gr_\mathcal{J}M` based on the proof; (2) Corollary 11 proof uses `\initial(x)` and `\initial(y)` but should use `\initial(a)` and `\initial(b)`.
- All definitions (1, 3, 5, 9), propositions/lemmas (2, 4, 6, 7), corollaries (8, 11), and Example 10 are correctly and fully translated with matching LaTeX formulas and proofs.


## Commutative_Algebra: Flatness
[STATUS: CONSISTENT]
- All mathematical content present in both files: Proposition 1, Corollary 2, Corollary 3, Lemma 4, Corollary 5, Corollary 6, Corollary 7, each with proofs
- All LaTeX formulas are identical between KO and EN
- Internal links properly adapted from /ko/ to /en/ paths
- Image references consistent (Flatness.png, Flatness-1.png)
- Reference to [Eis] David Eisenbud present in both
- No missing or extra content detected in either version


## Commutative_Algebra: Differentials
[STATUS: CONSISTENT]
- All 6 labeled items (Definitions 1, 3; Lemma 2; Propositions 4, 5, 6) present in both files with matching IDs
- All LaTeX formulas identical between KO and EN
- Proofs match (Prop 4 proof present in both, Prop 5 proof empty in both)
- Cross-references properly localized (KO vs EN paths and labels)
- Images reference same files with identical styling
- Section structure identical in both versions
- No missing or extra content detected


## Commutative_Algebra: Localization_of_Graded_Rings
[STATUS: CONSISTENT]
- All 8 labeled items (Definition 1, Lemma 2, Proposition 3, Proposition 4, Definition 5, Proposition 6, Proposition 7, Proposition 8) present in both files with matching mathematical statements and proofs.
- All LaTeX formulas identical between KO and EN.
- Cross-references to external sections correctly translated (section names, anchor links).
- HTML tag <em-ko> correctly converted to <em> in EN.
- Minor KO-original issue (not a translation error): Lemma 2 statement in KO line 52 has duplicated text "다음이 성립한다. 다음이 성립한다."; EN correctly translates this only once as "Then the following hold."
- Pre-existing content issue in both files: text before Lemma 2 references "Lemma 1" / "보조정리 1" with anchor #lem1, but the actual displayed lemma is labeled Lemma 2 (id=lem2). This is a numbering inconsistency in the Korean original, faithfully preserved in the translation.


## Commutative_Algebra: Completion
[STATUS: CONSISTENT]
- All 3 sections (Definition of Completion, a-adic Topology, Basic Properties) present in both files with matching structure.
- Definitions 1, 2, 3: all mathematical content correctly translated; tags (def1, def2, def3) match.
- Example 4 (formal power series K[[x]]): present in both with identical LaTeX.
- Proposition 5, Corollary 6, Proposition 7: statements and proofs match in both files; tags (prop5, cor6, prop7) match.
- All LaTeX formulas are identical between KO and EN (inverse limit, isomorphisms, graded ring, series representations, degree calculations).
- Tagged equations (1), (2), (3), (4) match in both files.
- Universal property diagram image reference identical in both.
- References ([AM], [Eis]) match.
- Minor: KO has typo "neighoborhood" (line 88), EN correctly spells "neighborhood" (line 85) - EN version is an improvement.
- No missing content in either direction.


## Commutative_Algebra: Krull_Dimension
[STATUS: CONSISTENT]
- All definitions (1, 2, 5, 9, 12) present in both files with matching content and LaTeX formulas
- All theorems/propositions (Cor 3, Prop 4, Thm 6, Thm 7, Cor 8, Prop 10, Prop 11) have matching statements and proofs
- Section structure identical: Definition of Dimension, Computation of Dimension, Dimension in Graded Rings, Regular Local Rings
- All cross-references correctly translated with proper ko/en URL paths
- References ([Eis], [Nag]) consistent
- No missing content detected in either direction


## Commutative_Algebra: Properties_of_Completion
[STATUS: ISSUES FOUND]
- All 8 labeled results (Theorem 1, Lemma 2, Lemma 3, Theorem 4, Theorem 5, Corollary 6, Theorem 7, Theorem 8) present in both files with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN.
- All section structure and narrative flow consistent.
- ISSUE 1: In the proof of Theorem 4 (KO line 113), the notation "$$\widehat{a}$$" (plain lowercase a) is used where "$$\widehat{\mathfrak{a}}$$" (mathfrak a) is intended. The EN version (line 112) correctly uses "$$\widehat{\mathfrak{a}}$$". This is a typo in the KO source.
- ISSUE 2: In Theorem 8 (KO line 231), "noethherian" is misspelled (double h). The EN version correctly spells "Noetherian".
- Note: Both issues are in the KO source; the EN translation corrected them.

## Commutative_Algebra: Integral_Extension
[STATUS: ISSUES FOUND]
- **Theorem 1 (Cayley-Hamilton)**: KO states the result as a biconditional ("동치이다", meaning "is equivalent to"), while EN states it only as a forward implication ("there exists... such that"). The EN omits the "if and only if" framing present in the KO.
- **Lemma 5**: Both KO and EN use "R-submodule" (N의 R-submodule) when the ring throughout the article is A, not R. This is a consistent typo in the original KO that the EN faithfully reproduces.
- **Lemma 7 proof**: Both versions contain LaTeX typo `\cdots_p_n` where it should be `\cdots+p_n` (missing plus sign). Consistent in both.
- **Lemma 8 (Nakayama) proof, part 2**: Both versions write "N/IN=0" when it should be "N/aN=0" (using the ideal a from the theorem, not an unspecified I). Consistent typo.
- **Duplicate Proposition 15**: Both KO and EN have two distinct propositions labeled as "Proposition 15" with the same id="prop15". The second one (about integral over phi iff integral at all localizations) should be renumbered to Proposition 16.
- **Second Proposition 15 statement**: Both versions say "image of x in A_p" when x is an element of E, so it should be "image of x in E_p". Consistent error in both.
- **Second Proposition 15 proof**: Both versions reference "Lemma 14" / "보조정리 14" which does not exist as a label; the referenced result is Proposition 14 (prop14). Consistent wrong reference.
- All other definitions (Def 3: extension, integral, integral closure, normalization, normal domain, finite, finite type), theorems, propositions, corollaries, proofs, LaTeX formulas, section structure, and references match faithfully between KO and EN.
- No content is missing from either version.


## Commutative_Algebra: System_of_Parameters
[STATUS: CONSISTENT]
- All definitions (Proposition--Definition 3: system of parameters, parameter ideal, general module definition) are faithfully translated.
- All theorems/propositions (Corollary 1, Proposition 2, Proposition--Definition 3, Lemma 4, Lemma 5, Proposition 5, Corollary 6, Lemma 8, Theorem 9, Corollary 10, Corollary 11) have matching statements and proofs in both versions.
- All LaTeX formulas are identical between KO and EN.
- Section "평탄사상과 차원" correctly translated as "Flat Morphisms and Dimension".
- Internal cross-references and links correctly adapted (/ko/ to /en/).
- Theorem/proposition numbering is consistent (cor1, prop2, prop-def3, lem4, lem5, prop5, cor6, lem8, thm9, cor10, cor11).
- References section matches.
- Pre-existing issues present in both versions (not translation errors): (1) Corollary 1 has a typo "$$a_1,\\ldots, a\\in \\mathfrak{m}$$" missing the subscript d on the last element; (2) Corollary 6 proof references "Proposition 6" (#prop6) but the proposition is labeled as Proposition 5 (#prop5); (3) Theorem 9 statement says $$\\dim A/\\mathfrak{m}$$ but the proof uses $$e=\\dim B/\\mathfrak{m}B$$, suggesting the statement should read $$\\dim B/\\mathfrak{m}B$$.


## Commutative_Algebra: Fractional_Ideals
[STATUS: CONSISTENT]
- All 3 definitions (Def 1: invertible module, Def 2: fractional ideal, Def 5: Picard group / Cartier divisor) are correctly translated.
- All 2 theorems (Thm 3: 4-part characterization, Thm 4: Pic(R)=0 for UFD) and 1 corollary (Cor 6: surjectivity and free abelian group) have matching statements and proofs.
- All LaTeX formulas are identical between KO and EN (trace map, fractional ideal product, X^{-1} notation, intersection formula in Thm 4 proof).
- Internal cross-references properly adapted from ko/ to en/ paths.
- Mathematical notation (Hom, tensor, Pic, CaDiv, subscripts for localization) is consistent throughout.
- Minor: two Korean typos in the original KO file (not translation issues): "maximal idlal" (line 32, should be "ideal"), "free A_p-moule" (line 99, should be "module").


## Commutative_Algebra: Local_Criterion_for_Flatness
[STATUS: CONSISTENT]
- All mathematical definitions (Definition 4: Rees algebra, extended Rees algebra) match between KO and EN.
- Theorem 1 (local criterion for flatness): statement and proof fully consistent; all LaTeX formulas identical.
- Lemma 2: statement and proof fully consistent.
- Corollary 3: statement and proof fully consistent.
- Proposition 5: statement consistent in both versions (no proof given in either, as noted as "almost obvious").
- Section heading "Rees algebra" present in both.
- Cross-references correctly updated (e.g., §평탄성 → §Flatness, §부풀림 대수 → §Blowup Algebra, §조르단-횔더 정리 → §Jordan-Hölder Theorem) with correct /en/ paths.
- Both files share the same typo in the intermediate formula: A/(x) instead of A/(a) in the tensor product identity between Theorem 1 and Lemma 2 (KO line 106, EN line 105). This is a pre-existing typo in the Korean original faithfully preserved in translation.
- Both files share the notation inconsistency where I appears instead of mathfrak{a} in the Tor long exact sequence argument (KO line 76, EN line 75). Also a pre-existing issue in the original.
- No content is missing from either side; both files end at the same point after Proposition 5.


## Commutative_Algebra: Regular_Local_Rings
[STATUS: CONSISTENT]
- All 12 mathematical items (Corollary 1, Definition 2, Corollary 3, Proposition 4, Proposition 5, Proposition 6, Definition 6, Proposition 7, Theorem 8, Definition 9, Theorem 10) present in both KO and EN with matching statements and proofs.
- Three section headings translated correctly: Regular Local Rings, Discrete Valuation Rings, Serres Normality Criterion.
- All LaTeX formulas are identical between the two versions (set inclusions, dimension equalities, valuation definitions, inverse ideal computations, etc.).
- Internal cross-references (#cor1, #def2, #cor3, #prop4, #prop5, #prop6, #def6, #prop7, #thm8, #def9, #thm10) match in both files.
- External cross-reference links correctly redirect from /ko/ to /en/ paths.
- Notation consistent throughout: Frac(A), codim, dim, ann, mathematical calligraphic/fraktur fonts.
- Reference [Eis] (Eisenbud) present in both.
- Minor pre-existing typo in KO source: "noethereian" in Proposition 5 (corrected to "Noetherian" in EN translation — acceptable).
- Minor pre-existing inconsistency in both files: proof of Theorem 10 uses "$R$" instead of "$A$" for the reduced ring check — not a translation issue.


## Field_Theory: Algebraic_Extensions
[STATUS: CONSISTENT]
- All definitions (1, 4, 7, 9, 14, 16) match between KO and EN with correct translations.
- All propositions (2, 3, 5, 6, 8, 10, 11, 12, 13, 17, 19) and theorems (15, 18) have matching statements.
- All proofs are present and faithfully translated.
- All LaTeX formulas are identical or equivalent.
- The EN version corrects two minor LaTeX issues from the KO original:
  (1) In Prop 8 proof part 2: "L_1 otimes mathbb{K} L_2" (missing subscript) corrected to "L_1 otimes_mathbb{K} L_2".
  (2) In Prop 11 statement: "mathbb{L}_1 = Frac(E_i)" (wrong subscript) corrected to "mathbb{L}_i = Frac(E_i)".
- The typo "homomorpihsm" in Remark 1 is preserved consistently in both versions.
- No content is missing from either side.


## Field_Theory: Fields
[STATUS: CONSISTENT]
- All 19 numbered items (Def 1, Prop 2, Ex 3, Thm 4, Cor 5-6, Def 7, Prop 8, Lem 9, Thm 10, Def 11, Prop 12, Def 13-14, Thm 15, Prop 16, Def 17, Prop 18-19) present in both KO and EN with correct label translations (정의/Definition, 명제/Proposition, 정리/Theorem, 따름정리/Corollary, 보조정리/Lemma, 예시/Example).
- All LaTeX formulas are identical between KO and EN.
- All proofs/sketches are fully translated.
- Cross-references updated correctly from /ko/ to /en/ paths.
- Section titles translated: 소체/Prime Fields, 표수/Characteristic, 완전환/Perfect Rings.
- Notation consistent ($$\mathbb{K}$$, $$\Ring$$, $$\Field$$, $$\Frac$$, $$\Frob_p$$, $$\ch$$, $$\im$$, $$\varinjlim$$).
- No missing content detected in either direction.


## Field_Theory: Algebraically_Closed_Extensions
[STATUS: CONSISTENT]
- All definitions (2, 6, 9), propositions (1, 3, 4, 7, 8, 10, 11), and theorem (5) are present in both KO and EN with matching statements and proofs.
- No content is missing from either side.
- LaTeX formulas are identical in both versions.
- Mathematical notation is consistent throughout.
- Both files share the same pre-existing typos from the original: \matbb{K} instead of \mathbb{K} in proof of Prop 1, and $$\mathbb{2}$$ instead of $$\mathbb{K}$$ in the final paragraph. These are faithfully preserved in the translation.


## Field_Theory: Separable_Degree
[STATUS: CONSISTENT]
- All 10 mathematical items (Lemma 1, Proposition 2, Corollary 3, Corollary 4, Proposition 5, Theorem 6, Definition 7, Proposition 8, Proposition 9, Proposition 10) are present in both KO and EN with matching anchor IDs.
- All LaTeX formulas are identical between the two versions.
- All proofs are faithfully translated; mathematical reasoning is preserved.
- Internal cross-reference paths correctly use /ko/ in KO and /en/ in EN.
- Sidebar nav metadata correctly distinguishes field_theory-ko vs field_theory-en.
- Note: KO original contains minor typos (line 164 "성랍한다" should be "성립한다", line 171 "결쟁된다" should be "결정된다"), but these are in the source, not translation errors.


## Field_Theory: Separable_Extensions
[STATUS: ISSUES FOUND]
- KO line 91: "ddd$$0$$" typo, should be "ist $$0$$" (correct in EN as "and hence is $$0$$")
- KO line 248: LaTeX error "ldots" missing backslash, should be "\ldots" (correct in EN)
- KO line 250: LaTeX error "ldots" missing backslash, should be "\ldots" (correct in EN)
- KO line 321: "$\mathbb{K4}$" typo, should be "$\mathbb{K}$" (correct in EN)
- All 16 mathematical items (lemmas, theorems, propositions, definitions, example) present in both files with matching content
- All LaTeX formulas otherwise identical between KO and EN
- All cross-references and internal links consistent in both versions


## Field_Theory: Fundamental_Theorem_of_Galois_Theory
[STATUS: CONSISTENT]
- Theorem 1 (Galois correspondence): Statement and LaTeX formulas identical between KO and EN.
- Lemma 2 (closed subgroup well-definedness): Statement and LaTeX formulas identical between KO and EN.
- Both proof sections are empty in both languages (consistent).
- Front matter correctly adapted (title, excerpt, permalink, sidebar nav, translation metadata).
- No missing or extra content in either version.

## Field_Theory: Radical_Extensions
[STATUS: CONSISTENT]
- All 10 content blocks (Remark, Definitions 1/4, Propositions 2/5/6/8, Lemma 3, Corollary 7, Example 9) present in both files with matching structure.
- LaTeX formulas are identical across both files (polynomial expressions, field notation, set-builder notation, cross-reference formulas).
- Cross-references correctly adapted: internal anchors preserved (e.g. #def1, #prop2), external links adapted with /ko/ and /en/ path prefixes and translated section/theorem names.
- Mathematical terminology correctly translated: 정의/Definition, 명제/Proposition, 보조정리/Lemma, 따름정리/Corollary, 참고/Remark, 예시/Example, 증명/Proof.
- HTML tags correctly adapted (e.g. <em-ko>모든</em-ko> in KO becomes *all* markdown italics in EN).
- Empty proof block in Lemma 3 and empty statement in Proposition 8 are consistently empty in both files.


## Field_Theory: Properties_of_Galois_Extensions
[STATUS: ISSUES FOUND]
- Both KO and EN contain the same typo in the LaTeX for Proposition 5 proof: `\Gal9\mathbb{L}_i/\mathbb{K})` should be `\Gal(\mathbb{L}_i/\mathbb{K})` (digit 9 instead of opening parenthesis). This is a source error carried into the translation.
- KO has a typo: `contunuous` (line 157) should be `continuous`; the EN version correctly uses `continuous`.
- KO has a typo: `충분하미` (line 176) should be `충분하며`; the EN version renders this correctly as "it suffices to show that".
- In both KO and EN, Proposition 3 proof contains `\mathbb{M}\mathbb{K}(x)` which appears to be missing an operator (likely `\mathbb{M}:=\mathbb{K}(x)` or `\mathbb{M}=\mathbb{K}(x)`). This is a shared source error.
- All definitions (local base, U_M(sigma), subspace topology, totally disconnected), theorems (Props 2-5), examples (Ex 1), and proofs are present in both versions with consistent mathematical content and matching LaTeX formulas.
- Section structure matches: Topological Structure of Galois Groups / Galois Cohomology (cohomology section is empty in both).
- All cross-references to other posts correctly use /en/ paths in the EN version.


## Group_Theory: Extensions
[STATUS: CONSISTENT]
- All 6 definitions (Def 1-6) present in both files with matching mathematical content
- Proposition 4 (three equivalent conditions for trivial extension): statements and proof match
- Proposition 7 (semi-direct product yields trivial extension): statements match
- Corollary 8 (internal semi-direct product isomorphism): statement and proof match
- LaTeX formulas are identical between KO and EN throughout
- All cross-references (Set Theory retractions/sections, Algebraic Structures group actions) correctly adapted with /en/ paths
- Section headings accurately translated: 군의 확장→Group Extensions, 군의 반직접곱→Semidirect Products of Groups
- Note: both files share a likely typo in Def 6 semi-direct product formula $(x_1,y_1)(x_2,y_2)=(x_1\tau(y_1)(x_1), y_1y_2)$ where the second $x_1$ should presumably be $x_2$; this is a shared original error, not a translation discrepancy
- Note: both files share a missing opening parenthesis in the inverse formula for semi-direct product elements; again consistent between versions


## Group_Theory: Sylow_Theorems
[STATUS: CONSISTENT]
- All definitions (1, 5), lemmas (2, 6), theorems (3, 7, 8), propositions (4), corollaries (9-12), and example (13) are present in both files with matching IDs and consistent mathematical content.
- All LaTeX formulas are identical between KO and EN versions.
- Cross-references to other posts (Group Actions, Series of Groups, Isomorphism Theorems) are correctly translated with matching anchor IDs.
- Noted: KO original has a typo on line 102 — "$$p\not\\mid p$$" should be "$$p\not\\mid m$$". The EN version correctly has "$$p\\nmid m$$". This is a pre-existing bug in the KO source, not a translation error.
- Noted: Both versions use undefined notation "$$N$$" in the proof of Corollary 9 (line 218 KO / line 217 EN) where it should presumably be $$N_G(P)$$. This inconsistency exists in both versions identically.


## Homological_Algebra: Diagram_Chasing
[STATUS: CONSISTENT]
- Both files contain identical mathematical content: Proposition 1 (Four Lemma), Corollary 2 (Five Lemma), Corollary 3 (Short Five Lemma), Lemma 4, Lemma 5, Theorem 6 (Snake Lemma), Corollary 7 (3x3 Lemma).
- All proposition/theorem/corollary statements are correctly translated with matching mathematical meaning.
- All proofs are fully translated with identical LaTeX formulas and matching logical steps.
- Image references are identical between both files.
- Notation is consistent (e.g., surjective/injective/isomorphism correctly mapped from Korean terms).
- Reference to [Hu] is present in both files.
- Note: Both KO and EN versions contain the same typo in the Snake Lemma proof well-definedness step where a_1 should be a_prime. This is a pre-existing error in the original KO, faithfully carried into EN, not a translation issue.

## Commutative_Algebra: Noether_Normalization
[STATUS: CONSISTENT]
- All 3 labeled items (Theorem 1: Noether normalization lemma, Lemma 2, Theorem 3) present in both KO and EN with matching IDs (thm1, lem2, thm3).
- All LaTeX formulas are identical between KO and EN, including: inequality chains, ideal chains, polynomial ring constructions, intersection conditions, dimension arguments, and all displayed equations in the proof.
- Full proof of Theorem 1 faithfully translated with identical mathematical reasoning and all steps preserved.
- Cross-reference to System of Parameters correctly adapted (KO /ko/math/commutative_algebra/system_of_parameters#cor10 → EN /en/math/commutative_algebra/system_of_parameters#cor10).
- Internal anchor references ([정리 1](#thm1), [보조정리 2](#lem2]) correctly mapped to ([Theorem 1](#thm1), [Lemma 2](#lem2)).
- Section structure matches: introduction, Theorem 1, Lemma 2, Proof, Consequences, Theorem 3.
- EN front matter includes expected translation metadata (translated_at, translation_source: kimi-cli).
- No missing content detected in either direction.

## Group_Theory: Symmetric_Groups
[STATUS: CONSISTENT]
- All definitions (1, 3, 9, 11, 12) correctly translated with matching mathematical content.
- All propositions/theorems/corollaries/lemmas (4, 5, 6, 7, 8, 10) have matching statements and proofs.
- Examples 2 (S3 composition) and 13 (A5 is simple) faithfully translated.
- All LaTeX formulas are identical between KO and EN.
- Section structure (Symmetric Groups, Alternating Groups) and numbering consistent.
- Reference ([DF] Dummit and Foote) preserved.
- Note: Both versions share the same apparent typo in the cycle construction paragraph where $\sigma^{k_2-k_1}(1)=0$ should likely be $\sigma^{k_2-k_1}(1)=1$. This is an issue in the original KO text, faithfully preserved in EN.


## Homological_Algebra: Long_Exact_Sequence
[STATUS: CONSISTENT]
- All sections match between KO and EN: introduction, Theorem 1 with proof, Proposition 2, Definitions 3-5, Proposition 6 with proof, Lemma 7, Homotopy category discussion, Definition 8, and Corollary 9.
- All LaTeX formulas are identical between KO and EN (including shared typos in the proof of Proposition 6: `g_n(b)` should be `g_n(a)`, and extra closing parenthesis in `d_{n+1}^D)(h_n(a))`; also the mapping cone long exact sequence uses `H_n(B)` and `H_n(C)` instead of `H_n(D)` and `H_n(C)`, but this is consistent across both versions).
- All definitions (3, 4, 5, 8), theorems (1), propositions (2, 6), lemma (7), and corollary (9) are present in both versions with matching mathematical content.
- Both Proposition 2 proofs are empty in both versions (consistent).
- Reference section (Weibel) is identical in both.
- Footnote about quasi-isomorphism terminology is correctly adapted in the EN version.
- Mathematical notation (chain complexes, homology groups, connecting maps, mapping cone) is fully consistent.


## Homological_Algebra: Derived_Functors
[STATUS: CONSISTENT]
- All 9 numbered items (Definitions 1-4, 9; Lemmas 5-7; Proposition 8) present in both KO and EN with matching mathematical content.
- All LaTeX formulas are identical between the two versions.
- Cross-references properly localized (ko/ vs en/ paths, e.g. resolutions and hom_and_tensor links).
- Section structure matches exactly: delta-functor definitions (1-3), derived functor philosophy, Lemma 5 (well-definedness), Lemma 6 (additivity), Lemma 7 (delta-functor property), Proposition 8 (universality), Definition 4 (left derived), Definition 9 (right derived).
- Image references (Derived_Functors-1.png, -2.png, -3.png) identical in both.
- Minor note (not a translation issue): both versions write H_i(F(P)) in the L_0F(A) calculation where H_0(F(P)) would be more precise, but this is consistent across both files.


## Homological_Algebra: Resolutions
[STATUS: CONSISTENT]
- All 7 numbered items (Definition 1, Definition 2, Proposition 3, Proposition 4, Proposition 5, Theorem 6, Lemma 7) present in both files with matching mathematical content.
- All LaTeX formulas identical between KO and EN.
- All images referenced with same paths in both versions.
- Cross-references correctly adapted from /ko/ to /en/ paths.
- Proofs of Proposition 3, Proposition 4, Proposition 5, and Lemma 7 translated faithfully; proof of Theorem 6 empty in both (consistent).
- Minor stylistic note: Lemma 7 statement in KO says "exact sequence" while EN says "short exact sequence" -- EN is slightly more precise but no content discrepancy since the formula 0 to P to 0 makes it unambiguous.
- Notation consistent: \lMod{A}, \mathcal{A}^\op, \Hom_\Ab, \Ab all match.


## Commutative_Algebra: Divisors
[STATUS: ISSUES FOUND]
- Proof of Theorem 17 (well-definedness of Phi): KO version has mathematical error using `\subsetneq` on lines 190-191 where EN correctly uses `\not\subseteq` (first case: if a is NOT contained in p, then aA_p contains a unit) and `\subseteq` (second case: if a IS contained in p, then pA_p is a minimal prime containing aA_p). The KO `\subsetneq` in the first case is mathematically incorrect since proper containment would not yield a unit in the localization.
- Both files have a broken internal reference to [Theorem 11](#thm11) in the Krull-Akizuki section header, but no Theorem 11 is defined in this file (likely defined in a separate fractional ideals post). This is consistent between KO and EN.
- Both files have an incomplete sentence fragment "Meanwhile Phi" / "한편 Phi" in the Dimension and Normalization section (KO line 230, EN line 227). Consistent.
- All definitions (1, 3, 11, 13, 16, 18, 19), theorems/propositions (2, Cor 4, 12, 14, 15, 17, 20, Lemma 21), and their proofs otherwise match in mathematical content. LaTeX formulas are identical aside from the one notation issue above. Korean terminology labels (subscript annotations) are all properly translated.


## Homological_Algebra: Homology
[STATUS: CONSISTENT]
- All 5 definitions (Def 1: chain map, Def 2: n-cycle/n-boundary/n-th homology, Def 4: double complex, Def 5: total complex) present in both files with identical LaTeX formulas
- Proposition 3 (H_n is a functor) present in both with matching statement and proof
- All LaTeX formulas identical between KO and EN (chain map condition, ker/coker constructions, homology definition, total complex differential, d^2=0 verification, translation formulas, truncation definitions)
- All image references (Homology-1 through Homology-9.png) match between files
- All 3 footnotes present in both with consistent mathematical content
- Cross-references correctly adapted (ko/ vs en/ paths)
- References ([Wei], [Hu]) identical
- EN front matter includes expected translated_at and translation_source metadata
- No content missing from either side


## Group_Theory: Series_of_Groups
[STATUS: CONSISTENT]
- All 17 labeled items (definitions, propositions, lemmas, theorems) present in both files with matching IDs.
- All LaTeX formulas identical between KO and EN, including commutator identities, lower central series, derived series, Zassenhaus lemma isomorphism, Jordan-Holder theorem, and length formula.
- All proofs present in both versions with matching mathematical content.
- Cross-references correctly use language-specific URL paths (/ko/ vs /en/).
- No missing content in either direction.
- Note: The formula h'^{-1}hh'^{-1} in Proposition 2 context appears in both versions identically (possible typo in original Korean, but translation is faithful).


## Field_Theory: Galois_Extension
[STATUS: CONSISTENT]
- All definitions (2, 4, 9, 12), propositions (1, 3, 5, 7, 10, 11, 13), corollary (6), and theorem (8) present in both KO and EN with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN (e.g., splitting formula f(x)=prod(x-a_i), Gal(L/K)->S_A restriction homomorphism, K(x)cong K[x]/(f)cong K(y)).
- Mathematical notation fully consistent: same use of mathbb{K}, mathbb{L}, mathbb{M}, overline{mathbb{K}}, Aut, Gal throughout.
- Same anchor IDs used in both files (prop1, def2, prop3, def4, prop5, cor6, prop7, thm8, def9, prop10, prop11, def12, prop13).
- Pre-existing typos in KO carried consistently into EN: "comjugates" instead of "conjugates" in Theorem 8 proof (both files); "E" instead of "L" in Proposition 1 proof (both files); "S"/"A" inconsistency in Galois group paragraph (both files).
- EN correctly omits the stray "pf" text fragment at end of Proposition 5 proof (KO line 114), which appears to be an artifact rather than mathematical content.
- Minor Korean typos ("보년다는" for "보내다는") correctly translated to English ("sends").
- No missing content in either direction; section structure (Galois Extensions / Galois Groups) matches perfectly.


## Homological_Algebra: Ext_and_Tor
[STATUS: CONSISTENT]
- All 7 definitions (Def 1, 2, 7), 4 propositions (Prop 3, 4, 5, 6), and their proofs are present in both versions.
- All LaTeX formulas are identical between KO and EN.
- Cross-references correctly adjusted from /ko/ to /en/ paths.
- Mathematical notation (Ext, Tor, Hom, lMod, rMod, Ab, Tot, etc.) is consistent throughout.
- Section structure matches exactly: Ext Functor definition, Tor Functor definition, Balancing (with Prop 3 and 4), Examples (with Prop 5 and 6), Koszul complex (Def 7 with induction proof and polynomial algebra application).
- No missing or extra content in either version.


## Homological_Algebra: Derived_Categories
[STATUS: CONSISTENT]
- All 8 definitions (1-6, 8, 11) present in both files with identical mathematical content.
- All 5 propositions (7, 9, 10, 12, 13) present with matching statements and proofs.
- All LaTeX formulas are identical between KO and EN (homotopy category quotient, roof diagrams, shift functor, K-projective/K-injective definitions, derived functor definitions, triangulated category axioms, mapping cone formulas, derived adjunction isomorphism, tensor-Hom adjunction, Tor/Ext formulas).
- No content missing from either side.
- Internal cross-references correctly adapted (ko/ to en/ path changes).
- Theorem/definition numbering consistent.
- References section identical in both.
- Minor stylistic note: TR3 axiom in KO describes maps $(u,v,w)$ while EN describes maps $(u,v)$ then concludes existence of $w$; both convey the same standard triangulated category axiom, just slightly different phrasing.


## Field_Theory: Etale_Algebras
[STATUS: ISSUES FOUND]
- **Theorem 4, statement**: Korean version (line 113) has "$$A$$-algebra homomorphism들" while the English version correctly has "$$\mathbb{K}$$-algebra homomorphisms". This appears to be a typo in the Korean original where $A$ should be $\mathbb{K}$.
- **Redundant formula in EN (lines 30-33)**: The English version displays the dual-space isomorphism formula twice — once after "we have" and again after "and hence obtain an isomorphism of $$\mathbb{L}$$-vector spaces". The Korean version displays it only once. This is a minor structural redundancy in the EN translation.
- **Minor typo in KO (line 206)**: "fintite" instead of "finite" in Korean text for Proposition 8 condition 2. Not present in EN.
- **LaTeX quirk in both versions**: In the proof of Theorem 4, both versions share the same LaTeX oddities (e.g., `\mathbb{L}[\y_1,\ldots, \y_n}` with mismatched brackets, `_n` instead of `\y_n` in one place). These are consistent between KO and EN.
- All other mathematical content is fully consistent: definitions (5, 10), theorems (1, 4), propositions (6, 8, 9, 12, 13), corollaries (2, 3, 7, 14), and lemma (11) have matching statements, proofs, and LaTeX formulas.
- Cross-references correctly point to language-appropriate pages (/ko/... in KO, /en/... in EN).


## Homological_Algebra: Spectral_Sequences
[STATUS: CONSISTENT]
- All 6 definitions (1-5, 9), 4 propositions (6-8, 10), 1 example (11), and 1 proof (Prop 8) present in both files
- All LaTeX formulas are identical between KO and EN
- Cross-references correctly remapped from /ko/ to /en/ paths
- Internal anchor references consistent
- References ([GM], [Wei], [God]) match
- EN metadata includes translated_at and translation_source fields
- No missing or extra content in either version


## Linear_Algebra: Basis
[STATUS: CONSISTENT]

All 12 numbered items match between KO and EN with identical IDs:
- def1 (Definition 1: spanning set), def2 (Definition 2: span), lem3 (Lemma 3: intersection of subspaces), lem4 (Lemma 4: span characterization), def5 (Definition 5: linearly independent), prop6 (Proposition 6: equivalence of linear independence), def7 (Definition 7: basis), ex8 (Example 8), ex9 (Example 9), thm10 (Theorem 10: existence of basis), ex11 (Example 11: standard basis), ex12 (Example 12: K[x] basis)

All LaTeX formulas are identical across both files.

Cross-references correctly adapted:
- KO [§부분공간, ⁋명제 3](/ko/math/linear_algebra/subspaces#prop3) -> EN [§Subspaces, ⁋Proposition 3](/en/math/linear_algebra/subspaces#prop3)
- KO [\[집합론\] §집합의 곱](/ko/math/set_theory/product_of_sets) -> EN [\[Set Theory\] §Product of Sets](/en/math/set_theory/product_of_sets)
- Internal anchor links (def2, lem4, prop6) correctly adapted with translated display text

No content missing in either direction. Structure matches completely.

Minor shared note: Both KO and EN contain the same mathematical typo in the proof of Lemma 4 where "$$v+w\in S$$" appears instead of "$$v+w\in\langle S\rangle$$" (line 96 KO, line 95 EN). This is a faithful translation of an existing typo, not a translation error.
## Linear_Algebra: Bilinear_Form
[STATUS: ISSUES FOUND]

### Structure & IDs
All 7 numbered items match correctly between KO and EN:
- def1: 정의 1 / Definition 1
- def2: 정의 2 / Definition 2
- cor3: 따름정리 3 / Corollary 3
- def4: 정의 4 / Definition 4
- prop5: 명제 5 / Proposition 5
- def6: 정의 6 / Definition 6
- prop7: 명제 7 / Proposition 7

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. No discrepancies found.

### Content Completeness
No content is missing in either direction. Both files have the same structure:
- Introduction (dual space recap)
- Section: Bilinear Forms (Definitions 1, 2)
- Section: Non-Degenerate Bilinear Forms (Corollary 3, Definition 4, Proposition 5)
- Section: Orthogonal Bases (Definition 6, Proposition 7 with proof)
- Section: Gram Matrix
- References (same two references in both)

### Cross-References
1. ISSUE (line 131 EN): EN file has cross-reference `[§Dual Spaces, §§Orthogonal Complements](/en/math/linear_algebra/dual_space#직교여공간)` where the anchor `#직교여공간` is Korean text. This should be the English anchor (e.g., `#orthogonal-complements`) for the link to work correctly on the English site. The text "Orthogonal Complements" is correctly translated but the URL anchor remains Korean.
2. All other cross-references correctly adapted (ko paths -> en paths, Korean text -> English text):
   - `#cor5` anchor: correctly used in both
   - `#def7` anchor: correctly used in both
   - `#ex8` anchor: correctly used in both
   - Internal `#cor3` reference: correctly used in both

### Duplicate Tag Note
Both KO and EN files use `\tag{1}` twice (lines 64/126 in KO, lines 63/123 in EN), creating duplicate equation numbers. This is not a translation issue but exists in both versions.

## Linear_Algebra: Gaussian_Elimination
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All IDs match between KO and EN:
- `lem1`: 보조정리 1 / Lemma 1
- `ex2`: 예시 2 / Example 2
- `def3`: 정의 3 / Definition 3
- `def4`: 정의 4 / Definition 4
- `ex5`: 예시 5 / Example 5
- `lem6`: 보조정리 6 / Lemma 6
- `ex7`: 예시 7 / Example 7

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN:
- Equation tags (1), (2), (3) match exactly.
- All matrix displays (A, x, b, E_{1,2}, E'_{1,r}, E''_{1,2,r}) match exactly.
- Rank-nullity formula matches exactly.
- All augmented matrix computations in Examples 5 and 7 match exactly.
- The final inverse matrix A^{-1} matches exactly.

### Content Completeness
No content is missing in either direction. All sections are present:
- Introduction (motivation from previous post)
- Lemma 1 and its proof
- Discussion of computing inverse via Av_i = e_i
- Gaussian-Jordan Elimination section with conditions (*)
- Example 2 (system of equations and solution)
- Elementary Row Operations section (Definitions 3, 4)
- Elementary matrices (E_{i,j}, E'_{i,r}, E''_{i,j,r})
- Augmented Matrix section
- Examples 5 and 7
- Lemma 6
- Final paragraph about determinants
- References (both cite the same [Lee] reference)

### Cross-References
All internal cross-references correctly adapted with /ko/ → /en/ path swap:
- ftla#def8, matrices#def7, isomorphic_vector_spaces#cor4, retraction_and_section#prop3, isomorphic_vector_spaces#thm7, matrices#def2, existence_and_uniqueness_of_determinant#prop9
- In-file links (#ex2) work in both versions.

### Note
Both KO (line 98) and EN (line 95) contain `a_{nk}x_n` in the j-th equation where `a_{jn}x_n` is likely intended. This is a pre-existing error in the source, not a translation discrepancy.

## Linear_Algebra: Fields
[STATUS: CONSISTENT]

All mathematical content is faithfully translated between KO and EN.

**Numbered items (IDs)**: All six items match with identical IDs:
- `def1` (Definition 1 / 정의 1): Abelian group definition -- consistent
- `prop2` (Proposition 2 / 명제 2): Uniqueness of identity/inverse, cancellation -- consistent
- `cor3` (Corollary 3 / 따름정리 3): -(-a)=a, -(a+b)=-a-b -- consistent
- `ex4` (Example 4 / 예시 4): R, C as abelian groups -- consistent
- `def5` (Definition 5 / 정의 5): Field definition -- consistent
- `prop5` (Proposition 5 / 명제 5): 0a=0, (-1)a=-a -- consistent

Note: Both files share the same numbering where the number 5 is used for both Definition 5 and Proposition 5 (the numbering sequence is 1, 2, 3, 4, 5, 5). This is consistent between KO and EN.

**LaTeX formulas**: All formulas are identical in both files. Checked all inline and display math including the multi-line aligned environment in the proof of Corollary 3.

**Cross-references**: All internal links correctly adapted:
- References to `#def1` and `#prop2` use the same anchor IDs in both files.

**Content completeness**: No content is missing in either direction. Both files contain:
- Introduction paragraph on vector spaces and scalars
- Definition 1 (Abelian group) with 4 conditions
- Remark on groups vs abelian groups
- Proposition 2 with full proof (3 parts)
- Remark on simplified identity/inverse conditions
- Corollary 3 with full proof (2 parts)
- Remark on multiplicative notation
- Example 4 (R and C under addition/multiplication)
- Definition 5 (Field) with 3 conditions
- Remark that 0 != 1
- Notation convention remark
- List of consequences from Proposition 2 applied to fields
- Proposition 5 with full proof
- References section (Gockenbach)
- Footnote 1 (inner product and cross product examples)

**Minor style note**: KO uses `<em-ko>반드시</em-ko>` custom tag (line 92 of KO) where EN uses standard markdown `*must*`. This is a stylistic difference only, not a content issue.

## Linear_Algebra: Dual_Space
[STATUS: CONSISTENT]

**Numbered items (IDs):** All 11 numbered items match between KO and EN with identical IDs:
- def1 (정의 1 / Definition 1) -- bilinear
- def2 (정의 2 / Definition 2) -- pairing, non-degenerate
- ex3 (예시 3 / Example 3) -- canonical pairing
- prop4 (명제 4 / Proposition 4) -- injective map from non-degenerate pairing
- cor5 (따름정리 5 / Corollary 5) -- finite-dimensional spaces with non-degenerate pairing are isomorphic
- prop6 (명제 6 / Proposition 6) -- injective/surjective dual map relations
- def7 (정의 7 / Definition 7) -- orthogonal complement / annihilator
- prop8 (명제 8 / Proposition 8) -- L(U)^perp = (L*)^{-1}(U^perp)
- cor9 (따름정리 9 / Corollary 9) -- (im L)^perp = ker(L*)
- prop10 (명제 10 / Proposition 10) -- (L*(U))^perp = L^{-1}(U^perp)
- cor11 (따름정리 11 / Corollary 11) -- (im L*)^perp = ker L

**LaTeX formulas:** All mathematical formulas are identical between KO and EN. This includes all inline math, display equations, matrix representations, the tagged equation (1), and the evaluation map notation (\ev_v).

**Cross-references:** All cross-references are correctly adapted:
- `/ko/math/linear_algebra/space_of_linear_maps#prop5` → `/en/math/linear_algebra/space_of_linear_maps#prop5`
- `/ko/math/linear_algebra/space_of_linear_maps#cor2` → `/en/math/linear_algebra/space_of_linear_maps#cor2`
- `/ko/math/linear_algebra/ftla` → `/en/math/linear_algebra/ftla`
- `/ko/math/linear_algebra/basis#lem3` → `/en/math/linear_algebra/basis#lem3`
- Internal anchors (#ex3, #prop8, #prop10) are identical in both.

**Content completeness:** No content is missing in either direction. All sections (Dual Basis, Double Dual Space, Dual Map, Orthogonal Complement) with all definitions, propositions, corollaries, proofs, and examples are present in both files. The references section is also present in both.

**Pre-existing note:** In Definition 2, both KO and EN use `$$(-,w):U\rightarrow \mathbb{K}$$` where U refers to the space from Definition 1, but the pairing is defined on V x W. This appears to be a pre-existing typo in the original KO that was faithfully preserved in EN -- not a translation issue.

## Linear_Algebra: Isomorphic_Vector_Spaces
[STATUS: CONSISTENT]

- All 7 labeled items (Definition 1, Lemma 2, Proposition 3, Corollary 4, Proposition 5, Definition 6, Theorem 7) present in both files with matching IDs (def1, lem2, prop3, cor4, prop5, def6, thm7).
- All LaTeX formulas are identical between KO and EN, including: isomorphism definition (L∘L'=id_W, L'∘L=id_V), inverse linearity proof, equivalence relation verification steps, rank-nullity equation (rank L + nullity L = dim V), and the full proof of Theorem 7 (basis extension, linear independence argument, spanning argument).
- Definition 6 parts 1-2 (nullity, rank) match with identical notation (nullity L, rank L, dim ker L, dim im L).
- Two unnumbered statements after Definition 6 (injective iff nullity=0, surjective iff rank=dim W) are present in both versions.
- Cross-references correctly adapted: internal anchors preserved (#def1, #lem2, #prop3, #cor4, #prop5, #def6, #thm7); external links properly use /ko/ vs /en/ paths (set_theory/natural_numbers#cor15, set_theory/cardinals#def1, linear_algebra/linear_map#ex14, linear_algebra/linear_map#cor9).
- Cross-reference display text correctly translated (e.g., "§자연수와 무한집합, ⁋따름정리 15" → "§Natural Numbers and Infinite Sets, ⁋Corollary 15"; "§선형사상, ⁋에시 14" → "§Linear Maps, ⁋Example 14").
- Section structure matches: introduction, Isomorphic Vector Spaces, Rank-Nullity Theorem, References.
- References ([Goc] Gockenbach) identical.
- EN includes expected translation metadata (translated_at, translation_source: kimi-cli).
- Note: Both versions share the same minor content issue in Proposition 5 — statement says "L(B) is also a basis of V" where "basis of W" is mathematically intended (since L:V→W). This is a pre-existing issue in the KO original, faithfully preserved in the translation.
- No content missing from either direction; paragraph-by-paragraph correspondence is complete.
## Linear_Algebra: Characteristic_Polynomial
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All 10 numbered items match between KO and EN:
- def1 (Definition 1): characteristic polynomial definition — ✓
- prop2 (Proposition 2): degree n, coefficient of (n-1) term, constant term — ✓
- def3 (Definition 3): eigenvalue and spectrum — ✓
- cor4 (Corollary 4): well-definedness for linear maps — ✓
- cor5 (Corollary 5): similar matrices share trace and determinant — ✓
- def6 (Definition 6): multiplicity of a root — ✓
- ex7 (Example 7): J matrix with λ²+1 over ℝ — ✓
- thm8 (Theorem 8): Fundamental Theorem of Algebra — ✓
- def9 (Definition 9): eigenvector — ✓
- def10 (Definition 10): geometric multiplicity — ✓

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN:
- Eq (1): determinant expansion via permutations — ✓
- Eq (2): diagonal product (λ−A₁₁)⋯(λ−Aₙₙ) — ✓
- Coefficient: −(A₁,₁+⋯+Aₙ,ₙ) — ✓
- Constant term: det(0I−A) = (−1)ⁿdet(A) — ✓
- Similar matrices: det(λI−A) = det(λI−B) chain — ✓
- J matrix: \begin{pmatrix}0&-1\\1&0\end{pmatrix} — ✓
- (λI−A)v = 0 — ✓
- Av = λv — ✓
- det(λI−A) definitions — ✓

### Cross-References
- KO `[§기저변환, ⁋명제 5](/ko/math/multilinear_algebra/change_of_basis#prop5)` → EN `[§Change of Basis, ⁋Proposition 5](/en/math/multilinear_algebra/change_of_basis#prop5)` — correctly adapted ✓
- KO `[명제 2](#prop2)` → EN `[Proposition 2](#prop2)` — ✓
- KO `[예시 7](#ex7)` → EN `[Example 7](#ex7)` — ✓

### Content Completeness
No missing content in either direction. All sections present:
- Characteristic Polynomial and Eigenvalues — ✓
- Algebraic Multiplicity — ✓
- Eigenvectors and Geometric Multiplicity — ✓
- References ([Goc]) — ✓

## Linear_Algebra: Eigenspace_Decomposition
[STATUS: CONSISTENT]

All 12 numbered items (def1, prop2, prop3, prop4, prop5, prop6, prop7, def8, def9, prop10, lem10, prop11) match between KO and EN with identical IDs.
All LaTeX formulas are identical across both files.
All content (definitions, propositions, proofs, examples, corollaries, lemmas, footnotes) is present in both directions with no missing material.
Cross-references are correctly adapted: /ko/ paths changed to /en/, Korean section/item names changed to English equivalents.

Pre-existing errors (identical in both files, not translation issues):
- Typo `p_A(\mathbf{x}=p_{A'}(\mathbf{x})` — missing closing paren (KO:209, EN:210)
- Typo `\x` instead of `\mathbf{x}` in `$$\x^2+1=0$$` (KO:228, EN:229)
- Missing `=\{0\}` after `W_i \cap W_j` in the R^2 example (KO:88, EN:87)
- Definition 8 references "Proposition 5" / #prop5 but the diagonalizability conditions are from Proposition 6 (KO:256, EN:257)
- Broken cross-reference `#def4` should be `#prop4` (KO:314, EN:315)

## Linear_Algebra: Jordan_Canonical_Form
[STATUS: CONSISTENT]

**IDs:** All 13 numbered items match between KO and EN with identical IDs:
lem1, ex2, def3, cor4, lem5, thm6, def7, lem8, thm9, lem9, def10, thm11, ex12

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. Verified all matrices, kernel/span expressions, characteristic polynomial formulas, Jordan block definitions, and proof calculations.

**Cross-references:** Correctly adapted. KO uses `/ko/math/linear_algebra/...` paths and EN uses `/en/math/linear_algebra/...` paths. Internal references (e.g., [Lemma 1](#lem1), [Corollary 4](#cor4)) are identical. External references to Eigenspace Decomposition and Determinant sections correctly use language-appropriate paths.

**Content completeness:** No missing content in either direction. All sections (Generalized Eigenspaces, Primary Decomposition Theorem, Jordan Canonical Form), all proofs (Lemmas 1, 5, 8, 9; Corollary 4), all definitions (3, 7, 10), all theorems (6, 9, 11), and both examples (2, 12) are present in both files.

**Pre-existing issues (present in both files, not translation errors):**
- In the proof of Lemma 5 (line KO:188, EN:179), the expression `=\lambda_i (L-\lambda_jI)^{p_j-1}w_\lambda w'` contains a likely typo (`w_\lambda w'` instead of `=w'`). This error is identical in both files.
- References to "Theorem 8" (KO:326, EN:311 and KO:354, EN:339) when the Cyclic Decomposition Theorem is labeled as Theorem 9 (thm9). There is no item labeled thm8. This error is identical in both files.

## Linear_Algebra: Dimension
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All 8 numbered items present in both files with matching IDs:
- thm1: Theorem 1 / 정리 1
- lem2: Lemma 2 / 보조정리 2
- def3: Definition 3 / 정의 3
- ex4: Example 4 / 예시 4
- prop5: Proposition 5 / 명제 5
- prop6: Proposition 6 / 명제 6
- ex7: Example 7 / 예시 7
- ex8: Example 8 / 예시 8

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Checked every displayed equation, inline formula, and tagged equation (1) and (2). No discrepancies found.

### Content Completeness
No content missing in either direction. Both files contain:
- Introductory paragraph referencing basis examples
- Theorem 1 (infinite basis case)
- Three-step outline for the theorem
- Lemma 2 with full proof (Steinitz exchange argument)
- Blockquote stating the stronger proposition
- Definition 3 (dimension)
- Example 4 (5 items: trivial space, field, Kn, C over R, K[x])
- Remark about finite-dimensional assumption
- Proposition 5 with proof (extending independent set to basis)
- Proposition 6 with proof (extracting basis from spanning set)
- Example 7 (product of vector spaces)
- Example 8 (sum of subspaces) with dimension formula and proof
- Reference [Goc]

### Cross-References
All cross-references correctly adapted:
- Internal: #thm1, #lem3, #prop5 anchor links match
- External to basis post: /ko/math/linear_algebra/basis#* → /en/math/linear_algebra/basis#* correctly mapped
- Display names translated (예시→Example, 명제→Proposition, 보조정리→Lemma, 정리→Theorem, 정의→Definition)

## Linear_Algebra: Space_of_Linear_Maps
[STATUS: CONSISTENT]

Checked on 2026-05-27.

**Numbered items (IDs):** All 5 IDs match between KO and EN.
- thm1: 정리 1 / Theorem 1 (Extension by linearity)
- cor2: 따름정리 2 / Corollary 2
- lem3: 보조정리 3 / Lemma 3
- def4: 정의 4 / Definition 4
- prop5: 명제 5 / Proposition 5

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. This includes:
- All inline math and display equations in Theorem 1, its proof, and the subsequent discussion (matrix representation (1), expansion, final correspondence)
- Corollary 2 statement and proof (retraction/section formulas)
- Lemma 3 statement and proof (addition/scalar multiplication of linear maps)
- Definition 4 (Hom notation, dual space notation V^\* and V^\ast)
- Proposition 5 statement and proof (B_i^j basis of Hom(V,W))

**Cross-references:** Correctly adapted.
- KO: `/ko/math/set_theory/retraction_and_section#prop1` → EN: `/en/math/set_theory/retraction_and_section#prop1`
- KO: `/ko/math/linear_algebra/linear_map#ex10` → EN: `/en/math/linear_algebra/linear_map#ex10`
- Internal anchor links (#thm1, #lem3) consistent in both.

**Content completeness:** No missing content in either direction. All sections, proofs, diagrams, and explanatory text are present in both files. Korean-specific inline tags (<em-ko>) are not carried over to EN, as expected.

## Linear_Algebra: Determinant
[STATUS: CONSISTENT]

**Checked files:**
- KO: `_posts/Math/Linear_Algebra/ko/2022-03-07-Determinant.md`
- EN: `_posts/Math/Linear_Algebra/en/2022-03-07-Determinant.md`

**1. Numbered items (IDs):**
- def1: KO "정의 1" / EN "Definition 1" — present in both, ID matches ✓
- def2: KO "정의 2" / EN "Definition 2" — present in both, ID matches ✓
- prop3: KO "명제 3" / EN "Proposition 3" — present in both, ID matches ✓
- def4: KO "정의 4" / EN "Definition 4" — present in both, ID matches ✓

**2. LaTeX formulas — all identical between KO and EN:**
- isomorphism formula (column vector decomposition) ✓
- Definition 1: multilinear map function signature ✓
- Definition 2: alternating condition equation ✓
- Proposition 3 proof: first aligned equation (alternating → antisymmetric) ✓
- Proposition 3 proof: antisymmetry zero equation ✓
- Proposition 3 proof: expanded multilinearity equation ✓
- Definition 4: `D(e_1,...,e_n)=1` and function signature ✓
- All inline formulas (`$$\Mat_n(\mathbb{K})$$`, `$$\mathbb{K}^n$$`, `$$D(v_1,...,v_n)=0$$`, etc.) ✓

**3. Content completeness:**
- All three major sections present: Definition of the Determinant, Area and Volume, Geometric Meaning of the Determinant ✓
- Introduction paragraph fully translated ✓
- Both footnotes present: [^1] (congruent parallelograms) and [^2] (well-definedness of area) ✓
- Reference [Goc] present in both ✓
- All 5 images referenced identically (Determinant.png, Determinant-1 through -4) ✓

**4. Cross-references:**
- KO "[명제 3](#prop3)" → EN "[Proposition 3](#prop3)" ✓
- KO "[정의 4](#def4)" → EN "[Definition 4](#def4)" ✓

**5. Minor note (non-mathematical):**
- EN file uses `<em-ko>` HTML tags for emphasis on English terms ("hypervolume", "orientation") — appears to be a translation artifact where the Korean emphasis tag was kept. Not a mathematical content issue, but the tag name is misleading in the EN context. The `<phrase>` tags are correctly used in both.

## Linear_Algebra: Fundamental_Theorem_of_Linear_Algebra
[STATUS: CONSISTENT]

Numbered items: All 8 items match (ex1, thm2, thm3, thm4, thm5, cor6, def7, def8).

LaTeX formulas: All formulas are identical between KO and EN. Checked equations (1), (2), (3), theorems 2-5, corollary 6, definitions 7-8, all proofs, change-of-basis formulas, and similar matrices formula.

Cross-references: All internal cross-references (#ex1, #thm2, #thm3, #thm4, #thm5, #cor6) correctly use same IDs. External links correctly adapted from /ko/ to /en/ paths (isomorphic_vector_spaces, space_of_linear_maps, matrices, dimension).

Content completeness: No missing content in either direction. Both files contain the same structure: intro, Example 1, Theorems 2-5 with proofs, Corollary 6 with proof, remark on transpose matrix, change-of-basis section with Definitions 7-8, references, and footnote [^1].
## Manifold: Cotangent_Space
[STATUS: ISSUES FOUND]

### Numbered Items
- Lemma 1 (`id="lem1"`): Present in both KO and EN. ✓
- Theorem 2 (`id="thm2"`): Present in both KO and EN. ✓
- Definition 3 (`id="def3"`): Present in both KO and EN. ✓
All IDs match correctly.

### LaTeX Formulas
All major LaTeX formulas are identical between KO and EN:
- Ideal chain: `\mathcal{C}^\infty_p\supset\mathfrak{m}_p\supset\mathfrak{m}_p^2\supset\cdots` ✓
- Isomorphism: `T_pM\cong(\mathfrak{m}_p/\mathfrak{m}_p^2)^\ast` ✓
- Double dual: `(T_pM)^\ast\cong(\mathfrak{m}_p/\mathfrak{m}_p^2)^{\ast\ast}\cong\mathfrak{m}_p/\mathfrak{m}_p^2` ✓
- Derivation rule: `v(\mathbf{f}_i\mathbf{f}_j)=\mathbf{f}_i(p)v(\mathbf{f}_j)+\mathbf{f}_j(p)v(\mathbf{f}_i)=0` ✓
- Definition of v_L: `v_L(\mathbf{f})=L((\mathbf{f}-\mathbf{f(p)})+\mathfrak{m}_p^2)` ✓
- 4-line computation in proof of Lemma 1: All 4 lines match exactly between KO and EN. ✓
- Taylor approximation formulas: All identical. ✓
- Directional derivative definition: Identical. ✓
- Basis expansion formula: Identical. ✓

### Cross-References
- KO `[§접공간, ⁋명제 2](/ko/math/manifold/tangent_space#prop2)` ↔ EN `[§Tangent Space, ⁋Proposition 2](/en/math/manifold/tangent_space#prop2)` ✓
- KO `[§접공간, ⁋정의 3](/ko/math/manifold/tangent_space#def3)` ↔ EN `[§Tangent Space, ⁋Definition 3](/en/math/manifold/tangent_space#def3)` ✓
Internal anchor IDs (lem1, thm2, def3) are consistent in both files. ✓

### Content Completeness
- No content missing in either direction. All paragraphs, proofs, examples, and remarks are present in both versions. ✓

### ISSUE FOUND
- **KO line 99**: `이들 $$n$$개의 원소들` uses variable `n`, but the dimension throughout the proof is `m` (from `$$\varphi=(x^i)_{i=1}^m$$`). The EN version (line 96) correctly says `these $$m$$ elements`. This is a typo in the Korean version: `n` should be `m`.

### References
Both versions cite [War] and [Lee] identically. ✓

## Linear_Algebra: Vector_Spaces
[STATUS: CONSISTENT]

**IDs:** All 6 numbered items match between KO and EN (def1, prop2, cor3, ex4, ex5, ex6).

**LaTeX formulas:** All mathematical expressions are identical in both files. Verified:
- Definition 1: scalar multiplication axioms (conditions 1-4) with +_V and +_K notation
- Proposition 2: alpha*0=0, 0*v=0, converse statement
- Proposition 2 proof: all three derivations (alpha*0=0, 0*v=0, v=0)
- Corollary 3: (-1)v = -v and its proof equation
- Example 4: {0}, 0+0=0, alpha*0=0, K x K -> K, K' superset K
- Example 5: column vector notation, addition formula, scalar multiplication formula
- Notation paragraph: (a1 a2 ... an)^t and (a1,a2,...,an) conventions
- Example 6: Fun(I,R), f+g and alpha*f definitions, C(I), C^k(I)

**Cross-references:** All correctly adapted:
- /ko/math/linear_algebra/fields#prop2 -> /en/math/linear_algebra/fields#prop2
- /ko/math/linear_algebra/fields (Corollary 3) -> /en/math/linear_algebra/fields
- /ko/math/linear_algebra/fields#prop5 -> /en/math/linear_algebra/fields#prop5
- /ko/math/set_theory/product_of_sets#def1 -> /en/math/set_theory/product_of_sets#def1
- Internal anchors (def1, prop2, cor3, ex4, ex5, ex6) preserved

**Content completeness:** No missing content in either direction. All paragraphs, explanatory notes, and the reference section (Gockenbach) are present in both versions.

## Manifold: Differential_Forms
[STATUS: CONSISTENT]

### Numbered Items
All four numbered items present in both files with matching IDs:
- `def1`: KO "정의 1" / EN "Definition 1"
- `thm2`: KO "정리 2" / EN "Theorem 2"
- `def3`: KO "정의 3" / EN "Definition 3"
- `prop4`: KO "명제 4" / EN "Proposition 4"

### LaTeX Formulas
All 15 LaTeX formula blocks are identical between KO and EN (ignoring trivial English trailing periods after display math). Formulas checked:
- Definition 1 tensor/exterior bundle definitions
- Smooth sections definitions
- Simple tensor pairing formulas (tensor and wedge)
- Direct sum isomorphism
- Exterior algebra isomorphism chain
- Differential form function notation
- Wedge product definition
- N-graded R-algebra
- Functor pullback construction
- Pullback evaluation formula
- Cochain complex sequence (2)
- Interior multiplication formula

### Cross-References
All cross-references correctly adapted from /ko/ to /en/ paths with translated display text:
- Tangent and cotangent bundles: Example 5, Theorem 6
- Linear Algebra: Dual Spaces, Corollary 5
- Multilinear Algebra: Tensor Algebras, Definition 10
- Examples of Differentials: Definition 6
- Both files share the same unresolved `[##ref##]()` placeholder on Theorem 2

### Content Completeness
No missing content in either direction. Both files contain identical structure: 4 sections (Vector Bundles, Differential Forms and Pullback, Exterior Derivative and de Rham Cohomology, Interior Multiplication), the same image reference, and the same references ([War], [Lee]).

## Manifold: Differentials
[STATUS: CONSISTENT]

**Numbered IDs (KO vs EN):**
- def1, prop2, ex3, ex4, prop5, def6, rmk1, def7, prop8 -- all present in both files with matching IDs. No discrepancies.

**LaTeX formulas:**
- All LaTeX expressions are identical between KO and EN, including:
  - Definition 1: `\psi\circ F\circ\varphi^{-1}` condition
  - Proposition 2 proof: `F=\psi^{-1}\circ(\psi\circ F\circ\varphi^{-1})\circ\varphi`
  - Remark: `(\psi\circ F\circ \varphi^{-1})(t)=t` and `(\psi^{-1}\circ F^{-1}\circ \varphi)(s)=s`
  - Pullback linearity formulas for `F^\ast`
  - Dual map: `(F^\ast)^\ast(L)=L\circ F^\ast`
  - Leibniz rule verification (3-line aligned equation)
  - Definition 7: `(dF_p(v))g=v(g\circ F)`
  - Chain rule: `d(G\circ F)_p=(dG_{F(p)})\circ (dF_p)`
  - Partial derivative bases: `\frac{\partial}{\partial x^i}\bigg|_p` etc.
  - Jacobian matrix (n x m matrix with partial derivatives)
  - Footnotes about `\varphi^{-1}` being diffeomorphism and `\psi(F(p))=0` assumption

**Cross-references:**
- KO `[§미분다양체, ⁋정의 2](/ko/math/manifold/smooth_manifolds#def2)` → EN `[§Smooth Manifolds, ⁋Definition 2](/en/math/manifold/smooth_manifolds#def2)` ✓
- KO `[§미분다양체의 예시들, ⁋정의 3](/ko/math/manifold/examples_of_manifolds#def3)` → EN `[§Examples of Manifolds, ⁋Definition 3](/en/math/manifold/examples_of_manifolds#def3)` ✓
- KO `[§미분다양체, ⁋예시 4](/ko/math/manifold/smooth_manifolds#ex4)` → EN `[§Smooth Manifolds, ⁋Example 4](/en/math/manifold/smooth_manifolds#ex4)` ✓
- Internal `[정의 1](#def1)` → `[Definition 1](#def1)`, `[정의 7](#def7)` → `[Definition 7](#def7)` -- all correct ✓
- Permalink `/ko/math/manifold/differentials` vs `/en/math/manifold/differentials` ✓

**Content completeness:**
- All 3 definitions, 3 propositions (2 with proofs), 2 examples, 1 remark, and 2 footnotes present in both files. No missing content in either direction.
- Images, references ([War], [Lee]), and sidebar nav keys correctly adapted.

## Linear_Algebra: Matrices
[STATUS: CONSISTENT]

**Sections (3/3 matched):**
- "행렬의 기본 정의" → "Basic Definitions" ✓
- "행렬의 연산" → "Operations on Matrices" ✓
- "행렬의 곱" → "Matrix Multiplication" ✓

**Numbered items (8/8 matched, all IDs preserved):**
- def2 (정의 2 / Definition 2): Matrix-vector product Ax = Σ x_j A_j ✓
- def3 (정의 3 / Definition 3): Matrix multiplication BA definition ✓
- def4 (정의 4 / Definition 4): Identity matrix I ✓
- def5 (정의 5 / Definition 5): Invertible matrix / singular matrix ✓
- def6 (정의 6 / Definition 6): GL(n, K) general linear group ✓
- def7 (정의 7 / Definition 7): Trace tr(A) ✓
- def8 (정의 8 / Definition 8): Transpose A^t ✓
- prop9 (명제 9 / Proposition 9): (AB)^t = B^t A^t ✓

**LaTeX formulas:** All identical between KO and EN. No discrepancies found.
- Matrix definition, scalar multiplication, basis matrices
- Ax sum formula and explicit component form
- BA sum formula, (BA)_ij formula
- Associative law, identity matrix, trace formulas, transpose formula
- All verified line-by-line ✓

**Cross-references correctly adapted:**
- `/ko/math/linear_algebra/fields#prop2` → `/en/math/linear_algebra/fields#prop2` ✓
- `/ko/math/linear_algebra/ftla` → `/en/math/linear_algebra/ftla` ✓
- `[정의 5](#def5)` → `[Definition 5](#def5)` ✓

**Footnotes:** Both files have 1 footnote each; content is consistent. ✓

**References:** Both list [Goc] and [Lee] identically. ✓

**Missing content:** None in either direction.

## Manifold: Orientation
[STATUS: CONSISTENT]

- **Numbered items**: All 3 items (def1, prop2, ex3) present in both files with identical IDs. Proposition 2's 3 sub-items also match.
- **LaTeX formulas**: All formulas are identical between KO and EN, including:
  - Cross product expressions ($$e_1\times e_2=e_3$$, etc.)
  - Determinant expressions ($$\det[x_1\;x_2\;\cdots\;x_m]$$)
  - Exterior algebra expressions ($$\bigwedge\nolimits^n(L)$$, $$\bigwedge\nolimits^m(M)\setminus\{0\}$$)
  - Bundle notation ($$E=T^\ast M$$)
  - Lie group example ($$\Omega_\text{l.inv}^\ast(G)$$, $$\omega_1\wedge\cdots\wedge\omega_n$$)
- **Cross-references**: Correctly adapted — KO links to `/ko/math/multilinear_algebra/tensor_algebras#prop11`, EN links to `/en/math/multilinear_algebra/tensor_algebras#prop11`.
- **Content completeness**: No missing content in either direction. Both files have the same structure: Euclidean space intro, determinant and orientation section, Definition 1, Proposition 2 (with empty proof), Example 3, and identical references ([War], [Lee]).
- **Translation note**: KO "0보다 크도록" accurately rendered as "always positive" in EN.

## Manifold: Distribution
[STATUS: CONSISTENT]

**Numbered IDs:** All 5 items match between KO and EN with identical IDs.
- def1 (정의 1 / Definition 1)
- def2 (정의 2 / Definition 2)
- thm3 (정리 3 / Theorem 3 -- Frobenius)
- lem4 (보조정리 4 / Lemma 4)
- lem5 (보조정리 5 / Lemma 5)

**LaTeX formulas:** All display math formulas are identical across both files. Minor stylistic difference: EN appends periods after some display formulas where KO does not (e.g., after dΦ_s formula in Lemma 4 proof, after Y_i definition in Theorem 3 proof). This is a punctuation convention, not a mathematical discrepancy.

**Content completeness:** No content missing in either direction. Both files contain:
- Intro section on distributions and integral flow
- Definition 1 (k-dimensional distribution), Definition 2 (integral manifold)
- Frobenius Theorem (Theorem 3) with all 3 sub-assertions
- Lemma 4 (integrable implies involutive) with full proof
- Lemma 5 (straightening lemma) with full proof
- Full proof of Theorem 3 (induction on k)
- References ([War], [Lee])

**Cross-references:** All correctly adapted.
- KO `[/ko/math/manifold/vector_fields]` → EN `[/en/math/manifold/vector_fields]` ✓
- KO `[§리 미분, ⁋명제 9](/ko/math/manifold/Lie_derivative#prop9)` → EN `[§Lie Derivative, ⁋Proposition 9](/en/math/manifold/Lie_derivative#prop9)` ✓
- KO `[§벡터장, ⁋정리 6](/ko/math/manifold/vector_fields#thm6)` → EN `[§Vector Fields, ⁋Theorem 6](/en/math/manifold/vector_fields#thm6)` ✓
- Internal links `[보조정리 5](#lem5)` → `[Lemma 5](#lem5)` ✓
- Internal links `[정리 3](#thm3)` → `[Theorem 3](#thm3)` ✓

**Note:** Both files share a likely typo in the Theorem 3 proof (line ~203): `Y_1(Y_i(x^{k+j})` is missing a closing parenthesis (should be `Y_1(Y_i(x^{k+j}))`). This is an original-content issue, not a translation discrepancy.
## Linear_Algebra: Inner_Product_Spaces
[STATUS: CONSISTENT]

**Numbered items (9 total):** All IDs match between KO and EN.
- def1 (Definition 1), def2 (Definition 2), prop3 (Proposition 3 / Cauchy-Schwarz), prop4 (Proposition 4), prop5 (Proposition 5), ex6 (Example 6), def7 (Definition 7), lem8 (Lemma 8), thm9 (Theorem 9)

**LaTeX formulas:** All display math formulas are identical between KO and EN. No discrepancies found.

**Content completeness:** All 4 sections present in both files:
1. Inner Products and Norms (내적과 노름)
2. Orthonormal Bases (정규직교기저)
3. Orthogonal Matrices (직교행렬)
4. Projection Theorem (Projection theorem)

All proofs, discussions, and explanatory paragraphs are complete in both directions.

**Cross-references:** Correctly adapted with language-specific URL paths.
- KO `[명제 4](#prop4)` ↔ EN `[Proposition 4](#prop4)`
- KO `[명제 5](#prop5)` ↔ EN `[Proposition 5](#prop5)`
- KO cross-ref to bilinear_form (ko path) ↔ EN cross-ref (en path)

**Pre-existing typos (consistently present in both files, not translation issues):**
1. In the second change-of-basis matrix, `$$\langle x'_n,n\rangle$$` should be `$$\langle x'_n,x_n\rangle$$` (KO line 207, EN line 206).
2. In the proof of Proposition 4, `$$(v,v)\geq 0$$` should be `$$\langle v,v\rangle\geq 0$$` (KO line 99, EN line 98).

## Manifold: Lie_Derivative
[STATUS: CONSISTENT]

All numbered items (IDs) match between KO and EN:
- def1, def2, def3, prop4, def5, def6, prop7, prop8, prop9

All LaTeX formulas are identical in both files:
- Directional derivative limit, formula (1), Definitions 1-3, 5-6
- Proposition 4 (all 6 items including formulas for L_X on functions, vector fields, derivation property, Cartan's formula, Leibniz-type identity, and exterior derivative formula)
- Formula (2) (XY)(fg) expansion
- Proposition 7, 8, 9 statements and proofs (including all aligned equation blocks)

Cross-references correctly adapted:
- `/ko/math/manifold/examples_of_differentials#def1` -> `/en/math/manifold/examples_of_differentials#def1`
- `/ko/math/manifold/vector_fields#thm6` -> `/en/math/manifold/vector_fields#thm6` (two occurrences)
- Internal refs `[정의 1](#def1)` -> `[Definition 1](#def1)`, `[명제 2](#prop2)` -> `[Proposition 2](#prop2)`

No content missing in either direction. Both files have identical structure: 6 definitions and 3 propositions with proofs, plus references.

## Manifold: Examples_of_Differentials
[STATUS: CONSISTENT]

All 7 numbered items (def1, prop2, prop3, prop4, ex5, def6, prop7) have matching IDs in KO and EN.
All LaTeX formulas are identical between the two files.
No content is missing in either direction: all definitions, propositions, examples, proofs, references, and footnotes are present in both.
All cross-references are correctly adapted (ko/ paths → en/ paths, Korean labels → English labels).
Note: The directional derivative formula uses `\lim_{h\to 0}` with variable `h` but `t` in the fraction body — this is a pre-existing issue in the Korean source, faithfully preserved in the English translation, not a translation error.

## Linear_Algebra: Subspaces
[STATUS: CONSISTENT]

All numbered items (def1, prop2, prop3, def4, ex5, ex6) match between KO and EN with identical IDs.

LaTeX formulas: All identical between KO and EN.

Content completeness: No missing content in either direction. All definitions, propositions, proofs, examples, and references are present in both files.

Cross-references: All external cross-references to vector_spaces are correctly adapted (ko/ vs en/ paths, correct anchor names such as #ex6, #def1, #prop2, #cor3, #ex4). Internal references (#prop2) are correct.

Notes on pre-existing content issues (identical in both files, not translation errors):
- Example 6 references "preceding Example 7" (#ex7) which does not exist; should be Example 5 (#ex5).
- Scalar multiplication formula for polynomials: last term is $\alpha_0$ instead of $\gamma\alpha_0$ (missing $\gamma$ factor on constant term).

## Manifold: Differential_Ideal
[STATUS: CONSISTENT]

**IDs:** All 7 numbered items match between KO and EN (def1, prop2, def3, prop4, def5, thm6, thm7).

**LaTeX formulas:** All mathematical expressions are identical in both files. Verified:
- Definition 1: annihilate condition ω_p(v_1,...,v_l)=0
- Proposition 2: I(D) is ideal, locally generated by m-k 1-forms, uniqueness
- Proposition 2 proof: dual basis ω_i(X_j)=δ_{ij}
- Definition 3: differential ideal (closed under d)
- Proposition 4: involutive iff I(D) is differential ideal
- Definition 5: integral manifold (dΦ)*ω≡0
- Theorem 6: existence of k-dimensional integral manifold
- Theorem 7: graph(f) as integral manifold, existence of local f with (df)*ω_i=α_i|_U
- Theorem 7 proof: (dι)*(μ_i)=0 computation, Frobenius application

**Cross-references:** All correctly adapted:
- /ko/math/manifold/examples_of_manifolds#ex5 -> /en/math/manifold/examples_of_manifolds#ex5
- Section names translated (미분다양체의 예시들 → Examples of Manifolds, 예시 5 → Example 5)

**Content completeness:** No missing content in either direction. All three sections (Definition of Differential Ideal, Differential Ideals and Frobenius's Theorem, Graphs and Differential Forms), all proofs, and references ([War], [Lee]) are present in both versions.

**Minor note:** EN has a dangling "given by" fragment at line 131 (leftover from translating the Korean "로 주어진다."), followed by a blank line before the next paragraph. This is a translation artifact, not a mathematical content issue.

**Pre-existing issue in both versions:** In the proof of Theorem 7 part 1 (KO line 139, EN line 137), the text says "show that (dι)*(ω_i)=0" but the actual computation shows (dι)*(μ_i)=0. The ω_i vs μ_i discrepancy is a typo in the KO original, faithfully preserved in the EN translation.
## Linear_Algebra: Least_Squares_Method
[STATUS: ISSUES FOUND]

### Numbered Items
All numbered items match between KO and EN with identical IDs:
- prop1 (Proposition 1 / 명제 1)
- ex2 (Example 2 / 예시 2)
- prop3 (Proposition 3 / 명제 3)
- prop4 (Proposition 4 / 명제 4)
- def5 (Definition 5 / 정의 5)
- rmk6 (Remark 6 / 참고 6)

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. No discrepancies found.

### Cross-References
ISSUE: EN line 23 contains a broken cross-reference. The link text says "§Bilinear Forms, §§Non-degenerate Bilinear Forms" and the URL path points to the EN version (`/en/math/linear_algebra/bilinear_form`), but the anchor is the Korean heading slug `#비퇴화-쌍선형형식`. Since the EN bilinear form post uses the heading "## Non-Degenerate Bilinear Forms" (without an explicit anchor ID), Jekyll would auto-generate an English slug like `#non-degenerate-bilinear-forms`. The Korean anchor will not resolve in the English version.

KO original (line 24):
  `[§쌍선형형식, §§비퇴화 쌍선형형식](/ko/math/linear_algebra/bilinear_form#비퇴화-쌍선형형식)`
EN translation (line 23):
  `[§Bilinear Forms, §§Non-degenerate Bilinear Forms](/en/math/linear_algebra/bilinear_form#비퇴화-쌍선형형식)`

Fix: Change the anchor from `#비퇴화-쌍선형형식` to the correct English auto-generated anchor for the "Non-Degenerate Bilinear Forms" heading in the EN bilinear form post.

All other cross-references (prop1, prop3, prop5, thm9) use explicit `<ins id="...">` attributes and are correctly adapted in EN.

### Content Completeness
No content is missing in either direction. All propositions, proofs, examples, definitions, and remarks are fully present and mathematically equivalent.

## Linear_Algebra: Bilinear_Form
[STATUS: ISSUES FOUND]

### Numbered Items (IDs)
All 7 numbered items match between KO and EN:
- `def1`: 정의 1 → Definition 1 ✓
- `def2`: 정의 2 → Definition 2 ✓
- `cor3`: 따름정리 3 → Corollary 3 ✓
- `def4`: 정의 4 → Definition 4 ✓
- `prop5`: 명제 5 → Proposition 5 ✓
- `def6`: 정의 6 → Definition 6 ✓
- `prop7`: 명제 7 → Proposition 7 ✓

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Checked all equations including:
- Canonical pairing, symmetric/alternating conditions, isomorphism (1)
- Corollary 3, Definition 4 (orthogonal complement)
- Dual basis, transferred basis, delta equations
- Matrix representation, adjoint equation (1), verification chain
- Proposition 5 (4 items), four fundamental subspaces, direct sums
- Definition 6 (characteristic), F_2 field operations
- Proposition 7 proof (all steps: 2<u,v> identity, decomposition, dimension formula, u' construction)
- Gram matrix formulas, basis change formula

### Content Completeness
No content is missing in either direction. Both files have identical structure:
- Introduction (dual space recap)
- Bilinear Forms section (Definitions 1, 2)
- Non-Degenerate Bilinear Forms section (Corollary 3, Definition 4, Proposition 5)
- Orthogonal Bases section (Definition 6, Proposition 7 with full proof)
- Gram Matrix section
- Same two references ([Lee] and [Goc])

### Cross-References
ISSUE: EN line 131 cross-reference `[§Dual Spaces, §§Orthogonal Complements](/en/math/linear_algebra/dual_space#직교여공간)` uses Korean anchor `#직교여공간`. The English Dual Space post (`2022-08-07-Dual_Space.md`) has section header `## Orthogonal Complement` which generates anchor `#orthogonal-complement`. This link will not navigate correctly in the English version. Should be changed to `#orthogonal-complement`.

All other cross-references are correctly adapted:
- `/ko/` → `/en/` paths ✓
- Korean display text → English display text ✓
- Anchors `#cor5`, `#def7`, `#ex8`, `#cor3` are consistent ✓

### Minor Note
Both files contain duplicate `\tag{1}` (first on the isomorphism equation, second on the adjoint equation). This is present identically in both files and is not a translation issue, but a pre-existing labeling issue in the source.

## Manifold: Vector_Fields
[STATUS: CONSISTENT]

All 7 numbered items (def1, prop2, ex3, def4, def5, thm6, def7) present in both files with matching IDs.
All LaTeX formulas are identical between KO and EN (including all displayed equations, inline math, and tagged equation (1)).
Proof of Proposition 2 is complete and mathematically equivalent in both files.
All cross-references correctly adapted (prop2 link, tangent space footnote link).
No missing content in either direction: definitions, propositions, proofs, examples, hairy ball theorem discussion, parallelizable manifold discussion, integral flow explanation, and references all present in both.
Theorem 6 items 1-8 are fully translated with identical LaTeX.

## Manifold: Tangent_Space
[STATUS: CONSISTENT]

**Numbered items (all IDs match):**
- `prop1`: KO "명제 1" ↔ EN "Proposition 1" ✓
- `prop2`: KO "명제 2" ↔ EN "Proposition 2" ✓
- `def3`: KO "정의 3" ↔ EN "Definition 3" ✓
- `prop4`: KO "명제 4" ↔ EN "Proposition 4" ✓
- `lem6`: KO "보조정리 6" ↔ EN "Lemma 6" ✓
- Note: numbering skips from 4 to 6 in both files (no item 5) -- consistent.

**LaTeX formulas:** All displayed and inline math formulas are identical across both files. Verified all 20+ LaTeX expressions including the directional derivative limit, stalk definition, Leibniz rule, exact sequence diagram, and the aligned computation in the Prop 4 proof.

**Cross-references:** All correctly adapted.
- KO `[명제 1](#prop1)` → EN `[Proposition 1](#prop1)` ✓
- KO `[정의 3](#def3)` → EN `[Definition 3](#def3)` ✓
- KO `[위상수학] §층, ⁋정의 1` → EN `[Topology] §Sheaves, ⁋Definition 1` ✓
- KO `[위상수학] §준층, ⁋정의 9` → EN `[Topology] §Presheaves, ⁋Definition 9` ✓

**Content completeness:** No missing content in either direction. Both files contain the same sections (Motivation, Sheaf of Differentiable Functions, Tangent Vectors), the same five numbered items, the same references ([War], [Lee]), and the same footnote [^1].

**Minor note:** EN file uses `<em-ko>` tags (Korean emphasis class) on lines 31 and 85 for the translated terms "directional derivative" and "directional derivative at the point $p$". This is a styling/presentation detail, not a mathematical inconsistency.

## Manifold: Implicit_Function_Theorem
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All six numbered items match with identical IDs between KO and EN:
- def1: "정의 1" / "Definition 1"
- lem2: "보조정리 2" / "Lemma 2"
- thm3: "정리 3 (음함수 정리)" / "Theorem 3 (Implicit Function Theorem)"
- cor4: "따름정리 4 (Submersion level set theorem)" / "Corollary 4 (Submersion Level Set Theorem)"
- cor5: "따름정리 5 (Constant-rank level set theorem)" / "Corollary 5 (Constant-Rank Level Set Theorem)"
- ex6: "예시 6" / "Example 6"

### LaTeX Formulas
All LaTeX formulas are mathematically identical between KO and EN. Minor typographic differences:
- EN adds trailing periods inside some display math (`.$$` vs `$$`) in Definition 1 and Example 6. This is a stylistic punctuation convention difference with no mathematical impact.
- In Theorem 3, EN presents the n×n submatrix first, then the full Jacobian matrix (reversed from KO's order: Jacobian first, then submatrix). Both contain the same two matrices with identical entries.

### Content Completeness
No content is missing in either direction. Both files contain:
- Same definition, lemma, theorem, two corollaries, one example
- Same empty proof blocks (details/proof elements)
- Same counterexample image reference
- Same quoted summary ("Immersed submanifold is locally embedded")
- Same references ([War] and [Lee])
- Same section heading ("음함수 정리와 그 결과들" / "The Implicit Function Theorem and Its Consequences")

### Cross-References
KO: `[따름정리 5](#cor5)` correctly adapted to EN: `[Corollary 5](#cor5)`.


## Linear_Algebra: Linear_Map
[STATUS: CONSISTENT]

**Numbered items**: All 14 items match with same IDs in both files (def1, prop2, prop3, prop4, def5, def6, prop7, prop8, cor9, ex10, ex11, ex12, ex13, ex14).

**LaTeX formulas**: All mathematical formulas are identical between KO and EN.

**Content completeness**: No content is missing in either direction. All definitions, propositions, corollaries, examples, proofs, and explanatory paragraphs are present in both versions.

**Cross-references**: All correctly adapted:
- Internal references use same anchor IDs (#prop2, #prop3, etc.)
- External section references correctly map ko/ paths to en/ paths and translate display text (e.g., "§벡터공간, ⁋명제 2" -> "§Vector Spaces, ⁋Proposition 2")
- Cross-topic references correctly adapted (e.g., set_theory/operation_of_functions#ex3)

**Minor observations (not translation issues)**:
- Both versions share a typo in Definition 5, item 2: `$$v\in L$$` should be `$$v\in V$$`.
- Example 11 in KO uses `$$L$$` where `$$\iota$$` is meant (lines 243, 247). The EN version corrected this to `$$\iota$$`, making it more accurate than the KO original.
- Both versions cite Proposition 3 in the proof of Proposition 8 where Proposition 2 (item 3) would be more directly applicable.

## Linear_Algebra: Existence_and_Uniqueness_of_Determinant
[STATUS: CONSISTENT]

### Numbered Items
All 12 IDs present in both files with matching types:
- def1: Definition 1 (symmetric group) ✓
- lem2: Lemma 2 (existence and uniqueness) ✓
- cor4: Corollary 4 (det(A^t) = det A) ✓
- lem5: Lemma 5 (det(AB) = det(A)det(B)) ✓
- prop6: Proposition 6 (det A ≠ 0 iff A invertible) ✓
- cor7: Corollary 7 (det(A^{-1}) = (det A)^{-1}) ✓
- def8: Definition 8 (triangular/diagonal matrices) ✓
- prop9: Proposition 9 (det of triangular = product of diagonal) ✓
- prop10: Proposition 10 (block matrix det) ✓
- cor11: Corollary 11 (block matrix det with C) ✓
- def12: Definition 12 (minor matrix A^{(i,j)}) ✓
- thm13: Theorem 13 (Laplace expansion) ✓

### LaTeX Formulas
All tagged equations (1), (2), (3) are identical between KO and EN.
All 2 aligned display blocks are identical.
All 10 matrix blocks are identical.
All 2 cases blocks are identical.
No formula discrepancies found.

### Cross-References
Internal anchors (#lem5, #prop9, #prop10) correctly preserved in both files.
External links correctly use /ko/ prefix in KO and /en/ prefix in EN:
- group_theory/symmetric_groups ✓
- linear_algebra/determinant#def4, #prop3 ✓
- linear_algebra/Gaussian_elimination#def4, parent ✓

### Content Completeness
5 sections in both: Symmetric Group, Existence and Uniqueness, Triangular Matrices, Block Matrix, Laplace Expansion.
3 definitions, 9 propositions, 8 proofs in both.
No missing content in either direction.

### Minor Note
KO uses `<em-ko>` tag for emphasis on "않는다" (line 284) but EN has no corresponding emphasis tag on "does not hold" (line 283). This is a minor formatting difference that does not affect mathematical content.

## Manifold: Smooth_Manifolds
[STATUS: CONSISTENT]

All 5 numbered items (def1, def2, prop3, ex4, lem5) present in both files with matching IDs and equivalent titles:
- def1: "정의 1" ↔ "Definition 1" (C^k-compatible, C^k-atlas, C^k-differentiable structure) ✓
- def2: "정의 2" ↔ "Definition 2" (C^∞ at a point on a manifold) ✓
- prop3: "명제 3" ↔ "Proposition 3" (uniqueness of maximal atlas) ✓
- ex4: "예시 4" ↔ "Example 4" (two different differentiable structures on R) ✓
- lem5: "보조정리 5" ↔ "Lemma 5" (C^∞ Urysohn lemma) ✓

All LaTeX formulas are identical between KO and EN:
- Partial derivative limit definition (r^i notation) ✓
- C^2 partial derivative examples (∂²f/∂x², etc.) ✓
- Transition maps in Definition 1 (ψ∘φ⁻¹, φ∘ψ⁻¹) ✓
- Atlas examples: A = {(R, id_R)} and A' = {((-∞,1), id), ...} ✓
- Composition f∘ψ⁻¹ = (f∘φ⁻¹)∘(φ∘ψ⁻¹) in Definition 2 discussion ✓
- Maximal atlas construction formula in Proposition 3 proof ✓
- Transition map ψ'∘ψ⁻¹ = (ψ'∘φ⁻¹)∘(φ∘ψ⁻¹) in proof ✓
- Example 4 atlases A₁ and A₂ ✓
- Bump function definitions: f(t), g(t), ψ(t) in Lemma 5 proof ✓

All cross-references correctly adapted:
- KO "[명제 3](#prop3)" ↔ EN "[Proposition 3](#prop3)" ✓
- KO "[예시 4](#ex4)" ↔ EN "[Example 4](#ex4)" ✓
- KO "[명제 3](#prop3)" in Example 4 ↔ EN "[Proposition 3](#prop3)" ✓

No missing content in either direction:
- Notation section (r^i, component functions, C^k) present in both ✓
- Lee's superscript notation convention (x^i not x_i) present in both ✓
- Discussion of maximal vs non-maximal atlases present in both ✓
- "all manifolds are smooth differentiable" convention present in both ✓
- Well-definedness argument for Definition 2 present in both ✓
- Proof of Proposition 3 (uniqueness of maximal atlas) complete in both ✓
- Proof of Lemma 5 (C^∞ Urysohn lemma, bump function construction) complete in both ✓
- Smooth partition of unity motivation present in both ✓
- References ([Lee], [War]) present in both ✓

## Manifold: Uniqueness_of_Submanifold
[STATUS: CONSISTENT]

Numbered items (all IDs match between KO and EN):
- ex1 (Example 1 / 예시 1)
- prop2 (Proposition 2 / 명제 2)
- def3 (Definition 3 / 정의 3)
- prop4 (Proposition 4 / 명제 4)
- prop5 (Proposition 5 / 명제 5)

LaTeX formulas: All mathematical expressions are identical between KO and EN. Every inline and display formula matches exactly, including:
- All manifold/immersion notation (Phi, Psi, bar-Phi, etc.)
- All coordinate system notation (U,varphi), (V,psi), (W,z^1,...,z^m), (V,sigma)
- All differential notation (d iota_x, d(id), etc.)
- Dimension expressions and the key inequality dim(A,T',A') < dim(A,T,A)
- The chain rule formula d iota' = d iota o d(id)
- The factorization formula (pi o gamma o Phi) o F_0 = pi o gamma o F

Cross-references: Correctly adapted. Internal anchor links (#ex1, #prop2, #def3, #prop4, #prop5) are preserved. External cross-reference to submanifolds#cor10 correctly uses /en/ path in EN vs /ko/ path in KO.

Content completeness: All sections, proofs, images, and references ([War], [Lee]) are present in both files. No missing content in either direction.

Notes:
- <em-ko> tags in KO are rendered as markdown italic (*...*) in EN; this is a formatting convention difference with no mathematical impact.
- The reference to [Example 2](#ex2) in both files points to an item defined in another post; this is identical in both files and not a translation issue.

## Field_Theory: Properties_of_Galois_Extensions
[STATUS: ISSUES FOUND]
- Both KO and EN share a LaTeX typo in the Proposition 5 proof: `\Gal9\mathbb{L}_i/\mathbb{K})` should be `\Gal(\mathbb{L}_i/\mathbb{K})` (digit 9 instead of opening parenthesis). This is a source error carried into the translation.
- KO has a typo on line 157: `contunuous` should be `continuous`. The EN version correctly renders this as `continuous`.
- KO has a typo on line 176: `충분하미` should be `충분하며`. The EN version correctly translates this as "it suffices to show that".
- Both KO and EN Proposition 3 proof contain `\mathbb{M}\mathbb{K}(x)` which appears to be missing an operator (likely `\mathbb{M}=\mathbb{K}(x)` or `\mathbb{M}:=\mathbb{K}(x)`). This is a shared source error.
- All definitions (local base, U_M(sigma), subspace topology, totally disconnected, compact, inverse limit, topological group), all propositions (2 through 5) with their proofs, and Example 1 are present in both versions with matching mathematical content.
- All LaTeX formulas are identical between KO and EN.
- Section structure matches: "Topological Structure of Galois Groups" and "Galois Cohomology" (cohomology section is a placeholder in both).
- Cross-references to other posts correctly use /en/ paths in the EN version and /ko/ paths in the KO version.

## Mirror_Symmetry: Frobenius_Manifold
[STATUS: CONSISTENT]

**IDs checked:** def1, ex2, def3, ex4, def5, prop6, prop7, ex8, prop9, ex10 -- all present in both files with matching IDs.

**LaTeX formulas:** All mathematical expressions are identical between KO and EN, including:
- Def 1 (Frobenius algebra condition)
- Example 2 (Poincaré pairing)
- Def 3 (isolated hypersurface singularity conditions)
- Example 4 (residue pairing formula, non-degenerate simplification, Jacobi decomposition, P^1 Hessian computation, P^1 residue pairing matrix, P^2 Hessian and residue pairing computation)
- Def 5 (all 6 conditions of Frobenius manifold)
- Proposition 6 (potential existence statement and proof)
- Proposition 7 (WDVV equation and proof, including tagged equation (1))
- Example 8 (Euclidean Frobenius manifold, Euler field, Lie derivative computations, potential, WDVV verification)
- Proposition 9 (quantum cohomology Frobenius manifold, Euler vector field formula)
- Example 10 (P^1 GW potential, third derivatives, quantum product, Euler field, Lie derivative weights, Novikov variable identification)

**Cross-references:** All adapted correctly:
- `/ko/math/` paths correctly changed to `/en/math/`
- Internal links (ex2, ex4, ex5, ex8, def5, prop6, prop7, prop9) all preserved with correct anchors
- External references to riemannian_geometry, toric_geometry, symplectic_geometry sections all adapted

**Content completeness:** No content missing in either direction. Both files have matching structure: introduction, "Frobenius Algebras" section (definitions, examples with P^1 and P^2 computations), "Frobenius Manifolds" section (motivation, Def 5), "WDVV Equation" section (Prop 6, Prop 7, discussion), "Examples" section (Ex 8, Prop 9, Ex 10), and identical reference lists.

## Multilinear_Algebra: Basis_of_Free_Modules
[STATUS: CONSISTENT]

All items verified:
- IDs: def1, prop2, def3, prop4, def5, prop6, def7, def8, def9 match in both files.
- LaTeX formulas: All 29 formula blocks are identical between KO and EN.
- Content completeness: No missing definitions, propositions, proofs, examples, or explanatory text in either direction. Both proofs for Proposition 4 are empty in both versions (consistent).
- Cross-references: All internal links correctly adapted (ko/ → en/). External references to Algebraic Structures, Linear Algebra categories properly updated.
- Section structure: 3 sections (Basis, Invariant Basis Number, Basis of an Algebra) with identical subsection ordering.

## Manifold: Examples_of_Manifolds
[STATUS: CONSISTENT]

**IDs checked (all match):**
- ex1: KO "예시 1" ↔ EN "Example 1"
- ex2: KO "예시 2" ↔ EN "Example 2"
- def3: KO "정의 3" ↔ EN "Definition 3"
- ex4: KO "예시 4" ↔ EN "Example 4"
- ex5: KO "예시 5" ↔ EN "Example 5"
- ex6: KO "예시 6" ↔ EN "Example 6"
- ex7: KO "예시 7" ↔ EN "Example 7"
- ex8: KO "예시 8" ↔ EN "Example 8"
- ex9: KO "예시 9" ↔ EN "Example 9"

**LaTeX formulas: All identical across both files.**
Key formulas verified:
- Atlas `{(\mathbb{R}^m,\id_{\mathbb{R}^m})}` (Ex1)
- Coordinate representation `\varphi_\mathcal{B}:v\mapsto [v]_{\mathcal{B}}` (Ex2)
- Transition maps `\varphi_\mathcal{B}\circ\varphi_\mathcal{C}^{-1}` (Ex2)
- `\Mat_n(\mathbb{R})`, `\mathbb{C}^n` special cases (Ex2)
- Open submanifold atlas `\mathcal{A}_V` definition (Def3)
- `\GL(n,\mathbb{R})`, `\det(A)\neq 0` (Ex4)
- Graph definition `\graph(f)=\{(x,y)\in\mathbb{R}^m\times\mathbb{R}^n\mid ...\}` (Ex5)
- Sphere chart `U_{n+1}^+`, `f(x)=\sqrt{1-\lvert x\rvert^2}` (Ex6)
- Sphere atlas `\mathcal{A}=\{(U_i^\pm, \varphi_i^\pm\mid ...\}` (Ex6)
- Transition maps with `\pm\sqrt{1-\lvert x\rvert^2}` and `\hat{x}^j` (Ex6)
- Jacobian matrix (Ex7)
- Level set `x^i=f(x^1,\ldots,\hat{x}^i,\ldots,x^n)` (Ex7)
- Zero set `F(x^1,\ldots,x^{n+1})=(x^1)^2+\cdots+(x^{n+1})^2-1` (between Ex7/Ex8)
- Equivalence relation `x\sim y\iff\exists\lambda(x=\lambda y)` (Ex8)
- `\RP^n=\RP^n/\sim`, chart maps `\varphi_i`, `\psi_i` (Ex8)
- Transition map for RP^n charts (Ex8)
- Product manifold atlas `\mathcal{A}` (Ex9)

**Cross-references: All correctly adapted.**
- `[예시 6](#ex6)` → `[Example 6](#ex6)` ✓
- `[예시 7](#ex7)` → `[Example 7](#ex7)` ✓
- `[\[위상수학\] §몫공간, ⁋명제 8](/ko/math/topology/quotient_spaces#prop8)` → `[\[Topology\] §Quotient Spaces, ⁋Proposition 8](/en/math/topology/quotient_spaces#prop8)` ✓
- `[\[위상수학\] §몫공간, ⁋명제 9](/ko/math/topology/quotient_spaces#prop9)` → `[\[Topology\] §Quotient Spaces, ⁋Proposition 9](/en/math/topology/quotient_spaces#prop9)` ✓

**Footnotes:**
- [^1]: Content about representative independence of `varphi_i` on RP^n is present and equivalent in both files. LaTeX in footnote (`[\lambda x^1,\ldots,\lambda x^{n+1}]`) is identical.

**Content completeness:** No content missing in either direction. Both files contain the same 9 examples, 1 definition, 2 references, 1 footnote, and 2 images.

**References:** Both list [Lee] and [War] identically.


## Linear_Algebra: Determinant
[STATUS: CONSISTENT]

### Numbered Items
All numbered items in KO appear in EN with identical IDs:
- def1: Definition 1 (multilinear map) -- matches
- def2: Definition 2 (alternating multilinear map) -- matches
- prop3: Proposition 3 (alternating iff antisymmetric) -- matches
- def4: Definition 4 (determinant) -- matches

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Verified formulas include:
- Main isomorphism formula: $$A=(A_1\;A_2\;\cdots\;A_n)\cong\cdots$$
- Definition 1 formula: $$f:\underbrace{V\times\cdots\times V}_\text{ {\footnotesize $n$} times}\rightarrow W$$
- Definition 2 alternating condition: $$f(v_1,\ldots, v_i, \ldots, v_j,\ldots, v_n)=-f(\ldots)$$
- Proposition 3 proof (both directions, aligned equations) -- identical
- Antisymmetric consequence: $$f(v_1,\ldots, v_i+v_j,\ldots, v_i+v_j,\ldots, v_n)=0$$
- Definition 4: $$D(e_1,\ldots, e_n)=1$$ with $$D:(\mathbb{K}^n)^n\rightarrow \mathbb{K}$$
- Geometric meaning formulas: $$\mathbb{K}=\mathbb{R}$$, $$n=3$$, $$v_1,v_2,v_3$$, $$k>0$$, etc.

### Content Completeness
No content is missing in either direction. All sections present in both:
- Intro paragraph (eigenvalue motivation)
- Definition of the Determinant (4 numbered items + surrounding prose)
- Area and Volume (unit square, two transformation rules, area definition)
- Geometric Meaning of the Determinant (signed volume interpretation)
- References ([Goc])
- Footnotes [^1] and [^2]

### Cross-References
Correctly adapted:
- KO `[명제 3](#prop3)` → EN `[Proposition 3](#prop3)`
- KO `[정의 4](#def4)` → EN `[Definition 4](#def4)`

### Images
All 4 images present in both files with identical paths and attributes:
- Determinant-1.png, Determinant-2.png, Determinant-3.png, Determinant-4.png

### Minor Formatting Note
EN file retains `<em-ko>` tags (lines 99, 124) wrapping English text (`hypervolume`, `orientation`). These are cosmetic and do not affect mathematical content.

## Mirror_Symmetry: Frobenius_Manifold
[STATUS: CONSISTENT]

All numbered items (def1, ex2, def3, ex4, def5, prop6, prop7, ex8, prop9, ex10) match between KO and EN with identical IDs.

All LaTeX formulas are identical between the two files. Spot-checked key formulas:
- Frobenius algebra definition: η(x·y,z) = η(x,y·z) ✓
- Trilinear form symmetry derivation ✓
- Poincaré pairing η(α,β) = ∫_X α⌣β ✓
- Isolated hypersurface singularity definition ✓
- Residue pairing integral formula ✓
- Non-degenerate Hessian simplification ✓
- Jacobi ring decomposition ⊕_p C ✓
- P^1 Hessian and residue pairing computation ✓
- P^2 Hessian and residue pairing computation ✓
- Frobenius manifold Definition 5 (all 6 conditions) ✓
- Proposition 6 (potential existence) and proof ✓
- Equation (1) tagged identically ✓
- Proposition 7 (WDVV equation) and proof ✓
- Example 8 (Euclidean Frobenius manifold) with Euler field and potential ✓
- Proposition 9 (quantum cohomology Frobenius manifold) with Euler vector field formula ✓
- Example 10 (P^1 GW potential, quantum product, Lie derivative weights) ✓

Cross-references are correctly adapted:
- Internal links (ex2, ex4, ex5, ex6, ex8, def5, prop6, prop7, prop9) preserved correctly in both languages.
- External references to riemannian_geometry, toric_geometry, symplectic_geometry correctly use /ko/math/ in KO and /en/math/ in EN.
- Cross-reference anchors (e.g., #def1, #ex2, #ex5, #def5, #prop6, #prop7, #prop9) are consistent.

No content is missing in either direction. Both files have matching structure:
- Introduction referencing mirror symmetry overview
- Section "Frobenius Algebras" with def1, ex2, def3, ex4
- Section "Frobenius Manifolds" with motivation and def5
- Section "WDVV Equation" with prop6, prop7, and discussion
- Section "Examples" with ex8, prop9, ex10
- Reference list (4 references identical)
## Multilinear_Algebra: Change_of_Basis
[STATUS: ISSUES FOUND]

Numbered items: All 7 items (def1, prop2, def3, prop4, prop5, def6, def7) present in both files with matching IDs.

LaTeX formulas: All mathematical formulas are identical between KO and EN. No discrepancies.

Content completeness: No content missing in either direction.

Cross-reference issue:
- In the proof of Proposition 2, the EN file contains a link with a Korean anchor:
  `[§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#행렬의-곱셈)`
  The anchor `#행렬의-곱셈` (Korean for "matrix multiplication") should be adapted to the English anchor (e.g., `#matrix-multiplication`).

## Mirror_Symmetry: Dubrovin_Connection
[STATUS: CONSISTENT]

**Numbered items / IDs:** All four numbered items match between KO and EN with identical IDs:
- def1: 정의 1 ↔ Definition 1
- prop2: 명제 2 ↔ Proposition 2
- def3: 정의 3 ↔ Definition 3
- conj4: 주장 4 ↔ Conjecture 4

**LaTeX formulas:** All LaTeX expressions are identical between KO and EN. Verified formulas include:
- Connection formulas: `\nabla^z_{\partial_\alpha}`, `\nabla^z_{\partial_z}`, `\mathcal{C}_\alpha`
- Grading: `\Lie_E(\circ)`, `\Lie_E(\eta)`, `\mu = \frac{2-d}{2}I - \nabla E`
- Curvature expansion and its z^{-1}, z^{-2} coefficient analysis
- Component forms of Proposition 2 (potentiality, associativity/WDVV)
- Proof component form: `\sum_\delta (c_{\alpha\delta}^\epsilon c_{\beta\gamma}^\delta - c_{\beta\delta}^\epsilon c_{\alpha\gamma}^\delta) = 0`
- D-module commutator: `[\partial, f] = \partial(f)`, Leibniz rule
- Quantum differential equation: `\partial_\alpha s^\beta + \frac{1}{z} \sum_\gamma c_{\alpha\gamma}^\beta\, s^\gamma = 0`
- QDE in H^2 direction: `z\, q_a \partial_{q_a} s = -\,(T_a \qtimes s)`
- A-model base and state space: `M_A`, `H_A`
- Mirror isomorphism: `\Phi \circ \nabla^z = \nabla^{GM} \circ \Phi`

**Content completeness:** All sections, definitions, propositions, proofs, and prose are present in both files. No content missing in either direction. All 10 references ([Dub], [Giv], [Iri], [EHX], [Rie], [MR], [LT], [CCIT], [Kon], [SYZ], [CK]) are present in both.

**Cross-references:** All internal anchor links (#def1, #prop2, #def3, #conj4) are preserved. External cross-references to other posts correctly use /ko/ paths in KO and /en/ paths in EN (frobenius_manifold, riemannian_geometry/connection, riemannian_geometry/Levi-Civita_connection, commutative_algebra/differentials).

**Notes:**
- KO uses "주장 4" (claim/assertion) while EN uses "Conjecture 4". This is a reasonable translation choice given the surrounding text explicitly states the statement is not a proven fact but a guiding philosophy.
- No LaTeX discrepancies found. No missing content in either direction.
## Multilinear_Algebra: Hom_and_Tensor
[STATUS: CONSISTENT]

- All 7 numbered items (prop1, prop2, prop3, cor4, cor5, def6, prop7) present in both files with matching IDs.
- All LaTeX formulas are identical between KO and EN.
- Cross-references correctly adapted: `/ko/` to `/en/` paths, Korean labels to English equivalents (e.g., "따름정리 4" to "Corollary 4", "§완전열, ⁋명제 10" to "§Exact Sequences, ⁋Proposition 10").
- No content missing in either direction.
- Minor: KO line 95 has typo "fintiely" (correctly "finitely" in EN).

## Multilinear_Algebra: Exact_Sequences
[STATUS: CONSISTENT]

All 10 labeled items (lem1, def2, prop3, prop4, prop5, prop6, prop7, def8, lem9, prop10) appear in both files with identical IDs.
All LaTeX formulas are identical between KO and EN.
All cross-references are correctly adapted (ko/ paths mapped to en/ paths, Korean section/theorem names mapped to English equivalents).
No missing content in either direction.

Note: Both files contain the same pre-existing bug -- the internal link `[Proposition 6](#def6)` / `[명제 6](#def6)` points to `#def6` but the actual ID is `prop6`. This is not a translation inconsistency but a shared defect.
## Representation_Theory: Character_Theory
[STATUS: CONSISTENT]

- All 5 sections present in both files with matching content flow.
- All numbered items (def1, prop2, def3, def4, lem5) and equation tags (1), (2) appear in both files with identical IDs.
- All LaTeX formulas are identical between KO and EN.
- All cross-references are correctly adapted (ko/ vs en/ paths).
- No missing content in either direction.

Pre-existing issues (same in both files, not translation inconsistencies):
1. Definition 3: `\rchi(hgh^{-1})=f(g)` -- `f` should be `\rchi` (typo present in both KO and EN).
2. `\rho_\std((1\;2))\begin{pmatrix}0&1\\1&0\end{pmatrix}` is missing the `=` sign before `\begin{pmatrix}` (present in both KO and EN).
## Multilinear_Algebra: Tensor_Algebras
[STATUS: CONSISTENT]

**Numbered items (IDs):** All 14 items (def1, prop2, prop3, prop4, def5, prop6, prop7, prop8, prop9, def10, prop11, prop12, prop13, prop14) present in both files with matching IDs.

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. Verified all displayed equations including tensor algebra definition, universal properties, direct sum decompositions, basis descriptions, structure constants, ideal definitions, symmetric/alternating conditions, and exterior algebra bases.

**Sections present in both:**
- Definition of Tensor Algebras / 텐서대수의 정의
- Properties of Tensor Algebras / 탠서대수의 성질들
- Mixed tensor (incomplete notes in both)
- Definition of Symmetric Algebras / 대칭대수의 정의
- Properties of Symmetric Algebras / 대칭대수의 성질들
- Definition of Exterior Algebras / 외대수의 정의
- Properties of Exterior Algebras / 외대수의 성질들

**Cross-references:** All correctly adapted (KO /ko/ paths -> EN /en/ paths; Korean labels -> English labels).

**Images:** Both reference the same image files (Tensor_Algebras-1.png, Tensor_Algebras-2.png).

**Footnotes:** [^1] present in both, with cross-references correctly adapted.

**Pre-existing content note (not a translation issue):** Proposition 12 (prop12) in both files uses `\S^n(M)` in the domain of g and "symmetric n-linear map" in the codomain description, when the exterior algebra context would suggest `\bigwedge^n(M)` and "alternating n-linear map" respectively. This appears to be an error in the Korean source faithfully preserved in the English translation.
## Multilinear_Algebra: Dual_Spaces
[STATUS: CONSISTENT]

- **Numbered items (8 total):** def1, def2, def3, def4, prop5, def6, def7, prop8 all present in both files with matching IDs.
- **LaTeX formulas:** All formulas are identical across both files, including all display math and inline math.
- **Cross-references (3 total):**
  - [Algebraic Structures §Modules, Proposition 8] adapted from `/ko/` to `/en/` path and Korean to English labels -- correct.
  - Same reference used a second time in "Transpose of Linear Maps" section -- correct.
  - [§Basis, Definition 1] adapted from `/ko/` to `/en/` path and Korean to English labels -- correct.
- **Content completeness:** Both files contain the same 5 sections with identical mathematical content. No missing definitions, propositions, proofs, or examples in either direction.
- **Note:** A stray comma after `\langle x, \xi_1\rangle` in the orthogonality formula (def2 area) exists identically in both files -- pre-existing in KO, faithfully reproduced in EN.

## Mirror_Symmetry: Mirror_Symmetry_Overview
[STATUS: ISSUES FOUND]

### 1. Numbered Items
All IDs match perfectly between KO and EN:
- def1 (charge matrix), ex2 (P^n and P^1 x P^1 examples), def3 (Landau-Ginzburg model),
  def4 (Hori-Vafa mirror), ex5 (P^1 case), ex6 (P^2 case)

### 2. LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Verified every formula including:
- Charge matrix definition and examples
- GIT quotient expression
- Jacobi ring definitions
- Hori-Vafa mirror (domain restriction and superpotential)
- Complexified Kähler class, Novikov parameter
- Quantum cup product
- Mirror symmetry statement (Jac(W_q) = QH*(X_Sigma))
- P^1 and P^2 computations (critical points, Jacobi rings, quantum cohomology rings, Gromov-Witten invariants)

### 3. Content Completeness
No content is missing in either direction. Both files cover:
- Historical Background section (string theory motivation, MSRI 1991 workshop anecdote, Givental formalism)
- Hori-Vafa Mirror Construction section (charge matrix, Landau-Ginzburg models, Jacobi ring, Novikov parameter/Kähler moduli, quantum cohomology, P^1 and P^2 examples)
- References: [CK] and [HV]

### 4. Cross-References
**ISSUE FOUND:** EN line 22 cross-reference to Symplectic Geometry uses Korean anchor:
  EN: `/en/math/symplectic_geometry/classical_mechanics#최소작용의-원리`
  The EN Classical Mechanics page has heading "## Principle of Least Action", so the correct anchor should be `#principle-of-least-action`.
  (KO anchor is correct: `/ko/math/symplectic_geometry/classical_mechanics#최소작용의-원리`)

All other cross-references are correctly adapted:
  - Toric geometry link: path adapted /ko/ -> /en/, anchor #def3 preserved (valid ID)
  - Internal links #def4, #ex2: preserved correctly (valid IDs)
  - Link text translated (e.g., "예시 2" -> "Example 2", "정의 4" -> "Definition 4")

## Manifold: Submanifolds
[STATUS: CONSISTENT]

**Files compared:**
- KO: `_posts/Math/Manifold/ko/2022-06-17-Submanifolds.md`
- EN: `_posts/Math/Manifold/en/2022-06-17-Submanifolds.md`

**1. Numbered items / IDs:** All 10 IDs match exactly.
- def1, ex2, ex3, thm4, cor5, cor6, cor7, cor8, cor9, cor10 -- present in both files with identical IDs.

**2. LaTeX formulas:** All mathematical content is identical.
- 4 multi-line display math blocks (Jacobian matrix in thm4, diffeomorphism formula in cor5 proof, coordinate map in cor6 proof, dual map computation in cor9/cor10 proofs) -- character-for-character identical.
- 196 inline `$$...$$` formulas -- all present in both files; ordering differs due to Korean vs English word order, but every formula appears in both.

**3. Content completeness:** No content is missing in either direction.
- Both files have: 2 section headings, 1 definition (3 items), 2 examples, 1 theorem (with proof), 6 corollaries (each with proof), 1 footnote, 2 references ([War], [Lee]).

**4. Cross-references:** Correctly adapted.
- Internal anchor links: `[따름정리 5](#cor5)` / `[Corollary 5](#cor5)`, etc. (cor5, cor6, cor7, cor8) -- all match.
- External cross-reference to linear algebra post: KO uses `/ko/math/linear_algebra/dimension#cor2`, EN uses `/en/math/linear_algebra/dimension#cor2` -- correctly locale-adapted. Text ("선형대수학 / §백터공간의 차원 / ⁋보조정리 2" vs "Linear Algebra / §Dimension of Vector Spaces / ⁋Lemma 2") is correctly translated.

**Pre-existing issues (in both KO and EN, not translation errors):**
- cor6 statement: uses `$$p$$` in conclusion but `$$p_0$$` was introduced as the point.
- cor8 statement: uses subscript `$$\{y_1,\ldots, y_k\}$$` instead of superscript `$$\{y^1,\ldots, y^k\}$$` used everywhere else.
- cor5 proof: `$$U=\varphi^{-1}(U)$$` likely should be `$$U=\varphi^{-1}(U')$$`.
- cor9 proof: `$$=dx^j|_p$$` uses index `j` where `i` was used upstream.
## Multilinear_Algebra: Norms_and_Traces
[STATUS: CONSISTENT]

- All 4 numbered items (def1, prop2, prop3, prop4) present in both files with matching IDs.
- All LaTeX formulas are identical across both files (6 formula blocks total).
- Proofs for prop2 and prop4 present in both; no proof for prop3 in either.
- No missing content in either direction.
- Cross-references: none explicit in this file; no issues.
- Minor issues in KO source (not translation inconsistencies):
  - KO line 97: "먼알" typo (should be "만일"); EN correctly translated as "If we regard".
  - KO line 44: broken LaTeX `$$E$-basis` (should be `$$E$$-basis`); EN correctly has `$$E$$-basis`.

## Manifold: Tangent_and_Cotangent_Bundles
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All 7 numbered items match between KO and EN with identical IDs:
- def1 (Definition 1: vector bundle over topological space)
- ex2 (Example 2: tangent bundle)
- def3 (Definition 3: bundle map)
- def4 (Definition 4: smooth functor)
- ex5 (Example 5: Hom smooth functor)
- thm6 (Theorem 6: vector bundle from smooth functor)
- def7 (Definition 7: cotangent bundle)

### LaTeX Formulas
All LaTeX formulas are mathematically identical. Display formulas match exactly:
- `$$TM=\bigsqcup_{p\in M} T_pM$$` (Ex 2)
- `$$\tilde{\varphi}(v)=\bigl(x^1(\pi(v)), \ldots, x^m(\pi(v)), dx^1(v),\ldots, dx^m(v)\bigr)$$` (Ex 2)
- Aligned transition map equation (Ex 2)
- `$$\left((\psi\circ\varphi^{-1})(p), dy^1(v), \ldots, dy^m(v)\right)$$` (Ex 2)
- `$$dy^j\left(\sum v^i\frac{\partial}{\partial x^i}\bigg|_{\varphi^{-1}(p)}\right)=\sum_{i=1}^m v^i\frac{\partial y^j}{\partial x^i}\bigg|_{\varphi^{-1}(p)}$$` (Ex 2)
- Topology basis formula (Ex 2)
- `$$v|_p\mapsto (p, dx^1(v),\ldots, dx^m(v))$$` (Ex 2)
- `$$\tilde{\varphi}=(\varphi\times\id_{\mathbb{R}^m})\circ\phi$$` (Ex 2)
- `$$\Hom(f,g)(u)=g\circ u\circ f^{-1}$$` (Ex 5)
- `$$(g+tw_i^j)\circ u\circ f^{-1}=g\circ u\circ f^{-1}+tw_i^j\circ u\circ f^{-1}$$` (Ex 5)
- `$$E_b=F((E_1)_b,\ldots,(E_n)_b)$$` (Thm 6)
- k-fold product formula (after Def 4)

Inline math uses `$$...$$` in KO and `$...$` in EN (style convention only, content identical).

### Content Completeness
No content is missing in either direction. All sections present:
- KO "벡터다발" = EN "Vector Bundles"
- KO "접다발" = EN "Tangent Bundles"
- KO "Smooth functors" = EN "Smooth Functors"
- KO "여접다발" = EN "Cotangent Bundles"

Smooth functor examples list (6 items: dual, tensor, symmetric, exterior, tensor product, direct sum) matches in both.

### Cross-References
All cross-references correctly adapted:
- `[예시 5](#ex5)` → `[Example 5](#ex5)`
- `[§미분다양체의 예시들, ⁋예시 2](/ko/math/manifold/examples_of_manifolds#ex2)` → `[§Examples of Manifolds, ⁋Example 2](/en/math/manifold/examples_of_manifolds#ex2)`
- `[선형대수학] §쌍대공간](/ko/math/linear_algebra/dual_space)` → `[Linear Algebra] §Dual Space](/en/math/linear_algebra/dual_space)`
- `[다중선형대수] §텐서대수](/ko/math/multilinear_algebra/tensor_algebras)` → `[Multilinear Algebra] §Tensor Algebras](/en/math/multilinear_algebra/tensor_algebras)` (3 occurrences)
- `[정리 6](#thm6)` → `[Theorem 6](#thm6)` (2 occurrences)

### Notes
- Both files reference **[Mil]** in the body text (KO line 98, EN line 95) without a corresponding entry in the bibliography. This is a pre-existing issue in the KO source, consistently carried to EN.
- Both files have "homomorphism" on the line after Def 1 (KO line 32, EN line 31) where "homeomorphism" was used in the definition itself. This typo is consistent across both files.
- EN includes additional front matter: `translated_at`, `translation_source: kimi-cli`.

## Multilinear_Algebra: Differential_Modules

[STATUS: ISSUES FOUND]

### ID/Numbering Check
All numbered items match between KO and EN with identical IDs: prop1, prop2, prop3, prop4, prop5, lem6, prop7, prop8, def9, ex10, prop11, prop12, prop13, prop14. No missing or extra items in either direction.

### LaTeX Formula Check
All LaTeX formulas are mathematically equivalent between KO and EN.

### Issues Found

1. **Prop 14 statement -- incorrect equation in KO (line 424):** KO states "$$E'=\mathfrak{I}/\mathfrak{I}^2$$-linear map들의 sequence" but $$E' \cong E/\mathfrak{I}$$, not $$\mathfrak{I}/\mathfrak{I}^2$$. The EN version (line 410) correctly omits this erroneous equation and simply says "the sequence of $$E'$$-linear maps". This is a mathematical error in the KO version that was corrected in translation.

2. **Prop 14 proof -- LaTeX typo in KO (line 435):** KO has `$$\overline{d)$$` with a wrong closing parenthesis instead of `$$\overline{d}$$`. EN (line 420) has the correct LaTeX `$$\overline{d}$$`.

3. **Lemma 6 proof -- shared LaTeX typo (KO line 147, EN line 142):** Both files contain `$$\orimes$$` which should be `$$\otimes$$`. The typo `\orimes` is not a valid LaTeX command and would likely render incorrectly. This typo is identical in both files, suggesting it originated in the source.

4. **Prop 12 statement -- text typo in KO (line 337):** KO has "canonica morphism들" (missing 'l' in canonical). EN (line 324) correctly has "canonical morphisms".

### Cross-Reference Check
All cross-references are correctly adapted:
- `/ko/math/multilinear_algebra/derivations#def2` -> `/en/math/multilinear_algebra/derivations#def2`
- `/ko/math/algebraic_structures/change_of_base_ring#prop5` -> `/en/math/algebraic_structures/change_of_base_ring#prop5`
- `/ko/math/multilinear_algebra/various_modules#prop2` -> `/en/math/multilinear_algebra/various_modules#prop2`
- Internal anchors (#prop1, #prop2, etc.) are identical in both files.

### Content Completeness
No content is missing in either direction. The three section headings are correctly translated:
- "미분의 functoriality" -> "Functoriality of Derivations"
- "텐서대수와 미분" -> "Tensor Algebras and Derivations"
- "Universal property" -> "Universal Property"


## Multilinear_Algebra: Matrices

[STATUS: ISSUES FOUND]

**Structural/ID Check:**
- All 4 numbered items match: def1, def2, def3, prop4 -- consistent.
- Both files use \tag{1} and \tag{2} -- consistent.
- All cross-references correctly adapted (ko/ -> en/, same anchor IDs) -- consistent.

**LaTeX Formula Check:**
- Formula (1), (2): identical in both versions.
- All displayed equations (transpose, addition, scalar multiplication, E_ij, associativity/distributivity): identical.
- No missing or extra formulas in either direction.

**ISSUE 1 (KO source typo): Definition 2 submatrix label**
- KO (line 42): `*$$X$$의 $$I\times J$$ 부분행렬*` -- says "$I\times J$ submatrix"
- EN (line 41): `the *$$I_0\times J_0$$ submatrix of $$X$$*` -- says "$I_0\times J_0$ submatrix"
- The context introduces subsets $I_0\subseteq I$, $J_0\subseteq J$, so the italicized term should refer to $I_0\times J_0$, not $I\times J$. The EN version is correct; the KO version has a typo. Fix: change `$$I\times J$$` to `$$I_0\times J_0$$` in the Korean italicized label.

**ISSUE 2 (Minor formatting): Missing closing separator in EN**
- KO has a closing `---` after the references section (line 137).
- EN is missing this trailing `---`.

**Content completeness:** No content is missing in either direction. All prose, definitions, propositions, references, and examples are present in both versions.

## Representation_Theory: Representations_of_Finite_Groups
[STATUS: CONSISTENT]

### Numbered Items
All 10 numbered items match between KO and EN with identical IDs:
- def1 (정의 1 / Definition 1): representation definition ✓
- def2 (정의 2 / Definition 2): G-invariant, subrepresentation, irreducible ✓
- def3 (정의 3 / Definition 3): direct sum, tensor product, Hom, dual, conjugate ✓
- prop4 (명제 4 / Proposition 4): categorical equivalence Rep_C(G) ≅ C[G]-Mod ✓
- def5 (정의 5 / Definition 5): G-invariant inner product, unitary representation ✓
- prop6 (명제 6 / Proposition 6): every rep admits G-invariant inner product ✓
- cor7 (따름정리 7 / Corollary 7, Maschke): decomposition into irreducibles ✓
- lem8 (보조정리 8 / Lemma 8, Schur): Schur's lemma 3 items ✓
- prop9 (명제 9 / Proposition 9): isomorphism d ✓
- def10 (정의 10 / Definition 10): isotypical summand, multiplicity ✓

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Spot-checked:
- ρ: G×V → V (def1)
- δ_x definition, convolution product, big convolution identity
- ρ̃ formula for C[G]-module structure
- Rep_C(G) ≅ C[G]-Mod (prop4)
- ⟨g·u, g·v⟩ = ⟨u, v⟩ (def5)
- ⟨v,w⟩ = ⟨ρ(g)v, ρ(g)w⟩ = ⟨ρ(g)†ρ(g)v, w⟩
- Double bracket inner product construction in prop6 proof
- C[G] ≅ ⊕ Mat_{n_i}(C) (tagged equation 1)
- d = ⊕ d_W isomorphism (prop9)
- Hom_G(W,V) = Hom_G(W, ⊕V_j) ≅ ⊕ Hom_G(W, V_j)
- V = V_1^{⊕r_1} ⊕ ... ⊕ V_k^{⊕r_k}
- V^G definition and projection map p

### Cross-References
All cross-references correctly adapted:
- Internal anchor links (#def2, #def3, #cor7, #lem8) match in both files
- External links adapted: /ko/math/algebraic_structures/algebras#def5 ↔ /en/math/algebraic_structures/algebras#def5 ✓
- Placeholder refs (##ref##) for semisimple and artin-wedderburn preserved identically ✓

### Content Completeness
No content missing in either direction. The EN file is a complete and faithful translation of the KO file. Both files end at the same point (the V = V_1^{⊕r_1} ⊕ ... decomposition), with the EN version incorporating the trailing Korean sentence into the preceding English text.
## Scheme_Theory: Complete_Intersections
[STATUS: CONSISTENT]

- **Cross-references**: KO `[§닫힌 부분스킴, ⁋정의 7](/ko/math/scheme_theory/closed_subschemes)` correctly adapted to EN `[§Closed Subschemes, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes)`.
- **Definition IDs**: def1 and def2 present in both with correct labels ("정의 1/2" vs "Definition 1/2").
- **LaTeX formulas**: All 19 distinct LaTeX expressions are identical between KO and EN. No discrepancies found.
- **Content completeness**: No content missing in either direction. Both files end at the same concluding remark about effective Cartier divisors being locally principal but not conversely.
- **Note**: In both files, Definition 1 uses `\iota\vert^{U_i}` while Definition 2 uses `\iota^{U_i}` (without `\vert`). This is a pre-existing inconsistency in both languages, not a translation issue.

## Multilinear_Algebra: Various_Modules
[STATUS: CONSISTENT]

### Structure and Sections
Both files have 4 matching sections:
- KO "핵과 여핵" ↔ EN "Kernel and Cokernel"
- KO "직접곱과 직합" ↔ EN "Direct Products and Direct Sums"
- KO "사영가군과 단사가군" ↔ EN "Projective and Injective Modules"
- KO "평탄가군" ↔ EN "Flat Modules"

### Numbered Items (IDs)
All IDs match exactly between KO and EN:
- prop1 (명제 1 ↔ Proposition 1)
- prop2 (명제 2 ↔ Proposition 2)
- def3 (정의 3 ↔ Definition 3)
- prop4 (명제 4 ↔ Proposition 4)
- prop5 (명제 5 ↔ Proposition 5)
- prop6 (명제 6 ↔ Proposition 6)
- def7 (정의 7 ↔ Definition 7)
- Tags (1), (2), (3) all present in both files

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Verified all 20+ display equations including tagged equations (1), (2), (3).

Note: Both files share a pre-existing LaTeX typo on the tensor product isomorphism line (`M_i\otimes_AN)` has a stray closing parenthesis), and both files have `\Hom_\lMod{A}(M_1,A)` instead of `\Hom_\lMod{A}(M_1,N)` in the contravariant exact sequence discussion. Since these appear identically in both files, they are translation-consistent (the errors preexist in the source).

### Cross-References
All internal cross-references correctly adapted:
- KO `/ko/` paths ↔ EN `/en/` paths
- KO "§기저, ⁋명제 2" ↔ EN "§Bases, ⁋Proposition 2" (link to basis_of_free_modules#prop2)
- KO "[정의 3](#def3)" ↔ EN "[Definition 3](#def3)"
- KO "[명제 4](#prop4)" ↔ EN "[Proposition 4](#prop4)"
- All external references to Algebraic Structures and Category Theory correctly translated with proper permalinks

### Content Completeness
No content missing in either direction. All definitions, propositions, proofs, and explanatory text present in both files.
## Ring_Theory: Chinese_Remainder_Theorem
[STATUS: CONSISTENT]

**IDs:** All 6 items (def1, prop2, prop3, prop4, prop5, prop6) present in both files with matching IDs.

**Cross-references:** KO uses Korean labels (명제 3, 명제 4) with correct anchors (#prop3, #prop4); EN uses English labels (Proposition 3, Proposition 4) with same anchors. Correctly adapted.

**LaTeX formulas:** All formulas are identical across both files.

**Minor note:** In the proof of Proposition 2, one formula has a tiny formatting difference:
- KO: `a_1b_1+\cdots a_nb_n` (no trailing `+` after `\cdots`)
- EN: `a_1b_1+\cdots+a_nb_n` (has `+\cdots+`)
This is cosmetic only and does not affect mathematical content.

**Content completeness:** No missing content in either direction. All definitions, propositions, proofs, and prose sections are fully translated.

## Riemannian_Geometry: Connection
[STATUS: CONSISTENT]

**Numbered items (IDs):** All 6 numbered items match between KO and EN with identical IDs:
- def1 (Definition 1 / 정의 1)
- prop2 (Proposition 2 / 명제 2)
- def3 (Definition 3 / 정의 3)
- prop4 (Proposition 4 / 명제 4)
- prop5 (Proposition 5 / 명제 5)
- prop6 (Proposition 6 / 명제 6)

**LaTeX formulas:** All mathematical formulas are identical between KO and EN. Verified:
- Definition 1: connection map, Leibniz rule
- Proposition 2: locality conditions
- Proof of Proposition 2: bump function argument, coordinate expression
- Lie derivative vs connection comparison (L_{fX}Y expansion)
- Equation (1): expansion of nabla_X(sum Y^j E_j)
- Connection coefficients Gamma_{ij}^k
- Euclidean connection formula
- Proposition 4: dual connection definition
- Proof of Proposition 4: Leibniz rule verification
- Proposition 5: tensor extension conditions, Leibniz rule on simple tensors, value computation formula, replacement identity, final nabla_XF formula
- Proposition 6: second covariant derivative identity
- Total connection: nabla f, gradient vector, second covariant derivative definition

**Cross-references:** Correctly adapted:
- KO [정의 1](#def1) -> EN [Definition 1](#def1)
- KO [명제 2](#prop2) -> EN [Proposition 2](#prop2)
- KO [§리만 계량, §§Musical isomorphism](/ko/math/riemannian_geometry/Riemannian_metric#musical-isomorphism) -> EN [§Riemannian Metric, §§Musical Isomorphism](/en/math/riemannian_geometry/Riemannian_metric#musical-isomorphism)

**Content completeness:** No content missing in either direction. Both files contain the same 6 sections with identical structure: definitions, propositions, proofs, explanatory text, and references.

## Multilinear_Algebra: Determinants
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All 9 labeled items match between KO and EN with identical IDs:
- def1: 정의 1 / Definition 1 (determinant of u)
- prop2: 명제 2 / Proposition 2 (det(u∘v)=det(u)det(v), det(id)=1, det(u^{-1})=det(u)^{-1})
- cor3: 따름정리 3 / Corollary 3 (u bijective iff det u invertible)
- lem4: 보조정리 4 / Lemma 4 (wedge product expressed via submatrix determinants)
- prop5: 명제 5 / Proposition 5 (matrix of ∧^p(u) given by det(X_{J,I}))
- cor6: 따름정리 6 / Corollary 6 (det(α·id+βu) = Σ tr(∧^k(u)) α^{n-k} β^k)
- prop7: 명제 7 / Proposition 7 (exact sequence ι_!M → ι_!M → M_u → 0)
- def8: 정의 8 / Definition 8 (characteristic polynomial χ_u(x))
- prop9: 명제 9 (Cayley-Hamilton) / Proposition 9 (Cayley–Hamilton)

### LaTeX Formulas
All LaTeX formulas are mathematically identical between KO and EN. The only systematic difference is trailing punctuation: EN consistently adds periods/commas inside display math blocks (e.g., `$$...$$.`) while KO does not. This is a typesetting style convention, not a mathematical discrepancy.

### Minor KO-Original Typo Corrected in EN
In the proof of Proposition 5 (KO line 105, EN line 104): KO has `$$i_1<\cdots i_p$$` (missing `<` between `\cdots` and `i_p`), while EN correctly has `$$i_1<\cdots< i_p$$`. The EN translation fixes a LaTeX typo present in the Korean original.

### Content Completeness
No content is missing in either direction. Every paragraph, definition, proposition, corollary, lemma, proof, and example is present in both files with equivalent mathematical content. The section structure matches: Determinant (intro + Def 1 + Prop 2 + Cor 3), Minors of a Matrix (Lem 4 + Prop 5 + Cor 6), Characteristic Polynomial (Prop 7 + Def 8 + Prop 9).

### Cross-References
All cross-references correctly adapted:
- Internal anchor links (#def1, #prop2, #cor3, #lem4, #prop5, #cor6, #prop7, #def8, #prop9) preserved identically
- External links correctly use /ko/ paths in KO and /en/ paths in EN:
  - §행렬식의 존재성과 유일성 ↔ §Existence and Uniqueness of the Determinant
  - §스칼라의 변환 ↔ §Change of Base Ring
  - Anchor fragments (#lem2, #thm13, #def3) preserved identically

### Minor Typographic Note
KO uses "Cayley-Hamilton" (hyphen) while EN uses "Cayley–Hamilton" (en dash). No mathematical difference.

### Translation Metadata
EN includes expected fields: `translated_at: 2026-05-22T05:30:02+00:00`, `translation_source: kimi-cli`.

## Multilinear_Algebra: Symmetric_Tensors
[STATUS: ISSUES FOUND]

### ID and Structure Check
All 13 numbered items match between KO and EN with identical IDs:
def1, prop2 (items 1-3), def3, prop4 (items 1-2), cor5 (items 1-5), lem6 (items 1-2), prop7 (items 1-2), prop8 (items 1-2), prop9 (items 1-4), ex10, prop11, prop12 (items 1-2), prop13. Sections match: Introduction, Symmetric Tensors, Functoriality, Symmetric Algebra and Symmetric Tensors (with Remark), Polynomial Mappings, Symmetric Functions.

### Issues Found

1. **KO line 229 -- Typo in proof of Lemma 6: `N_H` should be `N^H`**
   - KO: `가정에 의해 $$N_1\subset N_H$$는 자명하다.`
   - EN: `By assumption $$N_1\subset N^H$$ is obvious.`
   - The EN version is correct. Throughout the post, the invariant submodule is denoted with superscript (e.g. `M^H`, `M^G`, `N^H`). The KO file uses `N_H` (subscript H) in one place, which is inconsistent with the rest of the document and with the EN translation.

### LaTeX Formula Comparison
All other LaTeX formulas are identical between KO and EN. Verified all 40+ displayed equations including:
- Relative trace definition and properties (Prop 1-2)
- S_n action on tensor powers (Def 3)
- Symmetric tensor product definition via S_{p,q}
- Proposition 4 proof (induction argument with subgroup towers)
- Corollary 5 (all 5 parts including partition formula, binomial-type identity, inclusion-exclusion formula)
- Lemma 6 proof (deposition N = N_1 + N_2)
- Proposition 7 (basis of Sym(M) via gamma products)
- Functoriality and natural isomorphism
- Symmetrization map s and its factorization through S(M)
- Proposition 8 (t composed with s-bar and vice versa)
- Proposition 9 (equivalence of 4 conditions for polynomial mappings)
- Proposition 11 (explicit polarization formula)
- Proposition 12 (isomorphism conditions)
- Symmetric function theory (elementary symmetric polynomials, Newton-type identities, splitting algebra E_f)
- Proposition 13 (universality of E_f)

### Cross-Reference Check
All cross-references are correctly adapted:
- External references use `/ko/math/` vs `/en/math/` paths appropriately
- Korean link text (명제, 따름정리, 보조정리, 참고) mapped to English (Proposition, Corollary, Lemma, Remark)
- All internal anchors (#def1, #prop2, #def3, #prop4, #cor5, #lem6, #prop7, #prop8, #prop9, #ex10, #prop11, #prop12, #prop13, #rmk1) match

### Content Completeness
No content is missing in either direction. Both files contain identical mathematical content with equivalent prose.
## Riemannian_Geometry: Riemannian_Metric
[STATUS: ISSUES FOUND]

**Structure and Definitions:**
- Both files have identical section structure: Riemannian Metric, Musical Isomorphism, Length of a Curve, Normal Bundle
- Definition 1 (def1): Present in both files with matching ID `def1`
- Definition 2 (def2): Present in both files with matching ID `def2`
- Formula tag \tag{1) (musical isomorphism): Present in both files

**LaTeX Formulas:**
- All LaTeX formulas are identical between KO and EN (12 formulas checked): exterior algebra bundle, coordinate expansion of g, sum of inner products, musical isomorphism map (1), g(X)(Y) expansion, g(X) covector formula, index lowering notation, curve length formula, distance function d_g, normal bundle inclusion.

**Cross-References:**
- KO line 28 `[\[미분다양체\] §미분형식, ⁋정의 1](/ko/math/manifold/differential_forms#def1)` correctly adapted to EN line 27 with English labels and anchor `#def1`
- KO line 28 `[\[다중선형대수\] §텐서대수, ⁋명제 11](/ko/math/multilinear_algebra/tensor_algebras#prop11)` correctly adapted to EN line 27 with English labels and anchor `#prop11`
- KO line 28 `[\[선형대수학\] §내적공간, ⁋정의 1](/ko/math/linear_algebra/inner_product_spaces)` correctly adapted to EN line 27 with English labels
- KO line 22 `[\[미분다양체\] §미분형식](/ko/math/manifold/differential_forms)` correctly adapted to EN line 25 with English labels

**ISSUE:**
- EN line 55: Cross-reference to Bilinear Forms uses Korean anchor fragment `#비퇴화-쌍선형형식` instead of the correct English anchor `#non-degenerate-bilinear-forms`. The display text is correctly translated ("§Bilinear Forms, §§Nondegenerate Bilinear Forms") but the URL fragment was not adapted. The EN Bilinear Form file has section `## Non-Degenerate Bilinear Forms` at line 59, so the link should be `(/en/math/linear_algebra/bilinear_form#non-degenerate-bilinear-forms)`.

**Content completeness:**
- No missing content in either direction. All paragraphs, definitions, examples, and remarks are present in both files.

## Scheme_Theory: Flat_Morphisms
[STATUS: ISSUES FOUND]

**ID consistency:** All 13 numbered items (def1, def2, prop3-prop8, ex9-ex11, prop12, prop13) present in both KO and EN with matching IDs.

**LaTeX formulas:** All displayed and inline LaTeX formulas are identical between KO and EN.

**Cross-references:** All cross-references correctly adapted (ko/ <-> en/, section names translated).

**Issue 1 (terminology mismatch in ex10):** In Example 10, KO line 175 says "이중원 xy=0" (이중원 = "double circle"), while EN line 175 says "the double line xy=0". "이중원" translates literally to "double circle", not "double line". The correct Korean term should be "이중직선" (double line). Note: mathematically, xy=0 is two intersecting lines rather than a double line (which would be x^2=0), so both versions have a minor inaccuracy, but the KO-EN inconsistency is the primary concern.

**Issue 2 (KO-only typo, not translation):** KO line 20 has "살펴본다" misspelled as "살편본다" in the introduction paragraph.

## Scheme_Theory: Algebraic_Groups
[STATUS: CONSISTENT]

### Numbered Items
All 20 IDs match between KO and EN: def1, ex2, def3, def4, def5, def6, def7, prop8, def9, def10, prop11, prop12, def13, def14, def15, ex16, def17, def18, def19, def20.

### LaTeX Formulas
All LaTeX formulas are identical across both files. Spot-checked every definition, proposition, example, and proof. No discrepancies found.

### Cross-References
- KO `[예시 2](#ex2)` -> EN `[Example 2](#ex2)` -- correctly adapted
- KO `[§스킴, ⁋예시 10](/ko/math/scheme_theory/schemes#ex10)` -> EN `[§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10)` -- correctly adapted (permalink prefix changed)
- KO `[정의 15](#def15)` -> EN `[Definition 15](#def15)` -- correctly adapted

### Content Completeness
No content missing in either direction. Both files contain identical:
- 8 definitions (def1, def3-7, def9-10, def13-15, def17-20)
- 2 propositions with proofs (prop8, prop11, prop12)
- 2 examples (ex2, ex16)
- 4 references ([Spr], [Hum], [Mil], [MFK])
- All prose sections (intro, section transitions, concluding remarks)

## Scheme_Theory: Closed_Subschemes_of_Projective_Spaces
[STATUS: CONSISTENT]

Both files are 19 lines long, containing only front matter and a single introductory paragraph. No definitions, theorems, propositions, proofs, examples, corollaries, or lemmas are present in either file.

**LaTeX formulas (5 total, all identical):**
- `$$\mathbb{P}_\mathbb{K}^n$$`
- `$$\mathbb{P}^n$$` (x3)
- `$$\mathbb{K}[\x_0,\ldots, \x_n]$$`

**Cross-references (1 total, correctly adapted):**
- KO: `[§사영스킴, ⁋정의 4](/ko/math/scheme_theory/projective_schemes)`
- EN: `[§Projective Schemes, ⁋Definition 4](/en/math/scheme_theory/projective_schemes)`
  - Path correctly changed from `/ko/` to `/en/`
  - Section name and label correctly translated

**Numbered items:** None exist in either file.

**Content completeness:** The EN paragraph is a faithful, complete translation of the KO paragraph. No content is missing in either direction.
## Multilinear_Algebra: Matrices_and_Linear_Maps
[STATUS: ISSUES FOUND]

### Numbered Items
All 5 numbered items match between KO and EN with identical IDs:
- def1 (Definition 1 / 정의 1)
- prop2 (Proposition 2 / 명제 2)
- prop3 (Proposition 3 / 명제 3)
- cor4 (Corollary 4 / 따름정리 4)
- prop5 (Proposition 5 / 명제 5)

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. No discrepancies found in any definition, proposition, corollary, proof, or inline formula.

### Content Completeness
No content is missing in either direction. All sections, proofs, and explanatory text are present in both versions.

### Cross-References
- def6 anchor in dual_spaces link: OK (custom ID works across languages)
- prop8 anchor in dual_spaces link: OK
- thm5 anchor in ftla link: OK
- **ISSUE**: EN line 93 references `[§Matrices, §§Matrix Multiplication](/en/math/multilinear_algebra/matrices#행렬의-곱셈)`. The anchor `#행렬의-곱셈` is Korean but points to the English Matrices page, whose heading is `## Matrix Multiplication` generating anchor `#matrix-multiplication`. This cross-reference is likely broken. The anchor should be adapted to `#matrix-multiplication`.
- prop2 internal link in EN: OK
- def6 anchor in hom_and_tensor link: OK (custom ID)

**Issue 3 (broken LaTeX in KO prop6 proof):** Lines 116-117 of KO have a LaTeX formula split across lines: line 116 ends with `소아이디얼 $$` and line 117 starts with `\mathfrak{p}$$에 대한`. This `$$\mathfrak{p}$$` block is broken by a line break, which may cause rendering failure in MathJax/KaTeX. The EN version correctly has `$$\mathfrak{p}$$` on a single line (line 116).

## Scheme_Theory: Schemes
[STATUS: CONSISTENT]

**Numbered Items (IDs):**
All 10 numbered items match between KO and EN with identical IDs:
- def1 (Definition 1)
- lem2 (Lemma 2 / 보조정리 2)
- lem3 (Lemma 3 / 보조정리 3)
- def4 (Definition 4 / 정의 4)
- def5 (Definition 5 / 정의 5)
- def6 (Definition 6 / 정의 6)
- ex7 (Example 7 / 예시 7)
- ex8 (Example 8 / 예시 8)
- lem9 (Lemma 9 / 보조정리 9)
- ex10 (Example 10 / 예시 10)

**LaTeX Formulas:**
All mathematical formulas are identical between KO and EN, including:
- Stalk isomorphism $(\ast)$
- Principal open subset isomorphism $(\ast\ast)$
- The full $\Hom$ adjunction chain in the proof of Lemma 2
- Union formula $U\cap V=\bigcup_{i\in I} D(f_i)$ in Lemma 3 proof
- Residue field computation $\kappa(x)\cong A_{\mathfrak{p}_x}/\mathfrak{p}_xA_{\mathfrak{p}_x}\cong \Frac(A/\mathfrak{p}_x)$
- $X_f$ and $\supp(f)$ definitions
- All formulas in Examples 7, 8, and 10
- Cocycle condition in Lemma 9
- Fiber product computations for global sections in Example 10

**Cross-References:**
All internal and external cross-references are correctly adapted:
- KO paths use `/ko/math/...`, EN paths use `/en/math/...` consistently
- All anchor IDs (e.g., #prop9, #lem8, #def10, #lem11, #ex12) match between versions
- Topology and commutative algebra references correctly adapted with locale-aware paths

**Content Completeness:**
No content is missing in either direction. Both files contain all the same sections, definitions, propositions, proofs, examples, and concluding remarks.

**Minor observation (not a translation issue):**
Both files use `f_{ii}` instead of `\varphi_{ii}` in Lemma 9 (line 216 in KO, line 211 in EN). Since the morphisms are denoted $\varphi_{ij}$, this appears to be a pre-existing typo in the Korean original that was faithfully carried into the English translation.

## Scheme_Theory: Properties_of_Scheme_Morphisms
[STATUS: CONSISTENT]

- All 17 numbered items (def1-def17, prop3, prop4, prop6, prop7, prop9, prop14, ex15) present in both files with matching IDs.
- All LaTeX formulas are identical between KO and EN, including: adjunction Hom formulas, morphism definitions (def10, def11, def12, def17), proof equations in prop3/prop7, and all example formulas in ex15 (ring maps, Spec morphisms, prime ideal computations).
- No content missing in either direction: all definitions, propositions, proofs, examples, explanatory paragraphs, and images are present in both.
- Cross-references correctly adapted: internal refs use same IDs (e.g., #def1, #prop7); external refs use `/ko/math/...` in KO and `/en/math/...` in EN with translated section names (e.g., "보조정리" to "Lemma", "명제" to "Proposition", "정의" to "Definition").
- Note: def10 in both files uses `\varphi^\ast \mathscr{O}_{\varphi^{-1}}(V)` which appears to be a pre-existing typo (should likely be `\varphi^\ast \mathscr{O}_{\varphi^{-1}(V)}(V)` as in def11), but this is consistent across both languages.

## Scheme_Theory: Projective_Schemes
[STATUS: CONSISTENT]

All 12 numbered items (def1, def2, lem3, def4, def5, cor6, cor7, lem8, lem9, thm10, lem11, ex12) present in both files with identical anchor IDs. All LaTeX formulas are identical between KO and EN. All cross-references correctly adapted (/ko/ to /en/ paths, Korean names to English names, anchor IDs preserved). Internal self-references also correct. No content missing in either direction.

Minor note: Korean original has a typo at line 179 ("석함" instead of "속함"), but this is not a translation issue -- the EN correctly renders the intended meaning.

**Issue 4 (mixed Korean-English typo in KO prop6 proof):** Line 116 of KO contains "필tration" which mixes Korean "필" with English "tration". This should be either "filtration" (pure English) or "여과" / "필터레이션" (Korean terms). The EN version correctly uses "filtration".

## Scheme_Theory: Valuative_Criteria
[STATUS: ISSUES FOUND]

**IDs**: All 11 numbered items (def1, ex2, def3, prop4, lem5, thm6, cor7, def8, thm9, cor9, thm10) match between KO and EN.

**LaTeX**: All mathematical formulas are identical between KO and EN.

**Cross-references**: Adapted correctly (KO links to Korean pages, EN to English pages).

**Issues found:**

1. **KO line 90 (Proposition 4 proof) — wrong cross-reference ID**: KO says `[보조정리 4](#lem4)` but the lemma is labeled "보조정리 5" with id `lem5`. The EN version at line 87 correctly uses `[Lemma 5](#lem5)`. Fix: change `#lem4` to `#lem5` and update the display text to "보조정리 5".

2. **KO line 30 (Definition 1, item 4) — stray character**: "합성으로 ㅅ분해할 수 있는" contains an errant Korean consonant "ㅅ" before "분해". Should be "합성으로 분해할 수 있는".

3. **KO line 131 (Corollary 7, item 1) — typo**: "closed ummersion" should be "closed immersion" (misspelling of "immersion").

4. **KO line 151 (Theorem 9) — wrong criterion stated**: The theorem text says "f가 **separated**인 것은" but Theorem 9 is the valuative criterion for **properness**, not separatedness. It should read "f가 **proper**인 것은". The EN version at line 147 correctly says "f being **proper**".

5. **Both KO line 147 and EN line 143 — circular cross-reference**: The text preceding Theorem 9 reads "Just as for [Theorem 9](#thm9), there is also a valuative criterion for proper morphisms." This is circular since Theorem 9 IS the properness criterion. The reference should be to Theorem 6 (#thm6), which is the separatedness criterion that the properness criterion parallels.
## Set_Theory: Axiom_of_Choice
[STATUS: CONSISTENT]

**IDs/Numbered items:** All 5 IDs match exactly between KO and EN:
- thm1 (Theorem 1 / Zermelo)
- lem2 (Lemma 2 / Tarski-Bourbaki)
- def3 (Definition 3 / inductive)
- thm4 (Theorem 4 / Zorn's lemma)
- prop5 (Proposition 5)

**LaTeX formulas:** All LaTeX expressions are identical across both files, including inline and display math. Verified:
- `\mathcal{S}`, `\mathcal{P}(A)`, `\mathcal{M}`, `\mathcal{F}`, `\mathcal{C}`
- `p:\mathcal{S}\rightarrow A`, `p(X)\not\in X`, `p(S_x)=x`
- `M\not\in\mathcal{S}`, `R\subseteq A\times A`, `R=\pr_1R`
- `M=\bigcup_{G\in\mathcal{M}}\pr_1G`, `S_a=M\in\mathcal{S}`
- `(\mathbb{R},\leq)`, `\preceq`
- Display math for `\tilde{f}(X)` piecewise definition: identical
- `\mathcal{S}=\mathcal{P}(A)\setminus\{A\}`, `\mathcal{P}(A)\setminus \{\emptyset\}`

**Content completeness:** No content missing in either direction. All proofs, definitions, theorems, propositions, and the equivalence argument at the end are present in both files.

**Cross-references:** Correctly adapted:
- KO `/ko/math/set_theory/ordinals#ex3` ↔ EN `/en/math/set_theory/ordinals#ex3`
- KO `/ko/math/set_theory/well_ordering#prop4` ↔ EN `/en/math/set_theory/well_ordering#prop4`
- KO `/ko/math/set_theory/well_ordering#lem5` ↔ EN `/en/math/set_theory/well_ordering#lem5`

**References:** Both cite [HJJ] and [Bou] with identical bibliographic details.

No issues found.

## Multilinear_Algebra: Derivations
[STATUS: CONSISTENT]

### IDs and Numbered Items
All 12 IDs match between KO and EN:
- def1 (Definition 1: Commutation factor) ✓
- def2 (Definition 2: ε-derivation) ✓
- prop3 (Proposition 3: ε-bracket of derivations) ✓
- prop4 (Corollary 4: Properties in Z-graded case) ✓
- prop5 (Proposition 5: Polynomial identity for derivations) ✓
- prop6 (Proposition 6: ker(d) is graded subalgebra) ✓
- prop7 (Proposition 7: Derivative of inverse) ✓
- prop8 (Proposition 8: Extension to field of fractions) ✓
- prop9 (Proposition 9: Z_ε element gives derivation) ✓
- def10 (Definition 10: ad_ε(z)) ✓
- prop11 (Proposition 11: Properties of ad) ✓
- cor12 (Corollary 12: Lie bracket of ad maps) ✓

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. No formulas were added, removed, or altered in either direction.

### Cross-References
All cross-references correctly adapted:
- `[정의 1](#def1)` ↔ `[Definition 1](#def1)` ✓
- `[정의 2](#def2)` ↔ `[Definition 2](#def2)` ✓
- `[명제 7](#prop7)` ↔ `[Proposition 7](#prop7)` ✓
- Tensor algebra cross-reference correctly adapted between /ko/ and /en/ paths ✓

### Content Completeness
No content is missing in either direction. All sections, definitions, propositions, proofs, and examples are present in both files.

### Notes: Shared Source Bugs (present identically in both files)
These bugs exist in the KO source and were faithfully preserved in the EN translation:

1. **prop7 proof cross-reference error**: Both files reference `[명제 5](#prop5)` / `[Proposition 5](#prop5)` for `d(1) = 0`, but this result is proved in prop6, not prop5.

2. **prop7 proof LaTeX mismatched parentheses**: Both have `d(x))x^{-1}` (extra closing paren) and `x(d(x^{-1})` (missing closing paren).

3. **prop8 proof variable name error**: Both reference `$$B$$` instead of `$$K$$` when discussing the field of fractions representation `u/v`.

4. **prop11 proof part 2 typos**: Both have `ax` (should be `zx`), `ay` (should be `zy`), `ya` (should be `yz`), `\xi xz` (missing closing paren, should be `\xi) xz`), and `zeta` (should be `\zeta`).

5. **prop11 statement typo**: Both write `[d, \ad(a)]` instead of `[d, \ad(z)]`.

### Notes: KO-Only Issue
- **KO line 290**: Garbled Korean text `ㅁ낮곻나다는 것은` (should be `만족한다는 것은`). The EN translation correctly conveys the intended meaning ("satisfies the condition").
## Set_Theory: Directed_Set
[STATUS: CONSISTENT]

**IDs:** All 8 numbered items (def1, prop2, prop3, def4, def5, prop6, prop7, prop8) present in both files with matching IDs.

**LaTeX:** All mathematical formulas are identical between KO and EN.

**Content:** No missing content in either direction. All definitions, propositions, proofs, examples, images, and the reference section are fully accounted for.

**Cross-references:**
- KO `/ko/math/set_theory/order_relations#rmk1` correctly adapted to EN `/en/math/set_theory/order_relations#rmk1`
- KO `/ko/math/set_theory/monotone_functions#rmk2` correctly adapted to EN `/en/math/set_theory/monotone_functions#rmk2`

**Notes:** No issues found.

## Scheme_Theory: Dimension_Schemes
[STATUS: CONSISTENT]

**Items checked:** def1, prop2, ex3, prop4, prop5, def6, prop7, thm8, prop9, prop10, prop11 (11 total)

**Numbered IDs:** All 11 IDs match between KO and EN with correct type mapping (정의→Definition, 명제→Proposition, 예시→Example, 정리→Theorem).

**LaTeX formulas:** All formulas are identical between KO and EN. Spot-checked: Spec notation, tensor products, Galois groups, codimension notation, Krull dimension, transcendence degree, polynomial expansions in Noether normalization proof, prime ideal chains.

**Cross-references:** All references correctly adapted:
- `/ko/` paths → `/en/` paths
- Korean section/item names → English equivalents (e.g., §스펙트럼→§Spectra, ⁋명제→⁋Proposition, §올곱→§Fiber Products)
- `##ref##` placeholders preserved identically (normalization, going_down)
- Anchor links preserved (e.g., #prop5, #def10, #prop16)

**Content completeness:** No content missing in either direction. All definitions, propositions, examples, proofs, and prose paragraphs present in both files.

**Minor note:** In the proof of Theorem 8 (Noether normalization lemma), the presentation order of two equations differs slightly -- in KO, `f(y_1,...,y_m)=0` appears before the general polynomial formula tagged (*), while in EN the general polynomial appears first and then `f(y_1,...,y_m)=0` is stated as the condition it satisfies. Mathematical meaning is identical; this is a natural prose reordering in translation.


## Scheme_Theory: Closed_Subschemes
[STATUS: ISSUES FOUND]

### Numbered Items
All 14 labeled items match between KO and EN with correct IDs:
- ex1: 예시 1 / Example 1
- def2: 정의 2 / Definition 2
- prop3: 명제 3 / Proposition 3
- prop4: 명제 4 / Proposition 4
- def5: 정의 5 / Definition 5
- prop6: 명제 6 / Proposition 6
- def7: 정의 7 / Definition 7
- def8: 정의 8 / Definition 8
- lem9: 보조정리 9 / Lemma 9
- def10: 정의 10 / Definition 10
- ex11: 예시 11 / Example 11
- cor12: 따름정리 12 / Corollary 12
- ex13: 예시 13 / Example 13
- def14: 정의 14 / Definition 14

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN (20+ display formulas checked).

### Cross-References
All cross-references are correctly adapted:
- /ko/ paths → /en/ paths
- Korean section names → English section names (e.g., §스킴 → §Schemes, §아핀스킴 → §Affine Schemes, §스펙트럼 → §Spectrums)
- Korean label text → English label text (e.g., ⁋보조정리 2 → ⁋Lemma 2, ⁋명제 9 → ⁋Proposition 9)
- Internal anchor references ([명제 3](#prop3) → [Proposition 3](#prop3), etc.)

### Content Completeness
No mathematical content is missing in either direction. Both files have identical structure, theorems, proofs, examples, and references.

### ISSUES FOUND
**ISSUE 1 (Major): EN body text remains in Korean.** The English file has only the following elements translated to English: (a) section headers, (b) `<ins>` item labels (e.g., "예시 1" → "Example 1"), (c) `<summary>` tags ("증명" → "Proof"), (d) one instance of `<em-ko>작은</em-ko>` changed to `*smaller*`, and (e) the references header ("참고문헌" → "References"). All explanatory prose between formulas — every paragraph, every sentence of mathematical exposition — remains in Korean. The EN file is effectively the KO file with only structural labels translated, not a proper English translation.

**ISSUE 2 (Minor): KO-only `<em-ko>` tag.** KO line 199 uses `<em-ko>작은</em-ko>` for Korean emphasis annotation. The EN file correctly replaces this with `*smaller*` (markdown italic). This is properly handled.


## Ring_Theory: Polynomial_Rings
[STATUS: CONSISTENT]

### Numbered Items
All 21 numbered items (IDs) present in both files with matching IDs:
- rmk, def1, prop2, lem3, prop4, prop5, prop6, prop7, prop8, prop9, prop10, prop11, prop12, prop13, prop14, cor15, thm16, def17, prop18, prop19, prop20

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN. Checked: N^(I) definition, |nu| formula, graded ring decomposition, degree definition, Prop 2 degree formulas, leading term/coefficient formulas, product expansion formula, Prop 5 division equation, all proof formulas (induction steps in Prop 5, 8, 9, 10, 11, 12, 13, 14, Cor 15, Thm 16, Prop 18), derivation formula and Leibniz rule, cardinality chain in Prop 13, Gauss lemma proof formulas, power series order formulas, Prop 19 and Prop 20 statements.

### Cross-References
All cross-references correctly adapted between languages:
- Internal links: #def7, #lem3, #prop2, #prop4, #prop6, #prop9, #prop14, #cor15 all correctly linked
- External links: algebraic_structures/algebras#def7, ring_theory/integral_domains#thm7, ring_theory/integral_domains#prop17, multilinear_algebra/derivations, set_theory/natural_numbers#prop12 all use correct /ko/ vs /en/ prefixes
- Link text properly translated (e.g., "보조정리 3" → "Lemma 3", "명제 6" → "Proposition 6", "따름정리 15" → "Corollary 15", "정리 16" → "Theorem 16")

### Content Completeness
No content missing in either direction. All sections present:
- KO "다항식의 차수" ↔ EN "Degree of Polynomials"
- KO "일변수다항식" ↔ EN "Univariate Polynomials"
- KO "인수분해" ↔ EN "Factorization"
- KO "유리식환" ↔ EN "Fields of Rational Functions"
- KO "멱급수환" ↔ EN "Formal Power Series Rings"
- All proofs (11 total), introductory text, and explanatory paragraphs faithfully translated.

### Pre-existing Typos (consistent in both files, not translation issues)
1. Proposition 2 item 1 (KO line 74, EN line 71): `p+q\neq 0` should be `u+v\neq 0` — both files have same typo.
2. Polynomial representation (KO line 44/62, EN line 43/59): `a_\nu` used in sum but `\alpha_\nu` in the finiteness condition — both files have same inconsistency.
3. Proposition 19 item 2 (KO line 502, EN line 486): `\omega(uv)+\omega(u)+\omega(v)` should be `\omega(uv)=\omega(u)+\omega(v)` — both files have `+` instead of `=`.
4. Order inequality formula (KO line 487, EN line 471): Stray closing parenthesis `)` after `\omega(v)` in the text — both files have same extra paren.

## Scheme_Theory: Fiber_Products
[STATUS: ISSUES FOUND]

1. **Broken cross-reference in KO source (line 44):** The KO file references `[정리 6](#thm6)` but no item with `id="thm6"` exists in the file. The existence theorem is actually labeled "정리 8" with `id="thm8"` (line 144). The EN file correctly references `[Theorem 8](#thm8)`. This is a pre-existing bug in the Korean source that the English translation correctly fixed.

2. **Typo in KO source (line 136):** The KO file contains "aßffine" (using eszett ß instead of "ff") in Lemma 7's statement. The EN file correctly spells "affine". This is a pre-existing typo in the Korean source.

3. All 15 numbered items (def1, prop2, lem3, lem4, lem5, lem6, lem7, thm8, ex9, lem10, ex11, def12, ex13, prop14, prop15) are present in both files with matching IDs.

4. All LaTeX formulas are identical between KO and EN. The EN file adds standard English trailing punctuation (periods/commas) after some display-math blocks, which is correct style.

5. No content is missing in either direction. Both files contain the same definitions, propositions/lemmas, proofs, examples, and explanatory paragraphs.

6. Cross-references in EN are correctly adapted: internal links updated from `/ko/` to `/en/` paths, and mathematical term names translated consistently (보조정리=Lemma, 정리=Theorem, 명제=Proposition, 예시=Example, 정의=Definition).
## Set_Theory: Equivalence_Relations
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All 7 items match between KO and EN:
- def1 (Definition 1 / 정의 1)
- ex2 (Example 2 / 예시 2)
- prop3 (Proposition 3 / 명제 3)
- def4 (Definition 4 / 정의 4)
- ex5 (Example 5 / 예시 5)
- lem6 (Lemma 6 / 보조정리 6)
- prop7 (Proposition 7 / 명제 7)

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN:
- Definition 1 transitivity formula: `$(x\mathrel{R}y)\wedge(y\mathrel{R}z)\implies x\mathrel{R}z$`
- Proposition 3 conditions: `$\pr_1R=A,\qquad R=R^{-1},\qquad R\circ R=R$`
- Proof equation (1): `$(x,y)\in R\iff (y,x)\in R\iff (x,y)\in R^{-1}$`
- Lemma 6 proof: `$R(y)\subseteq R(R(x))=(R\circ R)(x)=R(x)$`
- All other inline formulas match.

### Content Completeness
No missing content in either direction. All definitions, examples, propositions, proofs, prose paragraphs, images, and figure captions are present in both versions.

### Cross-References
Cross-references correctly adapted:
- KO `[§집합의 합, ⁋정의 1](/ko/math/set_theory/sum_of_sets#def1)` → EN `[§Sum of Sets, ⁋Definition 1](/en/math/set_theory/sum_of_sets#def1)`
- KO `[§이항관계들 사이의 연산, ⁋명제 6](/ko/math/set_theory/operation_of_binary_relations#prop6)` → EN `[§Operations on Binary Relations, ⁋Proposition 6](/en/math/set_theory/operation_of_binary_relations#prop6)`
- Internal links `[명제 3](#prop3)` and `[Example 2](#ex2)` preserved correctly.

### Minor Note
EN file uses `<em-ko>` tags on line 91 for English words "smallest" and "largest". This is a leftover from the Korean version's custom emphasis tag and is not a mathematical issue.


## Ring_Theory: Integral_Domains
[STATUS: CONSISTENT]

- All 19 labeled items (Definitions 1, 2, 4, 8, 11, 16; Propositions 3, 5, 6, 10, 12, 14, 17, 18; Theorems 7, 19; Corollary 9; Examples 13, 15) present in both files with matching IDs.
- All LaTeX formulas are identical between KO and EN.
- All proofs (Propositions 3, 6, 10, 12, 14, 17, 18; Theorems 7, 19) are correctly translated.
- Internal cross-references correctly adapted with consistent labels (#def1, #def2, #prop3, #prop5, #prop6, #def8, #prop18, #ex13, etc.).
- External links correctly adapted (ko to en paths, e.g. /ko/math/algebraic_structures/field_of_fractions#def5 → /en/math/algebraic_structures/field_of_fractions#def5).
- Section structure fully matches across both files (Euclidean Domains, Principal Ideal Domains, Unique Factorization Domains).
- Notes (not translation issues, pre-existing in both):
  - Definition 1: both KO and EN define integral domain as A but refer to "norm on R" instead of "norm on A".
  - Definition 11 item 3: both files use "associate in $$R$$" when the integral domain is named $$A$$.
  - KO has minor typos ("ㅑmage" for "image" on line 54, "prime idea" missing "l" on line 186) which EN correctly renders.


## Scheme_Theory: Algebra_of_Schemes
[STATUS: CONSISTENT]
- All 13 labeled items present in both KO and EN with matching IDs: def1 (Definition 1), lem2 (Lemma 2), lem3 (Lemma 3), prop4 (Proposition 4), prop5 (Proposition 5), def6 (Definition 6), def7 (Definition 7), def8 (Definition 8), def9 (Definition 9), prop10 (Proposition 10), ex11 (Example 11), def12 (Definition 12), ex13 (Example 13).
- All LaTeX formulas are identical between KO and EN, including: structure sheaf restriction and stalk isomorphisms (Lemma 2 proof), product over open sets, nilradical primality equivalences (Lemma 3 proof), integral iff reduced+irreducible (Proposition 4 proof with claim and D_U/Z_U argument), irreducible decomposition tagged equation ($\ast$) and intersection argument (Proposition 5 proof), support formula supp(f)=Z(ann(f)) (Proposition 10 proof), associated prime product injection, and rational function definitions.
- All proofs faithfully translated: Lemma 2, Lemma 3, Proposition 4 (including Claim), Proposition 5, Proposition 10.
- Cross-references correctly adapted: internal anchors (def1, lem2, lem3, prop4, prop5, def6, def7, def8, def9, prop10, ex11, def12, ex13) match in both versions; external links use /ko/ vs /en/ prefixes consistently (e.g., §분수체 to §Field of Fractions, §위상구조 to §Topology of Schemes, §스펙트럼 to §Spectra, §동반소아이디얼 to §Associated Primes, §국소화 to §Localization, §정수적 확장 to §Integral Extensions).
- Section structure matches: Reduced Schemes and Integral Schemes, Normal Schemes, Associated Points, Rational Functions.
- References section identical ([Har] Hartshorne, [Vak] Vakil).
- Footnote [^1] present in both with correct content.
- No missing content detected in either direction.


## Set_Theory: Binary_Relation
[STATUS: CONSISTENT]
- All 7 labeled items present in both files with matching IDs: Definition 1, Example 2, Proposition 3, Remark (rmk1), Definition 5, Proposition 6, Definition 7.
- All LaTeX formulas are identical between KO and EN, including:
  - Definition 1 (binary relation as set of ordered pairs)
  - Example 2 (E = {(A,A) | A any set})
  - Proposition 3 statement and full proof (∪(∪R), set A construction with property P, set B with property Q)
  - Remark (R ⊆ pr₁R × pr₂R ⊆ A × B)
  - Definition 5 (R(A') = ⋃_{x∈A'} {y∈B | (x,y)∈R})
  - Proposition 6 statement and proof (R(X) ⊆ R(A))
  - Post-proof discussion (R(A) = pr₂{z∈R | pr₁z∈A} ⊂ pr₂R, empty set cases)
  - Definition 7 (R({x}) as section)
- Internal cross-references correctly adapted:
  - KO `#순서쌍` → EN `#ordered_pairs`
  - KO `#ex4`, `#def7`, `#prop9` anchors preserved as-is
  - All paths adapted from `/ko/` to `/en/`
- Section structure matches: intro → def1 → ex2 → prop3 → projections/source/target → remark → domain/image section (def5 → prop6 → def7)
- Footnote [^1] (Bourbaki graph convention) correctly translated.
- References section ([HJJ], [Bou]) identical in both.

## Set_Theory: Cardinals
[STATUS: CONSISTENT]
- All 9 labeled items present in both files with matching IDs: def-3, thm-2, thm-1, prop-0, def1, def2, def3, lem4, thm5.
- All LaTeX formulas are identical between KO and EN, including:
  - def1: `\id_A` bijection
  - def3: `\mathfrak{a}\leq\mathfrak{b}`
  - lem4 proof: piecewise function `h(x)=\begin{cases} f(x)&x\in C\\ x&x\not\in C\end{cases}`, set definitions `C_0=\mathfrak{b}\setminus i(\mathfrak{a})`, `C_{n+1}=f(C_n)`, `C=\bigcup C_n`
  - thm5 proof: `A=\bigcup_{\mathfrak{a}\in E}\mathfrak{a}`, `\varphi(\mathfrak{a})`, `\varphi(\mathfrak{b})`
- All proofs (lem4 Cantor-Bernstein, thm5) are fully and correctly translated with all mathematical steps preserved.
- The Axiom of Choice statement is identical in both files.
- Section structure (Review, Basic Definitions) matches across both files.
- Cross-references: Theorem 5's proof references "[Proposition](#prop0)" — this anchor target uses `prop0` while the actual element ID is `prop-0`; this is the same in both KO and EN so it is a pre-existing issue in the original, not a translation error.
- External links (Wikipedia, Class) are identical in both files.
- Reference section ([Bou] Bourbaki) is correctly translated.
- No missing content in either direction.

## Set_Theory: Examples_of_Equivalence
[STATUS: CONSISTENT]

**IDs checked:** prop1, def2, def3, prop4, def5, def6, prop7, def8 — all 8 numbered items present in both files with identical IDs.

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. Key formulas verified:
- $P(x)\wedge (x\sim_{\tiny R}y)\implies P(y)$ (Def 3)
- $p^{-1}(p(X))\supseteq X$ and subsequent saturation formulas
- $f=h\circ p$, $f=j\circ\tilde{f}=j\circ h\circ p$ (Prop 7 / canonical decomposition)
- $x\sim_{\tiny S}y\implies x\sim_{\tiny R}y$ (Def 8)
- Aligned multilinear equation in product section

**Cross-references:** All 5 internal cross-references correctly adapted:
- KO §이항관계의 연산, ⁋명제 7 → EN §Operations on Binary Relations, ⁋Proposition 7
- KO §Retraction과 section, ⁋명제 4 (×2) → EN §Retraction and Section, ⁋Proposition 4
- KO §동치관계, ⁋예시 5 → EN §Equivalence Relations, ⁋Example 5
- [정의 2], [명제 7] internal links match in both files

**Content completeness:** No content missing in either direction. All sections present:
1. Equivalence Relations Defined by Functions
2. Unary Relations and Compatible Equivalence Relations
3. Saturation of Equivalence Relations
4. Canonical Decomposition
5. Preimage of an Equivalence Relation
6. Quotient of an Equivalence Relation
7. Product of Equivalence Relations

**Images:** All 9 image references identical in both files.

**Korean terminology correctly mapped:** 포화→saturated, 세밀하다→finer, 곱→product, 증명→Proof, 참고문헌→References.

## Scheme_Theory: Topology_of_Schemes
[STATUS: CONSISTENT]

**Numbered items:** All 16 items (def1-def3, ex4-ex6, prop7, def8-def10, lem11-lem13, def14-def15, prop16) present in both KO and EN with identical IDs.

**LaTeX formulas:** All formulas are identical between KO and EN. Verified all major formulas including:
- closure/ZI/Z chain formulas (lines 33-38)
- Spec(K[x,y]/(x(x-1))) and Z(xy) counterexamples (lines 91-99)
- Noetherian chain argument with sqrt radicals (lines 117-135)
- D(f) ≅ Spec A_f and covering formula (lines 157-161)
- Nike lemma and Lemma 12 proof formulas (lines 198-231)
- sheaf inclusion and stalk isomorphism (lines 255-295)
- Product ring counterexample Z/2Z (lines 307-313)

**Cross-references:** All internal links correctly adapted from /ko/ to /en/ paths. Fragment anchors (#def1 through #prop16, #prop5, #prop9, #prop13, #prop14, #prop16, #lem11, #lem12, #cor9, #thme, #ex8) are identical. External cross-references to Topology, Commutative Algebra, Set Theory sections correctly use /en/ paths.

**Content completeness:** No missing content in either direction. All definitions, propositions, lemmas, examples, proofs, footnotes, and references sections are present and correspond.

**Note:** Both files contain `IZ(a_1) ⊆ IZ(a_2) ⊇ ...` in the Proposition 7 proof (line 122 KO, line 121 EN) where the second symbol should likely be `⊆` rather than `⊇`. This is a pre-existing issue in the KO source, faithfully reproduced in EN -- not a translation discrepancy.


## Set_Theory: Operation_of_Cardinals
[STATUS: CONSISTENT]
- All 10 labeled items present in both files with matching IDs: Definition 1, Propositions 2-6, Definition 7, Propositions 8-10.
- All LaTeX formulas are identical between KO and EN, including: cardinal sum/product notation (def1), reindexing and partition formulas (prop2), zero/one elimination (prop3), distributive law (prop4), nonzero product condition (prop5), cancellation law with piecewise function (prop6), exponentiation (def7, prop8), power set cardinality (prop9), Cantor's theorem proof with diagonal argument (prop10), and the beth sequence definition.
- All proofs are faithfully translated: prop2 (cross-references to sum_of_sets, union_and_intersection, product_of_sets, property_of_products), prop3, prop5 (reference to ordered_pair#prop10), prop6 (bijection construction), prop9, prop10 (Cantor's diagonal argument).
- Cross-references correctly adapted: all /ko/ paths changed to /en/ paths, anchor IDs (prop7, prop4, prop5, prop3, prop7, prop10) preserved correctly.
- Internal cross-reference in singleton sum discussion: KO "[명제 4](#prop4)" correctly adapted to EN "[Proposition 4](#prop4)".
- Explanatory text about finite cases (commutativity, associativity, distributive law), singleton decomposition, continuum hypothesis, and independence results (Gödel, Cohen) all present and correctly translated.
- Reference section (Bourbaki) identical.
- No missing content in either direction.

## Set_Theory: Filter_and_Ideal
[STATUS: CONSISTENT]

**Numbered items:** All 8 labeled items (def1, ex2, ex3, def4, prop5, def6, prop7, def8) present in both KO and EN with identical IDs.

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. Verified all major formulas:
- $\downarrow x=\{y\in A\mid y\leq x\}$ and $\uparrow x=\{y\in A\mid y\geq x\}$ (Example 2)
- $X\vee Y=X\cup Y,\qquad X\wedge Y=X\cap Y$ and distributive laws (Example 3)
- Prime ideal/filter conditions: $x\wedge y\in I\implies x\in I\lor y\in I$ and $x\vee y\in F\implies x\in F\lor y\in F$ (Definition 4)
- Galois connection adjunction conditions: $F(a)\leq b\iff a\leq G(b)$ and $b\leq F(a)\iff a\leq G(b)$ (Definition 6)
- $a\leq G(F(a))$, $F(G(b))\leq b$, $b\leq F(G(b))$ (monotone/antitone analysis)
- $GFG(y)=G(y)$ and $FGF(x)=F(x)$ (Proposition 7)
- $GFGF(x)=GF(x)$ (closure operator derivation)
- Closure operator three conditions (Definition 8)
- All proof steps in Proposition 5 (maximal implies prime in distributive lattice) and Proposition 7 (idempotent closure)

**Proofs:** Both proofs (Proposition 5: maximal ideal/filter is prime; Proposition 7: GFG=G) are faithfully translated with identical mathematical reasoning and all steps preserved.

**Cross-references:** All cross-references correctly adapted:
- KO [§유향집합, ⁋정의 4](/ko/math/set_theory/directed_set#def4) → EN [§Directed Sets, ⁋Definition 4](/en/math/set_theory/directed_set#def4)
- KO [\[대수적 구조\] §분수체, ⁋명제 8](/ko/math/algebraic_structures/field_of_fractions#prop8) → EN [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 8](/en/math/algebraic_structures/field_of_fractions#prop8)
- Internal links [명제 7](#prop7) → [Proposition 7](#prop7)

**Content completeness:** No content missing in either direction. All sections present:
1. Filter and Ideal (definitions, examples, lattice characterization, prime ideals/filters, ultrafilters)
2. Preimage of lower sets under increasing functions
3. Galois Connection (monotone and antitone definitions, adjunction properties, closure operators, Galois correspondence)

**Footnote:** [^1] (upward/downward closed set terminology) present in both files with equivalent content.

**References:** [Bou] Bourbaki and [Wikipedia] Galois connection identical in both versions.

## Set_Theory: Operation_of_Binary_Relations
[STATUS: CONSISTENT]
- All 9 labeled items (Definition 1, Proposition 2, Definition 3, Proposition 4, Proposition 5, Proposition 6, Proposition 7, Proposition 8, Definition 9) present in both files with matching IDs (def1, prop2, def3, prop4, prop5, prop6, prop7, prop8, def9).
- All LaTeX formulas are identical between KO and EN, including: inverse definition formula, projection equalities for inverse, (A×B)^{-1}=B×A, composition definition, inverse-of-composition identity, associativity equation, (R2∘R1)(A)=R2(R1(A)), preimage/image inclusion inequalities (Prop 7), projection-of-composition formulas (Prop 8), diagonal definition, and identity-relation equations.
- All proofs (Propositions 2, 4, 5, 6, 7, 8) are faithfully translated with identical mathematical reasoning and LaTeX.
- Cross-references correctly adapted: internal anchor links (#prop2) preserved, external links use /ko/ vs /en/ paths as appropriate.
- Korean `<phrase>` and `<em-ko>` tags correctly adapted to English equivalents in the EN version.
- Explanatory paragraphs between definitions/propositions are fully translated with no content loss.
- References section ([Bou] Bourbaki) identical in both files.
- No missing content detected in either direction.


## Set_Theory: Order_Relations
[STATUS: CONSISTENT]

**Numbered items:** All 11 labeled items present in both KO and EN with identical IDs:
- def1 (Definition 1: anti-symmetric), def2 (Definition 2: order relation), ex3 (Example 3), def4 (Definition 4: order isomorphism), def5 (Proposition 5), ex6 (Example 6: preorder from function), def7 (Definition 7: preorder relation), prop8 (Proposition 8: preorder equivalence relation), def9 (Definition 9: asymmetric/strict order), prop10 (Proposition 10), rmk1 (Remark)

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. Verified all major formulas:
- Anti-symmetry condition: $x\mathrel{R}y$ and $y\mathrel{R}x$ implies $x=y$ (def1)
- Order relation characterization: $R\circ R=R$, $R\cap R^{-1}=\Delta_A$ (prop5)
- Preorder equivalence relation: all proof steps in prop8 (reflexive, symmetric, transitive)
- Strict order derivation: asymmetry proof chain (prop10 part 1)
- Order relation from strict order: antisymmetry and transitivity proof chains (prop10 part 2)
- Remark counterexample: $\mathcal{P}(S)$ inclusion relation

**Proofs:** All proofs (Proposition 5, Proposition 8, Proposition 10) are faithfully translated with identical mathematical reasoning and all steps preserved.

**Cross-references:** All cross-references correctly adapted:
- KO [§순서쌍, ⁋명제 2](/ko/math/set_theory/ordered_pair#prop2) → EN [§Ordered Pairs, ⁋Proposition 2](/en/math/set_theory/ordered_pair#prop2)
- KO [§순서쌍, ⁋명제 3](/ko/math/set_theory/ordered_pair#prop3) → EN [§Ordered Pairs, ⁋Proposition 3](/en/math/set_theory/ordered_pair#prop3)
- KO [§동치관계, ⁋명제 3](/ko/math/set_theory/equivalence_relations#prop3) → EN [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3)
- KO [§동치관계의 예시들, ⁋정의 2](/ko/math/set_theory/examples_of_equivalence#def2) → EN [§Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2)

**Content completeness:** No content missing in either direction. All sections present:
1. Order Relations (Definitions 1-2, Example 3, Definition 4, Proposition 5)
2. Preorder Relations (Example 6, Definition 7, Proposition 8 with proof)
3. Strict Orders (Definition 9, Proposition 10 with proof, Remark)

**References:** [Bou] Bourbaki and [HJJ] Hrbacek-Jeck-Jech identical in both versions.

## Set_Theory: Monotone_Functions
[STATUS: CONSISTENT]

### Numbered Items (IDs)
All 8 labeled items match between KO and EN with correct IDs:
- prop1: 명제 1 / Proposition 1
- prop2: 명제 2 / Proposition 2
- ex3: 예시 3 / Example 3
- def4: 정의 4 / Definition 4
- rmk1: 참고 / Remark
- def5: 정의 5 / Definition 5
- rmk2: 참고 / Remark
- prop6: 명제 6 / Proposition 6

### LaTeX Formulas
All LaTeX formulas are identical between KO and EN:
- Product preorder relation definition (line 44 KO / line 46 EN): `x\leq y\iff \forall i((i\in I)\implies(x_i\leq_{\tiny R_i} y_i))`
- Proof equation (line 60): `x_i\leq y_i\leq z_i\implies x_i\leq z_i`
- Strict order difference formula (line 78): `f< g\iff\forall x\bigl((x\in A)\implies (f(x)<_{\tiny R}g(x))\bigr)`
- Definition 4 conditions: `x\leq_{\tiny R} y\implies f(x)\leq_{\tiny R'} f(y)` and `x\leq_{\tiny R}y\implies f(y)\leq_{\tiny R'} f(x)`
- Definition 5 conditions: `x <_{\tiny S} y\implies f(x) <_{\tiny S'} f(y)` and `x <_{\tiny S} y\implies f(y)<_{\tiny S'}f(x)`
- Remark 2 order formula: `m\prec n\iff ((m-n\text{ is even}) \wedge (m<n))`
- Remark 2 function: `m\mapsto \lfloor m/2\rfloor`
- Proposition 6 conditions: `v(u(x))\geq x`, `u(v(x'))\geq x'`, `u\circ v\circ u=u`, `v\circ u\circ v=v`

### Content Completeness
No content is missing in either direction. Both files have the same structure:
- Section 1: Restriction of a Preorder Relation (Proposition 1 with proof)
- Section 2: Product of Preorder Relations (Proposition 2 with proof, Example 3)
- Interlude: order relations and strict order discussion
- Section 3: Monotone Functions (Definitions 4, 5; Remarks 1, 2; Proposition 6 with proof)
- References (Bourbaki)

### Cross-References
All cross-references correctly adapted:
- KO [명제 2](#prop2) → EN [Proposition 2](#prop2) (Example 3 text)
- KO [명제 1](#prop1) → EN [Proposition 1](#prop1) (strict order discussion)
- KO [명제 2](#prop2) → EN [Proposition 2](#prop2) (strict order discussion)
- KO [예시 3](#ex3) → EN [Example 3](#ex3) (strict order discussion)

### Proofs
All 3 proofs (Proposition 1, Proposition 2, Proposition 6) faithfully translated with identical mathematical reasoning.

### Translation Notes
- EN includes translation metadata: translated_at, translation_source (kimi-cli).
- All Korean terminology correctly mapped: 원순서관계→Preorder, 단조함수→Monotone function, 증가함수→Increasing function, 감소함수→Decreasing function, 순증가함수→Strictly increasing function, 순감소함수→Strictly decreasing function.
- References section identical ([Bou] Bourbaki).


## Set_Theory: Elements_in_Ordered_Set
[STATUS: CONSISTENT]

- All 12 labeled items (def1, def2, prop3, prop4, def5, def6, prop7, prop8, prop9, prop10, prop11, prop12) plus rmk4 present in both KO and EN with matching IDs.
- All LaTeX formulas are identical between KO and EN, including: minimal/maximal element condition, least/greatest element condition, sup/inf inequalities (prop7, prop8, prop9, prop12), covering sup identity (prop10), product sup identity (prop11), and all proof formulas (order extension via ∪(x,+∞), antisymmetry argument, transitivity, minimality arguments).
- All proofs (prop3, prop4, prop7, prop8, prop9, prop10, prop11, prop12) faithfully translated with identical mathematical reasoning.
- Remark 4 (rmk4) with all 3 items correctly translated with identical LaTeX.
- Image references (Elements_in_Ordered_Set-1.png, -2.png, -3.png) identical in both files.
- Cross-references (internal anchor def1) correctly preserved.
- References section ([Bou] Bourbaki Theory of Sets) identical.
- Section structure matches exactly: Maximal/Minimal Elements, Greatest/Least Elements, Suprema/Infima, Suprema/Infima and Set Operations.
- No content missing in either direction.
- Pre-existing issues in KO original, consistently carried to EN (not translation errors):
  - Proposition 10 statement uses $$(J_k)_{i\in I}$$ where $$(J_k)_{k\in K}$$ was likely intended (both versions).
  - Remark 4 item 2 writes $$\sup_{X_1}A$$ where $$\sup_{X_1}X'$$ was intended (both versions; item 1 correctly uses $$\sup_{X_1}X'$$).
  - Proposition 10 proof has inner sup indexed by $$i\in J_k$$ but variable is $$x_j$$ (both versions; likely should be $$x_i$$ or index should be $$j\in J_k$$).


## Set_Theory: Limits
[STATUS: CONSISTENT]
- All 15 labeled items present in both files with matching IDs: Definitions 1, 2, 7, 10, 12, 13; Examples 3, 4, 15; Lemma 5, Lemma 14; Corollary 6, Corollary 9; Proposition 8, Proposition 11.
- All LaTeX formulas are identical between KO and EN. Every equation, diagram reference, and inline math expression matches exactly.
- No content is missing in either direction. Both files contain the same sections: Inverse system/inverse limit (definitions, examples, lemma, corollary, propositions) and Directed system/direct limit (definitions, lemma, example).
- Proofs for Lemma 5, Proposition 8, Proposition 11 are fully translated with identical mathematical steps.
- Cross-references correctly adapted: [예시 3](#ex3) -> [Example 3](#ex3), [정의 2](#def2) -> [Definition 2](#def2).
- All 4 image references (/Limits-1.png through /Limits-4.png) and footnote [^1] are present in both files.
- Reference to [Bou] (Bourbaki) correctly carried over.
- Note: In Definition 12, both versions write `\id_{E_i}` where the context (sets called A_i) suggests `\id_{A_i}` may be intended. This is consistent across both files, not a translation issue.
- Note: In Definition 13's universal property, both versions write `u:\varprojlim A_i\rightarrow B` where `\varinjlim` (direct limit notation) would be expected. This is consistent across both files, not a translation issue.

## Set_Theory: Ordinals
[STATUS: CONSISTENT]
- All 6 labeled items (Theorem 1, Definition 2, Example 3, Definition 4, Proposition 5, Remark 1) present in both KO and EN with matching IDs (thm1, def2, ex3, def4, prop5, rmk1).
- Peano Axioms (5 axioms): statements and LaTeX formulas identical between KO and EN.
- Theorem 1 (Recursion theorem): statement with conditions f_0=a and f_{n+1}=g(f_n,n) identical in both versions.
- Proof of Recursion theorem: 4-step proof sketch identical, including m-step computation definition, set FrakF, union F, and steps involving pr_1F=mathbb{N} and pr_2F subseteq A.
- Axiom of Infinity: identical in both versions.
- Von Neumann construction of natural numbers: all formulas match (0=emptyset, 1={emptyset}, 2={0,1}, S(x)=x cup {x}, m<n iff m in n, omega notation, S(omega), omega+1, omega+2, omega cdot 2, omega^2, omega^3, omega^omega, omega^{omega^omega}).
- Definition 2 (well-ordering): identical statement.
- Example 3: identical content (mathbb{N} well-ordered, mathbb{R} not, mathbb{R}^{geq 0} vs mathbb{R}^{>0}, mathbb{Z}).
- Definition 4 (initial segment): identical condition.
- Proposition 5: identical statement (every segment other than A itself is of the form (-infty, a)).
- Proof of Proposition 5: identical argument (least element a of A setminus S, show A setminus S = [a,infty)).
- Remark: identical example (-infty, 3] = {0,1,2,3} = (-infty, 4) in mathbb{N}.
- Final displayed formula for bigcup_{a in A} S_a with two cases: identical in both versions.
- Footnote [^1] (cardinality vs ordered set distinction): identical.
- References section identical ([HJJ] Hrbacek-Jeck-Jech, [Bou] Bourbaki).
- No content missing from either direction; paragraph-by-paragraph correspondence is complete.

## Set_Theory: Ordered_Pair
[STATUS: CONSISTENT]
- All 10 numbered items (def1, prop2, prop3, def4, lem5, prop6, def7, def8, prop9, prop10) present in both KO and EN with matching IDs and correct label translations (정의/Definition, 명제/Proposition, 보조정리/Lemma).
- All LaTeX formulas are identical between KO and EN, including: subset relation, reflexivity, transitivity, ordered pair definition $$\big\{\{x\}, \{x,y\}\big\}$$, ordered pair equality characterization, projection definitions $$\pr_1 z, \pr_2 z$$, cartesian product definition, subset condition for products, and empty product characterization.
- All proofs (prop2, prop3, lem5, prop6, prop9, prop10) are faithfully translated with identical mathematical reasoning and LaTeX formulas.
- Cross-references correctly adapted: KO `/ko/math/set_theory/order_relations#def1` → EN `/en/math/set_theory/order_relations#def1`; KO `/ko/math/set_theory/zfc_axioms#ex4` → EN `/en/math/set_theory/zfc_axioms#ex4`; KO `[정의 7](#def7)` → EN `[Definition 7](#def7)`.
- Both footnotes [^1] and [^2] present in both files with correctly translated content and adapted links.
- Section structure matches: "집합의 포함관계" → "Subset Relations", "순서쌍" → "Ordered Pairs".
- References section identical (HJJ, Bou).
- No content missing in either direction.
- Note: Both versions share a minor notational imprecision in the proof of Proposition 9 where $$(a,b)\in A\times B$$ is written instead of $$(a',b')\in A\times B$$ (KO line 174, EN line 172). This is a pre-existing issue in the Korean original, faithfully preserved in the translation.

## Scheme_Theory: Morphism_of_Schemes
[STATUS: CONSISTENT]

- All 10 numbered items (prop1, ex2, def3, ex4, ex5, def6, ex7, ex8, def9, ex10) present in both KO and EN with identical IDs.
- All LaTeX formulas are identical between KO and EN, including: scheme morphism definitions, affine scheme morphisms via ring homomorphisms, projective space construction (D_+(x_i) isomorphisms, gluing condition), Hom isomorphisms for A-scheme structure, projective morphism via f_0,...,f_n, K-point bijections (evaluation homomorphisms, maximal ideals, kernel computation), functor of points, and the sphere projection family example.
- All proofs faithfully translated: Proposition 1 (both directions), Example 2 (projective space construction), Example 7 (K-points of affine space).
- Cross-references correctly adapted with /ko/ to /en/ path prefixes and translated section/label names (e.g., §아핀스킴 → §Affine Schemes, §사영스킴 → §Projective Schemes, §닫힌 부분스킴 → §Closed Subschemes).
- No content missing in either direction.
- Pre-existing broken cross-reference (not a translation issue): Both versions in Example 8 (line 186 KO / line 177 EN) reference "Example 6" with anchor #ex6, but no Example 6 exists in this post (ex6 is Definition 6). The intended target is Example 7 (#ex7), which contains the K-point calculation being referenced. This error originates in the KO original and is faithfully preserved in the EN translation.
- Minor: EN version retains `<em-ko>` tag in Example 10 (line 207) for "a family of circles parametrized by the $x$-axis"; this should be `<em>` in the English version.
- References section identical ([Har], [Vak]).
## Symplectic_Geometry: Symplectic_Manifold
[STATUS: CONSISTENT]
- Definition 1 (symplectic form, symplectic manifold): mathematical content identical in both versions.
- Notation ($$M$$, $$\omega$$, $$d\omega=0$$, $$\omega_p:T_pM\times T_pM\rightarrow \mathbb{R}$$, $$(M,\omega)$$): consistent.
- Consequence paragraph (even dimensionality): identical logical content and notation.
- References to [MS] and [Cd]: consistent.

## Set_Theory: Operation_of_Functions
[STATUS: CONSISTENT]
- All 8 labeled items present in both files with matching IDs: Proposition 1 (prop1), Definition 2 (def2), Example 3 (ex3), Example 4 (ex4), Proposition 5 (prop5), Remark (rmk1), Definition 6 (def6), Definition 7 (def7).
- All LaTeX formulas are identical between KO and EN.
- All proofs (Proposition 1, Proposition 5) are correctly translated.
- Cross-reference correctly adapted: KO links to /ko/math/set_theory/operation_of_binary_relations#prop8; EN links to /en/math/set_theory/operation_of_binary_relations#prop8.
- Section structure fully matches (Composition of Functions, Inverse Functions, Product of Functions).
- References section identical in both files.
- Note: Proof of Proposition 1 uses mixed notation (G∘H in the blockquote, G∘F in the body). This inconsistency exists in the Korean original and is faithfully reproduced in the EN translation — not a translation issue.

## Set_Theory: Natural_Numbers
[STATUS: CONSISTENT]
- All 16 labeled items (def1, prop2, lem3, prop4, prop5, prop6, prop7, def8, prop9, thm10, cor11, def11, prop12, lem13, lem14, cor15) present in both KO and EN with matching IDs and mathematical content.
- All LaTeX formulas are identical between KO and EN across all definitions, propositions, lemmas, theorems, corollaries, and proofs.
- All proofs faithfully translated: Proposition 2, Lemma 3, Proposition 4, Proposition 5, Proposition 7, Theorem 10, Lemma 13, Lemma 14, and Proposition 12 (proof--alone block).
- Section structure matches: An Alternative Definition of Natural Numbers, Order Relations Between Natural Numbers, Properties of the Set of Natural Numbers, Definition and Properties of Infinite Sets.
- Cross-references correctly adapted from /ko/ to /en/ paths:
  - [§기수, ⁋정리 5] → [§Cardinals, ⁋Theorem 5]
  - [§정렬집합의 성질들, ⁋보조정리 7] → [§Properties of Well-ordered Sets, ⁋Lemma 7]
  - [§기수들 사이의 연산, ⁋명제 6] → [§Operations on Cardinals, ⁋Proposition 6]
  - [§서수와 정렬집합] → [§Ordinals and Well-ordered Sets]
  - [§서수들 사이의 순서관계, ⁋명제 1] → [§Order Relations Between Ordinals, ⁋Proposition 1]
  - Internal anchors (#lem3) correctly preserved.
- References section (Bourbaki Theory of Sets) identical.
- EN translation corrects two errors in the KO original in Corollary 11 (Bézout's lemma):
  1. KO has "x와 b" (reusing variable b); EN correctly has "x and y".
  2. KO has "$$ax+by$$이도록 할 수 있다" (incomplete, missing "= d"); EN correctly has "$$ax+by=d$$".
- No content missing from either direction; paragraph-by-paragraph correspondence is complete.


## Set_Theory: Product_of_Sets
[STATUS: CONSISTENT]
- All 5 labeled items match between KO and EN: Definition 1, Proposition 2, Theorem 3, Proposition 4, Proposition 5.
- All LaTeX formulas are identical between KO and EN across every displayed equation (proof of Proposition 2 algebraic chains, projection identity in Theorem 3 proof, both adjunction isomorphism display blocks in Proposition 4 proof, and the final bijection diagram equations).
- All proofs (Propositions 2, 4; Theorem 3) are faithfully translated with identical mathematical reasoning and all steps preserved.
- Cross-references correctly adapted: KO `[§집합의 합, ⁋따름정리 9](/ko/math/set_theory/sum_of_sets#cor9)` maps to EN `[§Sum of Sets, ⁋Corollary 9](/en/math/set_theory/sum_of_sets#cor9)`.
- All 3 image references match (Product_of_Sets-1.png, Product_of_Sets-2.png, Product_of_Sets-3.png) with identical style attributes.
- Terminology note: KO uses "i번째 성분함수" (i-th component function) while EN uses "i-th projection"; these are equivalent mathematical terms, not a discrepancy.
- References section identical ([HJJ] Hrbacek-Jeck-Jech, [Bou] Bourbaki).
- Minor shared note: In the proof of Theorem 3, both KO (line 86) and EN (line 88) state "f(y) and f'(y) are elements of A" where A should likely be P (the product set). This is a pre-existing issue in the KO original, faithfully reproduced in EN.
- No missing content in either direction; paragraph-by-paragraph correspondence is complete.
## Set_Theory: Retraction_and_Section
[STATUS: CONSISTENT]

All mathematical content (Propositions 1, 3, 4; Definition 2; inclusion formulas; all proofs) is consistent between KO and EN versions. Formulas, logical arguments, and diagram image references match throughout.

Minor notes:
- Both files share a typo in Proof of Proposition 4 part 2 (uniqueness argument): "$$y\in G$$" should be "$$y\in C$$" (since h: C → A). This is a pre-existing error in the Korean source, faithfully preserved in translation.
- KO line 126 has a duplicated Korean word "$$h$$는 $$h$$는" which the EN version renders correctly. No mathematical impact.

## Symplectic_Geometry: Linear_Symplectic_Geometry
[STATUS: CONSISTENT]

All mathematical content matches between KO and EN versions:

- **Definitions**: Def 1 (symplectic vector space), Def 3 (symplectic complement, isotropic/coisotropic/symplectic/Lagrangian subspaces) — identical in both languages.
- **Lemmas**: Lemma 2 (basis decomposition for skew-symmetric bilinear maps), Lemma 4 (properties of symplectic complement), Lemma 5 (symplectic quotient on W/W^ω) — all statements and proofs are mathematically identical.
- **Equations**: All displayed equations (ω conditions, basis constructions, dimension formulas, quotient definitions) are identical.
- **Cross-references**: KO references [선형대학, §쌍대공간, ⁋명제 4] and [정의 7]; EN references [Linear Algebra, §Dual Spaces, ⁋Proposition 4] and [Definition 7] — consistent linking pattern.

Minor non-mathematical note: KO line 118 contains a typo "sympelctic" (should be "symplectic") in Lemma 4 item 2, but this does not affect the mathematical content.

## Topology: Dimension

[STATUS: CONSISTENT]

All mathematical definitions and propositions are consistent between the Korean and English versions:

- **Definition 1 (Order):** Both correctly state "no point lies in more than m+1, and some point lies in exactly m+1."
- **Definition 2 (Finite dimensional):** Both match on existence of m with open refinement of order m+1.
- **Proposition 3 (Closed subspace):** Proof is consistent in both versions.
- **Proposition 4 (Union of closed subspaces):** dim X = max(dim Y, dim Z) in both.
- **Proposition 5 (Compact subspace of R^n):** Both state dimension at most n.
- **Definition 6 (Irreducible):** Both define via non-existence of nontrivial closed sets A, B with X = A ∪ B.
- **Proposition 7 (Equivalent conditions for irreducibility):** All four equivalent conditions match.
- **Proposition 8 (Union of irreducible opens):** Hypothesis and proof consistent.
- **Definitions 9-11 (Irreducible component, Krull dimension, Noetherian):** All mathematically identical.
- **Propositions 12-15:** All statements and proofs are consistent.

Minor cosmetic note: In the EN Proposition 14 proof, "irreducible closes subset" appears as a typo for "irreducible closed subset" (in the function set notation). This is not a translation issue but a typo in the EN source itself. The KO version has the correct Korean equivalent.
## Set_Theory: ZFC_Axioms
[STATUS: CONSISTENT]
- All mathematical content verified: Russell's Paradox (Example 1), Axiom of Existence, Axiom of Extensionality, Proposition 2 and its proof, Axiom Schema of Comprehension, uniqueness argument, Examples 3-6, Axiom of Pair, Axiom of Union, Axiom of Power Set.
- All formulas (LaTeX) match exactly between KO and EN.
- All logical argument structures (case analysis in Example 3, proof of Proposition 2) are identical.
- Notation consistent throughout: $\mathcal{S}$, $\emptyset$, $A\cap B$, $A\setminus B$, $\mathcal{P}(S)$, $\bigcup\mathcal{S}$.
- Footnote about complement requiring a universal set is consistent.
- References ([HJJ], [Bou], Wikipedia) match.


## Symplectic_Geometry: Classical_Mechanics
[STATUS: CONSISTENT]
- All LaTeX formulas are identical between KO and EN across every displayed equation.
- Conservation of Energy section: F=ma, K=½mv², P=mgh, E:R²→R, E(x,v)=v², E(x,v)=½kx²+½mv² all match exactly.
- Principle of Least Action section: action integral A_H(z), boundary conditions x(t₀)=x₀/x(t₁)=x₁, Hamilton's equations (∂x-dot = ∂H_t/∂y, ∂y-dot = -∂H_t/∂x) all match.
- Proposition 1 and its proof: 1-parameter family variation, integration by parts, variational argument — all LaTeX identical between KO and EN.
- Complex structure section: J₀ matrix definition, equation (1) for J₀ acting on tangent vectors, gradient ∇H, Hamilton's equation in compact form ż = -J₀∇H(z), Hamiltonian vector field X_H = -J₀∇H(z) — all identical.
- Symplectic form section: 2-form ω₀(-,-) = ⟨J₀·,·⟩, canonical symplectic form ω₀ = Σ dxʲ∧dyʲ, inner product decomposition ⟨-,-⟩ = Σ dxʲ⊗dxʲ + Σ dyʲ⊗dyʲ, computation (ω₀)_p(∂/∂xʲ, ∂/∂yᵏ) = δⱼₖ — all identical.
- Cross-references correctly adapted: KO links to /ko/math/manifold/vector_fields#thm6, EN links to /en/math/manifold/vector_fields#thm6.
- Footnote [^1] (linear complex structure definition J²=-id, C-vector space structure via (a+bi)·v := av+bJv) is fully translated with identical LaTeX.
- Reference [MS] (Mcduff-Salamon) identical in both files.
- All 4 image references (Classical_Mechanics-1 through -4.png) match with identical style attributes.
- Section structure matches: Conservation of Energy, Principle of Least Action, Symplectic Form.
- No missing content detected in either direction.

## Topology: Equivalent_Formulations_of_Topology

[STATUS: CONSISTENT]

**Structural comparison:**
- Both files have identical section structure: Closed Sets, Closure Axiom, Interior Axiom, Neighborhood Filter.
- All numbered items match: Definition 1 (Kuratowski closure axiom), Theorem 2, Definition 3, Example 4, Definition 5, Proposition 6, Proposition 7, Definition 8.

**Mathematical formulas:**
- Kuratowski closure axioms (4 conditions): identical in both.
- Interior axioms (4 conditions): identical in both.
- All inline math expressions (cl, interior, filter, base notation) are identical.
- Derivation showing monotonicity of closure operator from the third axiom: identical.
- Proof that C = {C : cl(C)=C} satisfies closed set axioms: identical in both versions.
- Definition 3 (filter conditions 1-3): identical.
- Definition 5 (filter base conditions 1-2): identical.
- Neighborhood Axiom: identical phrasing of the condition in both.
- Proposition 7 proof: identical math steps.

**Cross-references:**
- All internal links use correct /ko/ vs /en/ prefixes consistently.
- All referenced section names are properly translated (e.g., "집합의 내부, 폐포, 경계" ↔ "Interior, Closure, and Boundary").
- External links to set_theory posts are consistent.

**No issues found.** Mathematical content is fully consistent between Korean and English versions.


## Set_Theory: Union_and_Intersection
[STATUS: ISSUES FOUND]

- All 8 labeled items (Definitions 1-3, Propositions 4-8) present in both KO and EN with matching IDs and correct mathematical content.
- All LaTeX formulas are identical between KO and EN, with one exception noted below.
- All proofs are faithfully translated with matching mathematical reasoning.
- Cross-references correctly adapted (ko/ → en/ paths, Korean titles → English titles, e.g. §ZFC 공리계 → §ZFC Axioms).
- Internal anchor links (def1, def2, def3, prop4, prop5, prop6, prop7, prop8) consistent across both files.
- References section ([Bou] Bourbaki) identical in both.
- Section structure matches exactly: Family of sets, Union and intersection, Associativity, Image of a union or intersection, De Morgan's laws.

- **ISSUE 1 (KO typo, line 90)**: KO is missing an `=` sign in the intersection chain equation after Proposition 4. KO has `\bigcap_{k\in K}A_k\bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i=A_{k_0}` (two terms concatenated without an operator). EN correctly has `\bigcap_{k\in K}A_k=\bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i=A_{k_0}` with the missing `=` restored.

- **ISSUE 2 (shared typo in both files)**: In the proof of Proposition 4, the converse direction of the second equality (KO line 84, EN line 83), both versions write "$x\in A_{f(k)}$" when the variable should be "$x\in A_i$" since the quantifier is over $i\in I$. The intended meaning is clear from context (surjectivity of $f$ ensures every $i\in I$ is $f(k)$ for some $k$), but the notation is incorrect in both files. This is a pre-existing error in the KO original faithfully preserved in the translation.


## Set_Theory: Functions
[STATUS: CONSISTENT]

**Numbered items:** All 5 definitions present in both KO and EN with identical IDs:
- def1 (Definition 1: function definition), def2 (Definition 2: identity function), def3 (Definition 3: compatibility), def4 (Definition 4: extension), def5 (Definition 5: restriction)

**LaTeX formulas:** All mathematical expressions are identical between KO and EN. Verified all formulas:
- Binary relation set: `$${<}=\{(0,1),(0,2),\ldots, (1,2),(1,3),\ldots, \}$$` (same in both)
- Image of `{1}`: `$${<}(1)=\{2,3,\ldots\}$$` (same in both)
- Function definition condition: `$$A=\pr_1F$$` and `$$F(\{x\})$$` is a singleton set (same in both)
- Uniqueness condition: for every `$$x\in A$$`, unique `$$y\in B$$` such that `$$(x,y)\in F$$` (same in both)
- Graph of function: `$$F=\{(x,y)\mid (y=f(x))\wedge(x\in A)\}$$` (same in both)
- Identity function: `$$\id_A$$` defined as triple `$$(\Delta_A,A,A)$$` with `$$f(x)=x$$` (same in both)
- Arrow notation: `$$A\overset{f}{\longrightarrow}B$$` (same in both)
- Commutative square condition: `$$(i\circ g)(x)=(j\circ h)(x)$$` for all `$$x\in B$$` (same in both)
- Commutative triangle: `$$h(x)=(f\circ g)(x)$$` and `$$H=F\circ G$$` (same in both)
- Identity compositions: `$${\id_B}\circ h=f\circ g,\qquad h\circ{\id_C}=f\circ{\id_A}\circ g,\quad\cdots$$` (same in both)
- Triple identity conditions: `$${\id_A}=g\circ h\circ f,\quad {\id_B}=f\circ g\circ h,\quad {\id_C}=h\circ f\circ g$$` (same in both)
- Inverse conditions: `$$g\circ f=\id_A$$` and `$$f\circ g=\id_B$$` (same in both)
- Compatibility condition on `$$S$$` (same in both)
- Piecewise extension formula with three cases (same in both)
- Extension conditions: `$$F\subseteq F'$$` and `$$B\subseteq B'$$` (same in both)
- Restriction notation: `$$f\vert_{X}$$` (same in both)
- Footnote condition: `$$x,y\in R(a)\implies x=y$$` (same in both)

**Content completeness:** No content missing in either direction. Both files have the same structure:
1. Introduction (binary relations leading to functions)
2. Definition of a Function (Definitions 1, 2)
3. Commutative Diagrams (square, triangle, inverse diagram)
4. Extension and Restriction of Functions (Definitions 3, 4, 5)

**Cross-references:** All cross-references correctly adapted:
- KO [§이항관계, ⁋정의 7](/ko/math/set_theory/binary_relation#def7) → EN [§Binary Relation, ⁋Definition 7](/en/math/set_theory/binary_relation#def7)
- KO [§이항관계, ⁋정의 5](/ko/math/set_theory/binary_relation#def5) → EN [§Binary Relation, ⁋Definition 5](/en/math/set_theory/binary_relation#def5)
- KO [§이항관계들 사이의 연산, ⁋정의 1](/ko/math/set_theory/operation_of_binary_relations#def1) → EN [§Operations on Binary Relations, ⁋Definition 1](/en/math/set_theory/operation_of_binary_relations#def1)
- KO [§이항관계들 사이의 연산, ⁋정의 9](/ko/math/set_theory/operation_of_binary_relations#def9) → EN [§Operations on Binary Relations, ⁋Definition 9](/en/math/set_theory/operation_of_binary_relations#def9)

**Images:** All 6 images (Functions-1.png through Functions-6.png) referenced identically in both files with matching style attributes.

**Footnotes:** [^1] (singleton set cardinality remark) present in both files with equivalent content.

**References:** [Bou] Bourbaki, Theory of Sets identical in both versions.

**Translation notes:** Korean `<sub>` annotations (function, domain, constant, index set, extension, restriction) correctly omitted in EN. Korean `<em-ko>` tags correctly removed in EN.

**Pre-existing content note:** Both files state `$(1,n)\in\mathbb{N}$` (KO line 28 / EN line 25) where `$(1,n)\in{<}` was likely intended, since `<` is the binary relation being discussed. This is a shared issue in the original KO source, faithfully preserved in the EN translation.
## Set_Theory: Well_Ordering
[STATUS: CONSISTENT]

### Proposition 1
- KO and EN both define $A^\ast$ as the set of all segments of a well-ordered set $A$, state $(A^\ast,\subseteq)$ is well-ordered, and $x\mapsto S_x$ is an order isomorphism between $A$ and $A^\ast\setminus\{A\}$.
- Cross-references: "§유향집합, ⁋명제 6" → "§Directed Sets, ⁋Proposition 6"; "§서수와 정렬집합, ⁋명제 5" → "§Ordinals and Well-Ordered Sets, ⁋Proposition 5"; "§순서집합의 원소들, ⁋명제 4" → "§Elements of Ordered Sets, ⁋Proposition 4" — all consistent.

### Definition 2 (von Neumann)
- Both define an ordinal as a set $S$ whose elements are strictly well-ordered by $\in$ and each element is a subset of $S$. CONSISTENT.

### Proposition 3 (Successor ordinal)
- Both state $S(\alpha)=\alpha\cup\{\alpha\}$ is an ordinal if $\alpha$ is. CONSISTENT.

### Proposition 4 (Union of well-ordered sets)
- Both state that for a family $(A_i)_{i\in I}$ of well-ordered sets where each pair has one as a segment of the other, there is a unique well-ordering on $A=\bigcup_{i\in I}A_i$, segments of $A_i$ become segments of $A$, and every segment of $A$ (other than $A$) is a segment of some $A_i$. CONSISTENT.

### Lemma 5
- Minor note: KO has a stray closing parenthesis in "$(A_i)_{i\in I})$" (extra `)`), while EN has the correct "$(A_i)_{i\in I}$". This is a typo in the Korean source, not a translation discrepancy.
- Mathematical content is CONSISTENT.

### Proof of Lemma 5
- Both use $R_i$, $R$, $X_i$, $X_k$, $X_l$ with identical reasoning. CONSISTENT.

### Proof of Proposition 4
- Both proofs follow the same three-step structure: (1) every $A_i$ and its segments become segments of $A$; (2) $A$ is well-ordered (by showing the least element of $A_i\cap X$ is the least element of $X$); (3) every segment of $A$ is of the form $(-\infty, x)$ and lies in some $A_i$. CONSISTENT.

### Definition 6 (Successor / Limit ordinal)
- Both define successor ordinal as having a maximal element, and limit ordinal otherwise. CONSISTENT.

### Lemma 7 (Transfinite Induction)
- Both state: $\mathcal{S}$ is a collection of segments of a well-ordered set $A$ closed under (1) arbitrary unions and (2) $S_a\mapsto S_a\cup\{a\}$; then every segment of $A$ belongs to $\mathcal{S}$.
- Note: Both proofs refer to condition "(ii)" while the statement numbers the conditions 1 and 2. This is CONSISTENT between KO and EN (minor inconsistency in both versions with the numbering scheme).

### References
- Both list [HJJ] Hrbacek–Jeck–Jech (1978) and [Bou] Bourbaki (2013). CONSISTENT.

## Scheme_Theory: Spectrums
[STATUS: CONSISTENT]
- All 17 numbered items match between KO and EN with identical IDs: def1, prop2, def3, prop4, prop5, lem6, def7, prop8, prop9, def10, lem11, lem12, def13, prop14, thm15, prop16, cor17.
- All LaTeX formulas are identical between KO and EN across every definition, proposition, lemma, theorem, corollary, and proof.
- All proofs (prop4, prop5, lem6, prop8, lem12, prop14, prop16) are faithfully translated with identical mathematical reasoning and LaTeX.
- Section structure fully matches: (1) Remark, (2) Spec A as a set, (3) Spec A as a topological space, (4) Galois correspondence, (5) Classical algebraic geometry, (6) The relationship between rings and spectra.
- The summary table at the end is identical in both versions (all 8 rows: prime ideal/point, maximal ideal/closed point, prime ideal/irreducible closed subset, minimal prime ideal/irreducible component, radical ideal/closed set, ideal sum/intersection, ideal product/union, element/function).
- Cross-references to other posts (Algebraic Structures, Commutative Algebra, Topology, Set Theory) correctly adapted with /ko/ and /en/ path prefixes respectively.
- Cross-reference label translations consistent: 정의/Definition, 명제/Proposition, 보조정리/Lemma, 정리/Theorem, 따름정리/Corollary.
- External links (Nullstellensatz, Properties of Localization, Localization, Basic Notions, etc.) correctly localized.
- References section identical ([Har], [Vak]).
- No missing content detected in either direction.
- Pre-existing broken cross-references in both files (not translation errors): (1) both reference `#def12` which should be `#def13` (Definition 13 defining I(T)) in the Galois correspondence section and the classical algebraic geometry section; (2) both reference `#prop15` which should be `#thm15` in the Proposition 16 proof; (3) both reference `#thm14` which should be `#prop14` and `#prop13` which should be `#def13` in the classical algebraic geometry section.


## Topology: Compactness
[STATUS: CONSISTENT]

- All 10 labeled items match between KO and EN with correct IDs: Lemma 1 (lem1), Theorem 2 Tychonoff (thm2), Definition 3 locally compact (def3), Theorem 4 Alexandroff (thm4), Definition 5 paracompact (def5), Definition 6 partition of unity (def6), Theorem 7 (thm7), Definition 8 locally Euclidean (def8), Definition 9 topological manifold (def9), Theorem 10 (thm10).
- All LaTeX formulas are identical between KO and EN, including: ultrafilter prime property equations, one-point compactification open set characterization, partition of unity set-builder definition, and the gluing formula f = sum(phi_i f_i).
- All proofs (Lemma 1, Theorem 2, Theorem 4) are faithfully translated with identical mathematical reasoning and all steps preserved.
- Cross-references correctly adapted from /ko/ to /en/ paths (e.g., filter_convergence, compact_spaces, subspaces, continuous_functions, open_sets, other_concepts, connected_spaces).
- Section structure matches: Tychonoff theorem, Locally Compact Spaces, Topological Manifolds.
- Pre-existing typo in KO original, faithfully preserved in EN: Theorem 4 proof (KO line 95, EN line 94) says "If V contains *_{X'}" but should say "If V contains *_{X''}" since V is an open subset of X''. The first case on KO line 89 / EN line 88 correctly uses *_{X''}. This is a mathematical error in the Korean original, not a translation inconsistency.
- EN front matter includes expected translation metadata (translated_at, translation_source: kimi-cli).
- No missing content detected in either direction.

## Topology: Compact_Spaces
[STATUS: CONSISTENT]
- All 11 labeled items (Definition 1, Proposition 2, Lemma 3, Lemma 4, Corollary 5, Lemma 6, Proposition 7, Proposition 8, Proposition 9, Definition 10, Proposition 11) present in both files with matching IDs and mathematical content.
- All LaTeX formulas are identical between KO and EN versions, including: open covering definitions, subspace topology characterization, finite intersection reformulation, Hausdorff separation arguments, and compactness-to-continuity results.
- All proofs (Proposition 2, Lemma 3, Lemma 4, Corollary 5, Lemma 6, Proposition 7, Proposition 8, Proposition 9, Proposition 11) are faithfully translated with identical mathematical reasoning.
- Cross-references correctly adapted from /ko/ to /en/ paths (Hausdorff_spaces#def3, continuous_functions#thm4, equivalent_formulations_of_topology#def6).
- Internal anchor links (def1, prop2, lem3, lem4, cor5, lem6, prop7, prop8, prop9, def10, prop11) consistent in both versions.
- Section structure matches: Compact Sets, Compact Hausdorff Spaces, Compact Spaces and Continuous Functions, Finite Intersection Property.
- EN front matter includes expected translation metadata (translated_at, translation_source: kimi-cli).
- Minor pre-existing typo in both versions: Lemma 4 proof uses `y ∈ A` (line 74 KO, line 73 EN) where `y ∈ Y` is intended (A is not defined; Y is the compact subspace). This is a shared source error, not a translation discrepancy.
- Minor pre-existing index typo in both versions: Proposition 2 proof uses `(U_j ∩ Y)_{i ∈ J}` (line 42 KO, line 41 EN) where `(U_j ∩ Y)_{j ∈ J}` is intended. Consistent in both files.
- No missing or extra content detected in either direction.
## Topology: Filter_Convergence
[STATUS: CONSISTENT]

All mathematical content matches between KO and EN versions:
- **Definitions 1, 4, 10, 12, 13**: Limit point compact, sequentially compact, first/second countable, filter convergence, limit point of a function w.r.t. a filter -- all consistent.
- **Propositions 2, 5, 9, 11, 14, 15, 16**: Statements and proofs are mathematically equivalent in both languages.
- **Examples 3, 6, 8**: All examples (two-point space x discrete, lower limit topology on R, uncountable product R^J) are consistent.
- **Lemma 7**: Sequential convergence implies closure membership -- consistent.
- Cross-references correctly adapted from `/ko/` to `/en/` paths.
- Note: Both files reference `[Lemma 8](#lem8)` after Proposition 15's proof, but no Lemma 8 exists in this document (IDs go from lem7 to prop9). This is a shared issue in both files, not a translation discrepancy.

## Scheme_Theory: Affine_Schemes
[STATUS: ISSUES FOUND]

- All 13 numbered items match between KO and EN with identical IDs: def1, def2, lem3, lem4, lem5, lem6, def7, lem8, prop9, def10, prop11, def12, thm13.
- All LaTeX formulas are mathematically identical between KO and EN, with one exception noted below.
- All proofs faithfully translated with identical mathematical reasoning and LaTeX.
- Section structure fully matches: (1) Locally ringed space, (2) Algebraic Functions on Spec A, (3) Affine Schemes.
- Images (Affine_schemes-1.png through Affine_schemes-11.png) referenced identically in both.
- Cross-references to other posts correctly adapted with /ko/ and /en/ path prefixes.
- References section identical ([Har], [Vak]).
- No missing content detected in either direction.

### Issues found:

1. **KO-only: LaTeX rendering error (line 399)** -- `$$A=\\mathscr{O}_X(X)$$` has a double backslash before `mathscr`, which would cause MathJax to render incorrectly (interpreting `\\` as a line break rather than `\mathscr`). The EN file correctly has `$$A=\mathscr{O}_X(X)$$` with a single backslash. Fix: change `\\mathscr` to `\mathscr` in the KO file.

2. **KO-only: Broken cross-reference in Proposition 9 proof (line 335)** -- KO references `[보조정리 7](#lem7)` but there is no `lem7` anchor in the file (IDs go lem3, lem4, lem5, lem6, def7, lem8). The stalk isomorphism used in the proof is stated in Lemma 8 (lem8). The EN file correctly references `[Lemma 8](#lem8)`. Fix: change `[보조정리 7](#lem7)` to `[보조정리 8](#lem8)` in the KO file.

3. **Both files: Wrong cross-reference in Definition 10 (KO line 343, EN line 341)** -- Both reference "Proposition 8" via `#prop8`, but there is no `prop8` anchor in this file. The functor `Spec: cRing^op -> LRS` is defined in Proposition 9 (`prop9`). This error is identical in both files (pre-existing, not a translation discrepancy). Fix: change `[명제 8](#prop8)` to `[명제 9](#prop9)` in KO, and `[Proposition 8](#prop8)` to `[Proposition 9](#prop9)` in EN.

4. **KO-only: Link text mismatch in Lemma 8 proof (line 279)** -- KO displays `[§스펙트럼, ⁋보조정리 11]` ("Spectra, Lemma 11") but the URL points to `/ko/math/topology/topological_bases#lem11` (Topological Bases page). The EN file correctly displays `[[Topology] §Bases of Topological Spaces, ⁋Lemma 11]` matching the URL. Fix: change the link text in KO from `[§스펙트럼, ⁋보조정리 11]` to `[\[위상수학\] §위상공간의 기저, ⁋보조정리 11]`.

## Set_Theory: Property_of_Products
[STATUS: CONSISTENT]

**Sections compared:** 7 definitions/propositions (Def 1, 4; Prop 2, 3, 5, 6, 7), 4 proofs, 2 section headings.

**Mathematical formulas:** All LaTeX expressions match identically between KO and EN, including:
- Partial product definitions and projection function notation (pr_J, Delta_J, id_J)
- Proposition 3 (bijection via partition) and both proofs (Proof 1 via Sum of Sets, Proof 2 via universal property)
- Product of functions (Def 4, Prop 5) and composition formula
- Distributivity formulas in Prop 6 and Prop 7

**Cross-references:** KO links to `/ko/math/set_theory/sum_of_sets#prop2`, EN correctly adapts to `/en/math/set_theory/sum_of_sets#prop2`.

**Images:** Both files reference the same 7 image assets (Property_of_Products.png, -1 through -6.png).

**Notable (pre-existing in KO, not a translation issue):**
- KO excerpt reads "부분곱, 결합법칙과 결합법칙" -- the word 결합법칙 (associativity) is repeated; should be "결합법칙과 분배법칙" (associativity and distributivity). The EN excerpt correctly says "Partial products, associativity and distributivity."
- In Prop 6 and Prop 7, the second distributivity equation uses `i \in J` (without subscript k) rather than `i \in J_k`. This appears identically in both KO and EN, so it is a consistent faithful translation of the original.
- After Def 1, the formula uses lowercase `f` on the left-hand side (`f ∘ id_J`) while the prose introduces uppercase `F`. This inconsistency exists in both versions identically.

## Topology: Continuous_Functions
[STATUS: ISSUES FOUND]

- **Proposition 2 statement (both versions)**: Both KO (line 38) and EN (line 37) state the conclusion as "$$f(x)\in\cl(A)$$" but the proof demonstrates "$$f(x)\in\cl(f(A))$$". The correct conclusion should be $f(x)\in\cl(f(A))$ — i.e., if $f$ is continuous at $x$ and $x\in\cl(A)$, then $f(x)\in\cl(f(A))$. The proof is correct (it shows every neighborhood of $f(x)$ meets $f(A)$), but the statement has a missing $f$ around $A$ in the conclusion. This is a mathematical error in the KO original faithfully preserved in EN.

- **Proof of Theorem 4 (4 implies 1), both versions**: Both KO (line 86) and EN (line 85) write "$$f(x)\subseteq V'$$" where it should be "$$f(x)\in V'$$" (element, not subset). This is a shared typo from the KO original.

- **`<em-ko>` tag retained in EN**: The EN file (line 85) still contains `<em-ko>open neighborhood</em-ko>` which should have been converted to standard emphasis tags (e.g., `<em>open neighborhood</em>`) or markdown italics during translation. The KO original (line 86) has `<em-ko>열린근방</em-ko>` which is correct in context.

- **All 6 labeled items match** between KO and EN: Definition 1 (def1), Proposition 2 (prop2), Proposition 3 (prop3), Theorem 4 (thm4), Example 5 (ex5), Definition 6 (def6). All have matching IDs and corresponding mathematical content.

- **All LaTeX formulas are identical** between KO and EN for definitions, propositions, examples, and the display equations in proofs (set inclusions, composition, inverse image formulas, homeomorphism identities).

- **Proofs of Proposition 2, Proposition 3, and Theorem 4** are all present in both versions with faithful mathematical reasoning.

- **Cross-references correctly adapted**: KO `/ko/math/topology/other_concepts#prop6` mapped to EN `/en/math/topology/other_concepts#prop6`; KO links to Set Theory sections correctly adapted with `/en/` paths and English section names.

- **References section identical** in both files ([Bou] Bourbaki).

- **No missing content** in either direction; paragraph-by-paragraph correspondence is complete.

## Topology: Hausdorff_Spaces

[STATUS: CONSISTENT]

- All 9 numbered items (Definitions 1, 3; Example 2; Propositions 4, 8, 9; Lemma 5; Corollaries 6, 7) are present in both versions.
- All LaTeX formulas are identical between Korean and English.
- All proofs (Proposition 4, Lemma 5, Corollaries 6-7, Proposition 8) are translated faithfully.
- Section structure matches: Convergence of Sequences, Separation Axioms, Hausdorff Spaces, Subspaces and Products, Quotient Spaces.
- Footnote [^1] correctly translated; internal links use correct `/en/` paths.
- No missing content, no added content, no mistranslations detected.

## Topology: Open_Mappings_and_Closed_Mappings

[STATUS: CONSISTENT]

- All structural elements are present in both versions: Definition 1, Proposition 2 (with proof), Proposition 3 (with proof), Definition 4, Proposition 5, and Proposition 6 (empty placeholder in both).
- All LaTeX formulas are identical between Korean and English.
- Korean subscript annotations (열린사상, 닫힌사상) are correctly omitted in the English version.
- All internal links have been correctly translated to point to the English versions of referenced posts (e.g., `/en/math/set_theory/retraction_and_section#def2`, `/en/math/topology/continuous_functions#thm4`, `/en/math/topology/other_concepts#prop4`).
- Minor note: A typo exists in both versions in Proposition 5's canonical decomposition (`\overset{h}{\longrightarrow h}` instead of `\overset{h}{\longrightarrow}`) and a missing closing parenthesis in Proposition 2 proof part 3 (`g^{-1}(g(f(U))=f(U)` instead of `g^{-1}(g(f(U)))=f(U)`). These are present in the Korean original and faithfully preserved in the English translation, so they do not represent translation issues.
- No mistranslations, missing content, or added content detected.

## Set_Theory: Sum_of_Sets
[STATUS: CONSISTENT]
- All 8 labeled items match between KO and EN with correct IDs: Definition 1 (def1: covering/finer), Proposition 2 (prop2: two parts on gluing functions), Definition 3 (def3: disjoint/pairwise disjoint), Definition 4 (def4: partition), Proposition 5 (prop5: existence of sum set S), Definition 6 (def6: sum notation), Proposition 7 (prop7: bijection for pairwise disjoint), Theorem 8 (thm8: universal property of sum), Definition 6' (def6-1: sum via universal property), Corollary 9 (cor9: unique up to bijection).
- All LaTeX formulas are identical between KO and EN, including: union/covering conditions, restriction notation $f|_{A_i}$, intersection conditions $A_i\cap A_j$, bijection $x\mapsto(x,i)$, universal property condition $f_i=f\circ\iota_i$, composition identities $\phi'\circ\phi=\id_{S'}$ and $\phi\circ\phi'=\id_S$.
- All 5 proofs (Proposition 2, Proposition 5, Proposition 7, Theorem 8, Corollary 9) are faithfully translated with identical mathematical reasoning and all steps preserved.
- Prose paragraphs between sections match in content: preimage/image discussion, empty set remark, disjoint union alternative notation, "putting the cart before the horse" explanation of universal property, unique up to bijection discussion.
- Cross-references correctly adapted: KO [§기수의 연산, ⁋정의 1](/ko/math/set_theory/operation_of_cardinals#def1) -> EN [§Operations of Cardinals, ⁋Definition 1](/en/math/set_theory/operation_of_cardinals#def1); KO [§Retraction과 section, ⁋명제 3](/ko/math/set_theory/retraction_and_section#prop3) -> EN [§Retraction and Section, ⁋Proposition 3](/en/math/set_theory/retraction_and_section#prop3).
- Internal anchor links (def1, prop2, def3, def4, prop5, def6, prop7, thm8, def6-1, cor9) consistent in both files.
- Image references identical in both files (header image Sum_of_Sets.png, universal property diagram Sum_of_Sets-1.png).
- References section identical ([Bou] Bourbaki, Theory of Sets).
- Pre-existing issue in both versions (not a translation error): In the proof of Corollary 9, both KO and EN write $\iota_i':A_i\rightarrow Y$ where $Y$ should be $S'$ based on context. This is a typo in the Korean original faithfully preserved in the EN translation.
- EN front matter includes expected translation metadata (translated_at, translation_source: kimi-cli).
- No missing content detected in either direction.

## Topology: Proper_Maps

[STATUS: ISSUES FOUND]

Both files contain the same 9 numbered items (Definition 1, Propositions 2–4, Lemma 5, Theorem 6, Corollary 7, Proposition 8, Corollary 9) across 3 sections. All proofs are present in both. LaTeX formulas are consistent. Cross-references are correctly adapted (/ko/ → /en/). The following issues were found:

1. **Typo in Corollary 9 statement (both versions):** The text reads `$$f:X_1: X_2$$` but should read `$$f:X_1 \rightarrow X_2$$`. This typo exists identically in both the Korean original (line 189) and the English translation (line 186), suggesting it was carried over faithfully from the source.

2. **Typo in Corollary 9 one-point compactification definition (both versions):** The formula `$$\overline{X}_i=X\cup \{\ast_i\}$$` should be `$$\overline{X}_i=X_i\cup \{\ast_i\}$$`. Again, this typo is present in both versions.

3. **Translation note on "compact":** The Korean original consistently uses the transliteration "compact" (콤팩트) throughout, while the English uses "compact" — this is correct and expected.

4. **Front matter:** The English version correctly has additional fields `translated_at` and `translation_source: kimi-cli`.

5. **Translation quality:** The English translation is faithful to the Korean original. Mathematical terminology is appropriately rendered (보조정리 → Lemma, 따름정리 → Corollary, 명제 → Proposition, 정리 → Theorem, 정의 → Definition). No content is missing or added in the translation.


## Topology: Initial_and_Final_Topology

[STATUS: CONSISTENT]

All definitions, propositions, and proofs are present in both versions:
- Definition 1 (initial topology), Definition 4 (final topology)
- Proposition 2 (subbase characterization), Proposition 3 (initial topology universal property)
- Proposition 5 (final topology explicit construction), Proposition 6 (final topology universal property)
- All six proofs present and complete in both.

LaTeX formulas are identical across both versions.

Minor translation note: Korean line 74 uses "열린 진부분집합" (open proper subset) while English uses "open subset" -- mathematically insignificant, the proof holds for all open subsets. Also, Korean line 111 contains "연속이어야 한다" (must be continuous) which appears to be a typo in the original for a set (should be "열린집합이어야 한다"); the English correctly says "must be open in Y_i".

References identical: [Bou] N. Bourbaki, General Topology.

## Topology: Product_Spaces

[STATUS: CONSISTENT]

- All structural elements match: Definition 1, Proposition 2, Corollary 3, Corollary 4, Proposition 5, Proposition 6, Proposition 7, Proposition 8, plus the inline graph definition.
- Both files have two sections: "Definition and Properties of Product Spaces" and "Interior and Closure".
- Both files have empty proof blocks for Propositions 7 and 8.
- All LaTeX formulas are identical between the Korean original and English translation.
- All cross-references (def1, prop2, cor3, cor4, prop5, prop6, prop7, prop8) are preserved with matching IDs.
- Internal links correctly updated from `/ko/math/topology/...` to `/en/math/topology/...`.
- No missing content, no added content, no mistranslations detected.

## Topology: Connected_Spaces
[STATUS: ISSUES FOUND]

- Both files have 169 lines each and are truncated at the same point (beginning of "Path-Connected Spaces" section: "한편 우리는" / "Meanwhile, we"). This is consistent -- both are works in progress at the same cutoff.
- Proposition IDs and anchors match: def1, prop2, prop3, prop4, cor5, prop6, def7, prop8, def9, prop10.
- All LaTeX formulas are mathematically identical between KO and EN.
- All proofs (Propositions 2, 3, 4, 6) are faithfully translated with identical mathematical reasoning and formulas.
- Section structure fully matches: 연결집합의 성질들 / Properties of Connected Sets, 연결성분 / Connected Components, 국소연결공간 / Locally Connected Spaces.
- Cross-references to other posts correctly adapted with /ko/ and /en/ path prefixes (e.g., Subspaces Proposition 5 link).
- Shared image (Connected_Spaces.png) referenced identically in both.

### Issues found:

1. **KO: Missing "nonempty" in Definition 1 (line 24)** -- The EN version states connectedness as "cannot be written as the union of two disjoint nonempty open sets," explicitly including "nonempty." The KO version states "두 개의 서로소인 열린집합의 합집합으로 나타날 수 없는 것이다" (cannot be written as a union of two disjoint open sets), omitting "비어있지 않은" / "공집합이 아닌" (nonempty). The nonempty condition is essential: without it, X = X ∪ ∅ would trivially make every space disconnected. Fix: change "두 개의 서로소인 열린집합" to "두 개의 서로소인 비어있지 않은 열린집합" in the KO file.

2. **KO: Proposition 10 states a different mathematical condition (line 163-164)** -- The EN version correctly states the standard theorem: "That X is locally connected is equivalent to every component of every open set in X being open" (Munkres Theorem 25.3). The KO version states "X의 열린집합을 포함하는 임의의 component가 항상 open인 것이 동치이다," which parses as "any component that contains an open set of X is always open." These are different statements: EN says components *of* open sets are open; KO says components *containing* open sets are open. The EN formulation is the standard characterization of locally connected spaces. Fix: change the KO to "X의 각 열린집합의 component가 항상 open인 것이 동치이다" to match the EN meaning.

3. **Both files: Typo in Definition 7 (KO line 128, EN line 127)** -- "connected componenet" appears instead of "connected component." This is an identical typo in both files (pre-existing, not a translation discrepancy). Fix: correct to "connected component" in both files.

4. **Both files: Minor grammar issue in Proposition 8 (KO line 145, EN line 143)** -- The formula text reads "x and y lies in the same component" -- the verb should be "lie" (plural subject "x and y"). This is identical in both files. Fix: change "lies" to "lie" in both files.

5. **Both files: Notation inconsistency in Proposition 6 proof** -- Both files define f∘ι_i (composition) but then refer to it as "f_i" in the text ("f_i는 상수함수여야" / "f_i must be constant"). This is the same in both files. Minor notational inconsistency, not a translation discrepancy.


## Topology: Other_Concepts

[STATUS: CONSISTENT]

- All 11 labeled items present in both files with matching IDs: Definitions 1, 3, 5, 8, 9, 10; Propositions 2, 4, 6, 11; Corollary 7.
- All 4 sections match: Closed Sets, Interior and Closure, Boundary, Dense Sets.
- All LaTeX formulas are identical between KO and EN.
- All proofs (Propositions 2, 4, 6, 11; Corollary 7) are correctly translated.
- Internal cross-references (prop6, prop8) are correctly maintained.
- External links properly localized: /ko/math/... → /en/math/... (set_theory, open_sets).
- Korean custom tags `<em-ko>` correctly replaced with standard `<em>` in English.
- Paragraph-level content (discussions after definitions, intuitive explanations about dense sets, perturbation, etc.) faithfully translated.
- EN front matter includes translation metadata (translated_at, translation_source) as expected.

## Topology: Open_Sets

[STATUS: CONSISTENT]

- All 6 structural elements are present in both versions: Definition 1 (topology), Example 2 (trivial and discrete topology), Definition 3 (stronger/weaker topology), Definition 4 (open neighborhood/neighborhood), Proposition 5 (with proof), and Proposition 6 (with proof).
- All LaTeX formulas are identical between Korean and English, including complex expressions in the proofs (e.g., the union chain in Proposition 5 proof, all neighborhood filter proof steps).
- Internal links correctly use `/en/` paths (e.g., `/en/math/set_theory/union_and_intersection`).
- Internal anchor links (#def1, #def4, #prop5) preserved correctly.
- Korean `<em-ko>` and `<sub>` markup tags are appropriately omitted in the English version; `<phrase>` tags are preserved.
- Both footnotes [^1] and [^2] are present and correctly translated.
- Reference [Bou] (Bourbaki, General Topology) is present in both.
- All proof details in both Proposition 5 and Proposition 6 are faithfully translated with no omissions or additions.
- No mistranslations, missing content, or added content detected.

## Topology: Subspaces

[STATUS: ISSUES FOUND]

- **Mistranslation in Lemma 4 proof**: The Korean original states "U는 X에서의 x의 근방이다" (U is a neighborhood of x in X), but the English translation says "it follows that V is a neighborhood of x in X". The letter V should be U. The proof's goal is to show that an arbitrary neighborhood U of x in A is also a neighborhood in X, not V.
- All definitions (1), lemmas (2, 3, 4), propositions (5, 6, 8), and example (7) are present in both versions.
- LaTeX formulas are identical between the two versions.
- Note: both versions contain a pre-existing typo with $\iota^{-1}(U)$ instead of $\iota^{-1}(U_i)$ in the subspace topology derivation formulas, but this originates from the Korean original.


## Topology: Sheaves
[STATUS: CONSISTENT]
- All 16 labeled items present in both files with matching IDs: Definitions 1, 3, 5, 7, 10; Propositions 2, 4, 8, 15, 16; Lemmas 6, 11; Examples 9, 12, 13, 14.
- All LaTeX formulas are identical between KO and EN versions (including the tagged equation ($\ast$) for the inverse image sheaf).
- All proofs are faithfully translated: Proposition 2 (injectivity of stalk map), Proposition 4 (isomorphism via stalks), Lemma 6 (existence of sheafification), Proposition 8 (sheaves on a base), Lemma 11 (inverse image adjunction), Proposition 15 (surjectivity via stalks).
- Section structure fully matches: "The Abelian Category of Sheaves", "Sheaves Defined on a Base", "Examples of Sheaves", "Inverse Image of a Sheaf".
- Internal cross-references correctly adapted (ko to en path prefixes). Anchor IDs (def1, prop2, def3, prop4, def5, lem6, def7, prop8, ex9, def10, lem11, ex12, ex13, ex14, prop15, prop16) preserved identically.
- External links to Presheaves, Category Theory, and Subspaces pages correctly use /en/ prefixes.
- Bilingual subscript labels (e.g., "sheaf<sub>층</sub>" in Korean) correctly omitted in the English version, as expected.
- References section (Hartshorne, Vakil) identical in both versions.
- Note: Both versions share a minor notation inconsistency in the Proposition 4 proof where the quantifier uses $p\in U$ but subsequent formulas use subscript $x$ (e.g., $s_x$, $\phi_x$) instead of $p$ — this is a pre-existing issue in the original, not a translation error.
- No missing content, no added content, no mistranslations found.

## Toric_Geometry: Reflexive_Polytope_and_Fano_Variety

[STATUS: CONSISTENT]

All definitions (Def 1, Def 8), propositions (Prop 2, 3, 4, 5, 7), and example (Ex 6) are present in both Korean and English versions. All LaTeX formulas are identical. Cross-references to other sections (toric_varieties, toric_divisors, algebraic_varieties/canonical_bundle) are correctly adapted with proper English anchor IDs. Proofs are faithfully translated with all logical steps preserved. The References section is identical. No missing, added, or mistranslated content found.

## Toric_Geometry: Toric_Divisors_and_Line_Bundles
[STATUS: CONSISTENT]
- All 11 labeled items (Definitions 1, 2, 5, 8; Propositions 3, 4, 6, 7, 9, 10; Example 11) present in both files with matching IDs.
- All LaTeX formulas are identical between KO and EN.
- All proofs (Propositions 3, 4, 6, 7, 9, 10) are correctly translated with matching mathematical content.
- Internal cross-references use consistent language prefixes (/ko/ vs /en/).
- Section structure fully matches: "Torus-Invariant Weil Divisors", "Principal Divisors and the Class Group", "Cartier Divisors", "Line Bundles", "The Picard Group of a Toric Variety", "References".
- External references to earlier sections (toric_varieties, affine_toric_varieties, ring_theory, commutative_algebra, algebraic_varieties) are correctly translated and cross-linked.
- EN front matter includes additional translation metadata (translated_at, translation_source) which is expected.
- No mistranslations, missing content, or added content detected.


## Topology: Topological_Bases

[STATUS: CONSISTENT]

- All 6 labeled items present in both files with matching IDs: Definition 1 (base), Proposition 2 (three equivalent conditions for a base), Definition 3 (subbase), Definition 4 (local base), Proposition 5 (base iff elements containing x form local base), Corollary 6 (existence of unique topology from a base).
- All proofs (Proposition 2, Proposition 5, Corollary 6) are correctly and fully translated.
- All LaTeX formulas are identical between KO and EN, including the key formula N(x) = uparrow B(x) in Corollary 6 proof.
- Internal cross-references (def1, prop2, def3, def4, prop5, cor6) are correctly mapped with matching anchor IDs.
- External links correctly adapted (ko to en paths for Set Theory and Open Sets references).
- Section structure fully matches: "Bases and Subbases" and "Local Bases" sections present in both.
- The question/remark paragraph between Proposition 2 and Definition 3 (about endowing a set with a topology from a base) is faithfully translated.
- The final paragraph about topology generated by a base/subbase is correctly translated.
- References (Bourbaki, Munkres) are identical in both files.

## Toric_Geometry: Affine_Toric_Varieties

[STATUS: CONSISTENT]

Both files contain identical mathematical content. All definitions (1-5, 8), propositions (9-11, 13, 15), lemma (12), and examples (6, 7, 14) are present in both versions with matching numbering. All LaTeX formulas are identical. All proofs are fully translated. Internal cross-references and external links are properly adapted for each language. No mistranslations, missing content, or added content found.

## Toric_Geometry: Toric_Varieties

[STATUS: CONSISTENT]

- All 11 numbered items (Definition 1, Example 2, Definition 3, Proposition 4, Proposition 5, Definition 6, Proposition 7, Proposition 8, Proposition 9, Example 10, Proposition 11) are present in both versions.
- All LaTeX formulas are identical between Korean and English.
- Cross-references correctly use `/ko/` paths in Korean and `/en/` paths in English.
- All proofs are faithfully translated.
- Section structure matches exactly (5 main sections + references).
- Minor note: Korean original contains a typo "lattica" (line 197, Example 10 proof) which the English version corrects to "lattice."
- No missing content, no added content, no mistranslations detected.


## Set_Theory: Order_Relations_Between_Ordinals
[STATUS: ISSUES FOUND]

- All 4 labeled items (prop1, thm2, def3, def4) present in both KO and EN with matching IDs and correct translations (명제 1 → Proposition 1, 정리 2 → Theorem 2, 정의 3 → Definition 3, 정의 4 → Definition 4).
- **ISSUE**: In the proof of Proposition 1, KO line 36 uses `$$F$$` where EN line 38 correctly uses `$$B$$`. Specifically, KO says "$$v(S)$$는 ... $$F$$의 segment가 되며" (segment of F) while EN says "it becomes a segment of $$B$$". Mathematically, v(S) is the union of ranges of functions mapping into B, so it is a segment of B, not F. The EN translation corrected a typo in the KO original.
- All other LaTeX formulas are identical between KO and EN throughout (including Proposition 1 statement, Replacement axiom, Theorem 2 proof, Definitions 3 and 4, and cardinal number discussion with $$\omega_0$$, $$\omega_1,\omega_2,\ldots$$, $$\aleph_\alpha$$).
- All proofs (Proposition 1 and Theorem 2) are faithfully translated with identical mathematical reasoning.
- The Axiom schema of Replacement and its explanatory paragraph are correctly translated.
- Cardinal number section (Hartogs number, initial ordinals, aleph notation) fully consistent.
- References ([HJJ]) identical in both files.
- No missing content detected in either direction.
- EN includes expected translation metadata (translated_at, translation_source).

## Topology: Quotient_Spaces

[STATUS: CONSISTENT]

- All sections present in both files: Locally closed subspace, Quotient Spaces, Quotient Spaces and Subspaces.
- All definitions (1, 3), propositions (2, 4, 5, 6, 7) with proofs (Prop 2, Prop 5) present in both.
- All LaTeX formulas are identical between Korean and English.
- All internal link references correctly converted from `/ko/` to `/en/` paths.
- Footnote [^1] present and correctly translated in both.
- No missing content, no added content, no mistranslations detected.
- Minor note: Korean uses `<em-ko>` tag for emphasis while English uses standard markdown italics; this is acceptable.

## Topology: Presheaves
[STATUS: CONSISTENT]
- All 17 labeled items present in both files with matching IDs:
  - Lemma 1 (lem1) with proof
  - Definition 2 (def2) — presheaf
  - Example 3 (ex3)
  - Definition 4 (def4) — sections, restriction map
  - Example 5 (ex5) — Skyscraper sheaf
  - Example 6 (ex6) — Constant presheaf
  - Example 7 (ex7) — restriction to open set
  - Example 8 (ex8) — Pushforward
  - Definition 9 (def9) — stalk, germ
  - Definition 10 (def10) — presheaf morphism
  - Proposition 11 (prop11) — stalk morphism
  - Example 12 (ex12) — Sheaf Hom
  - Example 13 (ex13) — Product
  - Example 14 (ex14) — O_X-module
  - Definition 15 (def15) — abelian presheaf
  - Definition 16 (def16) — presheaf kernel
  - Lemma 17 (lem17) with proof
- All LaTeX formulas are identical between KO and EN (gluing condition, skyscraper sheaf, restriction, pushforward, stalk limit, equivalence relation, étalé space, Sheaf Hom, product, kernel diagram).
- All proofs (Lemma 1, Lemma 17) are correctly translated.
- Internal cross-references and external links use consistent language prefixes (/ko/ vs /en/).
- Section structure fully matches: Gluing lemma → Presheaves of continuous functions → Examples of presheaves → Stalks → Morphisms of presheaves → Abelian presheaves.
- References section and footnote [^1] (derivative intuition) both present and correctly translated.
- Korean original has a typo in Definition 4: "$\rho_{UV}(f)$" should likely be "$\rho_{VU}(s)$" given surrounding context; EN faithfully preserves this same text — not a translation issue.
- Korean original references "[예시 2](#ex2)" which does not exist on this page (examples start at 3); EN faithfully preserves the same broken reference — not a translation issue.
- Korean "현채로서" (line 152) appears to be a typo for "현재로서" (currently); EN translates as "For now" which captures the intended meaning.
- Korean section title "가환준층" (literally "commutative presheaf") correctly translated as "Abelian presheaves" — "가환군" is the standard Korean term for abelian group.
- No missing content, no added content, no mistranslations.
