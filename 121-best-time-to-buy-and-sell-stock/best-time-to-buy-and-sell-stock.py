class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l= 0
        maxi = 0
        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l =r
            else:
                maxi = max(maxi, prices[r] - prices[l])
        return maxi