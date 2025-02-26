class Solution:
    def decodeString(self, s: str) -> str:
        a = ""
        stack = []
        test = []
        for i in s:
            if i!= "]":
                stack.append(i)
            else:
                a = ""
                while stack[-1]!= "[":
                    a = stack.pop() + a
                stack.pop()
                no = ""
                while stack and stack[-1].isdigit(): 
                    no = stack.pop() + no
                stack.append(int(no)*a)
        return "".join(stack)
