import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("LA", -30.3, -131.21)
        loc2 = Location("SJ", 23.4, -110.9)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc1),"Location('LA', -30.3, -131.2)")
        self.assertEqual(repr(loc2),"Location('SJ', 23.4, -110.9)")
    
    def test_eq_false(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("LA", -30.3, -131.21)
        self.assertNotEqual(loc,loc1)
        
    def test_eq_true(self):
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc,loc1)

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
