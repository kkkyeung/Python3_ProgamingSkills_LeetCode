class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) >= output:
                output = sum(accounts[i])
        return output