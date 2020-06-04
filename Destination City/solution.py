class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        routes = dict(paths)
        for i in routes.values():
            if i not in routes.keys():
                return i
