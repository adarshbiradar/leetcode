class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        while(n>0):
            digits.append(n%10)
            n=n//10
        addition = sum(digits)
        multi = 1
        for i in digits:
            multi*=i
        return multi - addition
        
        
