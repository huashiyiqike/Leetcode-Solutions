class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        dicts={}
        start=res=0
        for i in range(len(s)):
            if s[i] in dicts: # and dic[item]>=start:  is better
                newstart=dicts[s[i]]+1
                dicts[s[i]]=i
                for j in range(start,newstart-1):
                    dicts.pop(s[j])

                start=newstart
            else:
                dicts[s[i]]=i
                res=max(res,i-start+1)
        return res

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start=0
        res=0
        dic={}

        for idx, item in enumerate(s):
            if item in dic and dic[item]>=start:
                start=dic[item]+1
            dic[item]=idx
            res=max(res,idx-start+1)
        return res


if __name__=="__main__":
    a=Solution()
    print a.lengthOfLongestSubstring('abcabcaa')
    print a.lengthOfLongestSubstring("tmmzuxt")
    print a.lengthOfLongestSubstring("ruowzgiooobpple")
    print a.lengthOfLongestSubstring("aab")