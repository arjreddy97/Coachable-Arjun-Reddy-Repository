class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isNonIncreasing = True
        isNonDecreasing = True
        
        for i in range(1,len(nums)):
            if (nums[i] < nums[i-1]):
                isNonDecreasing = False
                
                
        for i in range(1,len(nums)):
            
            if (nums[i] > nums[i-1]):
                isNonIncreasing = False
               
                
        return isNonDecreasing or isNonIncreasing
        
        
        
