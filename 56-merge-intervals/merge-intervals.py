class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l,r =0, 1
        res = []
        intervals.sort(key=lambda x: x[0])
        # if len(intervals) <=1:
        #     return [intervals[-1]]
        while r<len(intervals):
            if intervals[l][-1] >= intervals[r][0]:
                while r<len(intervals) and intervals[l][-1] >= intervals[r][0]:
                    intervals[l][-1] = max(intervals[l][-1], intervals[r][-1])
                    r+=1
                res.append(intervals[l])
                l=r
            else:
                res.append(intervals[l])
                l=r
                r+=1
        if l < len(intervals):
            res.append(intervals[l])
        
        return res