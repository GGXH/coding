def powerSetHelper(inputL, marker):
  res = []
  indx = 0
  while marker > 0:
    if marker & 1 == 1:
      res.append(inputL[indx])
    indx += 1
    marker >>= 1
  return res
  


def powerset(inputL):
  allSets = []
  for i in xrange(2**(len(inputL))):
    ss = powerSetHelper(inputL, i)
    allSets.append(ss)
  return allSets
  
if __name__ == "__main__":
  inputL = [1, 2]
  print powerset(inputL)
  
  inputL = [1, 2, 3, 4, 5, 6, 7, 8]
  print powerset(inputL)