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

def pathwithsum(nd, target):
  if nd is None:
     return 0
  return helper(nd, nd, nd.key, - nd.key, target)
  
  
def helper(nd, cur_nd, basesum, presum, target):
  if nd is None:
    return 0
  
  cnt = 0
  if cur_nd is None:
    if nd.left is not None:
      presum = basesum
      basesum += nd.left.key
      cnt += helper(nd.left, nd.left, basesum, presum, target)
      basesum -= nd.left.key
    if nd.right is not None:
      presum = basesum
      basesum += nd.right.key
      cnt += helper(nd.right, nd.right, basesum, presum, target)
      basesum -= nd.right.key
    return cnt

  print nd.key, cur_nd.key, basesum, presum, target

  
  currsum = presum + cur_nd.key
  if currsum - basesum == target:
    cnt += 1
  
  cnt += helper(nd, cur_nd.left, basesum, currsum, target)
  
  currsum = presum + cur_nd.key
  cnt += helper(nd, cur_nd.right, basesum, currsum, target)
  return cnt


if __name__ == "__main__":
  data = range(5)
  
  nd = minimal_tree(data)
  
  print pathwithsum(nd, 5)