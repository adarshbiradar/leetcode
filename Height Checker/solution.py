class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        arranged = sorted(heights)
        for i in range(len(heights)):
            if(heights[i]!=arranged[i]):
                count+=1
        return count
