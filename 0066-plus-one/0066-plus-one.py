class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # res = ''
        # for i in digits:
        #     res+=str(i)
        # res=int(res)+1
        # d = []
        # for i in str(res):
        #     d.append(int(i))
        # return d

        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits

            else:
                digits[i]=0
        return [1]+digits