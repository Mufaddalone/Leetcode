class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k>0 and int(stack[-1])> int(num[i]):
                stack.pop()
                k-=1
            stack.append(num[i])
        while k:
            stack.pop()
            k-=1
        if not stack: return "0"
        res = ""
        while stack:
            res+=stack.pop()
        res = res[::-1].lstrip("0")
        return res if res else "0"

