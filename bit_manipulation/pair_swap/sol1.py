def pairSwap(input):
  bitlen = input.bit_length()
  base1 = 3
  base2 = -1 << 2
  while base1.bit_length() - bitlen <= 1:
    if ( input | base1 != input and input & base2 != input):
      input ^= base1
    base1 <<= 2
    base2 <<= 2
    base2 += 3
  return input
  
  
def pairSwap1(input):
  base1 = 0xaaaaaaaaaaaaa
  base2 = 0x5555555555555
  return ( ( input & base1 ) >> 1 ) | ( ( input & base2 ) << 1)
  
if __name__ == "__main__":
  input = 273
  
  res = pairSwap1(input)
  print bin(input)
  print bin(res)