class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balanced = 0
        counter = 0
        for i in range(len(s)):
            count = 0
            if(s[i]=='L'):
                counter+=1
            else:
                counter-=1
            if(counter==0):
                balanced+=1
        return balanced
