class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        res = [0, 0]
        carry = 0
        for i in range(1, len(gas)+1):
            carry += gas[i-1] - cost[i-1]
            if carry < res[1]:
                res = [i, carry]
        res = res[0]%len(gas)
        carry = 0
        for i in range(res, res+len(gas)):
            i %= len(gas)
            carry += gas[i] - cost[i]
            if carry < 0:
                return -1
        return res

if __name__ == "__main__":
    a = Solution()
    print a.canCompleteCircuit([2, 4], [3, 4])
    print a.canCompleteCircuit([1, 2], [2, 1])
    print a.canCompleteCircuit([6,1,4,3,5], [3,8,2,4,2])
        # rest = []
        # start = 0
        # mins = 1 << 64
        # for i in range(len(gas)):
        #     rest.append(-cost[(len(cost)+i-1) % len(cost)] + gas[(len(gas)+i) % len(gas)] )
        #     if rest[i] < mins:
        #         start = i
        #         mins = rest[i]
        # print rest
        # total = 0
        # for i in range(start, start+len(gas)):
        #     total += gas[i % len(gas)] - cost[i % len(gas)]
        #     if total < 0:
        #         return -1
        # return start
        #
        #
        # gas = map(lambda x, y: x - y, gas, cost)
        # maxs = -1<<64
        # idx = 0
        # for i in range(len(gas)):
        #     if gas[i] > maxs:
        #         idx = i
        #         maxs = gas[i]
        # all = 0
        # for i in range(idx, idx + len(gas)):
        #     all += gas[i%len(gas)]
        #     if all < 0:
        #         return -1
        # return idx



class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        plus=[]
        for i in range(len(gas)):
            plus.append(gas[i]-cost[i])
        plus+=plus
        sums=0
        start=0
        for idx,item in enumerate(plus):
            if sums+item<0:
                sums=0 
                start=idx+1
                if start>=len(gas):
                    return -1
            else:
                if idx-start>=len(gas)-1:
                    return start 
                sums+=item

# learn regrex
class Solution:
# @param {string} s
# @return {integer}
    def calculate(self, s):
        s = re.sub(r'\d+', ' \g<0> ', s)
        op = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv}
        expression = s.split()
        total = d = idx = 0
        func = op['+']
        while idx < len(expression):
            e = expression[idx]
            if e in '+-':
                total = func(total, d)
                func = op[e]
            elif e in '*/':
                idx += 1
                d = op[e](d, int(expression[idx]))
            else:
                d = int(e)
            idx += 1
        return func(total, d)
