class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        def jumper(arr):
            l,r =0,0
            jumps = 0
            while r<n-1:
                mini = 0
                for i in range(l,r+1):
                    mini = max(mini,i+arr[i])
                l= r+1
                r = mini
                jumps+=1
            return jumps
        return jumper(nums)



