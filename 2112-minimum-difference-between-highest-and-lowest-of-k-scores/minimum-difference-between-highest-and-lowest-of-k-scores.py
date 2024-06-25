class Solution:
    def minimumDifference(self, s: List[int], k: int) -> int:
        s.sort()
        l,r = 0, k-1
        res = float("inf")
        while r < len(s):
            if s[r] - s[l] < res:
                res = s[r] - s[l]
            l,r = l+1,r+1
        return res

        
        