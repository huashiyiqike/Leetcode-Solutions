#might overflow
# class Solution:
#     # @return a boolean
#     def isPalindrome(self, x):
#         if x<0:
#             return False
#         num=0
#         copy=x
#         while x>0:
#             num=num*10+x%10
#             x/=10
#         return  num==copy

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        digits = -1
        while num:
            digits += 1
            num /= 10

        while x:
            if x / (10 ** digits) != x % 10:
                return False
            x %= 10 ** digits
            x /= 10
            digits -= 2
        return True


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:
            return False
        tmp=x
        count=-1
        while tmp:
            count+=1
            tmp/=10

        for i in range((count+1)/2):
            if x/10**count!=x%10:
                return False
            x/=10
            count-=1
            x-=(x/10**count)*10**count
            count-=1

        return True

if __name__=="__main__":
    a=Solution()
    print a.isPalindrome(1000021)
    print a.isPalindrome(0)
    print a.isPalindrome(121)
    print a.isPalindrome(123211)
    print a.isPalindrome(22)
    print a.isPalindrome(222)
    print a.isPalindrome(2147483648)
    print a.isPalindrome(-2147483648)
    


