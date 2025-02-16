class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l= 0 
        r = len(s1)
        z= defaultdict(int)
        b = defaultdict(int)
        for i in s1:
            b[i]+=1
        for r in range(len(s2)):
            z[s2[r]]+=1
            if r-l+1 == len(s1):
                if z==b:
                    return True
                z[s2[l]] -= 1
                if z[s2[l]] == 0:
                    del z[s2[l]]  
                l += 1
        return False
