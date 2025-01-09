class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:  
        result = {"runningSum":0}
        compute(root,low,high,result)
        return result["runningSum"]
        w
        
        
def compute(node,low,high,result):
    if node == None:
        return 
    if node.val >= low and node.val <= high:
        print(node.val)
        result["runningSum"] += node.val
    compute(node.left,low,high,result)
    compute(node.right,low,high,result)
        
