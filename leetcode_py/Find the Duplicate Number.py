class Solution(object):
    def findDuplicate(self, nums):
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (right + left) / 2
            # i <= mid gives 1 else 0
            # sum is counting
            left, right = [left, mid] \
                if sum(i <= mid for i in nums) > mid \
                else [mid + 1, right]
        return right

        #    The idea is that if you have a number (e.g. 5) and there
        #  are 5 numbers in the array that are less than or equal to 5 then
        # the duplicate has to be a number greater than 5. Otherwise, by the
        #  pigeonhole principle the duplicate has to be one of the numbers
        #  between 1 and 5 inclusive.
