# Graph-state MMI: computational supplement

## Files and commands

- `path_certificate.json`: 44 states, 176 transitions, and the potential certificate
- `path_automaton.py`: optional generator; rerunning overwrites `path_certificate.json`
- `independent_audit.py`: independently reconstructs the path state graph and verifies the frozen certificate, binary cut ranks, all four-colorings for paths of orders 1 through 10, and seeded larger cases; writes `independent_audit_results.json`
- `independent_cycle_audit.py`: verifies cycle cut ranks, alternating-cut correction, all four-colorings for cycles of orders 3 through 10, and seeded larger cases; writes `independent_cycle_results.json`
- `claw_classification/extension_certificate.json`: all 120 nonempty one-vertex attachments
- `claw_classification/verify.py`: replays all 120 attachment witnesses, enumerates the six labeled LC orbits, verifies entropy invariance on those orbits, and checks 5,460 representative four-colorings; writes `claw_classification/audit_result.json`
- `claw_classification/orbit_certificate.json`: 281 labeled graphs with reachability words
- `claw_classification/check_orbit_certificate.py`: checks the supplied orbit certificates for reachability, generator closure, and claw absence without searching

All checkers use only the Python standard library. From this supplement directory run:

    python3 independent_audit.py
    python3 independent_cycle_audit.py
    python3 claw_classification/verify.py
    python3 claw_classification/check_orbit_certificate.py

The optional generator is `python3 path_automaton.py`; recheck the certificate with `independent_audit.py` if it is regenerated. The three supplied result JSON files record the completed verification. The finite tests support the computations; the unbounded-size conclusions depend on the manuscript's proofs.

The extension certificate's `n` is the extended graph order (one greater than the base index). Local-complementation words act left to right. A claw tuple is its center followed by the leaves. A next-representative permutation maps each old representative label to its image.

## Build and execution

This directory contains the computational supplement. The corresponding manuscript source is at `../../latex/graph_state_mmi/main.tex`, relative to this README. Preserve the displayed relative directory layout. The Python commands above are run from this supplement directory. For a PDF build, change to `../../latex/graph_state_mmi/`, use a normal TeX Live or MiKTeX installation with the packages in the manuscript preamble, and run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice there. Bibliographies are embedded in the source; BibTeX is not needed. A LaTeX build does not run the Python verification commands.

Use Python 3.8 or later. Keep assertions enabled: do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`. The commands below access no network. Their inputs and generated outputs are resolved relative to each script, so the scripts can also be invoked by full path from another working directory. Any command that writes a result requires a writable package directory. Rerunning such commands overwrites only their stated generated outputs.

`MANIFEST.json` records SHA-256 hashes of the supplied supplement files, excluding the manifest itself. Generated output hashes may change after a rerun because some outputs record runtime. Hashes identify the delivered bytes; they do not prove the mathematics.

## Review boundary

These checks provide computational reproduction, not independent human mathematical review, external peer review, proof-assistant formalization, or novelty confirmation. The mathematical reductions and symbolic arguments in the manuscript require their own review.
