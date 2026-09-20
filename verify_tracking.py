"""Diagnostics for the local tracking proof, not certified ODE bounds."""
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from model import objective
from verify_zero_diversity_ray import parameters, failure_mp

ROOT=Path(__file__).resolve().parent


def hessian_check(L,w):
    mp.mp.dps=70
    ww=list(map(mp.mpf,w))
    def negative_failure(*args):
        return -failure_mp(args,L)
    hessian=np.zeros((3,3))
    for i in range(3):
        for j in range(i,3):
            orders=[0,0,0];orders[i]+=1;orders[j]+=1
            hessian[i,j]=hessian[j,i]=float(mp.diff(negative_failure,tuple(ww),tuple(orders)))
    F=failure_mp(ww,L)
    minz=min(ww[0]+p*ww[1]+L*ww[2] for p in range(L))
    # B_omega <= H max_p ||x_p||^2 exp(-min z) I, for every failed path.
    bound=float(2*L*(1+(L-1)**2+L**2)*mp.exp(-minz)*F)
    eigen=float(np.linalg.eigvalsh(hessian)[-1])
    assert eigen <= bound+1e-12*np.linalg.norm(hessian)
    return {'L':L,'w':w,'largest_hessian_eigenvalue':eigen,'upper_bound':bound}


def main():
    hessians=[hessian_check(L,w) for L in [4,5] for w in [[.1,.2,.5],[.5,.1,2.],[-.1,-.2,.7]]]
    rows=[]
    for L in [4,5,6]:
        u,_=parameters(L);M=float(u@u)
        beta=float(u@np.array([1.,2.,1.])/M);alpha=1/(1-beta)
        for power in [8,16,32,64]:
            eps=10.**(-power)
            end=(alpha-.1)*np.log(1/eps)
            def rhs(s,y):
                return np.exp(s)*np.concatenate((objective(y[:3],L,0.)[1],objective(y[3:],L,eps)[1]))
            sol=solve_ivp(rhs,(0,end),np.zeros(6),method='DOP853',
                          rtol=2e-11,atol=2e-13,max_step=.2)
            assert sol.success
            D=np.linalg.norm(sol.y[:3]-sol.y[3:],axis=0)
            scale=eps*np.expm1((1-beta)*sol.t)
            mask=(sol.t>1) & (scale>1e-7)
            # Do not normalize roundoff-scale trajectory differences.
            endD=float(D[-1]);endScale=float(scale[-1])
            rows.append({'L':L,'eps':eps,'eta':.1,'log1p_end_time':float(end),
                         'endpoint_distance':endD,'endpoint_scale':endScale,
                         'endpoint_ratio':endD/endScale,
                         'max_ratio_with_scale_above_1e_minus7':float(np.max(D[mask]/scale[mask])) if np.any(mask) else None,
                         'probe_at_endpoint':float(sol.y[3,-1]+((L+1)//2)*sol.y[4,-1])})
    out=ROOT/'results/tracking-diagnostics-filtered-20260919.json'
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    out=args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'hessian_checks':hessians,'tracking_checks':rows},indent=2)+'\n')
    print(json.dumps({'hessian_checks':len(hessians),'tracking_checks':rows},indent=2))

if __name__=='__main__':main()
