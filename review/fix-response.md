# Final Report (conclusion)

## 1. Do the stated fixes resolve the correctness concerns?

**Yes — for both theorems, with two riders.**

**Fix 1 (strict positivity).** The proposed display
$$V_j(q)\le \Pr_q[\tau_{\mathrm{near}}\le j]\,V_j(\mathrm{near})<V_j(\mathrm{near})$$
is valid and is the right repair. **Rider:** the first inequality is not immediate from the first-passage decomposition alone — it passes through
$$V_j(q)=\sum_{\tau\ge1}\Pr_q[\tau_{\mathrm{near}}=\tau]\,V_{j-\tau}(\mathrm{near})\le \Pr_q[\tau_{\mathrm{near}}\le j]\,V_{j-1}(\mathrm{near}),$$
so **monotonicity of $V_j(\cdot)$ in the remaining horizon $j$ must be stated** (one line: shrinking the horizon cannot increase success). With that, strictness at $i=0$, $j=H-1$ follows from $V_{H-1}(p+1)>0$ (distance $L-p-1\le L-1\le H-1$) and $\Pr_q[\tau_{p+1}\le H-1]<1$ (all left-action probabilities are positive). The chain $\kappa_p>0\Rightarrow a'>0,b'>0\Rightarrow$ cone $\Rightarrow a\to\infty$ is then intact, and with it [LB]'s use of $a_0'>0$, $b_0'>0$.

**Fix 2 (exhaustiveness).** "Once the walk reaches site $\ge2$ it cannot take another left in a minimal-score path, hence all left actions precede the final right run" is exactly the missing step and closes the multiplicity count ($1$ for odd $L$, $n$ for even $L$), hence $C_L$. Please add the companion half-line already implicit in the draft: a left action at site $\ge2$ is impossible in the first place, since it would force $S\ge n+1>r$ (odd) or $S\ge n>r$ (even). **Recommend applying the same sentence to [T] §3**, whose "all remaining actions are determined" for $u_-=n(1,L-1,L)$ has the identical hole (there the statement is: lefts occur only at $L-1$, so each must be preceded by a return right, and $p_0\le 2n-L-1$ pins $p_0=0$ for odd $L$, $p_0\in\{0,1\}$ for even $L$).

**Fix 3 (global existence).** Bounded derivatives of the finite logistic polynomial is the correct and sufficient justification. Note that boundedness of $\nabla J_0$ alone already precludes blow-up; the derivative bound is what you actually need again in [LB] §3 ("after increasing the constants on a compact initial interval"), so state it once and cite it twice.

**Fix 4 (abstract).** Dropping "a small positive training diversity eventually corrects the test-state verdict" removes the only unsupported assertion I found in [LB]. **Rider:** the same implication survives in [LB] §5 ("The theorem implies $\eps T_\eps\to\infty$. Thus an inverse-diversity correction-time bound would be too short in this model"), which is fine, but the consolidated text should state once and explicitly that **$T_\eps<\infty$ is not proved anywhere**, so $T_\eps=+\infty$ is not excluded by anything in the lower-bound chapter.

With Fixes 1–4 and the two riders, **I have no remaining correctness objection to [R] Theorem 1 or [LB] Theorem 1.**

## 2. Remaining essential conditions and non-correctness gaps

1. **Definitional (must fix).** [LB] §1 never defines the test state: $P_\eps=a_\eps+kb_\eps$ implicitly sets the coin coordinate $c=0$, which lies outside the training support $\{1,\dots,L\}$, and $k=\lceil L/2\rceil$ is unmotivated. The proof is unaffected, but the theorem's *meaning* is unanchored. Add one sentence tying $(p,c)=(k,0)$ to the A8 OOD probe.
2. **Probe mismatch (must explain).** [R] §6 computes $\beta_L$ for the logit at $(p,c)=(2,1)$; [LB] crosses at $(k,0)$. These are consistent — $\beta=\beta_1$ governs $\|G\|$, while $v_*=(1,k,0)$ is the probe — but the consolidated manuscript must say so, or a reader will read $\beta$ as the probe's exponent.
3. **Standing hypothesis.** $L\ge4$ (hence $n\ge3$) is genuinely load-bearing: it supplies $n\theta_1>\beta$ in [LB] §2 and $\alpha>1$ in [LB] §1. Keep it visible.
4. **Quantifier in `eq:Gbound`.** $G$ has no $t$-argument; restate as: for all $w$ with $\|w-w_0(t)\|\le R$, $\|G(w)\|\le C_R(1+t)^{-\beta}$.
5. **State the finite-path lemma.** [LB] §2's "a bound on the probability of every path in a fixed finite event also bounds the gradient" should be a displayed lemma with the explicit count $\le(L+1)2^{H}$ and score-norm $\le H\sqrt{1+2L^2}$; it is used four times.
6. **Export the rate, not just $o(1)$.** [R] proves $w_0(t)=\frac uM\log t+w_\infty+O(t^{-\gamma n/M})$. [LB] only needs $o(1)$, but the upper-bound session will need the quantified rate for the entrance/matching step. Promote it into the statement of [R] Theorem 1.
7. **Scope of $w_\infty$.** [R] pins only $u\cdot w_\infty=\log(C_LM)$ (plus $d=La$). Downstream text must not assume $w_\infty$ is otherwise determined.
8. **Notation collisions across the three documents** (a consolidation hazard, not a mathematical one): $J_0$ means the coin-$L$ return in [R] but would read as coin-at-$0$ in [LB]'s $J_c$ family; $v$ is [R]'s intermediate $a$-parametrised offset but [LB]/[T]'s $w_\infty$; $\kappa$ is $n(1+L^2)/M$ in [LB] and $(MX-D^2)/(D-X)$ in [T]; $D$ is $\|w_\eps-w_0\|$, $u\cdot x$, and $D_\omega$; $x$, $E$, $B$, $R$ each carry two meanings. Harmonise before merging.
9. **Keep the Dini-derivative remark** in [LB] §4; it is the correct handling of $D=0$.

**Robustness note worth recording:** [LB] Theorem 1 uses only $w_0=\frac uM\log t+v+o(1)$, $1-J_L\sim1/(Mt)$, $d_0=La_0$, $a_0'>0$, $b_0'>0$ — **none of which depends on $C_L$**. So even if the multiplicity count were wrong, the lower bound would stand. Likewise [T] §4's scaled crossing table depends only on $(u,u_-,x,W,k)$ and is insensitive to $C_L$, $B$, and $\tau^\ast$.

## 3. The $\alpha$ exponent and the transition analysis

$\alpha=1/(1-\beta)$ is **correct as a lower-bound exponent** and is the natural candidate, since $\beta=\beta_1$ is attained (coin $c=1$, start $p=2$, single left action) and is strictly below every competing exponent ($\beta_c$ for $c\ge2$, $n\theta_c$ for below-coin failures). But the lower bound stops when the displacement is $O(1)$, whereas crossing $P_\eps=0$ requires displacement $\Theta(\log(1/\eps))$. That is a genuine logarithmic-scale gap, compounded by the $b=0$ score switch. **The proved statement does not make $\alpha$ the true exponent.**

[T] is not hiding an obstruction; it names the right one. Its §1 limit is valid only on compact $y$, and the reduced ODE's finite-$\tau^\ast$ escape is an artefact of the exponential approximation (the true field is bounded — [T] says this). I re-derived [T]'s three "Predicted $(a,b,d)/E$" rows exactly from the two-segment construction, so the table is arithmetically sound and tests the *geometry*, not the prefactors; the residuals against the $\eps=10^{-96}$ column correspond to $O(1)$ additive offsets in $w$ at $E\approx221$, i.e. consistent but weak. One presentational defect: the §4 comparison pairs "reduced time to $q=-12$" against $\eps^\alpha T$ at crossing — different events; label it as a proxy.

**Upper-bound routes, classified:** (i) *entrance/matching* — **incomplete but likely completable** with existing tools: at $t=\eta\eps^{-\alpha}$ the tracking bound already gives $D=O(\eta^{1-\beta})$, which is the singular entrance condition with a quantified error; (ii) *compact-$y$ interior on $[\eta,\tau_1]$* — **incomplete, routine** (Grönwall against a locally Lipschitz limit field); (iii) *the $O(E)$ regime and the $b=O(1)$ layer* — **conjectural**, the real obstruction; the concrete suggestion is a uniform "$N=n$" expansion $\nabla J_L\approx\frac{e^{-nh}}{L+1}\sum_S m_S e^{-Sb}(n,S,nL)$, valid for $h\to\infty$, $h+(L-1)b\to\infty$, $b\in\mathbb R$ arbitrary, which interpolates $u$ and $u_-$ and turns the switch into a regular (not singular) layer, together with a tropical/piecewise-linear limit for $\hat y=y/E$; (iv) finally, any upper bound must first prove $T_\eps<\infty$, which nothing currently does.

## 4. Verdict

**[R] Theorem 1: ACCEPT** after Fixes 1–3 plus the horizon-monotonicity line and the "no left at site $\ge2$" line.
**[LB] Theorem 1: ACCEPT** after Fix 4 plus items 1, 4, 5 above.
**Package-level claim: LOWER BOUND ONLY.** $T_\eps=\eps^{-\alpha+o(1)}$, and even $T_\eps<\infty$, remain unproved here; the upper-bound chapter is outside this audit. No public acceptance, independent replication, or formal verification is implied by anything in this report.