#heap is a complete binary tree
#max heap: parent is greater than children
#min heap: parent is less than children

#It feels like it can't be implemented using tree, class, node, but it's easy to implement using array. 

class MaxHeap:

  def __init__(self):
    self.heap = []

  def lchild_index(self, i):
    return 2*i + 1
  
  def rchild_index(self, i):
    return 2*i + 2
  
  def parent_index(self, i):
    return (i-1)//2

  def insert(self, value):
    self.heap.append(value)
    self.heapify()
  
  def heapify(self):
    i = len(self.heap) - 1
    while i > 0:
      p = self.parent_index(i)
      if self.heap[i] > self.heap[p]:
        self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
        i = p
      else:
        break
      
    
