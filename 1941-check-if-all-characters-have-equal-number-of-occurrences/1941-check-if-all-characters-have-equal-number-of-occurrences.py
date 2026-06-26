class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        res=s.count(s[0])
        for i in s:
            if s.count(i) != res:
                return False
        return True