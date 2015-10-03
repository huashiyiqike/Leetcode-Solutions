class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        a, b = map(int, num1), map(int, num2)
        res = [0] * (len(num1) + len(num2))
        for i in range(len(a)-1, -1, -1):
            for j in range(len(b)-1, -1, -1):
                res[i+j+1] += a[i] * b[j]
        carry = 0
        for i in range(len(a)+len(b)-1, -1, -1):
            res[i] += carry
            carry = res[i] / 10
            res[i] %= 10
        idx = 0
        while idx+1 < len(res):
            if res[idx] == 0:
                idx += 1
            else:
                break
        return ''.join(map(str, res[idx:]))
if __name__ == "__main__":
    a = Solution()
    print a.multiply("12", "12")

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        a=map(int,num1)[::-1]
        b=map(int,num2)[::-1]
        res=[0]*(len(a)+len(b)+1)
        for i in range(len(a)):
            for j in range(len(b)):
                res[i+j]+=a[i]*b[j]
                res[i+j+1]+=res[i+j]/10
                res[i+j]%=10
        for i in range(len(res)-1,-1,-1):
            if res[i]!=0:
                return "".join(map(str,res[:i+1][::-1]))
        return '0'

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        res=[0 for i in range(len(num1+num2)-1)]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j]+=int(num1[i])*int(num2[j])
        carry=0
        for i in reversed(range(len(res))):
            res[i]+=carry
            carry=res[i]/10
            res[i]=str(res[i]%10)
        print res
        if carry:
            res=[str(carry)]+res
        i=0
        while len(res) > 1 and res[0] == "0":
            del res[0]
        #print res
        return "".join(res)

if __name__=="__main__":
    a=Solution()
    print a.multiply('100','10000')
    print a.multiply('0','78')
    print a.multiply('1','3443')
    print a.multiply('1','1')
    print a.multiply('333','0')
