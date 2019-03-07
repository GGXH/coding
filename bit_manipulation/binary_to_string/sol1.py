def binaryToString(input):
  res = "."
  cnt = 0
  while cnt < 32 and input != 0:
    input *= 2
    if input >= 1:
      res += "1"
      input -= 1
    else:
      res += "0"
    cnt += 1
  if cnt >= 32:
    print "Error"
  return res
  
  
if __name__ == "__main__":
  print binaryToString(0.251)