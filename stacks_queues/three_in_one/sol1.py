
class stack:
  def __init__(self, start, capacity):
    self._start = start
    self._capacity = capacity
    self._size = 0
    
  def Isempty(self):
    return self.size == 0
    
  def Isfull(self):
    return self.size == self.capacity
    
  @property
  def capacity(self):
    return self._capacity
    
  @property
  def size(self):
    return self._size
    
  @property
  def start(self):
    return self._start
    
    
class ListStack:
  def __init__(self, stackNum, allCapacity):
    self._stackNum = stackNum
    self._allCapacity = allCapacity
    self._data = [0] * allCapacity
    self._stacks = []
    sk_cap = allCapacity / stackNum
    for  i in xrange(stackNum):
      sk = stack(i * sk_cap, sk_cap)
      self._stacks.append(sk)
    
  def __str__(self):
    res = ""
    for it in self._data:
      res += str(it)
      res += " "
    return res
    
  def Isempty(self, stackNo):
    return self._stacks[stackNo-1].Isempty()
    
  def Isfull(self, stackNo):
    return self._stacks[stackNo-1].Isfull()
    
  def push(self, stackNo, data):
    if self._stacks[stackNo-1].Isfull():
      raise ValueError("Stack is full!")
    
    self._data[self._stacks[stackNo-1].start + self._stacks[stackNo-1].size] = data
    self._stacks[stackNo-1].size += 1
    return True
    
  def pop(self, stackNo):
    if self._stacks[stackNo-1].Isempty():
      raise ValueError("Stack is empty!")
    
    self._stacks[stackNo-1].size -= 1
    return self._data[self._stacks[stackNo-1].start + self._stacks[stackNo-1].size]
    
  def peek(self, stackNo):
    if self._stacks[stackNo-1].Isempty():
      raise ValueError("Stack is empty!")
      
    return self._data[self._stacks[stackNo-1].start + self._stacks[stackNo-1].size - 1]
    

if __name__ == "__main__":
  ls = ListStack(3, 9)
  
  
  for i in xrange(3):
    ls.push(1, i)
    ls.push(2, i*2)
    ls.push(3, i*3)
    
  print ls
  
  print "isfull:"
  
  print ls.Isfull(1)
  print ls.Isfull(2)
  print ls.Isfull(3)
  
  print ls.Isempty(1)
  print ls.Isempty(2)
  print ls.Isempty(3)  
  
  print "peek:"
  
  print ls.peek(1)
  print ls.peek(2)
  print ls.peek(3)
  
  print "pop"
  
  for i in xrange(3):
    print ls.pop(1)
    print ls.pop(2)
    print ls.pop(3)
    
  print "isempty:"
  
  print ls.Isfull(1)
  print ls.Isfull(2)
  print ls.Isfull(3)
  
  print ls.Isempty(1)
  print ls.Isempty(2)
  print ls.Isempty(3)