# Crown order-polytope numerator: computational supplement

## Core files and command

- `finite_sign_certificates.json`: rational endpoint certificates for n=3 through 39
- `verify_full_certificate.py`: standard-library integer/rational verifier; also included as a source listing in `main.tex`

Keep these two files together in this supplement directory and run:

    python3 verify_full_certificate.py

Its final line is:

    All finite root certificates and analytic rational bounds pass

The verifier reconstructs the finite polynomials, checks 740 distinct negative gamma-root intervals, checks H_2=(1+t)^2, and checks the finite rational comparisons used in the analytic bounds. It does not mechanically verify the symbolic all-n analytic proof.

The certificate SHA-256 is:

    9bb119f040fa1a8e883c9e6a648257f93446f3e6e5e1af5c940c1371d481e4d6

The primary checker's introductory documentation now identifies the manuscript in the `latex/crown_real_rootedness/` directory; its executable statements are unchanged. The manuscript includes a source listing, so `latex/crown_real_rootedness/verify_full_certificate.py` must also be present beside `main.tex` for a PDF build. That copy should match this supplement's primary checker.

## Optional independent finite check

- `independent_sturm_check.py`: separately implemented reconstruction using shifted-cosine coefficients and exact rational Sturm sequences through n=40
- `independent_sturm_results.json`: the recorded results

This optional command requires SymPy (verification here used SymPy 1.14.0):

    python3 independent_sturm_check.py

It overwrites `independent_sturm_results.json` beside its script. It may take several minutes. Its optional `optional_reference_hstar.json` comparison input is deliberately omitted; the script does not require it. This finite check does not prove the all-n analytic bounds.

## Build and execution

This directory contains the computational supplement. The corresponding manuscript source is at `../../latex/crown_real_rootedness/main.tex`, relative to this README. Preserve the displayed relative directory layout. The Python commands above are run from this supplement directory. For a PDF build, change to `../../latex/crown_real_rootedness/`, use a normal TeX Live or MiKTeX installation with the packages in the manuscript preamble, and run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice there. Bibliographies are embedded in the source; BibTeX is not needed. A LaTeX build does not run the Python verification commands.

Use Python 3.8 or later. Keep assertions enabled: do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`. The commands below access no network. Their inputs and generated outputs are resolved relative to each script, so the scripts can also be invoked by full path from another working directory. Any command that writes a result requires a writable package directory. Rerunning such commands overwrites only their stated generated outputs.

`MANIFEST.json` records SHA-256 hashes of the supplied supplement files, excluding the manifest itself. Generated output hashes may change after a rerun because some outputs record runtime. Hashes identify the delivered bytes; they do not prove the mathematics.

## Review boundary

These checks provide computational reproduction, not independent human mathematical review, external peer review, proof-assistant formalization, or novelty confirmation. The mathematical reductions and symbolic arguments in the manuscript require their own review.
