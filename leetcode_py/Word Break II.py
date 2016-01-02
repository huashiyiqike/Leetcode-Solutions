class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if not self.wordBreak1(s, dict):
            return []
        maps = [[] for i in range(len(s) + 1)]
        for idx, item in enumerate(s):
            for idy in range(idx + 1, len(s) + 1):
                if s[idx:idy] in dict:
                    if len(maps[idx]) > 0:
                        for i in maps[idx]:
                            maps[idy] += [i + " " + s[idx:idy]]
                    elif idx == 0:
                        maps[idy].append(s[:idy])
        return maps[-1]

    # just test which is faster for filtering out large negative case
    def wordBreak1(self, s, dict):
        maps = [0] * (len(s) + 1)
        maps[0] = 1
        for idx, item in enumerate(s):
            for idy in range(idx + 1, len(s) + 1):
                if maps[idx] == 1 and s[idx:idy] in dict:
                    maps[idy] = 1
        return maps[-1] == 1


#
# #
# # with backtracking time least
class Solution:
    def wordBreak(self, s, dict):
        if not s:
            return []
        in_dict = [[] for i in range(len(s) + 1)]
        in_dict[0].append(0)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if in_dict[j] and s[j: i] in dict:
                    in_dict[i].append(j)

                    # if no solution, backtracking stops
        res = []

        def backTracking(idx, cur_res):
            for n in in_dict[idx]:
                new_res = s[n:idx] + ' ' + cur_res if cur_res else s[n:idx]
                if n == 0:
                    res.append(new_res)
                else:
                    backTracking(n, new_res)

        backTracking(len(s), '')
        return res


if __name__ == "__main__":
    a = Solution()
    b = set([])
    # print a.wordBreak("a",b)
    print a.wordBreak("aaaa", set(['a', 'aa']))
    print a.wordBreak(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", \
        set(["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))


    # recursive slow TLE, can be improved with template
    # backward
    # class Solution:
    #     def wordBreak(self, s, dict):
    #         res=[]
    # #         if s in dict:
    # #             res.append(s)
    #         for i in range(0,len(s)):
    #             tmp=s[i:]
    #             if tmp in dict:
    #                 if i==0:
    #                     res.append(tmp)
    #                 else:
    #                     tmpres=self.wordBreak(s[0:i],dict)
    #                     if len(tmpres)>0:
    #                         for j in tmpres:
    #                             res.append(j+" "+tmp)
    #         return res
    #
    # forward
    # class Solution:
    #     def wordBreak(self, s, dict):
    #         res=[]
    #         if s in dict:
    #             res.append( s)
    #
    #         for i in range(0,len(s)):
    #             tmp=s[0:i]
    #             if tmp in dict:
    #                 if i==len(s):
    #                     res.append(tmp)
    #                 else:
    #                     ss=s[i:]
    #                     tmpres=self.wordBreak(ss,dict)
    #                     if len(tmpres)>0:
    #                         for j in tmpres:
    #                             res.append(tmp+" "+j)
    #
    #         return res
    #
    # #https://leetcode.com/discuss/12936/accepted-solution-backtracking-difference-front-tracking
    #
