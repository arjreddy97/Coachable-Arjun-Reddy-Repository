class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #
        ans = [0] * len(nums)
        low = 0
        high = len(nums) - 1
        num = 0
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[low]) > abs(nums[high]):
                num = nums[low]
                low += 1
            else:
                num = nums[high]
                high -= 1
            ans[i] = num * num
        return ans      
