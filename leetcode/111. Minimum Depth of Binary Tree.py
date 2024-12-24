# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        minSoFar = [float("inf")]
        self.getMinDepth(root,0,minSoFar)
        return minSoFar[0]
        
        
    def getMinDepth(self,node,runningPath,minSoFar):
        if node is None:
            return
        newRunningPath = 1 + runningPath
        if node.left is None and node.right is None:
            if newRunningPath < minSoFar[0]:
                print(newRunningPath)
                minSoFar[0] = newRunningPath
            return
        self.getMinDepth(node.left,newRunningPath,minSoFar)
        self.getMinDepth(node.right,newRunningPath,minSoFar)
        
        