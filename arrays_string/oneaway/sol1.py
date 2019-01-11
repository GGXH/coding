def oneaway(str1, str2):
  if str1 == str2:
    return True
    
  if len(str1) < len(str2):
    return oneaway(str2, str1)
    
  if len(str1) - len(str2) > 1:
    return False
    
  len_diff = len(str1) - len(str2)
  allow_diff = 1
  j = 0
  for i in xrange(len(str1)):
    if j < len(str2) and str1[i] != str2[j]:
      if allow_diff == 0:
         return False
      else:
         allow_diff -= 1
         j -= len_diff
    j += 1
  return True


if __name__ == "__main__":
  test_list = [["pale", "ple"], ["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["bake", "pale"]]
  
  for tl in test_list:
    print tl
    print oneaway(*tl)