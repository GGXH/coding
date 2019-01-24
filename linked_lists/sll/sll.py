class _node:
  def __init__(self, data, key, next = None):
    self._data = data
    self._key = key
    self._next = next
    
  @property
  def data(self):
    return self._data
    
  @data.setter
  def data(self, data):
    self._data = data
    
  @property
  def key(self):
    return self._key
    
  @property
  def next(self):
    return self._next
  
  @next.setter
  def next(self, node):
    self._next = node

class sll:
  def __init__(self):
    self._head = None
    self._last = None
    self._size = 0
    
  def __str__(self):
    nd = self.head
    res = ""
    while nd:
      res += str(nd.data)
      res += ", "
      nd = nd.next
    return res
    
  @property
  def head(self):
    return self._head
    
  @head.setter
  def head(self, node):
    self._head = node
    
  @property
  def last(self):
    return self._last
    
  @last.setter
  def last(self, node):
    self._last = node
    
  @property
  def size(self):
    return self._size
    
  def getNode(self, key):
    nd = self.head
    while nd and nd.key != key:
      nd = nd.next
    return nd
    
  def addFirst(self, key, data):
    self.head = _node(data, key, self.head)
    self.size += 1
  
  def addLast(self, key, data):
    nn = _node(data, key)
    if not self.head:
      self.head = nn
      self.last = self.head
    else:
      self.last.next = nn
      self.last = nn
    self.size += 1
    
  def addLastNode(self, nd):
    self.last.next = nd
    self.last = nd
    self.size += 1
    
  def insertAfter(self, key1, key2, data):
    s = self.size
    n = self.head
    nn = _node(data, key2)
    while n:
      if n.key == key1:
        nn.next = n.next
        n.next = nn
        self.size += 1
        break
      n = n.next
    return s != self.size
      
  def insertBefore(self, key1, key2, data):
    s = self.size
    nn = _node(data, key2)
    if self.head.key == key1:
      nn.next = self.head
      self.head = nn
      self.size += 1
    else:
      n = self.head
      while n.next:
        if n.next.key == key1:
          nn.next = n.next
          n.next = nn
          self.size += 1
          break
        n = n.next
    return s != self.size
    
  def delete(self, key):
    if self.head.key == key:
      self.head = self.head.next
      self.size -= 1
    else:
      n = self.head
      while n.next:
        if n.next.key == key:
          n.next = n.next.next
          self.size -= 1
          break
        n = n.next