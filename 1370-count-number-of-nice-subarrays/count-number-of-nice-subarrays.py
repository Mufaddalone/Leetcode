class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res,sums =0,0
        d= {0:1}
        for i in nums:
            if i%2 ==1:
                sums+=1
            rem = sums - k
            if rem in d:
                res+=d[rem]
            if sums in d:
                d[sums] +=1
            else:
                d[sums] = 1
        return res