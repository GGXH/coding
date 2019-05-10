

def coinsHelper(n, baseCoin, indx, countMat):
  if countMat[indx][n] > 0:
    return countMat[indx][n]
  
  if indx == len(baseCoin) - 1:
    return 1
  
  for i in xrange(int(n/baseCoin[indx]) + 1):
    countMat[indx][n] += coinsHelper(n - i * baseCoin[indx], baseCoin, indx + 1, countMat)
  
  return countMat[indx][n]

def coins(n):
  baseCoin = [25, 10, 5, 1]
  countMat = [ [ 0] * ( n + 1 ) for _ in xrange(len(baseCoin)) ]
  indx = 0
  return coinsHelper(n, baseCoin, indx, countMat)
  

if __name__ == "__main__":
  n = 8
  #coins(n)
  print coins(n)
  
  n = 30
  print coins(n)