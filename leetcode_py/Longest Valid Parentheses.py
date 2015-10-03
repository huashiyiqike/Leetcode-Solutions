# https://leetcode.com/discuss/9156/my-solution-using-one-stack-in-one-pass
class node:
    def __init__(self, idx, item):
        self.idx = idx
        self.item = item

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        left = 0
        maxlen = 0
        for idx, item in enumerate(s):
            if item == '(':
                stack.append(idx)
            else:
                if len(stack) == 0:
                    left = idx + 1
                else:
                    stack.pop()
                    if len(stack) == 0:
                        maxlen = max(maxlen, idx - left + 1)
                    else:
                        maxlen = max(maxlen, idx - stack[-1])

        return maxlen

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        maxs = 0
        for idx, item in enumerate(s):
            if item == '(':
                stack.append(item)
            else:
                if not stack:
                    continue
                elif stack[-1] != '(':
                    if len(stack) >= 2 and stack[-2] == '(':
                        tmp = stack[-1] + 2
                        stack.pop()
                        stack.pop()
                        stack.append(tmp)
                        if len(stack) >= 2 and stack[-2] != '(':
                            stack[-2] += stack[-1]  # stack.pop()
                            stack.pop()
                        maxs = max(stack[-1], maxs)
                    else:
                        stack.pop()
                else:
                    stack.pop()
                    if not stack or stack[-1] == '(':
                        stack.append(2)
                        maxs = max(2, maxs)
                    else:
                        stack[-1] += 2
                        maxs = max(stack[-1], maxs)

        return maxs




if __name__ == "__main__":
    a = Solution()
    print a.longestValidParentheses("(()()")
    print a.longestValidParentheses("()")
    print a.longestValidParentheses(")()())()()(")
    print a.longestValidParentheses("()()")
    print a.longestValidParentheses("(()(((()")

    print a.longestValidParentheses("()(()")
    print a.longestValidParentheses("((((()))(")

    print a.longestValidParentheses("()(())()")
    print a.longestValidParentheses("()(()))()")


class Solution:
    def longestValidParentheses(self, s):
        stack = []
        res = 0
        tmpres = 0

        for idx, item in enumerate(s):
            if item == '(':
                if len(stack) == 1 and stack[-1] == ')':
                    stack.pop()
                    stack.append(item)
                else:
                    stack.append(item)
            else:
                if len(stack) == 0:
                    stack.append(item)
                    tmpres = 0
                elif len(stack) == 1:
                    if stack[-1] == ')':
                        continue
                    elif stack[-1] == '(':
                        stack.pop()
                        stack.append(2)
                        res = max(res, 2)
                    else:
                        stack.pop()
                        #   stack.append(2)
                else:
                    if len(stack) > 0:
                        if stack[-1] != '(':
                            tmp = stack.pop()
                            stack.pop()
                            tmpres = tmp + 2
                        else:
                            stack.pop()
                            tmpres += 2
                    while len(stack) > 0 and stack[-1] != '(':
                        tmp = stack.pop()
                        tmpres += tmp

                    stack.append(tmpres)
                    res = max(res, tmpres)
                    tmpres = 0

        return res
