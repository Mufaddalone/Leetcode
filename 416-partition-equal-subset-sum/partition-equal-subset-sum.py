class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
    
        # If total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # Initialize a DP array where dp[i] means if the sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Update the DP array from right to left
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
        # arr_sum = sum(nums)
        # if arr_sum % 2 != 0:
        #     return False
        # sub_sum = arr_sum//2
        # n = len(nums)
        # dp = [[False for j in range(sub_sum+1)]for i in range(n)]
        # for i in range(n):
        #     dp[i][0] = True
        # if nums[0] <= sub_sum:
        #     dp[0][nums[0]] = True
        # for ind in range(1,n):
        #     for target in range(1,sub_sum+1):
        #         notake = dp[ind-1][target]
        #         take = False
        #         if nums[ind] <= target:
        #             take = dp[ind-1][target-nums[ind]]
        #         dp[ind][target] = notake or take
        # return dp[n-1][sub_sum]