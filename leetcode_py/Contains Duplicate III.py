class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        idxsorted = sorted(range(len(nums)), key=lambda i: nums[i])
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums) and nums[idxsorted[j]] - nums[idxsorted[i]] <= t:
                if abs(idxsorted[i] - idxsorted[j]) <= k:  # iterate idxsorted we get sorted nums
                    return True
                j += 1
        return False


from collections import OrderedDict
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False

        dict = OrderedDict()
        for i in nums:
            key = i / t if t else i
            for j in (dict.get(key - 1), dict.get(key), dict.get(key + 1)):
                if j is not None and abs(i - j) <= t:  # j can be 0, so not use if j
                    return True
            if len(dict) == k:
                dict.popitem(False)
            dict[key] = i

        return False


if __name__ == "__main__":
    a = Solution()
    print a.containsNearbyAlmostDuplicate([-1, -1], 1, 0)
    print a.containsNearbyAlmostDuplicate([2, 0, -2, 2], 2, 1)
    print a.containsNearbyAlmostDuplicate([1, 2, 1], 1, 1)
    print a.containsNearbyAlmostDuplicate([-3, 3], 2, 4)
    print a.containsNearbyAlmostDuplicate([3, 6, 0, 2], 2, 2)
    print ''
