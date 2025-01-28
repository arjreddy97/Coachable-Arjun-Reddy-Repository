# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        self.find_path_sum(root,0,[],output,targetSum)
        return output


    def find_path_sum(self,node,running_sum,curr_path,output,target_sum):
        if not node:
            return 
        
        running_sum += node.val
        new_path = curr_path + [node.val]
        if node.left == None and node.right == None:
            if running_sum == target_sum:
                output.append(new_path)
            return
        self.find_path_sum(node.left,running_sum,new_path,output,target_sum)
        self.find_path_sum(node.right,running_sum,new_path,output,target_sum)


