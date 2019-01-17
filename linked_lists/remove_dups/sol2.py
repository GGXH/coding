import sys

sys.path.append('../')

from sll import sll

def remove_dups(slinked_list):
  nd = slinked_list.head
  
  if not nd:
    return
  
  nd_a = nd.next
  
  while nd:
    while nd_a:
      if nd_a.data == nd.data:
        if nd == slinked_list.head:
          slinked_list.delete(nd_a.data)
          nd = slinked_list.head
          nd_a = nd.next
          continue
        else:
          nd = nd.next
          slinked_list.delete(nd_a.data)
          nd_a = nd.next
      else:
        nd_a = nd_a.next
    nd = nd.next



if __name__ == "__main__":
  slinked_list = sll.sll()
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  for it in value:
    slinked_list.addLast(it)
    
  print slinked_list.size
  print slinked_list
    
  remove_dups(slinked_list)
  
  nd = slinked_list.head
  
  print "after remove"
  print slinked_list.size
  print slinked_list
  