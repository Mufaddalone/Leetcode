class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        maxlen = 0
        count = 0
        z = {"a", "e", "i", "o", "u"}
        for r in range(len(s)):
            if r-l+1>k:
                if s[l] in z:
                    count-=1
                l+=1
            if s[r] in z:
                count+=1
            maxlen = max(count,maxlen)
        return maxlen
            
                    