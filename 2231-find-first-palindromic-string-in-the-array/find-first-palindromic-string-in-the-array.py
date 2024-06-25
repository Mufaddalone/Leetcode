class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def pal(i):
            l,r = 0,len(i)-1
            while l<r:
                if i[l]!=i[r]:
                    return False
                l,r = l+1,r-1
            return True
        for i in words:
            if pal(i):
                return i
        return ""
        
