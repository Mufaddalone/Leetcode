class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [-1]*len(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,i+n):
                ind = j%n
                if nums[ind]> nums[i]:
                    arr[i] = nums[ind]
                    break
        return arr
