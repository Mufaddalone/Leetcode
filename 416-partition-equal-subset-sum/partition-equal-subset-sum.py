class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        array_sum = sum(nums)

        # If array sum is odd, it cannot be partitioned into equal sum subsets.
        if array_sum % 2 != 0:
            return False

        # Calculate the subset sum.
        subset_sum = array_sum // 2

        # Create a lookup table and fill all entries with False.
        dp = [[False for _ in range(len(nums) + 1)] for _ in range(subset_sum + 1)]

        # Initialize the first row as True as each array has a subset whose sum is zero
        for i in range(len(nums) + 1):
            dp[0][i] = True

        # Fill the lookup table in a bottom-up manner.
        for i in range(1, subset_sum + 1):
            for j in range(1, len(nums) + 1):
                if nums[j - 1] > i:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - nums[j - 1]][j - 1] or dp[i][j - 1]

        # Return the last index of the matrix, which is our answer
        return dp[subset_sum][len(nums)]