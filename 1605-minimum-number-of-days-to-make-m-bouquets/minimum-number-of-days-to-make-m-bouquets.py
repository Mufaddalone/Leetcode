class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def finder(day):
            count,boq = 0,0
            for i in bloomDay:
                if day>=i:
                    count+=1
                else:
                    boq += count//k
                    count = 0
            boq += count//k
            return boq>=m
        l,r = min(bloomDay),max(bloomDay)
        val = k*m
        if len(bloomDay) <val:
            return -1
        while l<=r:
            mid = (l+r)//2
            if finder(mid):
                r = mid-1
            else:
                l = mid+1
        return l

            

            