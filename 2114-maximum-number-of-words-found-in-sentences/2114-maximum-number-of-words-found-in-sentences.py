class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        g = 0

        for sentence in sentences:
            g = max(g, len(sentence.split()))

        return g