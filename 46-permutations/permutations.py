class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        ind = 0
        def perm(ind):
            if ind == len(nums):
                ans.append(nums[:])
                return
            for i in range(ind,len(nums)):
                nums[ind],nums[i] = nums[i], nums[ind]
                perm(ind+1)
                nums[ind],nums[i] = nums[i], nums[ind]
        perm(0)
        return ans

        # maps = [0] * len(nums)
        # ans = []
        # arr = []

        # def perm(arr,maps):
        #     if len(arr) == len(nums):
        #         ans.append(arr[:])
        #         return 
        #     for i in range(len(nums)):
        #         if (maps[i] == False):
        #             arr.append(nums[i])
        #             maps[i] = True
        #             perm(arr,maps)
        #             arr.remove(nums[i])
        #             maps[i] = False
        # perm(arr,maps)
        # return ans
