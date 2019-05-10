from collections import defaultdict

def helper(charLib):
  if len(charLib) == 1:
    res = ""
    for k in charLib.keys():
      res += k * charLib[k]
    return [res]
  res = []
  for k in charLib.keys():
    if charLib[k] == 1:
      del charLib[k]
    else:
      charLib[k] -= 1
    subres = helper(charLib)
    for w in subres:
      res.append(k + w)
    charLib[k] += 1
  return res
    

def permDup(inputStr):
  charLib = defaultdict(int)
  for c in inputStr:
    charLib[c] += 1
  return helper(charLib)
  
  
if __name__ == "__main__":
  inputStr = "abc"
  print permDup(inputStr)
  
  inputStr = "aaa"
  print permDup(inputStr)
  
  inputStr = "abca"
  print permDup(inputStr)

