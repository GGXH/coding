def recursMult(a, b):
  if b > a:
    return recursMult(b, a)
  if b == 0:
    return 0
  if b == 1:
    return a
  adda = 0
  if b & 1 == 1:
    adda = a
  b >>= 1
  halfres = recursMult(a, b)
  return halfres + halfres + adda
  
if __name__ == "__main__":
  print recursMult(3, 2)
  
  print recursMult(30, 2)
  
  print recursMult(5, 11)
    