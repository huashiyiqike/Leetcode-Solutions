from collections import OrderedDict, defaultdict
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        sets = OrderedDict()
        dict = defaultdict(int)
        for i in words:
            dict[i] += 1
        width = len(words[0])
        start = 0
        res = []
        for i in range(width, len(s)+1, width):
           # print i, sets
            tmp = s[i-width:i]
            if tmp in words:
                if tmp in sets:
                    if sets[tmp][1] > dict[tmp]:
                        sets[tmp] = (i, sets[tmp][1]+1)
                        last = sets.popitem(last=False)
                        while last[0] != tmp:
                            last = sets.popitem(last=False)
                        start = last[1][0]

                else:
                    sets[tmp] = (i, 1)

                if len(sets) == len(words):
                    res.append(start)
                    sets.popitem(last=False)
            else:
                start = i
                sets = OrderedDict()
        return res

if __name__=="__main__":
    a=Solution()
    # print a.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    print a.findSubstring("barfoothefoobarman", ["foo", "bar","the"])
    print a.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print a.findSubstring("cab", ["a","b"])
    print a.findSubstring("aa", ["a","a"])
    print a.findSubstring("fooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    print ''

from copy import deepcopy
from collections import defaultdict
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        dicts=defaultdict(int)
        for i in words: dicts[i]+=1
        lens=len(words[0])
        i,j,res=0,0,[]
        for i in range(lens):  # mod len(words[0])
            dic=deepcopy(dicts)
            j=i
            while j+lens<=len(s):
                word=s[j:(j+lens)]
                dic[word]-=1
                while dic[word]<0:      #if repeated more than wanted
                    dic[s[i:(i+lens)]]+=1
                    i+=lens

                j+=lens
                if j-i==lens*len(words):
                    res.append(i)
        return res

from collections import defaultdict
class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        dicts=defaultdict(int)
        for i in words:
            dicts[i]+=1
        lens=len(words[0])
        res=[]

        for idx in range(len(s)-lens*len(words)+1): # THIS IS CRUCIAL
            tmpdicts=defaultdict(int)
            tmpidx=idx
            while tmpidx+lens<=len(s):
                word=s[tmpidx:(tmpidx+lens)]
                if word in dicts:
                    tmpdicts[word]+=1
                    if tmpdicts[word]>dicts[word]:
                        break
                else:
                    break
                tmpidx+=lens

            if (tmpidx-idx)/lens==len(words):
                res.append(idx)

            idx+=lens
        return res
        
if __name__=="__main__":
    a=Solution()
   # print a.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    print a.findSubstring("barfoothefoobarman", ["foo", "bar","the"])
    print a.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print a.findSubstring("cab", ["a","b"])
    print a.findSubstring("aa", ["a","a"])
    print a.findSubstring("fooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    print ''