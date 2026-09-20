"""MAIS-O87 finite-horizon return and analytic gradient; no Monte Carlo."""
import numpy as np
from scipy.special import expit
from scipy.integrate import solve_ivp


def components(w, L):
    """Per-coin returns and gradients using dual success/failure recurrences.

    At each step use the less saturated representation for the value difference.
    Propagating only success or only failure can lose gradients near infinity.
    """
    p = np.arange(L + 1)
    c = np.arange(1, L + 1)[:, None]
    x = np.stack(np.broadcast_arrays(np.ones((L,L+1)), p[None,:], c), axis=-1)
    z = x @ np.asarray(w)
    r, l = expit(z), expit(-z)
    dr = (r*l)[...,None] * x
    terminal = p[None,:] == c
    success = terminal.astype(float)
    failure = (~terminal).astype(float)
    deriv = np.zeros_like(x)
    left, right = np.maximum(p-1,0), np.minimum(p+1,L)
    for _ in range(2*L):
        sl, sr = success[:,left], success[:,right]
        fl, fr = failure[:,left], failure[:,right]
        advantage = np.where(sl+sr <= fl+fr, sr-sl, fl-fr)
        deriv = np.where(terminal[...,None], 0.,
            l[...,None]*deriv[:,left] + r[...,None]*deriv[:,right]
            + dr*advantage[...,None])
        success = np.where(terminal, 1., l*sl+r*sr)
        failure = np.where(terminal, 0., l*fl+r*fr)
    return success.mean(axis=1), deriv.mean(axis=1)


def objective(w, L, eps):
    values, grads = components(w,L)
    weights = np.full(L,eps/L)
    weights[-1] += 1-eps
    return weights@values, weights@grads


def flow(w, L, eps, s_end=25., samples=101):
    """Integrate in logarithmic time t=exp(s)-1; this is the same ODE."""
    return solve_ivp(lambda s,y: np.exp(s)*objective(y,L,eps)[1],
                     (0,s_end),w,t_eval=np.linspace(0,s_end,samples),
                     rtol=2e-8,atol=2e-10)
