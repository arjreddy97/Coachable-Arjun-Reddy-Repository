class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDiameter(root)[1]
        
        
    def getMaxDiameter(self,root):
        if (root == None):
            return (0,0)
        
        lTreeInfo = self.getMaxDiamter(root.left)
        rTreeInfo = self.getMaxDiamter(root.right)
        
        currHeight = 1 + max(lTreeInfo[0] ,rTreeInfo[0])
        
        diameterAsRoot =  lTreeInfo[0] + rTreeInfo[0]
        
        maxDiameter = max(lTreeInfo[0],
                          rTreeInfo[0], 
diameterAsRoot,lTreeInfo[1],rTreeInfo[1])
        
        return (currHeight,maxDiameter)
        
