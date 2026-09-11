#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recomputes the headline defect: one symbol naming two different sequences.

    python verify.py

Standard library only. Exit 0 means everything reproduced.
"""
from __future__ import annotations

import sys
from itertools import combinations, permutations

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-56s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def pascal(k):
    row = [1]
    for i in range(k):
        row.append(row[-1] * (k - i) // (i + 1))
    return [((-1) ** i) * row[i] for i in range(k + 1)]


def has_violation_any(S, coeffs):
    """Any injective assignment of distinct values to the coordinates."""
    n = len(coeffs)
    for q in combinations(sorted(S), n):
        for p in permutations(q):
            if sum(c * v for c, v in zip(coeffs, p)) == 0:
                return True
    return False


def has_violation_increasing(S, coeffs):
    """The values in sorted order only."""
    n = len(coeffs)
    for q in combinations(sorted(S), n):
        if sum(c * v for c, v in zip(coeffs, q)) == 0:
            return True
    return False


def maximum(N, coeffs, rule):
    for k in range(N, 0, -1):
        for S in combinations(range(1, N + 1), k):
            if not rule(S, coeffs):
                return k
    return 0


def test_collision():
    print("One symbol, two sequences: C_3 under two readings")
    c3 = pascal(3)
    check("the coefficient vector", c3, [1, -3, 3, -1])
    any_row, inc_row = [], []
    for N in range(3, 12):
        any_row.append(maximum(N, c3, has_violation_any))
        inc_row.append(maximum(N, c3, has_violation_increasing))
    print()
    print("   N      any-ordering   increasing-only")
    for i, N in enumerate(range(3, 12)):
        flag = "  <- diverge" if any_row[i] != inc_row[i] and \
            (i == 0 or any_row[i - 1] == inc_row[i - 1]) else ""
        print("   %-2d         %-12d %d%s" % (N, any_row[i], inc_row[i], flag))
    print()
    check("they agree for N = 3, 4, 5", any_row[:3], inc_row[:3])
    check("they differ from N = 6 onward", any_row[3] == inc_row[3], False)
    check("  C_3(6) under any-ordering", any_row[3], 4)
    check("  C_3(6) under increasing-only", inc_row[3], 5)
    print()
    print("     => both sequences are internally correct.")
    print("        They are different objects sharing a name.")


def test_c6_divergence():
    print("The same collision in C_6, which diverges later")
    c6 = pascal(6)
    check("the coefficient vector", c6, [1, -6, 15, -20, 15, -6, 1])
    a = maximum(11, c6, has_violation_any)
    i = maximum(11, c6, has_violation_increasing)
    check("C_6(11) under any-ordering", a, 8)
    check("C_6(11) under increasing-only", i, 9)
    check("  they differ", a == i, False)


def test_vacuous_gate():
    print("A passing kernel gate on a vacuous file")
    print("     the two theorems in it, evaluated:")

    def regular_choose2_sum(n, d):
        assert d >= 2                       # the hypothesis, never used
        return n * (d * (d - 1) // 2) == n * (d * (d - 1) // 2)

    for n, d in ((5, 3), (17, 9), (100, 2)):
        check("  X = X holds at (n,d) = (%d,%d)" % (n, d),
              regular_choose2_sum(n, d), True)
    check("  6 * 6 > 6 * 5", 6 * 6 > 6 * 5, True)
    check("    i.e. 36 > 30", 36 > 30, True)
    print("     both true, both contentless, and the gate passes the file")


def main():
    for fn in (test_collision, test_c6_divergence, test_vacuous_gate):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
