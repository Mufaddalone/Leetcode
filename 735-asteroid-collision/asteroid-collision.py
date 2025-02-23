class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                while stack and stack[-1]>0 and abs(i) - stack[-1] >0:
                    stack.pop()
                if stack and abs(i) == stack[-1]:
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(i)
        return stack