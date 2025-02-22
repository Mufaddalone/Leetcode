class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        ans = ""
        for i in s:
            if i =="*":
                stack.pop()
            else:
                stack.append(i)
        for i in stack:
            ans += i
        return ans
