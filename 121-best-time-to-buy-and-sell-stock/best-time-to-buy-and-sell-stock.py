class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l= 0
        r = 1
        maxi = 0
        while r<len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                maxi = max(maxi,profit)
            else:
                l=r
            r+=1
        return maxi
