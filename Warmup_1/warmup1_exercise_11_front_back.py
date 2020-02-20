"""

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
def front_back(str):
  if len(str)>=2:
    front = str[0]
    end = str[-1]
    return end + str[1:-1] + front
  return str