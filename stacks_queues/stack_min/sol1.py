class stackMin:
  def __init__(self):
    self._data = []
    self._minIndx = []
    
  def __str__(self):
     res = ""
     for it in self._data:
        res += str(it) + " "
     return res
    
  @property
  def size(self):
     return len(self._data)
     
  def isEmpty(self):
     return len(self._data) == 0
     
  def currentMin(self):
     if self.isEmpty():
        raise "Stack is empty"
     return self._data[self._minIndx[-1]]
    
  def push(self, data):
     if self.isEmpty():
        self._minIndx.append(0)
     else:
        cmin = self.currentMin()
        if cmin > data:
           self._minIndx.append(len(self._data))
           cmin = data
        else:
           self._minIndx.append(self._minIndx[-1])
     self._data.append(data)
           
  def pop(self):
      if self.isEmpty():
         raise "Stack is empty"
         
      self._minIndx.pop()
      return self._data.pop()
      
  def min(self):
      return self._data[self._minIndx[-1]]
      
      
if __name__ == "__main__":
   st = stackMin()
   
   data = [2, 3, 1, 10, 3, 4, 5]
   
   for it in data:
      st.push(it)
      
   print st
      
   for it in data:
      print st.min(), st.pop()
