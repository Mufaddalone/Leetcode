class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left,right=0,len(nums)-1

        ans=collections.deque()

        while left<=right:
            l=abs(nums[left])
            r=abs(nums[right])
            if l>r:
                ans.appendleft(l**2)
                left+=1
            else:
                ans.appendleft(r**2)
                right-=1

        return list(ans)