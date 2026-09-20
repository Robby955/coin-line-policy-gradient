"""Independent path counts and asymptotic diagnostics; not a proof checker."""
from collections import defaultdict
from fractions import Fraction
import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from model import objective

ROOT=Path(__file__).resolve().parent


def parameters(L):
    n=(L+2)//2
    r=L+1-n
    u=np.array([n,r,n*L],dtype=float)
    return u,Fraction(n if L%2==0 else 1,L+1)


def score_counts(L):
    states={(p,0,0):1 for p in range(L)}
    for _ in range(2*L):
        nxt=defaultdict(int)
        for (p,n,s),count in states.items():
            nxt[max(0,p-1),n+1,s+p]+=count
            if p+1<L:
                nxt[p+1,n,s]+=count
        states=nxt
    counts=defaultdict(int)
    for (_,n,s),count in states.items():
        counts[n,s]+=count
    return counts


def failure_mp(w,L):
    a,b,d=map(mp.mpf,w)
    right=[1/(1+mp.exp(-(a+p*b+L*d))) for p in range(L+1)]
    left=[1/(1+mp.exp(a+p*b+L*d)) for p in range(L+1)]
    f=[mp.mpf(p!=L) for p in range(L+1)]
    for _ in range(2*L):
        f=[left[p]*f[max(0,p-1)]+right[p]*f[p+1] for p in range(L)]+[mp.mpf(0)]
    return sum(f)/(L+1)


def main():
    mp.mp.dps=100
    counts=[]
    for L in range(4,13):
        u,C=parameters(L)
        number=score_counts(L)[int(u[0]),int(u[1])]
        assert number==C*(L+1)
        counts.append({'L':L,'minimal_score':u.tolist(),'path_count':number,'coefficient':str(C)})
    leading=[]
    for L in [4,5,6]:
        u,C=parameters(L)
        w=[mp.mpf(int(x))*8 for x in u]
        U=sum(mp.mpf(int(x))*y for x,y in zip(u,w))
        value=failure_mp(w,L)*mp.exp(U)/(mp.mpf(C.numerator)/C.denominator)
        assert abs(value-1)<mp.mpf('1e-5')
        leading.append({'L':L,'scaled_loss_ratio':float(value),'relative_error':float(abs(value-1))})
    trajectories=[]
    for L in [4,5,6]:
        u,C=parameters(L);M=float(u@u)
        times=[40.,80.,160.,320.,600.]
        sol=solve_ivp(lambda s,w:np.exp(s)*objective(w,L,0.)[1],(0,times[-1]),np.zeros(3),
                      method='DOP853',t_eval=times,rtol=2e-10,atol=2e-12,max_step=.2)
        assert sol.success
        for s,w in zip(sol.t,sol.y.T):
            F=failure_mp([float(x) for x in w],L)
            target=u/M
            trajectories.append({'L':L,'log1p_t':float(s),'w':w.tolist(),
                'ray_offset':(w-target*s).tolist(),
                'log_score_residual':float(u@w-s-np.log(float(C)*M)),
                'scaled_failure_MtF':float(mp.mpf(M)*mp.expm1(float(s))*F),
                'velocity_relative_error':float(np.linalg.norm(np.exp(s)*objective(w,L,0.)[1]-target)/np.linalg.norm(target))})
    result={'exact_counts':counts,'leading_coefficient_checks':leading,'trajectory_checks':trajectories}
    out=ROOT/'results/zero-diversity-ray-20260919.json'
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    out=args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'counts_checked':len(counts),'leading_checks':leading,'last_time':[r for r in trajectories if r['log1p_t']==600.]},indent=2))

if __name__=='__main__':main()
