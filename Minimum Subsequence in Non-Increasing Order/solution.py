class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        nums.sort()
        lst = [nums.pop()]
        while sum(lst)<=sum(nums):
            lst.append(nums.pop())
        return lst
