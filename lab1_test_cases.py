import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_exception(self):
        """Tests if the exception handling works for max_list_iter"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty_list(self):
        """Tests if an empty list evaluates to None"""
        self.assertEqual(max_list_iter([]),None)
    
    def test_max_list_iter_all_positions(self):
        """Tests that max_list_iter works for all positions"""
        self.assertEqual(max_list_iter([1,2,3]),3)    
        self.assertEqual(max_list_iter([2,3,1]),3)    
        self.assertEqual(max_list_iter([3,1,2]),3)
        self.assertEqual(max_list_iter([-12,3,0]),3)
        self.assertEqual(max_list_iter([0.2,0,0.1]),0.2)

    def test_max_list_iter_duplicates(self):
        """Tests max_list_iter when there are duplicates passed in"""
        self.assertEqual(max_list_iter([1,1,2]),2)    
        self.assertEqual(max_list_iter([2,2,1]),2)    
        self.assertEqual(max_list_iter([2,1,2]),2)    
        self.assertEqual(max_list_iter([2,2,2]),2)    
        self.assertEqual(max_list_iter([1,2,2]),2)    
        
    def test_reverse_rec(self):
        """Tests if reverse_rec works in all positions"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([2,1,3]),[3,1,2])
        self.assertEqual(reverse_rec([1,3,2]),[2,3,1])
   
    def test_reverse_rec_exception(self):
        """Tests if the exception handling works for reverse_rec"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)
       
    def test_reverse_rec_empty_list(self):
        """Tests if an empty list passed through reverse_rec evaluates to empty list"""
        self.assertEqual(reverse_rec([]),[]) 

    def test_bin_search(self):
        """Tests bin_search to make sure that it returns correct positions or None if not found"""
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), None )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
    
    def test_bin_search_floats_and_negatives(self):
        """Tests bin_search if it will work correctly with floats and negatives"""
        self.assertEqual(bin_search(-1, 0, 3, [-3, -1, 0, 3]), 1 )
        self.assertEqual(bin_search(0.2, 0, 3, [-3, -1, 0.2, 0.3]), 2 )      
 
    def test_bin_search_empty_list(self):
        """Tests bin_search when an empty list is passed in"""
        self.assertEqual(bin_search(4, 0, 5, []),None)
 
    def test_bin_search_exception(self):
        """Tests if the exception handling works for bin_search"""
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(4, 0, 5, list_val)
        

if __name__ == "__main__":
        unittest.main()

    
