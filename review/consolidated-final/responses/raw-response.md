# Adversarial Audit — *Correction times for linear policy gradient on a coin line* (ab42e66)

## (a) Verdict

**Valid**, with no critical or major mathematical gap found. Every load-bearing identity and inequality I could re-derive from the supplied text checks out. The residual issues are compression and notation, not logic. Confidence is bounded by the fact that a handful of steps (§2.1 κ-identity, §3.3 Grönwall step, §4.3 clock/compactness) are asserted at a density where an error could hide; I re-derived each and found them correct, but they are the places a referee will stall.

---

## (b) Findings

### Critical
None.

### Major (all "correct but too compressed", not gaps)

**J1. §2.1, the identity for $\kappa_p$.** The displayed formula
$\kappa_p=\sigma(z_p)\sigma(-z_p)\sum_i\rho_i(p)[V_{H-i-1}(p+1)-V_{H-i-1}(p^-)]$
is the finite-horizon policy-gradient theorem. A reader will immediately object that $\rho_i(p)$ itself depends on $z_p$, and the text ("Differentiating the finite Bellman recursion gives") does not say why those terms vanish. They do — the occupancy-derivative terms telescope, as in the standard policy-gradient theorem with deterministic transitions — but this is the foundation of the whole cone \eqref{ray:eq:cone} and of $b'>0$. *Repair:* one sentence naming the policy-gradient theorem, or three lines of the telescoping induction on $j$.

**J2. §3.3, derivation of $\Delta'\le K_R(t)\Delta+\eps C_R(1+t)^{-\beta}$.** The sentence "Integrating \eqref{track:eq:onesided} along that segment and using \eqref{track:eq:Gbound}" hides the two steps that actually matter: (i) $w_\eps'-w_0'=[\nabla J_L(w_\eps)-\nabla J_L(w_0)]+\eps G(w_\eps)$, and (ii) $\langle \delta w,\int_0^1\nabla^2J_L(w_0+s\,\delta w)\,\delta w\,ds\rangle\le K_R(t)\|\delta w\|^2$, which is exactly what the *one-sided* form \eqref{track:eq:onesided} delivers (a two-sided norm bound would be wasteful, and no lower bound is needed). *Repair:* two displayed lines. This is the single most important place to spend space, because it is where the "one-sided Hessian" motivation pays off.

**J3. §4.3, the clock change and the compactness bootstrap.** The paragraph beginning "Apply the same positive clock factor $C_Le^{-u\cdot y}$" is dense. Three things should be said explicitly: (i) multiplying *both* the $\eps$-family and the limit field by the same positive smooth $C_Le^{-u\cdot y}$ is a time reparametrisation, so orbits are unchanged and only the parametrisation differs; (ii) the $\xi$-parametrised full field is an $\eps$-indexed family, and uniform convergence on $\mathcal K_2$ follows from \eqref{upper:eq:limit} divided by a factor bounded above and away from zero on the compact $\mathcal K_2$; (iii) for $y\in\mathcal K_2$ and $E$ large, $WE+y$ satisfies \eqref{upper:eq:region} automatically (since $A(W),D(W),P(W)>0$), so Lemma~\ref{upper:lem:uniform} is legitimately available throughout the bootstrap — currently this is stated only for "a fixed compact set" at the start of §4.3 and never re-invoked for $\mathcal K_2$.

**J4. Lemma~\ref{upper:lem:uniform}, below-coin branch.** "Differentiate these below-coin contributions through their failure probabilities" needs the per-path logarithmic-gradient bound to convert a probability bound into a gradient bound. That bound is Lemma~\ref{lem:path-score}, proved in §3; §4 never cites it. *Repair:* cite Lemma~\ref{lem:path-score} explicitly in both the above-coin and below-coin branches.

### Minor

**m1. Symbol collisions that will actively mislead.** In order of severity:
- $F$: §2 defines $F:=1-J_L$ (an exact failure probability); \eqref{upper:eq:F} redefines $F$ as a *proxy* exponential sum that is **not** $1-J_L$. The paper never flags this. Rename the §4 object (e.g. $\Phi$).
- $R$: the tracking radius (§3.1–3.3) vs. the ratio $Q/F$ (§4.2). Rename one (e.g. $\rho=Q/\Phi$, keeping $\rho_0$, $\rho_1$).
- $P$: probe $P_\eps$ (§1, §4) vs. path probability $P_\omega$ (§2.2, §3.2).
- $E$: score-correction vector $E_\omega$ \eqref{ray:eq:grad} vs. $E=\log(1/\eps)$ (§4) vs. error $\mathcal E$ \eqref{upper:eq:approx}.
- $D$: $D=d-a$ (§4.1) vs. $D_\omega$ \eqref{ray:eq:path} vs. $D_s$, $D_+$ (§4.2–4.3).
- $H$ (horizon) vs. $H_0$ (Lipschitz constant, §4.3); $K$ (Thm 3) vs. $K_R$ vs. $\mathcal K_i$.

**m2. §1.** "Since $r\le n$ and $n\ge3$, we have $0<\beta<1$" is asserted. One line suffices: $n^2(1+L^2)\ge 3n(1+L^2)>n(L+1)$ and $r^2\ge 2r$ for $r\ge2$.

**m3. Abstract writes $\alpha_L$; Theorem~\ref{thm:rate} and §4 write $\alpha$.** Unify.

**m4. §2.3.** "eventually", "at sufficiently late times" appear four times without naming a time. Introduce a single $T_1$ and say "for $t\ge T_1$".

**m5. §4.3.** "Choose a fixed, sufficiently small $\tau_0>0$ so that \eqref{eq:tracking} applies" — the only constraint is $\tau_0\le c$. "Sufficiently small" suggests a second, unstated requirement. State $\tau_0:=c$.

**m6. §4.2 paragraph order.** "Hence any finite $t^*$ is a probe zero. If $t^*=\infty$, … which the following time bound rules out. But \eqref{upper:eq:decrease} also gives…" reads as an afterthought. Move the $e^q$ time bound before the case analysis, conclude $t^*<\infty$, then eliminate the three non-probe alternatives.

**m7. §5.** All three secant slopes exceed the theorem exponent. Since the theorem forbids no such bias, one sentence noting that the finite-$\eps$ slope is expected to approach $\alpha$ from above (or simply that the direction is unexplained) would pre-empt a referee's suspicion. Numerics are correctly labelled as non-premises.

**m8. Constants' dependence chain in §3.3** ($R$ chosen from $P_0(1)$, then $A_R$, then $S_\eps$, then $c$) is non-circular but invites a circularity objection. One clause — "$P_0(1)$ does not depend on $R$" — removes it.

---

## (c) Theorem dependency and quantifier audit

Order of quantifiers, as actually used: $L\ge4$ fixed $\Rightarrow$ $n,r,u,M,x,\beta,\alpha,k,C_L,W$ determined $\Rightarrow$ $R$ fixed (§3.3, from $P_0(1)$, $\|v_*\|$) $\Rightarrow$ $C_R,K_R,A_R$ $\Rightarrow$ $c$, $\eps_0$ (Thm 3) $\Rightarrow$ $\delta<\tfrac12\min(A(W),D(W))$ (§4.1) $\Rightarrow$ Lemma 2 constant $C$ $\Rightarrow$ $R_0=nL/2$, margin \eqref{upper:eq:margin}, $\mathcal R_*$, $R_1$ $\Rightarrow$ $\tau_0=c$, $\mathcal K_0,\xi_*,\mathcal K_1,\mathcal K_2,H_0,\eta_\eps$ $\Rightarrow$ $C_0$ $\Rightarrow$ final $\eps_0$. **No circularity.** No constant is chosen using a quantity that depends on it.

Dependencies: Thm 1 $\leftarrow$ {Thm 3 (lower bound and, separately, §4.3's entrance), §4.2}. Thm 3 $\leftarrow$ {Thm 2 via \eqref{track:eq:logits}, Lemma 1, \eqref{track:eq:onesided}}. §4.2 $\leftarrow$ Lemma 2 $\leftarrow$ {§2.2 path combinatorics, $m_r>0$, $m_{n(L-1)}>0$}. §4.3 $\leftarrow$ {Thm 2, Thm 3, Lemma 2}. Thm 3 is used inside the upper bound only to place $y_\eps(t_0)$ in a fixed compact set — a *bounded*, not small, deviation. This is the one place where a reader may suspect circularity; it is not, because Thm 3's proof is independent of §4 and the bookkeeping $\alpha(1-\beta)=1$ makes $K\eps(1+\tau_0\eps^{-\alpha})^{1-\beta}\to K\tau_0^{1-\beta}=O(1)$. I verified this exponent cancellation.

Uniformity: all constants may depend on $L$ (declared in §6). No claim is uniform in $L$; none is used as such.

---

## (d) Scope of verification and uncertainty

**Independently re-derived and confirmed:** $n,r,u,M,\beta,\alpha$ and the three exponents $157/138$, $81/73$, $601/567$; $r=n$ (odd) / $r=n-1$ (even). §2.1 strict positivity of $\kappa_p$ via the first-passage/horizon-monotonicity bound (including $p=0$, where $p^-=p$). The cone $d=La$, $0\le b\le(L-1)a$, $h=(1+L^2)a$, $z_p\ge h$. The wall/parity bookkeeping $p_H=p_0+2L-2N+N_0\le L-1$, hence $N\ge n$ and $S\ge L+1-N$. The gap identity \eqref{ray:eq:gap}. **Both endpoint multiplicities:** odd $L$ forces $p_0=N_0=0$ and yields a unique path, $m_r=1$; even $L$ forces $N_0=1,p_0=0$ and yields $m_r=n$ — so $C_L$ is right in both parities; and $m_{n(L-1)}>0$ with both exhibited paths having length exactly $2L$ and never reaching $L$. §2.3's $b'\ge\frac r2F$, $a'\le HF$, $b\ge\frac r{2H}a-O(1)$, and $\gamma=\min(L^2-L+2,\,r/(4H))$. §2.4's convergent offset, including the substitution eliminating $a$ in favour of $\log t$ and $u\cdot w_\infty=\log(C_LM)$; consistency of $u$ with the exact cone $d=La$.

**§3:** $n\theta_1-\beta=[n(n-1)(L+1)-2r]/M>0$; monotonicity $\theta_c\ge\theta_1$, $\beta_c\ge\beta$; $\nabla^2\log P_\omega=-B_\omega$ and the semidefinite ordering \eqref{track:eq:hessian}; $\kappa=n(1+L^2)/M$ and $\int K_R<\infty$; the first-exit/continuity argument at $S_\eps$; the $t\le1$ concavity bound $(1+t)^{1-\beta}-1\le(1-\beta)t$; and the correct handling of $P_\eps(0)=0$ under $T_\eps=\inf\{t>0:P_\eps<0\}$ — the strict definition is used consistently and the $(0,1]$ argument genuinely covers the degenerate initial point.

**§4:** all region algebra, both signs of $b$ — $a+d=A+b$, $d=(A+D+b)/2$, $(L-2k)b+D$ (with $L-2k=0$ or $-1$), \eqref{upper:eq:bd}, $q=A+3b$; the identity $h-b=\tfrac12[(L+1)A+(L-1)D+(L-1)b]$; the $b<0$ pivot to the $S=n(L-1)$ endpoint via $z_{L-1,L}=h+(L-1)b$ (this is exactly why the sum is kept through $b=0$, and it works); $n(a+d)-q=(n-1)A+(n-3)b\ge2\delta E$ — **this is where $n\ge3$, i.e. $L\ge4$, is used**, and it is the sharp hypothesis; $-\nabla F=Fz$; the ratio identity \eqref{upper:eq:ratio} with $\|x\|^2=6$; the braces polynomial at $R=R_0$ and its exact minimum \eqref{upper:eq:margin} $=n^2(1+\tfrac{L^2}4-\tfrac L2)+n(L-1)-1>0$; $D_s/R_0\le 6-2/L$ and $(n+ks)/R_0\le 2k$ (the latter reducing to $k\ge1$); $A,D$ preservation because $x\cdot(1,-1,1)=x\cdot(-1,0,1)=0$; the $e^q$ time bound $\le L^2(L+1)e^{q(t_e)}/\eps=O(\eps^{-\alpha})$; **all four first-exit possibilities** at $t^*$; the logistic ratio ODE in $\xi$ and $\mathcal R_*>R_0$ as a corollary of \eqref{upper:eq:margin} at $s=r$; the exact identities $u\cdot W=\alpha$, $x\cdot W=\alpha-1$, $\eps^{-\alpha}Q(WE+y)=Be^{-x\cdot y}$; all three clock conversions $t\to\tau=\eps^\alpha t\to\xi$ and back via $d\tau/d\xi=e^{u\cdot y}/C_L$ bounded on $\mathcal K_2$.

**On "does a bound on the first zero give $\inf P<0$":** yes. At $t^*$ the region still holds ($P\ge0$ with equality is admissible in \eqref{upper:eq:region}) and $R>R_0$, so \eqref{upper:eq:decrease} gives $P'(t^*)\le-Q(t^*)/2<0$; hence $P<0$ immediately after, and $T_\eps\le t^*$. The degenerate "touches zero and returns" scenario is genuinely excluded.

**Not verified:** the MAIS-A8 conventions behind reference [1]; all numerics in §5 and Figure 1; the rendered layout; whether $\eps^\alpha T_\eps$ converges (correctly disclaimed).

---

## (e) Ordered edit plan

1. **§3.3** — expand the two-line derivation of $\Delta'\le K_R\Delta+\eps C_R(1+t)^{-\beta}$ (J2). Highest value per line added.
2. **Rename $F$ in \eqref{upper:eq:F}** to $\Phi$ and add one sentence: "$\Phi$ is a proxy for the $N=n$ part of $1-J_L$, not the failure probability $F$ of §2" (m1, first bullet).
3. **§4.3** — split the compactness paragraph into three labelled steps (J3), stating the reparametrisation, the uniform convergence on $\mathcal K_2$, and that \eqref{upper:eq:region} is automatic on $\mathcal K_2$.
4. **§2.1** — name the policy-gradient theorem and note that the occupancy derivatives telescope (J1).
5. **Notation pass** — resolve $R$, $P$, $E$, $D$, $H$ collisions (m1); unify $\alpha_L$/$\alpha$ (m3).
6. **§4.2** — reorder so the $e^q$ time bound precedes the $t^*$ case analysis (m6).
7. **Lemma 2** — cite Lemma~\ref{lem:path-score} in both branches (J4).
8. **Small clarifications** — m2, m4, m5, m7, m8.
9. **Optional, high value for a reader:** a four-line roadmap after Theorem 1 with the scales — $w_0\approx\frac uM\log t$; corrective drift $Q\sim\eps t^{-\beta}$; $q=x\cdot w\approx\beta\log t$; balance at $t\asymp\eps^{-\alpha}$ where $w\approx WE$ — and a one-line statement that $\alpha(1-\beta)=1$ is the arithmetic identity that makes the tracking bound $O(1)$ exactly at the entrance time. This single addition would do more for comprehension than any other change.
