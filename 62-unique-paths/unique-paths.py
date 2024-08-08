class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = dp[i-1][j] if i > 0 else 0
                    left = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = up + left
        return dp[m-1][n-1]
        # dp = dp = [[-1 for i in range(n)] for j in range(m)]
        # def helper(i,j,dp):
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     if i==0 and j==0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
        #     up = helper(i-1,j,dp)
        #     left = helper(i,j-1,dp)
        #     dp[i][j] = up+left
        #     return dp[i][j]
        # return helper(m-1,n-1,dp)