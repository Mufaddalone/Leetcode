class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums ==k:
                count+=1
            rem = sums - k
            if rem in d:
                count += d[rem]
            if sums in d:
                d[sums] += 1
            else:
                d[sums] = 1
        return count
            
        