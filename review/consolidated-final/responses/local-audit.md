# Initial local final-manuscript review

Historical editing checklist, written before the independent report. Current
outcomes are in triage.md and revision-response.md.

- Main theorem is scoped to fixed L, zero initialization, exact continuous flow, first correction. The upper proof uses the tracking estimate, not its first-correction corollary; no circularity found.
- Replace undefined epsilon_L / c_L at end of tracking proof with epsilon_0 / c, matching its theorem.
- State epsilon in [0,1] when defining the coin distribution.
- Tighten path-event lemma to complete stopped episodes (first hit or H actions), which supplies its prefix-free premise.
- Add a short derivation of the critical scale from t^-1 versus epsilon t^-beta; label it an explanation of the candidate scale, with proofs supplied later.
- Explain the endpoint switch and weighted score s(b) immediately after the finite sum, since that is the reason the new upper-bound method works.
- Make positivity A(W), D(W), P(W) explicit once with formulas.
- Specify the compact set K0 and its trajectory image K1 as compact, rather than saying merely that they contain the points.
- Repair the repeated conjunction at the end of the exit-time argument and the awkward But after the infinite-exit alternative.
- Derived figure metadata still says conjectured/predicted, unlike the theorem in the paper. Update derived labels/keys to theorem, preserve all raw run files and numerical values.
- Caption should locate dashed lines in the slope panel and say each plotted slope is computed between consecutive diversity values.

No mathematical gap found in this local pass. Independent full-source review pending.
