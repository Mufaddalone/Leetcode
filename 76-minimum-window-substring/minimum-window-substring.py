class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT= defaultdict(int)
        window= defaultdict(int)
        for i in t:
            countT[i]+=1
        l=0
        have = 0
        need = len(countT)
        res,reslen = [-1,-1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[s[r]]+=1
            if c and countT[c] == window[c]:
                have+=1
            while have == need:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen!=float("inf") else  ""
 
        # if t == "": return ""
        # countT , window = {},{}

        # for i in t:
        #     countT[i] = countT.get(i,0)+1

        # have , need = 0 , len(countT)
        # res , resLen = [-1,-1] , float("infinity")
        # l = 0
        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = window.get(c,0) +1 
        #     print(window)

        #     if c in countT and window[c] == countT[c]:
        #         have+=1

        #     while have == need:
        #         #update our result
        #         if (r-l+1) < resLen:
        #             resLen = (r-l+1)
        #             res = [l,r]
        #         #pop from the left of the window
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -=1
        #         l+=1
        #     l,r = res
        # return s[l:r+1] if resLen != float("infinity") else  ""
    

        