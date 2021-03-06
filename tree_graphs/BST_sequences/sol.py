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
  
  
def BST_seque(nd):
  if nd is None:
    return []
    
  resl = BST_seque(nd.left)
  resr = BST_seque(nd.right)
  
  allresult = []
  if len(resl) > 0 and len(resr) > 0:
    for itl in resl:
      for itr in resr:
       allresult += mergeSequ(itl, itr, [nd.key])
  elif len(resl) > 0:
    for itl in resl:
      allresult += mergeSequ(itl, [], [nd.key])
  elif len(resr) > 0:
    for itr in resr:
      allresult += mergeSequ([], itr, [nd.key])
  else:
    allresult.append([nd.key])
  return allresult
  

def mergeSequ(first, second, prefix):
  if len(first) == 0 or len(second) == 0:
    res = prefix[:]
    for it in first:
      res.append(it)
    for it in second:
      res.append(it)
    return [res]
  
  allres = []
  prefix.append(first.pop(0))
  res = mergeSequ(first, second, prefix)
  for it in res:
   allres.append(it)
  first.insert(0, prefix.pop())
   
  prefix.append(second.pop(0))
  res = mergeSequ(first, second, prefix)
  for it in res:
   allres.append(it)
  second.insert(0, prefix.pop())
  
  return allres
  

  
  
if __name__ == "__main__":
  data = range(5)
  
  nd = minimal_tree(data)
  
  print BST_seque(nd)