"""Independent 100-digit differentiation of the direct success recurrence."""
import json
import mpmath as mp
import numpy as np
from model import objective


def reference(w,L,eps):
    w=list(map(mp.mpf,w)); eps=mp.mpf(eps)
    def J(*w):
        out=mp.mpf(0)
        for c in range(1,L+1):
            r=[1/(1+mp.exp(-(w[0]+p*w[1]+c*w[2]))) for p in range(L+1)]
            v=[mp.mpf(p==c) for p in range(L+1)]
            for _ in range(2*L):
                v=[mp.mpf(1) if p==c else (1-r[p])*v[max(p-1,0)]+r[p]*v[min(p+1,L)] for p in range(L+1)]
            out+=(eps/L+(1-eps if c==L else 0))*sum(v)/(L+1)
        return out
    return np.array([float(mp.diff(lambda x:J(*(w[:i]+[x]+w[i+1:])),w[i])) for i in range(3)])

if __name__=='__main__':
    mp.mp.dps=100
    rows=[]
    for w in [[0,-20,20],[0,-40,40],[20,10,-10],[-2,-6,8]]:
        ref=reference(w,4,'.001'); got=objective(w,4,.001)[1]
        np.testing.assert_allclose(got,ref,rtol=2e-12,atol=0)
        rows.append({'w':w,'reference':ref.tolist(),'computed':got.tolist(),
                     'max_relative_error':float(np.max(np.abs((got-ref)/ref)))})
    print(json.dumps(rows,indent=2))
