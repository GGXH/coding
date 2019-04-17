def robotInAGrid(mat):
  path = []
  res = helper(mat, 0, 0, path)
  return path
 
 
 
def helper(mat, row, col, path):
  if row == len(mat) - 1 and col == len(mat[0]) - 1:
    path.append((row, col))
    return True
  
  if row >= len(mat) or col >= len(mat[0]) - 1:
    return False
    
  if mat[row][col] == -1:
    return False
    
  if helper(mat, row + 1, col, path) or helper(mat, row, col + 1, path):
    path.append((row, col))
    return True
  else:
    mat[row][col] = -1  
    return False
    
    
if __name__ == "__main__":
  mat = [[0, 0 , 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0]]
  print robotInAGrid(mat)