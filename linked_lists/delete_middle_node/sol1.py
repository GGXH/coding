import sys

sys.path.append('../')

from sll import sll

def delete_middle(nd):
  nd.data = nd.next.data
  nd.next = nd.next.next
  
  

if __name__ == "__main__":
  slinked_list = sll.sll()
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  for it in value:
    slinked_list.addLast(it)
    
  print slinked_list.size
  print slinked_list
  
  nd = slinked_list.head
  for i in xrange(4):
    nd = nd.next
    
  print "to remove " + str(nd.data)
  delete_middle(nd)
  
  print "after remove"
  print slinked_list.size
  print slinked_list