class Solution(object):
    def addOperators(self, num, target):
        if not num: return []
        res = []
        self.addition(num, 0, "", res, target)
        return res

    def addition(self, num, val, s, res, target):
        if not num:
            if val == target:
                res.append(s)
            return
        for i in xrange(len(num)):
            for p, v in self.product(num[:i + 1], [], 1):
                if s:
                    self.addition(num[i + 1:], val + v, s + '+' + p, res, target)
                    self.addition(num[i + 1:], val - v, s + '-' + p, res, target)
                else:
                    self.addition(num[i + 1:], val + v, p, res, target)

    def product(self, s, temp, val):
        if not s:
            yield ['*'.join(temp), val]
            return

        for i in xrange(len(s)):
            new = s[:i + 1]
            if len(new) > 1 and new[0] == '0': break
            temp.append(new)
            for x in self.product(s[i + 1:], temp, val * int(new)):
                yield x
            temp.pop()
