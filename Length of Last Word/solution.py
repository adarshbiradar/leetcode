class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        words = list(filter(lambda a: a != "", words))
        try:
            return len(words[-1])
        except:
            return 0
