class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,prev2 = 0,0
        for n in nums:
            temp = max(prev+n, prev2)
            prev = prev2
            prev2 = temp
        return prev2
        # memo = {}
        # def helper(n):
        #     if n in memo:
        #         return memo[n]
        #     if n ==0:
        #         return nums[n]
        #     if n<0:
        #         return 0
        #     pick = nums[n] + helper(n-2)
        #     notpick = 0 + helper(n-1)
        #     memo[n] = max(pick,notpick)
        #     return memo[n]
        # return helper(len(nums)-1)
        # dp = len(nums)*[0]
        # dp[0] = nums[0]
        # if len(nums)>1:
        #     dp[1] = nums[1]
        # else:
        #     return dp[0]

        # for i in range(2,len(nums)):
        #     dp[i] = nums[i] + dp[i-2]
        # return max(dp[-1],dp[-2])
        # rob1, rob2 = 0, 0

        # for n in nums:
        #     temp = max(n + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2
