def conversion(in1, in2):
  value = in1 ^ in2
  marker = 1
  cnt = 0
  while value > 0:
    if value & marker == 1:
      cnt += 1
    value >>= 1
  return cnt
  
  
if __name__ == "__main__":
  in1 = 129
  in2 = 15
  print conversion(in1, in2)
  print bin(in1)
  print bin(in2)