class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in A:
            i.reverse()
        for i in range(len(A)):
            for j in range(len(A[i])):
                if(A[i][j]==0):
                    A[i][j]=1
                else:
                    A[i][j]=0
        return A
