class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lst = [x**2 for x in A]
        lst.sort()
        return lst
