class Solution:
    def minFlips(self, s: str) -> int:
        l= 0
        n = len(s)
        alt1,alt2 = "", ""
        s_extended = s+s
        res = float("inf")
        for i in range(n*2):
            alt1 += "1" if i%2 == 0 else "0"
            alt2 += "0" if i%2 == 0 else "1"
        flip1,flip2 = 0,0
        for i in range(n*2):
            if alt1[i]!=s_extended[i]:
                flip1+=1
            if alt2[i]!= s_extended[i]:
                flip2+=1
            if i-l+1>n:
                if s_extended[l]!= alt1[l]:
                    flip1-=1
                if s_extended[l]!= alt2[l]:
                    flip2-=1
                l+=1
            if i-l+1 == n:
                res = min(flip1,flip2,res)
        return res

