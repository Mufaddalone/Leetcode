class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for i in s:
            a[i] = a.get(i,0)+1
        for i in t:
            a[i] = a.get(i,0)-1
        
        for i in a.values():
            if i!=0:
                return False
        return True

