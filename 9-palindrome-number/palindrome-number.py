class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x>0 and x%10 == 0):
            return False
        revNum = 0
        while revNum < x:
            revNum = revNum*10 + x%10
            x = x//10
        if x==revNum or x==revNum//10:
            return True
        else:
            return False


        