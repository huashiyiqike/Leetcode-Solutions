class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in range(1, len(citations)+1):
            if citations[i-1] < i:
                return i - 1

        return len(citations)
