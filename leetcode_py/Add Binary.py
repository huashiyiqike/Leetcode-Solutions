class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        a = map(int, a[::-1])
        b = map(int, b[::-1])
        i = j = carry = 0
        res = []
        while i < len(a) and j < len(b):
            res.append(a[i] + b[j] + carry)
            carry = res[-1] / 2
            res[-1] %= 2
            i += 1
            j += 1
        while i < len(a):
            res.append(a[i] + carry)
            carry = res[-1] / 2
            res[-1] %= 2
            i += 1
        while j < len(b):
            res.append(b[j] + carry)
            carry = res[-1] / 2
            res[-1] %= 2
            j += 1
        if carry:
            res.append(carry)
        return ''.join(map(str, res))[::-1]


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        carry, res = 0, ""
        for i in range(max(len(a), len(b))):
            tmpres = carry
            if i < len(a):
                tmpres += int(a[-1 - i])
            if i < len(b):
                tmpres += int(b[-1 - i])
            # tmpres+=carry
            carry, tmpres = tmpres / 2, tmpres % 2
            res = "{0}{1}".format(tmpres, res)
        if carry:
            res = "1" + res  # "{0}{1}".format(carry,res)
        return res
