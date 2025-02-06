class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxlen = 0
        z = defaultdict(int)
        for r in range(len(s)):
            z[s[r]]+=1
            if r-l+1 - max(z.values())>k:
                z[s[l]]-=1
                l+=1
            maxlen = max(maxlen,r-l+1)
        return maxlen