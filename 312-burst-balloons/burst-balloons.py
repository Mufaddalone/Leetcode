class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] +nums+[1]
        n = len(nums)
        dp = [[-1 for j in range(n)]for i in range(n)]
        def burst(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi = float('-inf')
            for ind in range(i,j+1):
                bust = nums[i-1]*nums[ind]*nums[j+1] +burst(i,ind-1) + burst(ind+1,j)
                maxi = max(maxi,bust)
            dp[i][j] =maxi
            return dp[i][j]
        return burst(1,n-2)