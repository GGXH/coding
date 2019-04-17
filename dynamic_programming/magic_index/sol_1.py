def magicIdexHelper(inputList, startIdx):
  if len(inputList) < 1:
    return -1
  if inputList[0] == startIdx:
    return startIdx
  if inputList[-1] == startIdx + len(inputList) - 1:
    return startIdx + len(inputList) - 1
  mid = len(inputList) // 2
  if inputList[mid] == startIdx + mid:
    return mid
  res1 = magicIdexHelper(inputList[mid+1:], startIdx + mid + 1)
  if res1 >= 0:
    return res1
  res2 = magicIdexHelper(inputList[:mid], startIdx)
  return res2

def magicIdx(inputList):
  return magicIdexHelper(inputList, 0)
  
  
if __name__ == "__main__":
  inputStr = [-1, 0, 1, 2, 3, 4, 6, 8, 9]
  print magicIdx(inputStr)
  
  inputStr = [-1, 0, 1, 2, 3, 4, 7, 8, 9]
  print magicIdx(inputStr)
  
  inputStr = [-1, 0, 1, 2, 2, 5, 5, 8, 9]
  print magicIdx(inputStr)