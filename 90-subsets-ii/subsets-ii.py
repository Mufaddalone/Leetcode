class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = []
        ans = []
        nums.sort()
        def backtracking(ind):
            ans.append(arr[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i] == nums[i-1]: continue
                arr.append(nums[i])
                backtracking(i+1)
                arr.remove(nums[i])
        backtracking(0)
        return ans
