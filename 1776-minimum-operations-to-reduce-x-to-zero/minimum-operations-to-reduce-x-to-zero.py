class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l= 0 
        target = sum(nums) - x
        if target < 0:
            return -1
        maxlen = -1
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total > target:
                total-=nums[l]
                l+=1
            if total == target:
                maxlen = max(maxlen, r - l + 1)
        return len(nums) - maxlen if maxlen != -1 else -1