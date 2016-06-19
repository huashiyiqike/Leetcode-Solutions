class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map = {}
        for idx, item in enumerate(num, start=1):
            if item not in map:
                map[target - item] = idx
            else:
                return [map[item], idx]
