"""Exact algebra checks for the uniform upper-bound region and ratio barrier."""
from fractions import Fraction as F
import unittest


class TransitionChecks(unittest.TestCase):
    def test_ratio_barrier_and_descent(self):
        for L in range(4,101):
            n=(L+2)//2;k=(L+1)//2;r=L+1-n
            R0=F(n*L,2)
            minimum=n*n*(1+F(L*L,4)-F(L,2))+n*(L-1)-1
            self.assertGreater(minimum,0)
            for s in [F(r),F(n*(L-1)),F(r+n*(L-1),2)]:
                M=n*n*(1+L*L)+s*s;D=n*(L+1)+2*s
                barrier=M-D-(D-6)*R0
                square=(s-F(n*L+2,2))**2
                self.assertEqual(barrier,square+minimum)
                self.assertLessEqual(D/R0-6,-F(2,L))
                self.assertLessEqual((n+k*s)/R0-(1+2*k),-1)

    def test_uniform_region_logits(self):
        for L in range(4,15):
            k=(L+1)//2;n=(L+2)//2
            for a in range(-6,7):
                for b in range(-6,7):
                    for d in range(-6,7):
                        A=a+d-b;D=d-a;P=a+k*b
                        if min(A,D)<1 or P<0:continue
                        q=a+2*b+d
                        for c in range(1,L+1):
                            logits=[a+p*b+c*d for p in range(L+1)]
                            self.assertGreaterEqual(min(logits),min(A,D))
                            self.assertGreaterEqual(n*min(logits[:c])-q,min(A,D))
                        self.assertGreaterEqual(b+d,min(A,D))

if __name__=='__main__':unittest.main()
