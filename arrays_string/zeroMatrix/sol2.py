def zeroMat(m):
  if len(m) == 0 or len(m[0]) == 0:
    return
    
  N = len(m)
  M = len(m[0])
  
  row_zero = False
  col_zero = False
  for i in xrange(N):
    if m[i][0] == 0:
      col_zero = True
      break
  
  for j in xrange(M):
    if m[0][j] == 0:
      row_zero = True
      break
      
  for i in xrange(1, N):
    for j in xrange(1, M):
      if m[i][j] == 0:
        m[i][0] = 0
        m[0][j] = 0
  
  for i in xrange(N):
    if m[i][0] == 0:
      for j in xrange(1, M):
        m[i][j] = 0
        
  for j in xrange(M):
    if m[0][j] == 0:
      for i in xrange(1, N):
        m[i][j] = 0
        
  if row_zero:
    for j in xrange(0, M):
      m[0][j] = 0
      
  if col_zero:
    for i in xrange(0, N):
      m[i][0] = 0


if __name__ == "__main__":
  m = [[1, 2, 0, 4], [0, 2, 3, 4], [3, 4, 5, 6]]
  
  for ms in m:
    print ms
    
  zeroMat(m)
  
  print "after zero mat"
  
  for ms in m:
    print ms