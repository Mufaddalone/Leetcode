class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        z = set()
        for i in nums:
            if i in z:
                return True
            z.add(i)
        return False
        # a = {}
        # for i in nums:
        #     if i in a:
        #         return True
        #     a[i] = a.get(i,0)+1
        # return False

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
