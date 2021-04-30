class Solution(object):
    def maximumWealth(self, accounts):
        sum_account = []
        for account in accounts:
            sum_account.append(sum(account))
        return max(sum_account)