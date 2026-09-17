# Relation-family extremal atlas

A collection of exact finite extremal calculations for linear relations, Ramsey construction families, covering problems, and related finite set systems.

The most important semantic correction in this archive concerns the notation `C_k`.

## Two different `C_k` conventions

For the alternating-binomial relation

\[
\sum_i(-1)^i\binom ki x_i=0,
\]

two source branches used different meanings:

1. **any-ordering:** the distinct values may be assigned arbitrarily to the coordinates;
2. **increasing-only:** the values are inserted in sorted order.

These define different extremal sequences. They first diverge for `C_3` at `N=6`, where the maxima are 4 and 5 respectively.

All numerical results should therefore be read with the ordering convention stated explicitly. The focused any-ordering Pascal-relation work is published in [`pascal-relation-extremal-atlas`](https://github.com/jaredwilder/pascal-relation-extremal-atlas).

## Rado-equation avoidance

For distinct `x,y,z`, let `f(a,b,c;n)` be the largest subset of `[n]` containing no solution to

\[
ax+by=cz.
\]

The recovered solver atlas contains 11 complete optimal sequences and 839 exact values.

Two concrete lines are:

- for `x+2y=3z`, the sequence is computed through `n=63`;
- for `x+3y=4z`, the optimum is

  \[
  f(1,3,4;n)=20\quad(46\le n\le64),
  \]

  and rises to 21 at `n=65`.

The focused release is [`rado-equation-avoidance-atlas`](https://github.com/jaredwilder/rado-equation-avoidance-atlas).

## Exact extremizer censuses

Several finite classifications in the source are complete:

- in `Z/31Z`, the largest set simultaneously avoiding Schur triples and nontrivial 3-term progressions has size 6, with **330 extremal sets in 12 unit-dilation orbits**;
- on `[50]`, the maximum product-free and nontrivial-geometric-progression-free set has size **35**, with **240 extremal sets** and a 19-element common core;
- one `N=20` relation instance has a unique 12-element optimum

  ```text
  {0,1,2,4,5,6,13,14,15,17,18,19}.
  ```

## Ramsey and covering calculations

The archive also contains or cross-checks:

- the classical 41-vertex circulant `(5,5)` Ramsey witness;
- complete circulant-family exhaustions for the `R(3,10)` condition at order 40 and `R(4,6)` at order 36;
- exact small covering numbers such as

  \[
  C(7,4,2)=5,
  \qquad
  C(7,4,3)=12.
  \]

The circulant eliminations are construction-family results, not unrestricted Ramsey bounds.

## Intersecting-family calibration

For 2-intersecting 4-subsets of `[8]`, the star has size 15 while the Ahlswede–Khachatrian family has size 17. Exhaustive search confirms 17 is optimal.

Similarly, for 3-intersecting 6-subsets of `[14]`, the corresponding comparison is 165 versus 189.

These serve as useful controls against overgeneralizing star-optimality heuristics.

## Formalization audit

The same source collection includes more than 200 Lean receipts. A clean kernel receipt proves the Lean proposition it contains, but some audited files formalize only arithmetic skeletons rather than the intended graph or extremal statement.

For that reason, formal proof status and source-semantic fidelity are tracked separately. The dedicated semantic-audit tooling is in [`lean-semantic-blades`](https://github.com/jaredwilder/lean-semantic-blades).

## Purpose of this repository

This atlas is a cross-subject recovery/index layer. Results that have grown into coherent subjects now live in dedicated repositories; this page preserves the shared finite data and the semantic correction that links them.

Author: Jared Wilder. License: Apache-2.0.
