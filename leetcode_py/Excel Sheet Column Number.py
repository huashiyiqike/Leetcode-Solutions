class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res=ord(s[0])-ord('A')+1
        for i in range(1,len(s)):
            res*=26
            res+=ord(s[i])-ord('A')+1
        return res

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num=0
        for index,i in enumerate(s):
            num+=26**(len(s)-index-1)*(ord(i)-ord('A')+1)
        return num