class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in digits:
            number = number*10 + i
        number+=1
        numbers = list(str(number))
        return list(map(int,numbers))
            
