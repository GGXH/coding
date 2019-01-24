import sys

sys.path.append('../')

from sll import sll


def kth_to_last(slinked_list, k):
   nd = slinked_list.head
   
   nd_a = nd
   i = 0
   while i < k:
     nd_a = nd_a.next
     i += 1
     if not nd_a:
       if i == k:
         return nd.data
       else:
         return None
   
   while nd_a:
     nd_a = nd_a.next
     nd = nd.next
     
   return nd.data
  
  
if __name__ == "__main__":
  slinked_list = sll.sll()
  value = [1, 2, 3, 1, 3, 4, 5, 1, 2, 3]
  key = 0
  for it in value:
    slinked_list.addLast(key, it)
    key += 1
    
  print kth_to_last(slinked_list, 3)
  
 
 
 
 
 
 