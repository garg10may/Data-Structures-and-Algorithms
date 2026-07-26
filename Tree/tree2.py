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

print ('----Level Order Traversal----')
t.levelOrder()
print()
print(t.dfs())



class TreeNode2:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
root = TreeNode2(1)
root.left = TreeNode2(2)
root.right = TreeNode2(3)
root.left.left=TreeNode2(4)
root.left.right = TreeNode2(5)

def preOrder2(root):
  if not root:
    return []
  return [root.val] + preOrder2(root.left) + preOrder2(root.right)
    
def levelOrder(root):
 
  temp = [root]
  nodes = []
  while temp:
    el = temp.pop(0)
    nodes.append(el.val)
    
    if el.left:
      temp.append(el.left)
    if el.right:
      temp.append(el.right)
  
  return nodes

print(preOrder2(root))
print(levelOrder(root))
    
def levels(root):
  temp = [root]
  levels = []
  
  def next_nodes(nodes):
    result = []
    for node in nodes:
      if node.left:
        result.append(node.left)
      if node.right:
        result.append(node.right)
    return result
  
  while temp:
    levels.append([i.val for i in temp])
    temp = next_nodes(temp)
    
  return levels

print(levels(root))
    

def removeElement(nums, val: int) -> int:
    
    count = 0
    for i, value in enumerate(nums):
        if value == val:
            nums[i] = '_'
        else:
            count +=1
        
    print(nums)
    return count

print(removeElement([3,2,2,3], 3))
    