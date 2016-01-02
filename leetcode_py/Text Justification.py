import math


class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        res = []
        idx = 0
        while idx < len(words):
            cur = []
            lens = -1
            idx2 = idx
            last = False
            while idx2 < len(words) and lens + len(words[idx2]) + 1 <= maxWidth:
                if idx2 >= len(words) - 1:
                    last = True
                cur.append(words[idx2])
                lens += len(words[idx2]) + 1
                idx2 += 1

            if last:
                plus = [1] * len(cur) if len(cur[0]) > 0 else [1]
                plus[-1] -= 1
                while lens < maxWidth:
                    plus[-1] += 1
                    lens += 1
            else:
                plus = [1] * (len(cur) - 1) if len(cur) > 1 else [0]
                while lens < maxWidth:
                    for i in range(len(plus)):
                        plus[i] += 1
                        lens += 1
                        if lens == maxWidth:
                            break
            tmpres = ''
            for i in range(len(plus)):
                tmpres += cur[i] + ' ' * plus[i]
            if len(cur) > 1 and not last:
                tmpres += cur[-1]
            res.append(tmpres)
            if idx2 != idx:
                idx = idx2
            else:
                idx += 1

        return res


if __name__ == "__main__":
    a = Solution()
    print a.fullJustify(["Here", "is", "an", "example", "of", "text", "justification."], 15)
    print a.fullJustify(["What", "must", "be", "shall", "be."], 12)
    print a.fullJustify([''], 2)
    print a.fullJustify([''], 0)
    print a.fullJustify(['ab', 'cd', 'ef', 'g', 'hij'], 7)
    print a.fullJustify(['ab', 'cd', 'ef', 'g', 'hij'], 8)
    print a.fullJustify(['abc', 'cd', 'ef', 'g', 'hij'], 11)
    print a.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)
    print a.fullJustify([], 9)
    print ' '


class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        i = 0
        res = []
        while i < len(words):
            tmpres = words[i]
            j = i + 1
            count = len(words[i])
            while j < len(words) and count + len(words[j]) + 1 <= maxWidth:
                count += len(words[j]) + 1
                j += 1
            if j == i + 1:
                tmpres += " " * (maxWidth - len(words[i]))
            elif j == len(words):
                for k in range(i + 1, j):
                    tmpres += ' ' + words[k]
                tmpres += " " * (maxWidth - len(tmpres))
            else:
                surplus = maxWidth - count
                meansurplus = surplus / (j - i - 1)
                start = surplus - meansurplus * (j - i - 1)
                for k in range(i + 1, j):
                    if k - i - 1 < start:
                        tmpres += ' ' * (2 + meansurplus) + words[k]
                    else:
                        tmpres += ' ' * (1 + meansurplus) + words[k]
            res.append(tmpres)
            i = j
        return res


if __name__ == "__main__":
    a = Solution()
    print a.fullJustify(["Here", "is", "an", "example", "of", "text", "justification."], 15)
    print a.fullJustify(["What", "must", "be", "shall", "be."], 12)
    print a.fullJustify([''], 9)
    print a.fullJustify(['ab', 'cd', 'ef', 'g', 'hij'], 7)
    print a.fullJustify(['ab', 'cd', 'ef', 'g', 'hij'], 8)
    print a.fullJustify(['abc', 'cd', 'ef', 'g', 'hij'], 11)
    print a.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6)
    print a.fullJustify([], 9)

