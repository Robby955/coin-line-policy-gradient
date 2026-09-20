# Referee report — "The correction-time upper bound in the coin-line model"

**No tools were used and no computation was run.** Everything below is hand algebra on the displayed formulas, plus a logical audit. Where I say "checked," I mean I re-derived the identity symbolically by hand (and instantiated $L=4,5$ by hand arithmetic).

---

## 1. Verdict

**The upper bound does follow** — from the two stated inputs \eqref{eq:ray}, \eqref{eq:tracking} **plus a third, currently unstated, input: the path combinatorics.** I found no counterexample, and every quantitative identity I could check is correct, including the ones on which the argument is tight. The architecture is sound and, in two places (the endpoint-to-endpoint comparison in Lemma 1, and using \eqref{eq:tracking} at a *single* time $t_0$), it is well chosen.

Classification of what I found:

* **1 genuine logical hole as written**, one line to repair (M2).
* **1 substantive missing hypothesis**: Lemma 1 consumes combinatorial facts that are neither in the displayed path count nor in \eqref{eq:ray}–\eqref{eq:tracking} (M1).
* **3 "sketch-level" steps** that are routine but currently not arguments (M3–M5): the start-site decomposition of $\nabla J_\eps$, the §3 bootstrap, the §4 continuous-dependence step.
* The rest is exposition/notation.

Nothing I found threatens the conclusion. But as written, §2's Lemma and §4 are not yet a proof a reader can check without the companion notes in hand.

---

## 2. Ledger of what I verified by hand

These all check out, and several are *tight*, so they are worth recording:

| Claim | Status |
|---|---|
| $A+D=2d-b$, $a=(A-D+b)/2$, $q=A+3b$ ($b\ge0$), $q=2a+2b+D$ ($b<0$) | ✓ |
| $h-b=\tfrac12[(L+1)A+(L-1)D+(L-1)b]$ | ✓ |
| $(N-n)(h-b)+(N+S-n-r)b=(N-n)h+(S-r)b$; both terms $\ge0$ under $N>n$, $N+S\ge L+1$, $b\ge0$ | ✓ |
| $(N-n)[h+(L-1)b]+[S-N(L-1)]b$ identity; both terms $\ge0$ under $S\le N(L-1)$, $b<0$ | ✓ |
| $-\nabla F=Fz$ with $z=(n,s(b),nL)$, $\nabla\log Q=-x$, hence \eqref{eq:ratio} | ✓ |
| Brace at $R=R_0$: $s^2-(nL+2)s+n^2(1+\tfrac{L^2-L}{2})+n(2L-1)$ | ✓ |
| Its real minimum \eqref{eq:margin} $=n^2[(\tfrac L2-1)^2+\tfrac L2]+n(L-1)-1>0$ for $L\ge4,n\ge3$ | ✓ |
| $D_s/R_0-6\le -2/L$, **with equality at $s=n(L-1)$** | ✓ (tight) |
| $\frac{n+ks}{R}-(1+2k)\le-1-\frac{2(k-1)}{L}$ for $R\ge R_0$ | ✓ |
| $(1,-1,1)\cdot x=(-1,0,1)\cdot x=0$; $(1,-1,1)\cdot z=n(L+1)-s\ge2n$; $(-1,0,1)\cdot z=n(L-1)$ | ✓ |
| $d\mathcal R/ds=\mathcal R[(M-D_+)-(D_+-6)\mathcal R]$; $M>D_+>6$ | ✓ |
| $\mathcal R_*>R_0$ **is exactly** \eqref{eq:margin} evaluated at $s=r$ (since $M_r=M$, $D_r=D_+$) | ✓ |
| $u\cdot W=\alpha$, $x\cdot W=\alpha-1$, so both leading terms are exactly $\eps^\alpha$ at $WE$ | ✓ |
| $\eps\,t_0^{1-\beta}=\tau_0^{1/\alpha}$ at $t_0=\tau_0\eps^{-\alpha}$, using $1-\beta=1/\alpha$ | ✓ |
| Consistency of \eqref{eq:ray} with \eqref{eq:limit} at small $\tau$: forces $C_Le^{-u\cdot v}=1/M$ | ✓ (harmless, but see E5) |

**Uniformity for unbounded $w$ (your first question): this is genuinely achieved in §2–§3.** Every estimate there is *relative* ($\times(F+Q)$ or $\times Q$), the path log-gradients are bounded by $2L\|(1,L,L)\|$ uniformly in $w$, and the score gaps are $\ge\delta E$ with no hidden dependence on $|b|$. The region \eqref{eq:region} does **not** confine $b$, and it does not need to: $s(b)\to r$ as $b\to+\infty$ and $s(b)\to n(L-1)$ as $b\to-\infty$, and both endpoints are covered — by \eqref{eq:margin}'s min-over-real-$s$, by the tight bound $D_s/R_0-6\le-2/L$ at $s=n(L-1)$, and by the two-branch comparison in the Lemma. **The "keep all minimal-left-count paths" device is doing real work**, and I could not break it.

**Path-class coverage (your second question).** The classes are: $(c=L,\ \text{fail},\ N=n)$ → $Fz$; $(c=L,\ \text{fail},\ N>n)$ → $O(e^{-\delta E}F)$; $(c=1,\ \text{above},\ \text{succ},\ 1\ \text{left})$ → $-Qx$; $(c=1,\ \text{above},\ \text{succ},\ \ge2\ \text{lefts})$; $(c\ge2,\ \text{above},\ \text{succ})$; $(c<L,\ \text{below},\ \text{fail})$; start $=$ coin site (zero gradient). Complementary classes are absorbed by $\sum_{\text{all}}\nabla p=0$. **The list is complete** — provided M3 below is stated.

---

## 3. Mathematical gaps

**M1 (substantive — missing input). Lemma 1 uses combinatorics beyond the displayed count.** The displayed facts ($N\ge n$, $N+S\ge L+1$, $S\le N(L-1)$) are asserted only for *failed coin-$L$* paths, but the proof additionally uses, without statement or proof:

* (a) "failure from below **any** coin requires at least $n$ left actions" — needed for every rare $c$, including $c$ near $L$;
* (b) for $c\ge2$, every above-success contains a left action at site $c+1$;
* (c) for $c=1$, the one-left-action above-success is unique and is the step from site $2$, and every other above-success contains that step *plus* a further left action;
* (d) $m_r>0$ and $m_{n(L-1)}>0$.

(d) deserves particular attention because the $b<0$ branch of the Lemma (and only that branch) rests on it: $S=n(L-1)$ with $N=n$ forces **all** $n$ left actions at site $L-1$, hence $\ge 2n-1$ steps of oscillation plus the approach, and the path must still *fail* within horizon $2L$. That is a nontrivial compatibility condition between $n$, $L$ and the horizon; it looks satisfiable for $L\ge4$, but it must be verified in the companion note, not asserted here. **Fix:** promote (a)–(d) to a numbered "Input (C)" with a proof or an explicit pointer, on the same footing as \eqref{eq:ray}–\eqref{eq:tracking}. Note that (a) also silently assumes the logit index ranges (see E1).

**M2 (genuine hole, one-line fix). $q\ge\delta E$ on \eqref{eq:region} is used but never established.** In the last paragraph of the Lemma's proof, the $b<0$ case concludes "so $n$ copies exceed $q$ by at least $\delta E$" from "minimum below-coin logit $\ge q$". That inference needs $(n-1)q\ge\delta E$, i.e. a *lower* bound on $q$, which is nowhere in \eqref{eq:region}. It is true — $b\ge0$: $q=A+3b\ge\delta E$; $b<0$: $q=2a+2b+D\ge 2(1-k)b+D\ge D\ge\delta E$ using $a\ge-kb$ and $k\ge2$ — but as written the step is unjustified. Add it as a displayed consequence right after \eqref{eq:bd}.

**M3 (missing statement, real risk of double counting). The two representations of $\nabla J_\eps$ are never reconciled.** The proof uses *failed* paths for coin $L$ and *successful* paths for rare coins from above and *failed* paths for rare coins from below. This is legitimate only because, for each (coin, start-site) pair separately, $\sum_{\text{all paths}}\nabla p=0$, so $\nabla J_{c,p_0}=\nabla\sum_{\text{succ}}p=-\nabla\sum_{\text{fail}}p$ and one may choose the representation per pair. Without that sentence the reader cannot tell why rare-coin above-*failures* (weight $\eps$, but potentially cost $\ll\delta E$) never appear, nor why the below-failures are not double counted against $F$. One sentence; but it is the hinge of the whole class enumeration.

**M4 (sketch → argument). §3's bootstrap is asserted.** "Thus the region and ratio barrier persist until correction" mixes three mutually dependent claims: \eqref{eq:decrease}/\eqref{eq:preserve} need $R\ge R_0$; the barrier needs \eqref{eq:region}; the region needs \eqref{eq:preserve}. **Fix:** set $t^\ast=\inf\{t>t_e: A=\delta E \text{ or } D=\delta E \text{ or } R=R_0 \text{ or } P=0\}$; on $[t_e,t^\ast]$ all estimates hold by continuity in the *closed* region; then $\int_{t_e}^{t^\ast}Q\le2P(t_e)\le2C_0E$ gives $A,D\ge 2\delta E-2CC_0\zeta E>\delta E$, and $R'>0$ at $R=R_0$ excludes the third alternative — so $t^\ast$ is a $P$-zero. As written the paragraph reads circularly even though it is not.

**M5 (sketch → argument). §4's entrance is the least finished step.** Specifically:

* (i) The *crux* of \eqref{eq:limit} is not the displayed limit but the assertion that **no path class contributes at $\eps$-exponent $<\alpha$**. That is exactly the balance defining $W$ ($u\cdot W=\alpha$ and $1+x\cdot W=\alpha$), and it must be checked class by class, as in Lemma 1. The paper gives one clause ("the zero-diversity score gaps are strict at $W$") plus the below-coin check. The $\theta_1$ sentence is unreadable as stated: $\theta_1$ is undefined, and the intended content appears to be $(a+d)|_W=\alpha n(L+1)/M$, hence the requirement $n^2(L+1)>x\cdot u=n(L+1)+2r$, i.e. $n(L+1)(n-1)>2r$. That is true for $L\ge4$, but write it.
* (ii) "including its first derivatives on compact sets" is asserted with no proof and, as far as I can tell, is not what is needed — local Lipschitzness of the *limit* field plus $C^0$ uniform convergence suffices for the Gronwall/first-exit step.
* (iii) The first-exit argument needs an explicit enlarged compact: the limiting orbits on $[0,s_*]$ lie in a compact $\mathcal K_1$ (because $\mathcal R$ is monotone toward $\mathcal R_*$, hence bounded, hence $\|dy/ds\|\le\|u\|+\mathcal R\|x\|$); take a $1$-neighbourhood, get uniform convergence there, Gronwall, exit excluded for small $\eps$.
* (iv) The translation $s_*\mapsto\tau$ via $d\tau/ds=e^{U}/C_L$ requires $U=u\cdot y$ bounded **above** on the orbit, which follows from (iii) but is not said.
* (v) $R=Q/F\to\mathcal R$ must be uniform **along the trajectory**, not merely pointwise on compacts. It follows from (iii) + the $S=r$ domination, but the paper states only the latter.

None of (i)–(v) looks hard. (i) is the one with mathematical content.

---

## 4. Exposition / notation (no mathematical consequence)

* **E1.** The logit index ranges are never stated. The two extreme cases used ($a+d$ at $(p,c)=(0,1)$ for $b\ge0$; $a+Lb+d$ at $(L,1)$ for $b<0$) are correct **iff** $p\in\{0,\dots,L\}$, $c\in\{1,\dots,L\}$, $z_{p,c}=a+pb+cd$. Say so. Also: the step "$a+d\ge\delta E$ ⟹ every logit $\ge\delta E$" needs the trivial monotonicity $z_{p,c}\ge a+d$ for $b\ge0$, $d>0$, $c\ge1$. Relatedly, $x=(1,2,1)$ hardcodes "coin at site 1, reached from site 2"; if the model admitted $c=0$, the rare-coin leading form would be $(1,1,0)$ and $\alpha$ would change. One clause fixes this.
* **E2.** The order of constant selection is genuinely confusing: $\delta$ is used throughout §2–§3 but pinned only in §4 ("smaller than half the values of $A(W)$, $D(W)$"). State the order once: $L\Rightarrow W\Rightarrow\delta\Rightarrow\tau_0\le c\Rightarrow\mathcal K_0\Rightarrow s_*,\mathcal K_1\Rightarrow C_0\Rightarrow\eps_0$. There is no circularity, but the reader must reconstruct that.
* **E3.** "Failure from below any coin" in Lemma 1 is about *rare* coins only (coin-$L$ below-failures are already inside $F$). As written it reads as if it double counts. Same paragraph: "Differentiate these below-coin contributions through their failure probabilities" is the only hint of M3.
* **E4.** In \eqref{eq:logistic}, "$s$" is simultaneously the clock and the score coordinate; the parenthetical in "Applying \eqref{eq:margin} at $s=r$ (the score coordinate, not the clock)" concedes the collision rather than fixing it. Rename the clock $\sigma$.
* **E5.** The values $C_L=1/(L+1)$ (odd), $n/(L+1)$ (even) are stated but never used — $\mathcal R_*=(M-D_+)/(D_+-6)$ is independent of $C_L$, and $C_L$ affects only the initial ratio, which needs to be merely positive and finite. Either drop them or mark them as not load-bearing. (Note also the hidden consistency requirement $C_Le^{-u\cdot v}=1/M$ between \eqref{eq:ray} and \eqref{eq:limit}; worth a remark, since it is a nontrivial cross-check of the two companion notes.)
* **E6.** State that the flow is globally defined ($\|\nabla J_\eps\|\le C(L)$ uniformly), and note that $P(0)=0$ so $T_\eps>0$ needs $P'(0)>0$ — supplied by the lower-bound note, but the definition of $T_\eps$ as an infimum over $t>0$ from an initial point *on* $\{P=0\}$ deserves a word.
* **E7.** The lower bound $T_\eps\ge c_-\eps^{-\alpha}$ is listed among the inputs but is used **only** for the $\Theta$/limit corollary, never for the upper bound. Say that; it makes the logical dependency graph of the three notes clean.

---

## 5. Minimal repair list

1. Add "Input (C)" with M1(a)–(d), proved or cited. *(Required.)*
2. Insert $q\ge\delta E$ on \eqref{eq:region} after \eqref{eq:bd}. *(Required; one line.)*
3. Insert the per-(coin, start) complementarity sentence (M3). *(Required; one sentence.)*
4. Rewrite the §3 closing paragraph as a first-exit argument (M4). *(Half a page.)*
5. Expand \eqref{eq:limit} into a class-by-class exponent check mirroring Lemma 1, and write out (iii)–(v) of M5. *(One page.)*
6. E1, E2, E4, E7.

With 1–3 done and 4–5 written out, I would regard the upper bound as established modulo the two named inputs plus Input (C). I see no obstruction to any of these; in particular I searched specifically for a failure of uniformity at $|b|\to\infty$, for an uncovered path class, for a sign error in \eqref{eq:ratio}/\eqref{eq:preserve}, and for a mismatch between $\mathcal R_*$ and $R_0$, and found none.

## 6. Scope

The §5 disclaimers are accurate and appropriately conservative. Two additions worth making explicit: (i) the constants degrade in $L$ — the margin in \eqref{eq:decrease} is exactly $2/L$ and \eqref{eq:decrease} is *tight* at $s=n(L-1)$, so nothing here survives $L\to\infty$ without new work; (ii) the result is conditional on three companion inputs, one of which (Input (C)) is currently implicit. Since no publication has occurred, folding (C) into the trajectory note before combining is the cleanest route.