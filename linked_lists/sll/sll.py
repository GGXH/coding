class _node:
  def __init__(self, data, next = None):
    self._data = data
    self._next = next
    
  @property
  def data(self):
    return self._data
    
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
    
  def addFirst(self, data):
    self.head = _node(data, self._head)
    self.size += 1
  
  def addLast(self, data):
    nn = _node(data)
    if not self.head:
      self.head = nn
      self.last = self.head
    else:
      self.last.next = nn
      self.last = nn
    self.size += 1
    
  def insertAfter(self, data):
    s = self.size
    n = self.head
    nn = _node(data)
    while n:
      if n.data == data:
        nn.next = n.next
        n.next = nn
        self.size += 1
        break
      n = n.next
    return s != self.size
      
  def insertBefore(self, data):
    s = self.size
    nn = _node(data)
    if self.head.data == data:
      nn.next = self.head
      self.head = nn
      self.size += 1
    else:
      n = self.head
      while n.next:
        if n.next.data == data:
          nn.next = n.next
          n.next = nn
          self.size += 1
          break
        n = n.next
    return s != self.size
    
  def delete(self, data):
    if self.head.data == data:
      self.head = self.head.next
      self.size -= 1
    else:
      n = self.head
      while n.next:
        if n.next.data == data:
          n.next = n.next.next
          self.size -= 1
          break
        n = n.next