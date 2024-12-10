class Solution:
   def maxProfit(self, prices: List[int]) -> int:


       minPurchase = prices[0]
       maxProfit = 0


       for i in range(1,len(prices)):
           currPrice = prices[i]
           minPurchase = min(minPurchase,currPrice)
           currProfit = currPrice - minPurchase
           maxProfit = max(maxProfit,currProfit)


       return maxProfit
