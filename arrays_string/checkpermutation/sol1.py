def check_permutation(s1, s2):
 if len(s1) != len(s2):
  return False
  
 collect_map = {}
 for s in s1:
  if s in collect_map:
   collect_map[s] += 1
  else:
   collect_map[s] = 1
 for s in s2:
  if s not in collect_map or collect_map[s] == 0:
   return False
  collect_map[s] -= 1
  
 for k, v in collect_map.items():
  if v != 0:
   return False
 return True
 
 
if __name__ == "__main__":
 test_str = ["abc", "cba", "eeb"]
 print check_permutation(test_str[0], test_str[1])
 
 print check_permutation(test_str[1], test_str[2])