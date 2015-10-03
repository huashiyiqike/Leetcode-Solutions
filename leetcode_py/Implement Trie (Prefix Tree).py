from collections import defaultdict
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.nexts = defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for idx, i in enumerate(word):
            cur = cur.nexts[i]
        cur.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for idx, i in enumerate(word):
            if i in cur.nexts:
                cur = cur.nexts[i]
            else:
                return False
        return cur.end

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for idx, i in enumerate(prefix):
            if i in cur.nexts:
                cur = cur.nexts[i]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.end=False
        self.child=defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current=self.root 
        for i in word:
            current=current.child[i]
        current.end=True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current=self.root 
        for i in word:
            current=current.child.get(i)
            if current is None:
                return False
        return current.end

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current=self.root 
        for i in prefix:
            current=current.child.get(i)
            if current is None:
                return False
        return True


if __name__=="__main__":
    a=Trie()
    a.insert("app")
    a.insert("apple")
    a.insert("beer")
    a.insert("add")
    a.insert("jam")
    a.insert("rental")
    print a.search("apps")
    print a.search("app")
    print a.search("ad")
    print a.search("applepie")
    a.insert("something")
    print  a.search("something1")
    print  a.startsWith("something")
    #a.insert("som")
    print a.startsWith("som") 