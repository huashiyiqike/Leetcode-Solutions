class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for i in nums:
            diff ^= i
        diff &= -diff
        res = [0, 0]
        for i in nums:
            if i & diff == 0:
                res[0] ^= i
            else:
                res[1] ^= i
        return res
