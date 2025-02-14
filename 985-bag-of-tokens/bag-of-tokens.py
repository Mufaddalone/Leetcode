class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r = 0,len(tokens)-1
        res =0
        while l<=r:
            if power-tokens[l]>=0:
                power -= tokens[l]
                res+=1
                l+=1
            elif l<r and res:
                power += tokens[r]
                r-=1
                res-=1
            else:
                break
        return res
