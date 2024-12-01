​​class Solution(object):
   def maxSubArray(self, nums):
       """
       :type nums: List[int]
       :rtype: int
       """
       maxSoFar = nums[0]
       maxEndingHere = nums[0]
       for i in range(1,len(nums)):
           num = nums[i]
           maxEndingHere = max(num,maxEndingHere+num)
           maxSoFar = max(maxSoFar,maxEndingHere)
       return maxSoFar
