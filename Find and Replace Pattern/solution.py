class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def helper(s):
            res = []
            chars = []
            for i in s:
                if i in chars:
                    res.append(chars.index(i))
                else:
                    chars.append(i)
                    res.append(chars.index(i))
            return res
        words_number = [helper(x) for x in words]
        pattern_number = helper(pattern)
        res = []
        for idx,word in enumerate(words_number):
            if word == pattern_number:
                res.append(idx)
        ans = []
        for idx in res:
            ans.append(words[idx])
        return ans
