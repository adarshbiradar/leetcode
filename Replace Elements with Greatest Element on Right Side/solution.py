class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in range(len(arr)-1):
            lst.append(max(arr[i+1:]))
        lst.append(-1)
        return lst
        
