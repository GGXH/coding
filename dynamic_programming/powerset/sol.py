def powerSetHelper(inputL, allSets):
  if len(inputL) == 0:
    return
  curSets = []
  for s in allSets:
    news = s[:]
    news.append(inputL[0])
    curSets.append(news)
  allSets += curSets
  powerSetHelper(inputL[1:], allSets)

def powerset(inputL):
  allSets = []
  empty = []
  allSets.append(empty)
  powerSetHelper(inputL, allSets)
  return allSets
  
if __name__ == "__main__":
  inputL = [1, 2]
  print powerset(inputL)
  
  inputL = [1, 2, 3, 4, 5, 6, 7, 8]
  print powerset(inputL)