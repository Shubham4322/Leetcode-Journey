class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet=[chr(i) for i in range(97,97+26)]
        sentence=sentence.lower()
        for i in alphabet:
            if i not in sentence:
                return False
        return True
        