class Solution:
    def maxArea(self, height: List[int]) -> int:
        heights = height[::]
        leftMax = height[0]
        rightMax = heights[-1]
        totalWater = float("-inf")
        
        leftIdx = 0
        rightIdx = len(heights) - 1
        
        while leftIdx < rightIdx:
            
            if heights[leftIdx] < heights[rightIdx]:
                currentWater = ((rightIdx - leftIdx)) * heights[leftIdx]
                if currentWater > totalWater:
                    totalWater = currentWater
                leftIdx += 1
                leftMax = max(heights[leftIdx],leftMax)
            else:
                
                currentWater = ((rightIdx - leftIdx)) * heights[rightIdx]
                if currentWater > totalWater:
                    totalWater = currentWater
                rightIdx -=1
                rightMax = max(heights[rightIdx],rightMax)
                
        return totalWater
