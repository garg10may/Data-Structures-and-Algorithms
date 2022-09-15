#BST -> Binary Search Tree

class TreeNode(object):

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

class Tree(object):

    def __init__(self):
        self.root = None
        self.left  = None
        self.right = None

    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
        else:
            self._add(node, self.root)

    def _add(self, node, root):

        if node.data > root.data:
            if root.right == None:
                root.right = node
            else:
                self._add(node, root.right)

        if node.data < root.data:
            if root.left ==None:
                root.left = node
            else:
                self._add(node, root.left)

    def inOrder(self):
        node = self.root
        
        if node != None:
            self._inOrder(node)
            
    def _inOrder(self, node):

        if node !=None:
            self._inOrder(node.left)
            print (node.data, end=' ')
            self._inOrder(node.right)
    
    def postOrder(self):
        node = self.root
        
        if node != None:
            self._postOrder(node)
            
    def _postOrder(self, node):
        
        if node !=None:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print (node.data, end=" ")

    def preOrder(self):
        node = self.root
        
        if node != None:
            self._preOrder(node)
            
    def _preOrder(self, node):
        
        if node !=None:
            print (node.data, end=" ")
            self._preOrder(node.left)
            self._preOrder(node.right)

    def levelOrder(self):
        nodes = [self.root]
        while nodes:
            node = nodes.pop(0)
            print(node.data, end=" ")
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    def _height(self, node):

        if node == None:
            return 0
        
        lheight = self._height(node.left)
        rheight = self._height(node.right)
        
        if lheight > rheight:
            return lheight + 1 
        else:
            return rheight + 1

    def __str__(self):
        return str(self.root.data)

    def findLeafNodes(self):
        leafNodes = []
        if self.root != None:
            self._findLeafNodes(self.root, leafNodes)
        print(leafNodes)

    def _findLeafNodes(self, node, leafNodes):
        if node != None:
            self._findLeafNodes(node.left, leafNodes)
            self._findLeafNodes(node.right, leafNodes)
            if node.left == None and node.right == None:
                leafNodes.append(node.data)
        return leafNodes

t = Tree()
t.add(10)
t.add(5)
t.add(20)
t.add(4)
t.add(6)
t.add(15)
t.add(25)

print('-----In Order-----')
t.inOrder()
print()
print ('-----Post Order-----')
t.postOrder()
print() 
print('-----Pre Order-----')
t.preOrder()
print()
print ('----Level Order Traversal----')
t.levelOrder()
print()
print('-----Leaf Nodes-----')
t.findLeafNodes()

#notice how the inOrder, postOrder, preOrder are all DFS and same code 
#just the print statement changes




