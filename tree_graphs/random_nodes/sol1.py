import random

class node:
  def __init__(self, key, left=None, right=None, size = 1):
    self._key = key
    self._left = left
    self._right = right
    self._size = size
    if self._left is not None:
      self._size += self._left.size
    if self._right is not None:
      self._size += self._right.size
    
  def __str__(self):
    res = "m:" + str(self.key) + "(" + str(self.size) + ")"
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
    if self.right is not None:
      self.size -= self.right.size
    self._right = right
    if right is not None:
      self.size += right.size
    
  @property
  def left(self):
    return self._left
    
  @left.setter
  def left(self, left):
    print left
    if self.left is not None:
      self.size -= self.left.size
    self._left = left
    print left
    if left is not None:
      self.size += left.size
      print self.size
  
  @property
  def size(self):
    return self._size
    
  @size.setter
  def size(self, size):
    self._size = size


def minimal_tree(arr):
  if len(arr) == 0:
    return None
    
  if len(arr) == 1:
    return node(arr[0])
    
  mid = len(arr) / 2
  nd = node(arr[mid])
  nd.left = minimal_tree(arr[:mid])
  nd.right = minimal_tree(arr[mid+1:])
  if nd.left is not None:
    nd.size += nd.left.size
  if nd.right is not None:
    nd.size += nd.right.size
  return nd
  
  
def getRandomNd(nd, rnd = -1, start = 0, end = 1.):
  if rnd < 0:
    rnd = random.random()
    
  uplim = (end - start) / nd.size
  if rnd <= uplim + start:
    return nd.key
  
  lowlim = uplim
  if nd.left is not None:
    uplim += nd.left.size * ( end - start ) / nd.size
    if rnd <= uplim + start:
      return getRandomNd(nd.left, rnd, lowlim + start, uplim + start)
  
  return getRandomNd(nd.right, rnd, uplim + start, 1.)
  
if __name__ == "__main__":
  data = range(10)
  
  nd = minimal_tree(data)
  
  print nd
  
  for i in xrange(30):
    print getRandomNd(nd)
  