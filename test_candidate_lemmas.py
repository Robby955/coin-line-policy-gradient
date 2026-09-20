"""Exact checks of delicate finite-model bounds; not a formal proof of the ODE."""
from fractions import Fraction as F
import unittest


def exact_logit_derivatives(probabilities,c,H):
    L=len(probabilities)-1
    values=[F(p==c) for p in range(L+1)]
    derivatives=[[F(0)]*(L+1) for _ in range(L+1)]
    for _ in range(H):
        vnew=[]; dnew=[]
        for p,r in enumerate(probabilities):
            if p==c:
                vnew.append(F(1)); dnew.append([F(0)]*(L+1)); continue
            left,right=max(p-1,0),min(p+1,L)
            vnew.append((1-r)*values[left]+r*values[right])
            row=[(1-r)*derivatives[left][j]+r*derivatives[right][j] for j in range(L+1)]
            row[p]+=r*(1-r)*(values[right]-values[left])
            dnew.append(row)
        values,derivatives=vnew,dnew
    return [sum(row[j] for row in derivatives)/len(probabilities) for j in range(L+1)]


class CandidateLemmaChecks(unittest.TestCase):
    def test_policy_independent_adjacent_bounds(self):
        policies=[
            [F(1,2)]*5,
            [F(1,7),F(6,7),F(1,10000),F(9999,10000),F(1,2)],
            [F(9999,10000),F(1,10000),F(6,7),F(1,7),F(1,10000)],
        ]
        for policy in policies:
            for c in range(1,5):
                g=exact_logit_derivatives(policy,c,8)
                for p,value in enumerate(g):
                    if p<c: self.assertGreater(value,0)
                    elif p>c: self.assertLess(value,0)
                    else: self.assertEqual(value,0)
                r=policy[c-1]
                self.assertGreaterEqual(g[c-1],r*(1-r)**8/5)
                if c<4:
                    r=policy[c+1]
                    self.assertGreaterEqual(-g[c+1],r**8*(1-r)/5)

    def test_reachability_algebra_exact(self):
        # R0,S0 are arbitrary valid lower bounds, not assumed positive.
        for L in range(4,13):
            k=(L+1)//2
            for a in range(-8,9):
                for b in range(-8,9):
                    for d in range(-8,9):
                        A=d-b; P=a+k*b
                        if A<=0 or P<0: continue
                        R0=min(0,A-a); S0=min(0,A+a)
                        adjacent=[a+(c-1)*b+c*d for c in range(1,L+1)]
                        adjacent += [a+(c+1)*b+c*d for c in range(1,L)]
                        if b>=0:
                            bound=F(A,k)+F((k-1)*S0,k)
                        else:
                            bound=F(A,2)-L*abs(R0)
                        self.assertGreaterEqual(min(adjacent),bound)

    def test_monotone_coefficients(self):
        for L in range(4,30):
            for c in range(1,L+1):
                for p in range(L+1):
                    if p==c: continue
                    y=1 if c>p else -1
                    self.assertGreaterEqual(abs(c-p)-y,0)
                    self.assertGreaterEqual(abs(c-p)+y,0)


if __name__=='__main__': unittest.main()
