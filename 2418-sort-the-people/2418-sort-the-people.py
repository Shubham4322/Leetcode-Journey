class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}

        for i in range(len(names)):
            d[heights[i]] = names[i]

        res = []

        for h in sorted(heights, reverse=True):
            res.append(d[h])

        return res