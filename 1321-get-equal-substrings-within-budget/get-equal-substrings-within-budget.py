class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currcost= 0
        l =0
        maxlen = 0
        for i in range(len(s)):
            currcost += abs(ord(s[i]) - ord(t[i]))
            while currcost > maxCost:
                currcost -= abs(ord(s[l]) - ord(t[l]))
                l+=1
            maxlen = max(maxlen,i-l+1)
        return maxlen
        
                
