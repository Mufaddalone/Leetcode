class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # dp = [0]*n

        # for i in range(m):
        #     for j in range(n):
        #         if i ==0 and j==0:
        #             dp[j] = grid[i][j]
        #         elif i == 0:
        #             dp[j] = dp[j-1] + grid[i][j]
        #         elif j == 0:
        #             dp[j] = dp[j] + grid[i][j]
        #         else:
        #             dp[j] = min(dp[j],dp[j-1])+ grid[i][j]
        # return dp[-1]

        # m=len(grid)
        # n=len(grid[0])
        # prev = [0]*n
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[i][j] = grid[i][j]
        #         elif i == 0:
        #             dp[i][j] = dp[i][j-1] + grid[i][j]
        #         elif j == 0:
        #             dp[i][j] = dp[i-1][j] + grid[i][j]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # return dp[m-1][n-1]

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

        m = len(grid)
        n = len(grid[0])
        prev = [0] * n
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[j] = grid[i][j]
                else:
                    up = grid[i][j]
                    if i>0:
                        up+= prev[j]
                    else:
                        up += int(1e9)
                    left = grid[i][j]
                    if j>0:
                        left+= curr[j-1]
                    else:
                        left += int(1e9)
                    curr[j] = min(left,up)
            prev = curr
        return prev[n-1]

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1 for i in range(len(grid[0]))]for j in range(len(grid))]
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 and j==0:
        #             dp[i][j] = grid[i][j]
        #         else:
        #             up = grid[i][j]
        #             if i>0:
        #                 up+= dp[i-1][j]
        #             else:
        #                 up += int(1e9)
        #             left = grid[i][j]
        #             if j>0:
        #                 left+= dp[i][j-1]
        #             else:
        #                 left += int(1e9)
        #             dp[i][j] = min(left,up)
        # return dp[m-1][n-1]
                