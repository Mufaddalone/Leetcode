class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1 for i in range(len(grid[0]))]for j in range(len(grid))]
        def helper(i,j,dp):
            if i==0 and j==0:
                return grid[i][j]
            if i<0 or j<0:
                return float("inf")
            if dp[i][j]!= -1:
                return dp[i][j]
            up = grid[i][j] + helper(i-1,j,dp)
            left = grid[i][j] + helper(i,j-1,dp)
            dp[i][j] = min(up,left)
            return dp[i][j]
        return helper(len(grid)-1,len(grid[0])-1,dp)