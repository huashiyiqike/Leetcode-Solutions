class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip()
        idx = len(s) - 1
        while 0 <= idx < len(s) and s[idx] != ' ':
            idx -= 1

        return len(s) - idx - 1

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        tmp=s.split(" ")
        tmp=filter(lambda x:x!='',tmp) 
        #print tmp
        if len(tmp)>0:
            return len(tmp[-1])
        else:
            return 0


if __name__=="__main__":
    a=Solution()
    print a.lengthOfLastWord("a b c  ")
    

