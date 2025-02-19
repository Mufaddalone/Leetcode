class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        z = defaultdict(int)
        l = 0
        maxlen = 0
        for r in range(len(nums)):
            z[nums[r]]+=1
            while z[nums[r]]>k:
                z[nums[l]]-=1
                l+=1
            maxlen = max(maxlen,r-l+1)
        return maxlen