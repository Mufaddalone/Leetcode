class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r = 0,0
        count =0
        s.sort()
        g.sort()
        while l<len(g) and r<len(s):
            if g[l]-s[r] <=0:
                count+=1
                l+=1
                r+=1
            else:
                r+=1
        return count
        