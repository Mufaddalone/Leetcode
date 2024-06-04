class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in a:
                return [a[diff],i]
            a[nums[i]] = i




            