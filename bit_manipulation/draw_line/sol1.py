def drawLine(screen, width, x1, x2, y):
  l = x2 - x1 + 1
  base = 2**l - 1
  print l, 2**l, base, bin(base)
  totalspace = y * width + x1
  base <<= totalspace
  screen |= base
  return screen
  
  
if __name__ == "__main__":
  screen = 0
  width = 5
  screen = drawLine(screen, width, 1, 3, 1)
  base = 2**width - 1
  print bin(screen & base)
  screen >>= width
  print bin(screen & base)
  screen >>= width
  print bin(screen & base)