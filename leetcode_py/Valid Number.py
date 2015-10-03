class Solution:
    def checknum(self,s):
        if s == '.' or not s:
            return False
        s = s.split('.')
        if len(s) == 1:
            return self.checkdigit(s[0])
        elif len(s) > 2:
            return False
        else:
            return self.checkdigit(s[0]) and self.checkdigit(s[1])

    def checkdigit(self, s):
        for i in s:
            if i > '9' or i < '0':
                return False
        return True
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False
        if s and s[0] in ('+', '-'):
            s = s[1:]

        s2 = s.split('e')
        if len(s2) > 2:
            return False
        elif len(s2) == 1:
            return self.checknum(s2[0])
        else:
            if s2[1] and s2[1][0] in ('+', '-'):
                s2[1] = s2[1][1:]
            if not s2[1]:
                return False
            return self.checknum(s2[0]) and self.checkdigit(s2[1])

if __name__=="__main__":
    a=Solution()
    print a.isNumber( " 4e3."),'f'
    print a.isNumber("1e."),'f'
    print a.isNumber('1e2.'),'f'
    print a.isNumber('1e2.1'),'f'
    print a.isNumber("46.e3"),'t'
    print a.isNumber("46.2e3"),'t'

    print a.isNumber(".e3"),'f'
    print a.isNumber('4e+'),'f'
    print a.isNumber(' '),'f'
    print a.isNumber('.'),'f'
    print a.isNumber('..'),'f'
    print a.isNumber('01'),'t'
    print a.isNumber('1234.435'),'t'
    print a.isNumber('+1234.435'),'t'
    print a.isNumber('1.3e11'),'t'
    print a.isNumber('01.3'),'t'
    print a.isNumber('1234.435  04324'),'f'
    print a.isNumber('1234.435e'),'f'
    print a.isNumber('1234.e11'),'t'
    print a.isNumber('1234.e+11'),'t'
    print a.isNumber('e'),'f'
    print a.isNumber('e1'),'f'
    print a.isNumber('1e2'),'t'

    print a.isNumber('+1.'),'t'
    print a.isNumber('1.2.3'),'f'
    print ' '

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        start=0
        while start<len(s) and s[start]==' ':
            start+=1
        if start==len(s):
            return False
        if s[start]=='+' or s[start]=='-':
            start+=1
        end=len(s)-1
        while end>=0 and s[end]==' ':
            end-=1
        s=s[start:end+1] 
        if len(s)==0:
            return False 
        sets=set(['0','1','2','3','4','5','6','7','8','9','e','.'])
        setsnum=set(['0','1','2','3','4','5','6','7','8','9','.'])
        counte=0
        countdot=0
        check=False
        i=0
        while i<len(s):
            if s[i] not in sets:
                return False
            
            if check and s[i] not in setsnum:
                return False
            if check and s[i]=='.':
                return False
#                 if i+1<len(s):
#                     return False
#                 if s[i-1]=='e':
#                     return False
            if s[i] =='e':
                if i-1==0 and s[i-1]=='.' :
                    return False
                counte+=1
                check=True
                if i+1<len(s) and (s[i+1]=='+' or s[i+1]=='-'):
                    i+=1
                    
            elif s[i]=='.':
                countdot+=1
            
            i+=1
            
        if counte>1 or countdot>1:
            return False 
        
#         if len(s)>1:
#             if s[0]=='0' and s[1]!='.':
#                 return False
        if len(s)==1:
            if s[0]=='.':
                return False
        if s[0]=='e' or s[-1]=='e'  :
            return False
        if s[-1]=='+' or s[-1]=='-':
            return False
        return True
    
if __name__=="__main__":
    a=Solution()
    print a.isNumber( " 4e3."),'f'
    print a.isNumber("1e."),'f'
    print a.isNumber('1e2.'),'f'
    print a.isNumber('1e2.1'),'f'
    print a.isNumber("46.e3"),'t'
    print a.isNumber("46.2e3"),'t'
    
    print a.isNumber(".e3"),'f'
    print a.isNumber('4e+'),'f'
    print a.isNumber(' '),'f'
    print a.isNumber('.'),'f'
    print a.isNumber('..'),'f'
    print a.isNumber('01'),'t'
    print a.isNumber('1234.435'),'t'
    print a.isNumber('+1234.435'),'t'
    print a.isNumber('1.3e11'),'t'
    print a.isNumber('01.3'),'t'
    print a.isNumber('1234.435  04324'),'f'
    print a.isNumber('1234.435e'),'f'
    print a.isNumber('1234.e11'),'t'
    print a.isNumber('1234.e+11'),'t'
    print a.isNumber('e'),'f'
    print a.isNumber('e1'),'f'
    print a.isNumber('1e2'),'t'
    
    print a.isNumber('+1.'),'t'
    print a.isNumber('1.2.3'),'f'