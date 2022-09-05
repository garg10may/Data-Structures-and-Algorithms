#5th Sep, 2022, Fractal, practise

#Binary Search Tree 

class TreeNode(object):

  def __init__(self, data) -> None:
    self.left = None
    self.right = None
    self.data = data 

class Tree(object):

  def __init__(self) -> None:
    self.root = None

  def add(self, data):

    if self.root == None:
      self.root = TreeNode(data)
    else:
      self._add(self.root, data)

  def _add(self, node, data):
    if data > node.data:
      if node.right:
        self._add(node.right, data)
      else:
        node.right = TreeNode(data)
    if data < node.data:
      if node.left:
        self._add(node.left, data)
      else:
        node.left = TreeNode(data)

  def levelOrder(self):
    nodes = [self.root]
    while nodes:
      node = nodes.pop(0)
      print(node.data, end=" ")
      if node.left:
        nodes.append(node.left)
      if node.right:
        nodes.append(node.right)

  def dfs(self):
    self._dfs(self.root)

  def _dfs(self, node):
    if node !=None:
      self._dfs(node.left)
      self._dfs(node.right)
      print(node.data, end=" ")


t = Tree()
t.add(10)
t.add(5)
t.add(20)
t.add(4)
t.add(6)
t.add(15)
t.add(25)

# print('-----In Order-----')
# t.inOrder()
# print()
# print ('-----Post Order-----')
# t.postOrder()
# print() 
# print('-----Pre Order-----')
# t.preOrder()
# print()
print ('----Level Order Traversal----')
t.levelOrder()
print()
print(t.dfs())




