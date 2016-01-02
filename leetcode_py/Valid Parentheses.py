class Solution:
    # @return a boolean
    def isValid(self, s):
        stacks = []
        for i in s:
            if i in set(['(', '[', '{']):
                stacks.append(i)
            else:
                if len(stacks) == 0:
                    return False
                temp = stacks.pop()
                if (temp == '(' and i != ')') or (temp == '[' and i != ']') or (temp == '{' and i != '}'):
                    return False
        return len(stacks) == 0
