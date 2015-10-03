
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        digits=[0 for i in range(32)]
        for i in A:
            for j in range(32):
                if i>>j&1:
                    #print j
                    digits[j]+=1
        res=0
        for i in range(32):
            res+=(digits[i]%2)<<i
        return self.convert(res)

    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        a,b,c=0,0,0
        for i in A:
            c=b&i
            b=b|(a&i)
            a=a|i
            b=b&(~c)
            a=a&(~c)
        return a

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        c1=c2=mask=0
        for i in A:
            c2^=(i&c1)
            c1^=i
            mask=~(c2&c1)
            c2&=mask
            c1&=mask
        return c1
