def rotateMat(m):
  if len(m) < 2:
    return m
  N = len(m)
  for j in xrange(len(m) / 2):
    for i in xrange(j, len(m) - j - 1):
      tmp = m[N-1-j][i]
      m[N-1-j][i] = m[i][j]
      m[i][j] = m[j][N - 1 - i]
      m[j][N - 1 - i] = m[N-1-i][N-1-j]
      m[N-1-i][N-1-j] = tmp
  
  
if __name__ == "__main__":
   m = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
   
   for ms in m:
     print ms
     
   rotateMat(m)
   
   print "after rotation"
   
   for ms in m:
     print ms
