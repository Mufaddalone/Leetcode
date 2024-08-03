class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = len(nums)*[0]
        # dp[0] = nums[0]
        # if len(nums)>1:
        #     dp[1] = nums[1]
        # else:
        #     return dp[0]

        # for i in range(2,len(nums)):
        #     dp[i] = nums[i] + dp[i-2]
        # return max(dp[-1],dp[-2])
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
