class Solution:
    def isValid(self,s):
        if s=='0' or (s[0]!='0' and 0<int(s)<256):
            return True
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res=[]
        for i in range(1,4):
            for j in range(i+1,i+4):
                for k in range(j+1,j+4):
                    if k>=len(s):
                        break
                    else:
                        a,b,c,d=s[:i],s[i:j],s[j:k],s[k:]
                        if self.isValid(a) and self.isValid(b) and self.isValid(c)\
                            and self.isValid(d):

                            res.append("{0}.{1}.{2}.{3}".format(a,b,c,d))
        return res

class Solution:
    def f(self,s,res,path,seg,start):
        if seg==0 and start==len(s):
            res.append(path[1:])
        elif seg==0:
            return
        elif start==len(s):
            return
        for i in range(start,min(start+3,len(s))):
            char=s[start:i+1]
            if (char[0]!='0' and 0<int(char)<256) or char=='0':
                self.f(s,res,path+'.'+char,seg-1,i+1)

    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res=[]
        self.f(s,res,"",4,0)
        return res


class Solution:
    def check(self,s):
        if len(s)==0:
            return False
        #if s[0]=='0':
            #return False
        if int(s)<=255 and int(s)>=0:
            if int(s)!=0 and s[0]=='0':
                return False
            if int(s)==0 and len(s)>1:
                return False
            return True
    def f(self,s,id):
        if len(s)==0 or id + len(s)<5:
            return []
        res=[]
        if id==4:
            if self.check(s):
                return [s]
            else:
                return []
        else:
            for i in range(1,len(s)):
                if self.check(s[:i]):
                    tmp=self.f(s[i:],id+1)
                    if len(tmp)>0:
                        for j in tmp:
                            res.append(s[:i]+'.'+j)
            return res

    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
    		return self.f(s,1)
if __name__=="__main__":
    a=Solution()
    print  a.restoreIpAddresses("100050")
    print  a.restoreIpAddresses("12911112255")

