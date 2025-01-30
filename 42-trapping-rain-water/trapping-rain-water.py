class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0 , len(height)-1
        res = 0
        lefth, righth = height[l],height[r]
        while l<r:
            if lefth<righth:
                l+=1
                lefth = max(lefth,height[l])
                res += lefth - height[l]
            else:
                r-=1
                righth = max(righth,height[r])
                res+= righth-height[r]
        return res
