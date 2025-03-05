class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        mini = prices[0]
        maxi = 0
        for i in prices:
            profit = i - mini
            if profit > maxi:
                maxi = profit
            if i < mini:
                mini = i
        return maxi
