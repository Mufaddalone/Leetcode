class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        def back(ind):
            ans.append(arr[:])
            for i in range(ind,len(nums)):
                arr.append(nums[i])
                back(i+1)
                arr.pop()
        back(0)
        return ans
        
            

