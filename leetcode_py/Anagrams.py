from collections import defaultdict
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict=defaultdict(list)
        map(lambda s:dict[''.join(sorted(s))].append(s),strs)
        return [y for x in dict.keys() for y in dict[x] if len(dict[x])>1 ]



# from collections import defaultdict
# class Solution:
#     def anagrams(self, strs):
#         dicts=defaultdict(int)
#         map(lambda x:dicts[''.join(sorted(list(x)))]+1,strs)
#         print dicts
#         return filter(lambda x: dicts[''.join(sorted(list(x)))]>1,strs)


# class Solution:
#     def anagram(self, s, t):
#         # write your code here
#         s=''.join(sorted(list(s)))
#         t=''.join(sorted(list(t)))
#
#         return s==t
#     def anagrams(self, strs):
#         anagram_map, res = {}, []
#         for str in strs:
#             sorted_str = ''.join(sorted(str)) #list2str
#             if sorted_str in anagram_map:
#                 anagram_map[sorted_str].append(str)
#             else:
#                 anagram_map[sorted_str] = [str]
#         for anagrams in anagram_map.values():
#             if len(anagrams) > 1:
#                 res += anagrams
#         return res

    
if __name__=="__main__":
    a=Solution()
   # print a.anagram("django", "naogdj")
    print a.anagrams(["django", "naogdj"])
    print a.anagrams(['a','a','a'])
    print a.anagrams(['a','abc','cba','ba','ab','a','',''])
    print a.anagrams(["",""])
    
    
#    https://leetcode.com/discuss/18664/sharing-my-very-concise-solution-with-explanation
