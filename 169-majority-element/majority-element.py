class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = a.get(nums[i],0)+1
        print(a)
        for k,i in a.items():
            if i >= len(nums)/2:
                return k
            