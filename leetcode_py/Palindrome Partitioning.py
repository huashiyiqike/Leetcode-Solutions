class Solution:
    def partition(self, s):
        result = []
        self.partitionRecur(result, [], s, 0)
        return result

    def partitionRecur(self, result, current, s, i):
        if i == len(s):
            result.append(current)
        else:
            for j in range(i, len(s)):
                if self.isPalindrome(s[i: j + 1]):
                    self.partitionRecur(result, current + [s[i: j + 1]], s, j + 1)

    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True

class Solution:
    def ispal(self,str):
        return str==str[::-1]
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s)==0:
            return [[]]
        if len(s)==1:
            return [[s]]
        res=[]
        for idx in range(0,len(s)):
            head=s[:idx+1]
            # print head
            if self.ispal(head):
                tmpres=self.partition(s[idx+1:])
                for i in tmpres:
                    tmp=[head]
                    tmp.extend(i)
                    res.append(tmp)

        return res


class Solution:
    def ispal(self,str):
        return str==str[::-1]
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s)==0:
            return []
        if len(s)==1:
            return [[s]]
        res=[]
        for idx in range(0,len(s)):
            head=s[:idx+1]
            # print head
            if self.ispal(head):
                tmpres=self.partition(s[idx+1:])
                if len(tmpres)>0:
                    for i in tmpres:
                        res.append([head]+i)
                else:
                    res.append([head])

        return res

if __name__=="__main__":
    a=Solution()
    print a.partition('abcba')
    print a.partition('aaa')