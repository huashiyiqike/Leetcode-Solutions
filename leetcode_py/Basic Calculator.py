class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = s.strip()
        stack = []
        i = 0
        while i < len(s):
            if s[i] in '+-(':  # ('+', '-', '('):
                stack.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
                continue
            elif s[i] == ')':  # should not calculate here, because reverse
                num = stack.pop()
                stack.pop()  # '('
                stack.append(num)
                i += 1
            else:
                tmp = ''
                while i < len(s) and '0' <= s[i] <= '9':
                    tmp += s[i]
                    i += 1
                num = int(tmp)
                stack.append(num)
            while len(stack) >= 3 and stack[-2] in ('+', '-') and stack[-1] != '(':
                num2 = stack.pop()
                op = stack.pop()
                if op == '+':
                    stack[-1] += num2
                elif op == '-':
                    stack[-1] -= num2
        return stack[-1]


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = ''.join(s.strip().split(' '))
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ('+', '-', '('):
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                num = stack.pop()
                stack.pop()
                stack.append(num)

                i += 1
            else:
                j = i + 1
                while j < len(s) and '0' <= s[j] <= '9':
                    j += 1
                num = int(s[i:j])
                stack.append(num)
                i = j

            while len(stack) >= 3 and stack[-2] in ('+', '-') and stack[-1] not in ('+', '-', '('):
                num = stack.pop()
                if stack[-1] == '+':
                    stack.pop()
                    stack[-1] += num
                elif stack[-1] == '-':
                    stack.pop()
                    stack[-1] -= num

        return stack[-1]
