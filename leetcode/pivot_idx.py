class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftRunning = 0
        for i in range(len(nums)):
            num = nums[i]
            if i == len(nums)-1 and leftRunning == 0:
                return i
            rightRunning = totalSum - leftRunning - num
            if leftRunning == rightRunning:
                return i
            leftRunning += num
        return -1
                
            


      

       
