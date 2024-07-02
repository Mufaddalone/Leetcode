class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = []
        ans = []

        def back(ind):
            if ind == len(nums):
                ans.append(nums[:])
                return 
            for i in range(ind,len(nums)):
                nums[i],nums[ind] = nums[ind],nums[i]
                back(ind+1)
                nums[i],nums[ind] = nums[ind],nums[i]
        back(0)
        return ans
        # maps = [0] * len(nums)
        # arr =[]
        # ans = []

        # def back(arr,maps):
        #     if len(arr) == len(nums):
        #         ans.append(arr[:])
        #         return
        #     for i in range(len(nums)):
        #         if (maps[i]==False):
        #             maps[i] = True
        #             arr.append(nums[i])
        #             back(arr,maps)
        #             maps[i] = False
        #             arr.pop()
        # back(arr,maps)
        # return ans