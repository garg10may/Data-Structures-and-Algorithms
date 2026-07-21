#22nd July, 2026, Google prep

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree():

    def __init__(self):
        self.root = None
    
    def add(self, data):
        node = Node(data)
        
        if self.root:
            self._add(self.root, node)
        else:
            self.root = node
        
    def _add(self, root, node):
        if node.data < root.data:
            if root.left:
                self._add(root.left, node)
            else:
                root.left = node
        
        if node.data > root.data:
            if root.right:
                self._add(root.right, node)
            else:
                root.right = node        
        
    
    def inOrder(self):
        self._inOrder(self.root)
        
    def _inOrder(self, root):
        if root:
            print(root.data, end=' ')
            self._inOrder(root.left)
            self._inOrder(root.right)
                
            
        
if __name__ == "__main__":
    
    t = Tree()
    t.add(3)
    t.add(1)
    t.add(51)
    t.add(52)
    t.add(50)
    
    t.inOrder()
    