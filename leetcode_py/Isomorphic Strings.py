class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dicts = {}
        sets = set([])
        for idx, item in enumerate(s):
            if item in dicts:
                if dicts[item] != t[idx]:
                    return False
            else:
                if t[idx] in sets:
                    return False
                dicts[item] = t[idx]
                sets.add(t[idx])
        return True



class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dicts={}
        to=set([])
        for idx in range(len(s)):
            if s[idx] in dicts:
                if dicts[s[idx]] != t[idx]:
                    return False
            else:
                if t[idx] not in to:
                    dicts[s[idx]]=t[idx]
                    to.add(t[idx])
                else:
                    return False
        return True
    
if __name__=="__main__":
    a=Solution()
    print a.isIsomorphic("ab", "aa")
    print a.isIsomorphic("ac", "ba")