

def diagChecker(colIndx, c, indx):
  for rr in xrange(indx):
    if colIndx[rr] == c or rr + colIndx[rr] == c + indx or rr - colIndx[rr] == indx - c:
      return False
  return True

def eightQueenHelper(colIndx, indx, totalIndx):
  if indx == 8:
    totalIndx.append(colIndx[:])
    return
  for i in xrange(8):
     if diagChecker(colIndx, i, indx):
       colIndx[indx] = i
       eightQueenHelper(colIndx, indx + 1, totalIndx)
  return

def eightQueen():
  colIndx = [0] * 8
  totalIndx = []
  eightQueenHelper(colIndx, 0, totalIndx)
  return totalIndx
  
  
if __name__ == "__main__":
  print eightQueen()