class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
        def atmost(k):
            l = 0 
            z = {}
            count = 0
            for r in range(len(s)):
                z[s[r]] = z.get(s[r],0)+1
                while len(z)>k:
                    z[s[l]] = z.get(s[l],0)-1
                    if z[s[l]] ==0:
                        del z[s[l]]
                    l+=1
                count+= r-l+1
            return count
        ans = atmost(k) - atmost(k-1)
        return ans