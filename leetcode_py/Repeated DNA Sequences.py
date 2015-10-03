class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        sets = set([])
        res = set([])
        for i in range(len(s)-9):
            tmp = s[i:(i+10)]
            if tmp in sets:
                res.add(tmp)
            else:
                sets.add(tmp)
        return list(res)


class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        dict2 = {value:key for key, value in dict.items()}
        has = set()
        res = set()
        num = 0
        for i in range(10):
            num <<= 2
            num += dict[s[i]]

        has.add(num)
        mask = 2**20 - 1
        for i in range(10, len(s)):
            num <<= 2
            num += dict[s[i]]
            num &= mask
            if num in has:
                res.add(num)
            has.add(num)
        mask = 2**2 - 1
        ans = []
        for i in res:
            tmpres = ''
            for j in range(10):
                tmpres = dict2[i&mask] + tmpres
                i >>= 2
            ans.append(tmpres)
        return ans
if __name__=="__main__":
    a=Solution()
    print  a.findRepeatedDnaSequences("TTTTTTTTTTT")
    print  a.findRepeatedDnaSequences("AAAAAAAAAAA")
    print a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

class Solution:
    def convert(self,s):
        maps={'A':1,'C':2,'G':3,'T':4}
        num=0
        for i in s:
            num+=maps[i]
            num<<=3
        num>>=3
        return num
 
    def findRepeatedDnaSequences(self, s):
        res=[]
        resmap=set([])
        repeatmap=set([])

        for i in range(len(s)):
            if s[i:(i+10)] in repeatmap:
                continue
            tmp=self.convert(s[i:(i+10)])
            if tmp in resmap:
                repeatmap.add(s[i:(i+10)])
                res.append(s[i:(i+10)])
            else:
                resmap.add(tmp)
        return res
                    
if __name__=="__main__":
    a=Solution()
    print  a.findRepeatedDnaSequences("TTTTTTTTTTT")
    print  a.findRepeatedDnaSequences("AAAAAAAAAAA")
    print a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")