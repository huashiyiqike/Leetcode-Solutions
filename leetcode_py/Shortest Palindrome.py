class Solution:
# @param {string} s
# @return {string}
    def shortestPalindrome(self, s):
        r=s[::-1];

        left=s[1:][::-1];
        middle= len(s)//2+1;
        while(middle>=0):
            if(r[len(s)-middle:]==s[middle+1:middle+1+middle]):
                left=s[middle+1+middle:][::-1];
                break;
            if(r[len(s)-middle:]==s[middle:middle+middle]):
                left=s[middle+middle:][::-1];
                break;
            middle-=1;

        return left+s;


if __name__=="__main__":
    a=Solution()
    print a.shortestPalindrome("aacecaaa")
    print a.shortestPalindrome('ababbbabbaba'),"ababbabbbababbbabbaba"
    print a.shortestPalindrome('ababbbabbaba') == "ababbabbbababbbabbaba"
    print len(a.shortestPalindrome('ababbbabbaba')), len("ababbabbbababbbabbaba")

    print a.shortestPalindrome('aaaa')
    print a.shortestPalindrome('baaa')
    print a.shortestPalindrome('aaa')
    print a.shortestPalindrome('abc')

    print a.shortestPalindrome("abbacd")
    print a.shortestPalindrome("ababbbabbaba")
    print a.shortestPalindrome('abc')
    print a.shortestPalindrome("aacecaaa")
    print a.shortestPalindrome('')
    print a.shortestPalindrome("abcd")

#TLE
# class Solution:
#     # @param {string} s
#     # @return {string}
#     def shortestPalindrome(self, s):
#         if len(s)<2:
#             return s
#         r=s[::-1]
#         res=2
#         for idx in range(2,len(s)+1):
#             if s[:idx]==r[-idx:]:
#                 res=idx+1
#
#         if res==len(s)+1:
#             return s
#         return s[res-1:][::-1]+s

#TLE
# class Solution:
#     # @param {string} s
#     # @return {string}
#     def shortestPalindrome(self, s):
#         if len(s)<2 or s==s[::-1]:
#             return s
#         end=len(s)-1
#         while end>0:
#             i,j=0,end
#             while i<=j:
#                 if s[i]!=s[j]:
#                     break
#                 else:
#                     i,j=i+1,j-1
#                 if i>=j:
#                     return s[end+1:][::-1]+s
#             end-=1
#         return  s[end+1:][::-1]+s
    
#TLE
# class Solution:
#     # @param {string} s
#     # @return {string}
#     def shortestPalindrome(self, s):
#         if len(s)<2:
#             return s
#         s2=s[::-1]
#         res=0
#         for start in range(len(s)-1,-1,-1):
#             if s[:start]==s2[len(s)-start:len(s)]:
#                 res=start
#                 break
#
#         return s[res:][::-1]+s
#             
# class Solution:
#     def shortestPalindrome(self, s):
#         r = s[::-1]
#         for i in range(len(s) + 1):
#             if s.startswith(r[i:]):
#                 return(r[:i] + s)     

class Solution:
# @param {string} s
# @return {string}
    def shortestPalindrome(self, s):
        A=s+"*"+s[::-1]
        cont=[0]
        for i in range(1,len(A)):
            index=cont[i-1]
            while(index>0 and A[index]!=A[i]):
                index=cont[index-1]
            cont.append(index+(1 if A[index]==A[i] else 0))
        return s[cont[-1]:][::-1]+s

# KMP now WA aabba
class Solution:
    def shortestPalindrome(self, s):
      #  r=s[::-1]
        r=s
        s=s+s[::-1]
        next=[0]
        k=0
        res=0
        for i in range(1,len(s)):
            while k>0 and s[i]!=s[k]:
                k=next[k-1]
            if s[i]==s[k]:
                k+=1
            next.append(k)
            res=max(res,k+1)

#         k=0
#         res=0
#         for i in range(len(r)):
#             while r[i]!=s[k] and k>0:
#                 k=next[k-1 ]
#
#             if r[i]==s[k]:
#                 k+=1
#             res=max(res,k)
#             if k==len(s):
#                 k=next[k-1]
        return r[next[-1]:][::-1]+r



    