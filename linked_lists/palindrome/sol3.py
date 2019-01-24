import sys

sys.path.append("../")

from sll import sll

class result:
  def __init__(self, node, res):
    self._node = node
    self._res = res
    
  @property
  def node(self):
    return self._node
    
  @node.setter
  def node(self, node):
    self._node = node
  
  @property
  def res(self):
    return self._res
    
  @res.setter
  def res(self, res):
    self._res = res

def ispalrecur(nd, length):
  if nd is None or length <= 0:
    return result(nd, True)
  elif length == 1:
    return result(nd.next, True)
    
  res = ispalrecur(nd.next, length - 2)
  
  if not res.res or res.node is None:
    return res
  
  res.res = res.node.data == nd.data
  
  res.node = res.node.next
  
  return res

def ispal(slinked_list):
  return ispalrecur(slinked_list.head, slinked_list.size).res

    
if __name__ == "__main__":
  slinked_list1 = sll.sll()
  key = 0
  value = [7, 1, 8, 1, 7]
  for it in value:
    slinked_list1.addLast(key, it)
    key += 1
  
  print ispal(slinked_list1)
 