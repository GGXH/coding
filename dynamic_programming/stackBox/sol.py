import heapq

def stackBoxHelper(boxHeap, curWidth, curLength, maxHeight):
  if len(boxHeap) == 0:
    return maxHeight
    
  curBox = heapq.heappop(boxHeap)
  if curBox[0] <= curWidth or curBox[1] <= curLength:
    return stackBoxHelper(boxHeap, curWidth, curLength, maxHeight)
    
  h1 = stackBoxHelper(boxHeap, curWidth, curLength, maxHeight)
  h2 = stackBoxHelper(boxHeap, curBox[0], curBox[1], maxHeight + curBox[2])
  
  heapq.heappush(boxHeap, curBox)
  
  return max(h1, h2)


def stackBox(width, length, height):
  boxHeap = []
  heapq.heapify(boxHeap)
  for i in xrange(len(width)):
    heapq.heappush(boxHeap, (width[i], length[i], height[i]))
    
  return stackBoxHelper(boxHeap, 0, 0, 0)
  
if __name__ == "__main__":
  width = [0.1, 0.2, 0.3]
  length = [0.1, 0.1, 0.3]
  height = [0.1, 0.2, 0.3]
  
  print stackBox(width, length, height)
  