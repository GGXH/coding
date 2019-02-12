
class stack:
  def __init__(self, start):
    self._start = start
    self._size = 0
    
  def Isempty(self):
    return self.size == 0
    
  @property
  def endIndx(self):
     return self.start + self.size
    
  @property
  def size(self):
    return self._size
    
  @size.setter
  def size(self, size):
    self._size = size
    
  @property
  def start(self):
    return self._start
    
  @start.setter
  def start(self, start):
    self._start = start
    
    
class ListStack:
  def __init__(self, stackNum, allCapacity):
    self._stackNum = stackNum
    self._allCapacity = allCapacity
    self._data = [0] * allCapacity
    self._stacks = []
    sk_cap = allCapacity / stackNum
    for  i in xrange(stackNum):
      sk = stack(i * sk_cap)
      self._stacks.append(sk)
    
  def __str__(self):
    res = ""
    for it in self._data:
      res += str(it)
      res += " "
    return res
  
  @property
  def allCapacity(self):
     return self._allCapacity
  
  @property
  def stackNum(self):
     return self._stackNum
    
  @property
  def stacks(self):
     return self._stacks
    
  def isStackEmpty(self, stackNo):
    return self.stacks[stackNo].Isempty()
    
  def isStackFull(self, stackNo):
    return self.stacks[stackNo].Isfull()
    
  def isFull(self):
    data_size = 0
    for i in xrange(self._stackNum):
      data_size += self.stacks[i].size
    if data_size == self.allCapacity:
      return True
    return False
    
  def _getIndx(self, indx):
     while indx >= self.allCapacity:
        indx -= self.allCapacity
     while indx < 0:
        indx += self.allCapacity
     return indx
     
  def _getNextIndx(self, indx):
     return self._getIndx(indx+1)
     
  def _getPreIndx(self, indx):
     return self._getIndx(indx-1)
    
  def _move(self, stackNo):
     if sefl._needMoveNext(stackNo):
        nextStackIndx = self._nextStackNo(stackNo)
        self._move(nextStackIndx)
     endIndx = self.stacks[stackNo].endIndx
     while endIndx != self.stacks[stackNo].start:
        pindx = self._getPreIndx(endIndx)
        self._data[endIndx] = self._data[pindx]
        endIndx = pindx
        
  def _needMoveNext(self, stackNo):
     endIndx = self.stacks[stackNo].endIndx
     nextStackIndx = self._nextStackNo(stackNo)
     if endIndx == self.stacks[nextStackIndx].start:
        return True
     return False
     
  def _nextStackNo(self, stackNo):
     if stackNo == self.stackNum - 1:
        return 0
     else:
        return stackNo + 1
    
  def push(self, stackNo, data):
    if self.isFull():
      raise ValueError("Stack is full!")

    if self._needMoveNext(stackNo):
       nextStackIndx = self._nextStackNo(stackNo)
       self._move(nextStackIndx)

    indx = self.stacks[stackNo].start + self.stacks[stackNo].size
    indx = self._getIndx(indx)
    self._data[indx] = data
    self.stacks[stackNo].size += 1
    
  def pop(self, stackNo):
    if self.stacks[stackNo].Isempty():
      raise ValueError("Stack is empty!")
    
    self.stacks[stackNo].size -= 1
    
  def peek(self, stackNo):
    if self._stacks[stackNo].Isempty():
      raise ValueError("Stack is empty!")
      
    indx = self.stacks[stackNo].start + self.stacks[stackNo].size
    indx = self._getIndx(indx)
    return self._data[indx]
    

if __name__ == "__main__":
  ls = ListStack(3, 12)
  
  
  for i in xrange(12):
    ls.push(2, i*3)
    
  print ls
  
  print "isfull:"
  
  print ls.isFull()
  
  print "peek:"
  
  print ls.peek(2)
  
  print "pop"
  
  for i in xrange(3):
    ls.pop(2)
    
  print ls.peek(2)
    
  print "isempty:"
  
  print ls.isFull()