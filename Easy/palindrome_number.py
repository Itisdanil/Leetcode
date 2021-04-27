class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1] and -2**31 <= x <= 2**31 - 1:
            return True
        return False