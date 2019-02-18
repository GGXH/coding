class Stack:
  def __init__(self, capacity):
    self._cap = capacity
    self._size = 0
    self._data = [0] * capacity
    
  def __str__(self):
    return ", ".join([str(i) for i in self._data]) + " size is " + str(self._size)
    
  def isEmpty(self):
    return self._size == 0
    
  def isFull(self):
    return self._size == self._cap
    
  def push(self, data):
    if self.isFull():
      raise "Stack is full"
    
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

class SetsOfStacks: 
  def __init__(self):
    self._size = 0
    self._stackCap = 10
    stck = Stack(self._stackCap)
    self._stackList = [stck]
    
  def __str__(self):
    i = 0
    sts = "size of stack is " + str(self._size)
    for st in self._stackList:
      sts += "stack " + str(i) + "\n"
      sts += st.__str__() + "\n"
      i += 1
    return sts
      
    
  def isEmpty(self):
    return self._size == 0
    
  def push(self, data):
    self._size += 1
    stck = self._stackList[-1]
    if stck.isFull():
      stck = Stack(self._stackCap)
      self._stackList.append(stck)
    stck.push(data)
  
  
  def pop(self):
    if self.isEmpty():
      raise "Sets of Stacks is empty"
    
    self._size -= 1
    stck = self._stackList[-1]
    while stck.isEmpty():
      self._stackList.pop()
      stck = self._stackList[-1]
    
    return stck.pop()
    
  def popAt(self, indx):
    if len(self._stackList) < indx + 1:
      raise "Stack at " + str(indx) + " does not exist"
      
    if self._stackList[indx].isEmpty():
      raise "Stack at " + str(indx) + " is empty"
      
    self._size -= 1
      
    return self._stackList[indx].pop()
    
    
if __name__ == "__main__":
   sos = SetsOfStacks()
   
  
   for it in xrange(30):
      sos.push(it)
      
   print sos
      
   for it in xrange(10):
      print sos.popAt(1)
      print sos

   while not sos.isEmpty():
      print sos.pop()
      print sos
