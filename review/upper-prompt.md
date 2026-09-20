O87 upper bound | fresh adversarial mathematical review | 2026-09-19

Review the following proof from scratch. Treat its two explicitly stated input estimates (zero-diversity ray and tracking) as hypotheses, and decide whether the upper bound follows. Focus on uniformity for unbounded w in the region A,D>=delta log(1/eps), P>=0; every failed and successful path class; the smooth sum of all minimal-left-count paths; the ratio barrier; invariant-region preservation; and the compact rescaled entrance argument. Try hard to find a counterexample or missing estimate. Return a precise verdict and anchored gaps/fixes; distinguish mathematical gaps from notation/exposition. No numerical checks have been supplied and you must not claim to run any. No tools are enabled. The author intends to combine this with the two input proofs, but no new publication has happened.

\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}\usepackage{lmodern,microtype}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}\newtheorem{lemma}{Lemma}
\newcommand{\eps}{\varepsilon}\newcommand{\R}{\mathbb R}
\title{The correction-time upper bound in the coin-line model}
\author{Rob Sneiderman}\date{September 19, 2026}
\begin{document}\maketitle
\begin{abstract}
We complete the correction-time estimate for the linear coin-line return-gradient
flow from zero initialization. Keeping all failed paths with the minimum number
of left actions gives an approximation valid through the change of sign of the
position coefficient. A ratio barrier forces the probe to correct in a bounded
multiple of the critical timescale. Together with the companion lower bound,
this gives a two-sided power law, with an explicit parity-dependent exponent.
\end{abstract}

\section{Statement and inputs}
Use the model and notation of the companion trajectory and lower-bound notes:
$L\ge4$, horizon $2L$, logistic features $(1,p,c)$, uniform initial position,
coin probabilities $(1-\eps)\mathbf1_{c=L}+\eps/L$, and Euclidean ascent
from $w=(a,b,d)=0$. Write $J_c$ for conditional return and $J_\eps$ for
training return. Set
\[
 k=\lceil L/2\rceil,\quad P=a+kb,\quad
 T_\eps=\inf\{t>0:P(w_\eps(t))<0\},
\]
\[
 n=\lceil(L+1)/2\rceil,\quad r=L+1-n,\quad u=(n,r,nL),\quad
 M=\|u\|^2,\quad x=(1,2,1),
\]
\[
 \beta=\frac{x\cdot u}{M},\quad \alpha=(1-\beta)^{-1},\quad
 E=\log(1/\eps),\quad W=\frac{\alpha u}{M}.
\]
The inputs from the companion notes are the zero-diversity asymptotic
\begin{equation}\label{eq:ray}
 w_0(t)=\frac uM\log t+v+o(1)
\end{equation}
and the tracking estimate, for some $K,c>0$,
\begin{equation}\label{eq:tracking}
 \|w_\eps(t)-w_0(t)\|
 \le K\eps((1+t)^{1-\beta}-1),\qquad 0\le t\le c\eps^{-\alpha}.
\end{equation}
The preceding lower bound is $T_\eps\ge c_-\eps^{-\alpha}$.
\begin{theorem}\label{thm:upper}
For every fixed $L\ge4$, there are $c_+,\eps_0>0$ such that
$T_\eps\le c_+\eps^{-\alpha}$ for $0<\eps\le\eps_0$. Consequently,
\[
 T_\eps=\Theta_L(\eps^{-\alpha}),\qquad
 \lim_{\eps\downarrow0}\frac{\log T_\eps}{\log(1/\eps)}=\alpha.
\]
\end{theorem}
No limiting prefactor is claimed. All constants may depend on $L$.

\section{An approximation that includes the sign change of $b$}
Put
\[
 A=a+d-b,\qquad D=d-a,\qquad q=a+2b+d=x\cdot w,\qquad h=a+Ld.
\]
For fixed $\delta>0$, consider the region
\begin{equation}\label{eq:region}
 A\ge\delta E,\qquad D\ge\delta E,\qquad P\ge0.
\end{equation}
Every training logit in this region is at least $\delta E$. Indeed, if
$b\ge0$, then $d=(A+D+b)/2>0$ and $a+d=A+b\ge\delta E$.
If $b<0$, $a\ge-kb$, $d=a+D>0$, and
\[
 a+Lb+d=2a+Lb+D\ge(L-2k)b+D\ge\delta E.
\]
Also
\begin{equation}\label{eq:bd}
 b+d\ge\delta E.
\end{equation}
For $b\ge0$, use $b+d=(A+D+3b)/2$; for $b<0$, use
$b+d=D+a+b\ge D+(1-k)b$.

For each failed length-$2L$ path with coin $L$, let $N$ be its number of
left actions and $S$ the sum of the sites at those actions. The path count
in the trajectory note gives
\[
 N\ge n,\qquad N+S\ge L+1=n+r,\qquad S\le N(L-1).
\]
Let $m_S$ be the number of such paths, including their starting sites,
with $N=n$ and position sum $S$. Define the positive exponential sum
\begin{equation}\label{eq:F}
 F(w)=\frac{e^{-nh}}{L+1}\sum_{S=r}^{n(L-1)}m_S e^{-Sb},\qquad
 s(b)=\frac{\sum_S S m_S e^{-Sb}}{\sum_S m_S e^{-Sb}},\qquad
 z(b)=(n,s(b),nL).
\end{equation}
Then $-\nabla F=Fz$ and $r\le s(b)\le n(L-1)$. The endpoint counts
$m_r>0$ and $m_{n(L-1)}>0$ were established in the trajectory and transition
calculations; only positivity, not their values, is needed below.
Set
\begin{equation}\label{eq:Q}
 Q(w)=\frac{\eps}{L(L+1)}e^{-q}.
\end{equation}

\begin{lemma}\label{lem:uniform}
Uniformly in \eqref{eq:region},
\begin{equation}\label{eq:approx}
 \nabla J_\eps=Fz-Qx+\mathcal E,\qquad
 \|\mathcal E\|\le C(\eps+e^{-\delta E})(F+Q).
\end{equation}
\end{lemma}
\begin{proof}
A failed path for coin $L$ has probability
$e^{-Nh-Sb}$ times a product of $2L$ logistic denominators. Since every
logit is at least $\delta E$, these denominators equal $1+O(e^{-\delta E})$;
their logarithmic gradients are $O(e^{-\delta E})$. These estimates are
uniform over the finite path set.

Paths with $N>n$ have a score gap of at least $\delta E$ relative to one
of the endpoint scores in \eqref{eq:F}. For $b\ge0$, write
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

For coins $c\ge2$, success from above requires a left action at $c+1$.
Its logit is $q+(c-1)(b+d)\ge q+\delta E$, by \eqref{eq:bd}.
Finally, failure from below any coin requires at least $n$ left actions.
If $b\ge0$, its minimum below-coin logit is $a+dc\ge a+d=A+b$, and
\[
 n(a+d)-q=(n-1)A+(n-3)b\ge\delta E.
\]
If $b<0$, that minimum is
$a+(c-1)b+dc=q+(c-1)(b+d)-2b\ge q$, so $n$ copies exceed $q$ by at
least $\delta E$. Differentiate these below-coin contributions through their
failure probabilities. Summing all the finitely many paths proves the lemma.
\end{proof}

\section{A ratio barrier}
Define $R=Q/F$ and $R_0=nL/2$. For $z=(n,s,nL)$, set
$M_s=\|z\|^2$ and $D_s=z\cdot x=n(L+1)+2s$. The exact logarithmic
derivatives of $F,Q$ imply
\begin{equation}\label{eq:ratio}
 (\log R)'=(z-x)\cdot\nabla J_\eps
 =F\{M_s-D_s-(D_s-6)R\}+(z-x)\cdot\mathcal E.
\end{equation}
At $R=R_0$, the expression in braces is
\[
 s^2-(nL+2)s+n^2\left(1+\frac{L^2-L}{2}\right)+n(2L-1).
\]
Its minimum over all real $s$ is
\begin{equation}\label{eq:margin}
 n^2\left(1+\frac{L^2}{4}-\frac L2\right)+n(L-1)-1>0.
\end{equation}
For sufficiently small $\eps$, Lemma~\ref{lem:uniform} therefore makes
$R'>0$ at $R=R_0$, throughout \eqref{eq:region}. A trajectory entering
with $R>R_0$ cannot cross down through this barrier while in the region.

For $R\ge R_0$, we have
\[
 \frac{D_s}{R}-6\le-\frac2L,\qquad
 \frac{n+ks}{R}-(1+2k)\le-1.
\]
Using \eqref{eq:approx}, and reducing the permitted $\eps$ if needed,
\begin{equation}\label{eq:decrease}
 q'\le-\frac QL,\qquad P'\le-\frac Q2.
\end{equation}
The two other linear coordinates satisfy
\begin{equation}\label{eq:preserve}
 A'\ge-C\zeta Q,\qquad D'\ge-C\zeta Q,
 \qquad \zeta=\eps+e^{-\delta E}.
\end{equation}
Indeed, the $-Qx$ contribution is zero in both coordinates, and the $Fz$
contributions are $F[n(L+1)-s]\ge2nF$ and $Fn(L-1)>0$. The error is
$O(\zeta Q)$ since $F\le Q/R_0$.

Suppose the flow enters at time $t_e$ with
\begin{equation}\label{eq:entry}
 A,D\ge2\delta E,\quad 0<P\le C_0E,\quad R>R_0,
 \quad q\le(\alpha-1)E+C_0.
\end{equation}
Before the probe reaches zero, \eqref{eq:decrease} gives
$\int_{t_e}^tQ\,du\le2P(t_e)\le2C_0E$. Equations \eqref{eq:preserve}
then show that neither $A$ nor $D$ can fall to $\delta E$ when $\eps$ is
sufficiently small. Thus the region and ratio barrier persist until correction.
But \eqref{eq:decrease} also gives
\[
 (e^q)'\le-\frac{\eps}{L^2(L+1)}.
\]
A positive $e^q$ cannot satisfy this inequality for more than
$L^2(L+1)e^{q(t_e)}/\eps=O(\eps^{-\alpha})$ time. The probe must
therefore reach zero within that time. Since $P'<0$ at this first zero,
it crosses into $P<0$ immediately. It remains to establish the entrance
conditions \eqref{eq:entry} at $t_e=O(\eps^{-\alpha})$.

\section{Reaching the ratio barrier}
At $w=WE+y$, uniformly for $y$ in compact sets, the finite path formulas give
\begin{equation}\label{eq:limit}
 \eps^{-\alpha}\nabla J_\eps(WE+y)
 \longrightarrow C_Lu e^{-u\cdot y}-Bxe^{-x\cdot y},
 \qquad B=\frac1{L(L+1)}.
\end{equation}
For completeness, $u\cdot W=\alpha$ and $x\cdot W=\alpha-1$.
The zero-diversity score gaps are strict at $W$, whose $b$ coordinate is
positive. The only surviving rare-coin path is the direct left action from
$(2,1)$. Every other successful path from above has an additional positive
logit cost, or has coin $c\ge2$ with a strictly larger adjacent logit.
Below-coin failures have cost at least $n\theta_1$, where
$\theta_1=n(L+1)/M$ and $n\theta_1>\beta$. This proves
\eqref{eq:limit}, including its first derivatives on compact sets.
Here $C_L=1/(L+1)$ for odd $L$ and $C_L=n/(L+1)$ for even $L$.

In time $\tau=\eps^\alpha t$, the limiting equation for $y$ is the right
side of \eqref{eq:limit}. Write $U=u\cdot y$, $q_y=x\cdot y$,
$D_+=u\cdot x$, and introduce a second clock by
$ds/d\tau=C_Le^{-U}$. In this clock the limiting equation and ratio are
\begin{equation}\label{eq:logistic}
 \frac{dy}{ds}=u-\mathcal R x,\qquad
 \mathcal R=\frac B{C_L}e^{U-q_y},\qquad
 \frac{d\mathcal R}{ds}
 =\mathcal R\{(M-D_+)-(D_+-6)\mathcal R\}.
\end{equation}
Since $M>D_+>6$, every positive ratio converges to
$\mathcal R_*=(M-D_+)/(D_+-6)$. Applying \eqref{eq:margin} at $s=r$
(the score coordinate, not the clock) shows $\mathcal R_*>R_0$.

Choose a fixed, sufficiently small $\tau_0>0$ so that \eqref{eq:tracking}
applies at $t_0=\tau_0\eps^{-\alpha}$. Equations \eqref{eq:ray} and
\eqref{eq:tracking} put
\[
 y_\eps(t_0):=w_\eps(t_0)-WE
\]
in a fixed compact set, independent of sufficiently small $\eps$.
On this set the initial limiting ratio is bounded above and bounded away
from zero. Choose $R_1$ strictly between $R_0$ and $\mathcal R_*$.
The logistic equation \eqref{eq:logistic} then puts every such limiting
solution above $R_1$ by a single finite clock time $s_*$.
All these limiting trajectories stay in one compact set on $0\le s\le s_*$:
their ratios remain bounded and their velocities are bounded in this clock.

Apply the same positive clock factor $C_Le^{-u\cdot y}$ to the rescaled
full equations. Uniform convergence of vector fields on a slightly larger
compact set, together with ordinary continuous dependence and a first-exit
argument, shows that the full trajectories stay close on $[0,s_*]$ to
limiting trajectories with the same initial points. Their ratios $Q/F$
converge uniformly there to $\mathcal R$, because the minimal-path sum
is dominated by its $S=r$ term at $WE+y$. In particular $R>R_0$ at the
end of this interval for all sufficiently small $\eps$.

The original rescaled time increment is uniformly bounded, since
$d\tau/ds=e^{u\cdot y}/C_L$ on this compact set. We have therefore reached
$t_e=O(\eps^{-\alpha})$ with $w_\eps(t_e)=WE+O(1)$ and $R>R_0$.
The linear forms $A,D,P$ are strictly positive at $W$, while
$q(W)=\alpha-1$. Choose $\delta>0$ smaller than half the values of
$A(W)$ and $D(W)$, and increase $C_0$ if necessary. This gives
\eqref{eq:entry}. If a probe crossing occurred earlier, the desired upper
bound already holds. The preceding section now proves Theorem~\ref{thm:upper}.

\section{Scope}
This closes the exponent and the two-sided order of the first correction
time. It does not establish convergence of $\eps^\alpha T_\eps$, a formula
for that possible prefactor, the time of permanent correction, or the law
of correction times under random initialization. No discrete-time or
sampled-gradient statement follows without further work.
\end{document}
