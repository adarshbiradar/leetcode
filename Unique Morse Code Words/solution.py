class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        dct = dict(zip(alpha,code))
        lst = []
        for word in words:
            lst.append("".join([dct[x] for x in word]))
        lst = set(lst)
        return len(lst)
