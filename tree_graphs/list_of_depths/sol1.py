import Queue

class node:
  def __init__(self, key, left=None, right=None):
    self._key = key
    self._left = left
    self._right = right
    
  def __str__(self):
     return str(self.key)
#    res = "m:" + str(self.key)
#    res += " "
#    if self.left is not None:
#      res += "l:" + self.left.__str__()
#    res += " "
#    if self.right is not None:
#      res += "r:" + self.right.__str__()
#    return res
    
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
      
class sllnode:
  def __init__(self, key):
    self._key = key
    self.next = None
    
  def __str__(self):
    res = str(self.key)
    if self.next is not None:
      res += " " + self.next.__str__()
    return res
    
  @property
  def key(self):
    return self._key
    
  @property
  def next(self):
    return self._next
    
  @next.setter
  def next(self, nd):
    self._next = nd
    
    
def list_of_depths(nd):
  q = Queue.Queue()
  res = []
  
  q.put((nd, 0))
  snd = None
  pre_indx = -1
  while not q.empty():
    nd, indx = q.get()
    if nd.left is not None:
      q.put((nd.left, indx + 1))
    if nd.right is not None:
      q.put((nd.right, indx + 1))
    if pre_indx == indx:
        snd.next = sllnode(nd)
        snd = snd.next
    else:
       snd = sllnode(nd)
       res.append(snd)
       pre_indx = indx
  return res
    
    
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
    
if __name__ == "__main__":
  data = range(10)
  
  nd = minimal_tree(data)
  
  for it in list_of_depths(nd):
    print it