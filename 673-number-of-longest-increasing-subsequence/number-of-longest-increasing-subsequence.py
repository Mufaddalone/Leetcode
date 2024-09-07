class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n  # length of LIS ending at i
        count = [1] * n  # number of LIS ending at i
        max_len = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            max_len = max(max_len, dp[i])
        
        return sum(count[i] for i in range(n) if dp[i] == max_len)
        