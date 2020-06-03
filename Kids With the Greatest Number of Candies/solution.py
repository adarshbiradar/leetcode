class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        mm = max(candies)
        candies = [x+extraCandies for x in candies]
        return [x>=mm for x in candies]
