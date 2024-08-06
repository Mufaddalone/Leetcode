class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            memo = [0] * len(nums)

            memo[0] = nums[0]

            for i in range(1, len(nums)):
                memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])

            return memo[-1]

        if len(nums) == 1:
            return nums[0]
        
        return max(dp(nums[1:]), dp(nums[:-1]))
        # def robber(nums):
        #     rob1 , rob2 = 0, 0

        #     for i in nums:
        #         tmp = max(i+rob1,rob2)
        #         rob1 = rob2
        #         rob2 = tmp
        #     return rob2
        # return max(nums[0],robber(nums[1:]),robber(nums[:-1]))