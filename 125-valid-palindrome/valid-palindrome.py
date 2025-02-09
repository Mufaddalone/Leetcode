class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while r>l and not s[r].isalnum():
                r-=1
            if s[l].lower()!= s[r].lower():
                return False
            r-=1
            l+=1
        return True
 
    # def alphaNum(self, c):
    #     return (ord("A") <= ord(c) <= ord("Z")or 
    #         ord("a") <= ord(c) <= ord("z") or
    #         ord("0") <= ord(c) <= ord("9"))
        # a = ""
        # for i in s:
        #     if i.isalnum():
        #         a+=i.lower()
        # return a == a[::-1]
        # a = []
        # for i in s:
        #     if len(s) <=1:
        #         return True
        #     if not i.isalnum():
        #         continue
        #     else:
        #         a.append(i.lower())
        # if a == a[::-1]:
        #     return True
        # return False