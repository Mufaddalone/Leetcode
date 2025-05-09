class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        d = {}
        sums = 0
        count = 0
        n = len(a)
        for i in range(n):
            sums+= a[i]
            if sums ==k:
                count+=1
            rem = sums-k
            if rem in d:
                count += d[rem]
            if sums in d:
                d[sums] +=1
            else:
                d[sums] = 1
        return count
        # n = len(a) # size of the array.

        # preSumMap = {}
        # Sum = 0
        # count = 0
        # for i in range(n):
        #     Sum += a[i]

        #     if Sum == k:
        #         count+=1

        #     rem = Sum - k

        #     if rem in preSumMap:
        #         count+= preSumMap[rem]

        #     if Sum in preSumMap:
        #         preSumMap[Sum] += 1
        #     else:
        #         preSumMap[Sum] = 1

        # return count
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     sums = 0
        #     for j in range(i,n):
        #         sums += nums[j]
        #         if sums == k:
        #             count+=1
        # return count