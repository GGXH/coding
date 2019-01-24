import sys

sys.path.append('../')

from sll import sll


def loop_detect(slinked_list):
  nd = slinked_list.head
  nd_f = slinked_list.head.next
  
  while nd and nd_f and nd != nd_f:
    nd = nd.next
    nd_f = nd_f.next
    if nd_f:
      nd_f = nd_f.next
    else:
      return False
      
  if not nd or not nd_f:
    return False
    
  print nd.data
    
  return True
  
if __name__ == "__main__":
  slinked_list1 = sll.sll()
  key = 0
  value = [7, 1, 6, 5, 8]
  for it in value:
    slinked_list1.addLast(key, it)
    key += 1
    
  nd = slinked_list1.getNode(2)
  print nd.data
  slinked_list1.addLastNode(nd)
    
  print "detect"
    
  print loop_detect(slinked_list1)
  