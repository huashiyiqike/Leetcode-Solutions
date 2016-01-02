# Source : https://leetcode.com/problems/different-ways-to-add-parentheses/

# Given a string of numbers and operators, return all possible results
#  from computing all the different possible ways to group numbers and operators.
#  The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]
#

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for idx, item in enumerate(input):
            if item in '-+*':
                left = input[:idx]
                right = input[idx + 1:]
                leftres = self.diffWaysToCompute(left)
                rightres = self.diffWaysToCompute(right)
                for l in leftres:
                    for r in rightres:
                        if item == '-':
                            res.append(l - r)
                        elif item == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)
        if not res:
            res.append(int(input))
        return res


class Solution(object):
    dict = {}

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for idx, item in enumerate(input):
            if item in '-+*':
                left = input[:idx]
                right = input[idx + 1:]
                if left in self.dict:
                    leftres = self.dict[left]
                else:
                    leftres = self.diffWaysToCompute(left)
                if right in self.dict:
                    rightres = self.dict[right]
                else:
                    rightres = self.diffWaysToCompute(right)
                for l in leftres:
                    for r in rightres:
                        if item == '-':
                            res.append(l - r)
                        elif item == '+':
                            res.append(l + r)
                        else:
                            res.append(l * r)
        if not res:
            res.append(int(input))
        return res
