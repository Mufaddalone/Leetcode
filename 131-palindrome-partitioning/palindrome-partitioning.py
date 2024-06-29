class Solution:
    def partition(self, s: str) -> List[List[str]]:
        arr = []
        ans = []

        def part(ind):
            if ind == len(s):
                ans.append(arr[:])
                return
            for i in range(ind,len(s)):
                if (ispal(ind,i,s)):
                    arr.append(s[ind:i+1])
                    part(i+1)
                    arr.pop()
        def ispal(l,r,s):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        part(0)
        return ans
            
