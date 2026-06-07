class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxt=0
        for i in range(len(accounts)):
            maxt=max(maxt,sum(accounts[i]))
        return maxt
        