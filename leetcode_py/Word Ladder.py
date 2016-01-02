class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        queue = [beginWord]
        count = 1
        while queue:
            next = []
            for word in queue:
                if word == endWord:
                    return count
                for idx in range(len(word)):
                    for j in range(ord('a'), ord('z') + 1, 1):
                        tmp = word[:idx] + chr(j) + word[idx + 1:]
                        if tmp == endWord:
                            return count + 1
                        if tmp in wordDict:
                            wordDict.remove(tmp)
                            next.append(tmp)  # set is better, remove duplicates
            queue = next
            count += 1
        return 0


if __name__ == "__main__":
    a = Solution()
    print a.ladderLength("hit", "cog", set(["hot", "cog", "dot", "dog", "hit", "lot", "log"]))
    print a.ladderLength("hot", "dog", set(["hot", "dog"]))
    print a.ladderLength("hit", "hit", set(["hot", "dot", "dog", "lot", "log"]))
    print a.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
    print a.ladderLength("hot", "dog", set(["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]))
    print ''


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        self.visited = set([beginWord])
        count = 0
        currents = [beginWord]
        wordDict.add(endWord)
        while currents:
            next = []
            for item in currents:
                if item == endWord:
                    return count + 1

                for idx in range(len(item)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = item[:idx] + j + item[idx + 1:]  # [idx]=j
                        if tmp not in self.visited and tmp in wordDict:
                            next.append(tmp)
                            self.visited.add(tmp)  # breadth first search with cut edge
                            #  print next
            count += 1
            currents = next
            #   print currents
        return 0


if __name__ == "__main__":
    a = Solution()
    print a.ladderLength("hit", "cog", set(["hot", "cog", "dot", "dog", "hit", "lot", "log"]))
    print a.ladderLength("hot", "dog", set(["hot", "dog"]))
    print a.ladderLength("hit", "hit", set(["hot", "dot", "dog", "lot", "log"]))
    print a.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
    print a.ladderLength("hot", "dog", set(["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]))

#
#
# # https://leetcode.com/discuss/16818/do-not-try-to-traverse-a-hash-set
# class Solution:
#     def ladderLength(self, start, end, dict):
#         distance, current, visited = 0, [start], set([start])
#         dict.add(end)
#         while current:
#             next = []
#             for word in current:
#                 if word == end:
#                     return distance + 1
#                 for i in range(len(word)):
#                     for j in 'abcdefghijklmnopqrstuvwxyz':
#                         candidate = word[:i] + j + word[i + 1:]
#                         if candidate not in visited and candidate in dict:
#                             next.append(candidate)
#                             visited.add(candidate)
#             distance += 1
#             current = next
#         return 0
# #
