class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = []
        for n in nums:
            count[n]+=1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for i,c in count.items():
                if c >1:
                    new_count[i] = c-1
            count = new_count
        for n in count:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res