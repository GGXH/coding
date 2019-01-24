import sys

sys.path.append("../")

from sll import sll

def ispal(slinked_list):
  rev_sll = sll.sll()
  
  nd = slinked_list.head
  
  while nd:
    rev_sll.addFirst(nd.key, nd.data)
    nd = nd.next
    
  nd = slinked_list.head
  nd_r = rev_sll.head
  
  while nd and nd_r:
    if nd.data != nd_r.data:
      return False
    nd = nd.next
    nd_r = nd_r.next
      
  return True
    
if __name__ == "__main__":
  slinked_list1 = sll.sll()
  key = 0
  value = [7, 1, 1, 7]
  for it in value:
    slinked_list1.addLast(key, it)
    key += 1
  
  print ispal(slinked_list1)
 