class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum % 2 != 0:
            return False
        sub_sum = arr_sum//2
        n = len(nums)
        dp = [[False for j in range(sub_sum+1)]for i in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= sub_sum:
            dp[0][nums[0]] = True
        for ind in range(1,n):
            for target in range(1,sub_sum+1):
                notake = dp[ind-1][target]
                take = False
                if nums[ind] <= target:
                    take = dp[ind-1][target-nums[ind]]
                dp[ind][target] = notake or take
        return dp[n-1][sub_sum]