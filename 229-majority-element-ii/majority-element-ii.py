class Solution:
    def majorityElement(self, v: List[int]) -> List[int]:
        n = len(v) # size of the array

        cnt1, cnt2 = 0, 0 # counts
        el1, el2 = float('-inf'), float('-inf') # element 1 and element 2

        # applying the Extended Boyer Moore’s Voting Algorithm:
        for i in range(n):
            if cnt1 == 0 and el2 != v[i]:
                cnt1 = 1
                el1 = v[i]
            elif cnt2 == 0 and el1 != v[i]:
                cnt2 = 1
                el2 = v[i]
            elif v[i] == el1:
                cnt1 += 1
            elif v[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ls = [] # list of answers

        # Manually check if the stored elements in
        # el1 and el2 are the majority elements:
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if v[i] == el1:
                cnt1 += 1
            if v[i] == el2:
                cnt2 += 1

        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)

        # Uncomment the following line
        # if it is told to sort the answer array:
        #ls.sort() #TC --> O(2*log2) ~ O(1);

        return ls
        # count = defaultdict(int)

        # for n in nums:
        #     count[n]+=1

        #     if len(count) <= 2:
        #         continue
        #     new_count = defaultdict(int)
        #     for n,c in count.items():
        #         count[n]-=1
        #         if c > 1:
        #             new_count[n] = c -1
        #     count = new_count
        # res = []
        # for n in count:
        #     if nums.count(n) > len(nums)//3:
        #         res.append(n)
        # return res