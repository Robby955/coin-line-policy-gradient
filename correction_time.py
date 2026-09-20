"""Exact-return flow: first downward probe crossing from zero initialization.

Numerical evidence only. The clock is s=log(1+t); neither a first crossing
nor integration to a finite horizon certifies permanent correction.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from model import objective


def measure(L, eps, rtol=2e-9, max_step=0.2, method='DOP853'):
    k = (L + 1) // 2
    def crossing(s, w):
        return w[0] + k*w[1]
    crossing.direction = -1
    crossing.terminal = True
    start = time.monotonic()
    initial_gradient = objective(np.zeros(3), L, eps)[1]
    if initial_gradient[0] + k*initial_gradient[1] <= 0:
        raise ValueError('This diagnostic requires an initially positive probe derivative.')
    end = max(50., 3*np.log(1/eps) + 20)
    sol = solve_ivp(lambda s, w: np.exp(s)*objective(w,L,eps)[1],
                    (0,end), np.zeros(3), events=crossing,
                    rtol=rtol, atol=rtol/100, max_step=max_step, method=method)
    event = bool(len(sol.t_events[0]))
    s = float(sol.t_events[0][0]) if event else None
    w = sol.y_events[0][0] if event else sol.y[:,-1]
    return {'L':L, 'eps':eps, 'rtol':rtol, 'max_step':max_step, 'method':method,
            'success':bool(sol.success), 'message':sol.message, 'crossed':event,
            'log1p_t_cross':s, 't_cross':float(np.expm1(s)) if event else None,
            'w_cross':w.tolist() if event else None, 'nfev':sol.nfev,
            'elapsed_seconds':time.monotonic()-start}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lengths',type=int,nargs='+',default=[4,5,6])
    parser.add_argument('--powers',type=int,nargs='+',default=[2,4,8,12,16])
    parser.add_argument('--rtol',type=float,default=2e-9)
    parser.add_argument('--method',default='DOP853',choices=['DOP853','RK45','Radau'])
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f'Preserve existing results: {args.output}')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as out:
        for L in args.lengths:
            for power in args.powers:
                row=measure(L,10.**(-power),args.rtol,method=args.method)
                out.write(json.dumps(row)+'\n');out.flush()
                print(json.dumps(row),flush=True)

if __name__=='__main__':
    main()
