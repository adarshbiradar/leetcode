class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        target = []
        for i in range(n-1):
            target.append(i)
        target.append(-(sum(target)))
        return target
