class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        left, right = 0, len(citations)-1
        while left <= right:
            mid = left + (right-left)/2
            if citations[mid] < len(citations) - mid:
                left = mid + 1
            elif citations[mid] > len(citations) - mid:
                right = mid - 1
            else:
                return len(citations) - mid
        return len(citations) - (right + 1)
        # if right < 0:
        #     return len(citations)
        # if left > len(citations)-1:
        #     return 0
        # return len(citations)-left

if __name__ == "__main__":
    a = Solution()
    print a.hIndex([11, 15])
    print a.hIndex([1, 3, 3, 4])
    print a.hIndex([1,2,4,4,4,4])
    print a.hIndex([0, 0, 0, 4, 4])
    print a.hIndex([100])
    print a.hIndex([1,1,3])
    print a.hIndex([1, 2])
    print a.hIndex([0])
#TLE
# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         for i in range(len(citations), -1, 0):
#             if citations[i-1] < len(citations) - i + 1:
#                 return len(citations) - i
#         return len(citations)
