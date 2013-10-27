import unittest
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

class ClosestOfThreeSpec(unittest.TestCase):
    def test_closest_of_three(self):
        p = (1,1)
        q = (6,1)
        r = (1,13)
        d = 5
        expected = (p,q),d
        self.assertEqual(expected, pyclops.closest_of_three(p,q,r))

class ClosestPairSpec(unittest.TestCase):
    def setUp(self):
        pass
    def test_closest_pair_a(self):
        self.assertEqual(1,1)
    def test_closest_pair_b(self):
        self.assertEqual(1,1)
    def tearDown(self):
        pass
