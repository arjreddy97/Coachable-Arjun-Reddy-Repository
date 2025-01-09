class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float("inf")
        for i in range(len(nums)-2):
            leftIdx = i + 1
            rightIdx = len(nums)-1
            while leftIdx < rightIdx:

                currentSum = nums[i] + nums[leftIdx] + nums[rightIdx]
                if currentSum == target:
                    return currentSum
                
                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum
                
                if currentSum   < target:
                    leftIdx += 1
                else:
                    rightIdx -= 1

        return closestSum
                


    
    


  

        
