class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [-1]*len(nums)
        stack = []
        n = len(nums)
        for i in range(n*2,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i<n:
                if not stack:
                    arr[i] =-1
                else:
                    arr[i] = stack[-1]
            stack.append(nums[i%n])
        return arr