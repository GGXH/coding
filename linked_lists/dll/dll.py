class _node:
  def __init__(self, data, next = None, before = None):
    self._data = data
    self._next = next
    self._before = before
    
  @property
  def before(self):
    return self._before
    
  @before.setter
  def before(self, before):
    self._before = before
  
  @property
  def data(self):
    return self._data
    
  @property
  def next(self):
    return self._next
  
  @next.setter
  def next(self, node):
    self._next = node

class dll:
  def __init__(self):
    self._head = None
    self._last = None
    self._size = 0
    
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
    self.head = _node(data, next = self._head)
    self.size += 1
  
  def addLast(self, data):
    nn = _node(data)
    if not self.head:
      self.head = nn
      self.last = self.head
    else:
      self.last.next = nn
      nn.before = self.last
      self.last = nn
    self.size += 1
    
  def insertAfter(self, key, data):
    s = self.size
    n = self.head
    nn = _node(data)
    while n:
      if n.data == key:
        nn.next = n.next
        nn.before = n
        if n.next:
          n.next.before = nn
        n.next = nn
        self.size += 1
        break
      n = n.next
    return s != self.size
      
  def insertBefore(self, key, data):
    s = self.size
    nn = _node(data)
    if self.head.data == key:
      self.addFirst(data)
    else:
      n = self.head
      while n.next:
        if n.next.data == key:
          nn.next = n.next
          nn.before = n
          n.next.before = nn
          n.next = nn
          self.size += 1
          break
        n = n.next
    return s != self.size
    
  def delete(self, data):
    if self.head.data == data:
      self.head = self.head.next
      self.head.before = None
      self.size -= 1
    else:
      n = self.head
      while n.next:
        if n.next.data == data:
          if n.next.next:
            n.next.next.before = n
          n.next = n.next.next
          self.size -= 1
          break