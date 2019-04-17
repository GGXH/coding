import collections

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
  runningLib = collections.defaultdict(int)
  return helper(nd, 0, target, runningLib)
  
  
def helper(nd, runningSum, target, runningLib):
  if nd is None:
    return 0
  
  runningSum += nd.key
  sumDiff = runningSum - target
  cnt = runningLib.get(sumDiff, 0)
  
  if runningSum == target:
    cnt += 1
  
  runningLib[runningSum] += 1
  cnt += helper(nd.left, runningSum, target, runningLib)
  cnt += helper(nd.right, runningSum, target, runningLib)
  runningLib[runningSum] -= 1
  return cnt
  
if __name__ == "__main__":
  data = range(10)
  
  nd = minimal_tree(data)
  
  print nd
  
  print pathwithsum(nd, 15)