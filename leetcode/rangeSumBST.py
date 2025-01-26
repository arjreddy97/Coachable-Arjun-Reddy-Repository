class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:  
        result = [0]
        compute(root,low,high,result)
        return result[0]
        
        
        
def compute(node,low,high,result):
    if node == None:
        return 
    if node.val >= low and node.val <= high:
        result[0] += node.val
    compute(node.left,low,high,result)
    compute(node.right,low,high,result)
        
