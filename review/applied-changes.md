# Applied changes and verification

Canonical document: companion/paper/coin-line-rates.tex and .pdf.

The trajectory, lower-bound, and upper-bound notes were combined into one
manuscript. All supporting path facts now precede their uses. The first-passage
argument, path enumeration, per-start event differentiation, and simultaneous
first-exit proof are explicit. The compact entrance estimate has an enlarged
compact set, a quantitative comparison bound, and bounded clock conversion.
The compact limiting vector field is a corollary of the uniform path-sum lemma,
as suggested in the final upper-bound review.

Both model reviewers accepted the mathematical components after the recorded
repairs. The upper review is conditional on the ray/tracking/path facts; those
are included and separately reviewed in the unified paper. There is no external
unproved mathematical assumption in the final theorem beyond the model's stated
L>=4, fixed L, zero initialization, and exact Euclidean flow conventions.

Review scope: independent model review of source text. No human peer review,
formal verification, or upstream acceptance is implied. Numerical evidence is
kept separate from proof. The original O87 publication is unchanged.

Checks: 13 unit tests; reruns of ray, tracking, precision, and transition
receipts match the retained values exactly; 27 uniform-approximation diagnostics
cover both signs of b and b=0. Build and final artifact hashes are recorded in
the companion manifest and local completion receipt.
