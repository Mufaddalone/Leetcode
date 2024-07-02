class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr =[]
        ans = []
        nums.sort()
        def back(ind):
            ans.append(arr[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:continue
                arr.append(nums[i])
                back(i+1)
                arr.pop()
        back(0)
        return ans


