class Solution(object):
    def decode(self, encoded, first):
        result = [first] * (len(encoded) + 1)
        for i in range(len(encoded)):
            result[i + 1] = encoded[i] ^ result[i]
        return result