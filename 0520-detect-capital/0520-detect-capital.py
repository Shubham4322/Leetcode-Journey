class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for i in word:
            if 'A'<=i<='Z':
                count+=1
        if count == len(word):
            return True
        elif count == 0:
            return True
        elif count == 1 and 'A'<=word[0]<='Z' :
            return True
        else:
            return False