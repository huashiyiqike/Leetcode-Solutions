class Solution:
    def nextPermutation(self, num):
        s=num
        for j in xrange(len(s)-2,-1,-1):
            for i in xrange(len(s)-1,j,-1):
                if s[i]>s[j]:
                    s[i],s[j]=s[j],s[i]
                    s[j+1:]=s[j+1:][::-1]
                    return
        num.sort()
        return

# class Solution:
#     def nextPermutation(self, num):
#         for j in range(len(num)-2,-1,-1):
#             for i in range(len(num)-1,j,-1):
#                 if num[i]>num[j]:
#                     num[i],num[j]=num[j],num[i]
#                     num[j+1:]=num[:j:-1]
#                     return
#         num.sort()
#         return

if __name__=="__main__":
    a=Solution()
    tmp=[4,2,0,2,3,2,0] #[1,3,2] #[0,8,1,3,1,1,0,3,4,0,3,9,1,9,6,9,3,3,8]
    for i in range(3):
        a.nextPermutation(tmp)
        print tmp
