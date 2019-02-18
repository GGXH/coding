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
    
def sortStack(st):
  temp_stack = Stack()
  
  while not st.isEmpty():
    data = st.pop()
    if temp_stack.isEmpty() or data > temp_stack.top():
      temp_stack.push(data)
    else:
      count = 0
      while not temp_stack.isEmpty() and temp_stack.top() > data:
        st.push(temp_stack.pop())
        count += 1
      temp_stack.push(data)
      for i in xrange(count):
        temp_stack.push(st.pop())
       
  while not temp_stack.isEmpty():
    st.push(temp_stack.pop())
  return st
    
if __name__ == "__main__":
   sos = Stack()
   
   data = [12, 3, 4, 11, 23, 45, 1, 5, 6]
  
  
   for it in data:
      sos.push(it)
      
   sos = sortStack(sos)
   
   print sos