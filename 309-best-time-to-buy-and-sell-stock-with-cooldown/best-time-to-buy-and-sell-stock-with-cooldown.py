class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for j in range(2)]for i in range(n+2)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if (buy):
                    profit = max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    profit = max(prices[ind]+dp[ind+2][1],dp[ind+1][0])
                dp[ind][buy] = profit
        return dp[0][1]