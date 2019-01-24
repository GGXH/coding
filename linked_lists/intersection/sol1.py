import sys

sys.path.append('../')

from sll import sll

def intersect_rec(nd1, nd2):
  if nd1.next is None and nd2.next is None:
    if nd1.data == nd2.data:
       return nd1
    else:
       return None
  
  res = intersect_rec(nd1.next, nd2.next)
  
  if res is not None:
    return nd1 if nd1.data == nd2.data else res
  return None

def intersect(sll1, sll2):
  if sll1.size < sll2.size:
    return intersect(sll2, sll1)
    
  ds = sll1.size - sll2.size
  
  nd1 = sll1.head
  for i in xrange(ds):
    nd1 = nd1.next
    
  nd2 = sll2.head
  
  return intersect_rec(nd1, nd2)
  
  
if __name__ == "__main__":
  slinked_list1 = sll.sll()
  key = 0
  value = [7, 1, 6]
  for it in value:
    slinked_list1.addLast(key, it)
    key += 1
  slinked_list2 = sll.sll()
  key = 0
  value = [5, 9, 7, 1, 6]
  for it in value:
    slinked_list2.addLast(key, it)
    key += 1
    
  print intersect(slinked_list1, slinked_list2).data


