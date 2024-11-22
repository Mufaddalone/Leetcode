class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r = 1,max(nums)
        def divisor(mid):
            divident = 0
            for i in nums:
                divident += math.ceil(i/mid)
            return divident
        while l<=r:
            mid = (l+r)//2 
            if divisor(mid) > threshold:
                l = mid+1
            else:
                r = mid-1
        return l
                