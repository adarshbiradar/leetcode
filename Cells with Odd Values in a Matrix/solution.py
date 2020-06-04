class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        lst = [ [ 0 for i in range(m) ] for j in range(n) ] 
        for index in indices:
            for i in range(n):
                lst[i][index[1]]+=1
            for j in range(m):
                lst[index[0]][j]+=1
        count = 0
        for i in range(n):
            for j in range(m):
                if(lst[i][j]%2!=0):
                    count+=1
        return count
