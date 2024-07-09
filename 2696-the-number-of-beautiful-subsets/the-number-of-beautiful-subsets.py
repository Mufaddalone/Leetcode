class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def back(i,count):
            if i == len(nums):
                return 1
            
            res = back(i+1, count)
            if not count[nums[i]+k] and not count[nums[i]-k]:
                count[nums[i]] +=1
                res += back(i+1,count)
                count[nums[i]] -= 1
            return res

        return back(0, defaultdict(int)) -1