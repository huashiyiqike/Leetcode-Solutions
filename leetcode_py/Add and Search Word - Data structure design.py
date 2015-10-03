# depth first
from collections import defaultdict
class  TrieNode:
    def __init__(self):
        self.end=False
        self.child=defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur=self.root
        for i in word:
            cur=cur.child[i]
        cur.end = True

    def searchs(self, word, start):
        if not word:
            return start.end
        tmp = start
        for idx, i in enumerate(word):
            if i == '.':
                for j in tmp.child:
                    if self.searchs(word[idx+1:], tmp.child[j]):
                        return True
                return False
            else:
                if i in tmp.child:
                    tmp = tmp.child[i]
                else:
                    return False
        return tmp.end

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchs(word, self.root)

# breadth first
from collections import defaultdict
class  TrieNode:
    def __init__(self):
        self.end=False
        self.child=defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur=self.root
        for i in word:
            cur=cur.child[i]
        cur.end = True
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        cur=[self.root]
        for i in word:
            next=[]
            for j in cur:
                if i=='.':
                    next.extend(j.child.values())
                else:
                    j=j.child.get(i)
                    if j!=None:
                        next.append(j)
            cur=next
        return any(tmp.end for tmp in cur)

from collections import defaultdict
class  TrieNode:
    def __init__(self):
        self.end=False
        self.child=defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        self.root=TrieNode()
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur=self.root
        for i in word:
            cur=cur.child[i]
        cur.end = True
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        cur=[self.root]
        for idx,item in enumerate(word):
            next=[]
            if item == '.':
                if len(cur)==1:
                    for i in cur[0].child:
                        next.append(cur[0].child[i])
                else:
                    for i in cur:
                        for j in i.child:
                            next.append(i.child[j])
            else:
                if len(cur)==1:
                    next=[cur[0].child.get(item)]
                    if next[0]==None:
                        return False
                else:
                    for i in cur:
                        tmp=i.child.get(item)
                        if tmp!=None:
                            next.append(tmp)
                    if len(next)==0:
                        return False
            cur=next

        if len(cur)==1:
            return cur[0].end
        else:
            for i in cur :
                if i.end:
                    return True
            return False