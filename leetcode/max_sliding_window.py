class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxDq = collections.deque([])
        output = []
        rightIdx = 0
        leftIdx = 0

        while rightIdx < len(nums):
            num = nums[rightIdx]
            while len(maxDq) and nums[maxDq[-1]] < num:
                maxDq.pop()

            maxDq.append(rightIdx)
            shouldMoveLeft = (rightIdx - leftIdx) + 1 == k
            if not shouldMoveLeft:
                rightIdx += 1
                continue
            output.append(nums[maxDq[0]])
            if maxDq[0] == leftIdx:
                maxDq.popleft()
            
            leftIdx += 1
            rightIdx += 1

        return output

      


      



        
