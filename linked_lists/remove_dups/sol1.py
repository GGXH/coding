import sys

sys.path.append('../')

from sll import sll

def remove_dups(slinked_list):
  value = {}
  nd = slinked_list.head
  
  while nd:
    if nd.data in value:
      value[nd.data].append(nd.key)
    else:
      value[nd.data] = [nd.key]
    nd = nd.next
  
  for k, v in value.items():
    while len(v) > 1:
      t = v.pop()
      slinked_list.delete(t)


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
  