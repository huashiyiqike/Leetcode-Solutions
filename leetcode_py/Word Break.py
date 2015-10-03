class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        maps = [False]*(len(s)+1)
        maps[0] = True
        for idx, item in enumerate(s):
            for idy in range(idx+1, len(s)+1):
                if maps[idx] and s[idx:idy] in dict:
                    maps[idy] = True
        return maps[-1]
        
if __name__=="__main__":
        a=Solution()
        dict=['aba','abc','ab']
        dict=set(dict)
        print a.wordBreak('ababc',dict)
        dict=['a','b' ]
        dict=set(dict)
        print a.wordBreak('abc',dict)
