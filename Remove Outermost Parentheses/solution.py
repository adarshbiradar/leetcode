class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count=0
        final=""
        stack=[]
        for i in S:
            if i == "(":
                count+=1
                if count!=1:
                    final+=i
            else:
                count-=1
                if count!=0:
                    final+=i
        return final
