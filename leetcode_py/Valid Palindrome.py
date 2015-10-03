class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():  # str.isalnum(str(s[l])):
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == "__main__":
    a = Solution()
    print a.isPalindrome("a.")

class Solution:
    # 125
    # @param {string s}
    # @param {boolean}
    def isPalindrome(self, s):
        s = filter(str.isalnum, str(s)).lower()
        return s == s[::-1]

class Solution:
    def check(self,a):
        if a<='z' and a>='a':
            return True
        elif a<='Z' and a>='A':
            return True
        elif a<='9' and a>='0':
            return True
        else:
            return False
            
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s)<=1:
            return True
        f,b=0,len(s)-1
        while f<b:
            while f<len(s) and not self.check(s[f]):
                f+=1
            while b>=0 and not self.check(s[b]):
                b-=1
            if f<=b:
                if str.upper(s[f])==str.upper(s[b]):
                    f+=1
                    b-=1
                else:
                    return False
        return True
            
if __name__=="__main__":
    a=Solution()
    print a.isPalindrome(".,")

