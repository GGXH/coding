class Stack:
  def __init__(self):
    self._size = 0
    self._data = []
    
  def __str__(self):
    return ", ".join([str(i) for i in self._data]) + " size is " + str(self._size)
    
  def isEmpty(self):
    return self._size == 0
    
  def push(self, data):
    if len(self._data) == self._size:
      self._data.append(data)
    else:
      self._data[self._size] = data
    self._size += 1
    
  def pop(self):
    if self.isEmpty():
      raise "Stack is empty"
    
    self._size -= 1
    return self._data[self._size]
    
  def top(self):
    if self.isEmpty():
      raise "Stack is empty"
      
    return self._data[self._size - 1]
    
    
class MyQueue:
   def __init__(self):
     self._stacka = Stack()
     self._stackb = Stack()
     self._size = 0
     
     
   def isEmpty(self):
     return self._size == 0
     
   def push(self, data):
     self._size += 1
     self._stackb.push(data)
     
   def pop(self):
     if self.isEmpty():
       raise "MyQueue is empty"
       
     if self._stacka.isEmpty():
       self._moveStack()
     
     self._size -= 1
     return self._stacka.pop()
       
   def _moveStack(self):
     while not self._stackb.isEmpty():
       self._stacka.push(self._stackb.pop())
       
       
if __name__ == "__main__":
   sos = MyQueue()
   
  
   for it in xrange(30):
      sos.push(it)
      
   for it in xrange(10):
      print sos.pop()
      
   for it in xrange(20):
      sos.push(it)

   while not sos.isEmpty():
      print sos.pop()