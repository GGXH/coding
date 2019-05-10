

def helper(lc, rc, maxc):
  if lc == maxc and rc == maxc:
    return []
  if lc == maxc:
    return [")" * (maxc - rc)]
  subres = helper(lc + 1, rc, maxc)
  res = []
  for p in subres:
    res.append("(" + p)
  if lc > rc:
    subres = helper(lc, rc + 1, maxc)
    for p in subres:
      res.append(")" + p)
  return res
  


def parens(n):
  return helper(0, 0, n)
  
if __name__ == "__main__":
  print parens(3)
  
  print parens(1)
  
  print parens(2)