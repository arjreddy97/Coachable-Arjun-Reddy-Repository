class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return merge(root1,root2)
        
        
def merge(nodeOne,nodeTwo):
    
    if nodeOne is None:
        return nodeTwo
    if nodeTwo is None:
        return nodeOne
    
    tree = TreeNode(nodeOne.val)
    tree.val += nodeTwo.val
    
    tree.left = merge(nodeOne.left,nodeTwo.left)
    tree.right = merge(nodeOne.right,nodeTwo.right)
    
    
    return tree
