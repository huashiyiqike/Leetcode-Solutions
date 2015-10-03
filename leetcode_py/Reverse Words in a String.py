class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(filter(lambda a: len(a) > 0, s.strip().split(' '))[::-1])


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        pre = 0
        stack = []
        for idx, i in enumerate(s):
            if i == ' ':
                if pre < idx:
                    stack.append(s[pre:idx])
                    pre = idx + 1
                else:
                    pre += 1
            elif idx == len(s) - 1:
                stack.append(s[pre:idx + 1])
        str = ''
        for i in reversed(stack):
            if i != ' ':
                str += i + ' '
        str = str[:-1]
        return str

class Solution:
    def reverseWords2(self, s):
        return " ".join(filter(lambda x: x, reversed(s.split(" "))))
