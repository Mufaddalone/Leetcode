class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        z = set()
        l= 0 
        maxlen = 0
        for r in range(len(s)):
            while s[r] in z:
                z.remove(s[l])
                l+=1
            z.add(s[r])
            maxlen = max(r-l+1,maxlen)    
        return maxlen