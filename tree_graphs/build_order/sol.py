class node:
  def __init__(self, key):
    self._key = key
    self._parentcount = 0
    self._childlist = []
    
  @property
  def key(self):
    return self._key
    
  @property
  def parentcount(self):
    return self._parentcount
    
  @parentcount.setter
  def parentcount(self, inc):
    self.parent += inc
    
  @property
  def childlist(self):
    return self._childlist
    
  def addchildlist(self, child):
    self.childlist.append(child)
    
class graph:
  def __init__(self):
    self._nodes = {}
    
  @property
  def nodes(self):
    return self._nodes
    
  def insertNode(self, key):
    if key in self.nodes:
      return
    else:
      nd = node(key)
      self.nodes[key] = nd
    
  def insertEdge(self, pndKey, chndKey):
    if pndKey in self.nodes:
      pnd = self.nodes[pndKey]
    else:
      pnd = node(pndKey)
      self.nodes[pndKey] = pnd
      
    if chndKey in self.nodes:
      chnd = self.nodes[chndKey]
    else:
      chnd = node(chndKey)
      self.nodes[chndKey] = chnd
    
    pnd.addchildlist(chndKey)
    chnd.parentcount += 1
    
  def getNextNodes(self):
    for k in self.nodes.keys():
      if self.nodes[k].parentcount == 0:
        for chk in self.nodes[k].childlist:
          self.nodes[chk].parentcount -= 1
        res = self.nodes.pop(k, None)
        return res
    return None
     
  def getOrderList(self):
    resList = []
    while len(self.nodes) > 0:
      res = self.getNextNodes()
      if res is None:
        return []
      resList.append(res.key)
    return resList


if __name__ == "__main__":
  inputnd = ['a', 'b', 'c', 'd', 'e', 'f']
  inputedge = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
  
  gp = graph()
  
  for it in inputnd:
    gp.insertNode(it)
  
  for it in inputedge:
    gp.insertEdge(it[0], it[1])
    
  res = gp.getOrderList()
  
  print res

