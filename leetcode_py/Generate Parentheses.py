class Solution:
    def f(self,left,right,res,path):
        if left==right==0:
            res.append(path)

        if right<left or left<0 or right<0:
            return
        self.f(left,right-1,res,path+')')
        self.f(left-1,right,res,path+'(')
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res=[]
        self.f(n,n,res,'')
        return res


class Solution:
    def generateParenthesis(self,n):
        left,right=n,n
        return self.f(left,right)

    def f(self,left,right):
        if left<0 or right<0 or left>right:
            return []
        if left==0 and right==1:
            return [')']
        tmpres=[]
        tmp1=self.f(left-1,right)
        if len(tmp1)!=0:
            for i in tmp1:
                tmpres+=['('+i]

        tmp2=self.f(left,right-1)
        if len(tmp2)!=0:
            for i in tmp2:
                tmpres+=[')'+i]
        return tmpres

if __name__=="__main__":
    a=Solution()
    print a.generateParenthesis(4)
