Please give the final verdict on the repaired upper-bound argument, in at most 1500 words. The revised full source follows. We have added the missing path facts and endpoint constructions; explicitly stated q>=delta E; separated coin L from the per-start success/failure decomposition for rare coins; written the simultaneous first-exit argument; expanded the class-by-class exponents; removed the unnecessary C1-convergence assertion; and made the compact-enlargement/clock argument quantitative. Check that these repairs actually close M1-M5, without re-deriving every accepted identity. The ray and lower-bound inputs have separately been accepted by another fresh reviewer after exposition fixes. If a gap remains, identify it exactly; otherwise give a clear conditional acceptance under those inputs. Do not stop with 'continues'.

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
Fix $\delta>0$ smaller than half of both $A(W)$ and $D(W)$; these
quantities are positive. All subsequent constants may depend on this choice.
Consider the region
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
In particular $q=z_{2,1}\ge\delta E$, since $(2,1)$ is a training state.
Equivalently, $q=A+3b$ for $b\ge0$, and
$q=2a+2b+D\ge2(1-k)b+D$ for $b<0$.


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

For coins $2\le c<L$, success from above requires a left action at $c+1$.
Its logit is $q+(c-1)(b+d)\ge q+\delta E$, by \eqref{eq:bd}.
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
Define $t^*$ to be the first time after $t_e$ at which $A=\delta E$,
$D=\delta E$, $R=R_0$, or $P=0$. Before this time all preceding estimates
hold. For any such $t$, \eqref{eq:decrease} gives
$\int_{t_e}^tQ\,du\le2P(t_e)\le2C_0E$. By \eqref{eq:preserve},
\[
 A(t),D(t)\ge2\delta E-2CC_0\zeta E>\delta E
\]
for sufficiently small $\eps$. These inequalities also hold at a finite
$t^*$ by continuity. The alternative $R(t^*)=R_0$ is impossible because
$R'>0$ there, whereas a first crossing from above would have $R'\le0$.
Hence any finite $t^*$ is a probe zero. If $t^*=\infty$, the same estimates
hold for all later times, which the following time bound rules out.
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
For clarity, put $\theta_1=n(L+1)/M$. A rare below-coin failed path
has exponent at least $1+\alpha n\theta_1>\alpha$, since
$n\theta_1-\beta=[n(n-1)(L+1)-2r]/M>0$. A rare above-coin path with
$c\ge2$ has exponent at least $1+\alpha\beta_c>\alpha$, with
$\beta_c=[n+(c+1)r+cnL]/M$. A non-direct coin-$1$ success has the
leading exponent $\alpha$ plus the strictly positive cost of another
left action. Finally, the change in the coin-$L$ mixture weight has
an additional factor $\eps$. These are all path classes. This proves
\eqref{eq:limit} uniformly on compact sets; only this uniform convergence is needed below.
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
full equations. Let $\mathcal K_0$ contain their initial points, and let
$\mathcal K_1$ contain all limiting trajectories from $\mathcal K_0$ on
$[0,s_*]$. The logistic ratio stays between its initial value and its
positive equilibrium, uniformly over $\mathcal K_0$. Thus these orbits
and their velocities are bounded and $\mathcal K_1$ is compact.
On the closed one-neighbourhood $\mathcal K_2$ of $\mathcal K_1$, the
clock factor is bounded above and away from zero. The transformed full
fields converge uniformly to the smooth limiting field. If their uniform
difference is $\eta_\eps\to0$ and a Lipschitz constant for the limit field
on a containing compact ball is $H_0$, comparison up to first exit gives
\[
 \sup_{0\le s\le s_*}\|y_\eps(s)-y(s)\|
 \le\eta_\eps s_* e^{H_0 s_*}.
\]
For small $\eps$ this is less than one, excluding exit from $\mathcal K_2$.
The initial limiting point is always chosen equal to the full initial
point; convergence of the initial points themselves is not required.

The ratios $Q/F$ converge uniformly on $\mathcal K_2$ to $\mathcal R$,
since $W_b>0$ makes the $S=r$ term dominate the finite sum. The comparison
therefore gives $R>R_0$ at clock time $s_*$, uniformly over the allowed
initial points. Finally $u\cdot y$ is bounded above on $\mathcal K_2$,
so $d\tau/ds=e^{u\cdot y}/C_L$ has a uniform upper bound. The elapsed
rescaled time is bounded independently of $\eps$. We have therefore reached
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
