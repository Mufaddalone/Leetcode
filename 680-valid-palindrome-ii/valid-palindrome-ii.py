class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(s):
            l,r =0,len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r =0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipleft, skipright = pal(s[l+1:r+1]),pal(s[l:r])
                return skipleft or skipright
            l+=1
            r-=1
        return True

