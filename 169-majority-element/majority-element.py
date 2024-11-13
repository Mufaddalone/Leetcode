class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count =0,0
        for i in nums:
            if count ==0:
                res = i
            count += (1 if i==res else -1)
        return res
        # a = {}
        # maxcount = 0
        # res = 0
        # for i in range(len(nums)):
        #     a[nums[i]] = a.get(nums[i],0)+1
        #     res = nums[i] if a[nums[i]] > maxcount else res
        #     maxcount = max(maxcount,a[nums[i]])
        # return res
        # for k,i in a.items():
        #     if i >= len(nums)/2:
        #         return k
            