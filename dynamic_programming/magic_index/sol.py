def magicIdexHelper(inputList, startIdx):
  if inputList[0] == startIdx:
    return startIdx
  if inputList[-1] == startIdx + len(inputList) - 1:
    return startIdx + len(inputList) - 1
  if inputList[0] > startIdx or inputList[-1] < startIdx + len(inputList) - 1:
    return -1
  mid = len(inputList) // 2
  if inputList[mid] == startIdx + mid:
    return mid
  if inputList[mid] < startIdx + mid:
    return magicIdexHelper(inputList[mid+1:], startIdx + mid + 1)
  else:
    return magicIdexHelper(inputList[:mid], startIdx)

def magicIdx(inputList):
  return magicIdexHelper(inputList, 0)
  
  
if __name__ == "__main__":
  inputStr = [-1, 0, 1, 2, 3, 4, 7, 8, 9]
  print magicIdx(inputStr)