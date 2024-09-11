class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] +nums+[1]
        n = len(nums)
        dp = [[0 for j in range(n)]for i in range(n)]
        for i in range(n-2,0,-1):
            for j in range(1,n-1):
                if i>j: continue
                maxi = float("-inf")
                for ind in range(i,j+1):
                    bust = nums[i-1]*nums[ind]*nums[j+1] +dp[i][ind-1] + dp[ind+1][j]
                    maxi = max(maxi,bust)
                dp[i][j] =maxi
        return dp[1][n-2]
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