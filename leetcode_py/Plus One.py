class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        tmp = digits[::-1]
        plus = 1
        res = []
        for i in tmp:
            t = int(i) + plus
            res.append((t % 10))
            plus = t / 10
        if plus > 0:
            res.append(1)
        return res[::-1]
