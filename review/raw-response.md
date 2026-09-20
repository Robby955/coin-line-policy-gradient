# Adversarial Referee Report

**Objects reviewed (2026-09-19 snapshot, source text only):**

- **[R]** `output/pdf/MAIS-O87-zero-diversity-ray.tex` — "The zero-diversity trajectory in the coin-line model", Theorem 1.
- **[

**LB]** `output/pdf/MAIS-O87-correction-time-lower-bound.tex` — "A lower bound on policy-gradient correction time", Theorem 1 (`thm:tracking`).
- **[T]** `TRANSITION_ANALYSIS.md` — exploratory, self-declared open.

**Method note.** No tools were enabled and nothing was executed. Everything below is hand re-derivation from the supplied LaTeX/Markdown. I cannot verify the "Observed at epsilon=1e-96" columns, `transition_model.py`, or the JSON receipt; those are treated as unverifiable assertions throughout.

---

## 1. Verdicts

| Object | Verdict |
|---|---|
| **[R] Theorem 1** (ray asymptotic) | **Correct as stated**, conditional on two fixable proof-text gaps (§2 strict positivity; §3 exhaustiveness of the minimal-score enumeration). Every displayed identity and estimate re-derives. No correctness risk to the *statement* was found. |
| **[R] §6** (the $\beta_L$ / $(1-\beta_L)^{-1}$ discussion) | **Correctly labelled conjecture.** The one proved sentence ($a+2b+d=\beta_L\log t+B_L+o(1)$) is right. |
| **[LB] Theorem 1** (`thm:tracking`) | **Correct.** The bootstrap, the one-sided Hessian bound, the Grönwall step and the two-regime probe argument all close. Independent of [R]'s $C_L$ (see §3.7), so the one [R] gap that could touch a constant does not propagate. |
| **[LB] abstract, sentence 2** ("a small positive training diversity eventually corrects the test-state verdict") | **Unproven claim.** $T_\eps<\infty$ is established nowhere in either document. Must be softened. |
| **[T] §1** (vector-field limit on compact $y$) | **Correct** as a vector-field limit; correctly disclaimed as not a trajectory theorem. |
| **[T] §2** (reduced ODE) | **Correct.** Logistic reduction, $R^\ast$, $-\kappa$, $V$, $u\cdot V=x\cdot V=1$, finite $\tau^\ast$ all re-derive exactly. |
| **[T] §3** ($b<0$ score switch, $u_-$, multiplicities 1/2) | **Correct**, with the same style of thin exhaustiveness argument as [R] §3. |
| **[T] §4–§5** | Honest. The table in §4 is *internally exact* (I re-derived all three rows, §5.3 below); it is not evidence for the model. |
| **Overall package claim** | A **valid lower bound only**. $T_\eps=\eps^{-\alpha+o(1)}$ is **not** established, and the documents mostly say so. |

---

## 2. Re-derivation checklist (requested items)

### 2.1 Failed-path count — **agrees**

$\Omega$ = (nonterminal start $p_0\in\{0,\dots,L-1\}$, length-$H$ action word never reaching $L$). Finite, $|\Omega|\le L\,2^{2L}$; all "constants depend on $L$" claims are therefore legitimate. On a failed path the walk stays in $\{0,\dots,L-1\}$, so **no right-clipping occurs** ([R] §3) — correct, and it is robust to whether $L$ is absorbing or merely "ever-hit" success.

Endpoint identity: with $N$ = lefts, $N_0$ = lefts at site $0$,
$$p_H=p_0+(H-N)-(N-N_0)=p_0+2L-2N+N_0\le L-1 .$$
Hence $2N-N_0\ge L+1+p_0$, giving $N\ge\lceil (L+1)/2\rceil=n$ and, with $S\ge N-N_0$,
$$S\ \ge\ N-N_0\ \ge\ L+1+p_0-N\ \ge\ L+1-N,\qquad N+S\ge n+r .$$
All three inequalities in [R] §3 verified.

### 2.2 Strict derivative signs — **agrees, but the printed justification does not close**

The occupancy formula
$$\kappa_p=\sigma(z_p)\sigma(-z_p)\sum_{i=0}^{H-1}\rho_i(p)\bigl[V_{H-i-1}(p+1)-V_{H-i-1}(\max(p-1,0))\bigr]$$
is the correct differentiated Bellman recursion (including the $p=0$ self-loop case, where the bracket is $V_j(1)-V_j(0)$).

Nonnegativity is fine. **Strictness at $i=0$ is asserted from two facts that do not imply it.** [R] §2 states (a) $V_{H-1}(p+1)>0$ and (b) $\Pr_{q}[\text{avoid }p+1\text{ for the horizon}]>0$, where $q=\max(p-1,0)$. These two facts alone do not give $V_{H-1}(p+1)>V_{H-1}(q)$. The missing step is the first-passage decomposition
$$V_j(q)=\sum_{\tau\ge1}\Pr_q[\tau_{p+1}=\tau]\,V_{j-\tau}(p+1)\ \le\ \Pr_q[\tau_{p+1}\le j]\;V_{j-1}(p+1)\ \le\ \Pr_q[\tau_{p+1}\le j]\;V_j(p+1),$$
using monotonicity of $V_j(p+1)$ in $j$. With $j=H-1$, (a) and (b) then do give strictness. **This is a one-line fix, not a defect in the claim**, but as printed the argument is a non-sequitur and a referee is entitled to call it a gap.

Consequences re-derived: $a'=\sum_{p<L}\kappa_p>0$, $b'=\sum_{p<L}p\,\kappa_p>0$ (needs some $p\ge1$, i.e. $L\ge2$), $d'=La'$.

### 2.3 Cone estimates — **agrees**

From $d'=La'$ and $w(0)=0$: $d=La$ exactly. From $b'\le(L-1)a'$: $0\le b\le(L-1)a$. Then
$$h:=a+Ld=(1+L^2)a,\qquad z_p=h+bp\ge h,\qquad h-b\ge(L^2-L+2)a .$$
All of `eq:cone` verified. `eq:errors` verified: $z_p\ge h\ge0\Rightarrow D_\omega\ge2^{-H}$, $D_\omega=1+O(e^{-h})$, $\|E_\omega\|=O(e^{-h})$.

$a(t)\to\infty$: correct (monotone $a$, monotone $b$, $d=La$ ⟹ $w$ converges ⟹ $a'\to a'(w_\infty)>0$, contradiction). **Global existence is asserted via "bounded and globally Lipschitz" without proof**; boundedness of $\nabla J_0$ plus local Lipschitzness already suffices and is the cleaner statement.

### 2.4 Score gap — **agrees (an identity)**

$v_\omega\cdot w=Nh+Sb$, $u\cdot w=nh+rb$, and
$$(v_\omega-u)\cdot w=(N-n)h+(S-r)b=(N-n)(h-b)+(N+S-n-r)b$$
is an algebraic identity; both coefficients are nonnegative **integers** by §2.1, and $h-b\ge0$, $b\ge0$ on the cone. `eq:gap` verified.

### 2.5 Dominant-path multiplicities — **agrees**

*Odd $L$* ($r=n$): $2n-N_0\ge L+1+p_0=2n+p_0\Rightarrow N_0=p_0=0$; then $S=n$ with $n$ lefts at sites $\ge1$ forces every left at site $1$. Unique path: $n$ right–left cycles from $0$, then $2L-2n=L-1$ rights, terminating at $L-1$. **Multiplicity 1**, $C_L=1/(L+1)$.

*Even $L$* ($r=n-1$): $S\ge N-N_0$ forces $N_0\ge1$; endpoint forces $N_0+p_0\le1$, hence $N_0=1$, $p_0=0$; remaining $n-1$ lefts all at site 1. Interleavings of one wall self-loop with $n-1$ "RL" cycles: **$n$ arrangements**, $C_L=n/(L+1)$. Checked explicitly at $L=4$ ($n=3$, three words, then $L-1=3$ rights, $N=3$, $S=2=r$).

**But the exhaustiveness step is not written.** Both cases silently use: *once the walk is at site $\ge2$ it can never take another left (all lefts are at $\le1$), hence all lefts precede a final monotone right-run.* Without it, "the unique path consists of…" and "There are $n$ paths" are assertions. Same remark applies verbatim to [T] §3 ("all remaining actions are determined by…").

I confirmed no minimal-score path can place a left at site $\ge2$: that would force $S\ge n+1>r$ (odd) or $S\ge n>n-1=r$ (even).

### 2.6 Gradient sign / structure — **agrees**

$P_\omega=e^{-v_\omega\cdot w}D_\omega$ with $v_\omega=(N,S,LN)$ is exact (`eq:path`); $\nabla\log P_\omega=-v_\omega+E_\omega$, $E_\omega=\sum_j\sigma(-z_{p_j})x_{p_j}$; hence
$$w'=\nabla J_0=\tfrac1{L+1}\textstyle\sum_\omega P_\omega(v_\omega-E_\omega)\quad(\texttt{eq:grad}).$$
Separation (§4): $F_>/F=O(e^{-(h-b)})\to0$; $b'\ge r(F-F_>)-H(L-1)e^{-h}F\ge \tfrac r2F$; $0<a'\le HF$; so $b'\ge\frac{r}{2H}a'$, $b\ge\frac{r}{2H}a-O(1)$, $b\ge\frac{r}{4H}a$ eventually. Then for $v_\omega\ne u$ the gap is $\ge\gamma a$ with $\gamma=\min\{L^2-L+2,\;r/(4H)\}$, and $\gamma\le 1+L^2$ absorbs the $e^{-h}$ denominator errors. `eq:lossasym`, `eq:flowasym` verified.

Integration (§5): $dw/da=u/n+O(e^{-\gamma a})$ (integrable), $\frac{d}{dt}e^U=C_LM(1+O(e^{-\gamma a}))\to C_LM$, so $e^U/t\to C_LM$ by L'Hôpital — **note this does not need the error to be $t$-integrable**, which is why the step is legitimate. Eliminating $a$ gives exactly the displayed $w_\infty$, and
$$u\cdot w_\infty=u\cdot v+\tfrac{\|u\|^2}{M}\bigl(\log(C_LM)-u\cdot v\bigr)=\log(C_LM).\ \checkmark$$
$1-J_0\sim 1/(Mt)$ and $tw'\to u/M$ follow. **Note $C_L$ cancels out of both.**

### 2.7 Hessian sign — **agrees; this is the load-bearing idea and it is sound**

$\nabla^2\log P_\omega=\nabla^2\log D_\omega=-B_\omega$ with $B_\omega=\sum_j\sigma(z)\sigma(-z)xx^{\mathsf T}\succeq0$; hence
$$\nabla^2J_L=\tfrac1{L+1}\sum_\omega P_\omega\bigl(B_\omega-g_\omega g_\omega^{\mathsf T}\bigr)\preceq \tfrac1{L+1}\sum_\omega P_\omega B_\omega .\ (\texttt{eq:hessian})$$
Verified. The point is quantitative and correct: $\|\nabla^2 J_L\|$ is only $O(t^{-1})$ (from the discarded $-g g^{\mathsf T}$, which is $O(1)$ per path), and $\int^\infty t^{-1}=\infty$ would produce a **polynomial** Grönwall amplification $t^{C}$ and destroy the exponent. Keeping the sign buys the extra factor $\sigma(z)\sigma(-z)\le e^{-z}\le C_R(1+t)^{-\kappa}$, $\kappa=n(1+L^2)/M>0$.

### 2.8 Integrable error — **agrees**

$\kappa=n(1+L^2)/M\in(0,1/n)$; e.g. $L=4$: $\kappa=51/157\approx0.325$. With $1-J_L(w)\le e^{RH\sqrt{1+2L^2}}\,(1-J_L(w_0(t)))\le C_R(1+t)^{-1}$,
$$\nabla^2J_L(w)\preceq K_R(t)I,\quad K_R(t)=C_R(1+t)^{-1-\kappa},\quad \int_0^\infty K_R=C_R/\kappa<\infty.\ (\texttt{eq:onesided})$$
The "increase the constants on a compact initial interval" remark is legitimate because $\nabla^2J_L$ is globally bounded.

### 2.9 First-crossing bootstrap — **agrees, no circularity**

$D'\le K_R(t)D+\eps C_R(1+t)^{-\beta}$ follows from $\langle\delta,\nabla J_L(w_0+\delta)-\nabla J_L(w_0)\rangle=\int_0^1\delta^{\mathsf T}\nabla^2J_L(w_0+s\delta)\delta\,ds\le K_R\|\delta\|^2$, the segment lying in the same ball. Grönwall gives `eq:tracking` with $A_R=e^{\|K_R\|_1}C_R/(1-\beta)$.

$S_\eps=(1+\tfrac{R}{2A_R\eps})^{1/(1-\beta)}-1$ satisfies $A_R\eps[(1+S_\eps)^{1-\beta}-1]=R/2$ exactly, so a first exit at $\tau\le S_\eps$ gives $R=D(\tau)\le R/2$. Standard and valid. $S_\eps\sim(R/2A_R)^\alpha\eps^{-\alpha}$.

**Order-of-quantifiers check (the place circularity usually hides):** $R$ is chosen from $\min\{1,P_0(1)/(2\|v_*\|)\}$, which depends only on $L$; **then** $C_R,K_R,A_R$; **then** $S_\eps,\eps_L,c_L$. No loop. ✔

Probe positivity: on $[1,S_\eps]$, $P_\eps\ge P_0(1)-\|v_*\|R/2\ge \tfrac34P_0(1)>0$; on $(0,1]$, concavity of $(1+t)^{1-\beta}$ gives $D\le A_R\eps(1-\beta)t$ and $P_\eps\ge(m-\|v_*\|A_R\eps(1-\beta))t>0$. The $t\downarrow0$ endpoint (where $P_\eps(0)=0$) is handled correctly — a common place to slip, handled here.

Also verified: the §5 remark $w_\eps-w_0\to0$ uniformly on $[0,\eps^{-\alpha+\eta}]$, since $(\alpha-\eta)(1-\beta)=1-\eta(1-\beta)$ gives $D\le A\eps^{\eta(1-\beta)}$.

---

*(Continues: §3 the $\alpha$ exponent; §4 genuine gaps vs exposition; §5 transition analysis and independent re-derivation of the crossing table; §6 upper-bound routes; §7 ordered fixes; §8 polish.)*