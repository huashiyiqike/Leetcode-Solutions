import sys

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        maxint = (1 << 31) - 1
        minint = - 1 << 31
        if divisor == 0:
            return maxint
        neg = False
        if dividend * divisor < 0:
            neg = True
        dividend, divisor = abs(dividend), abs(divisor)
        res, cur, minimum = 0, 1, divisor
        while dividend >= minimum:
            while (divisor << 1) <= dividend:
                divisor <<= 1
                cur <<= 1
            dividend -= divisor
            res += cur
            while divisor > dividend:
                divisor >>= 1   # cannot become minus
                cur >>= 1
        if neg:
            res = -res
        return max(minint, min(res, maxint))

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor==0:
            return (1<<31)-1
        elif dividend==0:
            return 0
        else:
            a=abs(dividend)
            b=abs(divisor)
            count=1
            res=0
            
            while b>0 and a>0:
                if a>=b :   
                    a-=b
                    res+=count
 
                if b<<1<=a:
                    b<<=1
                    count<<=1
                    
                elif  a<b:
                    count>>=1
                    b>>=1

            if dividend<0:
                res=0-res
            if divisor<0:
                res=0-res
            if res>=2147483648:
                return 2147483647
            return res
            
if __name__=='__main__':
    a=Solution()
    if len(sys.argv)==1:	
        print a.divide(-2147483648,1)
    else:
        print a.divide(int(sys.argv[1]),int(sys.argv[2]))
        

