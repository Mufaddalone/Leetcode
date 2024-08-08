class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1 for i in range(len(obstacleGrid[0]))]for j in range(len(obstacleGrid))]
        def helper(i,j,dp):
            if (i>=0 and j>=0) and (obstacleGrid[i][j] == 1):
                 return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up = helper(i-1,j,dp)
            left = helper(i,j-1,dp)
            dp[i][j] = up+left
            return dp[i][j]
        return helper(len(obstacleGrid)-1,len(obstacleGrid[0])-1,dp)