
from collections import defaultdict

def boolEvalHelper(inputStr, res, resMap):
  if len(inputStr) < 2:
    return 1 if int(inputStr[0]) == int(res) else 0
  strRes = inputStr + str(res)
  if strRes in resMap:
    return resMap[strRes]
  countT = 0
  for i in xrange(1, len(inputStr), 2):
    leftF = boolEvalHelper(inputStr[:i], False, resMap)
    leftT = boolEvalHelper(inputStr[:i], True, resMap)
    rightF = boolEvalHelper(inputStr[i+1:], False, resMap)
    rightT = boolEvalHelper(inputStr[i+1:], True, resMap)
    totalC = ( leftF + leftT ) * ( rightF + rightT)
#    print leftF, leftT, rightF, rightT
    if inputStr[i] == "&":
      cT = leftT * rightT
    elif inputStr[i] == "|":
      cT = leftT * rightT + leftT * rightF + leftF * rightT
    elif inputStr[i] == "^":
      cT = leftT * rightF + leftF * rightT
    countT += cT if res else totalC - cT
  resMap[strRes] = countT
#  print strRes, resMap[strRes]
  return countT
  

def boolEval(inputStr, res):
  resCntMap = defaultdict(int)
  return boolEvalHelper(inputStr, res, resCntMap)
  
  

if __name__ == "__main__":
  inputStr = '1^0|0|1'
  print boolEval(inputStr, False)
  
  inputStr = '0&0&0&1^1|0'
  print boolEval(inputStr, True)

  inputStr = '0&1'
  print boolEval(inputStr, True)