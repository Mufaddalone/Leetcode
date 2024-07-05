class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) //4 
        side = [0]*4

        if sum(matchsticks)/4 != length:
            return False

        matchsticks.sort(reverse= True)
        def back(ind):
            if ind == len(matchsticks):
                return True
            for i in range(4):
                if side[i] + matchsticks[ind] <= length:
                    side[i] += matchsticks[ind]
                    if back(ind+1):
                        return True
                    side[i] -= matchsticks[ind]
            return False
        return back(0)