class Solution:
    def sumof(self, num):
        res = 0
        while num > 0:
            digit = num % 10
            res += digit * digit
            num //= 10
        return res

    def isHappy(self, n: int) -> bool:
        res = n
        while True:
            if res == 1:
                return True
            elif res == 4:
                return False
            else:
                res = self.sumof(res)