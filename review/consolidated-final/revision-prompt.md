coin-line-rates | local preprint | consolidated revision

Review the exact revised manuscript below against your complete initial audit. Confirm J1-J4 are now explicit and correct, and check that the notation changes and added explanations introduce no mathematical error. This is the complete source, not isolated excerpts. Pay special attention to the stopped Bellman recursion, the signed Hessian estimate, the first-exit reordering, and the division by g in the clock change.

Changes: F remains the exact zero-diversity failure probability in Section 2; Phi is the finite exponential proxy in Section 4. The physical ratio is varrho, the limiting ratio stays mathcal R. D_s,D_+ became chi_s,chi_+; H_0 became ell_0. Other indexed path quantities retain their locally defined names. Alpha=alpha_L is explicit. R is selected from the unperturbed probe before the tracking comparison. tau0=c/2 is fixed. K0 is selected before the common xi_* and reused in the bootstrap. Lemma 1 is cited when path probability bounds become gradient bounds. Added the exponent-balance explanation and endpoint-switch explanation. The finite-time upper bound now precedes exclusion of the non-probe exit boundaries. Numerical slope direction is described only as an observation. No further theorem or assumption is added.

The main edit deliberately uses dy/dxi=f_epsilon/g, since dxi/dtau=g>0. Your J3 prose had both multiplication and division language; please verify the division in the revised equations directly.

For the optional suggestion to name a single T1 in Section 2.3, the existing eventual estimates were retained: each is a fixed-L late-time bound, with no epsilon-uniform claim at issue. Give your final verdict and any residual blocking or nonblocking issues, with exact anchors. Please limit the response to 1200 words. Do not assess numerical runs or PDF rendering; those are checked separately by the editing session.

COMPLETE REVISED SOURCE

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}\usepackage{lmodern,microtype,graphicx,booktabs}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}\newtheorem{lemma}{Lemma}
\newcommand{\eps}{\varepsilon}\newcommand{\R}{\mathbb R}
\title{Correction times for linear policy gradient on a coin line}
\author{Rob Sneiderman}\date{September 19, 2026}
\begin{document}\maketitle
\begin{abstract}
How long does a rare corrective training signal take to overturn a learned
preference for moving right? We answer this question for a linear logistic
policy on a finite coin line. From zero initialization, the first correction
time under exact return-gradient flow is of order $\varepsilon^{-\alpha_L}$,
where $\varepsilon$ is the training diversity and the explicit exponent
$\alpha_L>1$ depends on the line length and its parity. We first determine
the zero-diversity trajectory up to a convergent offset. We then prove a
perturbation bound up to the critical timescale and control the subsequent
transition through the change of dominant failed paths. Numerical experiments
illustrate the asymptotics; they are not used in the proofs.
\end{abstract}

\section{Model and results}
An agent moves on sites $0,\ldots,L$, where $L\ge4$, and succeeds on reaching
a coin. The initial site is uniform. Each episode stops on its first success,
including at time zero, or after $H=2L$ actions. Actions move one site left or
right, clipped at the endpoints. At position $p$ with coin $c$, the policy
moves right with probability
\[
 \sigma(z_{pc}),\qquad z_{pc}=a+bp+dc,\qquad \sigma(z)=(1+e^{-z})^{-1}.
\]
For $0\le\eps\le1$, the training coin $c\in\{1,\ldots,L\}$ has law
$\mu_c=(1-\eps)\mathbf1_{c=L}+\eps/L$. Let $J_c(w)$ be the conditional
success probability, for $w=(a,b,d)$, and set
\[
 J_\eps=(1-\eps)J_L+\frac\eps L\sum_{c=1}^LJ_c,\qquad
 w_\eps'=\nabla J_\eps(w_\eps),\qquad w_\eps(0)=0.
\]
This is Euclidean gradient ascent on the exact return. For every training
diversity the flow is globally defined: the return is a finite polynomial
in logistic probabilities of linear forms, with bounded gradient and Hessian.
The model and horizon
conventions are those of MAIS-A8~\cite{a8}.

At the test state the agent is at $k=\lceil L/2\rceil$ and the coin is at
zero. The logit $P_\eps=a_\eps+kb_\eps$ is positive when the agent favors
moving away from the coin. Define its first correction time by
\[
 T_\eps=\inf\{t>0:P_\eps(t)<0\},\qquad \inf\varnothing=+\infty.
\]
This paper quantifies first correction from zero initialization. The earlier
O87 note~\cite{o87} concerns eventual correction from every finite
initialization, without a rate. First correction and permanent correction
are different observables.

Write
\[
 n=\lceil(L+1)/2\rceil,\quad r=L+1-n,\quad
 u=(n,r,nL),\quad M=\|u\|^2,\quad x=(1,2,1),
\]
\[
 \beta=\frac{x\cdot u}{M}=\frac{n(L+1)+2r}{n^2(1+L^2)+r^2},\qquad
 \alpha=\alpha_L=(1-\beta)^{-1}.
\]
The coefficient $\beta$ comes from the corrective training state $(2,1)$,
whose feature vector is $x$; the test state is $(k,0)$.
Here $r=n$ for odd $L$ and $r=n-1$ for even $L$. Since $r\ge2$ and $n\ge3$,
$M-n(L+1)-2r=n[n(1+L^2)-(L+1)]+r(r-2)>0$.
Thus $0<\beta<1$ and $\alpha>1$.

\begin{theorem}\label{thm:rate}
For every fixed integer $L\ge4$, there are positive constants
$c_-,c_+,\eps_0$ such that
\[
 c_-\eps^{-\alpha}\le T_\eps\le c_+\eps^{-\alpha}
 \qquad(0<\eps\le\eps_0).
\]
In particular, $\log T_\eps/\log(1/\eps)\to\alpha$ as $\eps\downarrow0$.
\end{theorem}
Thus correction takes asymptotically longer than $1/\eps$. For $L=4,5,6$,
the exponents are $157/138$, $81/73$, and $601/567$, respectively. The theorem
does not assert convergence of $\eps^\alpha T_\eps$ to a constant.

The exponent can be anticipated from two gradient scales. Along the
zero-diversity trajectory, the coin-$L$ gradient has size $t^{-1}$, while
the rare corrective contribution from state $(2,1)$ has size
$\eps t^{-\beta}$. Their ratio becomes order one when
$\eps t^{1-\beta}$ does, suggesting $t\asymp\eps^{-\alpha}$.
This balance alone does not prove correction: the trajectory changes after
leaving the zero-diversity regime. The upper-bound argument controls that
change until the probe crosses zero.

Section 2 identifies the zero-diversity trajectory. Section 3 bounds its
perturbation, giving the lower bound. Section 4 retains all minimal
failed-path scores through the transition and uses a ratio barrier to
force probe correction, giving the upper bound.

\section{The zero-diversity trajectory}\label{sec:ray}
Set
\[
 C_L=\begin{cases}(L+1)^{-1},&L\text{ odd},\\n(L+1)^{-1},&L\text{ even}.
 \end{cases}
\]
\begin{theorem}\label{ray:thm:ray}
There is $w_\infty\in\R^3$, with $u\cdot w_\infty=\log(C_LM)$, such that
\begin{equation}\label{eq:ray}
 w_0(t)=\frac uM\log t+w_\infty+o(1),\qquad
 1-J_L(w_0(t))\sim\frac1{Mt}.
\end{equation}
Also $t w_0'(t)\to u/M$.
\end{theorem}
For this section only, write $w=w_0$, $J_L$ for its return, and $z_p=z_{pL}$.
\subsection{The cone containing the trajectory}
For the moment, regard the nonterminal logits as independent. Their
success derivatives $\kappa_p=\partial J_L/\partial z_p$ are strictly
positive. Here is a direct justification. Let $V_j(p)$ be the probability
of hitting $L$ within $j$ actions and let $\rho_i(p)$ be the probability
of occupying $p$ at time $i$ before stopping. With $s^-=\max(s-1,0)$,
the Bellman recursion for $s<L$ is
\[
 V_{j+1}(s)=\sigma(z_s)V_j(s+1)+\sigma(-z_s)V_j(s^-),\qquad V_j(L)=1.
\]
Its derivative with respect to $z_p$ propagates by the same stopped
transition kernel, with source term
\[
 \mathbf1_{\{s=p\}}\sigma(z_p)\sigma(-z_p)
 [V_j(p+1)-V_j(p^-)].
\]
The derivatives at $j=0$ and at the terminal site vanish. Iterating the
recursion and averaging over the uniform initial site therefore gives
\[
 \kappa_p=\sigma(z_p)\sigma(-z_p)
 \sum_{i=0}^{H-1}\rho_i(p)
 [V_{H-i-1}(p+1)-V_{H-i-1}(\max(p-1,0))].
\]
Every bracket is nonnegative: from the farther site a path must first
hit the nearer site, and reducing the remaining horizon cannot improve
success. For strictness, put $j=H-1$, $p^-=\max(p-1,0)$, and let $\tau$ be
the first visit to $p+1$ starting at $p^-$. First-passage decomposition and
horizon monotonicity give
\[
 V_j(p^-)\le\Pr_{p^-}(\tau\le j)V_j(p+1)<V_j(p+1).
\]
The last inequality is strict because taking left at every step avoids
$p+1$ with positive probability, whereas $V_j(p+1)>0$ by taking right
until success. Since $\rho_0(p)=1/(L+1)$, strict positivity follows.

The chain rule now gives
\[
 a'=\sum_{p<L}\kappa_p>0,\qquad
 b'=\sum_{p<L}p\kappa_p>0,\qquad d'=La'.
\]
Thus, along the trajectory,
\begin{equation}\label{ray:eq:cone}
 d=La,\qquad 0\le b\le(L-1)a,\qquad
 h:=a+Ld=(1+L^2)a.
\end{equation}
In particular $h-b\ge(L^2-L+2)a$. Also $a(t)\to\infty$. Otherwise
\eqref{ray:eq:cone} and monotonicity would
make all coordinates converge to a finite point, at which $a'>0$.
Continuity would then contradict convergence of $a$.

\subsection{Failed paths and their scores}
Let $\Omega$ consist of all pairs of a nonterminal starting site and a
length-$H$ action sequence that never reaches $L$. For $\omega\in\Omega$,
let $N$ count its left actions, let $N_0$ count left actions taken at zero,
and let $S$ be the sum of the sites at which left actions are taken.
Write $p_j$ for its position before action $j$ and set
\[
 v_\omega=(N,S,LN),\qquad x_p=(1,p,L).
\]
Its conditional probability, given its starting site, is exactly
\begin{equation}\label{ray:eq:path}
 P_\omega(w)=e^{-v_\omega\cdot w}D_\omega(w),\qquad
 D_\omega(w)=\prod_{j=0}^{H-1}(1+e^{-z_{p_j}})^{-1}.
\end{equation}
Consequently $F:=1-J_L=(L+1)^{-1}\sum_\omega P_\omega$ and
\begin{equation}\label{ray:eq:grad}
 w'=\frac1{L+1}\sum_\omega P_\omega(v_\omega-E_\omega),
 \qquad E_\omega=\sum_{j=0}^{H-1}\sigma(-z_{p_j})x_{p_j}.
\end{equation}
On the cone \eqref{ray:eq:cone}, $z_p\ge h$, so, uniformly over this finite
path set,
\begin{equation}\label{ray:eq:errors}
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
\begin{equation}\label{ray:eq:gap}
 (v_\omega-u)\cdot w
 =(N-n)(h-b)+(N+S-n-r)b\ge0.
\end{equation}
Both coefficients on the right are nonnegative integers.

The score $(N,S)=(n,r)$ is attained, and its multiplicity is explicit.
If $L$ is odd, $r=n$ and the endpoint inequality forces $p_0=N_0=0$.
All left actions must be taken at site one: a left at site two or higher
would make $S>n$. Once the walk reaches site two or higher, it cannot take another left
action without violating this restriction. Thus all left actions precede
a final monotone right run. The unique path consists of
$n$ right-left cycles from zero followed by right actions to site $L-1$.
If $L$ is even, $r=n-1$. The inequality $S\ge N-N_0$ forces $N_0\ge1$,
and the endpoint inequality forces $N_0=1$ and $p_0=0$. Every other left
action is at site one, since a left at site two or higher would make
$S>n-1$. Again, reaching site two forces the remaining actions
to be right, so these possibilities are exhaustive. There are $n$ paths: place the one left self-loop
in any of the $n$ slots before, between, or after the $n-1$ right-left
cycles, then finish with right actions. This proves the coefficient $C_L$
in the theorem.

\subsection{Separation of the dominant paths}
To use \eqref{ray:eq:gap}, we must show that $b$ also diverges. Let $F_>$ be
the contribution to $F$ from paths with $N>n$. Each has a score gap at
least $h-b$. Comparing with one path of score $u$, using
\eqref{ray:eq:path}--\eqref{ray:eq:errors}, gives
\begin{equation}\label{ray:eq:high}
 \frac{F_>}{F}=O(e^{-(h-b)})\longrightarrow0.
\end{equation}
For the remaining paths, $S\ge r$. The $b$ component of
\eqref{ray:eq:grad}, together with $S\ge0$ on all paths, therefore gives
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
in \eqref{ray:eq:gap} is positive. The cone bound and the preceding estimate
therefore give a constant $\gamma>0$ such that its score gap is at least
$\gamma a$ at sufficiently late times. Summing the finite path set in
\eqref{ray:eq:path} and \eqref{ray:eq:grad}, and using \eqref{ray:eq:errors}, yields
\begin{align}
 F&=C_Le^{-U}\bigl(1+O(e^{-\gamma a})\bigr),\label{ray:eq:lossasym}\\
 w'&=C_Le^{-U}\bigl(u+O(e^{-\gamma a})\bigr),
 \qquad U=u\cdot w.\label{ray:eq:flowasym}
\end{align}
Here and below $\gamma$ may be reduced to absorb the denominator errors.
The error in the second line is a vector error in Euclidean norm.

\subsection{Integrating the asymptotic flow}
Since $a'>0$ and $a\to\infty$, we may use $a$ as the independent variable.
Equation \eqref{ray:eq:flowasym} gives
\[
 \frac{dw}{da}=\frac un+O(e^{-\gamma a}).
\]
The error is integrable. There is therefore a vector $v$ such that
\begin{equation}\label{ray:eq:offset}
 w=\frac un a+v+O(e^{-\gamma a}).
\end{equation}
Taking the inner product of \eqref{ray:eq:flowasym} with $u$ gives
\[
 \frac{d}{dt}e^U=C_LM\bigl(1+O(e^{-\gamma a})\bigr)
 \longrightarrow C_LM.
\]
It follows by integration that $e^U/t\to C_LM$, and hence
\[
 U=\log t+\log(C_LM)+o(1).
\]
Combining this with \eqref{ray:eq:offset} proves
\[
 w=\frac uM\log t+
 \left[v+\frac uM\bigl(\log(C_LM)-u\cdot v\bigr)\right]+o(1).
\]
The bracket is $w_\infty$ and has the required inner product with $u$.
Finally, \eqref{ray:eq:lossasym} and \eqref{ray:eq:flowasym} give the return and
velocity limits in Theorem~\ref{ray:thm:ray}.


\section{Tracking and the lower bound}
\begin{theorem}\label{thm:tracking}
There are $K,c,\eps_0>0$ such that for $0<\eps\le\eps_0$,
\begin{equation}\label{eq:tracking}
 \|w_\eps(t)-w_0(t)\|\le
 K\eps((1+t)^{1-\beta}-1),\qquad 0\le t\le c\eps^{-\alpha}.
\end{equation}
The constants can be chosen so that $P_\eps(t)>0$ for every
$0<t\le c\eps^{-\alpha}$.
\end{theorem}
\subsection{The diversity perturbation}
Write
\[
 \nabla J_\eps=\nabla J_L+\eps G,\qquad
 G=\frac1L\sum_{c=1}^L\nabla J_c-\nabla J_L.
\]
Fix a radius $R>0$. All estimates in this section are uniform for
$\|w-w_0(t)\|\le R$, with constants allowed to depend on $L,R$.
By \eqref{eq:ray} and boundedness on finite time intervals,
\begin{equation}\label{track:eq:logits}
 z_{pc}(w)=\frac{n+pr+cnL}{M}\log(1+t)+O_R(1)
 \quad(0\le p\le L,\ 1\le c\le L).
\end{equation}
Define
\[
 \theta_c=\frac{n+cnL}{M},\qquad
 \beta_c=\frac{n+(c+1)r+cnL}{M}.
\]
Thus $\theta_c\ge\theta_1$ and $\beta_c\ge\beta_1=\beta$.

\begin{lemma}\label{lem:path-score}
For a fixed coin, stop each episode at its first success or after $H$
actions. Any event consisting of these stopped paths has at most
$(L+1)2^H$ paths, including their starting sites.
Each path probability $p_\omega$ satisfies
\[
 \|\nabla p_\omega\|\le H\sqrt{1+2L^2}\,p_\omega.
\]
Thus a common bound on these probabilities bounds the gradient of the
event probability, up to a constant depending only on $L$.
\end{lemma}
\begin{proof}
The paths are prefix-free at each starting site and may be injected into
length-$H$ action words. An action score is either
$\sigma(-z_{pc})(1,p,c)$ or $-\sigma(z_{pc})(1,p,c)$; summing at most $H$
such scores gives the displayed bound. Sum over the finite event.
\end{proof}

For a start below $c$, differentiate failure rather than success. Every
failed path stays below $c$. If it has $N_-$ left actions, clipping at zero
gives $p_H\ge p_0+2L-2N_-$. Since $p_H\le c-1$,
\[
 N_-\ge\left\lceil\frac{2L+p_0-c+1}{2}\right\rceil\ge n.
\]
By \eqref{track:eq:logits}, each left-action probability below $c$ is at most
$C_R(1+t)^{-\theta_c}$. The failed-path probability and its summed gradient
are therefore $O_R((1+t)^{-n\theta_c})$.

For a start above $c$, differentiate success. Every successful path includes
a left action from $c+1$. Its probability is at most
$C_R(1+t)^{-\beta_c}$ by \eqref{track:eq:logits}; all other action factors are
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
\begin{equation}\label{track:eq:Gbound}
 \|G(w)\|\le C_R(1+t)^{-\beta}\quad\text{if }\|w-w_0(t)\|\le R.
\end{equation}

\subsection{An integrable one-sided Hessian bound}
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
\begin{equation}\label{track:eq:hessian}
 \nabla^2 J_L
 =\frac1{L+1}\sum_\omega P_\omega
 (B_\omega-g_\omega g_\omega^{\mathsf T})
 \preceq\frac1{L+1}\sum_\omega P_\omega B_\omega.
\end{equation}
The ordering is that of symmetric quadratic forms.

Set $\kappa=n(1+L^2)/M>0$. Equation \eqref{track:eq:logits} gives
$z_{p,L}\ge\kappa\log(1+t)-C_R$, and hence
$B_\omega\preceq C_R(1+t)^{-\kappa}I$.
Also the bound on path scores gives
\[
 P_\omega(w)\le
 e^{RH\sqrt{1+2L^2}}P_\omega(w_0(t)).
\]
Summing and using \eqref{eq:ray}, we obtain
$1-J_L(w)\le C_R(1+t)^{-1}$.
It follows from \eqref{track:eq:hessian} that
\begin{equation}\label{track:eq:onesided}
 \nabla^2J_L(w)\preceq K_R(t)I,\qquad
 K_R(t)=C_R(1+t)^{-1-\kappa},\qquad
 \int_0^\infty K_R(t)\,dt<\infty.
\end{equation}
These bounds hold for all $t\ge0$ after increasing the constants on a
compact initial interval. In particular, no assumption about the perturbed
trajectory remaining in the zero-diversity invariant cone is needed.

\subsection{Tracking and the first crossing}
Put $v_*=(1,k,0)$. Since $a_0',b_0'>0$, the probe $P_0$ is strictly
increasing from zero. Fix
\[
 0<R\le\min\left\{1,\frac{P_0(1)}{2\|v_*\|}\right\};
\]
this choice depends only on the zero-diversity trajectory. Set
$\delta w=w_\eps-w_0$ and $\Delta=\|\delta w\|$, and stop the comparison
if $\Delta$ first reaches $R$. The segment between the two parameters lies
in the same radius-$R$ ball, and
\[
 (\delta w)'=\int_0^1\nabla^2J_L(w_0+s\delta w)\,\delta w\,ds
 +\eps G(w_\eps).
\]
Taking the inner product with $\delta w$ and applying
\eqref{track:eq:onesided} and \eqref{track:eq:Gbound} yields
\[
 \frac12(\Delta^2)'\le K_R(t)\Delta^2
 +\eps C_R(1+t)^{-\beta}\Delta.
\]
Thus, while $\Delta<R$,
\[
 \Delta'\le K_R(t)\Delta+\eps C_R(1+t)^{-\beta}.
\]
At $\Delta=0$ this is understood as an upper right derivative; equivalently,
one may regularize the norm. Gr\"onwall's inequality and integrability of
$K_R$ yield a finite constant $A_R$ such that
\begin{equation}\label{track:eq:tracking}
 \Delta(t)\le A_R\eps\bigl((1+t)^{1-\beta}-1\bigr).
\end{equation}
Consider
\[
 S_\eps=\left(1+\frac{R}{2A_R\eps}\right)^{1/(1-\beta)}-1.
\]
If the first exit occurred at or before $S_\eps$, continuity and
\eqref{track:eq:tracking} would imply $R\le R/2$. Thus
\eqref{track:eq:tracking} holds through $S_\eps$. The comparison time satisfies
\[
 S_\eps\sim\left(\frac{R}{2A_R}\right)^\alpha\eps^{-\alpha}.
\]

Our choice of $R$ also keeps the probe positive. For $1\le t\le S_\eps$,
the tracking bound $\Delta\le R/2$ gives
$P_\eps(t)\ge P_0(1)-\|v_*\|R/2>0$.
On $0\le t\le1$, let $m=\min_{[0,1]}P_0'>0$.
Concavity of $(1+t)^{1-\beta}$ implies
$\Delta(t)\le A_R\eps(1-\beta)t$, so
\[
 P_\eps(t)\ge
 \bigl(m-\|v_*\|A_R\eps(1-\beta)\bigr)t>0\qquad(0<t\le1)
\]
for sufficiently small $\eps$. Reduce $\eps_0$ so that $S_\eps\ge1$,
and choose $c>0$ with $c\eps^{-\alpha}\le S_\eps$ throughout the
remaining range. Equation \eqref{track:eq:tracking} and these positivity bounds
prove Theorem~\ref{thm:tracking}.


\section{The upper bound}
Write $E=\log(1/\eps)$ and $W=\alpha u/M$ throughout this section.
We first find a region in which a finite failed-path sum gives a uniform
approximation to the flow. We then prove that the trajectory enters that
region with enough corrective drift to force a crossing.
\subsection{An approximation through the sign change}
Put
\[
 A=a+d-b,\qquad D=d-a,\qquad q=a+2b+d=x\cdot w,\qquad h=a+Ld.
\]
At the ray scale,
\[
 A(W)=\frac\alpha M[n(L+1)-r]>0,\qquad
 D(W)=\frac\alpha M n(L-1)>0,\qquad
 P(W)=\frac\alpha M(n+kr)>0.
\]
Fix $\delta>0$ smaller than half of both $A(W)$ and $D(W)$.
All subsequent constants may depend on this choice.
Consider the region
\begin{equation}\label{upper:eq:region}
 A\ge\delta E,\qquad D\ge\delta E,\qquad P\ge0.
\end{equation}
Every training logit in this region is at least $\delta E$. Indeed, if
$b\ge0$, then $d=(A+D+b)/2>0$ and $a+d=A+b\ge\delta E$.
If $b<0$, $a\ge-kb$, $d=a+D>0$, and
\[
 a+Lb+d=2a+Lb+D\ge(L-2k)b+D\ge\delta E.
\]
Also
\begin{equation}\label{upper:eq:bd}
 b+d\ge\delta E.
\end{equation}
For $b\ge0$, use $b+d=(A+D+3b)/2$; for $b<0$, use
$b+d=D+a+b\ge D+(1-k)b$.
In particular $q=z_{2,1}\ge\delta E$, since $(2,1)$ is a training state.
Equivalently, $q=A+3b$ for $b\ge0$, and
$q=2a+2b+D\ge2(1-k)b+D$ for $b<0$.


For each failed length-$2L$ path with coin $L$, let $N$ be its number of
left actions and $S$ the sum of the sites at those actions. The path count
in Section~\ref{sec:ray} gives
\[
 N\ge n,\qquad N+S\ge L+1=n+r,\qquad S\le N(L-1).
\]
Let $m_S$ be the number of such paths, including their starting sites,
with $N=n$ and position sum $S$. Approximate their total failure probability
by the positive exponential sum
\begin{equation}\label{upper:eq:F}
 \Phi(w)=\frac{e^{-nh}}{L+1}\sum_{S=r}^{n(L-1)}m_S e^{-Sb},\qquad
 s(b)=\frac{\sum_S S m_S e^{-Sb}}{\sum_S m_S e^{-Sb}},\qquad
 z(b)=(n,s(b),nL).
\end{equation}
This $\Phi$ approximates only the $N=n$ failed paths; it is not the exact
failure probability $F=1-J_L$ used in Section~\ref{sec:ray}.
We have $-\nabla \Phi=\Phi z$ and $r\le s(b)\le n(L-1)$. The endpoint counts
$m_r$ and $m_{n(L-1)}$ are positive, as justified below. For large positive
$b$, the smallest score $S=r$ dominates; for large negative $b$, the
largest score $S=n(L-1)$ dominates. Near $b=0$, neither endpoint alone
is an adequate approximation. The finite sum retains every score, and
$s(b)$ is their weighted mean.
The following path facts will also be used. From any start $p_0<c$, a
failed path stays below $c$ and satisfies
$p_0+2L-2N_-\le p_{2L}\le c-1$. Thus
\[
 N_-\ge\left\lceil(2L+p_0-c+1)/2\right\rceil\ge n.
\]
Every successful path starting above $c$ must take a left action at $c+1$.
For $c=1$, the only such path with one left action is the immediate step
from site $2$: any larger start or any preceding right action requires
another left action before reaching the coin.
The endpoint score $S=n(L-1)$ is attained from start zero by climbing to
$L-1$, then taking $(\mathrm{left},\mathrm{right})^n$ for odd $L$; for
even $L$, take $(\mathrm{left},\mathrm{right})^{n-1}$ followed by one left.
The lengths are respectively $L-1+2n=2L$ and $L-1+2n-1=2L$.
Both paths fail. Positivity of $m_r$ follows from the explicit paths used
in the zero-diversity trajectory proof.

Set
\begin{equation}\label{upper:eq:Q}
 Q(w)=\frac{\eps}{L(L+1)}e^{-q}.
\end{equation}

\begin{lemma}\label{upper:lem:uniform}
Uniformly in \eqref{upper:eq:region},
\begin{equation}\label{upper:eq:approx}
 \nabla J_\eps=\Phi z-Qx+\mathcal E,\qquad
 \|\mathcal E\|\le C(\eps+e^{-\delta E})(\Phi+Q).
\end{equation}
\end{lemma}
\begin{proof}
For each fixed coin and starting site, success and failure probabilities
sum to one. We may therefore differentiate success from above and the
negative of failure from below. Starts at the coin have zero derivative.
We treat the entire coin-$L$ contribution first, and use this decomposition
only for the remaining coins $1\le c<L$, so no term is counted twice.

A failed path for coin $L$ has probability
$e^{-Nh-Sb}$ times a product of $2L$ logistic denominators. Since every
logit is at least $\delta E$, these denominators equal $1+O(e^{-\delta E})$;
their logarithmic gradients are $O(e^{-\delta E})$. These estimates are
uniform over the finite path set.

Paths with $N>n$ have a score gap of at least $\delta E$ relative to one
of the endpoint scores in \eqref{upper:eq:F}. For $b\ge0$, write
\[
 Nh+Sb-(nh+rb)=(N-n)(h-b)+(N+S-n-r)b,
\]
where
$h-b=((L+1)A+(L-1)D+(L-1)b)/2\ge\delta E$.
For $b<0$, write
\[
 Nh+Sb-n[h+(L-1)b]
 =(N-n)[h+(L-1)b]+[S-N(L-1)]b,
\]
where $h+(L-1)b=z_{L-1,L}\ge\delta E$.
Thus their probabilities and gradient contributions are $O(e^{-\delta E}\Phi)$.
The coin-$L$ term is $\Phi z+O((\eps+e^{-\delta E})\Phi)$ after its mixture
weight is included.

For a start above coin $1$, the unique successful path with only one left
action is the immediate left step from site $2$. Its gradient, with both
initial-site and coin weights, is $-Qx+O(e^{-\delta E}Q)$. Every other
successful path from above includes that left step and at least one further
left action. Its probability is at most $e^{-q-\delta E}$. Lemma~\ref{lem:path-score} gives the same bound on its gradient,
up to a constant.

For coins $2\le c<L$, success from above requires a left action at $c+1$.
Its logit is $q+(c-1)(b+d)\ge q+\delta E$, by \eqref{upper:eq:bd}.
Finally, for the remaining coins $1\le c<L$, failure from below requires at least $n$ left actions.
If $b\ge0$, its minimum below-coin logit is $a+dc\ge a+d=A+b$, and
\[
 n(a+d)-q=(n-1)A+(n-3)b\ge\delta E.
\]
If $b<0$, that minimum is
$a+(c-1)b+dc=q+(c-1)(b+d)-2b\ge q$, so $n$ copies exceed $q$ by at
least $\delta E$. Differentiate these below-coin contributions through their
failure probabilities and apply Lemma~\ref{lem:path-score} again. Summing
the finitely many paths proves the lemma.
\end{proof}

\subsection{A ratio barrier}
Define $\varrho=Q/\Phi$ and $\varrho_0=nL/2$. For $z=(n,s,nL)$, set
$M_s=\|z\|^2$ and $\chi_s=z\cdot x=n(L+1)+2s$. The exact logarithmic
derivatives of $\Phi,Q$ imply
\begin{equation}\label{upper:eq:ratio}
 (\log \varrho)'=(z-x)\cdot\nabla J_\eps
 =\Phi\{M_s-\chi_s-(\chi_s-6)\varrho\}+(z-x)\cdot\mathcal E.
\end{equation}
At $\varrho=\varrho_0$, the expression in braces is
\[
 s^2-(nL+2)s+n^2\left(1+\frac{L^2-L}{2}\right)+n(2L-1).
\]
Its minimum over all real $s$ is
\begin{equation}\label{upper:eq:margin}
 n^2\left(1+\frac{L^2}{4}-\frac L2\right)+n(L-1)-1>0.
\end{equation}
For sufficiently small $\eps$, Lemma~\ref{upper:lem:uniform} therefore makes
$\varrho'>0$ at $\varrho=\varrho_0$, throughout \eqref{upper:eq:region}. A trajectory entering
with $\varrho>\varrho_0$ cannot cross down through this barrier while in the region.

For $\varrho\ge \varrho_0$, we have
\[
 \frac{\chi_s}{\varrho}-6\le-\frac2L,\qquad
 \frac{n+ks}{\varrho}-(1+2k)\le-1.
\]
Using \eqref{upper:eq:approx}, and reducing the permitted $\eps$ if needed,
\begin{equation}\label{upper:eq:decrease}
 q'\le-\frac QL,\qquad P'\le-\frac Q2.
\end{equation}
The two other linear coordinates satisfy
\begin{equation}\label{upper:eq:preserve}
 A'\ge-C\zeta Q,\qquad D'\ge-C\zeta Q,
 \qquad \zeta=\eps+e^{-\delta E}.
\end{equation}
Indeed, the $-Qx$ contribution is zero in both coordinates, and the $\Phi z$
contributions are $\Phi[n(L+1)-s]\ge2n\Phi$ and $\Phi n(L-1)>0$. The error is
$O(\zeta Q)$ since $\Phi\le Q/\varrho_0$.

Suppose the flow enters at time $t_e$ with
\begin{equation}\label{upper:eq:entry}
 A,D\ge2\delta E,\quad 0<P\le C_0E,\quad \varrho>\varrho_0,
 \quad q\le(\alpha-1)E+C_0.
\end{equation}
Define $t^*$ to be the first time after $t_e$ at which $A=\delta E$,
$D=\delta E$, $\varrho=\varrho_0$, or $P=0$. Before $t^*$ all preceding
estimates hold. In particular, \eqref{upper:eq:decrease} gives
\[
 (e^q)'\le-\frac{\eps}{L^2(L+1)}.
\]
Since $e^q$ is positive, this implies
\[
 t^*-t_e\le L^2(L+1)e^{q(t_e)}/\eps=O(\eps^{-\alpha});
\]
otherwise integration would make $e^q$ nonpositive before the first exit.
Thus $t^*$ is finite.

For $t_e\le t<t^*$, \eqref{upper:eq:decrease} also gives
$\int_{t_e}^tQ\,du\le2P(t_e)\le2C_0E$. By \eqref{upper:eq:preserve},
\[
 A(t),D(t)\ge2\delta E-2CC_0\zeta E>\delta E
\]
for sufficiently small $\eps$. These inequalities hold at $t^*$ by
continuity. Also $\varrho(t^*)=\varrho_0$ is impossible: the barrier gives
$\varrho'>0$ there, whereas a first crossing from above would have
$\varrho'\le0$. The only remaining exit is $P(t^*)=0$. Since
$P'(t^*)\le-Q(t^*)/2<0$, the probe crosses into $P<0$ immediately.
It remains to establish \eqref{upper:eq:entry} at $t_e=O(\eps^{-\alpha})$.

\subsection{Reaching the ratio barrier}
For $y$ in a fixed compact set, $WE+y$ lies in the region
\eqref{upper:eq:region} for all sufficiently large $E$: the forms $A,D,P$
are strictly positive at $W$, and $A(W),D(W)>2\delta$. Also $W_b>0$, so
the finite sum in \eqref{upper:eq:F} is uniformly dominated by its $S=r$
term. Consequently,
\[
 \eps^{-\alpha}\Phi(WE+y)\to C_Le^{-u\cdot y},\qquad s(b)\to r,
 \qquad \eps^{-\alpha}Q(WE+y)=Be^{-x\cdot y},
 \quad B=\frac1{L(L+1)}.
\]
Here $u\cdot W=\alpha$, $x\cdot W=\alpha-1$, and
$C_L=m_r/(L+1)>0$ was computed in Section~\ref{sec:ray}.
Lemma~\ref{upper:lem:uniform} now gives the uniform compact-set limit
\begin{equation}\label{upper:eq:limit}
 \eps^{-\alpha}\nabla J_\eps(WE+y)
 \longrightarrow C_Lu e^{-u\cdot y}-Bxe^{-x\cdot y}.
\end{equation}
Indeed, its rescaled error is bounded by a constant times
$(\eps+e^{-\delta E})\eps^{-\alpha}(\Phi+Q)$, which tends uniformly to zero.
Thus all path classes are controlled by the same estimate used after entrance.

In time $\tau=\eps^\alpha t$, the limiting equation for $y$ is the right
side of \eqref{upper:eq:limit}. Write $U=u\cdot y$, $q_y=x\cdot y$,
$\chi_+=u\cdot x$, and introduce a second clock by
$d\xi/d\tau=C_Le^{-U}$. In this clock the limiting equation and ratio are
\begin{equation}\label{upper:eq:logistic}
 \frac{dy}{d\xi}=u-\mathcal R x,\qquad
 \mathcal R=\frac B{C_L}e^{U-q_y},\qquad
 \frac{d\mathcal R}{d\xi}
 =\mathcal R\{(M-\chi_+)-(\chi_+-6)\mathcal R\}.
\end{equation}
Since $M>\chi_+>6$, every positive ratio converges to
$\mathcal R_*=(M-\chi_+)/(\chi_+-6)$. Applying \eqref{upper:eq:margin} at $s=r$ shows $\mathcal R_*>\varrho_0$.

Fix $\tau_0=c/2$, with $c$ from Theorem~\ref{thm:tracking}, and put
$t_0=\tau_0\eps^{-\alpha}$. Equations \eqref{eq:ray} and
\eqref{eq:tracking} put
\[
 y_\eps(t_0):=w_\eps(t_0)-WE
\]
in a fixed compact set $\mathcal K_0$, independent of sufficiently small
$\eps$: $\alpha(1-\beta)=1$ makes the tracking error $O(1)$ at $t_0$.
On $\mathcal K_0$ the initial limiting ratio is bounded above and bounded away
from zero. Choose $\varrho_1$ strictly between $\varrho_0$ and $\mathcal R_*$.
The logistic equation \eqref{upper:eq:logistic} then puts every such limiting
solution above $\varrho_1$ by a single finite clock time $\xi_*$.

Write $f_\eps(y)=\eps^{-\alpha}\nabla J_\eps(WE+y)$ and
$g(y)=C_Le^{-u\cdot y}>0$. Use $d\xi/d\tau=g(y)$ also for the full
flow. Its transformed equation is
\[
 \frac{dy_\eps}{d\xi}=\frac{f_\eps(y_\eps)}{g(y_\eps)}.
\]
This preserves the orbits. Let $\mathcal K_1$ be the union of all limiting
trajectories from $\mathcal K_0$ on $[0,\xi_*]$. The logistic ratio stays
between its initial value and its
positive equilibrium, uniformly over $\mathcal K_0$. Thus these orbits
and their velocities are bounded. Continuous dependence on the initial
point makes $\mathcal K_1$ compact.

On the closed one-neighbourhood $\mathcal K_2$ of $\mathcal K_1$,
$WE+y$ lies in \eqref{upper:eq:region} for all sufficiently small $\eps$,
by the positivity of $A(W),D(W),P(W)$. Also $g$ is bounded above and away
from zero there. Dividing \eqref{upper:eq:limit} by $g$ therefore gives
uniform convergence of the transformed fields to $u-\mathcal R x$.
If their uniform difference is $\eta_\eps\to0$ and a Lipschitz constant for the limit field
on a containing compact ball is $\ell_0$, comparison up to first exit gives
\[
 \sup_{0\le \xi\le \xi_*}\|y_\eps(\xi)-y(\xi)\|
 \le\eta_\eps \xi_* e^{\ell_0 \xi_*}.
\]
For small $\eps$ this is less than one, excluding exit from $\mathcal K_2$.
The initial limiting point is always chosen equal to the full initial
point; convergence of the initial points themselves is not required.

The ratios $Q/\Phi$ converge uniformly on $\mathcal K_2$ to $\mathcal R$,
since $W_b>0$ makes the $S=r$ term dominate the finite sum. The comparison
therefore gives $\varrho>\varrho_0$ at clock time $\xi_*$, uniformly over the allowed
initial points. Finally $u\cdot y$ is bounded above on $\mathcal K_2$,
so $d\tau/d\xi=e^{u\cdot y}/C_L$ has a uniform upper bound. The elapsed
rescaled time is bounded independently of $\eps$. We have therefore reached
$t_e=O(\eps^{-\alpha})$ with $w_\eps(t_e)=WE+O(1)$ and $\varrho>\varrho_0$.
The values of $A,D,P$ at $W$, our choice of $\delta$, and
$q(W)=\alpha-1$ give \eqref{upper:eq:entry} after increasing $C_0$.
If a probe crossing occurred earlier, the upper bound already holds.
Otherwise Section 4.2 forces one within a further $O(\eps^{-\alpha})$ time.
Together with Theorem~\ref{thm:tracking}, this proves Theorem~\ref{thm:rate}.


\section{Numerical evidence and reproduction}
The companion code evaluates the return and its gradient by finite-horizon
dynamic programming. It propagates both success and failure probabilities
and uses the less saturated value difference in the gradient recursion.
Independent rational path enumeration checks the implementation, including
a saturated-policy case. No Monte Carlo return estimates are used.

We integrated the flow from zero for $L=4,5,6$ and $\eps=10^{-p}$, using
\[p\in\{2,4,8,12,16,24,32,48,64,96\}.\]
All thirty runs reached a downward probe crossing. Integration used the
clock $s=\log(1+t)$ and DOP853 with relative tolerance $2\times10^{-9}$.
Six repeats with RK45 and relative tolerance $2\times10^{-11}$ changed
crossing times by at most $2.20\times10^{-10}$ in relative terms.
Independent 180-digit differentiation at the three $\eps=10^{-96}$
crossing states agreed with the computed gradients to relative error below
$4.6\times10^{-14}$. These checks are not certified integration bounds.

\begin{center}
\begin{tabular}{ccc}\toprule
$L$ & Theorem exponent & Secant slope, $10^{-64}$ to $10^{-96}$\\\midrule
4 & $1.137681159$ & $1.138261638$\\
5 & $1.109589041$ & $1.110163109$\\
6 & $1.059964727$ & $1.061551262$\\\bottomrule
\end{tabular}
\end{center}
The displayed slopes lie above $\alpha$; no monotonicity or direction of
approach is asserted by the theorem.
\begin{figure}[ht]
\centering\includegraphics[width=\textwidth]{../output/figures/correction-time-scaling.pdf}
\caption{First correction times and successive log--log slopes from the
retained numerical runs. Each slope uses consecutive diversity values;
the dashed lines in the right panel show the theorem's exponents. The
finite-range slopes are evidence about convergence, not a proof of it.}
\end{figure}

The companion README records the environment, commands, source snapshot,
and result files. Its exact finite checks cover path scores, endpoint counts,
the ratio barrier and the invariant-region algebra. These checks cover only
their stated finite ranges; the proofs apply to every fixed integer $L\ge4$.

\section{Scope and remaining questions}
The result concerns exact continuous-time return-gradient ascent, fixed $L$,
and zero initialization. It supplies two-sided order bounds but no sharp
prefactor. A limiting law for Gaussian initializations, the time of permanent
correction, discrete gradient ascent, and sampled policy-gradient updates
remain separate questions. Constants may depend on $L$; no bound uniform
as $L\to\infty$ is asserted.

\paragraph{Acknowledgment.} Computations and draft review used Astra and Claude.

\begin{thebibliography}{9}
\bibitem{a8} MAIS, \emph{A predictive theory of out-of-distribution
generalization: which of two perfect policies does gradient descent select?}
Research agenda MAIS-A8, Definition 3.1 and Section 6.
\href{https://github.com/lionellevine/MAIS/blob/7b23a8a30c0eb0b1d3b55c592ca9554256fc4805/agendas/A8/MAIS-A8.tex}{Source version 7b23a8a}.
\bibitem{o87} R. Sneiderman, \emph{A negative solution to MAIS-O87},
September 2026. \href{https://github.com/lionellevine/MAIS/issues/35}{Submitted candidate, MAIS issue 35}.
\end{thebibliography}
\end{document}
