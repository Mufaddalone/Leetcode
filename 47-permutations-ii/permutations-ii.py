class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        maps = [0] * len(nums)
        arr =[]
        ans = []

        def back(ind,arr,maps):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            used = set()
            for i in range(len(nums)):
                # if i!=ind and nums[i]==nums[i-1]:continue
                if (maps[i]==False) and nums[i] not in used:
                    maps[i] = True
                    arr.append(nums[i])
                    used.add(nums[i])
                    back(i+1,arr,maps)
                    maps[i] = False
                    arr.pop()
        back(0,arr,maps)
        return ans
            
