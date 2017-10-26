/**
 * @param {string[]} words
 * @return {number[][]}
 */
var palindromePairs = function(words) {
    
};

/*
https://discuss.leetcode.com/topic/46084/concise-python-solution
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        dic = {}
        for i in range(len(words)):
            dic[words[i]] = i
        for word in words:
            word_rev = word[::-1]
            if word_rev in dic and dic[word_rev] != dic[word]:
                res.append([dic[word_rev], dic[word]])
            for i in range(len(word)):
                temp1 = word[:i][::-1]
                temp2 = word_rev[:i]
                if temp1 in dic and isPal(word[i:]):
                    res.append([dic[word], dic[temp1]])
                if temp2 in dic and isPal(word_rev[i:]):
                    res.append([ dic[temp2], dic[word]])
        return res
def isPal(word):
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

    */