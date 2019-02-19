import Queue

class node:
  def __init__(self, key):
    self._key = key
    self._child = []
    self._visit = False
    
  @property
  def key(self):
    return self._key
    
  @property
  def childs(self):
    return self._child
    
  @property
  def visit(self):
    return self._visit
    
  @visit.setter
  def visit(self, visit):
    self._visit = visit
    
  def addchild(self, childs):
    for ch in childs:
      self._child.append(ch)
      
      
def routeBetweenNodesDFS(nd1, nd2):
  if nd1.visit:
    return False
  
  if nd1 == nd2:
    return True
    
  nd1.visit = True
  for ch in nd1.childs:
    if routeBetweenNodesDFS(ch, nd2):
      return True
    
  return False
  
  
def routeBetweenNodesBFS(nd1, nd2):
  q = Queue.Queue()
  q.put(nd1)
  
  while not q.empty():
   nd = q.get()
   if nd == nd2:
     return True
   nd.visit = True
   for ch in nd.childs:
     if not ch.visit:
       q.put(ch)
  return False


if __name__ == "__main__":
  graph = {}
  for i in xrange(7):
    graph[i] = node(i)
  
  info = {0: [1], 1: [2], 2: [0, 3], 3: [2], 4: [6], 5: [4], 6: [5]}
   
  for k in info.keys():
    ch = [ graph[kk] for kk in info[k] ]
    print info[k]
    print ch
    graph[k].addchild(ch)
  
  #print routeBetweenNodesDFS(graph[0], graph[3])
  print routeBetweenNodesBFS(graph[0], graph[3])