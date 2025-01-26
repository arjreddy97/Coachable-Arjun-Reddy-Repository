class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        found = False
        for num in counts:
            if counts[num] >= 2:
                found = True
                break
        return found
        
