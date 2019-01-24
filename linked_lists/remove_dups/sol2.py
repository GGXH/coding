import sys

sys.path.append('../')

from sll import sll

def remove_dups(slinked_list):
  nd = slinked_list.head
  
  if not nd:
    return

  while nd:
    nd_a = nd.next
    while nd_a:
      if nd_a.data == nd.data:
        key = nd_a.key
        nd_a = nd_a.next
        slinked_list.delete(key)
      else:
        nd_a = nd_a.next
    nd = nd.next



if __name__ == "__main__":
  slinked_list = sll.sll()
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  key = 0
  for it in value:
    slinked_list.addLast(key, it)
    key += 1
    
  print slinked_list.size
  print slinked_list
    
  remove_dups(slinked_list)
  
  nd = slinked_list.head
  
  print "after remove"
  print slinked_list.size
  print slinked_list
  