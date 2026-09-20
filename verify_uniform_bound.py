"""Check the upper-bound approximation on both sides of b=0 and at b=0.

The exact minimum-count path polynomial is evaluated at the ratio barrier.
These finite checks do not certify the uniform asymptotic estimate.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.special import logsumexp
from model import objective
from verify_zero_diversity_ray import score_counts


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():raise FileExistsError(args.output)
    rows=[]
    x=np.array([1.,2.,1.])
    for L in [4,5,6]:
        n=(L+2)//2;k=(L+1)//2;R0=n*L/2
        counts=score_counts(L)
        terms=[(S,count) for (N,S),count in counts.items() if N==n]
        scores=np.array([t[0] for t in terms]);multiplicities=np.array([t[1] for t in terms])
        for sign in [-1,0,1]:
            errors=[]
            for scale in [4.,8.,12.]:
                b=sign*scale/(8*L)
                a=k*abs(b)+scale/8 if b<0 else b/2
                d=a+scale;w=np.array([a,b,d]);q=float(x@w)
                logs=np.log(multiplicities)-scores*b-n*(a+L*d)-np.log(L+1)
                logF=float(logsumexp(logs));F=float(np.exp(logF))
                s=float(np.exp(logs-logF)@scores);v=np.array([n,s,n*L])
                eps=float(np.exp(np.log(R0)+logF+q+np.log(L*(L+1))))
                assert 0<eps<1
                Q=R0*F
                got=objective(w,L,eps)[1];approx=F*v-Q*x
                error=float(np.linalg.norm(got-approx)/(F+Q))
                errors.append(error)
                rows.append({'L':L,'b_sign':sign,'scale':scale,'w':w.tolist(),'eps':eps,
                             'ratio':R0,'relative_vector_error':error,
                             'probe_derivative':float(got[0]+k*got[1]),
                             'q_derivative':float(x@got)})
                assert got[0]+k*got[1]<0 and x@got<0
            assert errors[-1]<errors[0]/100
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(rows,indent=2)+'\n')
    print('27 region checks passed, including b=0; normalized errors decrease by >100x.')

if __name__=='__main__':main()
