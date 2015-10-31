from heapq import *

class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings:
            return []
        heap = []
        res = []
        i = 0
        while i < len(buildings):
            while heap and heap[0][1] <= buildings[i][0]:
                tmp = heappop(heap)
                if -tmp[0] == buildings[i][2]:
                    heappush(heap, tmp)
                    break
                while heap and heap[0][1] < tmp[1]:
                    heappop(heap)
                if heap and res[-1][0] != -heap[0][0]:
                    if res and res[-1][0] == tmp[1]:
                        res[-1][1] = min(res[-1][1], -heap[0][0])
                    else:
                        res.append([tmp[1], -heap[0][0]])
                elif not heap:
                    if res and res[-1][0] == tmp[1]:
                        res[-1][1] = min(res[-1][1], 0)
                    else:
                        res.append([tmp[1], 0])

            if heap and buildings[i][2] == -heap[0][0]:
                heap[0][1] = max(heap[0][1], buildings[i][1])
            else:
                if not heap or buildings[i][2] > -heap[0][0]:
                    if res and res[-1][0] == buildings[i][0]:
                        res[-1][1] = max(res[-1][1], buildings[i][2])
                    else:
                        res.append([buildings[i][0], buildings[i][2]])

            heappush(heap, [-buildings[i][2], buildings[i][1]])

            i += 1

        while heap:
            tmp = heappop(heap)
            while heap and heap[0][1] < tmp[1]:
                heappop(heap)
            if heap and res[-1][0] != -heap[0][0]:
                if res and res[-1][0] == tmp[1]:
                    res[-1][1] = min(res[-1][1], -heap[0][0])
                else:
                    res.append([tmp[1], -heap[0][0]])
            elif not heap:
                if res and res[-1][0] == tmp[1]:
                    res[-1][1] = min(res[-1][1], 0)
                else:
                    res.append([tmp[1], 0])

        return res


if __name__ == "__main__":
    a = Solution()
    print a.getSkyline([[0, 2, 3], [2, 5, 3]])
    print a.getSkyline([[2, 13, 10], [10, 17, 25], [12, 20, 14]])
    print a.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
    print a.getSkyline([[1, 2, 1], [2147483646, 2147483647, 2147483647]])
    print a.getSkyline(
        [[2, 4, 70], [3, 8, 30], [6, 100, 41], [7, 15, 70], [10, 30, 102], [15, 25, 76], [60, 80, 91], [70, 90, 72],
         [85, 120, 59]])


class Solution:
    def merge(self, left, right):
        res = []
        i = j = 0
        h1 = h2 = None
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                h1 = left[i][1]
                new = [left[i][0], max(h1, h2)]
                if not res or res[-1][1] != new[1]:
                    res.append(new)
                i += 1
            elif right[j][0] > left[i][0]:
                h2 = right[j][1]
                new = [right[j][0], max(h1, h2)]
                if not res or res[-1][1] != new[1]:
                    res.append(new)
                j += 1
            else:
                h1 = left[i][1]
                h2 = right[j][1]
                new = [left[i][0], max(h1, h2)]
                if not res or res[-1][1] != new[1]:
                    res.append(new)
                i += 1
                j += 1
        while i < len(left):
            # new = [left[i][0], max(h1, h2)]
            if not res or res[-1][1] != left[i][1]:
                res.append(new)
            i += 1
        while j < len(right):
            # new = [right[j][0], max(h1, h2)]
            if not res or res[-1][1] != right[j][1]:  # new[1]:
                res.append(new)
            j += 1
        return res

    def getSkyline(self, LRH):
        if not LRH:
            return []
        elif len(LRH) == 1:
            return [[LRH[0][0], LRH[0][2]], [LRH[0][1], 0]]
        left = self.getSkyline(LRH[:len(LRH) / 2])
        right = self.getSkyline(LRH[len(LRH) / 2:])
        return self.merge(left, right)


#
#
# class Solution:
#     def getSkyline(self, LRH):
#         # changes when push and pop
#         res = []
#         heap = []
#         i = 0
#         while i < len(LRH):
#             if not heap or i < len(LRH) and LRH[i][0] <= - heap[0][1]:
#                 x = LRH[i][0]
#                 while i < len(LRH) and x == LRH[i][0]:
#                     heappush(heap, (-LRH[i][2], -LRH[i][1]))
#                     i += 1
#             else:
#                 x = -heap[0][1]
#                 while heap and x >= -heap[0][1]:
#                     heappop(heap)
#                 height = len(heap) and -heap[0][0]
#                 if not res or height != res[-1][1]:
#                     res.append([x, height])
#         return  res
#

#
#
# class Solution:
#     def getSkyline(self, LRH):
#         res = []
#         i = 0
#         liveHR = [] # queue
#         while i < len(LRH) or liveHR:
#             if not liveHR or LRH[i][0] <= -liveHR[0][1]:
#                 x = LRH[i][0]
#                 while i < n and LRH[i][0] == x:
#                     heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
#                     i += 1
#             else:
#                 x = -liveHR[0][1]
#                 while liveHR and -liveHR[0][1] <= x:
#                     heappop(liveHR)

class Solution:
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            # print liveHR
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline


if __name__ == "__main__":
    a = Solution()
    print a.getSkyline([[2, 13, 10], [10, 17, 25], [12, 20, 14]])
    print a.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
    print a.getSkyline([[1, 2, 1], [2147483646, 2147483647, 2147483647]])
    print a.getSkyline(
        [[2, 4, 70], [3, 8, 30], [6, 100, 41], [7, 15, 70], [10, 30, 102], [15, 25, 76], [60, 80, 91], [70, 90, 72],
         [85, 120, 59]])

    #
    # if __name__ == '__main__':
    #     a = Solution()
    #     print a.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15, 20, 10], [19, 24, 8] ])
