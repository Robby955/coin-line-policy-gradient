# Revision record

Edited `paper/coin-line-rates.tex` and rebuilt its PDF. Expanded the four
proof steps identified in the full review, clarified the critical timescale,
separated exact and approximate quantities, and made constant choices and
first-exit logic explicit. The theorem remains unchanged.

Edited `summarize_correction_time.py`, regenerated both figure formats and
the derived summary JSON. Labels now match the theorem status. Compared the
old and new JSON after renaming the two exponent keys: every numerical value
is identical. None of the thirty raw run receipts was modified.

Checks: thirteen existing unit tests pass; all thirty reported crossings
and six solver comparisons match the numerical claims; final LaTeX log is
free of warnings and box errors. The full compiled document is rendered
for visual inspection. Exact reviewed versions are identified by the packet's
input-hash files; the final repository manifest covers all retained companion artifacts.

The reviewer first audited the complete manuscript from scratch, without
receiving earlier verdicts as premises. A follow-up checks the complete
revised source, including the renaming and mathematical expansions.

Final result: both full audit and revision confirmation returned valid,
with no blocking issue. The final PDF has thirteen pages; all thirteen
rendered pages were inspected and the figure is legible. The final source
and PDF match `revision-input-hashes.json` byte for byte.
