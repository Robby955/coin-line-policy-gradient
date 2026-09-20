# Review triage

Two fresh Claude Code review sessions used model `claude-opus-5`, with tools
disabled. The reviewers received exact source snapshots and no claimed test
successes as premises. This is independent model review, not human peer review
or formal verification. Exact visible responses are archived separately.

| ID | Severity | Finding | Resolution |
|---|---|---|---|
| R1 | major exposition | Strict derivative signs need the first-passage inequality and horizon monotonicity. | Displayed the inequality and justified both strictness events. |
| R2 | major exposition | Dominant path counts need an exhaustion argument. | Added the exclusion of left moves at site >=2 and the forced final right run. |
| R3 | minor | Global existence should justify bounded derivatives. | Added bounded first and second derivatives of the finite logistic polynomial. |
| R4 | claim scope | The standalone lower-bound abstract presumed finite correction. | Removed it there; consolidated finiteness follows from the new upper bound. |
| R5 | exposition | Specify the OOD probe and distinguish its logit from the corrective state defining beta. | Explicit model and explanation in Section 1. |
| R6 | exposition | Finite-event gradient estimate should be stated explicitly. | Added the path-score lemma with path-count and score bounds. |
| R7 | notation | D, offsets, and the score/clock s collide after consolidation. | Tracking distance is Delta; theorem offset is w_infinity; transition clock is xi. Context separates the other indexed symbols. |
| R8 | optional strengthening | Export a quantitative zero-ray remainder. | Deferred: bounded-offset asymptotics suffice for the compact entrance argument; no such rate is claimed. |
| U1 | major exposition | Uniform approximation uses unstated path facts and endpoint-score attainment. | Added all path facts and explicit odd/even endpoint constructions. |
| U2 | proof detail | The rare below-coin estimate needs q >= delta E. | Displayed its derivation in the invariant region. |
| U3 | major exposition | Reconcile success/failure representations and avoid double counting coin L. | Added per-start complementarity and restricted rare-coin remainder classes to c<L. |
| U4 | major exposition | Simultaneous region/ratio preservation needs a first-exit argument. | Defined the first exit and excluded each non-probe boundary quantitatively. |
| U5 | major exposition | Critical-scale entrance needs class-by-class exponents and compact control. | Expanded every exponent class; added enlarged compact, uniform error, Gronwall bound and bounded clock conversion. |
| U6 | minor | C1 convergence is asserted but unnecessary. | Removed it; uniform field convergence and Lipschitzness of the limit suffice. |

The first reviewer accepted the ray and lower-bound theorems after these
repairs. The upper-bound review accepted the repaired argument under those
inputs and the path facts; see upper-fix-response.md and the outcome below.

## Final outcome

The upper-bound follow-up accepted M1-M5 as closed. Its stated inputs are
proved in Sections 2 and 3 of the unified paper, including the full path-count
inequalities and the positive endpoint coefficient. Final nonblocking repairs:
removed the second delta choice; renamed the clock xi; made global existence
and index ranges explicit; stated that L is fixed. Following the reviewer's
recommended simplification, the compact limiting field is now derived directly
from the uniform approximation lemma and the endpoint term of the finite sum.
This avoids duplicating the same path-class exponent argument.

No critical or major review issue remains open. The sharp limiting prefactor,
random initializations, permanent correction, and discrete/sampled updates
remain outside the theorem rather than deferred proof gaps in its statement.
