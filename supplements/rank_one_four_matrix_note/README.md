# Four rank-one matrix products: computational supplement

## Files and commands

Keep the three core files in this directory:

- `verify_rankone_n4.py`: original exact integer verifier
- `check_certificate.py`: separately implemented exhaustive checker with rational power-to-Bernstein conversion
- `rankone_n4_exact_scales.json`: the common 240-row exact scale certificate

The supplied `exact_audit_result.json` records the second checker's results. Both programs use only the Python standard library. From this supplement directory run:

    python3 verify_rankone_n4.py
    python3 check_certificate.py

The second command overwrites `exact_audit_result.json` beside its script. It explicitly rejects optimized Python execution. Both checkers cover all 4,096 Bernstein indices via 276 permutation orbits: 36 coefficientwise-nonnegative orbits and 240 weighted AM-GM orbits. The exact audit records 130 nonzero monomials, 370 coefficientwise-nonnegative indices and 3,726 AM-GM indices. The only zero-gap representative is (3,3,3,3,3,3).

The certificate SHA-256 is:

    14ddfdbca54628f35920459e51077309300932e8978b3371063073e069a32067

The original checker's introductory documentation now identifies the manuscript in the `latex/rank_one_four_matrix_note/` directory; its executable statements are unchanged. The result concerns four rank-at-most-one positive-semidefinite factors, not the unrestricted positive-semidefinite conjecture.

## Build and execution

This directory contains the computational supplement. The corresponding manuscript source is at `../../latex/rank_one_four_matrix_note/main.tex`, relative to this README. Preserve the displayed relative directory layout. The Python commands above are run from this supplement directory. For a PDF build, change to `../../latex/rank_one_four_matrix_note/`, use a normal TeX Live or MiKTeX installation with the packages in the manuscript preamble, and run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice there. Bibliographies are embedded in the source; BibTeX is not needed. A LaTeX build does not run the Python verification commands.

Use Python 3.8 or later. Keep assertions enabled: do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`. The commands below access no network. Their inputs and generated outputs are resolved relative to each script, so the scripts can also be invoked by full path from another working directory. Any command that writes a result requires a writable package directory. Rerunning such commands overwrites only their stated generated outputs.

`MANIFEST.json` records SHA-256 hashes of the supplied supplement files, excluding the manifest itself. Generated output hashes may change after a rerun because some outputs record runtime. Hashes identify the delivered bytes; they do not prove the mathematics.

## Review boundary

These checks provide computational reproduction, not independent human mathematical review, external peer review, proof-assistant formalization, or novelty confirmation. The mathematical reductions and symbolic arguments in the manuscript require their own review.
