class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal(s):
            l,r = 0,len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    r-=1
                    l+=1
            return True
        for i in words:
            if pal(i):
                return i
        return ""