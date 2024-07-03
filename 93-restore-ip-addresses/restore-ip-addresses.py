class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s)>12:
            return ans
        def back(i,dots,arr):
            if dots == 4 and i == len(s):
                ans.append(arr[:-1])
                return
            if dots>4:
                return
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                    back(j+1,dots+1,arr+s[i:j+1] + ".")
        back(0,0,"")
        return ans

