def zeroMat(m):
  if len(m) == 0 or len(m[0]) == 0:
    return

  M = len(m)
  N = len(m[0])
  
  row_zero = [0] * M
  col_zero = [0] * N
  
  for i in xrange(M):
    for j in xrange(N):
      if m[i][j] == 0:
        row_zero[i] = 1
        col_zero[j] = 1
  
  for i in xrange(M):
    if row_zero[i]:
      for j in xrange(N):
        m[i][j] = 0
  for j in xrange(N):
    if col_zero[j]:
      for i in xrange(M):
        m[i][j] = 0
        
        
if __name__ == "__main__":
  m = [[1, 2, 0, 4], [0, 2, 3, 4], [3, 4, 5, 6]]
  
  for ms in m:
    print ms
    
  zeroMat(m)
  
  print "after zero mat"
  
  for ms in m:
    print ms