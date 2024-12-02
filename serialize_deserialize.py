# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        if (root == None): 
            return '#'
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return ','.join([str(root.val), left, right])
        

    def deserialize(self, data):
        data = data.split(',')
        root = self.buildTree(data)
        return root
        
    def buildTree(self, data):
        val = data.pop(0)
        if (val == '#'): 
            return None
        root = TreeNode(val)
        root.left = self.buildTree(data)
        root.right = self.buildTree(data)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
