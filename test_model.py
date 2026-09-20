"""Independent exact path enumeration and differential checks."""
from fractions import Fraction as F
import unittest
import numpy as np
from model import components, objective


def enumerate_exact(L, bases):
    values, grads = [], []
    for c in range(1,L+1):
        total, derivative = F(0), [F(0)]*3
        def visit(p, h, prob, score):
            nonlocal total
            if p == c:
                total += prob
                for i in range(3): derivative[i] += prob*score[i]
                return
            if not h: return
            odds=bases[0]*bases[1]**p*bases[2]**c
            r=odds/(1+odds)
            for action, chance in [(1,r),(-1,1-r)]:
                ds=(1-r) if action==1 else -r
                visit(min(max(p+action,0),L),h-1,prob*chance,
                      [score[i]+ds*x for i,x in enumerate([1,p,c])])
        for p in range(L+1): visit(p,2*L,F(1,L+1),[F(0)]*3)
        values.append(float(total)); grads.append(list(map(float,derivative)))
    return np.array(values),np.array(grads)


class Checks(unittest.TestCase):
    def test_exact_exhaustive_paths(self):
        bases=[F(2),F(3,2),F(4,3)]
        want=enumerate_exact(4,bases)
        got=components(np.log(list(map(float,bases))),4)
        np.testing.assert_allclose(got[0],want[0],rtol=1e-13,atol=1e-15)
        np.testing.assert_allclose(got[1],want[1],rtol=1e-12,atol=1e-15)

    def test_saturated_exact_paths(self):
        # A correct saturated policy: single-representation DP loses precision.
        bases=[F(1), F(1,2**30), F(2**30)]
        want=enumerate_exact(4,bases)
        got=components([0.,-30*np.log(2),30*np.log(2)],4)
        np.testing.assert_allclose(got[1],want[1],rtol=2e-12,atol=0)

    def test_gradient_and_separator(self):
        rng=np.random.default_rng(87)
        for L in [4,5,8]:
            for _ in range(5):
                w=rng.normal(0,.3,3)
                _,g=objective(w,L,.2)
                fd=np.array([(objective(w+1e-5*d,L,.2)[0]-objective(w-1e-5*d,L,.2)[0])/2e-5 for d in np.eye(3)])
                np.testing.assert_allclose(g,fd,rtol=2e-6,atol=1e-9)
                self.assertGreater(g[2]-g[1],0)

    def test_probe_certificate(self):
        for L in range(4,101):
            k=(L+1)//2
            alpha=F(k+1,2)-F(L,L-1)
            beta=F(1,L-1); gamma=F(k+1,2)
            self.assertGreater(alpha,0)
            self.assertEqual(alpha+beta-gamma,-1)
            self.assertEqual((L-1)*beta-2*gamma,-k)
            self.assertEqual(alpha+L*beta-gamma,0)

    def test_zero_diversity_invariant(self):
        _,g=objective([.2,-.3,.4],5,0)
        self.assertAlmostEqual(g[2],5*g[0],places=14)


if __name__=='__main__': unittest.main()
