class Solution:
   def numJewelsInStones(self, jewels: str, stones: str) -> int:
       jewels_set = set(jewels)
       count = 0
       for i in range(len(stones)):
           stone = stones[i]
           if stone in jewels_set:
               count += 1
       return count
