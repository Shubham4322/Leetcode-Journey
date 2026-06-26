class Solution:
    def digit_sum(self,num):
        res=0
        while num>0:
            res+=num%10
            num//=10
        return res
    def differenceOfSum(self, nums: List[int]) -> int:
        res1=0
        res2=0
        for i in nums:
            res2+=self.digit_sum(i)
            res1+=i
        return res1-res2
        