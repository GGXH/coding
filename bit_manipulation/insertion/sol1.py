def insertion(M, N, i, j):
  mask = ( 1 << ( j - i + 1 + 1 ) ) - 1
  mask = ~( mask << i )
  return N & mask | M << i
  
if __name__ == "__main__":
   N = 0b10000000000
   M = 0b10011
   
   res = insertion(M, N, 2, 6)
   
   print bin(res)
  
  