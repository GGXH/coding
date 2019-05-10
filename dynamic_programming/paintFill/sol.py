

def helper(colorMap, i, j, newColor, orgColor):
  if i < 0 or i >= len(colorMap) or j < 0 or j >= len(colorMap[0]):
    return
  if colorMap[i][j] != orgColor:
    return
  colorMap[i][j] = newColor
  helper(colorMap, i - 1, j, newColor, orgColor)
  helper(colorMap, i + 1, j, newColor, orgColor)
  helper(colorMap, i, j - 1, newColor, orgColor)
  helper(colorMap, i, j + 1, newColor, orgColor)


def paintfill(colorMap, i, j, newColor):
  if colorMap[i][j] == newColor:
    return
    
  orgColor = colorMap[i][j]
  helper(colorMap, i, j, newColor, orgColor)
    
    
if __name__ == "__main__":
  colorMap = [ [1, 1, 1], [2, 1, 2], [1, 1, 3] ]
  
  paintfill(colorMap, 1, 1, 4)
  
  print colorMap