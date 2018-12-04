
def isunique(a):
 marker = 0
 bl = ord('a')
 for item in a:
  b = 1 << (ord(item) - bl)
  if marker & b > 0:
   return False
  else:
   marker |= b
 return True
 
 
if __name__ == "__main__":
 test_str = ['aaaaa', 'abcdea', 'abcdefg']
 test_sol = [False, False, True]
 
 for i in xrange(len(test_str)):
  sol = isunique(test_str[i])
  if sol == test_sol[i]:
   print test_str[i] + " passes " + str(sol)
  else:
   print test_str[i] + " no pass " + str(sol)