class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        z = defaultdict(int)
        l = 0
        maxlen = 0
        maxFreq = 0 
        for r in range(len(nums)):
            z[nums[r]]+=1
            maxFreq = max(maxFreq, z[nums[r]])
            while maxFreq>k:
                if z[nums[l]] == maxFreq:
                    maxFreq -=1
                z[nums[l]]-=1
                l+=1
            maxlen = max(maxlen,r-l+1)
        return maxlen