class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        greater = 0
        for i in accounts:
            temp=0
            for j in i:
                temp+=j
            if temp>greater:
                greater=temp
        return greater