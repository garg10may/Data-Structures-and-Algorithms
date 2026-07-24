class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

def in_order(root):
    if not root:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)

# pre, in, post, reverse (pre, in, post)

def level_order(root):
    nodes = [root]
    final = []
    while nodes:
        el = nodes.pop(0)
        final.append(el.val)
        if el.left:
            nodes.append(el.left)
        if el.right:
            nodes.append(el.right)
    return final

print(in_order(root))
print(level_order(root))

# BST (Binary Search Tree)
# class Tree:
    
#     def __init__(self, root=None):
#         self.root = root
    
#     def add(self, val):
#         if not self.root:
#             self.root = TreeNode(val)
#         else:
#             self._add(self.root, val)
            
#     def _add(self, root, val):
#         if val < root.val:
#             if root.left:
#                 self._add(root.left, val)
#             else:
#                 root.left = TreeNode(val)
#         if val > root.val:
#             if root.right:
#                 self._add(root.right, val)
#             else:
#                 root.right = TreeNode(val)

# t = Tree()
# t.add(14)
# t.add(3)
# t.add(20)
# t.add(1)
# t.add(34)
# t.add(15)

# print(level_order(t.root))
            
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))            

print(max_depth(root))

def leaves(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    return leaves(root.left) + leaves(root.right)

print(leaves(root))

def levels(root):
    temp = [root]
    levels = []
    
    while temp:
        levels.append([i.val for i in temp])
        temp = next_nodes(temp)

    return levels
            
def next_nodes(nodes):
    result = []
    for node in nodes:
        if node.left:
            result.append(node.left)
        if node.right:
            result.append(node.right)
    return result

print(levels(root))


