class Solution(object):
    def reverse(self, x):
        number = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])
        if -2 ** 31 <= number <= (2 ** 31) - 1:
            return number
        return 0