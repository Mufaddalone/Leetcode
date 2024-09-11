class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        c = len(cuts)
        dp = [[-1 for i in range(c)]for j in range(c)]
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini = float("inf")
            for ind in range(i,j+1):
                cost = cuts[j+1] - cuts[i-1] + f(i,ind-1) + f(ind+1,j)
                mini = min(mini,cost)
            dp[i][j] = mini
            return dp[i][j]
        return f(1,c-2)
        # dp = [[0] * c for _ in range(c)]
        
        # for i in range(c-2, 0, -1):
        #     for j in range(i+1, c):
        #         mini = float('inf')
        #         for ind in range(i, j):
        #             cut = cuts[j] - cuts[i-1] + dp[i][ind] + dp[ind+1][j]
        #             mini = min(mini, cut)
        #         dp[i][j] = mini
        
        # return dp[1][c-1]

        # # Extend the cuts list with 0 and n, and sort it
        # cuts = [0] + sorted(cuts) + [n]
        # c = len(cuts)
        # dp = [[-1] * c for _ in range(c)]

        # def cutting(i, j):
        #     if j - i <= 1:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     mini = float('inf')
        #     for ind in range(i+1, j):
        #         cut = cuts[j] - cuts[i] + cutting(i, ind) + cutting(ind, j)
        #         mini = min(mini, cut)
            
        #     dp[i][j] = mini
        #     return dp[i][j]

        # return cutting(0, c - 1)

        # # Recursive function to find the minimum cost
        # def f(i, j):
        #     # Base case
        #     if j - i <= 1:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     dp[i][j] = min(cuts[j] - cuts[i] + f(i, k) + f(k, j) for k in range(i+1, j))
        #     return dp[i][j]

        # return f(0, c-1)