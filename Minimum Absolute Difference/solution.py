class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minAbs = min([arr[i]-arr[i-1] for i in range(1,len(arr))])
        result = []
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1])==minAbs:
                result.append([arr[i-1],arr[i]])
        return result
