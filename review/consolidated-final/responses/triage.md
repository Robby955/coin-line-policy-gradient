# Full-manuscript review triage

The fresh end-to-end reviewer returned **valid**, with no critical or major
mathematical gap. J1-J4 were classified as major exposition issues: the
arguments were correct but too compressed. Their expansions and the full
revised source were checked in the same dedicated review session. The final
verdict is **valid**, with no blocking issue and no error introduced.

| ID | Finding | Resolution |
|---|---|---|
| J1 | Occupancy derivative lacked the Bellman induction. | Added the Bellman recursion, derivative source, zero initial/terminal derivatives, and iteration over the stopped transition kernel. |
| J2 | One-sided Hessian estimate was not used visibly. | Displayed the exact vector difference equation and squared-distance inequality before the scalar comparison. |
| J3 | Clock conversion and compact bootstrap were dense. | Defined f_epsilon and positive g; displayed division by g; fixed K0 before the common clock time; stated why the region and uniform convergence hold on K2. |
| J4 | Probability-to-gradient bounds lacked explicit references. | Cited the path-score lemma in both rare-coin branches. |
| m1 | Exact failure probability and approximation both used F; other symbol overlaps. | Renamed the proxy Phi, the physical ratio varrho, the cross-products chi_s/chi_+, and the Lipschitz constant ell_0. Retained locally defined indexed path quantities P_omega, D_omega and E_omega; their indices and contexts distinguish them without adding another notation layer. |
| m2 | beta<1 was asserted. | Added the positive expression for M-n(L+1)-2r. |
| m3 | alpha_L and alpha not identified. | Defined alpha=alpha_L. |
| m4 | Several late-time estimates use eventual language. | Retained. Each is a fixed-L estimate on the unperturbed trajectory; adding a repeatedly enlarged T1 would not strengthen the argument or clarify its quantifiers. |
| m5 | tau0 described only as sufficiently small. | Set tau0=c/2, with c from the tracking theorem. |
| m6 | Finite first-exit time argued after boundary exclusion. | Proved the e^q time bound first, then excluded non-probe boundaries. |
| m7 | Slopes all exceed alpha. | Stated this observation without claiming a direction of approach from the theorem. |
| m8 | Tracking constants' order could look circular. | Chose R from the unperturbed probe before deriving the comparison constants. |
| L1 | Missing epsilon range and ambiguous stopped-path premise. | Stated 0<=epsilon<=1 and the first-success/horizon stopping rule. |
| L2 | Critical-scale and sign-switch mechanisms were too implicit. | Added the t^-1 versus epsilon t^-beta balance and the endpoint-score explanation. |
| L3 | Figure still called exponents predicted/conjectured. | Updated labels and derived summary keys; all numerical values and raw receipts are unchanged. |

No theorem, assumption, exponent, or scope was broadened. No human peer
review, formal verification, or upstream acceptance is claimed.

## Final confirmation

`revision-response.md` confirms J1-J4, every notation substitution, the
constant choices and the reordered first-exit proof. No mathematical gap
remains identified by either pass.

Four optional clarifications were left unchanged after confirmation:
varrho_1 is a real threshold shared by the physical and limiting ratio;
the theorem's K is the proof's A_R; V_0 below the coin is zero by the stated
hitting-probability definition; P_omega remains an indexed path probability,
distinct from the probe P. The reviewer explicitly judged all four
nonblocking. No mathematical edit followed this confirmation.
