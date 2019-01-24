import sys

sys.path.append('../')

from sll import sll

def paddling(slinked_list, num):
  key = slinked_list.size
  for i in xrange(num):
    slinked_list.addFirst(key, 0)

def psum(nd1, nd2):
  if not nd1 and not nd2:
    return sll._node(0, 0)
    
  nd_n = psum(nd1.next, nd2.next)
  
  data = nd1.data + nd2.data + nd_n.data
  carry = data // 10
  data = data % 10
  
  nd_n.data = data
  
  nd_c = sll._node(carry, 0)
  nd_c.next = nd_n
  
  return nd_c


def sum_lists(sll1, sll2):
  if not sll1:
    return sll2
    
  if not sll2:
    return sll1
    
  if sll1.size > sll2.size:
    paddling(sll2, sll1.size - sll2.size)
  else:
    paddling(sll1, sll2.size - sll1.size)
    
  nd1 = sll1.head
  nd2 = sll2.head
    
  nd = psum(nd1, nd2)
  
  sll3 = sll.sll()
  sll3.head = nd
    
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