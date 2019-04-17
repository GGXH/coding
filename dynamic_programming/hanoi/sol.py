def helper(n, towerList):
  if n == 1:
    return [[1, (towerList[0], towerList[1])]]
  
  res = []
  res += helper(n - 1, [towerList[0], towerList[2], towerList[1]])
  res += [[n, (towerList[0], towerList[1])]]
  res += helper(n - 1, [towerList[2], towerList[1], towerList[0]])
  return res


def hanoi(n):
  return helper(n, [0, 1, 2])
  
  
if __name__ == "__main__":
  for it in hanoi(4):
    print it
 
 
