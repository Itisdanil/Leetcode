class Solution(object):
    def checkIfPangram(self, sentence):
        if len(list(set(sentence))) == 26:
            return True
        return False