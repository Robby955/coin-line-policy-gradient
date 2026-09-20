"""Checks for the proposed dominant failed-path score and crossing diagnostic."""
import unittest
from correction_time import measure
from verify_zero_diversity_ray import score_counts


def failed_scores(L):
    # Exact dynamic enumeration of (position, left count, sum of left positions).
    states={(p,0,0) for p in range(L)}
    for _ in range(2*L):
        nxt=set()
        for p,n,s in states:
            nxt.add((max(0,p-1),n+1,s+p))
            if p+1<L:
                nxt.add((p+1,n,s))
        states=nxt
    return {(n,s) for _,n,s in states}


class CorrectionChecks(unittest.TestCase):
    def test_exact_failed_path_scores(self):
        for L in range(4,13):
            n=(L+2)//2
            r=n-int(L%2==0)
            scores=failed_scores(L)
            self.assertIn((n,r),scores)
            for N,S in scores:
                self.assertGreaterEqual(N,n)
                self.assertGreaterEqual(S,max(0,L+1-N))
                # Difference at h=b >=0; h>b only increases it.
                self.assertGreaterEqual((N-n)+(S-r),0)

    def test_negative_b_dominant_paths(self):
        for L in range(4,13):
            n=(L+2)//2
            counts=score_counts(L)
            self.assertEqual(counts[n,n*(L-1)],2 if L%2==0 else 1)
            for N,S in counts:
                self.assertGreaterEqual(N,n)
                self.assertLessEqual(S,N*(L-1))

    def test_first_downward_event_not_initial_zero(self):
        row=measure(4,1e-4)
        self.assertTrue(row['success'] and row['crossed'])
        self.assertAlmostEqual(row['log1p_t_cross'],12.2703183953,places=6)
        self.assertGreater(row['t_cross'],0)
        self.assertAlmostEqual(row['w_cross'][0]+2*row['w_cross'][1],0,places=9)

if __name__=='__main__':
    unittest.main()
