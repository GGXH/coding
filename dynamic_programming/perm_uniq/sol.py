

def addChar(char, word):
  if len(word) == 0:
    return [char]
  res = [char + word, word + char]
  for i in xrange(1, len(word)):
    res.append(word[:i] + char + word[i:])
  return res
  

def helper(inputStr, preSet):
  if len(inputStr) == 0:
    return preSet
  curSet = []
  for word in preSet:
    curSet += addChar(inputStr[0], word)
  preSet = helper(inputStr[1:], curSet)
  return preSet

def permUniq(inputStr):
  perm = [inputStr[0]]
  perm = helper(inputStr[1:], perm)
  return perm
  
  
if __name__ == "__main__":
  inputstr = "abcd"
  
  print permUniq(inputstr)