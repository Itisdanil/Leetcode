class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        for word in words:
            sum, list_word = 0, list(set(word))
            for item in list_word:
                if item in allowed:
                    sum += 1
            if sum == len(list_word):
                count += 1
        return count