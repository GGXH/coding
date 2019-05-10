
def permUniq(inputStr):
  if len(inputStr) == 1:
    return [inputStr]
  res = []
  for i in xrange(len(inputStr)):
    if i == 0:
      subres = permUniq(inputStr[i+1:])
    elif i == len(inputStr) - 1:
      subres = permUniq(inputStr[:i])
    else:
      subres = permUniq(inputStr[:i] + inputStr[i+1:])
    for w in subres:
      res.append(inputStr[i] + w)
  return res

  
if __name__ == "__main__":
  inputstr = "abcd"
  
  print permUniq(inputstr)