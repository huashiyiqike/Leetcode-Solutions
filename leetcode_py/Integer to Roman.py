class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90,  50, 40,  10, 9,   5,  4,   1]
        res = ''
        while num:
            for idx, item in enumerate(value):
                if num/item != 0:
                    res += num/item * symbol[idx]
                    num %= item
        return res

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        value=[1000,900,500,400, 100, 90,  50, 40,  10, 9,   5,  4,   1]
        res=''
        while num>0:
            for idx,i in enumerate(value):
                while num/i>0:
                    res+=symbol[idx]
                    num-=i
        return res
