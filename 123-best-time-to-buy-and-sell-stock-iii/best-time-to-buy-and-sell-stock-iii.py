class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        
        def prof(ind, buy, cap):
            if ind == n or cap == 0:
                return 0
            
            if dp[ind][buy][cap] != -1:
                return dp[ind][buy][cap]
            
            if buy:
                profit = max(-prices[ind] + prof(ind+1, 0, cap),
                             prof(ind+1, 1, cap))
            else:
                profit = max(prices[ind] + prof(ind+1, 1, cap-1),
                             prof(ind+1, 0, cap))
            
            dp[ind][buy][cap] = profit
            return profit
        
        return prof(0, 1, 2)