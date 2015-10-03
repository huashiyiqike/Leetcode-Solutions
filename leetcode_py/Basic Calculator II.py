class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = s.strip()
        s = ''.join(s.split(' '))
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ('+', '-', '*', '/'):
                stack.append(s[i])
                i += 1
            else:
                idx = i
                while idx < len(s) and '0' <= s[idx] <= '9':
                    idx += 1
                num = int(s[i:idx])
                if stack:
                    n = stack[-1]
                    if n == '*':
                        stack.pop()
                        stack[-1] *= num
                    elif n == '/':
                        stack.pop()
                        stack[-1] /= num
                    else:
                        stack.append(num)
                else:
                    stack.append(num)
                i = idx
        stack = stack[::-1]
        res = stack.pop()
        while stack:
            op = stack.pop()
            num = stack.pop()
            if op == '+':
                res += num
            elif op == '-':
                res -= num
        return res


        # while len(stack) > 1:
        #     num = stack.pop()
        #     n = stack.pop()
        #     if n == '+':
        #         stack[-1] += num
        #     elif n == '-':
        #         stack[-1] -= num
        # return stack[0]

        # while len(stack) > 1:
        #     num = stack.pop(0)
        #     n = stack.pop(0)
        #     if n == '+':
        #         stack[0] += num
        #     elif n == '-':
        #         stack[0] -= num
        # return stack[0]
