def palin_perm(input_str):
  marker = 0
  od_a = ord('a')
  for s in input_str:
   if s == " ":
     continue
   else:
    od_diff = ord(s.lower()) - od_a
    if od_diff >= 0:
      marker ^= 1 << od_diff
  return marker & (marker - 1) == 0
  
  
  
if __name__ == "__main__":
  test_list = ["Tact Coa", "Tact Coaw", "Tact wCoaw"]
  
  for t in test_list:
    print t
    print palin_perm(t)