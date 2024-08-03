class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(n, memo):
            if n ==0 or n==1:
                return 1
            if n not in memo:
                memo[n] = helper(n-1,memo) + helper(n-2,memo)
            return memo[n]
        return helper(n,memo)
        # if n == 0 or n == 1:
        #     return 1

        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1
        
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        