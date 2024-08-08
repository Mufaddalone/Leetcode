class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[-1]

        # m=len(grid)
        # n=len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if i>0 and j>0:
        #             grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        #         elif i>0:
        #             grid[i][0]+=grid[i-1][0]
        #         elif j>0:
        #             grid[0][j]+=grid[0][j-1]
        # return grid[m-1][n-1]

        # dp = [[-1 for i in range(len(grid[0]))]for j in range(len(grid))]
        # def helper(i,j,dp):
        #     if i==0 and j==0:
        #         return grid[i][j]
        #     if i<0 or j<0:
        #         return float("inf")
        #     if dp[i][j]!= -1:
        #         return dp[i][j]
        #     up = grid[i][j] + helper(i-1,j,dp)
        #     left = grid[i][j] + helper(i,j-1,dp)
        #     dp[i][j] = min(up,left)
        #     return dp[i][j]
        # return helper(len(grid)-1,len(grid[0])-1,dp)