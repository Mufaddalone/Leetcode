class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        maps = [0] * len(nums)
        ans = []
        arr = []

        def perm(arr,maps):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 
            for i in range(len(nums)):
                if (maps[i] == False):
                    arr.append(nums[i])
                    maps[i] = True
                    perm(arr,maps)
                    arr.remove(nums[i])
                    maps[i] = False
        perm(arr,maps)
        return ans
