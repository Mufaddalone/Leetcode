class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        def airport(limit):
            din = 1 
            sums = 0
            for i in weights:
                if sums +i > limit:
                    din +=1
                    sums = i
                else:
                    sums+=i
            return din
        while l<=r:
            mid = (l+r)//2
            if airport(mid) >days:
                l=mid+1
            else:
                r = mid-1
        return l
        
                    

        