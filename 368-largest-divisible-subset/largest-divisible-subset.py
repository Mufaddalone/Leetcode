class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n
        hash = list(range(n))
        max_len, max_index = 1, 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    hash[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        result = []
        while len(result) < max_len:
            result.append(nums[max_index])
            max_index = hash[max_index]
        
        return result[::-1]

# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return []
        
#         nums.sort()
#         n = len(nums)
#         dp = [1] * n
#         hash = list(range(n))
#         max_len, max_index = 1, 0

#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
#                     dp[i] = dp[j] + 1
#                     hash[i] = j
#             if dp[i] > max_len:
#                 max_len = dp[i]
#                 max_index = i

#         result = []
#         while len(result) < max_len:
#             result.append(nums[max_index])
#             max_index = hash[max_index]

#         return result[::-1]
        