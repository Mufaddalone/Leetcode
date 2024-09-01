class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0 for j in range(2)]for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            dp[ind][1] = max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
            dp[ind][0] = max(prices[ind]+dp[ind+1][1]-fee,dp[ind+1][0])
        return dp[0][1]