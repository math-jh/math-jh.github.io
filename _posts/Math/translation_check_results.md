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

