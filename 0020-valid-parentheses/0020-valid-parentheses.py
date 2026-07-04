class Solution:
    def isValid(self, s: str) -> bool:
        b = {'{':'}','[':']','(':')'}
        c=[]
        for i in s:
            if i not in b:
                if not(c) or c.pop()!=i:
                    return False
            else:
                c.append(b[i])
        return len(c)==0












        # b = {'(':')','{':'}','[':']'}
        # c =[]
        # for i in s:
        #     if i not in b:
        #         if not(c) or c.pop()!=i:
        #             return False
        #     else:
        #         c.append(b[i])
        # return len(c)==0