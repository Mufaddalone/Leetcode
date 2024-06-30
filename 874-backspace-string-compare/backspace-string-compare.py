class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []
        l=0
        while l<len(s) or l< len(t):
            if l<len(s) :
                if s[l] == "#" and a:
                    a.pop()
                elif s[l]!="#": 
                    a.append(s[l]) 
            if l<len(t):
                if t[l] == "#" and b:
                    b.pop()
                elif t[l]!="#": 
                    b.append(t[l]) 
            l+=1
        return a==b
        