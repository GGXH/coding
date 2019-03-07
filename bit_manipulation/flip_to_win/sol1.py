def flip_to_win(input):
  l = input.bit_length()
  marker = 1
  current_count = 0
  last_count = 0
  seespace = False
  max_len = 0
  for i in xrange(l):
    if input & marker != 0:
      current_count += 1
    else:
      ll = last_count + 1 + current_count
      if max_len < ll:
        max_len = ll
      last_count = current_count
      current_count = 0
    marker <<= 1
  ll = last_count + 1 + current_count
  if max_len < ll:
     max_len = ll
  return max_len
  
  
if __name__ == "__main__":
  print flip_to_win(1775)
      