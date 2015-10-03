class Solution:
    # @return an integer
    def myAtoi(self, str):
        if len(str)==0:
            return 0
        res=0
        sign=1
        str=str.strip(' ')
            
        if str[0]=='-':
            sign=-1
            str=str[1:]
        elif str[0]=='+':
            str=str[1:]
        while len(str)>0 and str[0]=='0':
            str=str[1:]
            
        for i in str:
            if '0'<=i<='9':
                res*=10
                res+=int(i)
                # if res>21474836480:
                #     break
            else:
                break

        if sign==1 and res>2147483647:
            res=2147483647
        if res>2147483648:
            res=2147483648

        return sign*res
        
        
if __name__=="__main__":
    a=Solution()
    print a.myAtoi("  010")
    print a.myAtoi("-2147483649")
