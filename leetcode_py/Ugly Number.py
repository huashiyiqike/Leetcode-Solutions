class Solution(object):
    def helper(self, num, n):
        while num % n == 0 and num >= n:
            num /= n
        return num

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = self.helper(num, 5)
        num = self.helper(num, 3)
        num = self.helper(num, 2)
        return num == 1
