class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)-1
        i=0
        while i<l:
            s[i],s[l]=s[l],s[i]
            l-=1
            i+=1
        return s