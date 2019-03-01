
class node:
  def __init__(self, key, left=None, right=None, parent=None):
    self._key = key
    self._left = left
    self._right = right
    self._parent = parent
    
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
    
  @property
  def parent(self):
    return self._parent
    
def minimal_tree(arr, pnd):
  if len(arr) == 0:
    return None
    
  if len(arr) == 1:
    return node(arr[0], parent = pnd)
    
  mid = len(arr) / 2
  nd = node(arr[mid], parent = pnd)
  nd.left = minimal_tree(arr[:mid], nd)
  nd.right = minimal_tree(arr[mid+1:], nd)
  return nd
  
  
def sucessor(root, val):
  nd = findNd(root, val)
  
  if nd is None:
    return None

  if nd.right is not None:
    return getLeftMostNd(nd.right).key
    
  pnd = nd.parent
  
  #print pnd
  #print 
  
  while pnd:
   if nd == pnd.left:
     return pnd.key
   nd = pnd
   pnd = pnd.parent
   
  return None

def getLeftMostNd(root):
  if root is None:
    return None
  
  if root.left is not None:
    return getLeftMostNd(root.left)
  
  return root
  
def findNd(nd, val):
  if nd is None:
    return nd
  
  if nd.key == val:
    return nd
  
  left = findNd(nd.left, val)
  if left is not None:
    return left
    
  right = findNd(nd.right, val)
  if right is not None:
    return right
    
  return None
  
  
if __name__ == "__main__":
  data = range(10)
  
  nd = minimal_tree(data, None)
  
  #print sucessor(nd, 4)
  
  for i in range(10):
   print sucessor(nd, i)