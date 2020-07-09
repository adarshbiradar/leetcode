class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if(len(arr)<=2):
            return True
        else:
            arr.sort()
            diff = arr[0]-arr[1]
            for i in range(len(arr)-1):
                if(arr[i]-arr[i+1]!=diff):
                    return False
            else:
                return True
