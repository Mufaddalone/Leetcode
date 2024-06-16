class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            if s[l] == s[r]:
                l,r= l+1,r-1
            else:
                return (isPal(s,l+1,r) or isPal(s,l,r-1))
        return True
    
def isPal(s,l,r):
    while l<r:
        if  s[l] == s[r]:
            l,r = l+1,r-1
        else:
            return False
    return True
            

