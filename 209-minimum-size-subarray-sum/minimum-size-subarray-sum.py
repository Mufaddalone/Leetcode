class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l=0
        maxlen = float("inf")
        for r in range(len(nums)):
            total+= nums[r]
            while total>=target:
                maxlen = min(r-l+1,maxlen)
                total -= nums[l]
                l+=1
        return maxlen if maxlen!=float("inf") else 0

