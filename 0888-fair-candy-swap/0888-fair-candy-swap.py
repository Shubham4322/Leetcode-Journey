class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff  = (sum(aliceSizes)-sum(bobSizes))//2
        for i in aliceSizes:
            res = i - diff
            if res in bobSizes:
                return [i,res]