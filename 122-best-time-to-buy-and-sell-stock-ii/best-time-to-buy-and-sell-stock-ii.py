class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for i in range(2)]for j in range(n+1)]
        dp[n][0] = dp[n][1] = 0

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if dp[ind][buy] != -1:
                    return dp[ind][buy]
                if (buy):
                    profit = max(-prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    profit = max(prices[ind]+dp[ind+1][1],dp[ind+1][0])
                dp[ind][buy] = profit
        return dp[ind][buy]

        # n = len(prices)
        # dp = [[-1 for i in range(2)]for j in range(n)]
        # def prof(ind,buy):
        #     if ind ==n:
        #         return 0
        #     profit = 0
        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]
        #     if (buy):
        #         profit = max(-prices[ind]+prof(ind+1,0),prof(ind+1,1))
        #     else:
        #         profit = max(prices[ind]+prof(ind+1,1),prof(ind+1,0))
        #     dp[ind][buy] = profit
        #     return dp[ind][buy]
        # return prof(0,1)
        