import sys

sys.path.append('../')

from sll import sll

def partition(slinked_list, x):
  nd = slinked_list.head
  
  while nd:
    if nd != slinked_list.head and nd.data < x:
      nd_a = nd.next
      slinked_list.delete(nd.key)
      slinked_list.addFirst(nd.key, nd.data)
      nd = nd_a
    else:
      nd = nd.next

if __name__ == "__main__":
  slinked_list = sll.sll()
  key = 0
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  for it in value:
    slinked_list.addLast(key, it)
    key += 1
    
  print slinked_list
  
  partition(slinked_list, 3)
  
  print "after partition"
  print slinked_list