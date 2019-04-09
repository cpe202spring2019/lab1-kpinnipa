
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
       return None
   if int_list == None:
       raise ValueError('List cannot be None!')
   maximum = 0
   for i in range(1,len(int_list)):
      if int_list[maximum] < int_list[i]:
          maximum = i       
   return int_list[maximum]

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError('List cannot be None!')
   if int_list == []:
      return int_list
   return int_list[-1:] + reverse_rec(int_list[:-1]) 

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
       raise ValueError('List cannot be None!')
   if int_list == []:
       return None
   if low > high:
       return None
   mid = (low + high)//2
   if int_list[mid] == target:
       return mid
   if target > int_list[mid]:
       return bin_search(target, mid+1, high, int_list)
   return bin_search(target, low, mid-1, int_list)
