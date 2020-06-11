class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        lst = [x for x in range(1,m+1)]
        result = []
        for query in queries:
            result.append(lst.index(query))
            lst.remove(query)
            lst.insert(0,query)
            
        return result
