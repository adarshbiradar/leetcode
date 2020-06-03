class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = []
        while(num>0):
            digits.append(num%10)
            num=num//10
        digits.reverse()
        for i in range(len(digits)):
            if(digits[i]==6):
                digits[i]=9
                break
        number = 0
        for i in digits:
            number = number*10+i
        return number
