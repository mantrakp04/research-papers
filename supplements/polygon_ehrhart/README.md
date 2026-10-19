# Polygon-face-lattice Ehrhart: computational supplement

## Files and commands

- `verify_certificate.py`: primary exact recurrence and coefficient verifier, including the half-table and optional n=13 real-root sign certificate
- `independent_audit.py`: direct integer matrix powers and rational Lagrange interpolation, independently of the determinant recurrence and Newton interpolation
- `independent_results.json`: generated full coefficient data for n=3 through 13, crown counts, full-face-lattice values, and seven brute-force coordinate checks

Both programs use only the Python standard library. From this supplement directory run:

    python3 verify_certificate.py
    python3 independent_audit.py

The second command overwrites `independent_results.json`. For n=13, its `values` field starts with the 29 interpolation values E_13(0),...,E_13(28), followed by three additional check values. Its `coefficients` field lists the complete rational Ehrhart polynomial in ascending degree order. The `crown_values` field concerns the crown poset; it must not be confused with the full face lattice's `values` field.

The primary verifier confirms dimension 28, linear coefficient -298495711/35302608, positivity of all other n=13 coefficients, positivity for n=3 through 12, and 24 distinct negative roots of the n=13 h-star polynomial. The independent implementation additionally checks the seven small coordinate enumerations, three interpolation-independent values at each n, the stated negative-integer zeros and reflection symmetry, and the n=7 order-polynomial linear coefficient.

## Build and execution

This directory contains the computational supplement. The corresponding manuscript source is at `../../latex/polygon_ehrhart/main.tex`, relative to this README. Preserve the displayed relative directory layout. The Python commands above are run from this supplement directory. For a PDF build, change to `../../latex/polygon_ehrhart/`, use a normal TeX Live or MiKTeX installation with the packages in the manuscript preamble, and run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice there. Bibliographies are embedded in the source; BibTeX is not needed. A LaTeX build does not run the Python verification commands.

Use Python 3.8 or later. Keep assertions enabled: do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`. The commands below access no network. Their inputs and generated outputs are resolved relative to each script, so the scripts can also be invoked by full path from another working directory. Any command that writes a result requires a writable package directory. Rerunning such commands overwrites only their stated generated outputs.

`MANIFEST.json` records SHA-256 hashes of the supplied supplement files, excluding the manifest itself. Generated output hashes may change after a rerun because some outputs record runtime. Hashes identify the delivered bytes; they do not prove the mathematics.

## Review boundary

These checks provide computational reproduction, not independent human mathematical review, external peer review, proof-assistant formalization, or novelty confirmation. The mathematical reductions and symbolic arguments in the manuscript require their own review.
