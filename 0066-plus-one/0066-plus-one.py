class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for i in digits:
            res+=str(i)
        res=int(res)+1
        d = []
        for i in str(res):
            d.append(int(i))
        return d
