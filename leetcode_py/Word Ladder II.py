from collections import defaultdict


class Solution:
    def bp(self, res, path, bpdict, start, end):
        if start == end:
            res.append(path[::-1])
            return
        for i in bpdict[start]:
            self.bp(res, path + [i], bpdict, i, end)

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        bpdict = defaultdict(list)
        dict.add(end)
        dict.add(start)
        queue = set([start])
        res = []
        while queue:
            next = set()
            for word in queue:
                dict.remove(word)
                if word == end:
                    self.bp(res, [end], bpdict, end, start)
                    return res

            for word in queue:
                for i in range(len(word)):
                    for c in range(ord('a'), ord('z') + 1, 1):
                        tmp = word[:i] + chr(c) + word[i + 1:]
                        if tmp in dict:
                            # dict.remove(tmp)
                            next.add(tmp)  # set is better, remove duplicates
                            bpdict[tmp] += [word]
            queue = next
        return []


if __name__ == "__main__":
    a = Solution()
    print a.findLadders("hot", "dog", set(["hot", "dog"]))
    print a.findLadders("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))


class Solution:
    def backtrack(self, trace, dict, start, end):
        tmpres = [[end]]
        res = []
        while tmpres:
            next = []
            for idx, item in enumerate(tmpres):
                for i in trace[tmpres[idx][0]]:
                    if i == start:
                        res.append([i] + tmpres[idx])
                    else:
                        # tmpres[idx].insert(0,i)
                        next.append([i] + tmpres[idx])
            tmpres = next
        return res

    def findLadders(self, start, end, dict):
        count = 0
        currents = [start]
        dict.add(start)
        dict.add(end)
        trace = {i: [] for i in dict}
        while currents:
            for i in currents:
                if i == end:
                    # print trace
                    return self.backtrack(trace, dict, start, end)
                dict.remove(i)

            next = set([])
            for item in currents:
                for idx in range(len(item)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        tmp = item[:idx] + j + item[(idx + 1):]  # [idx]=j
                        if tmp in dict:
                            next.add(tmp)
                            trace[tmp].append(item)

            count += 1
            currents = next
            #   print currents
        return []

# class Solution:
#     # @param start, a string
#     # @param end, a string
#     # @param dict, a set of string
#     # @return a list of lists of string
#     def findLadders(self, start, end, dict):
#         visited=set([start])
#         current=[[start]]
#         dis=0
#         maxdis=1<<64
#         res=[]
#         dict.add(end)
#         while current:
#             next=[]
#             tmpvisited=[]
#             for i in current:
#                 if i[-1] == end:
#                     res.append(i)
#                     maxdis=dis
#                 if dis<=maxdis:
#                      
#                     for idx in range(len(start)):
#                         for chars in 'abcdefghijklmnopqrstuvwxyz':
#                             tmp=i[-1][:idx]+chars+i[-1][(idx+1):]
#                             if tmp not in visited and tmp in dict:
#                                 tmpvisited.append(tmp)
#                                 next.append(i+[tmp])
#                                 #print next
#             for i in tmpvisited:
#                 visited.add(i)
#                              
#             current=next
#             dis+=1
#         return res
if __name__ == "__main__":
    a = Solution()
    print a.findLadders("hot", "dog", set(["hot", "dog"]))
    print a.findLadders("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))


#     

# print a.findLadders("hit", "cog", set(["hot","cog","dot","dog","hit","lot","log"]))
#     print a.findLadders("hot", "dog", set(["hot","dog"]))
#     print a.findLadders("hit", "hit", set(["hot","dot","dog","lot","log"])  )  
#    
#    print a.findLadders("hot", "dog", set(["hot","cog","dog","tot","hog","hop","pot","dot"])  )
