class Solution:
    def reverseWords(self, s: str) -> str:
        l,r = 0,0
        ans =""
        while r<len(s):
            if s[r] == " ":
                ans+=s[l:r][::-1]
                ans+=" "
                l=r+1
                r+=1
            else:
                r+=1
        ans+=s[l:][::-1]
        return ans

        