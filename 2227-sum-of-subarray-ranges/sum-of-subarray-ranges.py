class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        minia =[0]*len(nums)
        for i in range(len(nums)):
            while stack and nums[i]<=nums[stack[-1]]:
                stack.pop()
            j = -1 if not stack else stack[-1]
            minia[i] = minia[j] + (i-j)*nums[i]
            stack.append(i)
        mini = sum(minia)
        stack = []
        maxa = [0]*len(nums)
        for i in range(len(nums)):
            while stack and nums[i]>= nums[stack[-1]]:
                stack.pop()
            j= -1 if not stack else stack[-1]
            maxa[i] = maxa[j] + (i-j)*nums[i]
            stack.append(i)
        maxi = sum(maxa)
        return maxi - mini
        