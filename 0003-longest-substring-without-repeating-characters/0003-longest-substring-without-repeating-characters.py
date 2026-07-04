class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            res=''
            for j in range(i,len(s)):
                if s[j] not in res:
                    res+=s[j]
                    count=max(count,len(res))
                else:
                    break
        return count



















        # count=0  
        # for i in range(len(s)):
        #     res=''
        #     c=0
        #     for j in range(i,len(s)):
        #         if s[j] not in res:
        #             res+=s[j]
        #             c+=1
        #         else:
        #             break
        #     count = max(count,c)                
        # return count