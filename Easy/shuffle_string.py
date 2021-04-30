class Solution(object):
    def restoreString(self, s, indices):
        list_str = [''] * len(s)
        for index, elem in enumerate(s):
            list_str[indices[index]] = elem
        return "".join(list_str)