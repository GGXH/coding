import sys

sys.path.append('../')

from sll import sll

def sum_lists(sll1, sll2):
  nd1 = sll1.head
  nd2 = sll2.head
  
  sll3 = sll.sll()
  
  add_one = 0
  key = 0
  while nd1 and nd2:
    data = nd1.data + nd2.data + add_one
    add_one = data // 10
    data = data % 10
    sll3.addLast(key, data)
    key += 1
    nd1 = nd1.next
    nd2 = nd2.next
    
  nd = None
  if nd1:
    nd = nd1
  elif nd2:
    nd = nd2
    
  while nd:
    data = nd.data + add_one
    add_one = data // 10
    data %= 10
    sll3.add_Last(key, data)
    key ++ 1
    nd = nd.next
    
  return sll3
  
if __name__ == "__main__":
  slinked_list1 = sll.sll()
  key = 0
  value = [7, 1, 6]
  for it in value:
    slinked_list1.addLast(key, it)
    key += 1
  slinked_list2 = sll.sll()
  key = 0
  value = [5, 9, 2]
  for it in value:
    slinked_list2.addLast(key, it)
    key += 1
    
  print slinked_list1
  print slinked_list2
  
  print "add"
  
  print sum_lists(slinked_list1, slinked_list2)