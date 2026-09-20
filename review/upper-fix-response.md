# Final verdict

**Conditional acceptance.** M1–M5 are closed. I re-checked only the new material (per your instruction) plus the few identities the new material touches; I found no remaining mathematical gap. No tools or computations were run — this is hand verification of the new passages.

Under the two named inputs \eqref{eq:ray}, \eqref{eq:tracking} — and the two facts still imported by reference from the trajectory note, itemized in §3 below — Theorem 1 follows: $T_\eps\le c_+\eps^{-\alpha}$, and with the accepted lower bound, $T_\eps=\Theta_L(\eps^{-\alpha})$ and $\log T_\eps/\log(1/\eps)\to\alpha$.

---

## 1. Closure of M1–M5

**M1 (path facts) — closed.**

*Below-start failures, all $c$.* The new identity $p_0+2L-2N_-\le p_{2L}\le c-1$ is correct (the inequality on the left is the right direction if the walk has a floor at site $0$, so the argument survives a boundary). It gives $N_-\ge\lceil(2L+p_0-c+1)/2\rceil$, and minimizing over $p_0\ge0$, $c\le L$ yields $\lceil(L+1)/2\rceil=n$. Checked in both parities: for $c\le L-1$ one actually gets $\lceil(L+2)/2\rceil$, equal to $n$ for even $L$ and $n+1$ for odd $L$. This also reproduces the $N\ge n$ half of the displayed coin-$L$ count as a special case, which is a good internal consistency check.

*Above-start successes.* "Must take a left action at $c+1$" is immediate from continuity of the walk; the $c=1$ uniqueness clause ("any larger start or any preceding right action requires another left action") is now argued rather than asserted.

*$m_{n(L-1)}>0$.* The explicit constructions are correct, and this was the item I flagged as genuinely at risk. Verified: climb $0\to L-1$ ($L-1$ rights), then $(\mathrm{L},\mathrm{R})^n$ for odd $L$ — lengths $L-1+2n=L-1+(L+1)=2L$ ✓; or $(\mathrm{L},\mathrm{R})^{n-1}\mathrm{L}$ for even $L$ — $L-1+2(n-1)+1=L-1+(L+1)=2L$ ✓ using $n=(L+2)/2$. In both, all $n$ left actions occur at site $L-1$, so $N=n$, $S=n(L-1)$; the walk never exceeds $L-1$, so both fail. Also $N+S=nL\ge L+1$, consistent with the displayed count. This is exactly what the $b<0$ branch of Lemma 1 needs.

*$m_r>0$* remains a reference (see §3).

**M2 ($q\ge\delta E$) — closed.** The added sentence derives it twice over: as the logit $z_{2,1}$ (legitimate once "every training logit $\ge\delta E$" is in hand, and $(2,1)$ is a state for $L\ge2$), and directly via $q=A+3b$ for $b\ge0$, $q=2a+2b+D\ge 2(1-k)b+D\ge D$ for $b<0$ with $k\ge2$. The step "so $n$ copies exceed $q$ by at least $\delta E$" now has its missing premise, since $(n-1)q\ge 2\delta E$ for $n\ge3$.

**M3 (double counting) — closed.** The opening paragraph of the proof states the per-(coin, start) complementarity, disposes of starts at the coin, and — crucially — quarantines coin $L$: the whole coin-$L$ contribution goes through failures, and the success-above/failure-below split is used *only* for $1\le c<L$. The body now matches ("For coins $2\le c<L$…", "for the remaining coins $1\le c<L$, failure from below…"). With this, the class list is exhaustive and disjoint: coin-$L$ failures with $N=n$ and with $N>n$; coin-$1$ above-successes with one and with $\ge2$ left actions; $c\ge2$ above-successes; $c<L$ below-failures; starts at the coin. No class is uncovered and none is counted twice.

**M4 (bootstrap) — closed.** The first-exit argument is now correct as written. $t^\ast$ is the first hitting time of the union of four boundary conditions; the estimates hold on $[t_e,t^\ast)$ and extend to $t^\ast$ by continuity; $\int_{t_e}^{t}Q\le 2P(t_e)\le 2C_0E$ then gives $A,D\ge 2\delta E-2CC_0\zeta E>\delta E$ for small $\eps$, excluding two alternatives; $R(t^\ast)=R_0$ is excluded because a first downward crossing forces $R'(t^\ast)\le0$ while the barrier gives $R'(t^\ast)>0$ (the barrier applies at $t^\ast$ because $w(t^\ast)$ is still in the closed region). Simultaneous hits are handled, since each non-$P$ alternative is excluded individually. The $t^\ast=\infty$ branch is now explicitly ruled out by $(e^q)'\le-\eps/(L^2(L+1))$, which is the one structural hole the old version had left implicit.

**M5 (entrance) — closed.**

*Exponents.* Checked the two new formulas. $n\theta_1-\beta=[n^2(L+1)-n(L+1)-2r]/M=[n(n-1)(L+1)-2r]/M>0$ ✓, and $1+\alpha n\theta_1>\alpha\iff n\theta_1>\beta$ ✓, matching the below-coin cost $n(a+d)|_W=\alpha n\theta_1$. For $c\ge2$, $\beta_c=[n+(c+1)r+cnL]/M$ is exactly $z_{c+1,c}|_W/\alpha$, and $\beta_c>\beta$ termwise ✓. The non-direct coin-$1$ clause is fine because every logit at $W$ is strictly positive ($W$ has all coordinates positive).

*Quantitative comparison.* The $\mathcal K_0\subset\mathcal K_1\subset\mathcal K_2$ construction is correct: $\mathcal R$ stays between its initial value and $\mathcal R_*$, so $\|dy/ds\|\le\|u\|+\mathcal R\|x\|$ is bounded and $\mathcal K_1$ is compact; the clock factor is bounded above and away from zero on $\mathcal K_2$, which is what transfers uniform convergence of $\eps^{-\alpha}\nabla J_\eps$ to the reparametrized fields. The Gronwall bound $\eta_\eps s_*e^{H_0s_*}$ is the correct form (it dominates $\eta_\eps(e^{H_0s}-1)/H_0$), and the "$<1$ excludes exit from $\mathcal K_2$" continuation is legitimate because $\mathcal K_2$ is the *closed one*-neighbourhood. The sentence that initial points are taken equal — so no convergence of initial data is needed — correctly handles the $\eps$-dependence of $y_\eps(t_0)$. Items (iv) and (v) of my earlier list are now explicit: $u\cdot y$ bounded above on $\mathcal K_2$ bounds $d\tau/ds$, giving $t_e=O(\eps^{-\alpha})$; and $Q/F\to\mathcal R$ uniformly on $\mathcal K_2$, which with the trajectory comparison and continuity of $\mathcal R$ yields $R>R_0$ at $s_*$. Dropping the $C^1$ claim is right — only $C^0$ uniform convergence plus local Lipschitzness of the *limit* field is used, and that is what is now stated.

---

## 2. Residual items (none blocking)

1. **Redundant $\delta$ choice.** §2 now fixes $\delta$ up front; §4 still says "Choose $\delta>0$ smaller than half the values of $A(W)$ and $D(W)$." Delete the §4 sentence — as it stands it reads as a second, independent choice.
2. **Coin-$L$ non-minimal classes in §4** are covered only by "the zero-diversity score gaps are strict at $W$", while the rare classes get explicit exponents. The fact is trivial — the exponent of a coin-$L$ failure at $W$ is $\alpha[Nn(1+L^2)+Sr]/M$, equal to $\alpha$ at $(N,S)=(n,r)$ and strictly increasing in both arguments — but one clause would make "These are all path classes" self-evidently complete.
3. **Simpler route to \eqref{eq:limit}.** Since $WE+y$ lies in \eqref{eq:region} for large $E$ (as $A=A(W)E+O(1)\ge\delta E$ by the §2 choice of $\delta$), \eqref{eq:limit} is an immediate corollary of Lemma 1 together with $s(b)\to r$, $F\sim C_L\eps^\alpha e^{-U}$, $Q=B\eps^\alpha e^{-q_y}$ and $\zeta\to0$. Citing it that way would make the exponent enumeration a cross-check rather than a second, parallel argument.
4. **Unstated conventions**: index ranges $p\in\{0,\dots,L\}$, $c\in\{1,\dots,L\}$, $z_{p,c}=a+pb+cd$ (used implicitly at $(0,1)$, $(L,1)$, $(2,1)$, $(L-1,L)$); global existence of the flow from $\|\nabla J_\eps\|\le C(L)$; that $P(0)=0$ so $T_\eps>0$ relies on the lower-bound note.
5. **Clock/score collision on $s$** persists (the parenthetical concedes it); rename the clock.
6. **The lower bound is used only for the $\Theta$ corollary**, never for the upper bound. Worth one sentence, since it makes the dependency graph of the three notes acyclic.
7. $C_L$'s parity values remain stated but unused — only $0<C_L<\infty$ matters ($\mathcal R_*$ is independent of $C_L$). Harmless; marking them non-load-bearing would preempt a reviewer checking them.

---

## 3. Exactly what the acceptance is conditional on

Beyond \eqref{eq:ray} and \eqref{eq:tracking}, the argument still consumes two facts by reference to the trajectory note, both in §2: (i) the coin-$L$ failure count $N\ge n$, $N+S\ge L+1$, $S\le N(L-1)$ — of which $N\ge n$ for below starts is now re-derived here, the other two are not; and (ii) $m_r>0$. Item (ii) is the same fact that pins the ray direction $u$ in \eqref{eq:ray}, so it is not an independent assumption, but it is load-bearing in two places ($F\ge\frac{m_r}{L+1}e^{-nh-rb}$ in the $b\ge0$ branch, and $C_L>0$ in §4) and should be given a pointer to the specific construction rather than "the explicit paths used in the zero-diversity trajectory proof."

Subject to those, and with items 1–2 above applied, I would accept the upper-bound note for combination with the two companion notes. The §5 scope statement remains accurate; I would add only that the constants degrade in $L$ (the margin in \eqref{eq:decrease} is exactly $2/L$ and is attained at $s=n(L-1)$), so nothing here is uniform as $L\to\infty$.