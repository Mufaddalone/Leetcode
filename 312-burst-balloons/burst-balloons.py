class Solution:
    def maxCoins(self, a: List[int]) -> int:
        n = len(a)
        
        # Extend the list 'a' with 1s at both ends
        a.insert(0, 1)
        a.append(1)

        # Create a 2D DP table initialized with 0s
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # Loop from the end of 'a' to the beginning
        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i > j:
                    continue
                maxi = float('-inf')
                
                # Iterate through the balloons from 'i' to 'j'
                for ind in range(i, j + 1):
                    cost = a[i - 1] * a[ind] * a[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                    maxi = max(maxi, cost)
                
                dp[i][j] = maxi
        
        return dp[1][n]
        # def burst(i,j):
        #     if i>j:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     maxi = float('-inf')
        #     for ind in range(i,j+1):
        #         bust = nums[i-1]*nums[ind]*nums[j+1] +burst(i,ind-1) + burst(ind+1,j)
        #         maxi = max(maxi,bust)
        #     dp[i][j] =maxi
        #     return dp[i][j]
        # return burst(1,n-2)