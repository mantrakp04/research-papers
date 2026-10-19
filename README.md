# Research papers

Prepared for Mantra Patel · 10 October 2026

The four editable manuscripts are at the top level:

- [Graph-state monogamy of mutual information](graph_state_mmi.md)
- [Polygon face-lattice Ehrhart counterexample](polygon_ehrhart.md)
- [Crown numerator real-rootedness](crown_real_rootedness.md)
- [Four-matrix rank-one certificate](rank_one_four_matrix_note.md)

## Files

- `pdf/`: compiled, visually checked copies of the revised manuscripts
- `latex/`: revised LaTeX sources, including the crown listing and certificate needed for its build
- `supplements/`: exact certificates, verification scripts, result records, and per-paper instructions
- `backups/`: untouched source ZIPs exported from the four Overleaf projects before editing
- `conversion_validation.json`: content-preservation checks for the Markdown conversion
- `MANIFEST.json` and `SHA256SUMS.txt`: integrity records for this delivery

The Markdown uses `$...$` and `$$...$$` for LaTeX mathematics, standard Markdown tables, and explicit HTML anchors for theorem, equation, and citation links. Use a Markdown viewer with math support. Some viewers strip HTML anchors; the text and mathematical content remain editable. Equation captions retain the compiled LaTeX numbering; a multiline display may share several equation numbers.

All theorem and proof environments, mathematical expressions, references, citation occurrences, and the crown Python listing were checked during conversion. Mathematical expressions were also round-trip parsed from the final Markdown. The revised PDFs compile without unresolved references or overflow warnings and were visually inspected. These checks do not certify novelty or replace mathematical review.

## Reproduce the calculations

Follow the README in each `supplements/` directory. Standard-library Python checkers are included for every paper. The optional independent crown Sturm check additionally requires SymPy. Keep assertions enabled. Scripts may overwrite their own generated result JSON files when rerun.

To rebuild a typeset manuscript, change into its `latex/<paper>/` directory and run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice. Use a normal LaTeX installation with the packages named in the preamble. Bibliographies are embedded; BibTeX is not needed. Supplements are stored separately in this delivery; use their own directories for the Python verification commands.

## Editorial changes and status

Mantra Patel is the displayed author in all four revised manuscripts. No affiliation, ORCID, funding statement, competing-interest declaration, or human-verification statement was invented. Repeated internal-draft banners were removed, references were updated, and scientific scope and limitations were retained. The quantum related-work section now explicitly credits the earlier results from which its order-seven bound also follows.

The crown and polygon manuscripts have no AI attribution in their main text. The quantum and matrix manuscripts note that generative AI tools were used to help draft the text. These are cleaned, reproducible manuscripts; submission readiness still requires author review and venue-specific facts.

The original Overleaf projects were retained. The polygon project received the revised byline/editorial source and a successful recompile before the requested destination changed to Markdown. The other three projects were not changed. The untouched source exports in `backups/` preserve the original version of all four.
