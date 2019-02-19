class node:
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

class AnimalShelter:
  def __init__(self):
     self._head = node(0, "")
     self._tail = None
     self._beforeDog = self._head
     self._beforeCat = self._head
     self._size = 0
     self._catsize = 0
     self._dogsize = 0
     
  def enqueue(self, animal, key)
    nd = node(animal, key)
    if type == "cat":
      self._catsize += 1
    elif type == "dog":
      self._dogsize += 1
    else:
      raise "unknown animal"

    if self._tail is None:
      self._head.next = nd
    self._tail = nd
    
    if type == "cat" and self._catsize == 1:
       self.updateAnimalHead(type)
    elif type == "dog" and self._dogsize == 1:
       self.updateAnimalHead(type)
       
  def dequeueAll(self):
    nd = self._head
    if nd.next is None:
       raise "No animal"
    
    if nd.key == "cat":
      self._catsize -= 1
    elif nd.key == "dog":
      self._dogsize -= 1
    
    res = nd.next
    
    nd.next = nd.next.next
    self.updateAnimalHead(res.key)
    
    return res
  
  def dequeueCat(self):
    nd = self._beforeCat
    if nd.next is None or nd == self._head:
       raise "No cat"
    
    self._catsize -= 1
    res = nd.next
    nd.next = nd.next.next
    self.updateAnimalHead(res.key)
    return res
    
  def dequeueDog(self):
    nd = self._beforeDog
    if nd.next is None or nd == self._head:
       raise "No dog"
    
    self._dogsize -= 1
    res = nd.next
    nd.next = nd.next.next
    self.updateAnimalHead(res.key)
    
    return res

  
  
  def updateAnimalHead(self, type):
     nd = self._head
     while nd.next:
       if nd.next.key == key:
         break
     if type == "dog":
      self._beforeDog = nd
     elif type == "cat":
      self._beoferCat = nd