class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        dq = deque()
        ans = []
        for r in range(len(nums)):
            while dq and dq[0] <l:
                dq.popleft()
            while dq and nums[dq[-1]]<nums[r]:
                dq.pop()
            dq.append(r)
            if r-l+1 == k:
                ans.append(nums[dq[0]])
                l+=1
        return ans