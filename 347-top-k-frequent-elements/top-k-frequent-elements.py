class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        b = [[] for i in range(len(nums)+1)]
        c = []

        for i in nums:
            a[i] = a.get(i,0)+1

        for i,j in a.items():
            b[j].append(i)

        for i in range(len(b)-1,-1,-1):
            for n in b[i]:
                c.append(n)
                if len(c) == k:
                    return c

        
        # for j in a.items():
        #     b.append(j[1])
        # b.sort()
        # for z in b:
        #     c.append(a[z])
        # return c[:k]
        
        #The question wants k frequent item k is not the limiter but the amount
        # for j in a.items():
        #     if j[1]>=k:
        #         b.append(j[0])
        # return b
        #     if a[j] >= k:
        #         b.append(a)
        # return b
        #     if j==k:
        #         b.append(a)
        # return b

