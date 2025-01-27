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
                


    
    


    """
    1) sort array
    2) iterate through every start of potential triplet
         - use left and right pointers to find sums
         - increment left pointer if sum < less than target
         - derement right pointer if sum > target

    3) update closest sum based on current sum distance to target

    4) return closest sum



    """

        
