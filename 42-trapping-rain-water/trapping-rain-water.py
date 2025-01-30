class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix = [height[0]]
        # for i in range(1,len(height)):
        #     prefix.append(max(prefix[i-1],height[i]))
        sufix = [0]*len(height)
        sufix[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            sufix[i] = max(sufix[i+1],height[i])
        total = 0
        leftmax = height[0]
        for i in range(len(height)):
            if height[i]<=leftmax and height[i]<= sufix[i]:
                total += min(leftmax,sufix[i]) - height[i]
            leftmax = max(leftmax,height[i])
        return total
        # for i in range(len(height)):
        #     if height[i] <= prefix[i] and height[i] <= sufix[i]:
        #         total += min(prefix[i],sufix[i]) - height[i]
        # return total
