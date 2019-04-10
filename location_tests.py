import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """Tests if string representation was coded correctly"""
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("LA", -30.3, -131.21)
        loc2 = Location("SJ", 23.4, -110.9)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        self.assertEqual(repr(loc1),"Location('LA', -30.3, -131.2)")
        self.assertEqual(repr(loc2),"Location('SJ', 23.4, -110.9)")
    
    def test_eq_false(self):
        """Tests if objects are not equal when they are different"""
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("LA", -30.3, -131.21)
        loc2 = Location("SJ", 23.4, -110.9)
        self.assertNotEqual(loc,loc1)
        self.assertNotEqual(loc1,loc2)
        self.assertNotEqual(loc2,loc)
         
    def test_eq_true(self):
        """Tests if objects are equal even though they have different memory numbers"""
        loc = Location("SLO", 35.3, -120.7)
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA", -30.3, -131.21)
        loc3 = Location("LA", -30.3, -131.21)
        self.assertEqual(loc,loc1)
        self.assertEqual(loc1,loc)
        self.assertEqual(loc2,loc3)
        self.assertEqual(loc3,loc2)

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
