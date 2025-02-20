class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        window = defaultdict(int)
        for i in t:
            count[i]+=1
        l = 0
        have = 0
        need = len(count)
        res,reslen = [-1,-1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c]+=1
            if c and window[c] == count[c]:
                have+=1
            while have == need:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res =[l,r]
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen!=float("inf") else ""
