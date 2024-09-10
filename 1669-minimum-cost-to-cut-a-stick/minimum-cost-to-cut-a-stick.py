class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Extend the cuts list with 0 and n, and sort it
        cuts = [0] + sorted(cuts) + [n]
        c = len(cuts)
        dp = [[-1] * c for _ in range(c)]

        def cutting(i, j):
            if j - i <= 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            mini = float('inf')
            for ind in range(i+1, j):
                cut = cuts[j] - cuts[i] + cutting(i, ind) + cutting(ind, j)
                mini = min(mini, cut)
            
            dp[i][j] = mini
            return dp[i][j]

        return cutting(0, c - 1)

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