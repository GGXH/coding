def trip_step(n):
  if n == 0:
   return 1
  if n == 1:
   return 1
  if n == 2:
   return 2
  
  a = 1
  b = 1
  c = 2
  for i in xrange(3, n + 1):
    res = a + b + c
    a = b
    b = c
    c = res
  return res
  
  
if __name__ == "__main__":
  print trip_step(10)