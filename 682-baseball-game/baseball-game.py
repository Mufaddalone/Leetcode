class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(int(stack[-1])*2)
            elif i == "+":
                a = int(stack[-1])
                b = int(stack[-2])
                stack.append(a+b)
            else:
                stack.append(int(i))
        print(stack)
        return sum(stack)
