"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
def cat_dog(str):
  sub = "cat"
  sub1 = "dog"
  x = str.count(sub)
  y = str.count(sub1)
  if x==y:
    return True
  return False