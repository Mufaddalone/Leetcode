class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1] * (n+1) for _ in range(n+1)]
        def helper(i,j):
            if i == len(triangle)-1:
                return triangle[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down = triangle[i][j] + helper(i+1,j)
            side = triangle[i][j] + helper(i+1,j+1)
            dp[i][j] = min(down,side)
            return dp[i][j]
        return helper(0,0)