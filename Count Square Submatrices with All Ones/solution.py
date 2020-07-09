class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if(len(matrix)==0):
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==1:
                    if i==0 or j==0:
                        result+=1
                    else:
                        value = min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])+1
                        result+=value
                        matrix[i][j]=value
                        
        return result
