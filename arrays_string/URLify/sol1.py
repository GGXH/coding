def URLify(s, true_size):
 space_no = 0
 for it in range(true_size):
  if s[it] == " ":
   space_no += 1
   
 if space_no == 0:
  return s
   
 ls = [" "] * len(s)
 
 for i in range(len(s)):
  ls[i] = s[i]
   
 realsize = true_size + 2 * space_no - 1
 for i in range(true_size - 1, -1, -1):
  print i
  print ls[i]
  if ls[i] != " ":
   ls[realsize] = ls[i]
  else:
   ls[realsize] = "0"
   realsize -= 1
   ls[realsize] = "2"
   realsize -= 1
   ls[realsize] = "%"
   space_no -= 1
  realsize -= 1
  if space_no == 0:
   break
 return "".join(ls)
 
if __name__ == "__main__":
 test_map = { 1: "a  ", 2: " a  ", 3: "a b  ", 4 : "  bc    " }
 
 for k in test_map:
  print k
  print URLify(test_map[k], k)
