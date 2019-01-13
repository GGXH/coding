def coutstringCompress(s):
  str_count = 0
  cnt = 0
  marker = ""
  for i in xrange(len(s)):
    if marker == "":
      marker = s[i]
      cnt = 1
    elif marker == s[i]:
      cnt += 1
    else:
      marker = s[i]
      cnt = 1
      str_count += 2
  str_count += 2
  return str_count


def stringCompress(s):
  if len(s) < 3:
    return s

  new_str_len = coutstringCompress(s)
  if new_str_len >= len(s):
    return s

  new_str = ["a"] * new_str_len
  pos = 0
  cnt = 0
  marker = ""
  for i in xrange(len(s)):
    if marker == "":
      marker = s[i]
      cnt = 1
    elif marker == s[i]:
      cnt += 1
    else:
      new_str[pos] = marker
      pos += 1
      new_str[pos] = str(cnt)
      pos += 1
      marker = s[i]
      cnt = 1
  new_str[pos] = marker
  pos += 1
  new_str[pos] = str(cnt)
  return "".join(new_str)
  
  
if __name__ == "__main__":
  test_str = ["aabccccca", "aaaaa", "aa", "aaa", "baa"];
  for t in test_str:
    print t, stringCompress(t)