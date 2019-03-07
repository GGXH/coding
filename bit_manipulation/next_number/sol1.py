def nextNumber(input):
  bl = input.bit_length()
  marker = 1
  zcnt = 0
  minG = input
  if minG & marker == 0:
    while minG & marker == 0:
      zcnt += 1
      marker <<= 1
    minG >>= zcnt
  marker = 1
  ocnt = 0
  while minG & marker != 0 and ocnt <= bl - zcnt:
    ocnt += 1
    marker <<= 1
  minG |= marker
  marker >>= 1
  minG ^= marker
  minG <<= zcnt
  
  maxS = input
  marker = 1
  ocnt = 0
  if maxS & marker != 0:
    while maxS & marker != 0:
      ocnt += 1
      marker <<= 1
    maxS >>= ocnt
  marker = 1
  zcnt = 0
  while maxS & marker == 0 and zcnt <= bl - ocnt:
    zcnt += 1
    marker <<= 1
  maxS ^= marker
  marker >>= 1
  maxS |= marker
  maxS <<= ocnt
  marker = 1 << ocnt
  marker -= 1
  maxS |= marker
  return (minG, maxS)
  
if __name__ == "__main__":
  input = 3
  a, b = nextNumber(input)
  print bin(input)
  print bin(a), bin(b)
  
    
    