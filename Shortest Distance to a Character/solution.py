class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        result = []
        distances = []
        s1 = list(S)
        indices = [i for i,x in enumerate(s1) if x==C]
        for i in range(len(s1)):
            lst = [abs(x-i) for x in indices]
            result.append(min(lst))
        return result
