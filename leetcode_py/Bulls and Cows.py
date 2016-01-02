from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        same = 0
        secret2 = defaultdict(int)
        guess2 = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                same += 1
            else:
                secret2[secret[i]] += 1
                guess2[guess[i]] += 1
        dif = 0
        for i in secret2.keys():
            if i in guess2:
                dif += min(secret2[i], guess2[i])
        return str(same) + 'A' + str(dif) + 'B'

if __name__ == "__main__":
    a = Solution()
    print a.getHint("1807", "7810")