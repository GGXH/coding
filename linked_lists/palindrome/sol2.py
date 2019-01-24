import sys

sys.path.append("../")

from sll import sll

def ispal(slinked_list):
  if slinked_list.size < 3:
    return True
 
  stack_store = []
  
  slow = slinked_list.head
  fast = slow.next
  stack_store.append(slow.data)
  
  while fast and fast.next:
    slow = slow.next
    stack_store.append(slow.data)
    fast = fast.next.next
    
  if not fast:
    stack_store.pop()
    slow = slow.next
  
  slow = slow.next
  
  while slow:
    data = stack_store.pop()
    if data != slow.data:
      return False
    slow = slow.next
  return True
    
if __name__ == "__main__":
  slinked_list1 = sll.sll()
  key = 0
  value = [7]
  for it in value:
    slinked_list1.addLast(key, it)
    key += 1
  
  print ispal(slinked_list1)
 