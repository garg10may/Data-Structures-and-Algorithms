#22nd July, 2026, Google prep

from typing import Optional

class Node():
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left =left
        self.right = right
        

#this is a BST only needed if looking for BST otherwise just using Node normally can 
#construct a sample tree 
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
        
    
    def pre_order(self):
        return self._pre_order(self.root) #works on root, so first we need to extract the root and then recurse

        
    def _pre_order(self, root): 
        if root:
            return [root.data] + self._pre_order(root.left) + self._pre_order(root.right)
        else:
            return []

def pre_order(root):
    if not root:
        return []
    return [root.data] + pre_order(root.left) + pre_order(root.right)

def in_order(root):
    if root:
        return in_order(root.left) + [root.data] + in_order(root.right)
    else: 
        return []
    
def post_order(root):
    if not root:
        return []
    return post_order(root.left) + post_order(root.right) + [root.data]

def reverse_pre_order(root):
    if not root:
        return []
    return [root.data] + reverse_pre_order(root.right) + reverse_pre_order(root.left)

def reverse_in_order(root):
    if not root:
        return []
    return reverse_in_order(root.right) + [root.data] + reverse_in_order(root.left)

def reverse_post_order(root):
    if not root:
        return []
    return reverse_post_order(root.right) + reverse_post_order(root.left) + [root.data]
    
def level_order(root):
    nodes=[root]
    final=[]
    while nodes:
        el = nodes.pop(0)
        final.append(el.data)
        if el.left:
            nodes.append(el.left)
        if el.right:
            nodes.append(el.right)
    return final

def reverse_level_order(root):
    nodes=[root]
    final=[]
    while nodes:
        el = nodes.pop(0)
        final.append(el.data)
        if el.right:
            nodes.append(el.right)
        if el.left:
            nodes.append(el.left)
    return final

if __name__ == "__main__":
    
    t = Tree()
    t.add(3)
    t.add(1)
    t.add(51)
    t.add(52)
    t.add(50)
    
    print(t.pre_order())

    
    root = Node(1)
    root.left=Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(pre_order(root))
    print(in_order(root))
    print(post_order(root))
    print(reverse_pre_order(root))
    print(reverse_in_order(root))
    print(reverse_post_order(root))
    print(level_order(root))
    print(reverse_level_order(root))
    
    
