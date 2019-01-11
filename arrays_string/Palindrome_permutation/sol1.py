def palin_perm(input_str):
  count_dict = {}
  for s in input_str:
   if s == " ":
     continue
   elif s.lower() in count_dict:
     count_dict[s.lower()] += 1
   else:
     count_dict[s.lower()] = 1
  odd = False
  for s in count_dict:
    if count_dict[s] % 2 == 1:
      if odd:
        return False
      else:
        odd = True
  return True
  
  
  
if __name__ == "__main__":
  test_list = ["Tact Coa", "Tact Coaw", "Tact wCoaw"]
  
  for t in test_list:
    print t
    print palin_perm(t)