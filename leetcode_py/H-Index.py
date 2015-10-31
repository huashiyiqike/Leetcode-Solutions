class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        for i in range(1, len(citations) + 1):
            if citations[i - 1] < i:
                return i - 1

        return len(citations)


class Solution(object):
    def hIndex(self, citations):
        ref = [0] * (len(citations) + 1)
        for i in citations:
            if i > len(citations):
                ref[-1] += 1
            else:
                ref[i] += 1
        total = 0
        for i in range(len(citations), -1, -1):
            total += ref[i]
            if total >= i:
                return i
        return 0