import unittest
from random import seed,randrange,randint
import src.pyclops.core as pyclops

class DistanceSpec(unittest.TestCase):
    def test_1d_distance(self):
        p = (0,1)
        q = (0,2)
        self.assertEqual(pyclops.distance(p,q), 1)
        m = (45,0)
        n = (67,0)
        self.assertEqual(pyclops.distance(m,n), 22)
    def test_2d_distance(self):
        a = (0,0)
        b = (5,12)
        self.assertEqual(pyclops.distance(a,b), 13)

class BruteForceClosestPairSpec(unittest.TestCase):
    def test_closest_of_two(self):
        m = (12,13)
        n = (15,17)
        d = 5
        expected = (m,n),d
        self.assertEqual(expected, pyclops.brute_force_closest_pair([m,n]))
    def test_closest_of_three(self):
        p = (1,1)
        q = (6,1)
        r = (1,13)
        d = 5
        expected = (p,q),d
        self.assertEqual(expected, pyclops.brute_force_closest_pair([p,q,r]))

class ClosestPairSpec(unittest.TestCase):
    def setUp(self):
        seed()
        rand_pair = lambda: (randint(-10000,10000), randint(-10000,10000))
        self.a_case = [rand_pair() for _ in xrange(randrange(2,100))]
        self.b_case = [rand_pair() for _ in xrange(randrange(101,500))]

    def test_a_closest_pair(self):
        (dcp,dcq),dcd = pyclops.closest_pair(self.a_case)
        (bfp,bfq),bfd = pyclops.brute_force_closest_pair(self.a_case)
        self.assertEqual(dcd,bfd)
        same = (dcp == bfp and dcq == bfq)
        swap = (dcp == bfq and dcq == bfp)
        self.assertTrue(same or swap)

    def test_b_closest_pair(self):
        (dcp,dcq),dcd = pyclops.closest_pair(self.b_case)
        (bfp,bfq),bfd = pyclops.brute_force_closest_pair(self.b_case)
        self.assertEqual(dcd,bfd)
        same = (dcp == bfp and dcq == bfq)
        swap = (dcp == bfq and dcq == bfp)
        self.assertTrue(same or swap)
