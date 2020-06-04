class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        numbs = [[],[]]
        for i in A:
            if(i%2==0):
                numbs[0].append(i)
            else:
                numbs[1].append(i)
        lst = []
        for i in range(len(A)/2):
            lst.append(numbs[0][i])
            lst.append(numbs[1][i])
        return lst        
