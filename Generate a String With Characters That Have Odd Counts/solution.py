class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n==0):
            return ""
        lst = []
        if(n%2!=0):
            return "".join(['a' for i in range(n)])
        elif(n%2==0):
            for i in range(n-1):
               lst.append("a")
            lst.append("b")
        return "".join([x for x in lst])
