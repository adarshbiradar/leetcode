class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split(' ')
        for i in range(len(lst)):
            lst[i] = lst[i][len(lst[i])::-1]
        return " ".join(lst)
