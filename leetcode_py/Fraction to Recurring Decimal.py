from collections import defaultdict


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        res = ''
        if numerator * denominator < 0:
            res = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        dict = defaultdict(int)
        if numerator % denominator == 0:
            return res + str(numerator / denominator)

        res += str(numerator / denominator) + '.'
        numerator %= denominator
        idx = len(res)
        dict[numerator] = idx
        while True:
            idx += 1
            numerator *= 10
            res += str(numerator / denominator)
            numerator %= denominator
            if numerator in dict:
                if numerator != 0:
                    res = res[:dict[numerator]] + '(' + res[dict[numerator]:] + ')'
                else:
                    res = res[:-1]
                return res
            dict[numerator] = idx


if __name__ == "__main__":
    a = Solution()
    print a.fractionToDecimal(-2147483648, 1)
    print a.fractionToDecimal(7, -12)
    print a.fractionToDecimal(-50, 8)
    print a.fractionToDecimal(50, -8)
    print a.fractionToDecimal(1, 6)
    print a.fractionToDecimal(2, 3)
    print a.fractionToDecimal(1, 17)
    print a.fractionToDecimal(1, 99)
    print a.fractionToDecimal(1, 111)
    print a.fractionToDecimal(200, 1)
    print a.fractionToDecimal(1, 2)
    print a.fractionToDecimal(50, 11)
    print a.fractionToDecimal(50, 3)
    print a.fractionToDecimal(1, 111)
    print a.fractionToDecimal(124, 123)
    print a.fractionToDecimal(98, 99)
    print ''


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        #         res=[]
        #         res.extend(str(numerator/denominator).split())
        sign = 1
        if (numerator < 0 and denominator < 0) or (numerator > 0 and denominator > 0):
            sign = 1
        elif numerator < 0:
            sign, numerator = -1, -numerator
        elif denominator < 0:
            sign, denominator = -1, -denominator

        res = str(numerator / denominator)
        if sign == -1:
            res = '-' + res
        dict = {}
        if numerator % denominator == 0:
            return res
        res += '.'
        idx = len(res)
        flag = False

        while numerator % denominator != 0:
            numerator %= denominator
            tmp = numerator % denominator
            numerator *= 10
            tmp1 = numerator / denominator

            if tmp != 0:
                flag = True
            if tmp in dict:
                if tmp != 0:
                    res = res[:dict[tmp]] + '(' + res[dict[tmp]:] + ')'
                    return res
                elif flag:
                    res = res[:dict[tmp]] + '(' + res[dict[tmp]:] + ')'
                    return res

            res += str(tmp1)
            if tmp not in dict:
                dict[tmp] = idx
            idx += 1

        return res


if __name__ == "__main__":
    a = Solution()
    print a.fractionToDecimal(-2147483648, 1)
    print a.fractionToDecimal(7, -12)
    print a.fractionToDecimal(-50, 8)
    print a.fractionToDecimal(50, -8)
    print a.fractionToDecimal(1, 6)
    print a.fractionToDecimal(2, 3)
    print a.fractionToDecimal(1, 17)
    print a.fractionToDecimal(1, 99)
    print a.fractionToDecimal(1, 111)
    print a.fractionToDecimal(200, 1)
    print a.fractionToDecimal(1, 2)
    print a.fractionToDecimal(50, 11)
    print a.fractionToDecimal(50, 3)
    print a.fractionToDecimal(1, 111)
    print a.fractionToDecimal(124, 123)
    print a.fractionToDecimal(98, 99)
