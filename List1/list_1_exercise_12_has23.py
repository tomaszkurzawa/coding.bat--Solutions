"""
Given an int array length 2, return True if it contains a 2 or a 3.


has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""
def has23(nums):
  for e in nums:
    if e ==2 or e==3:
      return True
  return False