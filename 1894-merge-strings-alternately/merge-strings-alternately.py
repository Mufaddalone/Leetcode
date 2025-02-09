class Solution:
    def mergeAlternately(self, l1: str, l2: str) -> str:
        l,r =0,0
        ans = ""
        while l<len(l1) and r<len(l2):
            ans+=l1[l]
            l+=1
            ans+=l2[r]
            r+=1
        if l <len(l1):
            ans+=l1[l:]
        elif r<len(l2):
            ans+=l2[r:]
        return ans