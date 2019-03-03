class node:
  def __init__(self, key, left=None, right=None):
    self._key = key
    self._left = left
    self._right = right
    
  def __str__(self):
    res = "m:" + str(self.key)
    res += " "
    if self.left is not None:
      res += "l:" + self.left.__str__()
    res += " "
    if self.right is not None:
      res += "r:" + self.right.__str__()
    return res
    
  @property
  def key(self):
    return self._key
    
  @property
  def right(self):
    return self._right
    
  @right.setter
  def right(self, right):
    self._right = right
    
  @property
  def left(self):
    return self._left
    
  @left.setter
  def left(self, left):
    self._left = left


def minimal_tree(arr):
  if len(arr) == 0:
    return None
    
  if len(arr) == 1:
    return node(arr[0])
    
  mid = len(arr) / 2
  nd = node(arr[mid])
  nd.left = minimal_tree(arr[:mid])
  nd.right = minimal_tree(arr[mid+1:])
  return nd

def isSubtree(nd1, nd2):
  if nd2 is None:
    return True
    
  if nd1 is None:
    return False
    
  if nd1.key == nd2.key:
    return isSameTree(nd1, nd2)
    
  return isSubtree(nd1.left, nd2) or isSubtree(nd1.right, nd2)
  
def isSameTree(nd1, nd2):
  if nd1 is None and nd2 is None:
    return True
  
  if nd1 is None or nd2 is None:
    return False
    
  if nd1.key != nd2.key:
    return False
    
  return isSameTree(nd1.left, nd2.left) and isSameTree(nd1.right, nd2.right)
  
  
if __name__ == "__main__":
  data = range(10)
  
  nd = minimal_tree(data)
  
  subnd = node(1)
  subnd1 = node(0)
  subnd.left = subnd1
  
  print isSubtree(nd, subnd)