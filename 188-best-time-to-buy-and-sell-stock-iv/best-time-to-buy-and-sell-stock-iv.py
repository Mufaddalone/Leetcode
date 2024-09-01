class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[0 for j in range(5)] for i in range(n + 1)]
        curr = [0]*(k*2+1)
        prev = [0]*(k*2+1)

        for ind in range(n - 1, -1, -1):
            for trans in range(k*2-1, -1, -1):
                if trans % 2 == 0:  # Buy
                    profit = max(-prices[ind] + prev[trans + 1], prev[trans])
                else:  # Sell
                    profit = max(prices[ind] + prev[trans + 1], prev[trans])
                curr[trans] = profit
            prev = curr

        return curr[0]
        # n = len(prices)
        # dp = [[-1 for j in range(k*2+1)]for i in range(n)]
        # def prof(ind,tras):
        #     if ind ==n:
        #         return 0
        #     if tras == 0:
        #         return 0
        #     if dp[ind][tras] != -1:
        #         return dp[ind][tras]

        #     if (tras%2 ==0):
        #         profit = max(-prices[ind]+prof(ind+1,tras-1),prof(ind+1,tras))
        #     else:
        #         profit = max(prices[ind]+prof(ind+1,tras-1),prof(ind+1,tras))

        #     dp[ind][tras] = profit
        #     return profit
        # return prof(0,k*2)