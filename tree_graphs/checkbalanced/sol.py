class node:
  def __init__(self, key, left=None, right=None):
    self._key = key
    self._left = left
    self._right = right
    
  def __str__(self):
    res = ""
    if self.left is not None:
      res += self.left.__str__()
    res += " " + str(self.key)
    if self.right is not None:
      res += self.right.__str__()
    res += " "
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
    

def ifBalanced(nd):
  if nd is None:
    return 0
    
  leftsize = ifBalanced(nd.left)
  rightsize = ifBalanced(nd.right)
  
  if leftsize < 0 or rightsize < 0:
    return -1
  
  if abs(leftsize - rightsize) > 1:
    return -1
  else:
    return max(leftsize, rightsize) + 1
  
if __name__ == "__main__":
  data = range(10)
  
  nd = minimal_tree(data)
  
  print nd
  
  print ifBalanced(nd) > 0