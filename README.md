# One symbol, two sequences

Author: Jared Wilder. First public timestamp: 2026-09-11.

Two independent sweeps of this estate's discovery engines and evidence tree found the same defect
without knowing about each other. That agreement is the most useful thing in either report.

**Attribution.** Results marked **[checked here]** were recomputed in this session. Results marked
**[checked by the sweep]** were verified by the sweeping process against its own independent
re-implementation, from the defining relation rather than from a stored witness, with CP-SAT
`status == OPTIMAL` required where a solver was used. Nothing is reported on a stored claim alone.

---

## The defect: `C_k` names two different sequences

The symbol `C_k` is used in this estate for the maximum subset of `[1..N]` containing no `k+1`
distinct elements admitting an ordering with `sum (-1)^i C(k,i) x_i = 0`.

**"Admitting an ordering" is doing all the work**, and two parts of the estate read it differently:

- **any-ordering** — any injective assignment of the distinct values to the coordinates
- **increasing-only** — the values in sorted order

**They are different sequences. [checked here]** They agree up to `N = 5` and diverge from `N = 6`,
where `C_3` is 4 under the first reading and 5 under the second. `C_6` diverges at `N = 11`, 8 versus
9.

Both families are internally correct and both are fully computed somewhere in the tree. **The OEIS
cross-reference and the novelty verdicts were run against one of them.** Two rows report `C_4(20) = 12`
while every other row in the family is consistent with `C_4(20) = 8` — and one of those two rows
explicitly cites "the ordered distinct-tuple semantics used by the verified solver", which is the
convention that gives 8.

Both numbers are individually right. The label on one of them is not.

The estate already holds the attack that catches this. A registry row demands *"a single versioned
semantics file plus invariance tests showing every published value uses exactly that convention."*
It is still marked untested.

---

## Exact values that survive the collision

All of these were re-derived from the defining relation, not read from a witness.

**A Rado-equation avoidance atlas. [checked by the sweep]** `f(a,b,c;n)` is the largest subset of
`[n]` with no solution to `ax + by = cz` in distinct `x, y, z`. Eleven complete solver-optimal
sequences, 839 values, **ten of them absent from OEIS**. Six of seven sampled tables were re-derived
exactly by independent brute force on `n = 3..20`. The seventh is Schur's, under the convention
permitting `x = y`, giving `ceil(n/2)`.

For `x + 2y = 3z`, `n = 3..63`:

```
3,3,3,4,4,4,5,6,7,7,7,7,7,8,9,9,9,9,9,10,...,19
```

**A plateau with its mechanism, and an honest scorecard. [checked by the sweep]** For `x + 3y = 4z`,
`f = 20` across `n = 46..64` — nineteen consecutive values — because the optimal periodic
construction `{0,1,3,5,6} mod 13` has a reach-4 conflict: blocks 1 and 5 annihilate through block 4,
saturating at `4 x 5 = 20` at any `n`. It breaks at `n = 65` with `f = 21`.

The generalizing conjecture (plateau length `4k`, break at `n = 5P`) was registered in advance and
**scored 2 of 3, with the miss recorded**: `x + 4y = 5z` plateaus at 20, not at `4 x 3 = 12`.

**Two pre-registered predictions killed by measurement. [checked by the sweep]** A predicted `C_6`
plateau value of 6, extrapolated from `C_3 -> 9`, `C_4 -> 8`, `C_5 -> 7`, was **refuted deductively**:
`C_6(9) = 8` plus monotonicity makes it impossible. The plateau values across `k` are
**9, 8, 7, 8 — not monotone.** Separately, a prediction that Sidon-ness and `C_3`-freeness do not
bind was refuted: the maximum Sidon subset of `[39]` has 8 elements, while the maximum Sidon and
`C_3`-free subset has 7.

**Counterexamples to "Sidon and 3-AP-free implies `C_3`-free". [checked by the sweep]** Four, each
verified: `{3,7,10,12}`, `{2,3,6,15}`, `{2,4,9,15}`, `{4,8,13,19}`. The first satisfies
`3 - 21 + 30 - 12 = 0` in the listed order while being Sidon and containing no three-term
progression.

**Complete extremizer censuses. [checked by the sweep]** In `Z/31Z` the maximum Schur-and-Roth-free
set has 6 elements, with **exactly 330 extremal sets in exactly 12 unit-dilation orbits** — ten of
size 30 and two of size 15 with a nontrivial stabilizer. Over `{1..50}`, the product-free and
geometric-progression-free problem has 149 hyperedges, maximum 35, **exactly 240 extremal sets**, a
19-element common core, and minimum transversal 15.

**A unique optimum. [checked by the sweep]** At `N = 20`, exhaustive enumeration of all optimal
solutions returns **exactly one** 12-element set, `{0,1,2,4,5,6,13,14,15,17,18,19}`, byte-identical
to the stored witness.

---

## Ramsey, covering, and extremal set theory

**`R(5,5) >= 42` by an explicit ladder. [checked by the sweep, and separately here]** Circulant
witnesses for every `n = 25..38, 40, 41`. The `n = 41` connection set is `{1,2,3,5,7,10,13,15,16,17}`
symmetrized, degree 20, 410 edges. Graphs rebuilt from the shift sets and exhaustively confirmed to
have no `K_5` and no independent 5-set at `n = 25, 30, 35, 38, 40, 41`.

Exhausted with **no** circulant witness at `n = 39, 42, 43, 44, 45`, recorded correctly as **not a
bound in either direction**.

**Two complete circulant exhaustions. [checked by the sweep]** **1,048,575 connection sets on 40
vertices with zero witnesses** for `R(3,10)`, and **262,143 sets on 36 vertices with zero witnesses**
for `R(4,6)`. Calibrated first: the checker finds two witnesses on `C_5` for `R(3,3)` and none on six
vertices. Scope stated honestly as one construction family at one order.

**Covering numbers above the Schönheim bound. [checked by the sweep]** `C(7,4,2) = 5` against a
Schönheim bound of 4, and `C(7,4,3) = 12` against 11, both by exhaustive branch and bound, with 69
further exact covering numbers carrying verified witnesses.

The honest part is the cross-reference: both machine lower bounds were checked against the published
repository and marked *weaker than published*. **The new-lower-bounds list is empty.**

**The star is not optimal for intersecting families. [checked by the sweep]** For `n=8, k=4, t=2` the
star has `C(6,2) = 15` members while the first Ahlswede-Khachatrian family — sets meeting `[1,4]` in
at least 3 points — has **17**. The exhaustive maximum 2-intersecting family of 4-sets on `[8]` is
**17**, so the star loses by exactly 2. At `n=14, k=6, t=3`: 165 versus **189**.

---

## Two analytic results worth the space

**An inf and a sup, computed. [checked by the sweep]** For monic `f` with all real roots in
`[-1,1]`, the measure of `{x : |f(x)| < 1}`:

```
sup side   all roots at +-1 in balance     2 sqrt 2 = 2.8284271247461901
           all roots equal                 exactly 2

inf side   two-atom family (x+1)^p (x-1)^q, t = q/p
           minimum  1.8715649889576256  at  t* = 5.8516017955725362

           richer discrete root measures go strictly lower:
           k=5 -> 1.8577561154   k=6 -> 1.8542680190   k=7 -> 1.8520646635
           best on file: 1.8306385693
```

**A twelve-sigma anomaly that is the asymptotic's error. [checked by the sweep]** For
`|{k! mod p}| ~ (1 - 1/e) p`, the measured image ratio at `p = 100003` is 0.632411 against
`1 - 1/e = 0.632121`.

The headline in the file was a departure at 12 standard deviations in the maximum preimage
multiplicity, with observed mean **6.12** over 24 primes. The sweep reports that against the *exact*
expectation for the maximum of `p` independent Poisson(1) variables this is `z = -0.06`, while
against the asymptotic `log p / log log p` it is `z = +12.04`.

**I could not reproduce the two reference values.** Computing the exact expectation directly at
`p = 100003` from the Poisson(1) distribution function gives **7.76**, and `log p / log log p` there
is **4.71**, against the sweep's 6.13 and 3.89. Those numbers presumably come from a different `p`
or from an average across the 24 primes, and the sweep does not say which — so **treat the two
reference values as unconfirmed.**

The structural point survives the discrepancy and is what matters: at `p = 100003` the asymptotic
gives 4.71 while the exact expectation is near 7.8, so an observed maximum in the 6-to-8 range sits
comfortably against the exact value and looks wildly anomalous against the asymptotic.
**The anomaly was in the approximation, not the arithmetic.** Two more in the same file point the
same way: a reflection identity has zero violations exhaustively at `p = 163, 311, 967`, and an
apparent excess of solutions with mean 2.375 raw drops to **exactly 1.000** after collapsing under
two symmetries.

---

## A verification layer that is real, and a gate that is not sufficient

**225 receipts, and they hold up. [checked by the sweep]** 217 carry a verified kernel gate, exit
code 0, every declaration clean, **no Mathlib dependency at all** — fully standalone — and axiom
footprints only among `{}`, `{propext, Quot.sound}`, and `{Classical.choice, propext, Quot.sound}`.
**No `sorryAx`, no custom axioms, and no compiler-trusted decision anywhere in the 218 theorem
files.** The single grep hit for "sorry" is a theorem *named* `zero_sorry : 0 = 0`.

Eight of the 225 have no kernel gate at all, only a factory pass record.

**But a passing kernel gate does not mean non-vacuous.** One file carries a verified gate, exit 0 and
clean axioms, and contains:

```lean
theorem regular_choose2_sum (n d : Nat) (hd : d ≥ 2) :
    n * (d * (d - 1) / 2) = n * (d * (d - 1) / 2) := rfl

theorem cubic_c4free_n6_fails : 6 * 6 > 6 * 5 := by omega
```

`X = X` with an unused hypothesis, and `36 > 30`. **The estate's own semantic check flags this file
as not verified; the kernel gate passes it.** Any count of verified declarations drawn from the
kernel gate alone is inflated.

The content is honest about itself elsewhere: 116 of the 225 are arithmetic skeletons with graph
semantics explicitly not formalized, and the manifest says so.

---

## What these engines actually produced

The narrow, honest answer from the sweep that asked it: **a block of exact extremal values and
complete extremizer censuses for one relation family** — minimum spans, plateau structure, unique
onset witnesses, the `Z/31` and `{1..50}` censuses. Every one re-derived from scratch and correct.
Nothing in OEIS matches, and the estate's own novelty index records no collisions against a pinned
corpus.

But the frame the estate's own prior-art sonar wrote is the right one: these are **new exact values
in a natural specialization of a well-studied framework**, not new theory. `C_k`-freeness is
Sidon-ness for the alternating-binomial form, a special case of `k`-fold Sidon sets and of
Rado-equation theory, and `C_2` **is** Roth's function. Nobody published these numbers because nobody
tabulated this particular one-parameter family, not because it was out of reach.

The general theorems in the same block are one-line consequences of a standard bound and of scaling
equivalence. **One construction — base-7 integers with digits in `{0,1,2}`, density exponent
`log_7 3 = 0.5646 > 1/2` — is structurally the classical Ruzsa digit construction**, and should be
treated as prior art until someone checks the 1993 paper directly. The registry does not cite it.

## And the negatives, which are the most valuable output

They all say the same thing, and they say it correctly:

- One campaign certifies that **every search class it can express is provably at least 1/3**, while
  the published wall is `5/16 = 0.3125`. The machine's own barriers certify it cannot reach the state
  of the art.
- Another is a real reduction chain to two boundedness statements, with **four claims retracted along
  the way** and its exceptions list matching the published one.
- A third records *"computation NEVER FINISHED, evidence dir empty."*
- A fourth made a plateau-value prediction in advance and **its own measurement refuted it.**

And the scale claims do not survive contact: 1,900 rows in one lane, 200 in another, 40 in a third,
**all marked untested**. The engine's own README ends with the accurate sentence: *"tools are
self-tested on tiny inputs, not yet run at campaign scale."*

## One row that could not be reproduced

A claim that "clean maximal Sidon sets exist at `N` in `{4,7,12,18}`, and no `N` has all maximal
Sidon sets clean" could not be reproduced under either reading of "clean" that the sweep tried. Under
both, *every* maximum Sidon set in `[1..N]` is clean for every `N` from 3 to 18, making the second
half false as read. **The row does not define its own term.** Not necessarily wrong — unreproducible
from its own text. The set `{4,7,12,18}` is exactly where the maximum Sidon size first increases.

## License

Apache-2.0.
