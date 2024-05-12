class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        l = 0
        z = set()

        for r in range(len(s)):
            while s[r] in z:
                z.remove(s[l])
                l+=1
            count = max(r-l+1,count)
            z.add(s[r])
            r+=1
        return count

        # l,r = 0,0
        # count = 0
        # a = []
        # while r < len(s):
        #     if s[r] in a:
        #         l = r
        #         a =[]
        #     a.append(s[r])
        #     count = max(count , len(a))
        #     r+=1
        # return count

#     def substring(s):
#     z = set()
#     l,r = 0, 0
#     count = 0
#     while r < len(s):
#         if s[r] in z:
#             count = max(count, r-l)
#             l = r
#         z.add(s[r])
#         r+=1
#     return count
    
# substring(" ")
        


            
                
        