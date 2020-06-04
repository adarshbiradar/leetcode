class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        l=0
        r=0
        u=0
        d=0
        for i in moves:
            if(i=="L"):
                l+=1
            elif(i=='R'):
                r+=1
            elif(i=="U"):
                u+=1
            else:
                d+=1
        return l==r and u==d
        
