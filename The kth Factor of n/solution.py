class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1,int(n//2)+1):
            if(n%i==0):
                res.append(i)
        res.append(n)
        print(res)
        if(k<=len(res)):
            return res[k-1]
        else:
            return -1
