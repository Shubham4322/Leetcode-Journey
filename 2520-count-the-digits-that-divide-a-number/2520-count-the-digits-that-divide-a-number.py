class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        copy=num
        while num>0:
            if copy%(num%10)==0:
                count+=1
            num//=10
        return count
        