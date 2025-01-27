# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution(object):
    def verticalTraversalHelper(self, root, row, col):
        if not root:
            return 
        
        
        if row in self.d[col]:
            self.d[col][row].append(root.val)
        else:
            self.d[col][row] = []
            self.d[col][row].append(root.val)
            
        
        self.verticalTraversalHelper(root.left, row+1, col-1)
        self.verticalTraversalHelper(root.right, row+1, col+1)
        
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.d = collections.defaultdict(dict)
        self.verticalTraversalHelper(root, 0, 0)
        
        res = []
        
        
        for col in sorted(self.d.keys()):
            col_res = [val for row in sorted(self.d[col].keys()) for val in sorted(self.d[col][row])]
            res.append(col_res)
                
        
        return res
