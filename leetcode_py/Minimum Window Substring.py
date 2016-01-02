from collections import defaultdict


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        dict = defaultdict(int)
        for i in t:
            dict[i] += 1
        left = right = 0
        has = defaultdict(int)
        minlen = 1 << 63
        res = ""
        count = 0
        while right < len(s):
            while right < len(s) and count < len(t):
                if s[right] in t:
                    has[s[right]] += 1
                    if has[s[right]] <= dict[s[right]]:
                        count += 1
                right += 1

            while count == len(t) and left <= right:
                if s[left] in t:
                    has[s[left]] -= 1
                    if has[s[left]] < dict[s[left]]:
                        count -= 1
                        if count == len(t) - 1 and right - left < minlen:
                            res = s[left:right]
                            minlen = right - left
                left += 1
        return res


if __name__ == "__main__":
    a = Solution()
    print a.minWindow("a", "aa")

from collections import defaultdict
from collections import OrderedDict
# using queue
class Solution:
    def minWindow(self, s, t):
        dicts = defaultdict(int)
        have_dic = defaultdict(int)
        for i in t:
            dicts[i] += 1
        count = 0
        res = ''
        queue = []
        for i in s:
            queue.append(i)
            if i in dicts:
                have_dic[i] += 1
                if have_dic[i] <= dicts[i]:
                    count += 1
                if count == len(t):
                    count -= 1
                    while queue:
                        if queue[0] in dicts:
                            if have_dic[queue[0]] == dicts[queue[0]]:
                                break
                            else:
                                have_dic[queue[0]] -= 1
                        queue.pop(0)

                    if res == '' or len(res) > len(queue):
                        res = ''.join(queue)
                    have_dic[queue[0]] -= 1
                    queue.pop(0)
        return res


class Solution:
    def minWindow(self, s, t):
        dicts = defaultdict(int)
        have_dic = defaultdict(int)
        for i in t:
            dicts[i] += 1
        count = start = 0
        res = ''

        for idx, i in enumerate(s):
            #  print dicts, have_dic
            if i in dicts:
                have_dic[i] += 1
                if have_dic[i] <= dicts[i]:
                    count += 1

                    if count == len(t):
                        count -= 1
                        while start <= idx:
                            c = s[start]
                            if c in dicts:
                                if have_dic[c] == dicts[c]:
                                    break
                                else:
                                    have_dic[c] -= 1
                            start += 1

                        if res == '' or len(res) > idx - start + 1:
                            res = s[start:idx + 1]
                        have_dic[s[start]] -= 1
                        start += 1
        return res


class Solution:
    def minWindow(self, s, t):
        if len(t) == 0:
            return s

        tmap = defaultdict(int)
        count = len(t)
        for idx, i in enumerate(t):
            tmap[i] += 1

        left = 0
        smap = defaultdict(int)
        minlen = 1 << 64
        res = ""
        for right in range(len(s)):
            #   print res,smap
            char = s[right]
            if char in tmap:
                smap[char] += 1
                if smap[char] <= tmap[char]:
                    count -= 1

            while left < right and count == 0:
                char = s[left]
                if char in tmap:
                    if smap[char] <= tmap[char]:
                        break
                    else:
                        smap[char] -= 1
                left += 1

            if count == 0 and right - left < minlen:
                res = s[left:right + 1]
                minlen = right - left

            while count == 0 and left < right:
                char = s[left]
                if char in tmap:
                    if smap[char] == tmap[char]:
                        count += 1
                        smap[char] -= 1
                    elif smap[char] < tmap[char]:
                        break
                    else:
                        smap[char] -= 1
                left += 1

        return res

#
# from collections import defaultdict
# class Solution:
#     def minWindow(self, s, t):
#         if len(t)==0:
#             return s
#
#         tmap=defaultdict(int)
#         count=0
#         for idx,i in enumerate(t):
#             tmap[i]+=1
#             count+=1
#
#         left=right=0
#         smap=defaultdict(int)
#         minlen=1<<64
#         res=""
#         while right<len(s):
#             if s[right] in tmap:
#                 if tmap[s[right]]>smap[s[right]]:
#                     count-=1
#                 smap[s[right]]+=1
#                 right+=1
#
#             while count>0 and right<len(s):
#                 if s[right] in tmap:
#                     if tmap[s[right]]>smap[s[right]]:
#                         count-=1
#                     smap[s[right]]+=1
#                 right+=1
#
#             while left<right-1:
#                 if s[left] not in tmap:
#                     left+=1
#                 elif tmap[s[left]] <smap[s[left]]:
#                     smap[s[left]]-=1
#                     left+=1
#                 else:
#                     break
#
#             if count==0 and right-left<minlen:
#                 minlen=right-left
#                 res=s[left:right]
#
#             if tmap[s[left]] == smap[s[left]]:
#                 smap[s[left]]-=1
#                 left+=1
#                 count+=1
#
#         return res
#
# from collections import defaultdict
# from copy import deepcopy
# class Solution:
#     # @param {string} s
#     # @param {string} t
#     # @return {string}
#     def minWindow(self, s, t):
#         base=defaultdict(int)
#         for i in t: base[i]+=1
#         res=""
#         i,j=0,0
#         count,minlen=0,1<<64
#         dic=defaultdict(int)
#         while i<len(s):
#             while j<len(s):
#                 if s[j] in base:
#                     dic[s[j]]+=1
#                     if dic[s[j]]<=base[s[j]]:
#                         count+=1
#                 if count==len(t):
#                     while i<j:
#                         if s[i] in dic:
#                             if dic[s[i]]<=base[s[i]]:
#                                 break
#                             else:
#                                 dic[s[i]]-=1
#                         i+=1
#
#                     if res=="" or j-i<len(res):
#                    #     print 1,s[i:(j+1)]
#                         res=s[i:(j+1)]
#                     j+=1
#                     break
#
#                 j+=1
#
#             if s[i] in dic:
#                 if dic[s[i]]<=base[s[i]]:
#                     count-=1
#                 dic[s[i]]-=1
#             i+=1
#
#         return res

if __name__ == "__main__":
    a = Solution()
    print a.minWindow("acbbaca", "aba")
    print a.minWindow("cabefgecdaecf", "cae")
    print a.minWindow("abccbc", "ac")

    print a.minWindow("aacaca", "cc")
    print a.minWindow("aacaca", "aaacc")

    print a.minWindow("abc", "ab")
    print a.minWindow("abc", "abc")
    print a.minWindow("abc", "ba")
    print a.minWindow("abc", "d")
    print a.minWindow("abcabc", "ac")







    # maps={}
    # lists=[]
    # count=len(t)
    # minlen=1<<64
    # base=defaultdict(int)
    #
    # for i in t:
    #     maps[i]=0
    #     base[i]+=1
    #
    # for idx,item in enumerate(s):
    #     if item in maps:
    #         if maps[item]==0 or maps[item]<base[item]:
    #             maps[item]+=1
    #             lists.append(idx)
    #             count-=1
    #         else:
    #             maps[item]=base[item]
    #             if item==s[lists[0]]:
    #                 lists.pop(0)
    #                 lists.append(idx)
    #         if count==0:
    #             minlen=min(minlen,lists[-1]-lists[0]+1)
    # if minlen!=1<<64:
    #     return  s[lists[0]:(lists[-1]+1)]
    # else:
    #     return ""
