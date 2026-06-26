class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        res = ""
        i = 0

        while i < k:
            res += s[i] + " "
            i += 1

        return res.strip()