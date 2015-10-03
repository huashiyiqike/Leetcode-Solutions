class Solution:
    # @return an integer
    def reverse(self, x):
        res=0
        flag=1
        if x<0:
            flag=-1
            x=-x
        while x:
            res*=10
            res+=x%10
            x/=10
            if res >= (1<<32)-1:
                return 0
                
        res*=flag
        return res
