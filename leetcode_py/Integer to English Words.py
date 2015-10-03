class Solution(object):
    def three(self, num):
        res = ''
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if num > 99:
            res += ' ' + to19[num/100 - 1] + ' Hundred'
            num %= 100
        if num > 19:
            res += ' ' + tens[num/10 - 2]
            num %= 10

        if num:
            res += ' ' + to19[num - 1]
        return res


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        res = ''
        count = 0
        while num:
            tmp = num % 1000
            num /= 1000
            tmp = self.three(tmp)
            count += 1
            if count == 1:
                res = tmp + res
            elif count == 2:
                if tmp:
                    res = tmp + ' Thousand' + res
            elif count == 3:
                if tmp:
                    res = tmp + ' Million' + res
            elif count == 4:
                if tmp:
                    res = tmp + ' Billion' + res
        return res[1:]

    # recursive by Pochmann
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [to19[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join(words(num)) or 'Zero'

if __name__ == "__main__":
    a = Solution()
    print a.numberToWords(123)
    print a.numberToWords(0)
    print a.numberToWords(1000000)
    print a.numberToWords(100001)
    print a.numberToWords(1911111111)
