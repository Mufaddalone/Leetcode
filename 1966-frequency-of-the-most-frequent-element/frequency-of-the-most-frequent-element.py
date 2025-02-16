class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l= 0 
        nums.sort()
        total = 0
        res = 0
        for r in range(len(nums)):
            total += nums[r]

            while nums[r]*(r-l+1) > total +k:
                total -= nums[l]
                l+=1
            res = max(res,r-l+1)
        return res
