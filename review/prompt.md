O87 extension | independent mathematical review | 2026-09-19 snapshot

You are an adversarial mathematical referee. Review the two complete proof drafts and the exploratory transition analysis below from scratch. Do not rely on author confidence or numerical evidence. No tools are enabled; inspect the supplied exact sources mathematically. Return a detailed report with: verdict per theorem; correctness risks; exact section/equation anchors; definitions/notation issues; proof weak points; ordered concrete fixes; and nonblocking polish. Separate genuine gaps from exposition. Re-derive the failed-path count, strict derivative signs, dominant-path multiplicities, gradient and Hessian signs, cone estimates, integrable error, and first-crossing bootstrap. Challenge the alpha exponent and examine whether the transition analysis could be completed or hides an obstruction. A valid lower bound is not a full correction-time asymptotic. The target is a local MAIS extension with no page limit; no public acceptance or formal verification should be inferred. Do not rewrite the paper or claim tests were executed. Give any possible upper-bound route explicitly as proved, conjectural, or incomplete.


===== output/pdf/MAIS-O87-zero-diversity-ray.tex =====
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}
\usepackage{lmodern,microtype}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newcommand{\R}{\mathbb R}
\title{The zero-diversity trajectory in the coin-line model}
\author{Rob Sneiderman}
\date{September 19, 2026}
\begin{document}
\maketitle
\begin{abstract}
For the linear coin-line policy trained only on a coin at the right endpoint,
we determine the gradient-flow trajectory from zero initialization up to a
convergent additive error. The leading direction is the score of the least
expensive failed action paths. An extra wall self-loop changes this direction
when the line length is even. This gives the logarithmic trajectory needed
for a small-diversity correction-time analysis; it does not determine the
correction time at positive diversity.
\end{abstract}

\section{Statement}
There are sites $0,\ldots,L$, with $L\ge4$. The coin is always at $L$.
The initial position is uniform on these $L+1$ sites. The agent succeeds
on reaching $L$, including at time zero; otherwise the episode ends after
$H=2L$ actions. Actions move one site left or right, clipped at the endpoints.
At site $p$, the probability of moving right is
\[
 \frac{1}{1+e^{-z_p}},\qquad z_p=a+bp+Ld.
\]
Let $J_0(w)$ be the success probability, where $w=(a,b,d)$. We study
Euclidean gradient ascent $w'=\nabla J_0(w)$ with $w(0)=0$.
These are the zero-diversity conventions of MAIS-A8, Definition 3.1 and
Section 6. Set
\[
 n=\left\lceil\frac{L+1}{2}\right\rceil,\qquad r=L+1-n,\qquad
 u=(n,r,nL),\qquad M=\|u\|^2,
\]
and define
\[
 C_L=\begin{cases}
 (L+1)^{-1},&L\text{ odd},\\
 n(L+1)^{-1},&L\text{ even}.
 \end{cases}
\]
\begin{theorem}\label{thm:ray}
There is a vector $w_\infty\in\R^3$ such that
\[
 w(t)=\frac{u}{M}\log t+w_\infty+o(1)
 \qquad(t\to\infty),
\]
with $u\cdot w_\infty=\log(C_LM)$. Moreover,
\[
 1-J_0(w(t))\sim\frac{1}{Mt},\qquad
 t\,w'(t)\longrightarrow\frac{u}{M}.
\]
\end{theorem}
The offset need not be parallel to $u$. The theorem concerns zero
initialization and zero diversity throughout.

\section{The cone containing the trajectory}
For the moment, regard the nonterminal logits as independent. Their
success derivatives $\kappa_p=\partial J_0/\partial z_p$ are strictly
positive. Here is a direct justification. Let $V_j(p)$ be the probability
of hitting $L$ within $j$ actions and let $\rho_i(p)$ be the probability
of occupying $p$ at time $i$ before stopping. Differentiating the finite
Bellman recursion gives
\[
 \kappa_p=\sigma(z_p)\sigma(-z_p)
 \sum_{i=0}^{H-1}\rho_i(p)
 [V_{H-i-1}(p+1)-V_{H-i-1}(\max(p-1,0))].
\]
Every bracket is nonnegative: from the farther site a path must first
hit the nearer site, and reducing the remaining horizon cannot improve
success. The bracket at $i=0$ is strictly positive. The nearer site can
reach $L$ within $H-1$ actions, while the farther site has positive
probability of avoiding the nearer site for the entire horizon. Since
$\rho_0(p)=1/(L+1)$, strict positivity follows.

The chain rule now gives
\[
 a'=\sum_{p<L}\kappa_p>0,\qquad
 b'=\sum_{p<L}p\kappa_p>0,\qquad d'=La'.
\]
Thus, along the trajectory,
\begin{equation}\label{eq:cone}
 d=La,\qquad 0\le b\le(L-1)a,\qquad
 h:=a+Ld=(1+L^2)a.
\end{equation}
In particular $h-b\ge(L^2-L+2)a$. The flow exists for all time because
its vector field is bounded and globally Lipschitz: the return is a
finite polynomial in logistic probabilities of linear forms.
Also $a(t)\to\infty$. Otherwise \eqref{eq:cone} and monotonicity would
make all coordinates converge to a finite point, at which $a'>0$.
Continuity would then contradict convergence of $a$.

\section{Failed paths and their scores}
Let $\Omega$ consist of all pairs of a nonterminal starting site and a
length-$H$ action sequence that never reaches $L$. For $\omega\in\Omega$,
let $N$ count its left actions, let $N_0$ count left actions taken at zero,
and let $S$ be the sum of the sites at which left actions are taken.
Write $p_j$ for its position before action $j$ and set
\[
 v_\omega=(N,S,LN),\qquad x_p=(1,p,L).
\]
Its conditional probability, given its starting site, is exactly
\begin{equation}\label{eq:path}
 P_\omega(w)=e^{-v_\omega\cdot w}D_\omega(w),\qquad
 D_\omega(w)=\prod_{j=0}^{H-1}(1+e^{-z_{p_j}})^{-1}.
\end{equation}
Consequently $F:=1-J_0=(L+1)^{-1}\sum_\omega P_\omega$ and
\begin{equation}\label{eq:grad}
 w'=\frac1{L+1}\sum_\omega P_\omega(v_\omega-E_\omega),
 \qquad E_\omega=\sum_{j=0}^{H-1}\sigma(-z_{p_j})x_{p_j}.
\end{equation}
On the cone \eqref{eq:cone}, $z_p\ge h$, so, uniformly over this finite
path set,
\begin{equation}\label{eq:errors}
 D_\omega=1+O(e^{-h}),\qquad
 \|E_\omega\|=O(e^{-h}),\qquad D_\omega\ge2^{-H}.
\end{equation}
All constants below may depend on $L$.

There are no clipped right actions on a failed path. Hence
\[
 p_H=p_0+2L-2N+N_0\le L-1.
\]
It follows that $N\ge n$ and
\[
 S\ge N-N_0\ge L+1+p_0-N\ge L+1-N.
\]
Since $n+r=L+1$, the score difference satisfies
\begin{equation}\label{eq:gap}
 (v_\omega-u)\cdot w
 =(N-n)(h-b)+(N+S-n-r)b\ge0.
\end{equation}
Both coefficients on the right are nonnegative integers.

The score $(N,S)=(n,r)$ is attained, and its multiplicity is explicit.
If $L$ is odd, $r=n$ and the endpoint inequality forces $p_0=N_0=0$.
All left actions must be taken at site one. The unique path consists of
$n$ right-left cycles from zero followed by right actions to site $L-1$.
If $L$ is even, $r=n-1$. The inequality $S\ge N-N_0$ forces $N_0\ge1$,
and the endpoint inequality forces $N_0=1$ and $p_0=0$. Every other left
action is at site one. There are $n$ paths: place the one left self-loop
in any of the $n$ slots before, between, or after the $n-1$ right-left
cycles, then finish with right actions. This proves the coefficient $C_L$
in the theorem.

\section{Separation of the dominant paths}
To use \eqref{eq:gap}, we must show that $b$ also diverges. Let $F_>$ be
the contribution to $F$ from paths with $N>n$. Each has a score gap at
least $h-b$. Comparing with one path of score $u$, using
\eqref{eq:path}--\eqref{eq:errors}, gives
\begin{equation}\label{eq:high}
 \frac{F_>}{F}=O(e^{-(h-b)})\longrightarrow0.
\end{equation}
For the remaining paths, $S\ge r$. The $b$ component of
\eqref{eq:grad}, together with $S\ge0$ on all paths, therefore gives
\[
 b'\ge r(F-F_>)-H(L-1)e^{-h}F\ge\frac r2 F
\]
for sufficiently large time. The $a$ component gives $0<a'\le HF$.
Thus $b'\ge(r/(2H))a'$ eventually. After integration,
\[
 b\ge\frac{r}{2H}a-O(1).
\]
In particular, $b\to\infty$ and $b\ge(r/(4H))a$ eventually.

For a path with $v_\omega\ne u$, at least one of the integer coefficients
in \eqref{eq:gap} is positive. The cone bound and the preceding estimate
therefore give a constant $\gamma>0$ such that its score gap is at least
$\gamma a$ at sufficiently late times. Summing the finite path set in
\eqref{eq:path} and \eqref{eq:grad}, and using \eqref{eq:errors}, yields
\begin{align}
 F&=C_Le^{-U}\bigl(1+O(e^{-\gamma a})\bigr),\label{eq:lossasym}\\
 w'&=C_Le^{-U}\bigl(u+O(e^{-\gamma a})\bigr),
 \qquad U=u\cdot w.\label{eq:flowasym}
\end{align}
Here and below $\gamma$ may be reduced to absorb the denominator errors.
The error in the second line is a vector error in Euclidean norm.

\section{Integrating the asymptotic flow}
Since $a'>0$ and $a\to\infty$, we may use $a$ as the independent variable.
Equation \eqref{eq:flowasym} gives
\[
 \frac{dw}{da}=\frac un+O(e^{-\gamma a}).
\]
The error is integrable. There is therefore a vector $v$ such that
\begin{equation}\label{eq:offset}
 w=\frac un a+v+O(e^{-\gamma a}).
\end{equation}
Taking the inner product of \eqref{eq:flowasym} with $u$ gives
\[
 \frac{d}{dt}e^U=C_LM\bigl(1+O(e^{-\gamma a})\bigr)
 \longrightarrow C_LM.
\]
It follows by integration that $e^U/t\to C_LM$, and hence
\[
 U=\log t+\log(C_LM)+o(1).
\]
Combining this with \eqref{eq:offset} proves
\[
 w=\frac uM\log t+
 \left[v+\frac uM\bigl(\log(C_LM)-u\cdot v\bigr)\right]+o(1).
\]
The bracket is $w_\infty$ and has the required inner product with $u$.
Finally, \eqref{eq:lossasym} and \eqref{eq:flowasym} give the return and
velocity limits in Theorem~\ref{thm:ray}.

\section{What this says about small positive diversity}
Evaluating the logit at $(p,c)=(2,1)$ along this zero-diversity trajectory
now gives a proved asymptotic:
\[
 a(t)+2b(t)+d(t)=\beta_L\log t+B_L+o(1),\qquad
 \beta_L=\frac{n(L+1)+2r}{n^2(1+L^2)+r^2}.
\]
In particular, the probability of moving left at that state is asymptotic
to $e^{-B_L}t^{-\beta_L}$. The balance
$\varepsilon t^{-\beta_L}\asymp t^{-1}$ suggests the correction-time
exponent $(1-\beta_L)^{-1}$. This last step remains a conjecture: it
requires estimates comparing the positive-diversity flow with the
zero-diversity flow over a growing time interval, followed by control of
the transition to a negative probe. No such comparison is asserted here.

\begin{thebibliography}{9}
\bibitem{a8} MAIS, \emph{A predictive theory of out-of-distribution
generalization: which of two perfect policies does gradient descent select?}
Research agenda MAIS-A8, Definition 3.1 and Section 6.
\href{https://github.com/lionellevine/MAIS/blob/7b23a8a30c0eb0b1d3b55c592ca9554256fc4805/agendas/A8/MAIS-A8.tex}{Source version 7b23a8a}.
\end{thebibliography}
\end{document}


===== output/pdf/MAIS-O87-correction-time-lower-bound.tex =====
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}
\usepackage{lmodern,microtype}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newcommand{\eps}{\varepsilon}
\newcommand{\R}{\mathbb R}
\title{A lower bound on policy-gradient correction time}
\author{Rob Sneiderman}
\date{September 19, 2026}
\begin{document}
\maketitle
\begin{abstract}
In the linear coin-line model, a small positive training diversity eventually
corrects the test-state verdict. We bound how long that correction takes
from zero initialization. The bound is a power of inverse diversity, with
an explicit exponent strictly greater than one. The proof compares the
perturbed flow with its zero-diversity logarithmic trajectory. An integrable
bound on the positive part of the return Hessian prevents error amplification
from changing the exponent. A matching upper bound remains open.
\end{abstract}

\section{Model and result}
Fix an integer $L\ge4$ and put $H=2L$. An agent moves on $0,\ldots,L$,
with actions clipped at the endpoints. The initial site is uniform, and
success means hitting a coin at $c$, including at time zero, within $H$
actions. At site $p$ the probability of moving right is
$\sigma(a+bp+dc)$, where $\sigma(z)=(1+e^{-z})^{-1}$ and $w=(a,b,d)$.
Let $J_c(w)$ be the conditional success probability for coin $c$. Define
\[
 J_\eps=(1-\eps)J_L+\frac\eps L\sum_{c=1}^LJ_c,\qquad
 w_\eps'=\nabla J_\eps(w_\eps),\qquad w_\eps(0)=0.
\]
Write $w_0$ for the flow at zero diversity. The test-state logit and its
first correction time are
\[
 P_\eps(t)=a_\eps(t)+k b_\eps(t),\qquad k=\lceil L/2\rceil,\qquad
 T_\eps=\inf\{t>0:P_\eps(t)<0\}.
\]
The infimum is $+\infty$ if the set is empty. Set
\[
 n=\lceil(L+1)/2\rceil,\quad r=L+1-n,\quad u=(n,r,nL),\quad M=\|u\|^2,
\]
\[
 \beta=\frac{n(L+1)+2r}{M},\qquad \alpha=\frac1{1-\beta}.
\]
Here $0<\beta<1$, so $\alpha>1$. Indeed, $r\le n$ and $n\ge3$ give
$M\ge n^2(1+L^2)>n(L+3)\ge n(L+1)+2r$.

The input from the companion note \cite{ray} is
\begin{equation}\label{eq:input}
 w_0(t)=\frac uM\log t+v+o(1),\qquad
 1-J_L(w_0(t))\sim\frac1{Mt}.
\end{equation}
That note also proves $d_0=La_0$, $a_0'>0$, and $b_0'>0$.
No positive-diversity tracking estimate is assumed.

\begin{theorem}\label{thm:tracking}
There are constants $A_L,c_L,\eps_L>0$ such that, for
$0<\eps\le\eps_L$ and $0\le t\le c_L\eps^{-\alpha}$,
\[
 \|w_\eps(t)-w_0(t)\|
 \le A_L\eps\bigl((1+t)^{1-\beta}-1\bigr).
\]
The constants can be chosen so that $P_\eps(t)>0$ throughout
$0<t\le c_L\eps^{-\alpha}$. In particular,
\[
 T_\eps\ge c_L\eps^{-\alpha},\qquad
 \liminf_{\eps\downarrow0}\frac{\log T_\eps}{\log(1/\eps)}\ge\alpha.
\]
\end{theorem}
For $L=4,5,6$, the exponents are respectively $157/138$, $81/73$, and
$601/567$. This is a bound for the exact Euclidean return-gradient flow
from zero initialization, not a statement about discrete or sampled updates.

\section{The diversity perturbation}
Write
\[
 \nabla J_\eps=\nabla J_L+\eps G,\qquad
 G=\frac1L\sum_{c=1}^L\nabla J_c-\nabla J_L.
\]
Fix a radius $R>0$. All estimates in this section are uniform for
$\|w-w_0(t)\|\le R$, with constants allowed to depend on $L,R$.
By \eqref{eq:input} and boundedness on finite time intervals,
\begin{equation}\label{eq:logits}
 z_{pc}(w)=\frac{n+pr+cnL}{M}\log(1+t)+O_R(1)
 \quad(0\le p\le L,\ 1\le c\le L).
\end{equation}
Define
\[
 \theta_c=\frac{n+cnL}{M},\qquad
 \beta_c=\frac{n+(c+1)r+cnL}{M}.
\]
Thus $\theta_c\ge\theta_1$ and $\beta_c\ge\beta_1=\beta$.

We use finite sums of action-path probabilities. The score vector of
one action is either $\sigma(-z_{pc})(1,p,c)$ or
$-\sigma(z_{pc})(1,p,c)$. A path of at most $H$ actions therefore has
score norm at most $H\sqrt{1+2L^2}$. Consequently, a bound on the probability
of every path in a fixed finite event also bounds the gradient of that
event's probability, up to a constant depending only on $L$.

For a start below $c$, differentiate failure rather than success. Every
failed path stays below $c$. If it has $N_-$ left actions, clipping at zero
gives $p_H\ge p_0+2L-2N_-$. Since $p_H\le c-1$,
\[
 N_-\ge\left\lceil\frac{2L+p_0-c+1}{2}\right\rceil\ge n.
\]
By \eqref{eq:logits}, each left-action probability below $c$ is at most
$C_R(1+t)^{-\theta_c}$. The failed-path probability and its summed gradient
are therefore $O_R((1+t)^{-n\theta_c})$.

For a start above $c$, differentiate success. Every successful path includes
a left action from $c+1$. Its probability is at most
$C_R(1+t)^{-\beta_c}$ by \eqref{eq:logits}; all other action factors are
at most one. Summing the finite set of stopped successful paths gives a
gradient bound $O_R((1+t)^{-\beta_c})$. There is no such starting site
when $c=L$, and a start at $c$ has zero derivative.

Finally,
\[
 n\theta_1-\beta
 =\frac{n(n-1)(L+1)-2r}{M}>0.
\]
Both parts of every conditional-return gradient are thus bounded by
$C_R(1+t)^{-\beta}$. We have proved
\begin{equation}\label{eq:Gbound}
 \|G(w)\|\le C_R(1+t)^{-\beta}.
\end{equation}

\section{An integrable one-sided Hessian bound}
A norm bound on the entire Hessian would discard the sign of its leading
term. We retain that sign using the failed-path representation for coin $L$.
For each failed path $\omega$, let $P_\omega$ be its conditional probability
given its starting site, and put $g_\omega=\nabla\log P_\omega$. Then
\[
 \nabla^2\log P_\omega=-B_\omega,\qquad
 B_\omega=\sum_{j}\sigma(z_{p_j,L})\sigma(-z_{p_j,L})
 x_{p_j,L}x_{p_j,L}^{\mathsf T},
\]
where $x_{p,L}=(1,p,L)$ and the sum has $H$ terms. Since
$1-J_L=(L+1)^{-1}\sum_\omega P_\omega$,
\begin{equation}\label{eq:hessian}
 \nabla^2 J_L
 =\frac1{L+1}\sum_\omega P_\omega
 (B_\omega-g_\omega g_\omega^{\mathsf T})
 \preceq\frac1{L+1}\sum_\omega P_\omega B_\omega.
\end{equation}
The ordering is that of symmetric quadratic forms.

Set $\kappa=n(1+L^2)/M>0$. Equation \eqref{eq:logits} gives
$z_{p,L}\ge\kappa\log(1+t)-C_R$, and hence
$B_\omega\preceq C_R(1+t)^{-\kappa}I$.
Also the bound on path scores gives
\[
 P_\omega(w)\le
 e^{RH\sqrt{1+2L^2}}P_\omega(w_0(t)).
\]
Summing and using \eqref{eq:input}, we obtain
$1-J_L(w)\le C_R(1+t)^{-1}$.
It follows from \eqref{eq:hessian} that
\begin{equation}\label{eq:onesided}
 \nabla^2J_L(w)\preceq K_R(t)I,\qquad
 K_R(t)=C_R(1+t)^{-1-\kappa},\qquad
 \int_0^\infty K_R(t)\,dt<\infty.
\end{equation}
These bounds hold for all $t\ge0$ after increasing the constants on a
compact initial interval. In particular, no assumption about the perturbed
trajectory remaining in the zero-diversity invariant cone is needed.

\section{Tracking and the first crossing}
Let $D(t)=\|w_\eps(t)-w_0(t)\|$ and stop the comparison if $D$ first
reaches $R$. The line segment between the two parameters lies in the same
radius-$R$ ball. Integrating \eqref{eq:onesided} along that segment and
using \eqref{eq:Gbound} gives, while $D<R$,
\[
 D'\le K_R(t)D+\eps C_R(1+t)^{-\beta}.
\]
At $D=0$ this is understood as an upper right derivative; equivalently,
one may regularize the norm. Gr\"onwall's inequality and integrability of
$K_R$ yield a finite constant $A_R$ such that
\begin{equation}\label{eq:tracking}
 D(t)\le A_R\eps\bigl((1+t)^{1-\beta}-1\bigr).
\end{equation}
Consider
\[
 S_\eps=\left(1+\frac{R}{2A_R\eps}\right)^{1/(1-\beta)}-1.
\]
If the first exit occurred at or before $S_\eps$, continuity and
\eqref{eq:tracking} would imply $R\le R/2$. Thus there is no exit, and
\eqref{eq:tracking} holds through $S_\eps$. Moreover
\[
 S_\eps\sim\left(\frac{R}{2A_R}\right)^\alpha\eps^{-\alpha}.
\]

To ensure a positive probe, put $v_*=(1,k,0)$. Since $a_0',b_0'>0$,
$P_0$ is strictly increasing from zero. Choose
\[
 0<R\le\min\left\{1,\frac{P_0(1)}{2\|v_*\|}\right\}.
\]
For $1\le t\le S_\eps$, the tracking bound $D\le R/2$ gives
$P_\eps(t)\ge P_0(1)-\|v_*\|R/2>0$.
On $0\le t\le1$, let $m=\min_{[0,1]}P_0'>0$.
Concavity of $(1+t)^{1-\beta}$ implies
$D(t)\le A_R\eps(1-\beta)t$, so
\[
 P_\eps(t)\ge
 \bigl(m-\|v_*\|A_R\eps(1-\beta)\bigr)t>0\qquad(0<t\le1)
\]
for sufficiently small $\eps$. Reduce $\eps_L$ so that $S_\eps\ge1$,
and choose $c_L>0$ with $c_L\eps^{-\alpha}\le S_\eps$ throughout the
remaining range. Equation \eqref{eq:tracking} and these positivity bounds
prove Theorem~\ref{thm:tracking}.

\section{What remains}
The theorem implies $\eps T_\eps\to\infty$. Thus an inverse-diversity
correction-time bound would be too short in this model, provided the
zero-diversity asymptotic \eqref{eq:input} holds as proved in the companion
note. It also gives uniform convergence $w_\eps-w_0\to0$ on
$0\le t\le\eps^{-\alpha+\eta}$ for each fixed $0<\eta<\alpha$.

The argument stops when the parameter displacement is of constant size.
It does not follow the later transition or prove
$T_\eps\le\eps^{-\alpha+o(1)}$. Establishing that matching upper bound
is the remaining correction-time problem.

\begin{thebibliography}{9}
\bibitem{ray} R. Sneiderman, \emph{The zero-diversity trajectory in the
coin-line model}, local proof draft, September 19, 2026, Theorem 1.
\bibitem{a8} MAIS, \emph{A predictive theory of out-of-distribution
generalization: which of two perfect policies does gradient descent select?}
Research agenda MAIS-A8, Definition 3.1 and Section 6.
\href{https://github.com/lionellevine/MAIS/blob/7b23a8a30c0eb0b1d3b55c592ca9554256fc4805/agendas/A8/MAIS-A8.tex}{Source version 7b23a8a}.
\end{thebibliography}
\end{document}


===== TRANSITION_ANALYSIS.md =====
# Transition analysis for the correction-time upper bound

2026-09-19. Status: exact local calculations and a solved reduced ODE;
matching upper bound for the full flow remains OPEN. Nothing posted.
These calculations and the preceding theorem drafts have not been independently
reviewed. The old O87 audit does not cover them.

## What changed

The one-vector transition approximation cannot simply be continued until the
probe crosses. The dominant zero-diversity failed-path score switches when b
changes sign. This is a concrete missing step, not a numerical solver issue.
There are two exact score vectors, one on either side of that switch.

## 1. Local limiting vector field near the critical scale

Retain n,r,u,M,beta,alpha from the preceding notes. Set

    x=(1,2,1), C=C_L, B=1/[L(L+1)], E=log(1/epsilon),
    W=alpha u/M, t=epsilon^(-alpha) tau, w=W E+y.

For y in any fixed compact subset of R^3, the rescaled vector field satisfies

    epsilon^(-alpha) grad J_epsilon(W E+y)
      -> C u exp(-u.y) - B x exp(-x.y),

uniformly as epsilon -> 0. This is a vector-field limit, not yet a convergence
theorem for the full trajectories and not an estimate for y of order E.

Proof of the local limit:

- u.W=alpha and x.W=alpha beta=alpha-1.
- All competing zero-diversity failed-path scores have strictly larger
  products with W, by the positive-b score-gap formula in the ray note.
  Logistic denominators tend uniformly to one. The surviving contribution
  is C u exp(-u.y).
- For coin 1 and starts above it, the unique successful path with least
  score is: start at p=2, take left immediately, stop. Its probability is
  exp(-x.w)(1+o(1)), and its gradient is -x exp(-x.w)(1+o(1)). Any other
  successful path from above requires at least one additional left action,
  whose product with W is strictly positive. Averaging the starting site
  and coin law gives B=1/[L(L+1)].
- All other above-coin successes have strictly larger exponents beta_c>beta.
  All below-coin failures have exponents at least n theta_1>beta, as in the
  tracking note. The diversity correction to the coin-L weight also vanishes.
- There are finitely many paths, so these strict gaps also control the
  differentiated sums, uniformly on compact y sets.

The natural entrance condition would be

    y(tau) = (u/M) log(tau) + v + o(1),  tau -> 0,

where v is the offset from the zero-diversity ray theorem. Selection of this
singular entrance solution by the full trajectories still needs a written
argument; the existing tracking estimate supplies a possible starting point.

## 2. The reduced ODE has finite-time escape

Consider the reduced equation y'=C u e^(-U)-B x e^(-q), with
U=u.y, q=x.y, M=u.u, D=u.x, X=x.x=6. Introduce the positive ratio

    R=(B/C) exp(U-q)

and the clock ds/dtau=C exp(-U). Then exactly

    dy/ds = u-Rx,
    dR/ds = R[(M-D)-(D-X)R].

For L>=4, M>D>X and D^2<MX. The last inequality is strict Cauchy-Schwarz,
since u and x are not parallel. Thus the logistic ratio converges to

    R*=(M-D)/(D-X)>0.

Moreover

    dU/ds -> M-D R* = -(MX-D^2)/(D-X) = -kappa < 0.

The logistic convergence is exponential, so U(s)=-kappa s+O(1) and
integrating d tau/ds=exp(U)/C gives a finite terminal time tau*. Hence

    U,q -> -infinity as tau -> tau*,
    y(tau)=V log(tau*-tau)+O(1),
    V=(u-R*x)/(M-D R*),
    u.V=x.V=1.

These assertions hold for any finite starting y, with its own tau*. They
are statements about the reduced ODE, not about a blow-up of the actual
parameter flow (whose vector field is globally bounded).

## 3. The dominant score changes at b=0

For b<0 and h+(L-1)b>0, let

    u_minus=n(1,L-1,L).

Every failed path for coin L satisfies N>=n and S<=N(L-1). Therefore

    Nh+Sb - n[h+(L-1)b]
      = (N-n)[h+(L-1)b] + [S-N(L-1)]b >= 0.

The score (N,S)=(n,n(L-1)) is attained: climb to L-1 and take every left
action there, returning right between successive left actions. Finish with
a right action if a step remains. For odd L only start p0=0 is possible,
and there is one path. For even L starts p0=0 and p0=1 are possible, giving
two paths. To see exhaustiveness, N0=0 on these paths and the endpoint
identity forces p0<=2n-L-1 (zero for odd L and one for even L); all remaining
actions are determined by the requirement that every left action occur at
L-1 and that the path never reach L.

Thus the leading coefficients on this side are 1/(L+1) for odd L and
2/(L+1) for even L. Separation of all other scores follows if both -b and
h+(L-1)b tend to infinity. At b=O(1), however, all N=n score classes can
contribute; neither extreme-score approximation is uniformly valid there.

Exact dynamic enumeration confirms both attainment and multiplicity for
L=4,...,12. That is a check of the general combinatorial argument, not its
replacement.

## 4. What the numerical comparison says

The initial reduced model reaches q=-12 at approximately these rescaled
times. The initialization uses the offset estimated at log(1+t)=600 and
starts at tau=1e-7, so these are approximate diagnostic values, not a certified
limiting prefactor.

| L | Reduced time to q=-12 | epsilon^alpha T at epsilon=1e-96 |
|---|---:|---:|
| 4 | 47.872 | 46.828 |
| 5 | 47.268 | 46.154 |
| 6 | 68.965 | 59.167 |

The L=6 zero-ray offset converges more slowly; no precision claim is made for
its reduced time. The discrepancy is not evidence of a contradiction.

Extrapolating the reduced escape direction to displacements of order E
predicts b=0 before P=0 for L=4,5,6. That extrapolation is outside the proved
compact-y limit. A second formal segment using u_minus gives the following
candidate scaled crossing parameters; it is only a heuristic consistency check.

| L | Predicted (a,b,d)/E | Observed at epsilon=1e-96 |
|---|---|---|
| 4 | (0.011616, -0.005808, 0.092493) | (0.011413, -0.005707, 0.094494) |
| 5 | (0.005934, -0.001978, 0.071994) | (0.005113, -0.001704, 0.073906) |
| 6 | (0.003474, -0.001158, 0.043931) | (0.002671, -0.000890, 0.045658) |

Reproduce using `OPENBLAS_NUM_THREADS=1 python3 transition_model.py`.
The script refuses to overwrite its receipt:
results/transition-model-two-phase-20260919.json.
The original single-phase diagnostic receipt is also retained.

## 5. Exact remaining obligation

The lower bound remains intact. To close the matching upper exponent, prove
that after an appropriate critical-scale entrance, the full flow crosses
b=0 and then P=0 within epsilon^(-alpha-o(1)) additional physical time.
The estimates must cover an O(E) displacement, the b=O(1) layer with multiple
failed-path scores, and possible contributions from the other coin positions.

Finite escape time of the reduced ODE is insufficient: the local vector-field
approximation fails precisely as y becomes unbounded. A valid proof needs
uniform region estimates through both score regimes. Do not promote the
numerical prefactor or two-segment path to a theorem.
