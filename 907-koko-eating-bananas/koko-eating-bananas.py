import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        l,r = 1,n
        maxtime = 0
        while l<=r:
            time = 0
            mid = (l+r)//2
            for i in piles:
                time += math.ceil(i/mid)
            if time<=h:
                maxtime = mid
                r = mid-1
            else:
                l= mid+1
        return maxtime