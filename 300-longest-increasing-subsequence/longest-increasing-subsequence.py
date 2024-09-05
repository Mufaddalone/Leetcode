class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(0,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = [[-1 for j in range(len(nums)+1)]for i in range(len(nums))]
#         def lis(ind,prev_ind):
#             if ind == len(nums):
#                 return 0
#             if dp[ind][prev_ind + 1] != -1:
#                 return dp[ind][prev_ind + 1]
#             leng = lis(ind+1,prev_ind)
#             if (prev_ind ==-1 or nums[ind]>nums[prev_ind]):
#                 leng = max(leng,1 + lis(ind+1,ind))
#             dp[ind][prev_ind+1] = leng
#             return dp[ind][prev_ind+1]
#         return lis(0,-1)