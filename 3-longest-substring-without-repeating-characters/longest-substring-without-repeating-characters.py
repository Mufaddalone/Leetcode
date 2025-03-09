class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a= defaultdict(int)
        l = 0
        maxlen = 0
        for r in range(len(s)):
            a[s[r]]+=1
            if s[r] in a:
                while a[s[r]]>1:
                    a[s[l]]-=1
                    l+=1
            maxlen= max(r-l+1,maxlen)
        return maxlen
