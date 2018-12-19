def check_permutation(s1, s2):
 if len(s1) != len(s2):
  return False
  
 return sorted(s1) == sorted(s2)
 
 
if __name__ == "__main__":
 test_str = ["abc", "cba", "eeb"]
 print check_permutation(test_str[0], test_str[1])
 
 print check_permutation(test_str[1], test_str[2])