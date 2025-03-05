class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxi = 0
        z = defaultdict(int)
        for r in range(len(s)):
            z[s[r]]+=1
            if r-l+1-max(z.values())>k:
                z[s[l]]-=1
                l+=1
            maxi = max(maxi,r-l+1)
        return maxi