

def getBool(inputStr):
  a = int(inputStr[0])
  b = int(inputStr[2])
  
  if inputStr[1] == '&':
    return a & b
  if inputStr[1] == '|':
    return a | b
  if inputStr[1] == '^':
    return a ^ b

def boolEval(inputStr, indx, res):
  print inputStr
  if len(inputStr) == 3:
    return 1 if getBool(inputStr) == int(res) else 0
    
  sum = 0
  for i in xrange(indx, len(inputStr)):
    if inputStr[i] != '1' and inputStr[i] != '0':
      if getBool(inputStr[i-1:i+2]):
        c = '1'
      else:
        c = '0'
      sum += boolEval(inputStr[:i-1] + c + inputStr[i+2:], i - 1, res)
  return sum
  

if __name__ == "__main__":
  inputStr = '1^0|0|1'
  print boolEval(inputStr, 0, False)
  
  inputStr = '0&0&0&1^1|0'
  print boolEval(inputStr, 0, True)