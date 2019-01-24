import sys

sys.path.append('../')

from sll import sll


def kth_to_last(slinked_list, k):
  count = slinked_list.size
    
  if k > count:
    return None;
    
  nd = slinked_list.head
  i = 1
  while i <= count - k:
    nd = nd.next
    i += 1
  
  return nd.data
  
  
if __name__ == "__main__":
  slinked_list = sll.sll()
  key = 0
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  for it in value:
    slinked_list.addLast(key, it)
    key += 1
    
  print kth_to_last(slinked_list, 1)
  
 
 
 
 
 
 