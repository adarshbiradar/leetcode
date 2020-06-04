class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])
        
        lst = []
        
        for i in range(n):
            minimum = min(matrix[i])
            index = matrix[i].index(minimum)
            maximum = 0
            for j in range(len(matrix)):
                if matrix[j][index]>maximum:
                    maximum = matrix[j][index]
            if(maximum == minimum):
                lst.append(minimum)
                
        return lst
