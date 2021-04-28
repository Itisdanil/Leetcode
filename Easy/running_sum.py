class Solution(object):
    def runningSum(self, nums):
        list_sum, sum = [], 0
        for i in range(len(nums)):
            sum += nums[i]
            list_sum.append(sum)
        return list_sum