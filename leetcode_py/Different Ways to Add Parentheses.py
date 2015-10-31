class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        dict = {}
        res = []
        for idx, item in enumerate(input):
            if item in '-+*':
                left = input[:idx]
                right = input[idx+1:]
                if left in dict:
                    leftres = dict[left]
                else:
                    leftres = self.diffWaysToCompute(left)
                if right in dict:
                    rightres = dict[right]
                else:
                    rightres = self.diffWaysToCompute(right)
                for l in leftres:
                    for r in rightres:
                        if item == '-':
                            res.append(l-r)
                        elif item == '+':
                            res.append(l+r)
                        else:
                            res.append(l*r)
        if not res:
            res.append(int(input))
        return res
