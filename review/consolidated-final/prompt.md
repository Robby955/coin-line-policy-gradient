coin-line-rates | local preprint | complete manuscript at ab42e66

Independently audit the complete manuscript below from first principles. It combines three proof stages. Do not assume any prior review or theorem is correct. Give a concise, adversarial mathematical report, with exact section/equation anchors. No tools are available; reason from the supplied text. Do not rewrite files.

The exact compiled PDF has been frozen by SHA256 in input-hashes.json. Its extracted text and complete LaTeX source are supplied below. The mathematical review covers that exact version; the authoring session separately checks the rendered layout.

Priorities:
1. Check the full theorem for every fixed integer L>=4 and sufficiently small positive epsilon, with zero initialization. Trace all hypotheses across sections, including use of the tracking theorem in the entrance argument. Look for circularity, hidden uniformity, unsupported asymptotics, parity or wall errors, and mistakes in the strict first-correction definition at P(0)=0.
2. Re-derive the failed-path inequalities and both endpoint multiplicities, the zero-diversity convergent offset, the one-sided Hessian control and the perturbation estimate.
3. Audit the full upper-bound proof, especially the uniform finite-sum approximation through b=0, preservation of A,D and the ratio, every first-exit possibility, the compact limiting field now derived from the uniform lemma, and conversion between all clocks. Verify that a bound on first zero really implies the claimed infimum of P<0.
4. Check the model, constants, notation and numerical claims for internal consistency. Numerics are evidence only, never premises. Distinguish an actual gap from an argument that is correct but too compressed.
5. Recommend concrete readability improvements that help a mathematically trained reader follow the mechanism. Prefer a few useful changes over cosmetic restyling.

Return: (a) verdict: valid / repairable gap / substantial gap / cannot establish, (b) critical/major/minor findings with exact anchors and proposed repairs, (c) theorem dependency and quantifier audit, (d) precise scope of verification and uncertainty, (e) ordered edit plan. Do not inflate confidence or rubber-stamp the paper. Do not request research extensions beyond the theorem as publication blockers. Keep the report below 3000 words.

COMPLETE LATEX SOURCE

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
During training, $c\in\{1,\ldots,L\}$ has law
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
 \alpha=(1-\beta)^{-1}.
\]
The coefficient $\beta$ comes from the corrective training state $(2,1)$,
whose feature vector is $x$; the test state is $(k,0)$.
Here $r=n$ for odd $L$ and $r=n-1$ for even $L$. Since $r\le n$ and
$n\ge3$, we have $0<\beta<1$ and $\alpha>1$.

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

The proof has three parts. First we identify the logarithmic trajectory
when all training coins are at $L$. Then we bound its perturbation under
small diversity, giving the lower bound. For the upper bound, we keep a
finite sum of minimal failed-path scores rather than following just one
score through the transition. A ratio barrier makes the probe decrease
while preserving the region in which that approximation is valid.

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
of occupying $p$ at time $i$ before stopping. Differentiating the finite
Bellman recursion gives
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
In particular $h-b\ge(L^2-L+2)a$. The flow exists for all time because
its vector field is bounded and globally Lipschitz: the return is a
finite polynomial in logistic probabilities of linear forms, whose first
and second derivatives are bounded.
Also $a(t)\to\infty$. Otherwise \eqref{ray:eq:cone} and monotonicity would
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
For a fixed coin, any event consisting of stopped action paths of at most
$H$ actions has at most $(L+1)2^H$ paths, including their starting sites.
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
Let $\Delta(t)=\|w_\eps(t)-w_0(t)\|$ and stop the comparison if $\Delta$ first
reaches $R$. The line segment between the two parameters lies in the same
radius-$R$ ball. Integrating \eqref{track:eq:onesided} along that segment and
using \eqref{track:eq:Gbound} gives, while $\Delta<R$,
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
\eqref{track:eq:tracking} would imply $R\le R/2$. Thus there is no exit, and
\eqref{track:eq:tracking} holds through $S_\eps$, and
\[
 S_\eps\sim\left(\frac{R}{2A_R}\right)^\alpha\eps^{-\alpha}.
\]

To ensure a positive probe, put $v_*=(1,k,0)$. Since $a_0',b_0'>0$,
$P_0$ is strictly increasing from zero. Choose
\[
 0<R\le\min\left\{1,\frac{P_0(1)}{2\|v_*\|}\right\}.
\]
For $1\le t\le S_\eps$, the tracking bound $\Delta\le R/2$ gives
$P_\eps(t)\ge P_0(1)-\|v_*\|R/2>0$.
On $0\le t\le1$, let $m=\min_{[0,1]}P_0'>0$.
Concavity of $(1+t)^{1-\beta}$ implies
$\Delta(t)\le A_R\eps(1-\beta)t$, so
\[
 P_\eps(t)\ge
 \bigl(m-\|v_*\|A_R\eps(1-\beta)\bigr)t>0\qquad(0<t\le1)
\]
for sufficiently small $\eps$. Reduce $\eps_L$ so that $S_\eps\ge1$,
and choose $c_L>0$ with $c_L\eps^{-\alpha}\le S_\eps$ throughout the
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
Fix $\delta>0$ smaller than half of both $A(W)$ and $D(W)$; these
quantities are positive. All subsequent constants may depend on this choice.
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
with $N=n$ and position sum $S$. Define the positive exponential sum
\begin{equation}\label{upper:eq:F}
 F(w)=\frac{e^{-nh}}{L+1}\sum_{S=r}^{n(L-1)}m_S e^{-Sb},\qquad
 s(b)=\frac{\sum_S S m_S e^{-Sb}}{\sum_S m_S e^{-Sb}},\qquad
 z(b)=(n,s(b),nL).
\end{equation}
Then $-\nabla F=Fz$ and $r\le s(b)\le n(L-1)$. The endpoint counts $m_r$ and $m_{n(L-1)}$ are positive, as justified below.
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
 \nabla J_\eps=Fz-Qx+\mathcal E,\qquad
 \|\mathcal E\|\le C(\eps+e^{-\delta E})(F+Q).
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
Thus their probabilities and gradient contributions are $O(e^{-\delta E}F)$.
The coin-$L$ term is $Fz+O((\eps+e^{-\delta E})F)$ after its mixture
weight is included.

For a start above coin $1$, the unique successful path with only one left
action is the immediate left step from site $2$. Its gradient, with both
initial-site and coin weights, is $-Qx+O(e^{-\delta E}Q)$. Every other
successful path from above includes that left step and at least one further
left action. Its probability is at most $e^{-q-\delta E}$. The norm of
a path's logarithmic gradient is uniformly bounded, so its gradient obeys
the same estimate up to a constant.

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
failure probabilities. Summing all the finitely many paths proves the lemma.
\end{proof}

\subsection{A ratio barrier}
Define $R=Q/F$ and $R_0=nL/2$. For $z=(n,s,nL)$, set
$M_s=\|z\|^2$ and $D_s=z\cdot x=n(L+1)+2s$. The exact logarithmic
derivatives of $F,Q$ imply
\begin{equation}\label{upper:eq:ratio}
 (\log R)'=(z-x)\cdot\nabla J_\eps
 =F\{M_s-D_s-(D_s-6)R\}+(z-x)\cdot\mathcal E.
\end{equation}
At $R=R_0$, the expression in braces is
\[
 s^2-(nL+2)s+n^2\left(1+\frac{L^2-L}{2}\right)+n(2L-1).
\]
Its minimum over all real $s$ is
\begin{equation}\label{upper:eq:margin}
 n^2\left(1+\frac{L^2}{4}-\frac L2\right)+n(L-1)-1>0.
\end{equation}
For sufficiently small $\eps$, Lemma~\ref{upper:lem:uniform} therefore makes
$R'>0$ at $R=R_0$, throughout \eqref{upper:eq:region}. A trajectory entering
with $R>R_0$ cannot cross down through this barrier while in the region.

For $R\ge R_0$, we have
\[
 \frac{D_s}{R}-6\le-\frac2L,\qquad
 \frac{n+ks}{R}-(1+2k)\le-1.
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
Indeed, the $-Qx$ contribution is zero in both coordinates, and the $Fz$
contributions are $F[n(L+1)-s]\ge2nF$ and $Fn(L-1)>0$. The error is
$O(\zeta Q)$ since $F\le Q/R_0$.

Suppose the flow enters at time $t_e$ with
\begin{equation}\label{upper:eq:entry}
 A,D\ge2\delta E,\quad 0<P\le C_0E,\quad R>R_0,
 \quad q\le(\alpha-1)E+C_0.
\end{equation}
Define $t^*$ to be the first time after $t_e$ at which $A=\delta E$,
$D=\delta E$, $R=R_0$, or $P=0$. Before this time all preceding estimates
hold. For any such $t$, \eqref{upper:eq:decrease} gives
$\int_{t_e}^tQ\,du\le2P(t_e)\le2C_0E$. By \eqref{upper:eq:preserve},
\[
 A(t),D(t)\ge2\delta E-2CC_0\zeta E>\delta E
\]
for sufficiently small $\eps$. These inequalities also hold at a finite
$t^*$ by continuity. The alternative $R(t^*)=R_0$ is impossible because
$R'>0$ there, whereas a first crossing from above would have $R'\le0$.
Hence any finite $t^*$ is a probe zero. If $t^*=\infty$, the same estimates
hold for all later times, which the following time bound rules out.
But \eqref{upper:eq:decrease} also gives
\[
 (e^q)'\le-\frac{\eps}{L^2(L+1)}.
\]
A positive $e^q$ cannot satisfy this inequality for more than
$L^2(L+1)e^{q(t_e)}/\eps=O(\eps^{-\alpha})$ time. The probe must
therefore reach zero within that time. Since $P'<0$ at this first zero,
it crosses into $P<0$ immediately. It remains to establish the entrance
conditions \eqref{upper:eq:entry} at $t_e=O(\eps^{-\alpha})$.

\subsection{Reaching the ratio barrier}
For $y$ in a fixed compact set, $WE+y$ lies in the region
\eqref{upper:eq:region} for all sufficiently large $E$: the forms $A,D,P$
are strictly positive at $W$, and $A(W),D(W)>2\delta$. Also $W_b>0$, so
the finite sum in \eqref{upper:eq:F} is uniformly dominated by its $S=r$
term. Consequently,
\[
 \eps^{-\alpha}F(WE+y)\to C_Le^{-u\cdot y},\qquad s(b)\to r,
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
$(\eps+e^{-\delta E})\eps^{-\alpha}(F+Q)$, which tends uniformly to zero.
Thus all path classes are controlled by the same estimate used after entrance.

In time $\tau=\eps^\alpha t$, the limiting equation for $y$ is the right
side of \eqref{upper:eq:limit}. Write $U=u\cdot y$, $q_y=x\cdot y$,
$D_+=u\cdot x$, and introduce a second clock by
$d\xi/d\tau=C_Le^{-U}$. In this clock the limiting equation and ratio are
\begin{equation}\label{upper:eq:logistic}
 \frac{dy}{d\xi}=u-\mathcal R x,\qquad
 \mathcal R=\frac B{C_L}e^{U-q_y},\qquad
 \frac{d\mathcal R}{d\xi}
 =\mathcal R\{(M-D_+)-(D_+-6)\mathcal R\}.
\end{equation}
Since $M>D_+>6$, every positive ratio converges to
$\mathcal R_*=(M-D_+)/(D_+-6)$. Applying \eqref{upper:eq:margin} at $s=r$ shows $\mathcal R_*>R_0$.

Choose a fixed, sufficiently small $\tau_0>0$ so that \eqref{eq:tracking}
applies at $t_0=\tau_0\eps^{-\alpha}$. Equations \eqref{eq:ray} and
\eqref{eq:tracking} put
\[
 y_\eps(t_0):=w_\eps(t_0)-WE
\]
in a fixed compact set, independent of sufficiently small $\eps$.
On this set the initial limiting ratio is bounded above and bounded away
from zero. Choose $R_1$ strictly between $R_0$ and $\mathcal R_*$.
The logistic equation \eqref{upper:eq:logistic} then puts every such limiting
solution above $R_1$ by a single finite clock time $\xi_*$.

Apply the same positive clock factor $C_Le^{-u\cdot y}$ to the rescaled
full equations. Let $\mathcal K_0$ contain their initial points, and let
$\mathcal K_1$ contain all limiting trajectories from $\mathcal K_0$ on
$[0,\xi_*]$. The logistic ratio stays between its initial value and its
positive equilibrium, uniformly over $\mathcal K_0$. Thus these orbits
and their velocities are bounded and $\mathcal K_1$ is compact.
On the closed one-neighbourhood $\mathcal K_2$ of $\mathcal K_1$, the
clock factor is bounded above and away from zero. The transformed full
fields converge uniformly to the smooth limiting field. If their uniform
difference is $\eta_\eps\to0$ and a Lipschitz constant for the limit field
on a containing compact ball is $H_0$, comparison up to first exit gives
\[
 \sup_{0\le \xi\le \xi_*}\|y_\eps(\xi)-y(\xi)\|
 \le\eta_\eps \xi_* e^{H_0 \xi_*}.
\]
For small $\eps$ this is less than one, excluding exit from $\mathcal K_2$.
The initial limiting point is always chosen equal to the full initial
point; convergence of the initial points themselves is not required.

The ratios $Q/F$ converge uniformly on $\mathcal K_2$ to $\mathcal R$,
since $W_b>0$ makes the $S=r$ term dominate the finite sum. The comparison
therefore gives $R>R_0$ at clock time $\xi_*$, uniformly over the allowed
initial points. Finally $u\cdot y$ is bounded above on $\mathcal K_2$,
so $d\tau/d\xi=e^{u\cdot y}/C_L$ has a uniform upper bound. The elapsed
rescaled time is bounded independently of $\eps$. We have therefore reached
$t_e=O(\eps^{-\alpha})$ with $w_\eps(t_e)=WE+O(1)$ and $R>R_0$.
The linear forms $A,D,P$ are strictly positive at $W$, while
$q(W)=\alpha-1$. Recall that $\delta$ was fixed smaller than half of both $A(W)$ and $D(W)$.
Increasing $C_0$ if necessary gives the remaining entrance bounds. This gives
\eqref{upper:eq:entry}. If a probe crossing occurred earlier, the desired upper
bound already holds. The preceding section proves the upper bound. Together with
Theorem~\ref{thm:tracking}, this completes Theorem~\ref{thm:rate}.


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
\begin{figure}[ht]
\centering\includegraphics[width=\textwidth]{../output/figures/correction-time-scaling.pdf}
\caption{First correction times and successive log--log slopes from the
retained numerical runs. Dashed lines show the theorem's exponents. The
finite-range slopes are evidence about convergence, not a proof of it.}
\end{figure}

The companion README records the environment, commands, source snapshot,
and result files. Exact finite checks cover the score inequalities, both
endpoint path counts, the ratio-barrier identity, and the invariant-region
algebra. The theoretical arguments apply to every fixed integer $L\ge4$;
the numerical checks cover only their stated finite ranges.

\section{Scope and remaining questions}
The result concerns exact continuous-time return-gradient ascent, fixed $L$,
and zero initialization. It supplies two-sided order bounds but no sharp
prefactor. A limiting law for Gaussian initializations, the time of permanent
correction, discrete gradient ascent, and sampled policy-gradient updates
remain separate questions. Constants may depend on $L$; no bound uniform
as $L\to\infty$ is asserted. The prefactor suggested by a reduced transition
ODE is exploratory and is not needed for the theorem.

\section*{Acknowledgment}
Computations and draft review used Astra and Claude.

\begin{thebibliography}{9}
\bibitem{a8} MAIS, \emph{A predictive theory of out-of-distribution
generalization: which of two perfect policies does gradient descent select?}
Research agenda MAIS-A8, Definition 3.1 and Section 6.
\href{https://github.com/lionellevine/MAIS/blob/7b23a8a30c0eb0b1d3b55c592ca9554256fc4805/agendas/A8/MAIS-A8.tex}{Source version 7b23a8a}.
\bibitem{o87} R. Sneiderman, \emph{A negative solution to MAIS-O87},
September 2026. \href{https://github.com/lionellevine/MAIS/issues/35}{Submitted candidate, MAIS issue 35}.
\end{thebibliography}
\end{document}


EXTRACTED COMPILED PDF TEXT

         Correction times for linear policy gradient on a coin line
                                               Rob Sneiderman

                                             September 19, 2026


                                                     Abstract
          How long does a rare corrective training signal take to overturn a learned preference for
      moving right? We answer this question for a linear logistic policy on a finite coin line. From zero
      initialization, the first correction time under exact return-gradient flow is of order ε−αL , where ε
      is the training diversity and the explicit exponent αL > 1 depends on the line length and its
      parity. We first determine the zero-diversity trajectory up to a convergent offset. We then prove
      a perturbation bound up to the critical timescale and control the subsequent transition through
      the change of dominant failed paths. Numerical experiments illustrate the asymptotics; they are
      not used in the proofs.


1    Model and results
An agent moves on sites 0, . . . , L, where L ≥ 4, and succeeds on reaching a coin. The initial site is
uniform. Each episode stops on its first success, including at time zero, or after H = 2L actions.
Actions move one site left or right, clipped at the endpoints. At position p with coin c, the policy
moves right with probability

                         σ(zpc ),       zpc = a + bp + dc,        σ(z) = (1 + e−z )−1 .

During training, c ∈ {1, . . . , L} has law µc = (1 − ε)1c=L + ε/L. Let Jc (w) be the conditional success
probability, for w = (a, b, d), and set
                                              L
                                           εX
                    Jε = (1 − ε)JL +             Jc ,      wε′ = ∇Jε (wε ),    wε (0) = 0.
                                           L c=1

This is Euclidean gradient ascent on the exact return. For every training diversity the flow is globally
defined: the return is a finite polynomial in logistic probabilities of linear forms, with bounded
gradient and Hessian. The model and horizon conventions are those of MAIS-A8 [1].
    At the test state the agent is at k = ⌈L/2⌉ and the coin is at zero. The logit Pε = aε + kbε is
positive when the agent favors moving away from the coin. Define its first correction time by

                              Tε = inf{t > 0 : Pε (t) < 0},          inf ∅ = +∞.

This paper quantifies first correction from zero initialization. The earlier O87 note [2] concerns
eventual correction from every finite initialization, without a rate. First correction and permanent
correction are different observables.
    Write

          n = ⌈(L + 1)/2⌉,          r = L + 1 − n,      u = (n, r, nL),   M = ∥u∥2 ,      x = (1, 2, 1),

                                                          1
                                   x·u   n(L + 1) + 2r
                            β=         = 2               ,        α = (1 − β)−1 .
                                   M    n (1 + L2 ) + r2
The coefficient β comes from the corrective training state (2, 1), whose feature vector is x; the test
state is (k, 0). Here r = n for odd L and r = n − 1 for even L. Since r ≤ n and n ≥ 3, we have
0 < β < 1 and α > 1.

Theorem 1. For every fixed integer L ≥ 4, there are positive constants c− , c+ , ε0 such that

                                   c− ε−α ≤ Tε ≤ c+ ε−α       (0 < ε ≤ ε0 ).

In particular, log Tε / log(1/ε) → α as ε ↓ 0.

    Thus correction takes asymptotically longer than 1/ε. For L = 4, 5, 6, the exponents are 157/138,
81/73, and 601/567, respectively. The theorem does not assert convergence of εα Tε to a constant.
    The proof has three parts. First we identify the logarithmic trajectory when all training coins
are at L. Then we bound its perturbation under small diversity, giving the lower bound. For the
upper bound, we keep a finite sum of minimal failed-path scores rather than following just one score
through the transition. A ratio barrier makes the probe decrease while preserving the region in
which that approximation is valid.


2      The zero-diversity trajectory
Set                                               (
                                                  (L + 1)−1 , L odd,
                                       CL =               −1
                                                  n(L + 1) , L even.

Theorem 2. There is w∞ ∈ R3 , with u · w∞ = log(CL M ), such that
                                   u                                               1
                        w0 (t) =     log t + w∞ + o(1),        1 − JL (w0 (t)) ∼      .             (1)
                                   M                                               Mt
Also tw0′ (t) → u/M .

      For this section only, write w = w0 , JL for its return, and zp = zpL .

2.1      The cone containing the trajectory
For the moment, regard the nonterminal logits as independent. Their success derivatives κp =
∂JL /∂zp are strictly positive. Here is a direct justification. Let Vj (p) be the probability of hitting
L within j actions and let ρi (p) be the probability of occupying p at time i before stopping.
Differentiating the finite Bellman recursion gives
                                      H−1
                                      X
                 κp = σ(zp )σ(−zp )         ρi (p)[VH−i−1 (p + 1) − VH−i−1 (max(p − 1, 0))].
                                      i=0

Every bracket is nonnegative: from the farther site a path must first hit the nearer site, and reducing
the remaining horizon cannot improve success. For strictness, put j = H −1, p− = max(p−1, 0), and
let τ be the first visit to p + 1 starting at p− . First-passage decomposition and horizon monotonicity
give
                                 Vj (p− ) ≤ Pr(τ ≤ j)Vj (p + 1) < Vj (p + 1).
                                             p−


                                                       2
The last inequality is strict because taking left at every step avoids p + 1 with positive probability,
whereas Vj (p + 1) > 0 by taking right until success. Since ρ0 (p) = 1/(L + 1), strict positivity follows.
   The chain rule now gives

                         a′ =                       b′ =                          d′ = La′ .
                                X                          X
                                      κp > 0,                    pκp > 0,
                                p<L                        p<L

Thus, along the trajectory,

                    d = La,           0 ≤ b ≤ (L − 1)a,           h := a + Ld = (1 + L2 )a.           (2)

In particular h − b ≥ (L2 − L + 2)a. The flow exists for all time because its vector field is bounded
and globally Lipschitz: the return is a finite polynomial in logistic probabilities of linear forms,
whose first and second derivatives are bounded. Also a(t) → ∞. Otherwise (2) and monotonicity
would make all coordinates converge to a finite point, at which a′ > 0. Continuity would then
contradict convergence of a.

2.2   Failed paths and their scores
Let Ω consist of all pairs of a nonterminal starting site and a length-H action sequence that never
reaches L. For ω ∈ Ω, let N count its left actions, let N0 count left actions taken at zero, and let S
be the sum of the sites at which left actions are taken. Write pj for its position before action j and
set
                                 vω = (N, S, LN ),      xp = (1, p, L).
Its conditional probability, given its starting site, is exactly
                                                                       H−1
                       Pω (w) = e−vω ·w Dω (w),                              (1 + e−zpj )−1 .
                                                                       Y
                                                           Dω (w) =                                   (3)
                                                                       j=0

Consequently F := 1 − JL = (L + 1)−1
                                                P
                                                ω Pω and

                                                                          H−1
                               1 X
                       w′ =
                                                                          X
                                    Pω (vω − Eω ),                 Eω =           σ(−zpj )xpj .       (4)
                              L+1 ω                                         j=0

On the cone (2), zp ≥ h, so, uniformly over this finite path set,

                       Dω = 1 + O(e−h ),            ∥Eω ∥ = O(e−h ),              Dω ≥ 2−H .          (5)

All constants below may depend on L.
    There are no clipped right actions on a failed path. Hence

                                      pH = p0 + 2L − 2N + N0 ≤ L − 1.

It follows that N ≥ n and

                              S ≥ N − N0 ≥ L + 1 + p0 − N ≥ L + 1 − N.

Since n + r = L + 1, the score difference satisfies

                       (vω − u) · w = (N − n)(h − b) + (N + S − n − r)b ≥ 0.                          (6)

                                                           3
Both coefficients on the right are nonnegative integers.
    The score (N, S) = (n, r) is attained, and its multiplicity is explicit. If L is odd, r = n and the
endpoint inequality forces p0 = N0 = 0. All left actions must be taken at site one: a left at site
two or higher would make S > n. Once the walk reaches site two or higher, it cannot take another
left action without violating this restriction. Thus all left actions precede a final monotone right
run. The unique path consists of n right-left cycles from zero followed by right actions to site L − 1.
If L is even, r = n − 1. The inequality S ≥ N − N0 forces N0 ≥ 1, and the endpoint inequality
forces N0 = 1 and p0 = 0. Every other left action is at site one, since a left at site two or higher
would make S > n − 1. Again, reaching site two forces the remaining actions to be right, so these
possibilities are exhaustive. There are n paths: place the one left self-loop in any of the n slots
before, between, or after the n − 1 right-left cycles, then finish with right actions. This proves the
coefficient CL in the theorem.

2.3   Separation of the dominant paths
To use (6), we must show that b also diverges. Let F> be the contribution to F from paths with
N > n. Each has a score gap at least h − b. Comparing with one path of score u, using (3)–(5),
gives
                                        F>
                                            = O(e−(h−b) ) −→ 0.                                       (7)
                                        F
For the remaining paths, S ≥ r. The b component of (4), together with S ≥ 0 on all paths, therefore
gives
                                                                       r
                               b′ ≥ r(F − F> ) − H(L − 1)e−h F ≥ F
                                                                       2
for sufficiently large time. The a component gives 0 < a ≤ HF . Thus b′ ≥ (r/(2H))a′ eventually.
                                                            ′

After integration,
                                                 r
                                           b≥       a − O(1).
                                               2H
In particular, b → ∞ and b ≥ (r/(4H))a eventually.
    For a path with vω ̸= u, at least one of the integer coefficients in (6) is positive. The cone bound
and the preceding estimate therefore give a constant γ > 0 such that its score gap is at least γa at
sufficiently late times. Summing the finite path set in (3) and (4), and using (5), yields

                              F = CL e−U 1 + O(e−γa ) ,
                                                        
                                                                                                     (8)
                             w′ = CL e−U u + O(e    −γa 
                                                       ) ,     U = u · w.                            (9)

Here and below γ may be reduced to absorb the denominator errors. The error in the second line is
a vector error in Euclidean norm.

2.4   Integrating the asymptotic flow
Since a′ > 0 and a → ∞, we may use a as the independent variable. Equation (9) gives

                                          dw  u
                                             = + O(e−γa ).
                                          da  n
The error is integrable. There is therefore a vector v such that
                                             u
                                       w=      a + v + O(e−γa ).                                    (10)
                                             n


                                                   4
Taking the inner product of (9) with u gives
                                d U
                                   e = CL M 1 + O(e−γa ) −→ CL M.
                                                        
                                dt
It follows by integration that eU /t → CL M , and hence

                                      U = log t + log(CL M ) + o(1).

Combining this with (10) proves
                           u             u
                                                                        
                                                             
                        w=   log t + v +   log(CL M ) − u · v + o(1).
                           M             M
The bracket is w∞ and has the required inner product with u. Finally, (8) and (9) give the return
and velocity limits in Theorem 2.


3     Tracking and the lower bound
Theorem 3. There are K, c, ε0 > 0 such that for 0 < ε ≤ ε0 ,

                     ∥wε (t) − w0 (t)∥ ≤ Kε((1 + t)1−β − 1),           0 ≤ t ≤ cε−α .             (11)

The constants can be chosen so that Pε (t) > 0 for every 0 < t ≤ cε−α .

3.1      The diversity perturbation
Write
                                                           L
                                                        1X
                            ∇Jε = ∇JL + εG,          G=       ∇Jc − ∇JL .
                                                        L c=1
Fix a radius R > 0. All estimates in this section are uniform for ∥w − w0 (t)∥ ≤ R, with constants
allowed to depend on L, R. By (1) and boundedness on finite time intervals,
                           n + pr + cnL
               zpc (w) =                log(1 + t) + OR (1)     (0 ≤ p ≤ L, 1 ≤ c ≤ L).           (12)
                                M
Define
                                    n + cnL              n + (c + 1)r + cnL
                             θc =           ,     βc =                      .
                                       M                         M
Thus θc ≥ θ1 and βc ≥ β1 = β.

Lemma 1. For a fixed coin, any event consisting of stopped action paths of at most H actions has
at most (L + 1)2H paths, including their starting sites. Each path probability pω satisfies
                                                    p
                                        ∥∇pω ∥ ≤ H 1 + 2L2 pω .

Thus a common bound on these probabilities bounds the gradient of the event probability, up to a
constant depending only on L.

Proof. The paths are prefix-free at each starting site and may be injected into length-H action
words. An action score is either σ(−zpc )(1, p, c) or −σ(zpc )(1, p, c); summing at most H such scores
gives the displayed bound. Sum over the finite event.

                                                    5
    For a start below c, differentiate failure rather than success. Every failed path stays below c. If
it has N− left actions, clipping at zero gives pH ≥ p0 + 2L − 2N− . Since pH ≤ c − 1,

                                         2L + p0 − c + 1
                                                                  
                                    N− ≥                 ≥ n.
                                                2

By (12), each left-action probability below c is at most CR (1 + t)−θc . The failed-path probability
and its summed gradient are therefore OR ((1 + t)−nθc ).
    For a start above c, differentiate success. Every successful path includes a left action from c + 1.
Its probability is at most CR (1 + t)−βc by (12); all other action factors are at most one. Summing
the finite set of stopped successful paths gives a gradient bound OR ((1 + t)−βc ). There is no such
starting site when c = L, and a start at c has zero derivative.
    Finally,
                                            n(n − 1)(L + 1) − 2r
                                 nθ1 − β =                         > 0.
                                                      M
Both parts of every conditional-return gradient are thus bounded by CR (1 + t)−β . We have proved

                            ∥G(w)∥ ≤ CR (1 + t)−β          if ∥w − w0 (t)∥ ≤ R.                      (13)

3.2   An integrable one-sided Hessian bound
A norm bound on the entire Hessian would discard the sign of its leading term. We retain that sign
using the failed-path representation for coin L. For each failed path ω, let Pω be its conditional
probability given its starting site, and put gω = ∇ log Pω . Then
                                                      X
                    ∇2 log Pω = −Bω ,          Bω =        σ(zpj ,L )σ(−zpj ,L )xpj ,L xT
                                                                                        pj ,L ,
                                                       j

where xp,L = (1, p, L) and the sum has H terms. Since 1 − JL = (L + 1)−1
                                                                                         P
                                                                                            ω Pω ,

                                  1 X                       1 X
                       ∇2 JL =         Pω (Bω − gω gωT ) ⪯       Pω Bω .                             (14)
                                 L+1 ω                     L+1 ω

The ordering is that of symmetric quadratic forms.
    Set κ = n(1 + L2 )/M > 0. Equation (12) gives zp,L ≥ κ log(1 + t) − CR , and hence Bω ⪯
CR (1 + t)−κ I. Also the bound on path scores gives
                                                   √
                                                       1+2L2
                                    Pω (w) ≤ eRH               Pω (w0 (t)).

Summing and using (1), we obtain 1 − JL (w) ≤ CR (1 + t)−1 . It follows from (14) that
                                                                              Z ∞
             ∇2 JL (w) ⪯ KR (t)I,       KR (t) = CR (1 + t)−1−κ ,                   KR (t) dt < ∞.   (15)
                                                                                0

These bounds hold for all t ≥ 0 after increasing the constants on a compact initial interval. In
particular, no assumption about the perturbed trajectory remaining in the zero-diversity invariant
cone is needed.




                                                      6
3.3    Tracking and the first crossing
Let ∆(t) = ∥wε (t) − w0 (t)∥ and stop the comparison if ∆ first reaches R. The line segment between
the two parameters lies in the same radius-R ball. Integrating (15) along that segment and using
(13) gives, while ∆ < R,
                                   ∆′ ≤ KR (t)∆ + εCR (1 + t)−β .
At ∆ = 0 this is understood as an upper right derivative; equivalently, one may regularize the norm.
Grönwall’s inequality and integrability of KR yield a finite constant AR such that

                                      ∆(t) ≤ AR ε (1 + t)1−β − 1 .
                                                                              
                                                                                                          (16)

Consider
                                                         1/(1−β)
                                                   R
                                                           
                                     Sε = 1 +                    − 1.
                                                 2AR ε
If the first exit occurred at or before Sε , continuity and (16) would imply R ≤ R/2. Thus there is
no exit, and (16) holds through Sε , and
                                                            α
                                                       R
                                                  
                                           Sε ∼                     ε−α .
                                                      2AR
   To ensure a positive probe, put v∗ = (1, k, 0). Since a′0 , b′0 > 0, P0 is strictly increasing from zero.
Choose
                                                        P0 (1)
                                                                 
                                    0 < R ≤ min 1,                  .
                                                        2∥v∗ ∥
For 1 ≤ t ≤ Sε , the tracking bound ∆ ≤ R/2 gives Pε (t) ≥ P0 (1) − ∥v∗ ∥R/2 > 0. On 0 ≤ t ≤ 1, let
m = min[0,1] P0′ > 0. Concavity of (1 + t)1−β implies ∆(t) ≤ AR ε(1 − β)t, so
                                                                
                         Pε (t) ≥ m − ∥v∗ ∥AR ε(1 − β) t > 0                      (0 < t ≤ 1)

for sufficiently small ε. Reduce εL so that Sε ≥ 1, and choose cL > 0 with cL ε−α ≤ Sε throughout
the remaining range. Equation (16) and these positivity bounds prove Theorem 3.


4     The upper bound
Write E = log(1/ε) and W = αu/M throughout this section. We first find a region in which a finite
failed-path sum gives a uniform approximation to the flow. We then prove that the trajectory enters
that region with enough corrective drift to force a crossing.

4.1    An approximation through the sign change
Put
            A = a + d − b,        D = d − a,          q = a + 2b + d = x · w,               h = a + Ld.
Fix δ > 0 smaller than half of both A(W ) and D(W ); these quantities are positive. All subsequent
constants may depend on this choice. Consider the region

                                   A ≥ δE,        D ≥ δE,                   P ≥ 0.                        (17)

Every training logit in this region is at least δE. Indeed, if b ≥ 0, then d = (A + D + b)/2 > 0 and
a + d = A + b ≥ δE. If b < 0, a ≥ −kb, d = a + D > 0, and

                          a + Lb + d = 2a + Lb + D ≥ (L − 2k)b + D ≥ δE.

                                                       7
Also
                                            b + d ≥ δE.                                         (18)
For b ≥ 0, use b + d = (A + D + 3b)/2; for b < 0, use b + d = D + a + b ≥ D + (1 − k)b. In
particular q = z2,1 ≥ δE, since (2, 1) is a training state. Equivalently, q = A + 3b for b ≥ 0, and
q = 2a + 2b + D ≥ 2(1 − k)b + D for b < 0.
   For each failed length-2L path with coin L, let N be its number of left actions and S the sum of
the sites at those actions. The path count in Section 2 gives

                     N ≥ n,       N + S ≥ L + 1 = n + r,       S ≤ N (L − 1).

Let mS be the number of such paths, including their starting sites, with N = n and position sum S.
Define the positive exponential sum
                      n(L−1)
                 e−nh X                               SmS e−Sb
                                                   P
         F (w) =             mS e−Sb ,      s(b) = PS     −Sb
                                                               ,       z(b) = (n, s(b), nL).    (19)
                 L + 1 S=r                            S mS e

Then −∇F = F z and r ≤ s(b) ≤ n(L − 1). The endpoint counts mr and mn(L−1) are positive, as
justified below. The following path facts will also be used. From any start p0 < c, a failed path
stays below c and satisfies p0 + 2L − 2N− ≤ p2L ≤ c − 1. Thus

                                 N− ≥ ⌈(2L + p0 − c + 1)/2⌉ ≥ n.

Every successful path starting above c must take a left action at c + 1. For c = 1, the only such
path with one left action is the immediate step from site 2: any larger start or any preceding right
action requires another left action before reaching the coin. The endpoint score S = n(L − 1)
is attained from start zero by climbing to L − 1, then taking (left, right)n for odd L; for even
L, take (left, right)n−1 followed by one left. The lengths are respectively L − 1 + 2n = 2L and
L − 1 + 2n − 1 = 2L. Both paths fail. Positivity of mr follows from the explicit paths used in the
zero-diversity trajectory proof.
    Set
                                                   ε
                                       Q(w) =            e−q .                                  (20)
                                                L(L + 1)
Lemma 2. Uniformly in (17),

                      ∇Jε = F z − Qx + E,        ∥E∥ ≤ C(ε + e−δE )(F + Q).                     (21)

Proof. For each fixed coin and starting site, success and failure probabilities sum to one. We may
therefore differentiate success from above and the negative of failure from below. Starts at the coin
have zero derivative. We treat the entire coin-L contribution first, and use this decomposition only
for the remaining coins 1 ≤ c < L, so no term is counted twice.
    A failed path for coin L has probability e−N h−Sb times a product of 2L logistic denominators.
Since every logit is at least δE, these denominators equal 1 + O(e−δE ); their logarithmic gradients
are O(e−δE ). These estimates are uniform over the finite path set.
    Paths with N > n have a score gap of at least δE relative to one of the endpoint scores in (19).
For b ≥ 0, write

                   N h + Sb − (nh + rb) = (N − n)(h − b) + (N + S − n − r)b,

where h − b = ((L + 1)A + (L − 1)D + (L − 1)b)/2 ≥ δE. For b < 0, write

              N h + Sb − n[h + (L − 1)b] = (N − n)[h + (L − 1)b] + [S − N (L − 1)]b,

                                                 8
where h+(L−1)b = zL−1,L ≥ δE. Thus their probabilities and gradient contributions are O(e−δE F ).
The coin-L term is F z + O((ε + e−δE )F ) after its mixture weight is included.
     For a start above coin 1, the unique successful path with only one left action is the immediate
left step from site 2. Its gradient, with both initial-site and coin weights, is −Qx + O(e−δE Q). Every
other successful path from above includes that left step and at least one further left action. Its
probability is at most e−q−δE . The norm of a path’s logarithmic gradient is uniformly bounded, so
its gradient obeys the same estimate up to a constant.
     For coins 2 ≤ c < L, success from above requires a left action at c+1. Its logit is q+(c−1)(b+d) ≥
q + δE, by (18). Finally, for the remaining coins 1 ≤ c < L, failure from below requires at least n
left actions. If b ≥ 0, its minimum below-coin logit is a + dc ≥ a + d = A + b, and

                               n(a + d) − q = (n − 1)A + (n − 3)b ≥ δE.

If b < 0, that minimum is a + (c − 1)b + dc = q + (c − 1)(b + d) − 2b ≥ q, so n copies exceed q by at
least δE. Differentiate these below-coin contributions through their failure probabilities. Summing
all the finitely many paths proves the lemma.

4.2   A ratio barrier
Define R = Q/F and R0 = nL/2. For z = (n, s, nL), set Ms = ∥z∥2 and Ds = z · x = n(L + 1) + 2s.
The exact logarithmic derivatives of F, Q imply

                (log R)′ = (z − x) · ∇Jε = F {Ms − Ds − (Ds − 6)R} + (z − x) · E.                 (22)

At R = R0 , the expression in braces is
                                                                      !
                           2                       2        L2 − L
                          s − (nL + 2)s + n              1+                + n(2L − 1).
                                                               2

Its minimum over all real s is
                                                         !
                                     2      L2 L
                                 n       1+   −              + n(L − 1) − 1 > 0.                  (23)
                                            4   2

For sufficiently small ε, Lemma 2 therefore makes R′ > 0 at R = R0 , throughout (17). A trajectory
entering with R > R0 cannot cross down through this barrier while in the region.
   For R ≥ R0 , we have
                               Ds     2                  n + ks
                                  −6≤− ,                        − (1 + 2k) ≤ −1.
                               R      L                    R
Using (21), and reducing the permitted ε if needed,

                                                   Q                      Q
                                          q′ ≤ −     ,           P′ ≤ −     .                     (24)
                                                   L                      2
The two other linear coordinates satisfy

                         A′ ≥ −CζQ,           D′ ≥ −CζQ,                   ζ = ε + e−δE .         (25)

Indeed, the −Qx contribution is zero in both coordinates, and the F z contributions are F [n(L +
1) − s] ≥ 2nF and F n(L − 1) > 0. The error is O(ζQ) since F ≤ Q/R0 .

                                                             9
   Suppose the flow enters at time te with

                    A, D ≥ 2δE,       0 < P ≤ C0 E,      R > R0 ,        q ≤ (α − 1)E + C0 .                 (26)

Define t∗ to be the first time after te at which A = δE, D =R δE, R = R0 , or P = 0. Before this
time all preceding estimates hold. For any such t, (24) gives tte Q du ≤ 2P (te ) ≤ 2C0 E. By (25),

                                     A(t), D(t) ≥ 2δE − 2CC0 ζE > δE

for sufficiently small ε. These inequalities also hold at a finite t∗ by continuity. The alternative
R(t∗ ) = R0 is impossible because R′ > 0 there, whereas a first crossing from above would have
R′ ≤ 0. Hence any finite t∗ is a probe zero. If t∗ = ∞, the same estimates hold for all later times,
which the following time bound rules out. But (24) also gives
                                                             ε
                                           (eq )′ ≤ −                .
                                                        L2 (L + 1)

A positive eq cannot satisfy this inequality for more than L2 (L + 1)eq(te ) /ε = O(ε−α ) time. The
probe must therefore reach zero within that time. Since P ′ < 0 at this first zero, it crosses into
P < 0 immediately. It remains to establish the entrance conditions (26) at te = O(ε−α ).

4.3     Reaching the ratio barrier
For y in a fixed compact set, W E + y lies in the region (17) for all sufficiently large E: the forms
A, D, P are strictly positive at W , and A(W ), D(W ) > 2δ. Also Wb > 0, so the finite sum in (19)
is uniformly dominated by its S = r term. Consequently,
                                                                                                   1
      ε−α F (W E + y) → CL e−u·y ,       s(b) → r,         ε−α Q(W E + y) = Be−x·y ,       B=            .
                                                                                                L(L + 1)

Here u · W = α, x · W = α − 1, and CL = mr /(L + 1) > 0 was computed in Section 2. Lemma 2
now gives the uniform compact-set limit

                             ε−α ∇Jε (W E + y) −→ CL ue−u·y − Bxe−x·y .                                      (27)

Indeed, its rescaled error is bounded by a constant times (ε + e−δE )ε−α (F + Q), which tends
uniformly to zero. Thus all path classes are controlled by the same estimate used after entrance.
    In time τ = εα t, the limiting equation for y is the right side of (27). Write U = u · y, qy = x · y,
D+ = u · x, and introduce a second clock by dξ/dτ = CL e−U . In this clock the limiting equation
and ratio are
              dy                        B U −qy            dR
                 = u − Rx,        R=       e    ,             = R{(M − D+ ) − (D+ − 6)R}.                    (28)
              dξ                        CL                 dξ
Since M > D+ > 6, every positive ratio converges to R∗ = (M − D+ )/(D+ − 6). Applying (23) at
s = r shows R∗ > R0 .
    Choose a fixed, sufficiently small τ0 > 0 so that (11) applies at t0 = τ0 ε−α . Equations (1) and
(11) put
                                       yε (t0 ) := wε (t0 ) − W E
in a fixed compact set, independent of sufficiently small ε. On this set the initial limiting ratio is
bounded above and bounded away from zero. Choose R1 strictly between R0 and R∗ . The logistic
equation (28) then puts every such limiting solution above R1 by a single finite clock time ξ∗ .

                                                      10
    Apply the same positive clock factor CL e−u·y to the rescaled full equations. Let K0 contain their
initial points, and let K1 contain all limiting trajectories from K0 on [0, ξ∗ ]. The logistic ratio stays
between its initial value and its positive equilibrium, uniformly over K0 . Thus these orbits and their
velocities are bounded and K1 is compact. On the closed one-neighbourhood K2 of K1 , the clock
factor is bounded above and away from zero. The transformed full fields converge uniformly to the
smooth limiting field. If their uniform difference is ηε → 0 and a Lipschitz constant for the limit
field on a containing compact ball is H0 , comparison up to first exit gives

                                    sup ∥yε (ξ) − y(ξ)∥ ≤ ηε ξ∗ eH0 ξ∗ .
                                  0≤ξ≤ξ∗

For small ε this is less than one, excluding exit from K2 . The initial limiting point is always chosen
equal to the full initial point; convergence of the initial points themselves is not required.
    The ratios Q/F converge uniformly on K2 to R, since Wb > 0 makes the S = r term dominate
the finite sum. The comparison therefore gives R > R0 at clock time ξ∗ , uniformly over the allowed
initial points. Finally u · y is bounded above on K2 , so dτ /dξ = eu·y /CL has a uniform upper bound.
The elapsed rescaled time is bounded independently of ε. We have therefore reached te = O(ε−α )
with wε (te ) = W E + O(1) and R > R0 . The linear forms A, D, P are strictly positive at W , while
q(W ) = α − 1. Recall that δ was fixed smaller than half of both A(W ) and D(W ). Increasing C0 if
necessary gives the remaining entrance bounds. This gives (26). If a probe crossing occurred earlier,
the desired upper bound already holds. The preceding section proves the upper bound. Together
with Theorem 3, this completes Theorem 1.


5    Numerical evidence and reproduction
The companion code evaluates the return and its gradient by finite-horizon dynamic programming.
It propagates both success and failure probabilities and uses the less saturated value difference in
the gradient recursion. Independent rational path enumeration checks the implementation, including
a saturated-policy case. No Monte Carlo return estimates are used.
    We integrated the flow from zero for L = 4, 5, 6 and ε = 10−p , using

                                 p ∈ {2, 4, 8, 12, 16, 24, 32, 48, 64, 96}.

All thirty runs reached a downward probe crossing. Integration used the clock s = log(1 + t)
and DOP853 with relative tolerance 2 × 10−9 . Six repeats with RK45 and relative tolerance
2 × 10−11 changed crossing times by at most 2.20 × 10−10 in relative terms. Independent 180-digit
differentiation at the three ε = 10−96 crossing states agreed with the computed gradients to relative
error below 4.6 × 10−14 . These checks are not certified integration bounds.

                        L   Theorem exponent        Secant slope, 10−64 to 10−96
                        4       1.137681159                  1.138261638
                        5       1.109589041                  1.110163109
                        6       1.059964727                  1.061551262

     The companion README records the environment, commands, source snapshot, and result
files. Exact finite checks cover the score inequalities, both endpoint path counts, the ratio-barrier
identity, and the invariant-region algebra. The theoretical arguments apply to every fixed integer
L ≥ 4; the numerical checks cover only their stated finite ranges.


                                                    11
                                                                                                                        Dashed: predicted exponents
                                         L=4                                                                                                                      L=4
                               100       L=5                                                            1.35                                                      L=5
                                         L=6                                                                                                                      L=6
                                                                                                        1.30




log10(first correction time)
                               80



                                                                                  Local log-log slope
                                                                                                        1.25
                               60
                                                                                                        1.20
                               40
                                                                                                        1.15
                               20
                                                                                                        1.10
                                0                                                                       1.05
                                     0         20      40          60      80   100                            0   10   20       30 40 50 60                 70    80
                                                    log10(1 / diversity)                                                     Midpoint log10(1 / diversity)

      Figure 1: First correction times and successive log–log slopes from the retained numerical runs.
      Dashed lines show the theorem’s exponents. The finite-range slopes are evidence about convergence,
      not a proof of it.


      6                              Scope and remaining questions
     The result concerns exact continuous-time return-gradient ascent, fixed L, and zero initialization. It
     supplies two-sided order bounds but no sharp prefactor. A limiting law for Gaussian initializations,
     the time of permanent correction, discrete gradient ascent, and sampled policy-gradient updates
     remain separate questions. Constants may depend on L; no bound uniform as L → ∞ is asserted.
     The prefactor suggested by a reduced transition ODE is exploratory and is not needed for the
     theorem.


      Acknowledgment
      Computations and draft review used Astra and Claude.


      References
      [1] MAIS, A predictive theory of out-of-distribution generalization: which of two perfect policies
          does gradient descent select? Research agenda MAIS-A8, Definition 3.1 and Section 6. Source
          version 7b23a8a.

      [2] R. Sneiderman, A negative solution to MAIS-O87, September 2026. Submitted candidate, MAIS
          issue 35.




                                                                                 12
