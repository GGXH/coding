import sys

sys.path.append('../')

from sll import sll


def kth_to_last(nd, k):
  if not nd:
    return 0
    
  index = kth_to_last(nd.next, k) + 1
  
  if index == k:
    print "kth to the last data is " + str(nd.data)
  
  return index

  
  
if __name__ == "__main__":
  slinked_list = sll.sll()
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  key = 0
  for it in value:
    slinked_list.addLast(key, it)
    key += 1
    
  kth_to_last(slinked_list.head, 2)
  
 
 
 
 
 
 